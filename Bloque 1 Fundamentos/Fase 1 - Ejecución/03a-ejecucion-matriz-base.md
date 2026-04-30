Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# Paso 3 — Matriz Base

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 13 outputs del Paso 3 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, reglas que aplican, checklist final y outputs consolidados.
> - **Bloque IV — Módulo doctrinal: GeoArticle Topics** explica el método de extracción de los topics (keyword research por servicio core).
> - **Bloque V — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 3

<small>§2</small>

Convertir el inventario calculado en Paso 2 en una **URL Matrix operativa** — una tabla donde cada URL del cluster ocupa una fila con todos los campos de producción (URL, H1, Meta Title, Schema, Priority, Phase, Status, Parent Page, Internal links, Notes).

**Outputs del paso:**

- **3.1** Spreadsheet Name — nombre del archivo/spreadsheet que contiene la matriz
- **3.2** GeoHub URL Style — Option A `/city/` o Option B `/category/city/` (decisión de diseño)
- **3.3** Additional Category Slugs — slugs URL-safe para las Additional Categories que necesitan página propia
- **3.4** URL Matrix completa — N filas (28 SEO + 1 auxiliar para Cerrajeros) con todos los campos rellenos
- **3.5** IDs por tipo de página — HP, SO-N, GH, LBS-N, AC-N, GA-N
- **3.6** Parent Page declarado por fila — jerarquía del cluster
- **3.7** Schema asignado desde la matriz — no en build-time
- **3.8** Enlaces internos Required por fila — linking contractual
- **3.9** Priority y Publish Phase por fila — orden y agrupación
- **3.10** Default Page Status — estado inicial de cada fila (Planned)
- **3.11** Notes estratégicas por fila — decisiones que no encajan en columnas estructuradas
- **3.12** Validación LCAs sin filas base — Local Coverage Areas no generan filas
- **3.13** Validación matriz cerrada antes de contenido — handoff a Paso 4 y Paso 15

**Errores que previene:**

- Crear URLs sin ID ni estado
- Perder la relación entre página padre y página hija
- Generar filas para Local Coverage Areas sin aprobación
- Olvidar schema o enlaces internos en la planificación
- Publicar páginas sin saber qué función cumplen
- Cambiar slugs durante la fase de redacción
- Mezclar Priority (importancia) con Publish Phase (orden de publicación)

**Cuándo se ejecuta:** después de Paso 2 cerrado (fórmula aplicada). Antes de Paso 4 (URL Rules) y Paso 15 (Redacción de contenido).

## Info heredada de pasos anteriores

<small>§3</small>

> Estos campos NO se deciden en Paso 3 — la IA los lee del paso indicado y los usa como input para construir la URL Matrix del Bloque III.

| Campo | Origen |
|---|---|
| Website Root Domain | Paso 1 §6.2 |
| Canonical Domain | Paso 1 §6.2 |
| Planned Primary GBP Category | Paso 1 §6.5 |
| Primary Category Slug | Paso 2 §6.2 |
| Main City | Paso 1 §6.7 |
| Main City Slug | Paso 2 §6.3 |
| Servicios principales (5 core services) | Paso 1 §6.9 |
| Service Slugs (S=5) | Paso 2 §6.4 |
| Additional Categories que necesitan página | Paso 1 §6.6 |
| Local Coverage Areas | Paso 1 §6.10 |
| Approved Expansion Areas | Paso 1 §6.11 |
| GeoArticles per Service (G) | Paso 1 §6.12 |

> Los outputs nuevos que se producen en Paso 3 (Spreadsheet Name, GeoHub URL Style, Additional Category Slugs) tienen sus propias secciones en Bloque III — §6.1, §6.2 y §6.3. Default Page Status y Default Priority son outputs de §6.10 y §6.9 respectivamente.

# Bloque II — Ejemplo rellenado para el Paso 3 — Matriz Base

<small>§4</small>

> Los 13 outputs del Paso 3 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 3.X declarado en §5.

### 3.1 — Spreadsheet Name

`Cerrajeros Madrid 24h – GMB Crush Website Architecture`

### 3.2 — GeoHub URL Style

Option A → `/madrid/`

### 3.3 — Additional Category Slugs

`duplicado-llaves` (1 slug, A=1)

### 3.4 — URL Matrix completa (28 filas SEO + 1 auxiliar)

| ID | URL | Tipo | Schema | Priority | Phase | Status |
|---|---|---|---|---|---|---|
| HP | `/` | Homepage | Organization + WebSite + LocalBusiness + FAQPage + Speakable | P1 | 1 | Planned |
| SO-1 | `/cerrajero/cerrajero-urgente/` | Service Overview | Service + WebPage + BreadcrumbList | P1 | 1 | Planned |
| SO-2 | `/cerrajero/apertura-puertas/` | Service Overview | Service + WebPage + BreadcrumbList | P1 | 1 | Planned |
| SO-3 | `/cerrajero/cambio-cerraduras/` | Service Overview | Service + WebPage + BreadcrumbList | P1 | 1 | Planned |
| SO-4 | `/cerrajero/cambio-bombines/` | Service Overview | Service + WebPage + BreadcrumbList | P1 | 1 | Planned |
| SO-5 | `/cerrajero/instalacion-cerraduras-seguridad/` | Service Overview | Service + WebPage + BreadcrumbList | P1 | 1 | Planned |
| GH | `/madrid/` | GeoHub | CollectionPage + BreadcrumbList | P1 | 1 | Planned |
| LBS-1 | `/cerrajero/madrid/cerrajero-urgente/` | LBS | LocalBusiness + BreadcrumbList | P1 | 1 | Planned |
| LBS-2 | `/cerrajero/madrid/apertura-puertas/` | LBS | LocalBusiness + BreadcrumbList | P1 | 1 | Planned |
| LBS-3 | `/cerrajero/madrid/cambio-cerraduras/` | LBS | LocalBusiness + BreadcrumbList | P1 | 1 | Planned |
| LBS-4 | `/cerrajero/madrid/cambio-bombines/` | LBS | LocalBusiness + BreadcrumbList | P1 | 1 | Planned |
| LBS-5 | `/cerrajero/madrid/instalacion-cerraduras-seguridad/` | LBS | LocalBusiness + BreadcrumbList | P1 | 1 | Planned |
| AC-1 | `/cerrajero/madrid/duplicado-llaves/` | Additional Category | Service + BreadcrumbList | P2 | 1 | Planned |
| GA-1 | `/madrid/cuanto-cuesta-un-cerrajero-urgente/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-2 | `/madrid/que-hacer-si-no-puedes-entrar-casa/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-3 | `/madrid/cuanto-tarda-un-cerrajero/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-4 | `/madrid/cuanto-cuesta-abrir-una-puerta/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-5 | `/madrid/que-hacer-si-te-dejas-las-llaves-dentro/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-6 | `/madrid/apertura-de-puertas-sin-romper-cerradura/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-7 | `/madrid/cuando-cambiar-la-cerradura-de-casa/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-8 | `/madrid/cambio-de-cerradura-tras-perder-llaves/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-9 | `/madrid/cerradura-nueva-o-reparacion/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-10 | `/madrid/cuando-cambiar-el-bombin/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-11 | `/madrid/bombin-antibumping-madrid/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-12 | `/madrid/cambio-de-bombin-sin-cambiar-cerradura/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-13 | `/madrid/mejores-cerraduras-de-seguridad-para-viviendas/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-14 | `/madrid/cerraduras-de-seguridad-para-comunidades/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-15 | `/madrid/instalar-cerradura-de-seguridad-en-puerta-blindada/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| AUX | `/contacto/` | Auxiliar | ContactPoint | P4 | 1 | Planned |

### 3.5 — IDs por tipo de página

| ID | URL | Tipo |
|---|---|---|
| HP | `/` | Homepage |
| SO-1 a SO-5 | `/cerrajero/{service}/` | Service Overview (5) |
| GH | `/madrid/` | GeoHub |
| LBS-1 a LBS-5 | `/cerrajero/madrid/{service}/` | Location-Based Service (5) |
| AC-1 | `/cerrajero/madrid/duplicado-llaves/` | Additional Category (A=1) |
| GA-1 a GA-15 | `/madrid/{topic}/` | GeoArticles (G×S=15) |
| AUX | `/contacto/` | Auxiliar |

### 3.6 — Parent Page declarado por fila

| ID | Parent Page |
|---|---|
| HP | – (root) |
| SO-1 a SO-5 | `/` (Homepage) |
| GH | `/` (Homepage) |
| LBS-1 a LBS-5 | `/cerrajero/{service}/` (su SO correspondiente) |
| AC-1 | `/madrid/` (GeoHub) |
| GA-1 a GA-15 | `/cerrajero/madrid/{matching service}/` (LBS correspondiente) |
| AUX | `/` (Homepage) |

### 3.7 — Schema asignado desde la matriz

| Page Type | Schema Required |
|---|---|
| Homepage | Organization + WebSite + LocalBusiness + FAQPage + Speakable |
| Service Overview | Service + WebPage + BreadcrumbList |
| GeoHub | CollectionPage + BreadcrumbList |
| Location-Based Service | LocalBusiness + BreadcrumbList |
| Additional Category | Service + BreadcrumbList |
| GeoArticle | Article + FAQPage + BreadcrumbList |
| Auxiliar (`/contacto/`) | ContactPoint |

### 3.8 — Enlaces internos Required por fila

Listado contractual de enlaces obligatorios por page type (detalle operativo en Paso 7):

| Page Type | Required outbound links |
|---|---|
| Homepage | 5 SO + 1 GeoHub + 1 AC + 1 contacto = 8 enlaces mínimos |
| Service Overview | LBS local + related services |
| GeoHub | 5 LBS + 1 AC + 15 GeoArticles = 21 enlaces |
| LBS | SO padre + GeoHub + related LBS + matching GAs |
| AC | GeoHub + LBS relacionados |
| GeoArticle | matching LBS + GeoHub |

### 3.9 — Priority y Publish Phase por fila

| Page Type | Priority | Phase |
|---|---|---|
| Homepage | P1 | Phase 1 |
| Service Overview | P1 | Phase 1 |
| GeoHub | P1 | Phase 1 |
| Location-Based Service | P1 | Phase 1 (o Phase 2 si dependencia bloqueada) |
| Additional Category | P2 | Phase 1 |
| GeoArticle | P3 | Phase 2 |
| Auxiliar | P4 | Phase 1 |

### 3.10 — Default Page Status

`Planned` (estado inicial de cada fila).

Ciclo de vida: `Planned → Draft → Ready for QA → Approved → Published`.

### 3.11 — Notes estratégicas por fila (ejemplos)

| ID | Notes |
|---|---|
| HP | Cliente solicita H1 con 'Madrid 24h' literal por reconocimiento de marca |
| LBS-1 | Consolida intención de Servicio de cerrajería de urgencia (categoría adicional cubierta) |
| AC-1 | Necesita keyword research específica para H1 antes de redacción |
| GA-1 a GA-15 | ⚠ Topics derivados de fórmula G×S, requieren validación con keyword research real (ver Bloque IV §9) |

### 3.12 — Validación LCAs sin filas base

| LCA | Tratamiento en matriz |
|---|---|
| Almagro, Chamberí (Direct) | Sin fila — viven en contenido y schema `areaServed` |
| Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad (Candidate) | Sin fila — viven en contenido y schema `areaServed` |

**Resultado:** 0 filas adicionales por LCA.

### 3.13 — Validación matriz cerrada antes de contenido

| Validación | Resultado para Cerrajeros |
|---|---|
| Una fila por URL | ✅ 28 filas SEO + 1 auxiliar |
| ID único por tipo | ✅ HP, SO-1..5, GH, LBS-1..5, AC-1, GA-1..15, AUX |
| Parent Page declarado | ✅ cada fila apunta a una URL existente o `–` (Homepage root) |
| Schema asignado desde matriz | ✅ no se decide en build-time |
| Internal links Required listados | ✅ contractual por tipo de página (ver Paso 7) |
| Anti-duplicación | ✅ Servicio de cerrajería de urgencia consolidada con LBS-1 |
| Matriz cerrada antes de contenido | ✅ todos los campos rellenos antes de Paso 15 (Redacción) |

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 13 outputs que el Paso 3 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `3.1`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Origen |
|---|---|---|---|
| 3.1 | Spreadsheet Name | String | Decisión de diseño |
| 3.2 | GeoHub URL Style | Enum (Option A / Option B) | Decisión de diseño |
| 3.3 | Additional Category Slugs | Lista de slugs URL-safe | GMB Crush ← Paso 1 §6.6 |
| 3.4 | URL Matrix completa | Tabla N filas × 20 columnas | GMB Crush |
| 3.5 | IDs por tipo de página | Strings únicos por fila | GMB Crush |
| 3.6 | Parent Page declarado por fila | URL del parent | GMB Crush |
| 3.7 | Schema asignado desde matriz | Schema Type(s) por fila | GMB Crush |
| 3.8 | Enlaces internos Required por fila | Lista de URLs internas | GMB Crush |
| 3.9 | Priority y Publish Phase por fila | P1-P4 + Phase 1-N | GMB Crush |
| 3.10 | Default Page Status | Enum (Planned / Draft / Published) | GMB Crush |
| 3.11 | Notes estratégicas por fila | String libre, opcional | Decisión de diseño |
| 3.12 | Validación LCAs sin filas base | Validation flag | GMB Crush |
| 3.13 | Validación matriz cerrada antes de contenido | Validation flag | GMB Crush |

## Reglas que Aplican

<small>§6</small>

> Esta sección desarrolla cada uno de los 13 outputs (3.1–3.13) con el mismo patrón: Explicación / Patrón o fórmula / Ejemplos correctos / Ejemplos incorrectos / Regla final / Validación operativa / Cómo se obtiene / Output del paso. Cada sub-sección §6.X corresponde 1:1 al output 3.X declarado en §5.

### 3.1 — Spreadsheet Name

<small>§6.1</small>

**Explicación**

El nombre del spreadsheet (Google Sheets, Airtable, Notion DB) que contendrá la URL Matrix del cluster. Identifica al cliente y al sistema GMB Crush. Se reutiliza en filenames de exports, referencias internas y handoffs entre operadores.

**Patrón o fórmula**

```text
[Business Name] – GMB Crush Website Architecture
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h – GMB Crush Website Architecture
```

**Ejemplos incorrectos**

```text
- URL Matrix v3 final.xlsx
- Sheet sin nombre
- Cliente1_matriz_2024 (no identifica al cliente real)
- Mezclar varios clientes en un solo spreadsheet
```

**Regla final**

```text
El spreadsheet name identifica al cliente y al sistema; reutilizable en filenames y referencias.
```

**Validación operativa**

El spreadsheet name se reutiliza en filenames de exports (`Cerrajeros Madrid 24h - URL Matrix - 2024-01.csv`), referencias entre docs (b-doc, briefs de contenido) y handoffs entre operadores. Una sola fórmula `[Business Name] – GMB Crush Website Architecture` mantiene rastreabilidad sin ambigüedad.

**Cómo se obtiene**

- **Fuente:** Decisión de diseño.
- **Método:** Aplicar la fórmula `[Business Name] – GMB Crush Website Architecture` usando el Business Name del Paso 1 §6.1.

**Output del paso**

- **Tipo:** String — nombre del spreadsheet/archivo.
- **Ejemplo (Cerrajeros Madrid 24h):** `Cerrajeros Madrid 24h – GMB Crush Website Architecture`.

### 3.2 — GeoHub URL Style

<small>§6.2</small>

**Explicación**

La URL del GeoHub de la Main City puede tener dos formas según preferencia de arquitectura. Esta decisión afecta a TODAS las URLs tipo GeoHub del cluster y debe tomarse antes de generar la matriz. Cambiarla mid-build obliga a regenerar URLs y redirects.

**Patrón o fórmula**

```text
Option A: /city/             → ej: /madrid/         (GeoHub limpio)
Option B: /category/city/    → ej: /cerrajero/madrid/ (GeoHub bajo categoría)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Option A: /madrid/
```

**Ejemplos incorrectos**

```text
- Mezclar Option A y Option B en el mismo cluster
- Cambiar de Option A a Option B después de publicar URLs
- Crear /madrid/ y /cerrajero/madrid/ ambas como GeoHub
```

**Regla final**

```text
Una sola GeoHub URL Style consistente en todo el cluster, decidida antes de generar URLs.
```

**Validación operativa**

La decisión es contractual con el Paso 4 §9 (Main City GeoHub URL Style). Por defecto se usa Option A (URL más corta y memorable). Option B se elige solo si el cliente quiere consolidar todo el cluster bajo `/category/`. Una vez elegida, aplica idéntica a todas las URLs tipo GeoHub.

**Cómo se obtiene**

- **Fuente:** Decisión de diseño.
- **Método:** Elegir Option A (default) salvo que el cliente tenga razones específicas para anidar el GeoHub bajo la Primary Category (Option B). La decisión debe tomarse antes de generar las URLs base.

**Output del paso**

- **Tipo:** Enum — Option A o Option B.
- **Ejemplo (Cerrajeros Madrid 24h):** Option A → `/madrid/`.

### 3.3 — Additional Category Slugs

<small>§6.3</small>

**Explicación**

Las Additional Categories que necesitan página propia (Paso 1 §6.6) necesitan slugs URL-safe específicos. La transformación es la misma que la del Paso 2 §6.2 Slug Generation, pero aplicada al subconjunto de Additional Categories no cubiertas por core services.

**Patrón o fórmula**

```text
additional_category_slug = slugify(additional_category_name)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Servicio de duplicado de llaves → duplicado-llaves
```

**Ejemplos incorrectos**

```text
- Slugs largos: servicio-de-duplicado-de-llaves
- Slugs con tildes: cerrajería-urgente
- Slugs duplicados con core service slugs
- Inventar slugs que no derivan del nombre real
```

**Regla final**

```text
Cada Additional Category con página propia tiene un slug derivado limpio y único.
```

**Validación operativa**

Aplicar slugify a cada Additional Category que necesita página propia (heredada del Paso 1 §6.6, validada en Paso 2 §6.7 Variable A). Validar que los slugs no colisionen con Service Slugs ni Primary Category Slug. Solo se generan slugs para Additional Categories efectivas (A); las cubiertas por core services no necesitan slug propio.

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredados del Paso 1 §6.6.
- **Método:** Aplicar la transformación slugify (ver Paso 2 §6.2) a cada Additional Category que necesita página propia. Validar que los slugs no colisionen con Service Slugs ni Primary Category Slug.

**Output del paso**

- **Tipo:** Lista de slugs URL-safe (uno por Additional Category con página propia).
- **Ejemplo (Cerrajeros Madrid 24h):** `duplicado-llaves` (1 slug, A=1).

### 3.4 — URL Matrix completa

<small>§6.4</small>

**Explicación**

La URL Matrix completa es el output central del Paso 3. Convierte arquitectura en producción: cada URL del cluster ocupa una fila con todos los campos de producción (URL, H1, Meta Title, Schema, Priority, Phase, Status, Parent Page, Internal links, Notes). Si una página no tiene fila, no existe dentro del sistema operativo.

**Patrón o fórmula**

```text
One URL = one row = one page type = one function

Total filas = Total inventario base (Paso 2 §6.10) + 1 auxiliar (/contacto/)
            = (1 + S + 1 + S + A + G×S) + 1
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
28 filas SEO base + 1 auxiliar = 29 filas totales

Distribución:
  1 Homepage (HP)
  5 Service Overview (SO-1..5)
  1 GeoHub (GH)
  5 LBS (LBS-1..5)
  1 Additional Category (AC-1)
  15 GeoArticles (GA-1..15)
  1 Auxiliar (AUX = /contacto/)
```

**Ejemplos incorrectos**

```text
- Crear contenido sin fila
- Crear URL fuera de la matriz
- Publicar sin ID
- Crear filas para Almagro, Salamanca y Retiro como cobertura sin aprobación
- Añadir ideas de artículos sin URL
- Duplicar una misma URL con dos IDs
- Mezclar /contacto/ dentro del conteo SEO base
```

**Regla final**

```text
Cada URL real del cluster ocupa exactamente una fila con todos sus campos rellenos. La matriz es contrato operativo, no lista de ideas.
```

**Validación operativa**

La matriz base no es una lista de ideas; es una tabla de producción. Cada fila debe corresponder a una URL real que se va a crear o mantener. Si una zona solo se menciona dentro del contenido, no debe aparecer como fila. La matriz es el handoff principal al Paso 4 (URL Rules valida patrones), Paso 7 (Internal Linking consume internal_links_required) y Paso 15 (Redacción usa H1, Meta Title, schema).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Para cada URL del cluster (heredada de Paso 2 §6.10 Tabla de inventario base), crear una fila con todos los campos obligatorios (§6.4.1 Columnas obligatorias listadas más abajo). Una URL = una fila exacta. Las URLs no aprobadas (LCAs sin AEA) NO se incluyen.

**Output del paso**

- **Tipo:** N filas en el spreadsheet (donde N = total de URLs del cluster + auxiliares).
- **Ejemplo (Cerrajeros Madrid 24h):** 28 filas SEO + 1 auxiliar = 29 filas. Ver tabla completa en §4 sub-sección 3.4.

#### Columnas obligatorias de la URL Matrix

| Columna | Nombre | Función |
|---|---|---|
| A | ID | Identificador único |
| B | Page Type | Tipo de página GMB Crush |
| C | Parent Page | Página padre |
| D | Service | Servicio |
| E | Service Slug | Slug del servicio |
| F | Main City | Ciudad principal |
| G | Main City Slug | Slug de la ciudad |
| H | Additional Category | Categoría adicional, si aplica |
| I | Local Coverage Areas | Zonas mencionadas en contenido |
| J | Approved Expansion Area | Solo si aplica |
| K | URL | URL final |
| L | H1 | H1 recomendado |
| M | Meta Title | Title SEO |
| N | Meta Description | Descripción SEO |
| O | Schema Type | Schema recomendado |
| P | Enlaces internos Required | Enlaces obligatorios |
| Q | Priority | P1/P2/P3/P4 |
| R | Publish Phase | Fase |
| S | Status | Estado |
| T | Notes | Notas estratégicas |

#### Patrones URL por tipo de página aplicados a la matriz

```text
Homepage             /
Service Overview     /{primary-cat-slug}/{service-slug}/
GeoHub Main City     /{main-city-slug}/                                  (Option A; Option B → /{primary-cat-slug}/{main-city-slug}/)
LBS                  /{primary-cat-slug}/{main-city-slug}/{service-slug}/
Additional Category  /{primary-cat-slug}/{main-city-slug}/{additional-slug}/
GeoArticle           /{main-city-slug}/{topic-slug}/
```

> **Regla:** Additional Category Pages siguen el mismo patrón que LBS (`/cat/city/slug/`), NO el patrón GeoArticle (`/city/slug/`). Esto las mantiene como páginas comerciales bajo la categoría principal, con la ciudad como nivel intermedio.

### 3.5 — IDs por tipo de página

<small>§6.5</small>

**Explicación**

Los IDs permiten filtrar, auditar y producir por lotes. Cada fila tiene un ID único derivado del tipo de página y su orden secuencial.

**Patrón o fórmula**

```text
HP                    (sin sufijo — solo hay una Homepage)
GH                    (sin sufijo — solo hay un GeoHub Main City)
SO-N, LBS-N, AC-N, GA-N    (correlativo simple, N empieza en 1)
AUX                   (página auxiliar, ej. /contacto/)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
HP    identifica /
SO-1  identifica /cerrajero/cerrajero-urgente/
LBS-1 identifica /cerrajero/madrid/cerrajero-urgente/
AC-1  identifica /cerrajero/madrid/duplicado-llaves/
GA-1  identifica /madrid/cuanto-cuesta-un-cerrajero-urgente/
AUX   identifica /contacto/
```

**Ejemplos incorrectos**

```text
- IDs aleatorios (A1B2C3)
- No usar IDs
- Mismo ID para varias URLs
- Repetir LBS-001 para varias páginas
- No diferenciar artículos de páginas comerciales
- IDs largos derivados del slug (cerrajero-urgente-madrid-id)
```

**Regla final**

```text
Cada fila tiene un ID único derivado del tipo de página y su contenido.
```

**Validación operativa**

Cada fila necesita un ID legible para controlar producción, QA y enlaces. El ID debe indicar el tipo de página y su orden, sin depender de títulos largos o slugs complejos. La numeración N es secuencial dentro del tipo (SO-1, SO-2, ..., SO-S; LBS-1, ..., LBS-S; GA-1, ..., GA-N donde N = G×S).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Asignar ID por tipo según la nomenclatura GMB Crush: `HP`, `SO-N`, `GH`, `LBS-N`, `AC-N`, `GA-N`. El número N es secuencial dentro del tipo, ordenado por importancia o por orden de aparición del servicio en Paso 1 §6.9.

**Output del paso**

- **Tipo:** String único por fila (formato `tipo-N`).
- **Ejemplo (Cerrajeros Madrid 24h):** `HP`, `SO-1`, `SO-2`, ..., `LBS-1`, ..., `GA-15`, `AUX`.

### 3.6 — Parent Page declarado por fila

<small>§6.6</small>

**Explicación**

Cada página debe tener una relación de dependencia jerárquica. Esto evita páginas huérfanas y permite construir el silo de internal linking del Paso 7.

**Patrón o fórmula**

```text
Page Type → Parent Page → Internal Link Required (mínimo desde el padre)

Jerarquía:
  Homepage (root, sin parent)
  ├─ Service Overview (parent = Homepage)
  ├─ GeoHub (parent = Homepage)
  │   ├─ Location-Based Service (parent = SO correspondiente)
  │   │   └─ GeoArticle (parent = LBS correspondiente)
  │   └─ Additional Category (parent = GeoHub)
  └─ Auxiliar (parent = Homepage)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
HP    parent = – (root)
SO-1  parent = / (Homepage)
GH    parent = / (Homepage)
LBS-1 parent = /cerrajero/cerrajero-urgente/ (SO-1)
AC-1  parent = /madrid/ (GeoHub)
GA-1  parent = /cerrajero/madrid/cerrajero-urgente/ (LBS-1)
AUX   parent = / (Homepage)
```

**Ejemplos incorrectos**

```text
- GeoArticle sin service page
- Additional Category sin GeoHub
- Service Overview sin homepage como parent
- Dejar Parent Page vacío en páginas locales
- Asignar homepage como padre de todos los artículos (saltarse niveles)
- Usar una página inexistente como parent
```

**Regla final**

```text
Cada fila debe declarar Parent Page existente; no hay páginas huérfanas en la matriz.
```

**Validación operativa**

Cada página que no sea homepage necesita una página padre que exista en la propia matriz. Esto ayuda a construir el silo y a saber desde dónde se enlazará cada URL. La regla aplica también para validar Publish Phase (§6.9): un GeoArticle no puede publicarse antes de que su LBS padre esté lista.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Cada fila declara explícitamente su Parent Page (la URL padre en la jerarquía). Homepage es root (parent vacío o `–`); el resto debe apuntar a una URL existente en la propia matriz.

**Output del paso**

- **Tipo:** String — URL del parent (vacío solo para Homepage).
- **Ejemplo (Cerrajeros Madrid 24h):** Homepage parent = `–`. SO Cerrajero urgente parent = `/`. LBS Cerrajero urgente Madrid parent = `/cerrajero/cerrajero-urgente/`.

### 3.7 — Schema asignado desde la matriz

<small>§6.7</small>

**Explicación**

La matriz debe definir el schema antes de producir contenido. Esto evita que el implementador decida schema en build-time y se salte páginas locales sin LocalBusiness o GeoArticles sin Article.

**Patrón o fórmula**

```text
Page Type → Schema Required → QA Schema en Paso 8

