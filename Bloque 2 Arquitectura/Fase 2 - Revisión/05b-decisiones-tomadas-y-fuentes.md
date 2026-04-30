# Paso 5 — Page Type Rules · Decisiones tomadas

Trazabilidad de decisiones del Paso 5 — formato compacto de 4 columnas.

## Convención de columnas

- **ID y referencia canónica** — identificador único + referencia al §X del ejecutable.
- **Viene de una decisión anterior** — `no` si nace en esta fila; `← X.YY` si cascadea.
- **Decisión y ejemplo** — qué se decide + valor concreto en el ejemplo Cerrajeros Madrid 24h.
- **Cómo decidimos** — cómo se obtiene el valor + fuente del catálogo.

Fuentes posibles: `GMB Crush`, `Input humano`, `Decisión de diseño`, `Competidores`, `Datos de búsqueda`, `IA sin respaldo` (o combinadas con `+` cuando la doctrina dirige a otra fuente).

---

## Bloque 1 — Homepage

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **5.01** · Paso-05 §5 | no | **Se decide que la Homepage sea Root Entity Anchor** = `/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.02** · Paso-05 §5; Paso-01 §5; Paso-01 §9; Paso-01 §11 | ← 1.01, 1.16, 1.20 | **Se decide que la Homepage ancle marca, servicio principal y ciudad** = `Cerrajeros Madrid 24h + Cerrajero + Madrid` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.03** · Paso-05 §5; Paso-01 §13 | ← 1.34–1.38 | **Se decide que la Homepage incluya servicios core** = `5 servicios principales` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.04** · Paso-05 §5; Paso-01 §8; Paso-01 §17 | ← 1.08–1.15, 1.42 | **Se decide que la Homepage incluya NAP y CTA** = `NAP + Llamar ahora` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 2 — Service Overview Pages

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **5.05** · Paso-05 §6 | no | **Se decide que las Service Overview Pages sean no geolocalizadas** = `/cerrajero/[service]/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.06** · Paso-05 §6; Paso-04 §8; Paso-03 §19 | ← 1.34 | **Se decide que Cerrajero urgente tenga Service Overview Page** = `/cerrajero/cerrajero-urgente/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.07** · Paso-05 §6; Paso-04 §8; Paso-03 §19 | ← 1.35 | **Se decide que Apertura de puertas tenga Service Overview Page** = `/cerrajero/apertura-puertas/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.08** · Paso-05 §6; Paso-04 §8; Paso-03 §19 | ← 1.36 | **Se decide que Cambio de cerraduras tenga Service Overview Page** = `/cerrajero/cambio-cerraduras/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.09** · Paso-05 §6; Paso-04 §8; Paso-03 §19 | ← 1.37 | **Se decide que Cambio de bombines tenga Service Overview Page** = `/cerrajero/cambio-bombines/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.10** · Paso-05 §6; Paso-04 §8; Paso-03 §19 | ← 1.38 | **Se decide que Instalación de cerraduras de seguridad tenga Service Overview Page** = `/cerrajero/instalacion-cerraduras-seguridad/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 3 — Location-Based Service Pages

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **5.11** · Paso-05 §7 | no | **Se decide que las LBS sean convertidores locales** = `/cerrajero/madrid/[service]/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.12** · Paso-05 §7; Paso-04 §10; Paso-03 §19 | ← 1.34 | **Se decide que Cerrajero urgente en Madrid sea LBS canónica** = `/cerrajero/madrid/cerrajero-urgente/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.13** · Paso-05 §7; Paso-06 §14 | ← 1.20 | **Se decide que las LBS incluyan servicio + ciudad en H1 y metadata** = `[Service] + Madrid` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 4 — Additional Category, GeoHub y GeoArticles

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **5.14** · Paso-05 §8 | ← 1.18 | **Se decide que Duplicado de llaves sea Additional Category Page** = `/cerrajero/madrid/duplicado-llaves/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.15** · Paso-05 §9 | ← 1.20 | **Se decide que `/madrid/` sea GeoHub** = `GeoHub de Madrid` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.16** · Paso-05 §10 | no | **Se decide que GeoArticles sean boosters semánticos, no landings** = `15 GeoArticles` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.17** · Paso-05 §10; Paso-07 §13 | no | **Se decide que GeoArticles enlacen a su LBS y GeoHub** = `GeoArticle → LBS + /madrid/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 5 — Schema

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **5.18** · Paso-05 §11 | no | **Se decide asignar schema por tipo de página** = `Organization, WebSite, Service, LocalBusiness, CollectionPage, Article` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **5.19** · Paso-05 §11; Paso-14 §11 | no | **Se decide no usar `sameAs` de GBP hasta que exista el GBP** = `N/A hasta Paso 14` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |