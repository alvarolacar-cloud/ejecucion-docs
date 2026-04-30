Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo la estructura fija acordada en la conversación.
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# §1 Paso 4 — URL Rules

# Bloque I — Introducción

## §2 Objetivo del Paso 4

Fijar las **reglas operativas de URL** que rigen toda la arquitectura del cluster local: dominio canónico, convención de slash, patrones de path por tipo de página, y filtros anti-canibalización. Estas reglas son la base sobre la que el Paso 3 (URL Matrix) genera URLs concretas y el Paso 5 (Page Type Rules) define cómo rellenar cada tipo de página.

**Outputs del Paso 4:**

- §5 Canonical Domain — versión única del dominio (con/sin www, http/https) usada en todas las URLs absolutas, schema y enlaces internos
- §6 Trailing Slash — convención boolean (Yes/No) aplicada idéntica a todo el cluster
- §7 Homepage URL — path constante `/` (doctrina, no decisión)
- §8 Service Overview URL pattern — `/{primary-cat-slug}/{service-slug}/` para Service Overview Pages (sin ciudad)
- §9 Main City GeoHub URL Style — Option A `/{main-city-slug}/` (default) u Option B `/{primary-cat-slug}/{main-city-slug}/`
- §10 Location-Based Service URL pattern — `/{primary-cat-slug}/{main-city-slug}/{service-slug}/` para LBS Pages
- §11 Additional Category URL pattern — `/{primary-cat-slug}/{main-city-slug}/{additional-slug}/` para AC Pages efectivas
- §12 GeoArticle URL pattern — Option A `/{main-city-slug}/{topic-slug}/` (default) u Option B con primary category prefijo
- §13 Local Coverage Areas no generan URLs — regla de doctrina: LCAs viven en contenido y schema `areaServed`, no en path
- §14 Approved Expansion URLs — patrones aplicables solo si hay AEAs aprobadas (Paso 1 §15); por defecto E=0
- §15 No "near me" en URLs — validación que rechaza patrones `near-me`, `cerca-de-mi`, equivalentes en slugs
- §16 No adjetivos vacíos en URLs — validación que rechaza `best`, `cheap`, `top-rated`, `mejor`, `barato`
- §17 Slugs limpios — transformación slugify estándar: lowercase + sin diacríticos + dashes + sin símbolos
- §18 No falsa ubicación — validación cruzada con NAP (Paso 1 §12) y AEA (Paso 1 §15) para rechazar URLs que sugieren oficina física inexistente
- §19 No duplicar intención — validación de pares de URLs en el cluster; consolida duplicados con 301

**Errores que previene el Paso 4:**

- Crear URLs distintas para la misma intención local (canibalización)
- Convertir Local Coverage Areas en carpetas sin aprobación (sprawl arquitectónico)
- Mezclar ciudad, servicio y artículo en el mismo patrón (silos rotos)
- Slugs con `near-me`, `best`, `cheap`, `top-rated` (modificadores inestables)
- Versiones inconsistentes con/sin trailing slash (duplicación técnica)
- Mezclar `www` y non-www, HTTP y HTTPS en URLs absolutas (señales canónicas mezcladas)
- Implicar oficina física en zonas donde el negocio no opera (E-E-A-T comprometido)

**Cuándo se ejecuta:**

Antes del Paso 3 (URL Matrix). El Paso 3 aplica los patrones aquí definidos para generar las URLs concretas. Sin las reglas del Paso 4, el Paso 3 no tiene base para validar el formato y la consistencia de cada URL del cluster.

## §3 Info heredada de pasos anteriores

El Paso 4 toma como input estos elementos generados en pasos previos. La IA no los re-decide aquí; los aplica como restricciones / fuentes para construir las reglas y patrones URL del cluster.

| # | Input heredado | Origen | Uso en el Paso 4 |
|---|---|---|---|
| 1 | Website URL (root domain) | Paso 1 §6 | Define la URL canónica base (§5) |
| 2 | Brand Name | Paso 1 §2 | Confirma identidad para validaciones cruzadas |
| 3 | NAP — Physical Location City | Paso 1 §12 | Valida el segmento Main City (§18 No falsa ubicación) |
| 4 | Core Services list (S core services) | Paso 1 §13 | Genera las S URLs Service Overview (§8) y S URLs LBS (§10) |
| 5 | Local Coverage Areas (Direct + Candidate) | Paso 1 §14 | Confirma que NO generan URLs por defecto (§13) |
| 6 | Approved Expansion Areas (E count) | Paso 1 §15 | Determina si se aplican patrones de expansión (§14); E=0 → 0 URLs adicionales |
| 7 | Slug Generation rule | Paso 2 §6 | Aplica slugify estándar a cada slug del cluster (§17) |
| 8 | Primary Category Slug | Paso 3 §3 (Slug Generation aplicado al Primary GBP Category) | Segmento `[primary-cat-slug]` en patrones §8, §10, §11, §12 (Option B), §14 |
| 9 | Main City Slug | Paso 3 §3 (Slug Generation aplicado a Main City) | Segmento `[main-city-slug]` en patrones §9, §10, §11, §12, §14 |
| 10 | Service slugs (S slugs aprobados) | Paso 3 §3 | Segmento `[service-slug]` en §8, §10, §14 |
| 11 | Additional Category slugs (A slugs efectivos) | Paso 3 §7 | Segmento `[additional-slug]` en §11 |
| 12 | GeoArticle topics validados | Paso 3 §21 (keyword research) | Segmento `[topic-slug]` en §12 (15 GeoArticles = G × S) |
| 13 | GeoHub URL Style (Option A / B) | Paso 3 §6 | Aplica directamente en §9 (decisión heredada, no se re-toma aquí) |

## §4 Ejemplo rellenado — Outputs del Paso 4 para Cerrajeros Madrid 24h

Esta sección consolida los 15 outputs del Paso 4 en tablas operativas. Cada output corresponde a una sección §X del Bloque II y se valida individualmente.

### §4.1 Reglas de dominio y convención (§5–§7)

| Output | §X | Valor (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|
| Canonical Domain | §5 | `https://www.cerrajerosmadrid24h.com` | confirmed |
| Trailing Slash | §6 | Yes (todas las URLs terminan en `/`) | confirmed |
| Homepage URL | §7 | `/` | confirmed |

### §4.2 Patrones URL por tipo de página (§8–§12)

| Output | §X | Patrón | Aplicado a (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|---|
| Service Overview pattern | §8 | `/{primary-cat-slug}/{service-slug}/` | 5 URLs SO → `/cerrajero/cerrajero-urgente/`, `/cerrajero/apertura-puertas/`, `/cerrajero/cambio-cerraduras/`, `/cerrajero/cambio-bombines/`, `/cerrajero/instalacion-cerraduras-seguridad/` | confirmed |
| Main City GeoHub pattern | §9 | Option A `/{main-city-slug}/` | 1 URL → `/madrid/` | confirmed |
| Location-Based Service pattern | §10 | `/{primary-cat-slug}/{main-city-slug}/{service-slug}/` | 5 URLs LBS → `/cerrajero/madrid/cerrajero-urgente/`, etc. (S=5) | confirmed |
| Additional Category pattern | §11 | `/{primary-cat-slug}/{main-city-slug}/{additional-slug}/` | 1 URL AC → `/cerrajero/madrid/duplicado-llaves/` (A=1 efectiva) | confirmed |
| GeoArticle pattern | §12 | Option A `/{main-city-slug}/{topic-slug}/` | 15 URLs GA (G=3 × S=5) → `/madrid/cuanto-cuesta-un-cerrajero-urgente/`, etc. | ⚠ inferido (topics requieren keyword research real, ver §24.1) |

### §4.3 Reglas de cobertura geográfica (§13–§14)

| Output | §X | Regla | Aplicación (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|---|
| LCAs no generan URLs | §13 | Las Local Coverage Areas viven en contenido y schema `areaServed`, NO en path | Almagro, Chamberí, Salamanca, Retiro → 0 URLs adicionales | confirmed |
| Approved Expansion URLs | §14 | Solo si E≥1 en Paso 1 §15; aplicar mismos patrones del cluster con AEA como segmento | E=0 en Phase 1 → 0 URLs de expansión | confirmed |

### §4.4 Validaciones anti-canibalización y limpieza (§15–§19)

| Output | §X | Validación | Resultado (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|---|
| No "near me" en URLs | §15 | Rechazar `near-me`, `cerca-de-mi`, `cerca-mi`, `near` y equivalentes en cualquier slug | 0 URLs del cluster contienen estos patrones | confirmed |
| No adjetivos vacíos | §16 | Rechazar `best`, `cheap`, `top-rated`, `mejor`, `barato`, `top` en cualquier slug | 0 URLs del cluster contienen estos patrones | confirmed |
| Slugs limpios | §17 | Aplicar slugify: lowercase + sin diacríticos + dashes + sin símbolos | Todos los slugs (`cerrajero-urgente`, `chamberi`, `duplicado-llaves`) cumplen | confirmed |
| No falsa ubicación | §18 | Cada segmento city del path debe corresponder a NAP (Paso 1 §12) o AEA aprobada (Paso 1 §15) | Solo `/madrid/` aparece como city; ninguna `/almagro/`, `/chamberi/` (LCAs sin oficina) | confirmed |
| No duplicar intención | §19 | Para cada par de URLs, validar que NO compartan intención local + servicio | 0 pares con duplicación detectada (core services y additional category cubren intenciones distintas) | confirmed |

### §4.5 Estructura final del cluster — totales

| Tipo de página | Patrón | Cantidad | Subtotal |
|---|---|---|---|
| Homepage | `/` | 1 | 1 |
| Service Overview | `/cerrajero/{service}/` | 5 | 5 |
| Main City GeoHub | `/madrid/` | 1 | 1 |
| Location-Based Service | `/cerrajero/madrid/{service}/` | 5 | 5 |
| Additional Category | `/cerrajero/madrid/{additional}/` | 1 | 1 |
| GeoArticle | `/madrid/{topic}/` | 15 | 15 |
| **Total cluster (sin expansión)** | — | — | **28** |
| Approved Expansion (Phase 1) | — | 0 | 0 |
| **Total final** | — | — | **28** |

### §4.6 Validaciones cruzadas con otros pasos

| Validación | Origen | Comprobación en Paso 4 | Status |
|---|---|---|---|
| Canonical Domain coincide con Website URL | Paso 1 §6 | `https://www.cerrajerosmadrid24h.com` = Website URL declarada | OK |
| Slugs generados con regla del Paso 2 | Paso 2 §6 | Todos los slugs del cluster pasan slugify estándar | OK |
| URLs de la URL Matrix (Paso 3 §3) cumplen los patrones del Paso 4 | Paso 3 §3 | 28 URLs de la matriz validadas contra §8, §9, §10, §11, §12 | OK |
| Main City del path = NAP del Paso 1 §12 | Paso 1 §12 | `/madrid/` corresponde a Madrid (oficina física declarada) | OK |
| LCAs heredadas no aparecen como path | Paso 1 §14 | 0 paths con `/almagro/`, `/chamberi/`, `/salamanca/`, `/retiro/` | OK |

# Bloque II — Ejecución por la IA

## §5 Canonical Domain

### §5.1 Explicación

**Explicación**

Todas las URLs deben salir de una sola versión del dominio. Esto evita duplicación técnica y señales inconsistentes.

**Patrón o fórmula**

```text
Canonical Domain → todas las URLs absolutas → redirección del resto
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h usa https://www.cerrajerosmadrid24h.com como dominio canónico para /cerrajero/madrid/cerrajero-urgente/.
```

**Ejemplos incorrectos**

```text
- https://cerrajerosmadrid24h.com mezclado con https://www.cerrajerosmadrid24h.com
- http://www.cerrajerosmadrid24h.com
- URLs relativas sin canonical
- Usar https://cerrajerosmadrid24h.com en schema y https://www.cerrajerosmadrid24h.com en la matriz
- Mantener versiones HTTP accesibles
- Crear enlaces internos con dominios mezclados
```

**Regla final**

```text
Una sola versión canónica del dominio en toda la web; el resto redirige 301.
```

**Validación operativa**

Todas las URLs deben salir de una única versión canónica del dominio. Mezclar www, non-www, HTTP y HTTPS crea duplicados técnicos y dificulta la consistencia del schema y la matriz.

### §5.2 Cómo obtenemos el Canonical Domain

**Fuente:** GMB Crush ← heredado del Paso 1 §6 Website URL.

**Método:** Tomar el dominio canónico declarado en el intake del Paso 1 §6. Aplicar como única versión válida en todo el cluster. El resto de variantes (con/sin www, http vs https, mayúsculas) redirigen 301 a la canónica.

### §5.3 Output del paso

**Tipo:** URL canónica única.

**Ejemplo (Cerrajeros Madrid 24h):** `https://www.cerrajerosmadrid24h.com`.

## §6 Trailing Slash

### §6.1 Explicación

**Explicación**

La regla del slash final debe ser consistente en todo el sitio.

**Patrón o fórmula**

```text
URL pattern → trailing slash uniforme → canonical
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
La URL correcta es /cerrajero/madrid/cerrajero-urgente/ si el sistema usa trailing slash.
```

**Ejemplos incorrectos**

```text
- /cerrajero/madrid/cerrajero-urgente
- Mezclar ambas versiones
- Canonical distinto al enlace interno
- Publicar /cerrajero/madrid/cerrajero-urgente y /cerrajero/madrid/cerrajero-urgente/
- Crear enlaces internos sin la convención aprobada
- No canonicalizar variantes
```

**Regla final**

```text
Trailing slash decidido al inicio se aplica idéntico a TODAS las URLs del cluster.
```

**Validación operativa**

La regla de slash final debe ser uniforme. No importa tanto si se usa o no slash, sino que todas las URLs sigan la misma convención.

### §6.2 Cómo obtenemos el Trailing Slash

**Fuente:** Decisión de diseño.

**Método:** Decidir Yes (trailing slash siempre) o No (nunca trailing slash) en el intake del Paso 4 §3. La decisión aplica idéntica a TODAS las URLs del cluster. Default: Yes (slash final, más limpio para parsing y consistente con la mayoría de CMSs).

### §6.3 Output del paso

**Tipo:** Boolean — Yes/No, aplicado a todas las URLs.

**Ejemplo (Cerrajeros Madrid 24h):** Yes → `/cerrajero/madrid/cerrajero-urgente/` (con `/` final).

## §7 Homepage URL

### §7.1 Explicación

**Explicación**

La homepage es la raíz de entidad y debe vivir en el root domain.

**Patrón o fórmula**

```text
Homepage = /
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h usa / como homepage y desde ahí enlaza a servicios, GeoHub de Madrid y contacto.
```

**Ejemplos incorrectos**

```text
- /home/
- /inicio/
- /madrid-cerrajero/
- /cerrajero-madrid/
- Usar /home/ como homepage principal
- Crear /madrid-cerrajero/ como sustituto de la homepage
- Duplicar contenido de homepage en otra URL
```

**Regla final**

```text
La Homepage vive en `/` — sin prefijo, sin sufijo.
```

**Validación operativa**

La homepage debe ser la raíz del dominio. No debe moverse a /home/, /inicio/ o /cerrajero-madrid/ porque actúa como Root Entity Anchor del negocio.

### §7.2 Cómo obtenemos la Homepage URL

**Fuente:** GMB Crush.

**Método:** La Homepage SIEMPRE vive en `/`. No hay decisión que tomar — es doctrina. No se permite `/home/`, `/inicio/`, `/index/`.

### §7.3 Output del paso

**Tipo:** Path constante.

**Ejemplo (Cerrajeros Madrid 24h):** `/`.

## §8 Service Overview URL pattern

### §8.1 Explicación

**Explicación**

Las páginas de servicio general son no geolocalizadas y no llevan ciudad.

**Patrón o fórmula**

```text
/[primary-category-slug]/[service-slug]/
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
La URL correcta para Cerrajero urgente general es /cerrajero/cerrajero-urgente/.
```

**Ejemplos incorrectos**

```text
- /cerrajero-urgente-madrid/
- /madrid/cerrajero-urgente/
- /services/cerrajero-urgente/
- /cerrajero/madrid/cerrajero-urgente-overview/
- /cerrajero/madrid-cerrajero-urgente/
- /services/cerrajero-urgente/ si rompe la taxonomía aprobada
```

**Regla final**

```text
Service Overview Pages siguen `/{primary-cat-slug}/{service-slug}/` sin ciudad.
```

**Validación operativa**

Las páginas de servicio general no deben incluir ciudad en la URL. Su función es construir autoridad temática y servir como padre de la página local.

### §8.2 Cómo obtenemos el Service Overview URL pattern

**Fuente:** GMB Crush.

**Método:** Aplicar `/{primary-cat-slug}/{service-slug}/` para cada core service heredado del Paso 1 §13 (S=5). Los slugs se obtienen del Paso 2 §6 Slug Generation. Genera S Service Overview Pages.

### §8.3 Output del paso

**Tipo:** Lista de S URLs (formato `/cat/service/`).

**Ejemplo (Cerrajeros Madrid 24h):** `/cerrajero/cerrajero-urgente/`, `/cerrajero/apertura-puertas/`, `/cerrajero/cambio-cerraduras/`, etc.

## §9 Main City GeoHub URL Style

### §9.1 Explicación

**Explicación**

El GeoHub de la Main City agrupa todo lo relacionado con la ciudad principal.

**Patrón o fórmula**

```text
/[main-city]/ OR /[category]/[main-city]/
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h usa /madrid/ como GeoHub de la Main City.
```

**Ejemplos incorrectos**

```text
- /areas-we-serve/madrid/
- /locations/madrid/
- /service-area/madrid/
- /madrid-cerrajero-services/
- /cerrajero-services-madrid/
```

**Regla final**

```text
GeoHub usa Option A (`/{main-city-slug}/`) por defecto; Option B solo si está justificado.
```

**Validación operativa**

El GeoHub de la Main City debe ser corto, estable y fácil de enlazar. Puede usar /city/ o /category/city/, pero en la base simplificada se recomienda /city/.

### §9.2 Cómo obtenemos el Main City GeoHub URL Style

**Fuente:** Decisión de diseño ← heredado del Paso 3 §6 GeoHub URL Style.

**Método:** Aplicar la decisión Option A (`/{main-city-slug}/`) o Option B (`/{primary-cat-slug}/{main-city-slug}/`) tomada en el Paso 3 §6. Default: Option A (más limpio).

### §9.3 Output del paso

**Tipo:** URL única para el GeoHub Main City.

**Ejemplo (Cerrajeros Madrid 24h):** Option A → `/madrid/`.

## §10 Location-Based Service URL pattern

### §10.1 Explicación

**Explicación**

Estas son las páginas comerciales para búsquedas service + city.

**Patrón o fórmula**

```text
/[category]/[main-city]/[service]/
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
La URL correcta es /cerrajero/madrid/cerrajero-urgente/.
```

**Ejemplos incorrectos**

```text
- /madrid/cerrajero-urgente/
- /cerrajero-urgente/madrid/
- /cerrajero/cerrajero-urgente-madrid/
- /cerrajero/madrid/urgente-car-cambio-cerraduras/
- /madrid/cerrajero-urgente/ si se reserva /madrid/ para GeoHub y artículos
```

**Regla final**

```text
LBS sigue `/{primary-cat-slug}/{main-city-slug}/{service-slug}/` — patrón fijo, sin variaciones.
```

**Validación operativa**

Las páginas comerciales locales deben seguir el patrón categoría + ciudad + servicio. Esto mantiene claro el silo y evita mezclar intención de servicio con artículo o hub.

### §10.2 Cómo obtenemos el Location-Based Service URL pattern

**Fuente:** GMB Crush.

**Método:** Aplicar `/{primary-cat-slug}/{main-city-slug}/{service-slug}/` para cada core service. Genera S LBS Pages en la Main City.

### §10.3 Output del paso

**Tipo:** Lista de S URLs (formato `/cat/city/service/`).

**Ejemplo (Cerrajeros Madrid 24h):** `/cerrajero/madrid/cerrajero-urgente/`, `/cerrajero/madrid/apertura-puertas/`, etc.

## §11 Additional Category URL pattern

### §11.1 Explicación

**Explicación**

Las categorías adicionales que no están cubiertas por un core service usan el mismo patrón local.

**Patrón o fórmula**

```text
/[category]/[main-city]/[additional-category-slug]/
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Duplicado de llaves usa /cerrajero/madrid/duplicado-llaves/.
```

**Ejemplos incorrectos**

```text
- /duplicado-llaves-madrid/
- /cerrajero/duplicado-llaves/
- /madrid-duplicado-llaves/
- /cerrajero/madrid/duplicado-llaves/
- /duplicado-llaves/
- /cerrajero/duplicado-llaves/ sin ciudad
```

**Regla final**

```text
Additional Category Page sigue `/{primary-cat-slug}/{main-city-slug}/{additional-slug}/` — mismo patrón que LBS.
```

**Validación operativa**

Las categorías adicionales efectivas usan el mismo patrón que una página servicio+ciudad, porque su función es dar soporte local a una categoría GBP secundaria.

### §11.2 Cómo obtenemos el Additional Category URL pattern

**Fuente:** GMB Crush.

**Método:** Aplicar `/{primary-cat-slug}/{main-city-slug}/{additional-slug}/` para cada Additional Category que necesita página propia (Paso 1 §10, A categorías efectivas). Slugs heredados del Paso 3 §7.

### §11.3 Output del paso

**Tipo:** Lista de A URLs (formato `/cat/city/additional/`).

**Ejemplo (Cerrajeros Madrid 24h):** `/cerrajero/madrid/duplicado-llaves/` (A=1).

## §12 GeoArticle URL pattern

### §12.1 Explicación

**Explicación**

Los GeoArticles son boosters semánticos y viven bajo la Main City.

**Patrón o fórmula**

```text
/[main-city]/[article-topic-slug]/
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
El artículo de coste usa /madrid/cuanto-cuesta-un-cerrajero-urgente/ y enlaza a /cerrajero/madrid/cerrajero-urgente/.
```

**Ejemplos incorrectos**

```text
- /blog/cerrajero-urgente-cost-madrid/
- /cerrajero/madrid/cerrajero-urgente/
- /articles/madrid-cerrajero-urgente-cost/
- /cuanto-cuesta-un-cerrajero-urgente-madrid/
- /cerrajero/madrid/cuanto-cuesta-un-cerrajero-urgente/ si complica la distinción de landing
- /cerrajero-urgente-cost-madrid/
- /blog/random-post-123/
```

**Regla final**

```text
GeoArticle sigue `/{main-city-slug}/{topic-slug}/` (Option A); Option B solo bajo Primary Category si está justificado.
```

**Validación operativa**

Los GeoArticles son contenido de soporte, no landings comerciales. Su URL debe reflejar un tema long-tail asociado a la Main City, sin competir con la página servicio+ciudad.

### §12.2 Cómo obtenemos el GeoArticle URL pattern

**Fuente:** GMB Crush.

**Método:** Aplicar Option A (`/{main-city-slug}/{topic-slug}/`) por defecto, u Option B (`/{primary-cat-slug}/{main-city-slug}/{topic-slug}/`) si el cliente quiere los GeoArticles bajo la Primary Category (override de diseño). Topics validados con keyword research (Paso 3 §21).

### §12.3 Output del paso

**Tipo:** Lista de G × S URLs (15 GeoArticles).

**Ejemplo (Cerrajeros Madrid 24h):** Option A → `/madrid/cuanto-cuesta-un-cerrajero-urgente/`, etc.

## §13 Local Coverage Areas no generan URLs

### §13.1 Explicación

**Explicación**

Las áreas de cobertura se mencionan en contenido y schema, pero no crean rutas.

**Patrón o fórmula**

```text
Local Coverage Area → mención de contenido | no URL base
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Almagro, Chamberí, Salamanca y Retiro se mencionan en contenido de Cerrajeros Madrid 24h, pero no se crean /almagro/ ni /cerrajero/almagro/... en fase base.
```

**Ejemplos incorrectos**

```text
- /almagro/ sin aprobación
- /cerrajero/almagro/cerrajero-urgente/ sin expansión
- /retiro/cuanto-tarda-un-cerrajero/ sin landing
- Crear una URL por cada área mencionada
- Enlazar a páginas inexistentes de cobertura
- Usar áreas de cobertura como Main City
```

**Regla final**

```text
Las Local Coverage Areas no generan URLs en la fase base; viven en contenido y schema `areaServed`.
```

**Validación operativa**

Las áreas de cobertura local pueden ser barrios, distritos o municipios cercanos, pero no generan URLs por defecto. Esta regla evita que el sistema base vuelva a multiplicarse sin necesidad.

### §13.2 Cómo obtenemos la decisión de LCAs sin URL

**Fuente:** GMB Crush ← heredado del Paso 1 §14 Local Coverage Areas.

**Método:** Las LCAs (Direct + Candidate) heredadas del Paso 1 NO se convierten en URLs en la fase base. Se mencionan en contenido y schema `areaServed` pero no como segmentos de path.

### §13.3 Output del paso

**Tipo:** 0 URLs adicionales por LCA.

**Ejemplo (Cerrajeros Madrid 24h):** Almagro, Chamberí, Salamanca, Retiro, etc. → ninguna `/almagro/`, `/chamberi/` en la URL Matrix.

## §14 Approved Expansion URLs

### §14.1 Explicación

**Explicación**

Una Approved Expansion Area puede usar los mismos patrones que la Main City, pero solo dentro del módulo de expansión.

**Patrón o fórmula**

```text
/[approved-area]/ + /[category]/[approved-area]/[service]/
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Si Almagro se aprueba después, Cerrajeros Madrid 24h puede crear /almagro/ y /cerrajero/almagro/cerrajero-urgente/ como expansión.
```

**Ejemplos incorrectos**

```text
- Crear expansión sin demanda
- Aprobar todas las zonas
- No diferenciar base y expansión
- Crear expansión sin justificación
- Mezclar expansión con fórmula base
- Crear páginas de expansión sin contenido único
```

**Regla final**

```text
Approved Expansion Areas generan URLs solo tras aprobación explícita y siguiendo los patrones del cluster.
```

**Validación operativa**

Si una Local Coverage Area pasa a Approved Expansion Area, entonces sí puede generar GeoHub, páginas servicio+zona y artículos. Pero ese módulo debe quedar separado de la base.

### §14.2 Cómo obtenemos las Approved Expansion URLs

**Fuente:** Decisión de diseño ← heredado del Paso 1 §15 Approved Expansion Areas.

**Método:** Si hay Approved Expansion Areas en Paso 1 §15, aplicar los mismos patrones del cluster con la zona aprobada como segmento. Por defecto E=0 en Phase 1 → no genera URLs.

### §14.3 Output del paso

**Tipo:** Lista de URLs de expansión (puede estar vacía).

**Ejemplo (Cerrajeros Madrid 24h):** Phase 1 sin expansion → 0 URLs.

## §15 No "near me" en URLs

### §15.1 Explicación

**Explicación**

Near me puede aparecer en FAQs o contenido, pero no en slugs principales.

**Patrón o fórmula**

```text
URL objetiva → servicio real → ciudad real
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Usar /cerrajero/madrid/cerrajero-urgente/ en vez de /best-cerrajero-urgente-near-me-madrid/.
```

**Ejemplos incorrectos**

```text
- /cerrajero/madrid/cerrajero-urgente-near-me/
- /near-me/cerrajero/
- /madrid/cerrajero-near-me/
- /best-cerrajero-madrid/
- /cheap-apertura-puertas-madrid/
```

**Regla final**

```text
Nunca usar `near-me` ni equivalentes (`cerca-de-mi`, `cerca-mi`) en ninguna URL.
```

**Validación operativa**

Near me, best, cheap o top-rated pueden aparecer en contenido si encajan, pero no deben formar parte de la arquitectura base. Son modificadores inestables y pueden debilitar la URL.

### §15.2 Cómo aplicamos la regla "No near-me"

**Fuente:** GMB Crush.

**Método:** Validar cada URL candidata contra patrones prohibidos: `near-me`, `cerca-de-mi`, `cerca-mi`, `near`, equivalentes. La intención `near-me` se sirve con la Main City + LBS, no con un slug literal.

### §15.3 Output del paso

**Tipo:** Validation flag — 0 URLs contienen `near-me` ni equivalentes.

**Ejemplo (Cerrajeros Madrid 24h):** Validado — ninguna URL del cluster contiene patrones prohibidos.

## §16 No adjetivos vacíos en URLs

### §16.1 Explicación

**Explicación**

Best, cheap y top-rated son modifiers comerciales, no arquitectura.

**Patrón o fórmula**

```text
URL objetiva → servicio real → ciudad real
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Usar /cerrajero/madrid/cerrajero-urgente/ en vez de /best-cerrajero-urgente-near-me-madrid/.
```

**Ejemplos incorrectos**

```text
- /best-apertura-puertas-madrid/
- /cheap-cerrajero-madrid/
- /top-rated-cerrajero-urgente-madrid/
- /cerrajero/madrid/cerrajero-urgente-near-me/
- /best-cerrajero-madrid/
- /cheap-apertura-puertas-madrid/
```

**Regla final**

```text
Nunca usar adjetivos vacíos (`best`, `cheap`, `top-rated`, `urgent-cheap`) en URLs.
```

**Validación operativa**

Near me, best, cheap o top-rated pueden aparecer en contenido si encajan, pero no deben formar parte de la arquitectura base. Son modificadores inestables y pueden debilitar la URL.

### §16.2 Cómo aplicamos la regla "No adjetivos vacíos"

**Fuente:** GMB Crush.

**Método:** Validar cada URL contra adjetivos vacíos: `best`, `cheap`, `top-rated`, `urgent-cheap`, `mejor`, `barato`, `top`. Estos términos no aportan SEO local y a menudo violan políticas de Google.

### §16.3 Output del paso

**Tipo:** Validation flag — 0 URLs contienen adjetivos vacíos.

**Ejemplo (Cerrajeros Madrid 24h):** Validado.

## §17 Slugs limpios

### §17.1 Explicación

**Explicación**

Los slugs deben ser humanos, minúsculos y sin símbolos.

**Patrón o fórmula**

```text
texto → lowercase → sin acentos → guiones medios → sin símbolos
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Chamberí se convierte en chamberi y Cerrajero urgente en cerrajero-urgente.
```

**Ejemplos incorrectos**

```text
- CerrajeroUrgentee
- cerrajero_urgente
- urgente%20cerrajero
- cerrajería-urgente
- /CerrajeroUrgentee/
- /cerrajero_urgente/
- /cerrajero-urgente!!!
```

**Regla final**

```text
Slugs limpios: lowercase, sin tildes, sin caracteres especiales, separados por guiones, derivados del nombre real.
```

**Validación operativa**

Los slugs deben ser legibles, estables y sin adornos. Minúsculas, guiones medios y sin símbolos es suficiente. Evita acentos, underscores, mayúsculas o palabras vacías innecesarias.

### §17.2 Cómo aplicamos la regla "Slugs limpios"

**Fuente:** GMB Crush ← heredado del Paso 2 §6 Slug Generation.

**Método:** Validar que cada slug aplica la transformación slugify estándar: lowercase + remove diacritics + replace non-alphanumeric con dash + collapse multiple dashes + trim. Slugs no derivados del nombre real se rechazan.

### §17.3 Output del paso

**Tipo:** Validation flag — todos los slugs cumplen la transformación.

**Ejemplo (Cerrajeros Madrid 24h):** Validado.

## §18 No falsa ubicación

### §18.1 Explicación

**Explicación**

Una URL o contenido no debe fingir oficina física.

**Patrón o fórmula**

```text
Service area ≠ physical office
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Atendemos clientes en Almagro
```

**Ejemplos incorrectos**

```text
- Nuestra oficina en Almagro si no existe
- Visita nuestra tienda en Salamanca si no existe
- Schema address en Chamberí sin oficina
```

**Regla final**

```text
Nunca inventar ubicación física en URLs — si no hay oficina en X, no se crea `/x/`.
```

**Validación operativa**

La regla aplica como filtro pre-publicación: para cada URL candidata, validar que la zona mencionada en el path corresponde a una ubicación física real (Paso 1 §12 Physical Location City) o a una Approved Expansion Area aprobada (Paso 1 §15). URLs que implican presencia en zonas donde el negocio solo opera remotamente o no opera en absoluto se rechazan.

### §18.2 Cómo aplicamos la regla "No falsa ubicación"

**Fuente:** GMB Crush ← heredado del Paso 1 §12 Physical Location City + §15 Approved Expansion.

**Método:** Para cada URL candidata cuya path implique una zona (LBS, Additional, GeoArticle), validar que la zona corresponde a (a) la Main City del NAP, (b) una Approved Expansion Area, o (c) ninguna ubicación implícita (caso de patterns sin segmento city). URLs que sugieren oficina física en zonas no declaradas se rechazan.

### §18.3 Output del paso

**Tipo:** Validation flag — 0 URLs implican falsa ubicación.

**Ejemplo (Cerrajeros Madrid 24h):** Validado — todas las URLs city son `/madrid/...` (NAP), no `/almagro/...` (LCA sin oficina).

## §19 No duplicar intención

### §19.1 Explicación

**Explicación**

Cada URL debe atacar una intención única.

**Patrón o fórmula**

```text
One URL = one primary intent
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/cerrajero/madrid/cerrajero-urgente/ cubre cerrajero urgente en Madrid
```

**Ejemplos incorrectos**

```text
- /madrid/cerrajero-urgente/ compitiendo con la landing
- /cerrajero/madrid/cerrajero-urgente/
- /cerrajero-urgente-madrid/
```

**Regla final**

```text
Una intención local = una sola URL principal. No duplicar variaciones que compitan entre sí.
```

**Validación operativa**

La regla aplica como filtro de detección de duplicados antes de cerrar la URL Matrix. Para cada par de URLs candidatas, validar que NO compartan intención local + servicio. Si dos URLs compiten en el mismo nicho semántico (ej. `/cerrajero/madrid/cerrajero-urgente/` y `/cerrajero/madrid/urgencias-cerrajero/`), consolidar en una y redirigir 301 la otra.

### §19.2 Cómo aplicamos la regla "No duplicar intención"

**Fuente:** GMB Crush.

**Método:** Para cada par de URLs en el cluster, validar que NO compitan en la misma intención local + servicio. Si dos URLs cubren la misma necesidad de búsqueda con slugs distintos, consolidar en la canónica y redirigir 301 la duplicada.

### §19.3 Output del paso

**Tipo:** Validation flag — 0 pares de URLs con intención duplicada.

**Ejemplo (Cerrajeros Madrid 24h):** Validado — no hay duplicación entre core services y additional categories.

## §20 Estructura final aprobada

```text
Homepage:
/ 

Service Overview:
/cerrajero/cerrajero-urgente/
/cerrajero/apertura-puertas/
/cerrajero/cambio-cerraduras/
/cerrajero/cambio-bombines/
/cerrajero/instalacion-cerraduras-seguridad/

Main City GeoHub:
/madrid/

Main City Location-Based Service:
/cerrajero/madrid/cerrajero-urgente/
/cerrajero/madrid/apertura-puertas/
/cerrajero/madrid/cambio-cerraduras/
/cerrajero/madrid/cambio-bombines/
/cerrajero/madrid/instalacion-cerraduras-seguridad/

Main City Additional Category:
/cerrajero/madrid/duplicado-llaves/

GeoArticles de la Main City:
/madrid/cuanto-cuesta-un-cerrajero-urgente/
/madrid/que-hacer-si-no-puedes-entrar-casa/
/madrid/cuanto-tarda-un-cerrajero/
```

## §21 URLs no aprobadas en la fase base

```text
/almagro/
/cerrajero/almagro/cerrajero-urgente/
/chamberi/
/cerrajero/salamanca/apertura-puertas/
/retiro/cuanto-cuesta-un-cerrajero-urgente/
```

Estas URLs solo se crearían como Approved Expansion Areas.

# Bloque III — Checklist Final

## §22 Checklist final del Paso 4

| Check | Pregunta | Estado |
|---|---|---|
| Dominio canónico | ¿Todas las URLs usan la misma versión del dominio? | ✅ / ⬜ |
| Trailing slash | ¿Todas las URLs siguen la misma convención? | ✅ / ⬜ |
| Homepage | ¿La homepage es `/`? | ✅ / ⬜ |
| Service Overview | ¿Las páginas de servicio no llevan ciudad? | ✅ / ⬜ |
| GeoHub | ¿El GeoHub usa la Main City? | ✅ / ⬜ |
| Location-Based Service | ¿La URL usa /category/main-city/service/? | ✅ / ⬜ |
| Additional Category | ¿La categoría adicional efectiva tiene URL local? | ✅ / ⬜ |
| GeoArticle | ¿El artículo usa /main-city/topic/? | ✅ / ⬜ |
| Local Coverage | ¿Las áreas cubiertas no generan URLs por defecto? | ✅ / ⬜ |
| Expansion | ¿Las áreas con URL están aprobadas? | ✅ / ⬜ |
| No near-me | ¿No hay near-me en slugs principales? | ✅ / ⬜ |
| No false location | ¿No se afirma ubicación física falsa? | ✅ / ⬜ |
| No duplicate intent | ¿Cada intención tiene una sola URL principal? | ✅ / ⬜ |

# Bloque IV — Outputs consolidados

## §23 Outputs del Paso 4

| # | Output | §X | Tipo |
|---|---|---|---|
| 1 | Canonical Domain | §5 | URL canónica única |
| 2 | Trailing Slash | §6 | Boolean (Yes/No) global |
| 3 | Homepage URL | §7 | Path constante (`/`) |
| 4 | Service Overview URL pattern | §8 | Patrón string |
| 5 | Main City GeoHub URL Style | §9 | Patrón string (Option A/B) |
| 6 | Location-Based Service URL pattern | §10 | Patrón string |
| 7 | Additional Category URL pattern | §11 | Patrón string |
| 8 | GeoArticle URL pattern | §12 | Patrón string (Option A/B) |
| 9 | Regla LCAs sin URL | §13 | Regla de doctrina |
| 10 | Approved Expansion URLs | §14 | Lista de URLs (puede estar vacía) |
| 11 | Validación No "near me" | §15 | Validation flag |
| 12 | Validación No adjetivos vacíos | §16 | Validation flag |
| 13 | Validación Slugs limpios | §17 | Validation flag |
| 14 | Validación No falsa ubicación | §18 | Validation flag |
| 15 | Validación No duplicar intención | §19 | Validation flag |

---

# Bloque V — Fuentes Internas GMB Crush Usadas

# §24 Fuentes internas GMB Crush usadas

- Analysis Framework.pdf
- GMB CRUSH Universal AI Local SEO Framework Template
- Website Homepage AI Optimization Prompts/Framework
- Service Pages AI Optimization Prompts/Framework
- Location Pages AI Optimization Prompts/Framework
- GeoHub Pages AI Framework
- GeoArticle Pages AI Framework
- Additional Categories Pages AI Framework

### §24.1 GeoArticles completos (15)

> **Aviso de trazabilidad:** estos 15 títulos son un primer borrador derivado de la fórmula G × S = 15 y de la lógica del servicio. **No vienen de keyword research real**. Antes de producirlos hay que validar volumen de búsqueda, dificultad y oportunidad competitiva por título. La fórmula garantiza la cantidad; los temas concretos requieren validación.

**Cerrajero urgente (3):**
1. /madrid/cuanto-cuesta-un-cerrajero-urgente/
2. /madrid/que-hacer-si-no-puedes-entrar-casa/
3. /madrid/cuanto-tarda-un-cerrajero/

**Apertura de puertas (3):**
4. /madrid/cuanto-cuesta-abrir-una-puerta/
5. /madrid/que-hacer-si-te-dejas-las-llaves-dentro/
6. /madrid/apertura-de-puertas-sin-romper-cerradura/

**Cambio de cerraduras (3):**
7. /madrid/cuando-cambiar-la-cerradura-de-casa/
8. /madrid/cambio-de-cerradura-tras-perder-llaves/
9. /madrid/cerradura-nueva-o-reparacion/

**Cambio de bombines (3):**
10. /madrid/cuando-cambiar-el-bombin/
11. /madrid/bombin-antibumping-madrid/
12. /madrid/cambio-de-bombin-sin-cambiar-cerradura/

**Instalación de cerraduras de seguridad (3):**
13. /madrid/mejores-cerraduras-de-seguridad-para-viviendas/
14. /madrid/cerraduras-de-seguridad-para-comunidades/
15. /madrid/instalar-cerradura-de-seguridad-en-puerta-blindada/
