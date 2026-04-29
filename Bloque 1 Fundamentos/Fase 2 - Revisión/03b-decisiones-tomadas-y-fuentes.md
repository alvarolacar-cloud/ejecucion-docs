# Paso 3 — Matriz Base · Decisiones tomadas

Trazabilidad de decisiones del Paso 3 — formato compacto de 4 columnas.

## Convención de columnas

- **ID y referencia canónica** — identificador único + referencia al §X del ejecutable.
- **Viene de una decisión anterior** — `no` si nace en esta fila; `← X.YY` si cascadea.
- **Decisión y ejemplo** — qué se decide + valor concreto en el ejemplo Cerrajeros Madrid 24h.
- **Cómo decidimos** — cómo se obtiene el valor + fuente del catálogo.

Fuentes posibles: `GMB Crush`, `Input humano`, `Decisión de diseño`, `Competidores`, `Datos de búsqueda`, `IA sin respaldo` (o combinadas con `+` cuando la doctrina dirige a otra fuente).

---

## Bloque 1 — Estructura de la matriz

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **3.01** · Paso-03 §8; Paso-03 §18 | no | **Se decide crear una matriz operativa para controlar las URLs** = `URL Matrix` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.02** · Paso-03 §10; Paso-03 §8 | no | **Se decide que cada página tenga un ID único** = `HP, SO, GH, LBS, AC, GA` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.03** · Paso-03 §18; Paso-03 §8 | no | **Se decide incluir columnas de producción** = `URL, H1, Meta Title, Schema, Priority, Phase, Status` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 2 — Homepage y páginas auxiliares

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **3.04** · Paso-03 §19; Paso-05 §7 | no | **Se decide incluir la Homepage en la matriz** = `HP-001` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.05** · Paso-03 §19; Paso-04 §9 | no | **Se decide que la Homepage use la raíz** = `/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.06** · Paso-03 §19; Paso-02 §17 | no | **Se decide incluir página de contacto como auxiliar** = `/contacto/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 3 — Service Overview Pages

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **3.07** · Paso-03 §19; Paso-05 §8; Paso-04 §10 | ← 1.34 | **Se decide crear Service Overview para Cerrajero urgente** = `/cerrajero/cerrajero-urgente/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.08** · Paso-03 §19; Paso-05 §8; Paso-04 §10 | ← 1.35 | **Se decide crear Service Overview para Apertura de puertas** = `/cerrajero/apertura-puertas/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.09** · Paso-03 §19; Paso-05 §8; Paso-04 §10 | ← 1.36 | **Se decide crear Service Overview para Cambio de cerraduras** = `/cerrajero/cambio-cerraduras/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.10** · Paso-03 §19; Paso-05 §8; Paso-04 §10 | ← 1.37 | **Se decide crear Service Overview para Cambio de bombines** = `/cerrajero/cambio-bombines/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.11** · Paso-03 §19; Paso-05 §8; Paso-04 §10 | ← 1.38 | **Se decide crear Service Overview para Instalación de cerraduras de seguridad** = `/cerrajero/instalacion-cerraduras-seguridad/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 4 — GeoHub y Location-Based Service Pages

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **3.12** · Paso-03 §19; Paso-05 §11; Paso-04 §11 | ← 1.20 | **Se decide crear el GeoHub principal de Madrid** = `/madrid/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.13** · Paso-03 §19; Paso-05 §9; Paso-04 §12 | ← 1.34 | **Se decide crear LBS de Cerrajero urgente en Madrid** = `/cerrajero/madrid/cerrajero-urgente/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.14** · Paso-03 §19; Paso-05 §9; Paso-04 §12 | ← 1.35 | **Se decide crear LBS de Apertura de puertas en Madrid** = `/cerrajero/madrid/apertura-puertas/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.15** · Paso-03 §19; Paso-05 §9; Paso-04 §12 | ← 1.36 | **Se decide crear LBS de Cambio de cerraduras en Madrid** = `/cerrajero/madrid/cambio-cerraduras/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.16** · Paso-03 §19; Paso-05 §9; Paso-04 §12 | ← 1.37 | **Se decide crear LBS de Cambio de bombines en Madrid** = `/cerrajero/madrid/cambio-bombines/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.17** · Paso-03 §19; Paso-05 §9; Paso-04 §12 | ← 1.38 | **Se decide crear LBS de Instalación de cerraduras de seguridad en Madrid** = `/cerrajero/madrid/instalacion-cerraduras-seguridad/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 5 — Additional Category Page

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **3.18** · Paso-03 §19; Paso-05 §10; Paso-04 §13 | ← 1.18 | **Se decide crear página de duplicado de llaves en Madrid** = `/cerrajero/madrid/duplicado-llaves/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 6 — GeoArticles

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **3.19** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle de coste de cerrajero urgente** = `/madrid/cuanto-cuesta-un-cerrajero-urgente/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.20** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre no poder entrar en casa** = `/madrid/que-hacer-si-no-puedes-entrar-casa/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.21** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre tiempo de llegada** = `/madrid/cuanto-tarda-un-cerrajero/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.22** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre coste de apertura de puertas** = `/madrid/cuanto-cuesta-abrir-una-puerta/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.23** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre llaves dentro** = `/madrid/que-hacer-si-te-dejas-las-llaves-dentro/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.24** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre apertura sin romper cerradura** = `/madrid/apertura-de-puertas-sin-romper-cerradura/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.25** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre cuándo cambiar cerradura** = `/madrid/cuando-cambiar-la-cerradura-de-casa/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.26** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre cambio tras perder llaves** = `/madrid/cambio-de-cerradura-tras-perder-llaves/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.27** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre cerradura nueva o reparación** = `/madrid/cerradura-nueva-o-reparacion/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.28** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre cuándo cambiar bombín** = `/madrid/cuando-cambiar-el-bombin/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.29** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre bombín antibumping** = `/madrid/bombin-antibumping-madrid/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.30** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre cambio de bombín sin cambiar cerradura** = `/madrid/cambio-de-bombin-sin-cambiar-cerradura/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.31** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre cerraduras de seguridad para viviendas** = `/madrid/mejores-cerraduras-de-seguridad-para-viviendas/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.32** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre cerraduras de seguridad para comunidades** = `/madrid/cerraduras-de-seguridad-para-comunidades/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |
| **3.33** · Paso-03 §21; Paso-02 §11 | no | **Se decide crear GeoArticle sobre cerradura de seguridad en puerta blindada** = `/madrid/instalar-cerradura-de-seguridad-en-puerta-blindada/` | Se extrae de keyword research. **Fuente:** GMB Crush + Datos de búsqueda. |

## Bloque 7 — Tratamiento de Local Coverage Areas

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **3.34** · Paso-03 §9; Paso-06 §10 | ← 1.22–1.31 | **Se decide que las Local Coverage Areas aparezcan como notas o campos de contenido** = `Almagro, Chamberí, Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **3.35** · Paso-03 §9; Paso-04 §15; Paso-06 §31 | no | **Se decide que no haya filas URL para Local Coverage Areas** = `No /almagro/, no /chamberi/, no /salamanca/` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |