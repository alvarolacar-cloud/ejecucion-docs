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
│                          (ID / Nombre / Tipo / Origen)       │
│                                                              │
│ §6 Reglas que Aplican → X sub-secciones, UNA POR OUTPUT      │
│                          Cada sub-sección explica:           │
│                            • qué es ese output               │
│                            • cómo se obtiene                 │
│                            • ejemplos correctos              │
│                            • ejemplos incorrectos            │
│                            • la regla operativa final        │
│                                                              │
│ §7 Checklist Final → lista de ☐ que validar antes de cerrar  │
│                                                              │
│ §8 Outputs Consolidados → tabla final con VALOR concreto     │
│                            de cada output para Cerrajeros    │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Bloque IV — Fuentes Internas GMB Crush                       │
│ ──────────────────────────────────────                       │
│ Lista de frameworks GMB Crush en los que se basa el paso     │
└──────────────────────────────────────────────────────────────┘
```

---

## El truco mental: los outputs aparecen 3 veces

Cada output del paso aparece en tres sitios distintos del a-doc, con el mismo ID `N.X`:

1. **En §5** — listado en una tabla (ficha técnica: tipo, origen)
2. **En §4 (Bloque II)** — con su valor concreto para Cerrajeros
3. **En §6** — explicado con prosa, fórmula, ejemplos correctos/incorrectos, regla

Son tres vistas del mismo conjunto de outputs. Por eso hay que mantener los **mismos IDs** (`N.1`, `N.2`, ..., `N.X`) en los tres sitios.

---

## Cómo se nombra cada cosa

| Elemento | Formato |
|---|---|
| Título del doc | `# Paso N — [Título]` |
| Sección top-level | `## [Nombre]` con `<small>§N</small>` debajo |
| Sub-sección | `### [Nombre]` con `<small>§N.M</small>` debajo |
| ID de output | `N.X` (ej. `2.7` = output 7 del Paso 2) |
| Cross-ref interna | `§6.5` (mismo doc) |
| Cross-ref externa | `Paso-NN §X` (otro paso) |

**El §X siempre va debajo del título en `<small>`, NUNCA dentro del título.**

---

## Reglas mínimas

1. Solo 4 bloques (I / II / III / IV). No añadir más sin discusión.
2. Un §X = una sección. Numeración fija: §2 Objetivo, §3 Heredados, §4 Ejemplo, §5 Outputs a Conseguir, §6 Reglas, §7 Checklist, §8 Outputs Consolidados, §9 Fuentes.
3. **§4, §5, §6 y §8 tienen los mismos X outputs con los mismos IDs `N.1`–`N.X`**. Si añades un output, lo añades en los 4 sitios.
4. Cada §6.X explica un solo output (mapeo 1:1).
5. Fuentes solo del catálogo (ver abajo). Combinaciones inventadas no se permiten.

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
2. Que las refs del b-doc al a-doc resuelven
3. Cuántas rows tiene el b-doc
4. Que las Fuentes están en el catálogo
5. Que los outputs declarados en §5 tienen rows en el b-doc

Comando:

```bash
python _autocheck_paso.py <a-doc>.md <b-doc>.md Paso-NN
```
