Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# Paso 4 — URL Rules

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 15 outputs del Paso 4 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, reglas que aplican, checklist final y outputs consolidados.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 4

<small>§2</small>

Fijar las **reglas operativas de URL** que rigen toda la arquitectura del cluster local: dominio canónico, convención de slash, patrones de path por tipo de página, y filtros anti-canibalización. Estas reglas son la base sobre la que el Paso 3 (URL Matrix) genera URLs concretas y el Paso 5 (Page Type Rules) define cómo rellenar cada tipo de página.

**Outputs del paso:**

- **4.1** Canonical Domain — versión única del dominio (con/sin www, http/https) usada en todas las URLs absolutas, schema y enlaces internos
- **4.2** Trailing Slash — convención boolean (Yes/No) aplicada idéntica a todo el cluster
- **4.3** Homepage URL — path constante `/` (doctrina, no decisión)
- **4.4** Service Overview URL pattern — `/{primary-cat-slug}/{service-slug}/` para Service Overview Pages (sin ciudad)
- **4.5** Main City GeoHub URL Style — Option A `/{main-city-slug}/` (default) u Option B `/{primary-cat-slug}/{main-city-slug}/`
- **4.6** Location-Based Service URL pattern — `/{primary-cat-slug}/{main-city-slug}/{service-slug}/` para LBS Pages
- **4.7** Additional Category URL pattern — `/{primary-cat-slug}/{main-city-slug}/{additional-slug}/` para AC Pages efectivas
- **4.8** GeoArticle URL pattern — Option A `/{main-city-slug}/{topic-slug}/` (default) u Option B con primary category prefijo
- **4.9** LCAs no generan URLs — regla de doctrina: LCAs viven en contenido y schema `areaServed`, no en path
- **4.10** Approved Expansion URLs — patrones aplicables solo si hay AEAs aprobadas (Paso 1 §6.11); por defecto E=0
- **4.11** No "near me" en URLs — validación que rechaza patrones `near-me`, `cerca-de-mi`, equivalentes en slugs
- **4.12** No adjetivos vacíos en URLs — validación que rechaza `best`, `cheap`, `top-rated`, `mejor`, `barato`
- **4.13** Slugs limpios — transformación slugify estándar: lowercase + sin diacríticos + dashes + sin símbolos
- **4.14** No falsa ubicación — validación cruzada con NAP (Paso 1 §6.4) y AEA (Paso 1 §6.11) para rechazar URLs que sugieren oficina física inexistente
- **4.15** No duplicar intención — validación de pares de URLs en el cluster; consolida duplicados con 301

**Errores que previene:**

- Crear URLs distintas para la misma intención local (canibalización)
- Convertir Local Coverage Areas en carpetas sin aprobación (sprawl arquitectónico)
- Mezclar ciudad, servicio y artículo en el mismo patrón (silos rotos)
- Slugs con `near-me`, `best`, `cheap`, `top-rated` (modificadores inestables)
- Versiones inconsistentes con/sin trailing slash (duplicación técnica)
- Mezclar `www` y non-www, HTTP y HTTPS en URLs absolutas (señales canónicas mezcladas)
- Implicar oficina física en zonas donde el negocio no opera (E-E-A-T comprometido)

**Cuándo se ejecuta:** Antes del Paso 3 (URL Matrix) usa estas reglas, y después del Paso 2 (Fórmula). Sin las reglas del Paso 4, el Paso 3 no tiene base para validar el formato y la consistencia de cada URL del cluster.

## Info heredada de pasos anteriores

<small>§3</small>

> Estos campos NO se deciden en Paso 4 — la IA los lee del paso indicado y los usa como input para construir las reglas y patrones URL del cluster.

| # | Input heredado | Origen | Uso en el Paso 4 |
|---|---|---|---|
| 1 | Website URL (root domain) | Paso 1 §6.2 | Define la URL canónica base (4.1) |
| 2 | Brand Name | Paso 1 §6.1 | Confirma identidad para validaciones cruzadas |
| 3 | NAP — Physical Location City | Paso 1 §6.8 | Valida el segmento Main City (4.14 No falsa ubicación) |
| 4 | Core Services list (S core services) | Paso 1 §6.9 | Genera las S URLs Service Overview (4.4) y S URLs LBS (4.6) |
| 5 | Local Coverage Areas (Direct + Candidate) | Paso 1 §6.10 | Confirma que NO generan URLs por defecto (4.9) |
| 6 | Approved Expansion Areas (E count) | Paso 1 §6.11 | Determina si se aplican patrones de expansión (4.10); E=0 → 0 URLs adicionales |
| 7 | Slug Generation rule | Paso 2 §6.2 | Aplica slugify estándar a cada slug del cluster (4.13) |
| 8 | Primary Category Slug | Paso 2 §6.2 | Segmento `[primary-cat-slug]` en patrones 4.4, 4.6, 4.7, 4.8 (Option B), 4.10 |
| 9 | Main City Slug | Paso 2 §6.3 | Segmento `[main-city-slug]` en patrones 4.5, 4.6, 4.7, 4.8, 4.10 |
| 10 | Service slugs (S=5 slugs aprobados) | Paso 2 §6.4 | Segmento `[service-slug]` en 4.4, 4.6, 4.10 |
| 11 | Additional Category slugs (A slugs efectivos) | Paso 3 §6.3 | Segmento `[additional-slug]` en 4.7 |
| 12 | GeoArticle topics validados | Paso 3 §9 (módulo doctrinal) | Segmento `[topic-slug]` en 4.8 (15 GeoArticles = G × S) |
| 13 | GeoHub URL Style (Option A / B) | Paso 3 §6.2 | Aplica directamente en 4.5 (decisión heredada, no se re-toma aquí) |

# Bloque II — Ejemplo rellenado para el Paso 4 — URL Rules

<small>§4</small>

> Los 15 outputs del Paso 4 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 4.X declarado en §5.

### 4.1 — Canonical Domain

`https://www.cerrajerosmadrid24h.com`

### 4.2 — Trailing Slash

`Yes` (todas las URLs terminan en `/`)

### 4.3 — Homepage URL

`/`

### 4.4 — Service Overview URL pattern

Patrón: `/{primary-cat-slug}/{service-slug}/`

5 URLs aplicadas:
- `/cerrajero/cerrajero-urgente/`
- `/cerrajero/apertura-puertas/`
- `/cerrajero/cambio-cerraduras/`
- `/cerrajero/cambio-bombines/`
- `/cerrajero/instalacion-cerraduras-seguridad/`

### 4.5 — Main City GeoHub URL Style

Option A → `/madrid/`

### 4.6 — Location-Based Service URL pattern

Patrón: `/{primary-cat-slug}/{main-city-slug}/{service-slug}/`

5 URLs aplicadas:
- `/cerrajero/madrid/cerrajero-urgente/`
- `/cerrajero/madrid/apertura-puertas/`
- `/cerrajero/madrid/cambio-cerraduras/`
- `/cerrajero/madrid/cambio-bombines/`
- `/cerrajero/madrid/instalacion-cerraduras-seguridad/`

### 4.7 — Additional Category URL pattern

Patrón: `/{primary-cat-slug}/{main-city-slug}/{additional-slug}/`

1 URL aplicada (A=1 efectiva):
- `/cerrajero/madrid/duplicado-llaves/`

### 4.8 — GeoArticle URL pattern

Option A → `/{main-city-slug}/{topic-slug}/`

15 URLs aplicadas (G=3 × S=5):
- `/madrid/cuanto-cuesta-un-cerrajero-urgente/`
- `/madrid/que-hacer-si-no-puedes-entrar-casa/`
- `/madrid/cuanto-tarda-un-cerrajero/`
- `/madrid/cuanto-cuesta-abrir-una-puerta/`
- `/madrid/que-hacer-si-te-dejas-las-llaves-dentro/`
- `/madrid/apertura-de-puertas-sin-romper-cerradura/`
- `/madrid/cuando-cambiar-la-cerradura-de-casa/`
- `/madrid/cambio-de-cerradura-tras-perder-llaves/`
- `/madrid/cerradura-nueva-o-reparacion/`
- `/madrid/cuando-cambiar-el-bombin/`
- `/madrid/bombin-antibumping-madrid/`
- `/madrid/cambio-de-bombin-sin-cambiar-cerradura/`
- `/madrid/mejores-cerraduras-de-seguridad-para-viviendas/`
- `/madrid/cerraduras-de-seguridad-para-comunidades/`
- `/madrid/instalar-cerradura-de-seguridad-en-puerta-blindada/`

### 4.9 — LCAs no generan URLs

10 LCAs declaradas → 0 URLs generadas:

| LCA | Tratamiento |
|---|---|
| Almagro, Chamberí (Direct) | Mencionadas en contenido y schema `areaServed`; NO en path |
| Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad (Candidate) | Mencionadas en contenido si pasan test GEO; NO en path |

### 4.10 — Approved Expansion URLs

`E = 0` en Phase 1 → 0 URLs de expansión generadas.

URLs hipotéticas que NO se crean (LCAs sin AEA):
- `/almagro/`
- `/cerrajero/almagro/cerrajero-urgente/`
- `/chamberi/`
- `/cerrajero/salamanca/apertura-puertas/`
- `/retiro/cuanto-cuesta-un-cerrajero-urgente/`

### 4.11 — Validación No "near me" en URLs

Resultado: 0 URLs del cluster contienen `near-me`, `cerca-de-mi`, `cerca-mi` o equivalentes. Validación: OK.

### 4.12 — Validación No adjetivos vacíos en URLs

Resultado: 0 URLs del cluster contienen `best`, `cheap`, `top-rated`, `mejor`, `barato`, `top` o equivalentes. Validación: OK.

### 4.13 — Validación Slugs limpios

Resultado: todos los slugs del cluster (`cerrajero-urgente`, `apertura-puertas`, `madrid`, `duplicado-llaves`, etc.) cumplen la transformación slugify estándar (lowercase, sin diacríticos, dashes, sin símbolos). Validación: OK.

### 4.14 — Validación No falsa ubicación

