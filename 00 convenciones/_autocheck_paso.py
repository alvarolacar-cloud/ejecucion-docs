"""Autocheck para un paso del sistema GMB Crush.

Recibe path al a-doc del paso. Ejecuta:
1. Cross-refs internas: cada §X en body referencia un heading existente.
2. Lista Fuentes únicas para revisión manual de validez catálogo.
3. Cobertura outputs §5 ↔ §8: los IDs declarados en §5 (Outputs a Conseguir)
   coinciden con los IDs consolidados en §8 (Outputs Consolidados).

Nota terminológica: en este sistema "output" reemplaza a "decisión" — son sinónimos.
Cada row de §5/§8 es un output del paso.

Cambio v2: el b-doc se ha consolidado dentro de §8 del a-doc. Los checks de
cobertura b-doc ↔ a-doc se eliminaron — la trazabilidad ahora vive en un único
archivo por paso.
"""
import re
import sys
from pathlib import Path

VALID_FUENTES = {
    "GMB Crush",
    "Input humano",
    "Decisión de diseño",
    "Competidores",
    "Datos de búsqueda",
    "IA sin respaldo",
    "GMB Crush + Competidores",
    "GMB Crush + Datos de búsqueda",
    "GMB Crush + IA sin respaldo",
    "GMB Crush + Input humano",
}


def parse_headings(path: Path):
    """Returns set of heading IDs (§N or §N.M) present in the doc.

    Soporta DOS formatos:

    Formato A (legacy): ID dentro del heading line.
        ## §2 Objetivo del Paso 2

    Formato B (nuevo): ID en línea <small> después del heading.
        ## Objetivo del Paso 2
        <small>§2</small>

        ### Planned GBP Categories Before GBP Creation
        <small>§6.1 · ref. canónica 1</small>
    """
    headings = set()
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    inline_pattern = re.compile(r"^#{1,3} §(\d+)(?:\.(\d+))?\s")
    heading_any = re.compile(r"^#{1,3}\s+\S")
    small_id_pattern = re.compile(r"<small>\s*§(\d+)(?:\.(\d+))?\b")

    for i, line in enumerate(lines):
        # Formato A: §X dentro del heading
        m = inline_pattern.match(line)
        if m:
            num = m.group(1)
            sub = m.group(2)
            if sub:
                headings.add(f"§{num}.{sub}")
            headings.add(f"§{num}")
            continue

        # Formato B: heading sin §X, seguido de <small>§N</small>
        if heading_any.match(line):
            for j in range(i + 1, min(i + 4, len(lines))):
                if not lines[j].strip():
                    continue
                m2 = small_id_pattern.search(lines[j])
                if m2:
                    num = m2.group(1)
                    sub = m2.group(2)
                    if sub:
                        headings.add(f"§{num}.{sub}")
                    headings.add(f"§{num}")
                break  # solo primera línea no vacía
    return headings


def parse_internal_refs(path: Path, own_paso_id: str):
    """Find §X refs in body (excluding heading lines, excluding heading metadata
    <small>§N</small> lines, y excluding 'Paso-NN §X' external refs)."""
    text = path.read_text(encoding="utf-8")
    refs = set()
    heading_pattern = re.compile(r"^#{1,3} §\d+")  # legacy heading format
    heading_metadata = re.compile(r"^<small>\s*§\d+")  # new format heading meta
    paso_prefix_pattern = re.compile(r"[Pp]aso[\- ]?\d{1,2}[\- ]+§(\d+)(?:\.(\d+))?")
    ref_pattern = re.compile(r"§(\d+)(?:\.(\d+))?")

    for line in text.split("\n"):
        if heading_pattern.match(line):
            continue
        if heading_metadata.match(line):
            continue  # skip new-format heading metadata
        # Mark spans that are inside "Paso-NN §X" so we skip those
        external_spans = []
        for m in paso_prefix_pattern.finditer(line):
            external_spans.append((m.start(), m.end()))
        for m in ref_pattern.finditer(line):
            # Skip if this match is inside an external span
            inside_external = any(start <= m.start() < end for start, end in external_spans)
            if inside_external:
                continue
            num = m.group(1)
            sub = m.group(2)
            if sub:
                refs.add(f"§{num}.{sub}")
            else:
                refs.add(f"§{num}")
    return refs


def parse_fuentes(path: Path):
    """Extract Fuente declarations from a-doc.

    Strips trailing annotations like '← heredado del Paso N §M' which are
    documentation aids, not part of the Fuente value.
    """
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(r"\*\*Fuente:\*\*\s*([^.\n]+)")
    fuentes = []
    for m in pattern.finditer(text):
        raw = m.group(1).strip().rstrip(".")
        # Strip trailing arrow annotations
        for arrow in ["←", "<-", "<--"]:
            if arrow in raw:
                raw = raw.split(arrow)[0].strip()
        fuentes.append(raw)
    return fuentes


def parse_section_output_ids(path: Path, section_num: int):
    """Extract output IDs (e.g. '5.1', '5.2') from a specific section.

    Locates the heading whose <small> tag contains §<section_num>, then reads
    until the next ## heading and extracts all `N.M` IDs that appear at the
    start of table rows (after a `|` pipe).
    """
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    section_marker = f"§{section_num}"
    section_marker_dotted = f"§{section_num}."

    # Find the section heading (look for <small>§N</small> line)
    in_section = False
    section_lines = []
    section_start_pattern = re.compile(
        rf"^<small>\s*§{section_num}(?!\.\d)\b"
    )

    i = 0
    while i < len(lines):
        line = lines[i]
        # Detect entering target section: <small>§N</small> right after a ## heading
        if section_start_pattern.match(line.strip()):
            in_section = True
            i += 1
            continue
        if in_section:
            # Stop when we hit the next ## heading (top-level)
            if line.startswith("## ") or line.startswith("# "):
                break
            section_lines.append(line)
        i += 1

    # Extract IDs from table rows: lines starting with | <ID> | ...
    ids = set()
    row_pattern = re.compile(r"^\|\s*(\d+\.\d+)\s*\|")
    for line in section_lines:
        m = row_pattern.match(line.strip())
        if m:
            ids.add(m.group(1))
    return ids


def main():
    if len(sys.argv) < 3:
        print("Usage: _autocheck_paso.py <a-doc> <paso-id>")
        print("Example: _autocheck_paso.py 01a.md Paso-01")
        sys.exit(1)
    a_path = Path(sys.argv[1])
    paso_id = sys.argv[2]

    print(f"=== Autocheck {paso_id} ===\n")

    # Check 1: Internal refs
    headings = parse_headings(a_path)
    internal_refs = parse_internal_refs(a_path, paso_id)
    broken_refs = internal_refs - headings
    print(f"[1] Internal refs en a-doc")
    print(f"    Total refs en body: {len(internal_refs)}")
    print(f"    Total headings:     {len(headings)}")
    if broken_refs:
        print(f"    BROKEN ({len(broken_refs)}): {sorted(broken_refs, key=lambda x: tuple(int(p) for p in x.lstrip('§').split('.')))}")
    else:
        print(f"    Todas las refs resuelven. OK")
    print()

    # Check 2: Fuentes validation
    fuentes = parse_fuentes(a_path)
    print(f"[2] Fuentes declaradas en a-doc")
    invalid_fuentes = [f for f in fuentes if f not in VALID_FUENTES]
    print(f"    Total: {len(fuentes)}")
    if invalid_fuentes:
        print(f"    INVALID:")
        for f in invalid_fuentes:
            # Use ASCII-safe representation
            safe = f.encode("ascii", errors="replace").decode("ascii")
            print(f"      - {safe!r}")
    else:
        print(f"    Todas válidas según catálogo. OK")
    print()

    # Check 3: Cobertura §5 (declaración) ↔ §8 (consolidación)
    ids_section_5 = parse_section_output_ids(a_path, 5)
    ids_section_8 = parse_section_output_ids(a_path, 8)
    only_in_5 = ids_section_5 - ids_section_8
    only_in_8 = ids_section_8 - ids_section_5

    print(f"[3] Cobertura §5 (declaracion) <-> §8 (consolidacion)")
    print(f"    IDs declarados en §5: {len(ids_section_5)}")
    print(f"    IDs en §8:            {len(ids_section_8)}")
    if only_in_5 or only_in_8:
        if only_in_5:
            ordered = sorted(only_in_5, key=lambda x: tuple(int(p) for p in x.split(".")))
            print(f"    SOLO en §5 (faltan en §8): {ordered}")
        if only_in_8:
            ordered = sorted(only_in_8, key=lambda x: tuple(int(p) for p in x.split(".")))
            print(f"    SOLO en §8 (faltan en §5): {ordered}")
    else:
        print(f"    §5 y §8 cubren los mismos IDs. OK")
    print()

    # Summary
    issues = (
        len(broken_refs)
        + len(invalid_fuentes)
        + len(only_in_5)
        + len(only_in_8)
    )
    print(f"=== {issues} issues encontrados ===")
    return 0 if issues == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
