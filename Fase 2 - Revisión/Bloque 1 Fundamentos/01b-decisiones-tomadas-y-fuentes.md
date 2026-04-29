# Paso 1 — Intake Form · Decisiones tomadas

Trazabilidad de decisiones del Paso 1 — formato compacto de 4 columnas.

## Convención de columnas

- **ID y referencia canónica** — identificador único + referencia al §X del ejecutable.
- **Viene de una decisión anterior** — `no` si nace en esta fila; `← X.YY` si cascadea.
- **Decisión y ejemplo** — qué se decide + valor concreto en el ejemplo Cerrajeros Madrid 24h.
- **Cómo decidimos** — cómo se obtiene el valor + fuente del catálogo.

Fuentes posibles: `GMB Crush`, `Input humano`, `Decisión de diseño`, `Competidores`, `Datos de búsqueda`, `IA sin respaldo` (o combinadas con `+` cuando la doctrina dirige a otra fuente).

---

## Bloque 1 — Identidad del negocio

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **1.01** · Paso-01 §5 | no | **Se define el nombre del negocio** = `Cerrajeros Madrid 24h` | Lo declara el cliente en el intake. **Fuente:** Input humano. |
| **1.02** · Paso-01 §6 | no | **Se define la URL principal de la web** = `https://www.cerrajerosmadrid24h.com` | Lo declara el cliente en el intake. **Fuente:** Input humano. |
| **1.03** · Paso-01 §6 | no | **Se define el dominio canónico** = `https://www.cerrajerosmadrid24h.com` | Lo declara el cliente en el intake. **Fuente:** Input humano. |

## Bloque 2 — Estado inicial del GBP

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **1.04** · Paso-01 §3 | no | **Se decide el estado del GBP** = `GBP Status: Not Created` | Lo declara el cliente en el intake. **Fuente:** Input humano. |
| **1.05** · Paso-14 §7; Paso-01 §3 | no | **Se decide el momento de creación del GBP** = `After website launch` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **1.06** · Paso-01 §3 | no | **Se decide el estado de verificación del GBP** = `Not Started` | Lo declara el cliente en el intake. **Fuente:** Input humano. |
| **1.07** · Paso-14 §11; Paso-01 §3 | no | **Se decide que no hay GBP URL todavía** = `N/A — GBP not created yet` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 3 — NAP y contacto

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **1.08** · Paso-01 §8 | ← 1.01 | **Se define el nombre NAP** = `Cerrajeros Madrid 24h` | Lo declara el cliente en el intake. **Fuente:** Input humano. |
| **1.09** · Paso-01 §8 | no | **Se define la dirección del negocio** = `Calle Rafael Calvo 12, Barrio Almagro, Distrito Chamberí` | Lo declara el cliente en el intake. **Fuente:** Input humano. |
| **1.10** · Paso-01 §8 | no | **Se define la ciudad del negocio** = `Madrid` | Lo declara el cliente en el intake. **Fuente:** Input humano. |
| **1.11** · Paso-01 §8 | ← 1.10 | **Se define la provincia o comunidad** = `Comunidad de Madrid` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **1.12** · Paso-01 §8 | no | **Se define el código postal** = `28010` | Lo declara el cliente en el intake. **Fuente:** Input humano. |
| **1.13** · Paso-01 §8 | no | **Se define el país** = `España` | Lo declara el cliente en el intake. **Fuente:** Input humano. |
| **1.14** · Paso-01 §8 | no | **Se define el teléfono del negocio** = `+34 600 000 000` | Lo declara el cliente en el intake. **Fuente:** Input humano. |
| **1.15** · Paso-01 §8 | no | **Se define el email del negocio** = `info@cerrajerosmadrid24h.com` | Lo declara el cliente en el intake. **Fuente:** Input humano. |

## Bloque 4 — Categorías GBP planificadas

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **1.16** · Paso-01 §9 | no | **Se define la categoría principal planificada para el futuro GBP** = `Cerrajero` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.17** · Paso-01 §10 | no | **Se define una categoría adicional planificada** = `Servicio de cerrajería de urgencia` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.18** · Paso-01 §10 | no | **Se define otra categoría adicional planificada** = `Servicio de duplicado de llaves` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |

## Bloque 5 — Dirección física, Main City y zonas

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **1.19** · Paso-01 §8; Paso-01 §11 | ← 1.09 | **Se define la dirección física como ancla del sistema** = `Calle Rafael Calvo 12, Barrio Almagro, Distrito Chamberí, Madrid` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **1.20** · Paso-01 §11; Paso-01 §8 | ← 1.10 | **Se define la ciudad que crea la arquitectura base** = `Madrid` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **1.21** · Paso-01 §12 | no | **Se define la ciudad de ubicación física** = `Madrid` | Lo declara el cliente en el intake. **Fuente:** Input humano. |
| **1.22** · Paso-01 §14; Paso-06 §10 | ← 1.09 | **Se define una Direct Local Coverage Area** = `Almagro` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **1.23** · Paso-01 §14; Paso-06 §10 | ← 1.09 | **Se define una Direct Local Coverage Area** = `Chamberí` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **1.24** · Paso-01 §14; Paso-06 §10 | no | **Se define una Candidate Local Coverage Area** = `Salamanca` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.25** · Paso-01 §14; Paso-06 §10 | no | **Se define una Candidate Local Coverage Area** = `Retiro` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.26** · Paso-01 §14; Paso-06 §10 | no | **Se define una Candidate Local Coverage Area** = `Centro` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.27** · Paso-01 §14; Paso-06 §10 | no | **Se define una Candidate Local Coverage Area** = `Tetuán` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.28** · Paso-01 §14; Paso-06 §10 | no | **Se define una Candidate Local Coverage Area** = `Chamartín` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.29** · Paso-01 §14; Paso-06 §10 | no | **Se define una Candidate Local Coverage Area** = `Arganzuela` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.30** · Paso-01 §14; Paso-06 §10 | no | **Se define una Candidate Local Coverage Area** = `Moncloa` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.31** · Paso-01 §14; Paso-06 §10 | no | **Se define una Candidate Local Coverage Area** = `Prosperidad` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |

## Bloque 6 — Expansión geográfica

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **1.32** · Paso-01 §15; Paso-04 §15; Paso-06 §31 | no | **Se decide que las Local Coverage Areas no generarán páginas en la base** = `No, not in the base build` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **1.33** · Paso-01 §15; Paso-02 §13 | no | **Se decide que no hay Approved Expansion Areas en la fase inicial** = `None in Phase 1` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 7 — Servicios principales

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **1.34** · Paso-01 §13 | no | **Se define el servicio principal 1** = `Cerrajero urgente` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.35** · Paso-01 §13 | no | **Se define el servicio principal 2** = `Apertura de puertas` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.36** · Paso-01 §13 | no | **Se define el servicio principal 3** = `Cambio de cerraduras` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.37** · Paso-01 §13 | no | **Se define el servicio principal 4** = `Cambio de bombines` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.38** · Paso-01 §13 | no | **Se define el servicio principal 5** = `Instalación de cerraduras de seguridad` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |

## Bloque 8 — Consolidación de categorías adicionales

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **1.39** · Paso-01 §10; Paso-02 §10 | ← 1.17, 1.34 | **Se decide que una categoría adicional ya está cubierta por un servicio principal** = `Servicio de cerrajería de urgencia queda cubierta por Cerrajero urgente` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **1.40** · Paso-01 §10; Paso-02 §10 | ← 1.18 | **Se decide que una categoría adicional necesita página propia** = `Servicio de duplicado de llaves` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |

## Bloque 9 — Contenido, conversión y confianza

| ID y referencia canónica | Viene de una decisión anterior | Decisión y ejemplo | Cómo decidimos |
|---|---|---|---|
| **1.41** · Paso-02 §11; Paso-01 §3 | no | **Se define el número de GeoArticles por servicio** = `3` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **1.42** · Paso-01 §17 | no | **Se define el CTA principal** = `Llamar ahora` | Lo decide el operador con criterio de diseño. **Fuente:** Decisión de diseño. |
| **1.43** · Paso-01 §18 | no | **Se define una señal de confianza** = `10+ años de experiencia` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.44** · Paso-01 §18; Paso-14 §15 | no | **Se define una señal de confianza pendiente del futuro GBP** = `Reseñas iniciales pendientes de recopilar tras crear y verificar el GBP` | Lo dicta la doctrina GMB Crush. **Fuente:** GMB Crush. |
| **1.45** · Paso-01 §18 | no | **Se define una señal de confianza** = `Técnicos cerrajeros cualificados` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.46** · Paso-01 §18 | no | **Se define una señal de confianza** = `Servicio móvil en el mismo día` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |
| **1.47** · Paso-01 §18 | no | **Se define una señal de confianza** = `Garantía de trabajo` | Se extrae del análisis de competidores top del Local Pack. **Fuente:** GMB Crush + Competidores. |