Mapeo doctrinal:
  Homepage              → Organization + WebSite + LocalBusiness + FAQPage + Speakable
  Service Overview      → Service + WebPage + BreadcrumbList
  GeoHub                → CollectionPage + BreadcrumbList
  Location-Based Service → LocalBusiness + BreadcrumbList
  Additional Category   → Service + BreadcrumbList
  GeoArticle            → Article + FAQPage + BreadcrumbList
  Auxiliar (/contacto/) → ContactPoint
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1 (/cerrajero/madrid/cerrajero-urgente/) usa LocalBusiness + BreadcrumbList
GA-1 (/madrid/cuanto-cuesta-un-cerrajero-urgente/) usa Article + FAQPage + BreadcrumbList
HP (/) usa Organization + WebSite + LocalBusiness + FAQPage + Speakable
```

**Ejemplos incorrectos**

```text
- Schema decidido al final
- Mismo schema para todo
- Sin schema en GeoArticles
- Dejar schema vacío hasta el final
- Usar Article schema en una landing comercial
- Usar LocalBusiness con dirección falsa en una zona de cobertura
- Olvidar BreadcrumbList en páginas internas
```

**Regla final**

```text
Cada fila tiene Schema Type asignado desde la matriz; el implementador no decide schema.
```

**Validación operativa**

La matriz debe incluir schema requerido por tipo de página para que el equipo no lo decida al final. Esto evita que páginas locales salgan sin LocalBusiness, Service, Article o BreadcrumbList. El Paso 8 (Schema Markup) consume directamente este campo; cualquier schema añadido fuera de matriz debe propagar a la matriz para mantener consistencia.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Cada fila declara Schema Type según el page type según el mapeo doctrinal (Homepage → Organization + LocalBusiness; SO → Service; GeoHub → CollectionPage; LBS → LocalBusiness + BreadcrumbList; AC → Service; GA → Article + FAQPage). El implementador no decide schema en build time.

**Output del paso**

- **Tipo:** Schema Type(s) por fila (uno o más, separados por `+`).
- **Ejemplo (Cerrajeros Madrid 24h):** Homepage → `Organization + LocalBusiness + WebSite + FAQPage + Speakable`. SO → `Service + WebPage + BreadcrumbList`. LBS → `LocalBusiness + BreadcrumbList`. GA → `Article + FAQPage + BreadcrumbList`.

### 3.8 — Enlaces internos Required por fila

<small>§6.8</small>

**Explicación**

La matriz debe listar enlaces obligatorios para evitar páginas aisladas. El linking es contractual: si los enlaces no están en la matriz, las páginas pueden publicarse aisladas y el silo pierde fuerza.

**Patrón o fórmula**

```text
Source URL → Required Links (mínimo) → QA de enlaces en Paso 7

Por page type:
  Homepage         → 5 SO + 1 GeoHub + 1 AC + 1 contacto = 8 links mínimos
  Service Overview → LBS local + related SOs
  GeoHub           → Todas las LBS + AC + GAs (silo Main City)
  LBS              → SO padre + GeoHub + related LBS + matching GAs
  Additional Cat.  → GeoHub + LBS relacionados
  GeoArticle       → matching LBS + GeoHub
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1 (/cerrajero/madrid/cerrajero-urgente/) requiere enlaces a:
  - /cerrajero/cerrajero-urgente/ (SO padre)
  - /madrid/ (GeoHub)
  - /cerrajero/madrid/apertura-puertas/ (related LBS)
  - /cerrajero/madrid/cambio-cerraduras/ (related LBS)
  - /madrid/cuanto-cuesta-un-cerrajero-urgente/ (matching GA)
  - /madrid/que-hacer-si-no-puedes-entrar-casa/ (matching GA)
