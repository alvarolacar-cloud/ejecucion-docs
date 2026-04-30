# Paso 4 — URL Rules · Decisiones tomadas

Trazabilidad de decisiones del Paso 4 — formato compacto de 4 columnas.

## Convención de columnas

- **ID y referencia canónica** — identificador único + referencia al §X del ejecutable.
- **Viene de una decisión anterior** — `no` si nace en esta fila; `← X.YY` si cascadea.
- **Decisión y ejemplo** — qué se decide + valor concreto en el ejemplo Cerrajeros Madrid 24h.
- **Cómo decidimos** — cómo se obtiene el valor + fuente del catálogo.

Fuentes posibles: `GMB Crush`, `Input humano`, `Decisión de diseño`, `Competidores`, `Datos de búsqueda`, `IA sin respaldo` (o combinadas con `+` cuando la doctrina dirige a otra fuente).

---

## Bloque 1 — Dominio y formato general

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **4.01** · Paso-04 §5 | no | **Se decide usar HTTPS** = `https://` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.02** · Paso-04 §5; Paso-01 §6 | ← 1.03 | **Se decide usar dominio canónico con www** = `https://www.cerrajerosmadrid24h.com` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.03** · Paso-04 §6 | no | **Se decide usar trailing slash** = `Sí` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 2 — Patrones URL principales

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **4.04** · Paso-04 §7 | no | **Se decide que la Homepage use raíz** = `/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.05** · Paso-04 §8; Paso-05 §8 | no | **Se decide que Service Overview use categoría + servicio** = `/cerrajero/[service-slug]/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.06** · Paso-04 §10; Paso-05 §9 | no | **Se decide que LBS use categoría + ciudad + servicio** = `/cerrajero/madrid/[service-slug]/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.07** · Paso-04 §11; Paso-05 §10 | no | **Se decide que Additional Category use categoría + ciudad + servicio** = `/cerrajero/madrid/duplicado-llaves/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.08** · Paso-04 §9; Paso-05 §11 | no | **Se decide que GeoHub use ciudad** = `/madrid/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.09** · Paso-04 §12; Paso-05 §12 | no | **Se decide que GeoArticles usen ciudad + topic** = `/madrid/[article-topic-slug]/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 3 — URLs concretas de servicio

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **4.10** · Paso-04 §10; Paso-05 §9; Paso-03 §19 | ← 1.34 | **Se decide crear URL local de Cerrajero urgente** = `/cerrajero/madrid/cerrajero-urgente/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.11** · Paso-04 §10; Paso-05 §9; Paso-03 §19 | ← 1.35 | **Se decide crear URL local de Apertura de puertas** = `/cerrajero/madrid/apertura-puertas/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.12** · Paso-04 §10; Paso-05 §9; Paso-03 §19 | ← 1.36 | **Se decide crear URL local de Cambio de cerraduras** = `/cerrajero/madrid/cambio-cerraduras/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.13** · Paso-04 §10; Paso-05 §9; Paso-03 §19 | ← 1.37 | **Se decide crear URL local de Cambio de bombines** = `/cerrajero/madrid/cambio-bombines/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.14** · Paso-04 §10; Paso-05 §9; Paso-03 §19 | ← 1.38 | **Se decide crear URL local de Instalación de cerraduras de seguridad** = `/cerrajero/madrid/instalacion-cerraduras-seguridad/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 4 — Reglas anti-URL débil

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **4.15** · Paso-04 §17; Paso-04 §19 | no | **Se decide no usar `near-me` en URLs principales** = `No se usa near-me` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.16** · Paso-04 §17; Paso-04 §19 | no | **Se decide no usar adjetivos SEO vacíos en URLs** = `No usar best, cheap, top-rated` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.17** · Paso-04 §13; Paso-03 §9; Paso-06 §31 | no | **Se decide no crear URLs para Local Coverage Areas en la base** = `No /almagro/, no /chamberi/, no /salamanca/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **4.18** · Paso-04 §14; Paso-02 §13; Paso-01 §15 | no | **Se decide que Approved Expansion Areas podrían generar URLs solo en expansión** = `None in Phase 1` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |