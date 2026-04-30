Versión literal del chat · Sistema GMB Crush para webs locales
Esqueleto canónico para a-docs (`NNa-ejecucion-*.md`).
Proveniencia: extraído de `02a-ejecucion-formula-maestra-arquitectura.md` (commit c27c56c).

# Esqueleto de un a-doc

Cada a-doc tiene **4 bloques**. Solo 4.

---

## Vista general

```
┌──────────────────────────────────────────────────────────────┐
│ Bloque I — Introducción                                      │
│ ─────────────────────────                                    │
│ • Objetivo: qué hace este paso, lista de outputs, errores    │
│ • Info heredada: qué inputs vienen de pasos anteriores       │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Bloque II — Ejemplo rellenado                                │
│ ──────────────────────────────                               │
│ Una sección corta por cada output con su valor concreto:     │
│   N.1 — [Output 1]: [valor para Cerrajeros]                  │
│   N.2 — [Output 2]: [valor para Cerrajeros]                  │
│   N.3 — [Output 3]: [valor para Cerrajeros]                  │
│   ... (X sub-secciones, una por output)                      │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Bloque III — Ejecución por la IA                             │
│ ─────────────────────────────────                            │
│ §5 Outputs a Conseguir → tabla con los X outputs             │
│                          (ID / Output / Tipo / Fuente /      │
│                           Hereda de)                         │
│                                                              │
│ §6 Obtención de Outputs → X sub-secciones, UNA POR OUTPUT    │
│                            Cada sub-sección explica:         │
│                            • qué es ese output               │
│                            • cómo se obtiene                 │
│                            • ejemplos correctos              │
│                            • ejemplos incorrectos            │
│                            • la regla operativa final        │
│                                                              │
│ §7 Checklist Final → lista de ☐ que validar antes de cerrar  │
│                                                              │
│ §8 Outputs Consolidados → tabla compacta row-per-output con  │
│                            ID / Hereda de / Output y valor / │
│                            Cómo se obtiene + Fuente / Status │
│                            (absorbe lo que antes estaba en   │
│                            el b-doc — fuente única de verdad)│
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Bloque IV — Fuentes Internas GMB Crush                       │
│ ──────────────────────────────────────                       │
│ Lista de frameworks GMB Crush en los que se basa el paso     │
└──────────────────────────────────────────────────────────────┘
```

---

## El truco mental: los outputs aparecen 4 veces

Cada output del paso aparece en cuatro sitios distintos del a-doc, con el mismo ID `N.X`:

1. **En §4 (Bloque II)** — con su valor concreto para Cerrajeros (en prosa o tabla)
2. **En §5 Outputs a Conseguir** — listado en tabla declarativa (ficha técnica: ID / Output / Tipo / Fuente / Hereda de)
3. **En §6 Obtención de Outputs** — explicado con prosa, fórmula, ejemplos correctos/incorrectos, regla, validación, fuente, método
4. **En §8 Outputs Consolidados** — tabla compacta row-per-output (ID / Hereda de / Output y valor / Cómo se obtiene + Fuente / Status)

Son cuatro vistas del mismo conjunto de outputs. Por eso hay que mantener los **mismos IDs** (`N.1`, `N.2`, ..., `N.X`) en los cuatro sitios.

> **Nota:** §8 absorbe lo que antes vivía en un b-doc separado. La consolidación tabular y el a-doc viven en el mismo archivo — sin drift entre docs, sin cross-refs cruzados, una única fuente de verdad por paso.

---

## Cómo se nombra cada cosa

| Elemento | Formato |
|---|---|
| Título del doc | `# Paso N — [Título]` |
| Sección top-level | `## [Nombre]` con `<small>§N</small>` debajo |
| Sub-sección | `### [Nombre]` con `<small>§N.M</small>` debajo |
| ID de output | `N.X` (ej. `2.7` = output 7 del Paso 2) |
| Cross-ref interna | `§6.5` (mismo doc, refiere a sub-sección) |
| Cross-ref externa | `Paso-NN N.X` (otro paso, refiere a output ID, NO a sección) |

**El §X siempre va debajo del título en `<small>`, NUNCA dentro del título.**

**Cross-refs externas siempre por Output ID** (`Paso-NN N.X`), no por sección (`Paso N §X`). Esto hace las refs robustas frente a futuros cambios de numeración interna.

---

## Tabla §5 Outputs a Conseguir — formato exacto

```markdown
| ID  | Output           | Tipo                  | Fuente                  | Hereda de       |
|-----|------------------|-----------------------|-------------------------|-----------------|
| N.1 | [Nombre output]  | [String/Entero/etc.]  | GMB Crush               | Paso-(N-1) X.Y  |
| N.2 | [Nombre output]  | [Tipo]                | Decisión de diseño      | —               |
| N.3 | [Nombre output]  | [Tipo]                | GMB Crush + Input humano| —               |
```

- **Fuente** = una de las 10 del catálogo (ver abajo). Indica de DÓNDE sale el output (doctrina / cliente / diseño / etc.)
- **Hereda de** = output ID del paso anterior cuyo valor se usa. Si es output nuevo (no hereda), poner `—`.

---

## Outputs compuestos — Formato A vs Formato B

Cuando un output contiene múltiples valores (ej. lista de slugs, NAP con 8 campos), tienes **dos formatos posibles**:

### Formato A — Una fila, valores agregados (default)

