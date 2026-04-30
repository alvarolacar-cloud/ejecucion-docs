Versión literal del chat · Sistema GMB Crush para webs locales
Esqueleto canónico para a-docs (`NNa-ejecucion-*.md`).
Proveniencia: extraído de `02a-ejecucion-formula-maestra-arquitectura.md` (commit c27c56c) tras iteración con el usuario.

# Esqueleto canónico — a-doc del Paso N

Este documento define la estructura que TODOS los a-docs (`01a`, `02a`, …, `19a`) deben seguir. Reemplazar cada `[placeholder]` con el contenido real del paso. NO eliminar la estructura ni renombrar los bloques.

---

## Convenciones de formato

### Headings

```markdown
# Paso N — [Título del Paso]
<small>§1</small>

# Bloque N — [Nombre del Bloque]

## [Nombre de la sección]
<small>§N</small>

### [Nombre de la sub-sección]
<small>§N.M</small>
```

- El número `§X` SIEMPRE va en `<small>` debajo del heading, NUNCA dentro del título
- El título se queda con el nombre puro, sin `§X` prefijo
- Aplica a todos los niveles (`#`, `##`, `###`)

### IDs de outputs

- Cada output tiene un ID global `N.X` donde `N` es el número del paso y `X` es el índice secuencial del output
- Ejemplo: outputs del Paso 2 son `2.1`, `2.2`, …, `2.15`
- Outputs del Paso 7 son `7.1`, `7.2`, …, `7.X`
- Los IDs son citables desde cualquier doc del sistema como `Paso-NN N.X`

### Cross-refs

- Refs internas (mismo paso): `§N` o `§N.M` directamente
- Refs externas (otro paso): `Paso-NN §X` o `Paso NN §X` con prefijo explícito
- Refs a outputs: `Paso-NN N.X` (ej. `Paso-02 2.7` para Variable A)

### Fuentes válidas (catálogo)

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

## Estructura completa del documento

```markdown
Versión literal del chat · Sistema GMB Crush para webs locales
[Línea 2 de proveniencia]
[Línea 3 de proveniencia]

# Paso N — [Título del Paso]
<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los X outputs del Paso N con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, reglas que aplican, checklist final y outputs consolidados.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso N
<small>§2</small>

[Resumen de 1-2 líneas de qué hace el paso. Debe responder: ¿qué calcula/produce? ¿con qué inputs? ¿para qué se usa después?]

**Outputs del paso:**

- **N.1** [Nombre del output] — [descripción de 1 línea]
- **N.2** [Nombre del output] — [descripción de 1 línea]
- **N.3** [Nombre del output] — [descripción de 1 línea]
- … (un bullet por cada output del paso)
- **N.X** [Último output] — [descripción]

**Errores que previene:**

- [Error 1 que evita ejecutar este paso correctamente]
- [Error 2]
- [Error 3]
- … (5-7 errores típicos)

**Cuándo se ejecuta:** [Posición en la secuencia. Después de qué paso, antes de qué paso. Por qué en ese orden.]

## Info heredada de pasos anteriores
<small>§3</small>

> Estos campos NO se deciden en Paso N — la IA los lee del paso indicado y los usa como input para producir los outputs del Bloque III.

| Campo | Origen |
|---|---|
| [Campo heredado 1] | Paso N-k §M |
| [Campo heredado 2] | Paso N-k §M |
| … | … |
| [Campo heredado X] | Paso N-k §M |

> [Nota opcional: si el paso es origen (Paso 1), reemplazar título de §3 por "Lo que la IA tiene que rellenar/obtener" y la tabla por la spec del intake.]

# Bloque II — Ejemplo rellenado para el Paso N — [Título del Paso]

<small>§4</small>

> Los X outputs del Paso N con sus valores reales para Cerrajeros Madrid 24h.

### N.1 — [Nombre del output 1]

[Valor concreto, tabla, código, o lo que mejor represente el output. Sin explicación de qué es — la explicación va en §6.1]

### N.2 — [Nombre del output 2]

[Valor concreto]

### N.3 — [Nombre del output 3]

[Valor concreto]

… (una sub-sección por cada output, en orden)

### N.X — [Nombre del último output]

[Valor concreto]

# Bloque III — Ejecución por la IA

## Outputs a Conseguir
<small>§5</small>

> Tabla declarativa de los X outputs que el Paso N debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `N.1`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Origen |
|---|---|---|---|
| N.1 | [Nombre output 1] | [Tipo: Status/String/Entero/Boolean/Fórmula/Validation flag/Tabla/etc.] | [Fuente del catálogo + ref al paso heredado si aplica] |
| N.2 | [Nombre output 2] | [Tipo] | [Origen] |
| … | … | … | … |
| N.X | [Nombre último] | [Tipo] | [Origen] |

## Reglas que Aplican
<small>§6</small>

> Esta sección desarrolla cada uno de los X outputs (N.1–N.X) con el mismo patrón: Explicación / Patrón o fórmula / Ejemplos correctos / Ejemplos incorrectos / Regla final / Validación operativa / Cómo se obtiene / Output del paso. Cada sub-sección §6.X corresponde 1:1 al output N.X declarado en §5.

### N.1 — [Nombre output 1]
<small>§6.1</small>

**Explicación**

[Prosa de 2-4 líneas explicando QUÉ es este output, POR QUÉ existe, y CÓMO se relaciona con otros outputs del paso. Lenguaje accesible para humanos no técnicos.]

**Patrón o fórmula**

```text
[Fórmula matemática, transformación o estructura que define el output. Ejemplo:
output_X = funcion(input_A, input_B)
o
estructura: prefijo + variable + sufijo]
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
[Caso real con valores concretos. Mostrar el output completo, paso a paso si hace falta.]
```

**Ejemplos incorrectos**

```text
- [Anti-patrón 1: error típico]
- [Anti-patrón 2: error típico]
- [Anti-patrón 3]
- [Más anti-patrones según sea relevante]
```

**Regla final**

```text
[Regla operativa en 1-2 frases. La esencia que la IA y el humano deben recordar.]
```

**Validación operativa**

[Prosa de 1-3 líneas explicando cómo validar que el output está correcto. Cross-refs a otros §6.X si la validación involucra otros outputs.]

**Cómo se obtiene**

- **Fuente:** [Una de las 10 fuentes válidas del catálogo. Si es heredada: `GMB Crush ← heredado del Paso N-k §M [Nombre del campo]`]
- **Método:** [Pasos concretos para producir el output a partir de la fuente. Mencionar herramientas, validaciones, decisiones intermedias.]

**Output del paso**

- **Tipo:** [Tipo concreto del output. Ej: `String — URL canónica única`, `Entero — número de servicios`, `Boolean (Yes/No) + lista de exclusiones`, `Validation flag — N condiciones cumplidas`]
- **Ejemplo (Cerrajeros Madrid 24h):** [Valor concreto del output para Cerrajeros, idéntico al que aparece en §4 Bloque II]

### N.2 — [Nombre output 2]
<small>§6.2</small>

[Misma estructura que §6.1 — Explicación / Patrón / Ejemplo correcto / Ejemplos incorrectos / Regla final / Validación operativa / Cómo se obtiene / Output del paso]

### N.3 — [Nombre output 3]
<small>§6.3</small>

[Misma estructura]

… (una sub-sección §6.X por cada output, 1:1 con la tabla §5 y con las sub-secciones de §4)

### N.X — [Nombre último output]
<small>§6.X</small>

[Misma estructura]

## Checklist Final
<small>§7</small>

> Validación operativa antes de cerrar el Paso N y avanzar al Paso N+1. Cada ☐ es un check que debe pasar antes del handoff.

### Validación de outputs

- ☐ [Check 1: confirma que un output está bien calculado/derivado]
- ☐ [Check 2]
- ☐ [Check 3]
- ☐ [Check 4]
- ☐ [Check 5]

### Validación de reglas

- ☐ [Check 1: confirma que una regla operativa se respeta]
- ☐ [Check 2]
- ☐ [Check 3]
- ☐ [Check 4]
- ☐ [Check 5]

### Validación de auditabilidad

- ☐ [Check 1: confirma que el resultado del paso es auditable componente a componente]
- ☐ [Check 2]
- ☐ [Check 3]

> [Las categorías de checks pueden adaptarse al paso. Mínimo: una categoría que cubra los outputs, una los principios/reglas operativas, una la auditabilidad/handoff.]

## Outputs Consolidados
<small>§8</small>

> Tabla final con valores reales para Cerrajeros Madrid 24h y status de cada output. Los IDs (`N.1`–`N.X`) coinciden con los declarados en §5.

| ID | Output | Valor (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|
| N.1 | [Nombre output 1] | [Valor concreto] | confirmed |
| N.2 | [Nombre output 2] | [Valor concreto] | confirmed |
| … | … | … | … |
| N.X | [Nombre último] | [Valor concreto] | confirmed/OK |

> Status valores típicos: `confirmed` (output cerrado y validado), `OK` (validation flag superada), `⚠ inferido` (output derivado por inferencia, requiere validación manual), `⚠ placeholder` (output pendiente de input real).

# Bloque IV — Fuentes Internas GMB Crush usadas

## Fuentes internas GMB Crush usadas
<small>§9</small>

- [Framework GMB Crush 1]
- [Framework GMB Crush 2]
- [Framework GMB Crush 3]
- … (frameworks oficiales de los que se deriva el paso)

> [Sub-sección §9.1 opcional para listas auxiliares específicas del paso, ej. GeoArticles concretos, etc.]
```

---

## Reglas inviolables

1. **Estructura de 4 bloques**: I (Introducción) / II (Ejemplo rellenado) / III (Ejecución por la IA) / IV (Fuentes). NO añadir bloques nuevos sin discusión.
2. **Numeración top-level §1–§9**: §1 título, §2 Objetivo, §3 Heredados, §4 Ejemplo, §5 Outputs a Conseguir, §6 Reglas, §7 Checklist, §8 Outputs Consolidados, §9 Fuentes.
3. **§6 mapeo 1:1 con outputs**: si hay X outputs, hay X sub-secciones §6.1–§6.X. Sin excepciones.
4. **§4 sub-secciones individuales**: una `### N.X — [Nombre]` por cada output, NO agrupar.
5. **§5 tabla declarativa**: los X outputs listados con `# / Output / Tipo / Origen`. NO incluir valores aquí.
6. **§8 tabla con valores**: los X outputs con `# / Output / Valor / Status`. SÍ incluir valores y status.
7. **§7 con `☐` checkbox**: por categoría (outputs / reglas / auditabilidad). NO usar tabla.
8. **Headings sin §X**: el §X siempre debajo en `<small>`. NUNCA dentro del título.
9. **Outputs numerados N.X**: el ID global SIEMPRE empieza por el número del paso (1.1 para Paso 1, 2.1 para Paso 2, etc.).
10. **Fuentes solo del catálogo**: ninguna combinación inventada. Solo las 10 válidas listadas arriba.

---

## Apéndices opcionales

Si el paso requiere contenido específico no cubierto por la estructura base (ej. módulo doctrinal de Paso 1, page types específicos de Paso 5), se puede añadir como:

- **Bloque V (o posterior)** después del Bloque III pero antes del Bloque IV (Fuentes)
- Documentar en el callout "Cómo leer este documento" del top
- Mantener convenciones de headings, refs y outputs

Ejemplo de paso con apéndice:

```markdown
# Bloque I — Introducción
# Bloque II — Ejemplo rellenado
# Bloque III — Ejecución por la IA
# Bloque IV — [Apéndice específico del paso, ej. Módulo doctrinal]
# Bloque V — Fuentes Internas GMB Crush usadas
```

---

## Autocheck

Cada a-doc debe pasar autocheck (`_autocheck_paso.py`):

- **Check 1**: refs internas resuelven a headings existentes
- **Check 2**: refs en b-doc apuntan a §X válidos en a-doc
- **Check 3**: row count del b-doc se reporta
- **Check 4**: Fuentes en a-doc son del catálogo válido
- **Check 5**: outputs declarados en a-doc tienen rows en b-doc

Comando:

```bash
python _autocheck_paso.py <a-doc>.md <b-doc>.md Paso-NN
```