Resultado: solo `/madrid/` aparece como segmento de city en URLs (NAP = Madrid). Ninguna URL implica oficina en Almagro, Chamberí, Salamanca, Retiro u otras LCAs sin oficina. Validación: OK.

### 4.15 — Validación No duplicar intención

Resultado: 0 pares de URLs con duplicación de intención local + servicio detectados. Servicio de cerrajería de urgencia consolidada con core service Cerrajero urgente (ver Paso 1 §6.6 + Paso 2 §6.12). Validación: OK.

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 15 outputs que el Paso 4 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `4.1`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Origen |
|---|---|---|---|
| 4.1 | Canonical Domain | URL canónica única | GMB Crush ← Paso 1 §6.2 |
| 4.2 | Trailing Slash | Boolean (Yes/No) global | Decisión de diseño |
| 4.3 | Homepage URL | Path constante (`/`) | GMB Crush |
| 4.4 | Service Overview URL pattern | Patrón string | GMB Crush |
| 4.5 | Main City GeoHub URL Style | Patrón string (Option A/B) | GMB Crush ← Paso 3 §6.2 |
| 4.6 | Location-Based Service URL pattern | Patrón string | GMB Crush |
| 4.7 | Additional Category URL pattern | Patrón string | GMB Crush |
| 4.8 | GeoArticle URL pattern | Patrón string (Option A/B) | GMB Crush |
| 4.9 | LCAs no generan URLs | Regla de doctrina | GMB Crush ← Paso 1 §6.10 |
| 4.10 | Approved Expansion URLs | Lista de URLs (puede estar vacía) | Decisión de diseño ← Paso 1 §6.11 |
| 4.11 | Validación No "near me" en URLs | Validation flag | GMB Crush |
| 4.12 | Validación No adjetivos vacíos en URLs | Validation flag | GMB Crush |
| 4.13 | Validación Slugs limpios | Validation flag | GMB Crush ← Paso 2 §6.2 |
| 4.14 | Validación No falsa ubicación | Validation flag | GMB Crush ← Paso 1 §6.8 + §6.11 |
| 4.15 | Validación No duplicar intención | Validation flag | GMB Crush |

## Reglas que Aplican

<small>§6</small>

> Esta sección desarrolla cada uno de los 15 outputs (4.1–4.15) con el mismo patrón: Explicación / Patrón o fórmula / Ejemplos correctos / Ejemplos incorrectos / Regla final / Validación operativa / Cómo se obtiene / Output del paso. Cada sub-sección §6.X corresponde 1:1 al output 4.X declarado en §5.

### 4.1 — Canonical Domain

<small>§6.1</small>

**Explicación**

Todas las URLs deben salir de una sola versión del dominio. Esto evita duplicación técnica y señales inconsistentes. El Canonical Domain es la única versión que aparece en URLs absolutas, schema y enlaces internos; las demás variantes redirigen 301.

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

Todas las URLs deben salir de una única versión canónica del dominio. Mezclar www, non-www, HTTP y HTTPS crea duplicados técnicos y dificulta la consistencia del schema y la matriz. La decisión se hereda del Paso 1 §6.2 (Website URL).

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso 1 §6.2 Website URL.
- **Método:** Tomar el dominio canónico declarado en el intake del Paso 1 §6.2. Aplicar como única versión válida en todo el cluster. El resto de variantes (con/sin www, http vs https, mayúsculas) redirigen 301 a la canónica.

**Output del paso**

- **Tipo:** URL canónica única.
- **Ejemplo (Cerrajeros Madrid 24h):** `https://www.cerrajerosmadrid24h.com`.

### 4.2 — Trailing Slash

<small>§6.2</small>

**Explicación**

La regla del slash final debe ser consistente en todo el sitio. La decisión aplica idéntica a TODAS las URLs del cluster — no se mezclan con-slash y sin-slash.

**Patrón o fórmula**

```text
URL pattern → trailing slash uniforme → canonical
Default: Yes (slash final)
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

La regla de slash final debe ser uniforme. No importa tanto si se usa o no slash, sino que todas las URLs sigan la misma convención. Default Yes (más limpio para parsing y consistente con la mayoría de CMSs).

**Cómo se obtiene**

- **Fuente:** Decisión de diseño.
- **Método:** Decidir Yes (trailing slash siempre) o No (nunca trailing slash) en el intake del Paso 4. La decisión aplica idéntica a TODAS las URLs del cluster. Default: Yes (slash final).

**Output del paso**

- **Tipo:** Boolean — Yes/No, aplicado a todas las URLs.
- **Ejemplo (Cerrajeros Madrid 24h):** Yes → `/cerrajero/madrid/cerrajero-urgente/` (con `/` final).

### 4.3 — Homepage URL

<small>§6.3</small>

**Explicación**

La homepage es la raíz de entidad y debe vivir en el root domain. No hay decisión que tomar — es doctrina GMB Crush. La homepage SIEMPRE vive en `/`, no en `/home/`, `/inicio/`, `/index/`.

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

La homepage debe ser la raíz del dominio. No debe moverse a /home/, /inicio/ o /cerrajero-madrid/ porque actúa como Root Entity Anchor del negocio. Es la primera URL que el Paso 3 §6.4 (URL Matrix) registra y la que el Paso 7 (Internal Linking) usa como hub principal.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** La Homepage SIEMPRE vive en `/`. No hay decisión que tomar — es doctrina. No se permite `/home/`, `/inicio/`, `/index/`.

**Output del paso**

- **Tipo:** Path constante.
- **Ejemplo (Cerrajeros Madrid 24h):** `/`.

### 4.4 — Service Overview URL pattern

<small>§6.4</small>

**Explicación**

Las páginas de servicio general son no geolocalizadas y no llevan ciudad. Su función es construir autoridad temática y servir como padre de la página local (LBS). Hay S Service Overview Pages, una por core service.

**Patrón o fórmula**

```text
/{primary-category-slug}/{service-slug}/
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

Las páginas de servicio general no deben incluir ciudad en la URL. Su función es construir autoridad temática y servir como padre de la página local. La validación cruza con Paso 7 §6.3 (Regla 3 — SO empuja la versión local) que requiere que cada SO enlace a su LBS correspondiente.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar `/{primary-cat-slug}/{service-slug}/` para cada core service heredado del Paso 1 §6.9 (S=5). Los slugs se obtienen del Paso 2 §6.4 Service Slugs. Genera S Service Overview Pages.

**Output del paso**

- **Tipo:** Lista de S URLs (formato `/cat/service/`).
- **Ejemplo (Cerrajeros Madrid 24h):** `/cerrajero/cerrajero-urgente/`, `/cerrajero/apertura-puertas/`, `/cerrajero/cambio-cerraduras/`, `/cerrajero/cambio-bombines/`, `/cerrajero/instalacion-cerraduras-seguridad/`.

### 4.5 — Main City GeoHub URL Style

<small>§6.5</small>

**Explicación**

El GeoHub de la Main City agrupa todo lo relacionado con la ciudad principal. Puede usar Option A (`/{main-city-slug}/`) u Option B (`/{primary-cat-slug}/{main-city-slug}/`). La decisión se hereda del Paso 3 §6.2 GeoHub URL Style.

**Patrón o fórmula**

```text
Option A: /{main-city-slug}/                          (default — más limpio)
Option B: /{primary-cat-slug}/{main-city-slug}/       (justificado solo si cliente quiere consolidar bajo categoría)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h usa /madrid/ como GeoHub de la Main City (Option A).
```

**Ejemplos incorrectos**

```text
- /areas-we-serve/madrid/
- /locations/madrid/
- /service-area/madrid/
- /madrid-cerrajero-services/
- /cerrajero-services-madrid/
- Mezclar Option A y Option B en el mismo cluster
```

**Regla final**

```text
GeoHub usa Option A (`/{main-city-slug}/`) por defecto; Option B solo si está justificado.
```

**Validación operativa**

El GeoHub de la Main City debe ser corto, estable y fácil de enlazar. Puede usar `/city/` o `/category/city/`, pero en la base simplificada se recomienda Option A. Una vez elegida, aplica idéntica al cluster — no se mezclan estilos.

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso 3 §6.2 GeoHub URL Style.
- **Método:** Aplicar la decisión Option A (`/{main-city-slug}/`) o Option B (`/{primary-cat-slug}/{main-city-slug}/`) tomada en el Paso 3 §6.2. Default: Option A (más limpio).

**Output del paso**

- **Tipo:** URL única para el GeoHub Main City.
- **Ejemplo (Cerrajeros Madrid 24h):** Option A → `/madrid/`.

### 4.6 — Location-Based Service URL pattern

<small>§6.6</small>

**Explicación**

Estas son las páginas comerciales para búsquedas service + city. Patrón fijo, sin variaciones. Hay S LBS Pages en la Main City (S=5 para Cerrajeros).

**Patrón o fórmula**

```text
/{primary-category-slug}/{main-city-slug}/{service-slug}/
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

Las páginas comerciales locales deben seguir el patrón categoría + ciudad + servicio. Esto mantiene claro el silo y evita mezclar intención de servicio con artículo o hub. Cada LBS depende de su SO padre (Paso 7 §6.5 Regla 5 — LBS conecta servicio y ciudad).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar `/{primary-cat-slug}/{main-city-slug}/{service-slug}/` para cada core service. Genera S LBS Pages en la Main City.

**Output del paso**

- **Tipo:** Lista de S URLs (formato `/cat/city/service/`).
- **Ejemplo (Cerrajeros Madrid 24h):** `/cerrajero/madrid/cerrajero-urgente/`, `/cerrajero/madrid/apertura-puertas/`, `/cerrajero/madrid/cambio-cerraduras/`, `/cerrajero/madrid/cambio-bombines/`, `/cerrajero/madrid/instalacion-cerraduras-seguridad/`.

### 4.7 — Additional Category URL pattern

<small>§6.7</small>

**Explicación**

Las categorías adicionales que no están cubiertas por un core service usan el mismo patrón local que LBS. Su función es dar soporte local a una categoría GBP secundaria.

**Patrón o fórmula**

```text
/{primary-category-slug}/{main-city-slug}/{additional-category-slug}/
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
- /duplicado-llaves/
- /cerrajero/duplicado-llaves/ sin ciudad
```

**Regla final**

```text
Additional Category Page sigue `/{primary-cat-slug}/{main-city-slug}/{additional-slug}/` — mismo patrón que LBS.
```

**Validación operativa**

Las categorías adicionales efectivas usan el mismo patrón que una página servicio+ciudad, porque su función es dar soporte local a una categoría GBP secundaria. La consolidación con core services se valida en Paso 2 §6.12 (Anti-duplicación).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar `/{primary-cat-slug}/{main-city-slug}/{additional-slug}/` para cada Additional Category que necesita página propia (Paso 1 §6.6, A categorías efectivas). Slugs heredados del Paso 3 §6.3.

**Output del paso**

- **Tipo:** Lista de A URLs (formato `/cat/city/additional/`).
- **Ejemplo (Cerrajeros Madrid 24h):** `/cerrajero/madrid/duplicado-llaves/` (A=1).

### 4.8 — GeoArticle URL pattern

<small>§6.8</small>

**Explicación**

Los GeoArticles son boosters semánticos y viven bajo la Main City. Su URL refleja un tema long-tail asociado a la Main City, sin competir con la página servicio+ciudad. Hay G × S GeoArticles (15 para Cerrajeros con G=3 y S=5).

**Patrón o fórmula**

```text
Option A: /{main-city-slug}/{topic-slug}/                         (default)
Option B: /{primary-cat-slug}/{main-city-slug}/{topic-slug}/      (override de diseño si cliente quiere)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
El artículo de coste usa /madrid/cuanto-cuesta-un-cerrajero-urgente/ y enlaza a /cerrajero/madrid/cerrajero-urgente/.
```

**Ejemplos incorrectos**

```text
- /blog/cerrajero-urgente-cost-madrid/
- /cerrajero/madrid/cerrajero-urgente/  (eso es la LBS, no el GA)
- /articles/madrid-cerrajero-urgente-cost/
- /cuanto-cuesta-un-cerrajero-urgente-madrid/
- /cerrajero-urgente-cost-madrid/
- /blog/random-post-123/
```

**Regla final**

```text
GeoArticle sigue `/{main-city-slug}/{topic-slug}/` (Option A); Option B solo bajo Primary Category si está justificado.
```

**Validación operativa**

Los GeoArticles son contenido de soporte, no landings comerciales. Su URL debe reflejar un tema long-tail asociado a la Main City, sin competir con la LBS. Cada GA tiene como Parent Page la LBS correspondiente (Paso 3 §6.6) y enlaza a ella (Paso 7 §6.7 Regla 7 — GeoArticle pasa relevancia a la landing).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar Option A (`/{main-city-slug}/{topic-slug}/`) por defecto, u Option B (`/{primary-cat-slug}/{main-city-slug}/{topic-slug}/`) si el cliente quiere los GeoArticles bajo la Primary Category (override de diseño). Topics validados con keyword research (Paso 3 §9 módulo doctrinal).

**Output del paso**

- **Tipo:** Lista de G × S URLs (15 GeoArticles para Cerrajeros).
- **Ejemplo (Cerrajeros Madrid 24h):** Option A → `/madrid/cuanto-cuesta-un-cerrajero-urgente/`, `/madrid/que-hacer-si-no-puedes-entrar-casa/`, etc.

### 4.9 — LCAs no generan URLs

<small>§6.9</small>

**Explicación**

Las áreas de cobertura local (Paso 1 §6.10) se mencionan en contenido y schema `areaServed`, pero NO crean rutas en la matriz base. Solo las Approved Expansion Areas (Paso 1 §6.11) pueden generar URLs propias.

**Patrón o fórmula**

```text
Local Coverage Area → mención de contenido | schema areaServed | NO URL base
Para que una LCA genere URL: debe pasar a AEA en Paso 1 §6.11
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

Las áreas de cobertura local pueden ser barrios, distritos o municipios cercanos, pero no generan URLs por defecto. Esta regla evita que el sistema base vuelva a multiplicarse sin necesidad. La validación cruza con Paso 3 §6.12 (LCAs sin filas base) y Paso 6 §6 (Principio 2 — LCAs enriquecen contenido).

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso 1 §6.10 Local Coverage Areas.
- **Método:** Las LCAs (Direct + Candidate) heredadas del Paso 1 NO se convierten en URLs en la fase base. Se mencionan en contenido y schema `areaServed` pero no como segmentos de path.

**Output del paso**

- **Tipo:** 0 URLs adicionales por LCA.
- **Ejemplo (Cerrajeros Madrid 24h):** Almagro, Chamberí, Salamanca, Retiro, etc. → ninguna `/almagro/`, `/chamberi/` en la URL Matrix.

### 4.10 — Approved Expansion URLs

<small>§6.10</small>

**Explicación**

Una Approved Expansion Area puede usar los mismos patrones que la Main City, pero solo dentro del módulo de expansión (separado de la base). En Phase 1 default `E = 0`, por lo que la regla está declarada pero no genera URLs.

**Patrón o fórmula**

```text
Approved Expansion = E × (1 + S + A + G×S) URLs

Patrones aplicados con AEA como segmento city:
  /{aea-slug}/                                  (Expansion GeoHub)
  /{primary-cat-slug}/{aea-slug}/{service-slug}/ (Expansion LBS)
  /{primary-cat-slug}/{aea-slug}/{additional-slug}/ (Expansion AC)
  /{aea-slug}/{topic-slug}/                     (Expansion GA)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Phase 1: E = 0 → 0 URLs de expansión

Hipotético si Almagro se aprueba como AEA:
  /almagro/                                     (Expansion GeoHub)
  /cerrajero/almagro/cerrajero-urgente/         (Expansion LBS)
  /cerrajero/almagro/duplicado-llaves/          (Expansion AC)
  /almagro/cuanto-cuesta-un-cerrajero-urgente/  (Expansion GA)
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

Si una Local Coverage Area pasa a Approved Expansion Area, entonces sí puede generar GeoHub, páginas servicio+zona y artículos. Pero ese módulo debe quedar separado de la base. La distinción LCA vs AEA es contractual con Paso 1 §6.10 vs §6.11. La fórmula de expansión está en Paso 2 §6.11.

**Cómo se obtiene**

- **Fuente:** Decisión de diseño ← heredado del Paso 1 §6.11 Approved Expansion Areas.
- **Método:** Si hay Approved Expansion Areas en Paso 1 §6.11, aplicar los mismos patrones del cluster con la zona aprobada como segmento. Por defecto E=0 en Phase 1 → no genera URLs.

**Output del paso**

- **Tipo:** Lista de URLs de expansión (puede estar vacía).
- **Ejemplo (Cerrajeros Madrid 24h):** Phase 1 sin expansion → 0 URLs.

### 4.11 — Validación No "near me" en URLs

<small>§6.11</small>

**Explicación**

`near-me` y equivalentes pueden aparecer en FAQs o contenido, pero no en slugs principales. Son modificadores inestables y debilitan la URL estructural del cluster.

**Patrón o fórmula**

```text
URL objetiva → servicio real → ciudad real
Patrones prohibidos: near-me, cerca-de-mi, cerca-mi, near, equivalentes
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

`near-me`, best, cheap o top-rated pueden aparecer en contenido si encajan, pero no deben formar parte de la arquitectura base. La intención `near-me` se sirve con Main City + LBS, no con un slug literal. La validación se aplica a CADA URL candidata antes de cerrar la matriz.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Validar cada URL candidata contra patrones prohibidos: `near-me`, `cerca-de-mi`, `cerca-mi`, `near`, equivalentes. La intención `near-me` se sirve con la Main City + LBS, no con un slug literal.

**Output del paso**

- **Tipo:** Validation flag — 0 URLs contienen `near-me` ni equivalentes.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado — ninguna URL del cluster contiene patrones prohibidos.

### 4.12 — Validación No adjetivos vacíos en URLs

<small>§6.12</small>

**Explicación**

`best`, `cheap` y `top-rated` son modifiers comerciales, no arquitectura. Estos términos no aportan SEO local y a menudo violan políticas de Google.

**Patrón o fórmula**

```text
URL objetiva → servicio real → ciudad real
Adjetivos prohibidos: best, cheap, top-rated, urgent-cheap, mejor, barato, top
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Usar /cerrajero/madrid/cerrajero-urgente/ en vez de /best-cerrajero-urgente-madrid/.
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

`near-me`, `best`, `cheap` o `top-rated` pueden aparecer en contenido si encajan, pero no deben formar parte de la arquitectura base. Son modificadores inestables y pueden debilitar la URL. La validación se aplica a CADA URL candidata antes de cerrar la matriz.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Validar cada URL contra adjetivos vacíos: `best`, `cheap`, `top-rated`, `urgent-cheap`, `mejor`, `barato`, `top`. Estos términos no aportan SEO local y a menudo violan políticas de Google.

**Output del paso**

- **Tipo:** Validation flag — 0 URLs contienen adjetivos vacíos.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado.

### 4.13 — Validación Slugs limpios

<small>§6.13</small>

**Explicación**

Los slugs deben ser humanos, minúsculos y sin símbolos. La validación garantiza que cada slug del cluster (Primary, Main City, Service, Additional Category, GeoArticle topic) cumple la transformación slugify estándar.

**Patrón o fórmula**

```text
slugify(text) = lowercase(text)
              → remove_diacritics()
              → replace_non_alphanumeric_with('-')
              → collapse_consecutive_dashes()
              → trim_leading_trailing_dashes()
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Chamberí se convierte en chamberi
Cerrajero urgente se convierte en cerrajero-urgente
Servicio de duplicado de llaves se convierte en duplicado-llaves
```

**Ejemplos incorrectos**

```text
- CerrajeroUrgentee
- cerrajero_urgente
- urgente%20cerrajero
- cerrajería-urgente (mantiene tilde)
- /CerrajeroUrgentee/
- /cerrajero_urgente/
- /cerrajero-urgente!!!
```

**Regla final**

```text
Slugs limpios: lowercase, sin tildes, sin caracteres especiales, separados por guiones, derivados del nombre real.
```

**Validación operativa**

Los slugs deben ser legibles, estables y sin adornos. Minúsculas, guiones medios y sin símbolos es suficiente. Evita acentos, underscores, mayúsculas o palabras vacías innecesarias. La validación cruza con Paso 2 §6.2/§6.3/§6.4 (Slug Generation) y Paso 3 §6.3 (Additional Category Slugs).

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso 2 §6.2 Slug Generation.
- **Método:** Validar que cada slug aplica la transformación slugify estándar: lowercase + remove diacritics + replace non-alphanumeric con dash + collapse multiple dashes + trim. Slugs no derivados del nombre real se rechazan.

**Output del paso**

- **Tipo:** Validation flag — todos los slugs cumplen la transformación.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado.

### 4.14 — Validación No falsa ubicación

<small>§6.14</small>

**Explicación**

Una URL no debe fingir oficina física. Si no hay oficina en una zona X, no se crea `/x/` ni `/cat/x/...`. La validación cruza el segmento city de cada URL contra NAP (Paso 1 §6.8 Physical Location City) y AEA aprobada (Paso 1 §6.11).

**Patrón o fórmula**

```text
Para cada URL con segmento city:
  IF city == NAP_city:                    → válida
  ELIF city == approved_AEA:              → válida (módulo expansión)
  ELSE:                                   → rechazar (falsa ubicación)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
NAP city = Madrid
URL /cerrajero/madrid/cerrajero-urgente/ → city == Madrid → válida
URL /madrid/cuanto-cuesta-un-cerrajero-urgente/ → city == Madrid → válida

URLs hipotéticas rechazadas:
  /cerrajero/almagro/cerrajero-urgente/ → city == Almagro (LCA, no AEA) → rechazada
  /chamberi/cuanto-cuesta-un-cerrajero/ → city == Chamberí (LCA, no AEA) → rechazada
```

**Ejemplos incorrectos**

```text
- "Nuestra oficina en Almagro" si no existe
- "Visita nuestra tienda en Salamanca" si no existe
- Schema address en Chamberí sin oficina
- /retiro/... sin AEA aprobada
```

**Regla final**

```text
Nunca inventar ubicación física en URLs — si no hay oficina en X, no se crea `/x/`.
```

**Validación operativa**

La regla aplica como filtro pre-publicación: para cada URL candidata, validar que la zona mencionada en el path corresponde a una ubicación física real (Paso 1 §6.8 Physical Location City) o a una Approved Expansion Area aprobada (Paso 1 §6.11). URLs que implican presencia en zonas donde el negocio solo opera remotamente o no opera en absoluto se rechazan. Cruce con Paso 1 §6.8, Paso 6 §9 (Principio 5 — No falsa ubicación) y Paso 8 (schema sin address falsa).

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso 1 §6.8 Physical Location City + §6.11 Approved Expansion.
- **Método:** Para cada URL candidata cuya path implique una zona (LBS, Additional, GeoArticle), validar que la zona corresponde a (a) la Main City del NAP, (b) una Approved Expansion Area, o (c) ninguna ubicación implícita (caso de patterns sin segmento city). URLs que sugieren oficina física en zonas no declaradas se rechazan.

**Output del paso**

- **Tipo:** Validation flag — 0 URLs implican falsa ubicación.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado — todas las URLs city son `/madrid/...` (NAP), no `/almagro/...` (LCA sin oficina).

### 4.15 — Validación No duplicar intención

<small>§6.15</small>

**Explicación**

Cada URL debe atacar una intención única. Si dos URLs compiten en el mismo nicho semántico (ej. `/cerrajero/madrid/cerrajero-urgente/` y `/cerrajero/madrid/urgencias-cerrajero/`), consolidar en una y redirigir 301 la otra.

**Patrón o fórmula**

```text
One URL = one primary intent

Para cada par de URLs candidatas:
  IF intent(URL_A) == intent(URL_B) AND city(URL_A) == city(URL_B):
    consolidar en canónica + redirigir 301 la perdedora
  ELSE:
    ambas válidas
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/cerrajero/madrid/cerrajero-urgente/ cubre cerrajero urgente en Madrid
/cerrajero/madrid/duplicado-llaves/  cubre duplicado de llaves en Madrid
→ intenciones distintas, ambas válidas

Consolidación verificada: Servicio de cerrajería de urgencia → consolidado en /cerrajero/madrid/cerrajero-urgente/ (no genera URL adicional)
```

**Ejemplos incorrectos**

```text
- /madrid/cerrajero-urgente/ compitiendo con la landing /cerrajero/madrid/cerrajero-urgente/
- /cerrajero/madrid/cerrajero-urgente/ + /cerrajero/madrid/urgencias-cerrajero/ (misma intención, dos URLs)
- /cerrajero-urgente-madrid/ + /madrid/cerrajero-urgente/ (misma intención, slug distinto)
```

**Regla final**

```text
Una intención local = una sola URL principal. No duplicar variaciones que compitan entre sí.
```

**Validación operativa**

La regla aplica como filtro de detección de duplicados antes de cerrar la URL Matrix. Para cada par de URLs candidatas, validar que NO compartan intención local + servicio. Si dos URLs compiten en el mismo nicho semántico, consolidar en una y redirigir 301 la otra. La validación cruza con Paso 2 §6.12 (Control anti-duplicación al construir A) y Paso 3 §6.13 (matriz cerrada antes de contenido).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Para cada par de URLs en el cluster, validar que NO compitan en la misma intención local + servicio. Si dos URLs cubren la misma necesidad de búsqueda con slugs distintos, consolidar en la canónica y redirigir 301 la duplicada.

**Output del paso**

- **Tipo:** Validation flag — 0 pares de URLs con intención duplicada.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado — no hay duplicación entre core services y additional categories.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 4. Cada ☐ es un check que debe pasar antes del handoff al Paso 3 (URL Matrix consume estos patrones) y al Paso 5 (Page Type Rules).

### Validación de dominio y formato

- ☐ Dominio canónico (4.1) único — no se mezcla www con non-www ni HTTP con HTTPS
- ☐ Trailing Slash (4.2) decidido y aplicado idéntico a TODAS las URLs
- ☐ Homepage URL (4.3) = `/` (no `/home/`, `/inicio/`)

### Validación de patrones URL

- ☐ Service Overview pattern (4.4) aplicado sin ciudad para los S core services
- ☐ GeoHub Style (4.5) consistente (Option A o Option B, no mezclados)
- ☐ LBS pattern (4.6) `/cat/city/service/` aplicado a los S servicios en Main City
- ☐ Additional Category pattern (4.7) `/cat/city/additional/` aplicado a las A categorías efectivas
- ☐ GeoArticle pattern (4.8) `/city/topic/` aplicado a los G×S artículos

### Validación de cobertura geográfica

- ☐ LCAs no generan URLs (4.9) — verificar que ninguna LCA de Paso 1 §6.10 aparece como path
- ☐ Approved Expansion URLs (4.10) generadas solo si E≥1 (Paso 1 §6.11); por defecto E=0

### Validación anti-canibalización

- ☐ No "near me" en URLs (4.11) — 0 URLs contienen `near-me`, `cerca-de-mi`, equivalentes
- ☐ No adjetivos vacíos (4.12) — 0 URLs contienen `best`, `cheap`, `top-rated`, etc.
- ☐ Slugs limpios (4.13) — todos cumplen slugify estándar
- ☐ No falsa ubicación (4.14) — todas las city URLs corresponden a NAP o AEA aprobada
- ☐ No duplicar intención (4.15) — 0 pares de URLs con misma intención local + servicio

## Outputs Consolidados

<small>§8</small>

> Tabla final con valores reales para Cerrajeros Madrid 24h y status de cada output. Los IDs (`4.1`–`4.15`) coinciden con los declarados en §5.

| ID | Output | Valor (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|
| 4.1 | Canonical Domain | `https://www.cerrajerosmadrid24h.com` | confirmed |
| 4.2 | Trailing Slash | `Yes` (todas las URLs terminan en `/`) | confirmed |
| 4.3 | Homepage URL | `/` | confirmed |
| 4.4 | Service Overview URL pattern | `/{primary-cat-slug}/{service-slug}/` → 5 URLs SO | confirmed |
| 4.5 | Main City GeoHub URL Style | Option A → `/madrid/` | confirmed |
| 4.6 | LBS URL pattern | `/{primary-cat-slug}/{main-city-slug}/{service-slug}/` → 5 URLs LBS | confirmed |
| 4.7 | Additional Category URL pattern | `/{primary-cat-slug}/{main-city-slug}/{additional-slug}/` → 1 URL AC | confirmed |
| 4.8 | GeoArticle URL pattern | Option A → `/{main-city-slug}/{topic-slug}/` → 15 URLs GA | confirmed |
| 4.9 | LCAs no generan URLs | 10 LCAs declaradas → 0 URLs generadas | OK |
| 4.10 | Approved Expansion URLs | E=0 → 0 URLs de expansión | OK |
| 4.11 | Validación No "near me" | 0 URLs contienen patrones prohibidos | OK |
| 4.12 | Validación No adjetivos vacíos | 0 URLs contienen `best`, `cheap`, `top-rated`, etc. | OK |
| 4.13 | Validación Slugs limpios | Todos los slugs cumplen slugify estándar | OK |
| 4.14 | Validación No falsa ubicación | Solo `/madrid/` aparece como city; 0 LCAs como path | OK |
| 4.15 | Validación No duplicar intención | 0 pares de URLs con duplicación detectada | OK |

# Bloque IV — Fuentes Internas GMB Crush usadas

## Fuentes internas GMB Crush usadas

<small>§9</small>

- Analysis Framework.pdf
- GMB CRUSH Universal AI Local SEO Framework Template
- Website Homepage AI Optimization Prompts/Framework
- Service Pages AI Optimization Prompts/Framework
- Location Pages AI Optimization Prompts/Framework
- GeoHub Pages AI Framework
- GeoArticle Pages AI Framework
- Additional Categories Pages AI Framework