```markdown
| 2.4 | Service Slugs (S=5) | URL-safe strings | GMB Crush | Paso-01 1.9 |
```

Y en §8 Outputs Consolidados (formato compacto):

```markdown
| 2.4 | ← 1.9 | **Service Slugs (5)** = `cerrajero-urgente, apertura-puertas, cambio-cerraduras, cambio-bombines, instalacion-cerraduras-seguridad` | Generados con la fórmula de Paso-02 §6.4. **Fuente:** GMB Crush. | confirmed |
```

**Usar cuando:** los N valores son del mismo tipo, mismo status, sin sub-categorización. La IA lee "es una lista de N elementos" sin ambigüedad.

### Formato B — Multi-fila con MISMO ID (sub-categorización)

```markdown
| 1.10 | Direct LCAs (proximidad NAP) | Lista | GMB Crush | Paso-01 1.4 (NAP) |
| 1.10 | Candidate LCAs (validables con test GEO) | Lista | GMB Crush + Competidores | — |
```

Y en §8 Outputs Consolidados (formato compacto):

```markdown
| 1.10 | ← 1.4 | **Direct LCAs** = `Almagro, Chamberí` | Calculadas por proximidad NAP (Paso-01 §6.10). **Fuente:** GMB Crush. | confirmed |
| 1.10 | — | **Candidate LCAs** = `Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad` | Validadas con test GEO (Paso-01 §6.10). **Fuente:** GMB Crush + Competidores. | confirmed |
```

**Usar cuando:**
- Hay sub-categorías semánticamente distintas (ej. NAP tiene 8 campos: Name, Street, City, etc.)
- Cada sub-categoría tiene metadata propia (Fuente distinta, Status distinto, Hereda de distinto)
- Aporta legibilidad significativa vs lista comma-separated

### Cuándo NO usar ni A ni B — Tabla aparte

Para outputs con 10+ valores (URL Matrix, GeoArticle Topics), se usa una **tabla detallada en §4 Bloque II Ejemplo** con su propio formato (columns específicas del output). El §8 Outputs Consolidados solo muestra un resumen y referencia esa tabla.

### Decisión rápida

```
¿Tu output tiene...

  Un solo valor escalar?
  → Formato A, valor literal en §8

  2-5 valores cortos del mismo tipo?
  → Formato A, comma-separated

  2-5 valores con sub-categorías o metadata distinta?
  → Formato B (multi-fila mismo ID)

  6+ campos distintos como un NAP?
  → Formato B (multi-fila mismo ID)

  10+ valores estructurados (URLs, topics)?
  → Tabla aparte en §4, §8 referencia el resumen
```

---

## Reglas mínimas

1. Solo 4 bloques (I / II / III / IV). No añadir más sin discusión.
2. Un §X = una sección. Numeración fija: §2 Objetivo, §3 Heredados, §4 Ejemplo, §5 Outputs a Conseguir, §6 **Obtención de Outputs**, §7 Checklist, §8 Outputs Consolidados, §9 Fuentes.
3. **§4, §5, §6 y §8 tienen los mismos X outputs con los mismos IDs `N.1`–`N.X`**. Si añades un output, lo añades en los 4 sitios.
4. Cada §6.X explica un solo output (mapeo 1:1).
5. Fuentes solo del catálogo (ver abajo). Combinaciones inventadas no se permiten.
6. **Cross-refs cross-paso por Output ID** (`Paso-NN N.X`), no por sección.
7. **§5 tabla con 5 columnas** (ID / Output / Tipo / Fuente / Hereda de), no 4.
8. **§8 tabla con 5 columnas** (ID / Hereda de / Output y valor / Cómo se obtiene + Fuente / Status). Es la fuente única de la trazabilidad consolidada — sustituye al b-doc.

---

## Catálogo de Fuentes

Solo se permiten estas 10 fuentes (o combinaciones marcadas con `+`):

```
GMB Crush
Input humano
Decisión de diseño
Competidores
Datos de búsqueda
IA sin respaldo
GMB Crush + Competidores
GMB Crush + Datos de búsqueda
GMB Crush + IA sin respaldo
GMB Crush + Input humano
```

---

## Si el paso necesita algo extra

Algunos pasos tienen contenido específico que no encaja en los 4 bloques estándar (ej. el módulo doctrinal de zonas GEO en Paso 1, los 6 page types específicos del Paso 5).

En esos casos, se añade un **bloque extra** entre Bloque III y Bloque IV:

```
Bloque I — Introducción
Bloque II — Ejemplo rellenado
Bloque III — Ejecución por la IA
Bloque IV — [Apéndice específico del paso]   ← extra
Bloque V — Fuentes Internas GMB Crush usadas
```

Y se documenta el bloque extra en el callout "Cómo leer este documento" del top.

---

## Validación automática

El autocheck (`_autocheck_paso.py`) verifica:

1. Que las cross-refs internas resuelven (no hay §X rotos)
2. Que las Fuentes están en el catálogo
3. Que §5 (declaración) y §8 (consolidación) tienen los mismos IDs de outputs

> **Nota:** los checks de "refs b-doc → a-doc" y "cobertura outputs ↔ rows" se eliminaron al consolidar el b-doc dentro del a-doc. La trazabilidad ahora vive en §8 del propio a-doc.

Comando:

```bash
python _autocheck_paso.py <a-doc>.md Paso-NN
```