```

**Ejemplos incorrectos**

```text
- Solo footer links
- Sin enlace al GeoHub
- Sin enlace al servicio padre
- Publicar páginas sin enlaces obligatorios
- Enlazar a áreas de cobertura sin URL (LCAs sin AEA)
- Usar solo enlaces de footer
- LBS sin links a related services en Main City
```

**Regla final**

```text
Cada fila lista los enlaces internos requeridos; el linking es contractual, no opcional.
```

**Validación operativa**

La matriz debe listar enlaces obligatorios para cada URL. Sin esta columna, las páginas pueden publicarse aisladas y el sistema pierde fuerza de silo. El detalle operativo de qué enlaces requiere cada page type está en Paso 7 (Internal Linking Rules); la matriz captura el listado contractual para QA.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Cada fila lista los enlaces internos obligatorios (internal_links_required) según el internal linking framework (Paso 7). El linking es contractual: ausentes los enlaces, la página queda incompleta.

**Output del paso**

- **Tipo:** Lista de URLs internas obligatorias por fila.
- **Ejemplo (Cerrajeros Madrid 24h):** SO Cerrajero urgente → enlaces a `/`, `/madrid/`, `/cerrajero/madrid/cerrajero-urgente/`, otras SO. LBS Cerrajero urgente Madrid → 6 enlaces (SO padre + GeoHub + 2 related LBS + 2 matching GAs).

### 3.9 — Priority y Publish Phase por fila

<small>§6.9</small>

**Explicación**

Cada fila debe tener prioridad y fase. La matriz no es solo inventario, también es cola de producción. Priority mide importancia estratégica; Publish Phase mide cuándo se publica (puede estar bloqueado por dependencias del Parent Page).

**Patrón o fórmula**

```text
Priority Tier (P1-P4) + Dependency (Parent Page existe?) → Publish Phase

Mapeo default por page type:
  Homepage              → P1, Phase 1
  Service Overview      → P1, Phase 1
  GeoHub                → P1, Phase 1
  Location-Based Service → P1, Phase 1 (Phase 2 si SO padre no listo)
  Additional Category   → P2, Phase 1
  GeoArticle            → P3, Phase 2 (espera a LBS padre)
  Auxiliar              → P4, Phase 1
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
GA-1 (cuanto-cuesta-un-cerrajero-urgente) puede ser P3 (importancia media),
pero queda en Phase 2 porque primero deben existir:
  - /madrid/ (GeoHub, P1 Phase 1)
  - /cerrajero/madrid/cerrajero-urgente/ (LBS-1 padre, P1 Phase 1)
```

**Ejemplos incorrectos**

```text
- Todas P1 (no hay priorización)
- Sin fase asignada
- Publicar según intuición
- Publicar GeoArticles P3 antes de landings P1
- Confundir score alto con listo para publicar
- No marcar páginas bloqueadas por dependencia
- Mezclar Priority (importancia) con Publish Phase (orden)
```

**Regla final**

```text
Priority y Publish Phase son campos separados; nunca se confunden ni se mezclan.
```

**Validación operativa**

La prioridad mide importancia estratégica; la fase mide cuándo se publica. Una página P1 puede estar bloqueada si su padre no existe. La matriz debe incluir ambos campos para evitar publicar por impulso. El Paso 10 (Producción en fases) consume Publish Phase para construir el calendario.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Priority captura el orden de importancia (P1 alta → P4 baja); Publish Phase captura cuándo se publica (Phase 1, 2, 3...). Default Priority del intake aplica a filas sin override explícito. Son dos campos independientes que NUNCA se mezclan. Validar dependencias antes de asignar Phase: si el Parent Page (§6.6) no existe, la fila se mueve a Phase posterior.

**Output del paso**

- **Tipo:** Priority (P1-P4) + Publish Phase (Phase 1-N) por fila.
- **Ejemplo (Cerrajeros Madrid 24h):** Homepage = P1, Phase 1. SO core services = P1, Phase 1. GeoHub = P1, Phase 1. LBS = P1, Phase 1. AC = P2, Phase 1. GeoArticles = P3, Phase 2.

### 3.10 — Default Page Status

<small>§6.10</small>

**Explicación**

El estado permite saber si una página está planificada, en borrador, en QA o publicada. Define el ciclo de vida operativo de cada fila a lo largo del proyecto.

**Patrón o fórmula**

```text
Ciclo de vida:
Planned → Draft → Ready for QA → Approved → Published

Default al cerrar la matriz: Planned (todas las filas)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h marca todas las 28 filas SEO + 1 auxiliar como Planned
hasta que el contenido y los links estén listos para Draft.
```

**Ejemplos incorrectos**

```text
- Publicada sin QA
- Borrador sin responsable
- Estado vacío
- Usar estados vagos como "en proceso"
- Publicar sin pasar por Ready for QA
- No actualizar estado después de QA
- Saltar de Planned a Published sin pasar por Draft / Ready for QA
```

**Regla final**

```text
Status refleja el estado real de cada fila a lo largo del ciclo de vida de la página.
```

**Validación operativa**

Cada URL necesita un estado para controlar el flujo de producción. Planned, Draft, Ready for QA, Approved y Published son estados suficientes para saber qué hacer con cada fila. El cierre de la matriz (Paso 3 §6.13) deja todas las filas en Planned; los pasos posteriores actualizan según avance: Paso 15 Redacción → Draft, Paso 16 QA → Ready for QA, Paso 18 Deploy → Published.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Status refleja el estado real de cada fila a lo largo del ciclo de vida (Planned → Draft → Published). Default Page Status del intake aplica a filas nuevas; se actualiza manualmente al avanzar de fase.

**Output del paso**

- **Tipo:** Enum — Planned / Draft / Ready for QA / Approved / Published.
- **Ejemplo (Cerrajeros Madrid 24h):** Default Page Status = `Planned`. Cada fila arranca como Planned hasta que se redacte.

### 3.11 — Notes estratégicas por fila

<small>§6.11</small>

**Explicación**

La columna Notes registra decisiones estratégicas que no encajan en columnas estructuradas: razón de un Priority anómalo, dependencia con otro paso, observación del cliente, excepción a la doctrina, etc. Es el campo libre que evita que la matriz pierda contexto sobre por qué cada fila existe.

**Patrón o fórmula**

```text
Decisión estratégica → Notes → trazabilidad para QA y handoffs
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Notes ejemplos:
  HP    → "Cliente solicita H1 con 'Madrid 24h' literal por reconocimiento de marca"
  LBS-1 → "Consolida intención de Servicio de cerrajería de urgencia (categoría adicional cubierta)"
  AC-1  → "Necesita keyword research específica para H1 antes de redacción"
  GA-1..GA-15 → "⚠ Topics derivados de fórmula G×S, requieren validación con keyword research real (Bloque IV §9)"
```

**Ejemplos incorrectos**

```text
- Dejar notas vacías en páginas complejas
- No documentar por qué una categoría adicional se consolida
- No indicar Local Coverage Areas relevantes
- Notes con información redundante (que ya está en otras columnas)
```

**Regla final**

```text
Las Notes capturan decisiones estratégicas que no encajan en columnas estructuradas.
```

**Validación operativa**

La columna Notes debe registrar por qué una página existe, qué categoría soporta, si consolida una categoría adicional o qué cobertura local debe mencionarse. Esto ayuda a evitar repetir discusiones cuando el operador o el cliente vuelven a la matriz semanas después. Las notas son opcionales pero recomendadas para cualquier fila con contexto no estructurado.

**Cómo se obtiene**

- **Fuente:** Decisión de diseño.
- **Método:** Cada fila tiene un campo Notes opcional para capturar decisiones que no encajan en columnas estructuradas: razón de un Priority anómalo, dependencia con otro paso, observación del cliente, excepción a la doctrina, etc.

**Output del paso**

- **Tipo:** String libre, opcional, por fila.
- **Ejemplo (Cerrajeros Madrid 24h):** Homepage Notes = `Cliente solicita H1 con 'Madrid 24h' literal por reconocimiento de marca`.

### 3.12 — Validación LCAs sin filas base

<small>§6.12</small>

**Explicación**

Las Local Coverage Areas (Paso 1 §6.10) son zonas seleccionadas como señales GEO. NO generan filas en la matriz base mientras no sean Approved Expansion Areas (Paso 1 §6.11). Esta validación garantiza que la matriz no se infla con URLs no aprobadas.

**Patrón o fórmula**

```text
Local Coverage Areas (Direct + Candidate) → contenido + schema areaServed
                                          ↛ filas en matriz

Para cada LCA: 0 filas adicionales en la matriz base.
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LCAs declaradas (Paso 1 §6.10):
  Direct: Almagro, Chamberí
  Candidate: Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad

Filas adicionales generadas: 0

Tratamiento en matriz:
  Columna I (Local Coverage Areas) — listadas como contenido para LBS, GeoHub, GAs
  Schema areaServed (Paso 8) — incluye TODAS las LCAs declaradas
  URL — NO se generan /almagro/, /chamberi/, etc.
```

**Ejemplos incorrectos**

```text
- GH-002 /almagro/ sin aprobación
- LBS para Salamanca en fase base
- GeoArticle de Retiro sin landing
- Poner Almagro en la columna City sin URL aprobada
- Crear slugs de cobertura en la matriz base
- Mezclar ciudad principal y zonas de cobertura en el mismo campo
```

**Regla final**

```text
Las Local Coverage Areas no generan filas en la matriz base; refuerzan contenido y schema.
```

**Validación operativa**

En la matriz base, el campo Main City (columna F) debe corresponder a la Main City del Paso 1 §6.7. Las Local Coverage Areas (columna I) listan las zonas mencionadas en contenido pero NO en path. Esta validación cruza con Paso 4 §13 (LCAs no generan URLs) y Paso 6 §6 (Principio 2 — LCAs enriquecen contenido). Para que una LCA pase a fila, debe pasar antes a AEA en Paso 1 §6.11.

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso 1 §6.10 Local Coverage Areas.
- **Método:** No crear filas en la matriz base para LCAs. La columna geográfica (Main City) usa la Main City (Paso 1 §6.7). Las LCAs aparecen en columna Local Coverage Areas (texto) y schema `areaServed` (Paso 8), no como URLs.

**Output del paso**

- **Tipo:** Validation flag — 0 filas adicionales por LCA en la matriz base.
- **Ejemplo (Cerrajeros Madrid 24h):** 0 filas extra para Almagro, Chamberí, Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad. Validación: OK.

### 3.13 — Validación matriz cerrada antes de contenido

<small>§6.13</small>

**Explicación**

La URL Matrix se cierra (todos los campos rellenos para todas las filas) ANTES de empezar redacción de contenido (Paso 15) o construcción (Paso 17). La matriz es el contrato operativo entre arquitectura, contenido, schema, enlaces y publicación. Cambiar la matriz mid-build obliga a reabrirla y reaplicar QA.

**Patrón o fórmula**

```text
URL Matrix aprobada (todos los campos rellenos) → briefs → contenido → QA

Validación: para cada fila, todos los 20 campos obligatorios deben tener valor (puede ser "–" si no aplica).
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h aprueba primero sus 28 URLs base + 1 auxiliar antes de
redactar los textos de homepage, servicios, GeoHub y GeoArticles.

Estado al cierre:
  29 filas con 20 columnas rellenas cada una = 580 celdas operativas
  Status: todas en Planned
  Hand-off: listo para Paso 4 (URL Rules), Paso 7 (Internal Linking) y Paso 15 (Redacción)
```

**Ejemplos incorrectos**

```text
- Redactar páginas sin saber si existen en la matriz
- Crear nuevos slugs durante escritura
- Cambiar page type sin actualizar matriz
- Empezar Paso 15 con la matriz a medio rellenar
- Tener filas con Schema vacío al iniciar redacción
- Tener Internal links Required pendientes al iniciar Paso 17
```

**Regla final**

```text
La matriz base se cierra antes de empezar contenido; un cambio aguas abajo obliga a reabrirla.
```

**Validación operativa**

No se debe escribir contenido página por página sin haber cerrado la matriz. La matriz es el contrato operativo entre arquitectura, contenido, schema, enlaces y publicación. Cualquier cambio aguas abajo obliga a reabrir la matriz, aplicar el cambio en la fila correspondiente y reaplicar QA. Esto evita que la matriz quede desincronizada con el sitio publicado.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** La URL Matrix se cierra (todos los campos rellenos para todas las filas) ANTES de empezar redacción de contenido (Paso 15) o construcción (Paso 17). Cualquier cambio aguas abajo obliga a reabrir la matriz y reaplicar QA. Validar que las 20 columnas obligatorias (§6.4) tienen valor en cada fila.

**Output del paso**

- **Tipo:** Validation flag — matriz cerrada (todos los campos rellenos).
- **Ejemplo (Cerrajeros Madrid 24h):** Matriz cerrada con 29 filas (28 SEO + 1 AUX), todos los 20 campos rellenos, antes de iniciar Paso 15 Redacción. Validación: OK.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 3 y avanzar al Paso 4 (URL Rules) o Paso 15 (Redacción). Cada ☐ es un check que debe pasar antes del handoff.

### Validación de outputs declarativos

- ☐ Spreadsheet Name (3.1) sigue la fórmula `[Business Name] – GMB Crush Website Architecture`
- ☐ GeoHub URL Style (3.2) elegido (Option A o B) y aplicado consistentemente
- ☐ Additional Category Slugs (3.3) validados contra Service Slugs (sin colisiones)
- ☐ URL Matrix completa (3.4) con N filas = total inventario base + auxiliares

### Validación de campos por fila

- ☐ ID único por fila (3.5) en formato `tipo-N`
- ☐ Parent Page declarado (3.6) y existente en la matriz
- ☐ Schema asignado (3.7) según mapeo doctrinal por page type
- ☐ Enlaces internos Required listados (3.8) según Paso 7
- ☐ Priority y Publish Phase asignados (3.9) — campos separados, no mezclados
- ☐ Status inicial = Planned (3.10) en todas las filas

### Validación de doctrina

- ☐ Notes estratégicas (3.11) capturadas para filas con contexto especial
- ☐ Local Coverage Areas SIN filas base (3.12) — verificar columna Main City = Main City declarada
- ☐ Matriz cerrada antes de contenido (3.13) — todos los 20 campos rellenos antes de Paso 15

## Outputs Consolidados

<small>§8</small>

> Tabla final con valores reales para Cerrajeros Madrid 24h y status de cada output. Los IDs (`3.1`–`3.13`) coinciden con los declarados en §5.

| ID | Output | Valor (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|
| 3.1 | Spreadsheet Name | `Cerrajeros Madrid 24h – GMB Crush Website Architecture` | confirmed |
| 3.2 | GeoHub URL Style | Option A → `/madrid/` | confirmed |
| 3.3 | Additional Category Slugs | `duplicado-llaves` (1 slug, A=1) | confirmed |
| 3.4 | URL Matrix completa | 28 filas SEO + 1 auxiliar = 29 filas | confirmed |
| 3.5 | IDs por tipo de página | HP, SO-1..5, GH, LBS-1..5, AC-1, GA-1..15, AUX | confirmed |
| 3.6 | Parent Page declarado por fila | Cada fila apunta a URL existente o `–` | confirmed |
| 3.7 | Schema asignado desde matriz | Mapeo doctrinal aplicado a 29 filas | confirmed |
| 3.8 | Enlaces internos Required por fila | Listado contractual por page type | confirmed |
| 3.9 | Priority y Publish Phase por fila | P1-P4 + Phase 1-2 según page type | confirmed |
| 3.10 | Default Page Status | `Planned` (todas las 29 filas) | confirmed |
| 3.11 | Notes estratégicas por fila | Sample notes documentadas | confirmed |
| 3.12 | Validación LCAs sin filas base | 0 filas extra para 10 LCAs (Almagro, Chamberí, Salamanca, etc.) | OK |
| 3.13 | Validación matriz cerrada antes de contenido | 29 filas × 20 columnas = 580 celdas rellenas | OK |

# Bloque IV — Módulo doctrinal: GeoArticle Topics

## GeoArticle Topics — método de extracción

<small>§9</small>

### Explicación

<small>§9.1</small>

Los topics de GeoArticle no se inventan: se extraen mediante keyword research por servicio core. La fórmula maestra del Paso 2 fija la cantidad (G × S = N artículos), pero los temas concretos requieren validación con datos reales de búsqueda antes de producirse. Sin keyword research el GeoArticle nace sin demanda real y se vuelve thin content.

### Patrón o método

<small>§9.2</small>

```text
Por cada core service (Paso 1 §6.9, S=5 servicios):

1. Ejecutar keyword research con volumen ≥ X impresiones/mes
   y dificultad ≤ Y (umbrales del cliente / sector).
2. Filtrar queries con intent informativo:
   - cómo, qué, cuándo, por qué, cuánto, dónde, cuál, mejor.
3. Excluir queries con intent transaccional o que coincidan
   con la query de la LBS (anti-canibalización Paso-04 §19).
4. Seleccionar G topics por servicio (G=3 por defecto, Paso 1 §6.12):
   - Priorizar volumen alto + dificultad baja.
   - Asegurar complementariedad: cada topic responde una intención
     distinta dentro del mismo servicio.
5. Generar el slug del topic:
   - Base = la query como apareció en keyword research.
   - Normalizar siguiendo Paso-04 §17 + Paso-04 §18 + Paso-04 §19 (lowercase, sin acentos,
     guiones medios, sin adjetivos SEO vacíos).
6. Construir la URL del GeoArticle:
   - Patrón: /[main-city]/[topic-slug]/ (Paso 4 §12).
```

### Ejemplo correcto con Cerrajeros Madrid 24h

<small>§9.3</small>

15 GeoArticles = 5 servicios core × G=3 topics. Ver listado completo en §10.1.

### Ejemplos incorrectos

<small>§9.4</small>

```text
- Inventar topics por intuición sin datos de búsqueda
- Usar el mismo topic para varios servicios (canibalización)
- Crear GeoArticles con intent transaccional que ya cubre la LBS
- Topics con dificultad muy alta sin volumen que la justifique
- Slug que no es la query real (manipulado para SEO)
- GeoArticles sin servicio core asignado (huérfanos)
```

### Regla final

<small>§9.5</small>

```text
Los topics de GeoArticle se descubren con keyword research por servicio
core. Cantidad fija por fórmula, contenido validado por datos reales.
```

# Bloque V — Fuentes Internas GMB Crush usadas

## Fuentes internas GMB Crush usadas

<small>§10</small>

- Analysis Framework.pdf
- GMB CRUSH Universal AI Local SEO Framework Template
- Website Homepage AI Optimization Prompts/Framework
- Service Pages AI Optimization Prompts/Framework
- Location Pages AI Optimization Prompts/Framework
- GeoHub Pages AI Framework
- GeoArticle Pages AI Framework
- Additional Categories Pages AI Framework

### GeoArticles completos (15)

<small>§10.1</small>

> **Aviso de trazabilidad:** estos 15 títulos son un primer borrador derivado de la fórmula G × S = 15 y de la lógica del servicio. **No vienen de keyword research real**. Antes de producirlos hay que validar volumen de búsqueda, dificultad y oportunidad competitiva por título según el método del Bloque IV §9.2. La fórmula garantiza la cantidad; los temas concretos requieren validación.

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
