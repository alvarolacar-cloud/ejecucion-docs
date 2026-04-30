# Paso 6 — Estructura de Contenido + LCAs · Outputs

Trazabilidad de outputs del Paso 6 — formato compacto de 4 columnas.

## Convención de columnas

- **ID y referencia canónica** — identificador único + referencia al §X del a-doc.
- **Viene de un output anterior** — `no` si nace en esta fila; `← X.YY` si deriva de un output anterior.
- **Output y ejemplo** — qué output produce el paso + valor concreto en el ejemplo Cerrajeros Madrid 24h.
- **Cómo se obtiene** — método de obtención del output + fuente del catálogo.

Fuentes posibles: `GMB Crush`, `Input humano`, `Decisión de diseño`, `Competidores`, `Datos de búsqueda`, `IA sin respaldo` (o combinadas con `+` cuando la doctrina dirige a otra fuente).

> **Nota terminológica:** Cada row representa un **output** del paso. Antes llamábamos a esto "decisiones"; ahora se llama **output** (mismo concepto, nombre actualizado). La columna "Output y ejemplo" describe qué genera el paso; la columna "Cómo se obtiene" describe el método y la fuente del catálogo.

---

## Bloque 1 — Main City y Local Coverage Areas

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **6.01** · Paso-06 §5; Paso-01 §11 | ← 1.20 | **Madrid crea la estructura principal** = `Madrid` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **6.02** · Paso-06 §8; Paso-01 §14 | ← 1.22, 1.23 | **Direct Local Coverage Areas refuercen el contenido** = `Almagro, Chamberí` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **6.03** · Paso-06 §8; Paso-01 §14 | ← 1.24–1.31 | **Candidate Local Coverage Areas puedan usarse si pasan test GEO** = `Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **6.04** · Paso-06 §8; Paso-02 §12 | no | **las Local Coverage Areas no sustituyan a Madrid** = `La página sigue siendo Madrid` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 2 — Uso por tipo de página

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **6.05** · Paso-06 §10 | no | **la Homepage pueda mencionar Local Coverage Areas de forma ligera** = `Almagro, Chamberí, etc.` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **6.06** · Paso-06 §11 | no | **Service Overview no use Local Coverage Areas** = `Sin zonas locales` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **6.07** · Paso-06 §12 | no | **LBS use Local Coverage Areas en intro, H2s y FAQs** = `Páginas servicio + Madrid` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **6.08** · Paso-06 §14 | no | **GeoHub use sección de cobertura local** = `/madrid/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **6.09** · Paso-06 §13 | no | **Additional Category use cobertura local como contexto** = `/cerrajero/madrid/duplicado-llaves/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **6.10** · Paso-06 §15 | no | **GeoArticles usen zonas como ejemplos locales** = `Madrid + zonas GEO` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 3 — Restricciones

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **6.11** · Paso-06 §8; Paso-04 §13; Paso-03 §9 | no | **una mención de zona no equivale a crear URL** = `Mencionar Almagro ≠ crear /almagro/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **6.12** · Paso-06 §9 | no | **No afirmar oficina física en cada Local Coverage Area** = `No oficina en Salamanca/Retiro salvo verdad` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **6.13** · Paso-06 §21; Paso-14 §20 | no | **`areaServed` pueda incluir cobertura real validada** = `Madrid + zonas validadas` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |