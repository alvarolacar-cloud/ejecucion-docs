# Paso 7 — Internal Linking Rules · Outputs

Trazabilidad de outputs del Paso 7 — formato compacto de 4 columnas.

## Convención de columnas

- **ID y referencia canónica** — identificador único + referencia al §X del a-doc.
- **Viene de un output anterior** — `no` si nace en esta fila; `← X.YY` si deriva de un output anterior.
- **Output y ejemplo** — qué output produce el paso + valor concreto en el ejemplo Cerrajeros Madrid 24h.
- **Cómo se obtiene** — método de obtención del output + fuente del catálogo.

Fuentes posibles: `GMB Crush`, `Input humano`, `Decisión de diseño`, `Competidores`, `Datos de búsqueda`, `IA sin respaldo` (o combinadas con `+` cuando la doctrina dirige a otra fuente).

> **Nota terminológica:** Cada row representa un **output** del paso. Antes llamábamos a esto "decisiones"; ahora se llama **output** (mismo concepto, nombre actualizado). La columna "Output y ejemplo" describe qué genera el paso; la columna "Cómo se obtiene" describe el método y la fuente del catálogo.

---

## Bloque 1 — Enlaces desde Homepage

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **7.01** · Paso-07 §6; Paso-05 §5 | ← 1.34–1.38 | **la Homepage enlace a Service Overview Pages** = `5 Service Overview Pages` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.02** · Paso-07 §6; Paso-05 §9 | ← 1.20 | **la Homepage enlace al GeoHub de Madrid** = `/madrid/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.03** · Paso-07 §6; Paso-05 §8 | ← 1.18 | **la Homepage enlace a la página de categoría adicional** = `/cerrajero/madrid/duplicado-llaves/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.04** · Paso-07 §6; Paso-02 §17 | no | **la Homepage enlace a contacto** = `/contacto/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 2 — Enlaces desde Service Overview y LBS

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **7.05** · Paso-07 §7; Paso-05 §6 | no | **cada Service Overview enlace a su versión local en Madrid** = `/cerrajero/[service]/ → /cerrajero/madrid/[service]/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.06** · Paso-07 §7 | no | **Service Overview enlace a servicios relacionados** = `Cross-links entre servicios` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.07** · Paso-07 §9; Paso-05 §7 | no | **LBS enlace a su página padre** = `LBS → Service Overview` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.08** · Paso-07 §9; Paso-05 §9 | no | **LBS enlace al GeoHub** = `LBS → /madrid/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.09** · Paso-07 §9 | no | **LBS enlace a servicios relacionados en Madrid** = `LBS → otras LBS` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.10** · Paso-07 §9; Paso-05 §10 | no | **LBS enlace a GeoArticles relacionados** = `LBS → GeoArticles` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 3 — Enlaces desde GeoHub y GeoArticles

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **7.11** · Paso-07 §8; Paso-05 §9; Paso-01 §13 | ← 1.34–1.38 | **GeoHub enlace a todas las LBS de Madrid** = `5 LBS` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.12** · Paso-07 §8; Paso-05 §8 | ← 1.18 | **GeoHub enlace a Additional Category Page** = `/cerrajero/madrid/duplicado-llaves/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.13** · Paso-07 §8; Paso-05 §10; Paso-03 §21 | ← 3.19–3.33 | **GeoHub enlace a GeoArticles** = `15 GeoArticles` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.14** · Paso-07 §11 | no | **GeoArticles enlacen a su LBS correspondiente** = `GeoArticle → LBS` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.15** · Paso-07 §11 | no | **GeoArticles enlacen al GeoHub** = `GeoArticle → /madrid/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 4 — Restricciones de enlaces

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **7.16** · Paso-07 §13; Paso-04 §13; Paso-03 §9 | no | **No enlazar Local Coverage Areas sin URL aprobada** = `No enlazar /almagro/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.17** · Paso-07 §13 | no | **usar anchors contextuales** = `Anchors naturales` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **7.18** · Paso-07 §17; Paso-05 §11 | no | **usar breadcrumbs** = `Home > Madrid > Servicio` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |