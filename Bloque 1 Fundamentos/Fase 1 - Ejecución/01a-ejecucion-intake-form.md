Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# Paso 1 — Intake Form

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso. El Paso 1 es origen del sistema, así que §3 lista lo que la IA tiene que rellenar/obtener (no hay heredados de pasos anteriores).
> - **Bloque II — Ejemplo rellenado** muestra los 14 outputs del Paso 1 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, reglas que aplican, checklist final y outputs consolidados.
> - **Bloque IV — Módulo doctrinal: Interpretación de la dirección física y zonas GEO** es un apéndice específico del Paso 1 que explica cómo decidir Local Coverage Areas y Approved Expansion Areas.
> - **Bloque V — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 1

<small>§2</small>

Paso 1 es el **origen del sistema** — la IA recoge del cliente y/o del análisis competitivo los datos mínimos del negocio que alimentan toda la arquitectura aguas abajo (Pasos 2-19). En este paso no hay heredados; todos los outputs nacen aquí.

**Outputs del paso:**

- **1.1** Business Name — nombre legal de la entidad
- **1.2** Website URL / Canonical Domain — dominio canónico único
- **1.3** GBP Lifecycle Status — 4 campos del ciclo de vida del GBP (Status, Creation Timing, Verification, URL)
- **1.4** Full NAP — 8 campos completos (Name, Street, City, State, ZIP, Country, Phone, Email)
- **1.5** Planned Primary GBP Category — categoría principal del futuro GBP
- **1.6** Planned Additional GBP Categories — categorías adicionales clasificadas (cubiertas vs necesitan página)
- **1.7** Main City — ciudad que genera la arquitectura base
- **1.8** Physical Location City — ciudad de presencia física real
- **1.9** Servicios principales — los 5 core services del cluster
- **1.10** Local Coverage Areas — Direct LCAs (del NAP) + Candidate LCAs (de competidores)
- **1.11** Approved Expansion Areas — zonas con URL propia (default: vacío en Phase 1)
- **1.12** GeoArticles per Service (G) — variable de la fórmula del Paso 2
- **1.13** Preferred CTA — CTA principal del cluster
- **1.14** Trust Signals — señales de confianza reales y reutilizables

**Errores que previene:**

- Empezar a crear páginas sin conocer la categoría principal del GBP
- Confundir Main City con Local Coverage Areas
- Crear páginas para zonas donde el negocio no atiende clientes
- Usar un NAP inconsistente con el futuro GBP
- Crear servicios sin distinguir core services de categorías adicionales
- Inventar GBP URL, sameAs o reseñas antes de que el GBP exista (web-first doctrina)
- Afirmar oficina física en zonas donde el negocio solo opera de forma móvil

**Cuándo se ejecuta:** primer paso del sistema. Recibe input del cliente (preflight `00preflight.md`) y, donde aplica, complementa con análisis competitivo (Local Pack) o keyword research. Antes de Paso 2 (Fórmula maestra).

## Lo que la IA tiene que rellenar/obtener

<small>§3</small>

> El Paso 1 NO hereda de pasos anteriores — es origen. La IA recoge estos campos del cliente (preflight) o los obtiene mediante análisis competitivo / keyword research según indica el método de cada output en §6.

```text
Business Name:

Website URL:

Canonical Domain:
Option A: https://www.domain.com
Option B: https://domain.com

GBP Status:
Not Created / Created / Verified / Pending Verification

GBP Creation Timing:
After website launch

GBP Verification Status:
Not Started / Pending / Verified

GBP URL:
Leave blank until the GBP is created in Paso 14.

Full NAP:
- Name:
- Street Address:
- City:
- State / Province:
- ZIP / Postal Code:
- Country:
- Phone:
- Email:

Planned Primary GBP Category:

Planned Additional GBP Categories:
1.
2.
3.

Main City:
The primary city that will generate the base architecture.

Physical Location City:
The city where the business is physically located, if applicable.

Servicios principales:
1.
2.
3.
4.
5.

Direct Local Coverage Areas:
Zonas que salen directamente de la dirección física.

> **Nota para la IA:** Antes de decidir las Local Coverage Areas, consultar el Bloque IV — Módulo doctrinal de este documento. Ese bloque explica cómo se interpreta la dirección física, cómo se eligen las zonas y qué criterios deben cumplir.
1.
2.

Candidate Local Coverage Areas:
Zonas que no salen de la dirección pero pueden tener sentido por proximidad, búsqueda o competencia. Solo se usan como señales GEO activas si pasan el test de coherencia GEO.
1.
2.
3.
4.
5.
6.
7.
8.

Should Local Coverage Areas generate pages?
Default: No.

Approved Expansion Areas:
Optional. Only list areas that deserve their own URLs.
1.
2.
3.

Additional Categories already covered by core services:
1.
2.

Additional Categories that need separate pages:
1.
2.

GeoArticles per Service:
Default: 3

Preferred CTA:
Option A: Llamar ahora
Option B: Reservar online
Option C: Solicitar presupuesto
Option D: Contactar

Trust Signals:
- Years in business:
- Reviews:
- Certifications:
- Awards:
- Guarantees:
- Urgencias / servicio en el mismo día / servicio móvil:
```

# Bloque II — Ejemplo rellenado para el Paso 1 — Intake Form

<small>§4</small>

> Los 14 outputs del Paso 1 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 1.X declarado en §5.

### 1.1 — Business Name

`Cerrajeros Madrid 24h`

### 1.2 — Website URL / Canonical Domain

| Campo | Valor |
|---|---|
| Website URL | `https://www.cerrajerosmadrid24h.com` |
| Canonical Domain | `https://www.cerrajerosmadrid24h.com` |

### 1.3 — GBP Lifecycle Status (web-first)

| Campo | Valor |
|---|---|
| GBP Status | `Not Created` |
| GBP Creation Timing | `After website launch` |
| GBP Verification Status | `Not Started` |
| GBP URL | `N/A — GBP not created yet` |

### 1.4 — Full NAP

| Campo | Valor |
|---|---|
| Name | Cerrajeros Madrid 24h |
| Street Address | Calle Rafael Calvo 12, Barrio Almagro, Distrito Chamberí |
| City | Madrid |
| State / Province | Comunidad de Madrid |
| ZIP / Postal Code | 28010 |
| Country | España |
| Phone | +34 600 000 000 |
| Email | info@cerrajerosmadrid24h.com |

### 1.5 — Planned Primary GBP Category

`Cerrajero` (status: `Planned`)

### 1.6 — Planned Additional GBP Categories

| Categoría | Status arquitectónico |
|---|---|
| Servicio de cerrajería de urgencia | Cubierta por core service `Cerrajero urgente` (no genera página adicional) |
| Servicio de duplicado de llaves | Necesita página propia (A = 1) |

### 1.7 — Main City

`Madrid`

### 1.8 — Physical Location City

`Madrid`

### 1.9 — Servicios principales (S = 5)

| # | Servicio |
|---|---|
| 1 | Cerrajero urgente |
| 2 | Apertura de puertas |
| 3 | Cambio de cerraduras |
| 4 | Cambio de bombines |
| 5 | Instalación de cerraduras de seguridad |

### 1.10 — Local Coverage Areas

| Tipo | Lista |
|---|---|
| Direct LCAs (del NAP) | Almagro, Chamberí |
| Candidate LCAs (de competidores) | Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad |
| ¿LCAs generan páginas en la base? | No, not in the base build |

### 1.11 — Approved Expansion Areas

`None in Phase 1`

### 1.12 — GeoArticles per Service (G)

`G = 3`

Aplicación: G × S = 3 × 5 = 15 GeoArticles para Madrid (calculados en Paso-02 2.8).

### 1.13 — Preferred CTA

`Llamar ahora`

### 1.14 — Trust Signals

| # | Trust signal |
|---|---|
| 1 | 10+ años de experiencia |
| 2 | Reseñas iniciales pendientes de recopilar tras crear y verificar el GBP |
| 3 | Técnicos cerrajeros cualificados |
| 4 | Servicio móvil en el mismo día |
| 5 | Garantía de trabajo |

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 14 outputs que el Paso 1 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `1.1`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 1.1 | Business Name | String | Input humano | — |
| 1.2 | Website URL / Canonical Domain | URL canónica | Input humano | — |
| 1.3 | GBP Lifecycle Status | 4 campos discretos | GMB Crush + Input humano | — |
| 1.4 | Full NAP | Bloque NAP de 8 campos | Input humano | — |
| 1.5 | Planned Primary GBP Category | Categoría GBP oficial | GMB Crush + Competidores | — |
| 1.6 | Planned Additional GBP Categories | Lista clasificada (cubiertas vs página propia) | GMB Crush + Competidores | — |
| 1.7 | Main City | Ciudad única | GMB Crush | — |
| 1.8 | Physical Location City | Ciudad de presencia física | Input humano | — |
| 1.9 | Servicios principales | 5 core services priorizados | GMB Crush + Competidores | — |
| 1.10 | Local Coverage Areas | Direct + Candidate (dos listas) | GMB Crush + Competidores | — |
| 1.11 | Approved Expansion Areas | Lista de zonas aprobadas (puede estar vacía) | Decisión de diseño | — |
| 1.12 | GeoArticles per Service (G) | Entero (default 3) | GMB Crush | — |
| 1.13 | Preferred CTA | Una opción de 4 estándar | Decisión de diseño | — |
| 1.14 | Trust Signals | Lista de 4-7 señales reales | GMB Crush + Competidores | — |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 14 outputs (1.1–1.14) con el mismo patrón: Explicación / Patrón o fórmula / Ejemplos correctos / Ejemplos incorrectos / Regla final / Validación operativa / Cómo se obtiene / Output del paso. Cada sub-sección §6.X corresponde 1:1 al output 1.X declarado en §5.

### 1.1 — Business Name

<small>§6.1</small>

**Explicación**

El nombre del negocio es la entidad base. Debe coincidir con el nombre del GBP cuando se use como NAP, schema o bloque de confianza. Es la pieza canónica que se reutiliza en homepage, contacto, footer, schema LocalBusiness y, eventualmente, GBP cuando se cree en el Paso 14.

**Patrón o fórmula**

```text
Business Name = nombre oficial de la entidad local
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h
```

**Ejemplos incorrectos**

```text
- Cerrajeros Madrid 24h Madrid (duplicado de ciudad)
- Cerrajeros Madrid 24h 24/7 Best Cheap (modificadores comerciales añadidos)
- Cerrajeros Madrid 24h Almagro (zona añadida si no es el nombre real)
- locksmiths-madrid (idioma cambiado o slug en vez de nombre)
```

**Regla final**

```text
El nombre del negocio debe ser estable, rastreable y consistente.
```

**Validación operativa**

El Business Name se reutiliza en TODOS los componentes del cluster (homepage H1, footer, contact page, schema LocalBusiness, JSON-LD, breadcrumbs, GBP cuando se cree en Paso 14). Si difiere entre página y página, la entidad local proyecta señales débiles. Validar que coincide con el nombre legal declarado y con el que se usará en el GBP.

**Cómo se obtiene**

- **Fuente:** Input humano.
- **Método:** Tomar el nombre legal de la entidad declarado por el cliente en el intake. Validar que coincide con el nombre que se usará en el GBP cuando se cree (Paso 14).

**Output del paso**

- **Tipo:** String — nombre legal de la entidad local.
- **Ejemplo (Cerrajeros Madrid 24h):** `Cerrajeros Madrid 24h`.

### 1.2 — Website URL / Canonical Domain

<small>§6.2</small>

**Explicación**

La URL raíz define el dominio canónico sobre el que se generarán todas las páginas. No se deben mezclar variantes con www y sin www, ni HTTP con HTTPS. La canónica es la única versión que aparece en URLs absolutas, schema y enlaces internos; las demás variantes redirigen 301.

**Patrón o fórmula**

```text
Canonical Domain = una sola versión del dominio (con o sin www, siempre HTTPS)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
https://www.cerrajerosmadrid24h.com
```

**Ejemplos incorrectos**

```text
- http://cerrajerosmadrid24h.com (HTTP en vez de HTTPS)
- https://cerrajerosmadrid24h.com y https://www.cerrajerosmadrid24h.com mezclados
- /home como página raíz
- URLs con mayúsculas o trailing slash inconsistente
```

**Regla final**

```text
Una web local debe operar con un solo dominio canónico.
```

**Validación operativa**

Una sola versión canónica del dominio en TODA la web; el resto redirige 301. Esta decisión se hereda al Paso-04 4.1 (Canonical Domain) que aplica la regla a las URLs absolutas, schema y enlaces internos del cluster.

**Cómo se obtiene**

- **Fuente:** Input humano.
- **Método:** Tomar el dominio canónico declarado por el cliente. Una sola versión (con o sin www, siempre con https). El resto de variantes deben redirigir 301 a la canónica.

**Output del paso**

- **Tipo:** URL canónica con protocolo y, si aplica, subdominio www.
- **Ejemplo (Cerrajeros Madrid 24h):** `https://www.cerrajerosmadrid24h.com`.

### 1.3 — GBP Lifecycle Status

<small>§6.3</small>

**Explicación**

En esta versión web-first, el Google Business Profile típicamente no existe cuando se ejecuta el Paso 1. La web se publica primero (Pasos 15-18) y el GBP se crea/verifica en el Paso 14. Estos 4 campos capturan el ciclo de vida del GBP en el momento del intake. Si el cliente ya tiene un GBP creado, se declara el estado real.

**Patrón o fórmula**

```text
GBP Status              ∈ {Not Created, Created, Verified, Pending Verification}
GBP Creation Timing     = After website launch (default web-first)
GBP Verification Status ∈ {Not Started, Pending, Verified}
GBP URL                 = blank hasta Paso 14, o URL real si ya existe
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
GBP Status: Not Created
GBP Creation Timing: After website launch
GBP Verification Status: Not Started
GBP URL: N/A — GBP not created yet
```

**Ejemplos incorrectos**

```text
- Marcar GBP Status = Verified sin haberlo creado
- Inventar una GBP URL antes del Paso 14
- Incluir sameAs del GBP en schema cuando no existe
- Afirmar reseñas de Google si el perfil aún no está creado
```

**Regla final**

```text
Hasta que el Paso 14 cree y verifique el GBP, los 4 campos toman valores web-first y la web no afirma señales del GBP (URL, sameAs, reseñas).
```

**Validación operativa**

La doctrina GMB Crush separa estrictamente la fase web-first (Pasos 1-13 + 15-18) de la fase GBP (Paso 14). Cualquier referencia al GBP en schema, contenido o trust signals antes del Paso 14 es invento. Si el cliente declara un GBP ya creado, el operador decide si adelantar el Paso 14 fuera del orden estándar o congelar el GBP existente y sincronizarlo en el momento normal.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Input humano.
- **Método:** Preguntar al cliente si ya tiene GBP creado o verificado. Si NO (default web-first según doctrina): los 4 campos toman los valores fijos `Not Created / After website launch / Not Started / N/A`. Si SÍ: capturar el estado real declarado por el cliente y considerar adelantar el Paso 14 fuera del orden estándar.

**Output del paso**

- **Tipo:** 4 valores discretos del ciclo de vida del GBP.
- **Ejemplo (Cerrajeros Madrid 24h):** Status: Not Created · Creation Timing: After website launch · Verification: Not Started · URL: N/A (pending Paso 14).

### 1.4 — Full NAP

<small>§6.4</small>

**Explicación**

El NAP (Name, Address, Phone) es una señal de entidad local. Debe ser igual en homepage, contacto, footer, schema y GBP cuando proceda. El intake captura los 8 campos completos para que se reutilicen como dato canónico aguas abajo.

**Patrón o fórmula**

```text
NAP completo = Name + Street Address + City + State/Province + ZIP/Postal Code + Country + Phone + Email
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h, Calle Rafael Calvo 12, Barrio Almagro, Distrito Chamberí, 28010 Madrid, España, +34 600 000 000, info@cerrajerosmadrid24h.com
```

**Ejemplos incorrectos**

```text
- Cambiar el teléfono entre páginas
- Usar direcciones distintas sin explicación
- Ocultar el NAP en imágenes no rastreables
- NAP solo en footer pero no en homepage o contact
```

**Regla final**

```text
El NAP debe ser visible, consistente y rastreable.
```

**Validación operativa**

El NAP debe quedar definido una sola vez en el intake y reutilizarse sin variaciones en homepage, footer, contact page y schema LocalBusiness. Si cambia entre páginas o entre la web y el GBP que se cree en el Paso 14, la entidad local arranca con una señal débil y se pierde rastreabilidad. El intake convierte el NAP en un dato canónico que después se reutiliza en schema, bloques de confianza y CTAs con teléfono.

**Cómo se obtiene**

- **Fuente:** Input humano.
- **Método:** Recoger los 8 campos del NAP completos (Name, Street Address, City, State/Province, ZIP/Postal Code, Country, Phone, Email) y dejarlos como dato canónico reutilizable en homepage, footer, contact page y schema.

**Output del paso**

- **Tipo:** Bloque NAP completo (8 campos) en formato canónico único.
- **Ejemplo (Cerrajeros Madrid 24h):** Cerrajeros Madrid 24h, Calle Rafael Calvo 12, Barrio Almagro, Distrito Chamberí, 28010 Madrid, España, +34 600 000 000, info@cerrajerosmadrid24h.com

### 1.5 — Planned Primary GBP Category

<small>§6.5</small>

**Explicación**

La categoría principal del GBP manda sobre la arquitectura. Los servicios y páginas deben apoyar esa categoría. Es el eje semántico del sistema y define el slug raíz (`primary_category_slug`) que se usa en URLs.

**Patrón o fórmula**

```text
Planned Primary GBP Category → Primary Category Slug → Service Pages
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajero → cerrajero
```

**Ejemplos incorrectos**

```text
- Usar una categoría que no existe en el catálogo GBP oficial
- Construir la web alrededor de un servicio secundario
- No crear páginas que soporten la categoría principal
- Inventar una categoría sin validar con competidores
```

**Regla final**

```text
La categoría principal debe verse reflejada en homepage, servicios y páginas locales.
```

**Validación operativa**

La categoría principal del GBP define el eje semántico del sistema y debe tener soporte directo en homepage y servicios core. Si el GBP intenta posicionar `Cerrajero` pero la web habla mayoritariamente de servicios secundarios, la entidad local proyecta dos intenciones distintas y diluye autoridad. Antes de avanzar al Paso 2, validar que los servicios core (§6.9) realmente apoyan la Primary Category.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Competidores.
- **Método:**
  1. Buscar en Google Maps `[servicio principal] [main city]` sin login.
  2. Anotar la categoría primaria declarada por los 5 negocios mejor posicionados en el Local Pack.
  3. Seleccionar la categoría que más se repite (>3 de 5) como Primary Category Planned. Si hay empate, priorizar la más amplia (categoría madre del catálogo GBP).
  4. Validar contra el catálogo oficial de GBP. Si la categoría no existe exactamente, escoger la más próxima del catálogo.

**Output del paso**

- **Tipo:** Categoría GBP oficial (Primary).
- **Ejemplo (Cerrajeros Madrid 24h):** `Cerrajero` (status: `Planned` hasta Paso 14).

### 1.6 — Planned Additional GBP Categories

<small>§6.6</small>

**Explicación**

Las categorías adicionales refuerzan la profundidad de entidad, pero no siempre generan páginas nuevas si ya están cubiertas por un core service. La consolidación se hace ANTES de cerrar el intake para evitar duplicados aguas abajo.

**Patrón o fórmula**

```text
Additional Category → covered by core service OR needs separate page
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Servicio de cerrajería de urgencia: cubierta por core service Cerrajero urgente (NO genera página)
Servicio de duplicado de llaves: necesita página propia (genera /cerrajero/madrid/duplicado-llaves/)
```

**Ejemplos incorrectos**

```text
- Crear cerrajero-urgente y cerrajero-urgente como páginas separadas
- Ignorar Servicio de duplicado de llaves
- Crear categorías sin relación con el GBP
- Inflar A contando categorías ya cubiertas por core
```

**Regla final**

```text
Cada categoría adicional se consolida o se convierte en página, pero nunca se duplica.
```

**Validación operativa**

Cada categoría adicional debe clasificarse antes de entrar en la arquitectura. Primero se revisa si ya está cubierta por un servicio core (entonces no genera URL — queda consolidada); si no, se marca como categoría efectiva que necesita página propia. Esta clasificación evita duplicar intenciones, crear páginas casi idénticas y canibalizar la Service Overview Page del core service. La consolidación final se valida en Paso-02 2.12 (Control anti-duplicación).

**Cómo se obtiene**

- **Fuente:** GMB Crush + Competidores.
- **Método:**
  1. Tras escoger la Primary Category (§6.5), revisar las categorías adicionales declaradas por los mismos 5 competidores top.
  2. Listar todas las categorías secundarias que aparecen en al menos 2 de los 5 competidores.
  3. Filtrar las que el cliente realmente ofrece (cruce con servicios reales). Las que no ofrece se descartan.
  4. Aplicar la regla de consolidación: si una categoría adicional coincide con un core service, se marca como cubierta. Si no, se marca como "necesita página propia".

**Output del paso**

- **Tipo:** Lista de categorías clasificadas (cubiertas vs necesitan página propia).
- **Ejemplo (Cerrajeros Madrid 24h):** Servicio de cerrajería de urgencia → cubierta por Cerrajero urgente. Servicio de duplicado de llaves → necesita página propia.

### 1.7 — Main City

<small>§6.7</small>

**Explicación**

La Main City es la ciudad que genera la arquitectura base. Es la unidad local principal del sistema simplificado y se hereda al Paso 2 (Fórmula maestra) y al Paso 3 (URL Matrix) como `main_city_slug`.

**Patrón o fórmula**

```text
Main City = /city/ + /category/city/service/
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Madrid
```

**Ejemplos incorrectos**

```text
- Almagro como Main City si el GBP y el NAP están en Madrid
- Meter cinco ciudades como base
- Cambiar la Main City según la página
- Confundir Main City con Local Coverage Areas
```

**Regla final**

```text
La base se construye sobre una sola Main City.
```

**Validación operativa**

La Main City genera URLs base; las Local Coverage Areas (§6.10) refuerzan contenido y schema sin generar URLs por defecto; las Approved Expansion Areas (§6.11) son URLs opcionales que requieren aprobación explícita. Estas tres capas deben mantenerse separadas en el intake — mezclarlas vuelve al sistema viejo de target cities y secondary cities con páginas innecesarias. Cruce con Bloque IV (Módulo doctrinal) para entender por qué la dirección física determina la Main City sin más.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Extraer la ciudad directamente del campo City del NAP (§6.4). Una sola Main City genera la arquitectura base. No se multiplica por barrios ni por zonas de cobertura.

**Output del paso**

- **Tipo:** Ciudad única — la del NAP.
- **Ejemplo (Cerrajeros Madrid 24h):** `Madrid`.

### 1.8 — Physical Location City

<small>§6.8</small>

**Explicación**

La ciudad de ubicación física evita falsas señales. Si no hay oficina en un área, no se debe decir que la hay. Este campo controla qué páginas pueden usar lenguaje de oficina o address local.

**Patrón o fórmula**

```text
Physical Location City = ciudad de presencia real (puede ser "móvil")
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Madrid
```

**Ejemplos incorrectos**

```text
- "Nuestra oficina en Almagro" si no existe
- "Visit our Chamberí storefront" si no existe
- Schema con address falsa
- Marcar Physical Location en una LCA donde no hay oficina
```

**Regla final**

```text
Nunca se inventa ubicación física.
```

**Validación operativa**

El intake debe indicar la ciudad de presencia física real y si existe atención presencial. Esto controla qué páginas pueden usar LocalBusiness con dirección, mapa o lenguaje de oficina. Nunca afirmar oficinas en áreas de cobertura donde el negocio solo presta servicio móvil — si no hay oficina en Almagro, las páginas de Madrid no deben decir «our Almagro storefront». La validación cruzada se aplica en Paso-04 4.14 (No falsa ubicación) y Paso 6 §9 (Principio 5 — No falsa ubicación).

**Cómo se obtiene**

- **Fuente:** Input humano.
- **Método:** Tomar la ciudad de presencia física real declarada por el cliente (oficina, almacén o punto de atención). Si el negocio es móvil sin oficina, declarar "móvil" o coincidir con la Main City sin afirmar oficina física.

**Output del paso**

- **Tipo:** Ciudad de presencia física real (puede ser "móvil").
- **Ejemplo (Cerrajeros Madrid 24h):** `Madrid`.

### 1.9 — Servicios principales

<small>§6.9</small>

**Explicación**

Los core services son los servicios principales que generan Service Overview Pages y Páginas de servicio en la Main City. Son el multiplicador principal de la fórmula del Paso 2 (variable S) y definen los slugs operativos del cluster.

**Patrón o fórmula**

```text
S = número de core services (default: 5)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
1. Cerrajero urgente
2. Apertura de puertas
3. Cambio de cerraduras
4. Cambio de bombines
5. Instalación de cerraduras de seguridad
```

**Ejemplos incorrectos**

```text
- Meter servicios irrelevantes
- Crear servicios que no se ofrecen
- Agrupar todos los servicios en una única página
- Contar sinónimos como servicios separados (urgente cerrajero / cerrajero urgente)
- Inflar S con microvariantes
```

**Regla final**

```text
Cada core service importante debe tener página propia.
```

**Validación operativa**

Los core services son los que generan Service Overview Pages y Location-Based Service Pages en la Main City. Deben tener nombres claros, slugs limpios y valor comercial real. Solo entran servicios reales — no microvariantes, no sinónimos, no servicios que el negocio no ofrece. La fórmula del Paso 2 depende de S = número de servicios core; inflar S aquí infla todo el inventario de páginas aguas abajo.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Competidores.
- **Método:**
  1. Buscar en Google Maps `[categoría principal] [main city]` y abrir los 5 perfiles GBP mejor posicionados del Local Pack.
  2. En cada perfil, abrir la sección «Servicios» del GBP y listar los servicios declarados.
  3. Contar la frecuencia de cada servicio entre los 5 competidores. Seleccionar los 5 servicios más frecuentes (top 5 por frecuencia).
  4. Cruzar con la oferta real del cliente. Si el cliente no ofrece uno de los servicios top, sustituirlo por el siguiente más frecuente que sí ofrezca.
  5. Si hay empate de frecuencia, priorizar el servicio con más volumen de búsqueda local (cruce con keyword research).

**Output del paso**

- **Tipo:** 5 core services (S=5) priorizados.
- **Ejemplo (Cerrajeros Madrid 24h):** Cerrajero urgente, Apertura de puertas, Cambio de cerraduras, Cambio de bombines, Instalación de cerraduras de seguridad.

### 1.10 — Local Coverage Areas

<small>§6.10</small>

**Explicación**

Son zonas seleccionadas por proximidad al NAP, coherencia GEO y lógica GMB Crush. Incluyen barrios, distritos, municipios cercanos o áreas de servicio. Se clasifican en Direct (salen del ancla física) y Candidate (requieren validación GEO). NO generan URLs por defecto — viven en contenido, FAQs y schema `areaServed`.

**Patrón o fórmula**

```text
Direct LCAs    = zonas extraídas directamente del NAP (barrio + distrito de la dirección)
Candidate LCAs = zonas que aparecen en ≥ 2 competidores Y pasan test GEO 3/6
Local Coverage Areas → contenido + FAQs + schema areaServed (no URLs base)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Direct LCAs: Almagro, Chamberí
Candidate LCAs: Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad
Páginas generadas: 0 (LCAs no generan URLs en la base)
```

**Ejemplos incorrectos**

```text
- Crear /almagro/ por defecto solo porque está en LCAs
- Usar áreas donde no se atiende
- Listar 40 zonas sin naturalidad
- Confundir LCAs con Approved Expansion Areas
- Inventar zonas para inflar contenido
```

**Regla final**

```text
Las áreas de cobertura refuerzan el contenido; no crean páginas automáticamente.
```

**Validación operativa**

Las LCAs son señales GEO, no URLs. Para entender CÓMO se eligen Direct y Candidate, consultar el Bloque IV — Módulo doctrinal (§9-§19) que explica el test GEO 3/6, los criterios de validación y la diferencia LCA vs AEA. Validación cruzada en Paso-04 4.9 (LCAs no generan URLs), Paso 6 §6 (Principio 2 — LCAs enriquecen contenido) y Paso 8 (schema `areaServed`).

**Cómo se obtiene**

- **Fuente:** GMB Crush + Competidores.

- **Método (Direct LCAs):**
  1. Las Direct LCAs salen del propio ancla físico del NAP (§6.4): barrio y distrito de la dirección. Se registran de forma directa sin más validación.

- **Método (Candidate LCAs):**
  1. Revisar las áreas de servicio declaradas por los 3-5 competidores top en Google Maps.
  2. Listar todas las zonas (barrios, distritos, municipios) que aparecen en al menos 2 competidores y NO están ya en Direct.
  3. Para cada zona candidata, aplicar el test de coherencia GEO 3/6 (Bloque IV §14). Si pasa 3 de 6 criterios, queda como Candidate validable. Si no, se descarta.
  4. Las Candidate aprobadas entran como contenido en LBS, GeoHub y GeoArticles. Solo generan URL si pasan a Approved Expansion (§6.11).

**Output del paso**

- **Tipo:** Dos listas — Direct (del NAP) y Candidate (de competidores).
- **Ejemplo (Cerrajeros Madrid 24h):** Direct: Almagro, Chamberí. Candidate: Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad.

### 1.11 — Approved Expansion Areas

<small>§6.11</small>

**Explicación**

Son áreas que sí pueden generar URLs propias, pero solo si se aprueban por demanda, competencia o valor comercial. Default vacío en Phase 1; activación es decisión consciente, no default.

**Patrón o fórmula**

```text
Approved Expansion Area → optional URLs (E ≥ 1)
Default: E = 0 en Phase 1 (None)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
None in Phase 1
```

**Ejemplos incorrectos**

```text
- Aprobar todas las áreas de cobertura
- Crear una capa de expansión sin contenido único
- Confundir cobertura con arquitectura
- Activar AEA sin demanda comercial verificada
```

**Regla final**

```text
Solo las áreas aprobadas generan URLs propias.
```

**Validación operativa**

El sistema base no crea páginas para todas las zonas de cobertura. Solo una Local Coverage Area pasa a Approved Expansion Area si hay demanda, oportunidad, valor comercial y capacidad de escribir contenido único. En el intake base este campo puede estar vacío sin que el sistema quede incompleto — la expansión territorial se aprueba; no se asume. Los criterios concretos están en Bloque IV §17 (Cuándo una zona pasa a página propia).

**Cómo se obtiene**

- **Fuente:** Decisión de diseño.
- **Método:** Vacío por defecto en Phase 1. Una zona pasa de Candidate LCA (§6.10) a Approved Expansion solo si cumple los criterios del Bloque IV §17: demanda de búsqueda + competidores trabajándola + contenido único posible + valor comercial + sin fingir oficina física. Cada aprobación es una decisión consciente, no un default.

**Output del paso**

- **Tipo:** Lista de zonas aprobadas (puede estar vacía en Phase 1).
- **Ejemplo (Cerrajeros Madrid 24h):** `None in Phase 1`.

### 1.12 — GeoArticles per Service (G)

<small>§6.12</small>

**Explicación**

G es una variable de la Fórmula Maestra del Paso 2 (`Total = 1 + S + 1 + S + A + G × S`). Define cuántos artículos de blog/GeoArticles se generan por cada servicio core dentro de la Main City. El intake del Paso 1 captura el valor (default 3) para que el Paso 2 lo aplique directamente.

**Patrón o fórmula**

```text
GeoArticles per Service = G ∈ {2, 3, 4, 5}
Default: G = 3
Total GeoArticles del cluster = G × S
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
GeoArticles per Service: 3
G × S = 3 × 5 = 15 GeoArticles para Madrid
```

**Ejemplos incorrectos**

```text
- Usar G = 10 sin capacidad de producción real
- Multiplicar G por cada Local Coverage Area
- G = 0 dejando los core services sin boosters semánticos
- Cambiar G entre pasos sin recalcular el inventario
```

**Regla final**

```text
G es el default doctrinal (3); ajustable solo si el cliente justifica otra capacidad de producción y refresh.
```

**Validación operativa**

G se decide en Paso 1 y la Fórmula Maestra del Paso 2 lo aplica como multiplicador. Cambiar G aquí cambia el inventario completo del cluster aguas abajo. Si el cliente no tiene capacidad para producir 15 artículos, hay que negociar G más bajo en el intake en lugar de aceptarlo y luego no publicarlos. Cruce con Paso-02 2.8 (Variable G).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Default `G = 3` según doctrina GMB Crush. Ajustable solo si el cliente justifica capacidad de producción y plan de refresh distintos al default doctrinal.

**Output del paso**

- **Tipo:** Entero — GeoArticles por servicio core.
- **Ejemplo (Cerrajeros Madrid 24h):** `G = 3` → 15 GeoArticles totales.

### 1.13 — Preferred CTA

<small>§6.13</small>

**Explicación**

El CTA debe ser coherente con el tipo de negocio y el servicio. Se elige uno de 4 estándar y se reutiliza consistentemente en toda la web (homepage, service pages, LBS, GeoArticles).

**Patrón o fórmula**

```text
CTA ∈ {Llamar ahora, Reservar online, Solicitar presupuesto, Contactar}
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Llamar ahora
```

**Ejemplos incorrectos**

```text
- Usar un CTA distinto en cada página sin criterio
- No tener CTA
- CTA genérico sin ciudad ni servicio
- Mezclar 3 CTAs distintos en la misma página
```

**Regla final**

```text
Cada página debe tener un CTA claro y consistente con el del cluster.
```

**Validación operativa**

El CTA preferido se hereda al Paso 5 (Page Type Rules) que lo aplica a cada page type, y al Paso 7 (Internal Linking) que lo usa como anchor de los enlaces de conversión. Para servicios urgentes (cerrajería, fontanería) el CTA estándar es `Llamar ahora` con `tel:` link. Para servicios de cita previa (consultorías, salud) suele ser `Reservar online` o `Contactar`.

**Cómo se obtiene**

- **Fuente:** Decisión de diseño.
- **Método:** Elegir uno de los 4 CTAs estándar — Llamar ahora / Reservar online / Solicitar presupuesto / Contactar — según el tipo de negocio, urgencia del servicio y comportamiento esperado del usuario. El CTA debe ser consistente en homepage, service pages y LBS.

**Output del paso**

- **Tipo:** Una sola opción de CTA reutilizable en toda la web.
- **Ejemplo (Cerrajeros Madrid 24h):** `Llamar ahora`.

### 1.14 — Trust Signals

<small>§6.14</small>

**Explicación**

Las señales de confianza ayudan al usuario, a Google y a sistemas de IA a validar autoridad. Son datos reales y reutilizables que sostienen E-E-A-T del cluster.

**Patrón o fórmula**

```text
Trust Signals = Reviews + years + certifications + guarantees + diferenciadores reales
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
1. 10+ años de experiencia
2. Reseñas iniciales pendientes de recopilar tras crear y verificar el GBP
3. Técnicos cerrajeros cualificados
4. Servicio móvil en el mismo día
5. Garantía de trabajo
```

**Ejemplos incorrectos**

```text
- Afirmaciones sin base ("líder del sector")
- Reviews inventadas
- Badges falsos
- Certificaciones que el cliente no tiene
- Trust signals sin fuente verificable
```

**Regla final**

```text
Los trust signals deben ser reales y reutilizables.
```

**Validación operativa**

Las señales de confianza recogidas en el intake se reutilizan en homepage, páginas de servicio, GeoHub, CTAs y QA. Años de experiencia, reseñas, certificaciones, garantías y servicio móvil sostienen autoridad sin inventar contenido. Toda señal debe ser real, reutilizable y verificable — no inventar certificaciones, no usar reseñas sin fuente, no usar badges falsos. La validación cruzada se aplica en Paso 6 §19 (Reviews y trust blocks contextualizados).

**Cómo se obtiene**

- **Fuente:** GMB Crush + Competidores.
- **Método:**
  1. Revisar las homepages y LBS de los 5 competidores top del Local Pack.
  2. Listar los trust signals que aparecen en al menos 3 de los 5 competidores (el «estándar» del sector).
  3. Listar los trust signals que aparecen en 1 o 2 competidores (los «diferenciadores» que pocos usan).
  4. Confirmar con el cliente cuáles puede acreditar como reales (años, certificaciones, garantías, equipo cualificado). Filtrar los que no puede demostrar.
  5. Resultado: 3-5 trust signals que sean del estándar del sector + 1-2 diferenciadores acreditables.

**Output del paso**

- **Tipo:** Lista de 4-7 trust signals reales y reutilizables.
- **Ejemplo (Cerrajeros Madrid 24h):** 10+ años de experiencia, técnicos cerrajeros cualificados, servicio móvil en el mismo día, garantía de trabajo, reseñas iniciales pendientes de recopilar tras crear el GBP.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 1 y avanzar al Paso 2 (Fórmula Maestra). Cada ☐ es un check que debe pasar antes del handoff.

### Validación de identidad y dominio

- ☐ El Business Name (1.1) coincide con la entidad real y con el nombre que se usará en el GBP
- ☐ Hay una sola versión canónica del dominio (1.2) — no se mezcla www con non-www ni HTTP con HTTPS
- ☐ El NAP (1.4) es completo (8 campos) y consistente con la dirección física
- ☐ El GBP Lifecycle Status (1.3) refleja el estado real (default web-first: Not Created)

### Validación de categorías y servicios

- ☐ La Primary Category (1.5) está validada contra el catálogo GBP oficial
- ☐ Las Additional Categories (1.6) están clasificadas en cubiertas vs página propia
- ☐ Los core services (1.9) están priorizados (S=5) y son reales (no microvariantes)
- ☐ G (1.12) está fijado (default 3) y es factible para la capacidad del cliente

### Validación de geografía

- ☐ La Main City (1.7) coincide con la del NAP — no se mezcla con LCAs
- ☐ La Physical Location City (1.8) refleja oficina real (o "móvil" si no hay)
- ☐ Las LCAs (1.10) son reales y validadas (Direct + Candidate con test GEO 3/6)
- ☐ Las AEAs (1.11) están vacías por defecto en Phase 1; cualquier zona aprobada cumple criterios del Bloque IV §17

### Validación de conversión y autoridad

- ☐ El CTA principal (1.13) está definido y es coherente con el tipo de negocio
- ☐ Los Trust Signals (1.14) son reales (4-7 acreditados) y reutilizables

## Outputs Consolidados

<small>§8</small>

> Tabla final con valores reales para Cerrajeros Madrid 24h y status de cada output. Los IDs (`1.1`–`1.14`) coinciden con los declarados en §5.

| ID | Output | Valor (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|
| 1.1 | Business Name | `Cerrajeros Madrid 24h` | confirmed |
| 1.2 | Website URL / Canonical Domain | `https://www.cerrajerosmadrid24h.com` | confirmed |
| 1.3 | GBP Lifecycle Status | Not Created / After website launch / Not Started / N/A | confirmed (web-first) |
| 1.4 | Full NAP | Cerrajeros Madrid 24h, Calle Rafael Calvo 12, 28010 Madrid, España, +34 600 000 000, info@cerrajerosmadrid24h.com | confirmed |
| 1.5 | Planned Primary GBP Category | `Cerrajero` (Planned) | confirmed |
| 1.6 | Planned Additional GBP Categories | Servicio de cerrajería de urgencia (cubierta) + Servicio de duplicado de llaves (página propia) | confirmed |
| 1.7 | Main City | `Madrid` | confirmed |
| 1.8 | Physical Location City | `Madrid` | confirmed |
| 1.9 | Servicios principales (S=5) | Cerrajero urgente, Apertura de puertas, Cambio de cerraduras, Cambio de bombines, Instalación de cerraduras de seguridad | confirmed |
| 1.10 | Local Coverage Areas | Direct: Almagro, Chamberí · Candidate: Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad | confirmed |
| 1.11 | Approved Expansion Areas | None in Phase 1 (E=0) | confirmed |
| 1.12 | GeoArticles per Service (G) | `G = 3` → G × S = 15 GeoArticles | confirmed |
| 1.13 | Preferred CTA | `Llamar ahora` | confirmed |
| 1.14 | Trust Signals | 10+ años, técnicos cualificados, servicio móvil, garantía, reseñas iniciales pendientes | confirmed |

# Bloque IV — Módulo doctrinal: Interpretación de la dirección física y zonas GEO

## Módulo — Interpretación GMB Crush de la dirección física y zonas GEO

<small>§9</small>

> **Definición operativa — Local Coverage Areas:** zonas, barrios, distritos o landmarks seleccionados desde la dirección física, la Main City, la coherencia GEO, la proximidad, los datos de búsqueda, los competidores y la lógica GMB Crush para reforzar relevancia local dentro del contenido, schema y futuros análisis. No son automáticamente URLs. No son automáticamente páginas propias. No son necesariamente oficinas físicas. Las Local Coverage Areas se usan primero como señales GEO dentro del contenido. No generan URLs por defecto.

Este bloque se añade dentro del **Paso 1 — Intake Form**, justo después de recoger el **Physical Address / NAP** y antes de definir:

```text
Main City
Local Coverage Areas
Approved Expansion Areas
```

La función de este bloque es dejar claro cómo se interpreta una dirección física concreta dentro de la lógica GMB Crush.

## Interpretación GMB Crush de la dirección física

<small>§10</small>

A partir de una dirección concreta como:

```text
Rafael Calvo 40, Madrid
```

GMB Crush nos dice que hagamos esto:

| Orden | Qué hacer | Resultado |
|---:|---|---|
| 1 | Usar la dirección como **Physical Address / NAP** | Nombre, dirección, ciudad, teléfono y país quedan como datos base del negocio. El Analysis Framework pide Physical Address y Service Areas como input inicial. |
| 2 | Extraer la **Main City** desde la dirección | Main City = **Madrid**. |
| 3 | Construir la arquitectura sobre la ciudad, no sobre la calle | La unidad base no es "Rafael Calvo", sino **Madrid**. |
| 4 | Crear la homepage como entidad raíz | `/` con H1 tipo `[Brand] + [Primary Service] + Madrid`, NAP visible, servicios core y enlaces internos. |
| 5 | Crear páginas de servicio sin ciudad | `/cerrajero/apertura-puertas/`, `/cerrajero/cerrajero-urgente/`, etc. Estas páginas son pilares temáticos, no páginas locales. |
| 6 | Crear páginas servicio + ciudad | `/cerrajero/madrid/apertura-puertas/`, `/cerrajero/madrid/cerrajero-urgente/`, etc. GMB Crush define este patrón como `/category/city/service/`. |
| 7 | Crear GeoHub de ciudad | `/madrid/`, como contenedor de todos los servicios, categorías y artículos de Madrid. |
| 8 | Usar barrios, zonas cercanas o landmarks solo como señales GEO dentro del contenido | Se pueden mencionar barrios, zonas o landmarks en intro, H2s, FAQs, GeoHub y GeoArticles, pero no generan páginas por defecto. El framework permite "neighborhood coverage" en GeoHub y referencias locales en GeoArticles. |
| 9 | No fingir ubicación física en otras zonas | Puedes decir que el contenido referencia zonas locales, pero no "tenemos oficina en X" si no es verdad. Los GeoArticles indican expresamente no fingir ubicación física. |
| 10 | Usar `areaServed` en schema | En páginas locales, el schema `LocalBusiness` debe incluir `areaServed`, URL, teléfono, email y `sameAs` si existe. |

### En una frase

<small>§10.1</small>

GMB Crush no dice:

```text
Tengo una dirección en Rafael Calvo 40 → creo páginas por barrios automáticamente.
```

Dice:

```text
Tengo una dirección física → fijo NAP y Main City → construyo homepage, servicios, páginas servicio+Madrid, GeoHub Madrid y GeoArticles → uso barrios/zonas como señales GEO dentro del contenido, no como URLs por defecto.
```

### Aplicado al ejemplo

<small>§10.2</small>

```text
Dirección:
Rafael Calvo 40, Madrid

Main City:
Madrid
```

Arquitectura base:

```text
/
/cerrajero/apertura-puertas/
/cerrajero/cerrajero-urgente/
/madrid/
/cerrajero/madrid/apertura-puertas/
/cerrajero/madrid/cerrajero-urgente/
/madrid/cuanto-cuesta-un-cerrajero-urgente/
```

Si luego queremos crear páginas por zona o barrio, eso ya es una **expansión**, no la base GMB Crush.

## Qué dice GMB Crush sobre elegir barrios, zonas o landmarks

<small>§11</small>

GMB Crush **no da una fórmula cerrada tipo "elige estos 3 barrios"**.

Lo que sí dice es:

1. **El input inicial debe incluir Physical Address y Service Areas.**

   Es decir, la dirección física y las áreas relevantes son datos base de análisis local.

2. **La arquitectura base se construye con ciudad, no con barrio.**

   La homepage usa:

   ```text
   [Brand] + [Primary Service] + [Main City]
   ```

   Las páginas locales usan:

   ```text
   /category/city/service/
   ```

   Y el GeoHub es:

   ```text
   /city/
   ```

3. **Los barrios, zonas o landmarks se usan dentro del contenido como señales GEO.**

   GMB Crush los menciona en tres sitios:

   ```text
   Location-Based Service Pages:
   opening geo-specific con neighborhood / local issues

   GeoHub Pages:
   neighborhood coverage opcional

   GeoArticles:
   local references, landmarks, neighborhoods
   ```

4. **No se debe fingir ubicación física en esas zonas.**

   GeoArticles dice expresamente que deben enviar señales geográficas sin pretender que el negocio está físicamente ubicado allí si no es verdad.

## ¿Cómo se deciden las zonas?

<small>§12</small>

Según GMB Crush, se deciden así:

| Orden | Criterio | Qué significa |
|---:|---|---|
| 1 | **Dirección física** | Primero extraes la ciudad, barrio, distrito o zona que salen directamente del NAP. |
| 2 | **Main City** | La ciudad de la dirección se convierte en la base de la arquitectura. |
| 3 | **Service Areas / zonas relevantes** | Se identifican zonas que tienen sentido como señales GEO dentro de la ciudad o área principal. |
| 4 | **Neighborhood coverage** | Se usan barrios o zonas en GeoHub, páginas locales y artículos como cobertura semántica. |
| 5 | **Local issues / landmarks** | Se añaden referencias locales reales para dar contexto humano y GEO. |
| 6 | **No URLs automáticas** | Esas zonas no generan páginas por defecto. Solo se mencionan como señales GEO. |

### Aplicado a Rafael Calvo 40, Madrid

<small>§12.1</small>

| Paso | Resultado |
|---|---|
| Dirección física | Rafael Calvo 40, Madrid |
| Main City | Madrid |
| Zonas derivadas directas | Si la dirección está en Almagro / Chamberí, esas zonas son las primeras referencias GEO |
| Zonas cercanas o representativas | Se pueden usar como neighborhood coverage si son coherentes: Salamanca, Retiro, Centro, etc. |
| Uso en arquitectura | No crean URLs por defecto |
| Uso en contenido | Intro local, H2s, FAQs, GeoHub, GeoArticles, schema `areaServed` |

## Regla final sobre barrios, zonas y landmarks

<small>§13</small>

GMB Crush no dice:

```text
Crea páginas por barrios.
```

GMB Crush dice:

```text
Usa la dirección física para fijar Main City, crea páginas city+service, y usa barrios, zonas o landmarks como señales GEO dentro del contenido.
```

Y para elegir esas zonas:

```text
Empieza por las zonas derivadas directamente de la dirección física.
Después añade zonas cercanas o relevantes solo si tienen sentido GEO, semántico o competitivo.
No las conviertas en URLs salvo que pasen a una fase de expansión aprobada.
```

## Test GMB Crush para saber si una zona tiene sentido

<small>§14</small>

Una zona se puede añadir como señal GEO si cumple **al menos 3 de estos 6 criterios**.

| Criterio | Pregunta | Si la respuesta es sí |
|---|---|---|
| 1. Ancla física | ¿La zona sale directamente de la dirección? | Entra casi seguro |
| 2. Main City | ¿La zona pertenece claramente a la Main City? | Puede usarse como señal GEO |
| 3. Proximidad | ¿Está cerca o conectada al punto físico? | Puede usarse como zona candidata |
| 4. Intención local | ¿La zona ayuda a explicar una necesidad local real del servicio? | Puede aparecer en contenido |
| 5. Demanda o competencia | ¿Hay búsquedas o competidores trabajando esa zona? | Refuerza su inclusión |
| 6. No falsa ubicación | ¿Podemos mencionarla sin decir que tenemos oficina allí? | Es segura para contenido |

Si una zona solo cumple 1 criterio débil, no la metemos.

## Regla práctica

<small>§15</small>

### Entra directamente

<small>§15.1</small>

Zonas que salen de la dirección física.

Ejemplo:

```text
Dirección:
Calle Rafael Calvo 40, Barrio Almagro, Distrito Chamberí, Madrid
```

Entonces:

```text
Madrid = Main City
Almagro = zona GEO directa
Chamberí = zona GEO directa
```

Estas son coherentes porque salen del propio ancla físico.

### Entra como candidata

<small>§15.2</small>

Zonas que no salen de la dirección, pero pueden tener sentido por proximidad, búsqueda o competencia.

Ejemplo:

```text
Salamanca
Retiro
Centro
Tetuán
Chamartín
Arganzuela
Moncloa
Prosperidad
```

Estas no deberían añadirse automáticamente. Solo entran si podemos justificar que:

```text
están conectadas geográficamente
o tienen demanda
o aparecen en competencia
o ayudan a explicar contexto local real
```

### No entra

<small>§15.3</small>

Una zona no entra si:

```text
no sale de la dirección
no está conectada a la Main City
no aporta contexto local
no hay búsqueda ni competencia
solo se añade para inflar contenido
obliga a fingir ubicación física
```

Ejemplo incorrecto:

```text
"Cerrajero en Valencia" dentro de una página de Madrid.
```

Ejemplo también débil:

```text
Meter 20 barrios de Madrid en todas las páginas sin relación concreta.
```

## Cómo se usa una zona aprobada

<small>§16</small>

Una zona aprobada primero se usa como **señal GEO**, no como URL.

### Correcto

<small>§16.1</small>

```text
/cerrajero/madrid/cerrajero-urgente/
```

Dentro del contenido:

```text
Atendemos situaciones habituales de cerrajería urgente en Madrid, especialmente en zonas próximas al eje Almagro-Chamberí y otras áreas urbanas donde son frecuentes los problemas de acceso en viviendas, oficinas y comunidades.
```

### Incorrecto

<small>§16.2</small>

```text
/cerrajero/almagro/cerrajero-urgente/
```

si Almagro no está aprobada como Expansion Area.

## Cuándo una zona pasa a página propia

<small>§17</small>

Una zona solo puede pasar de "señal GEO" a "URL propia" si cumple criterios más fuertes:

| Criterio | Necesario para página propia |
|---|---|
| Está geográficamente clara | Sí |
| Tiene demanda de búsqueda | Muy recomendable |
| Competidores la trabajan | Muy recomendable |
| Puede tener contenido único | Sí |
| No duplica la página de Madrid | Sí |
| No finge oficina física | Obligatorio |
| Tiene valor comercial | Sí |

Ejemplo:

```text
/madrid/chamberi/
```

o:

```text
/cerrajero/madrid/chamberi/cerrajero-urgente/
```

solo si Chamberí pasa a **Approved Expansion Area**.

## Aplicado a Rafael Calvo 40, Madrid

<small>§18</small>

| Zona | Decisión correcta |
|---|---|
| Madrid | Crea arquitectura base |
| Almagro | Señal GEO directa |
| Chamberí | Señal GEO directa |
| Salamanca | Candidata, validar proximidad/demanda/competencia |
| Retiro | Candidata, validar antes de usar fuerte |
| Centro | Candidata, no automática |
| Tetuán | Candidata, no automática |
| Chamartín | Candidata, no automática |
| Arganzuela | Candidata, no automática |

## Fórmula final

<small>§19</small>

```text
Dirección física → Main City → zonas directas → zonas candidatas → validación → uso en contenido → expansión solo si procede
```

En una frase:

```text
Una zona tiene sentido GEO si sale del ancla física o ayuda a reforzar la relevancia local de la Main City sin crear una falsa ubicación, y si además puede justificarse por proximidad, demanda, competencia o contexto real del servicio.
```

# Bloque V — Fuentes Internas GMB Crush usadas

## Fuentes internas GMB Crush usadas

<small>§20</small>

- Analysis Framework.pdf
- GMB CRUSH Universal AI Local SEO Framework Template
- Website Homepage AI Optimization Prompts/Framework
- Service Pages AI Optimization Prompts/Framework
- Location Pages AI Optimization Prompts/Framework
- GeoHub Pages AI Framework
- GeoArticle Pages AI Framework
- Additional Categories Pages AI Framework

> **Nota importante — GBP Services ≠ core services del sitio web:**
> Las categorías adicionales del Google Business Profile (como "Servicio de duplicado de llaves") pueden tener página propia en la web, pero **no forman parte de `core_services`**. La variable `core_services` define los 5 servicios principales que generan Service Overview, LBS y GeoArticles. Las Additional Categories con página propia se gestionan por separado mediante `additional_categories_with_page`. No mezclar ambos conjuntos.
