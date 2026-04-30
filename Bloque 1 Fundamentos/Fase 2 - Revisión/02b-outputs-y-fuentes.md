# Paso 2 — Fórmula Maestra de Arquitectura · Outputs

Trazabilidad de outputs del Paso 2 — formato compacto de 4 columnas.

## Convención de columnas

- **ID y referencia canónica** — identificador único + referencia al §X del a-doc.
- **Viene de un output anterior** — `no` si nace en esta fila; `← X.YY` si deriva de un output anterior.
- **Output y ejemplo** — qué output produce el paso + valor concreto en el ejemplo Cerrajeros Madrid 24h.
- **Cómo se obtiene** — método de obtención del output + fuente del catálogo.

Fuentes posibles: `GMB Crush`, `Input humano`, `Decisión de diseño`, `Competidores`, `Datos de búsqueda`, `IA sin respaldo` (o combinadas con `+` cuando la doctrina dirige a otra fuente).

> **Nota terminológica:** Cada row representa un **output** del paso. Antes llamábamos a esto "decisiones"; ahora se llama **output** (mismo concepto, nombre actualizado). La columna "Output y ejemplo" describe qué genera el paso; la columna "Cómo se obtiene" describe el método y la fuente del catálogo.

---

## Bloque 1 — Alcance de la fórmula base

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **2.01** · Paso-02 §7; Paso-01 §11 | ← 1.20 | **la fórmula base se construye sobre una sola Main City** = `Madrid` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.02** · Paso-02 §12; Paso-02 §7 | no | **las Local Coverage Areas no multiplican páginas por defecto** = `Almagro, Chamberí, Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa y Prosperidad no generan URLs base` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.03** · Paso-02 §13; Paso-02 §18 | no | **las Approved Expansion Areas no entran en la fórmula inicial** = `None in Phase 1` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 2 — Servicios incluidos en el cálculo

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **2.04** · Paso-02 §8; Paso-01 §13 | ← 1.34–1.38 | **Se define el número de servicios principales usados en la fórmula** = `S = 5` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.05** · Paso-02 §8; Paso-01 §13 | ← 1.34 | **Se incluye Cerrajero urgente en el cálculo** = `Cerrajero urgente` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.06** · Paso-02 §8; Paso-01 §13 | ← 1.35 | **Se incluye Apertura de puertas en el cálculo** = `Apertura de puertas` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.07** · Paso-02 §8; Paso-01 §13 | ← 1.36 | **Se incluye Cambio de cerraduras en el cálculo** = `Cambio de cerraduras` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.08** · Paso-02 §8; Paso-01 §13 | ← 1.37 | **Se incluye Cambio de bombines en el cálculo** = `Cambio de bombines` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.09** · Paso-02 §8; Paso-01 §13 | ← 1.38 | **Se incluye Instalación de cerraduras de seguridad en el cálculo** = `Instalación de cerraduras de seguridad` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 3 — Páginas generadas por la fórmula

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **2.10** · Paso-02 §7; Paso-05 §7 | no | **crear una Homepage** = `1 Homepage` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.11** · Paso-02 §8; Paso-02 §7 | ← 1.34–1.38 | **crear una Service Overview Page por cada servicio principal** = `5 Service Overview Pages` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.12** · Paso-02 §7; Paso-05 §11 | no | **crear un GeoHub para la Main City** = `1 GeoHub para Madrid` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.13** · Paso-02 §8; Paso-02 §7; Paso-05 §9 | ← 1.34–1.38 | **crear una Location-Based Service Page por cada servicio principal en Madrid** = `5 LBS` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.14** · Paso-02 §10; Paso-05 §10 | ← 1.18 | **crear una Additional Category Page para la categoría adicional efectiva** = `1 Additional Category Page` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 4 — Categorías adicionales efectivas

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **2.15** · Paso-02 §10; Paso-01 §10 | ← 1.39 | **Servicio de cerrajería de urgencia no suma como categoría adicional separada** = `Queda cubierta por Cerrajero urgente` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.16** · Paso-02 §10; Paso-01 §10 | ← 1.40 | **Servicio de duplicado de llaves sí cuenta como categoría adicional efectiva** = `A = 1` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 5 — GeoArticles

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **2.17** · Paso-02 §11 | no | **usar 3 GeoArticles por servicio principal** = `G = 3` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.18** · Paso-02 §11; Paso-02 §8 | ← 1.34–1.38 | **calcular GeoArticles como G × S** = `3 × 5` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.19** · Paso-02 §11; Paso-02 §7 | ← 1.34–1.38 | **Se calcula el número total de GeoArticles** = `15 GeoArticles` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.20** · Paso-02 §11; Paso-02 §12 | no | **los GeoArticles se generan para Madrid, no para cada Local Coverage Area** = `15 GeoArticles para Madrid` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 6 — Total de páginas SEO base

| ID y referencia canónica | Viene de un output anterior | Output y ejemplo | Cómo se obtiene |
|---|---|---|---|
| **2.21** · Paso-02 §17; Paso-02 §7 | no | **Se calcula el bloque de Homepage** = `1 página` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.22** · Paso-02 §17; Paso-02 §8 | ← 1.34–1.38 | **Se calcula el bloque de Service Overview Pages** = `5 páginas` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.23** · Paso-02 §17; Paso-02 §7 | no | **Se calcula el bloque de GeoHub** = `1 página` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.24** · Paso-02 §17; Paso-02 §8 | ← 1.34–1.38 | **Se calcula el bloque de Location-Based Service Pages** = `5 páginas` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.25** · Paso-02 §17; Paso-02 §10 | ← 1.18 | **Se calcula el bloque de Additional Category Pages** = `1 página` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.26** · Paso-02 §17; Paso-02 §11 | ← 1.34–1.38 | **Se calcula el bloque de GeoArticles** = `15 páginas` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.27** · Paso-02 §7; Paso-02 §17 | ← 1.18, 1.34–1.38 | **Se calcula el total de páginas SEO base** = `28 páginas SEO base` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **2.28** · Paso-02 §17; Paso-03 §8 | no | **`/contacto/` queda fuera del inventario SEO base** = `Página auxiliar` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |