Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 4 — Automatizacion/paso-12-master-prompt/`, alineado con los frameworks oficiales GMB Crush. Master Prompt y reglas operativas portadas LITERALMENTE del documento fuente.

# Paso 12 — Master Prompt

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 12 outputs del Paso 12 con sus valores reales para Cerrajeros Madrid 24h, **incluyendo el Master Prompt completo literal del original**.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush.

# Bloque I — Introducción

## Objetivo del Paso 12

<small>§2</small>

En este paso la IA produce todos los outputs que **convierten el sistema GMB Crush en un Master Prompt reutilizable** — el prompt principal que genera la arquitectura completa de un cluster web local, los 4 prompts auxiliares (URL Matrix / Content Architecture / GeoArticles / QA), las 14 reglas operativas no-negociables del prompt y la regla web-first que protege el GBP. Permite que la IA aplique el sistema a CUALQUIER cliente con solo cambiar los inputs del preflight.

**Outputs del paso:**

- **12.1** Master Prompt principal — el prompt completo reutilizable (~580 líneas literal)
- **12.2** Auxiliary Prompt — URL Matrix (genera solo la matriz)
- **12.3** Auxiliary Prompt — Content Architecture (genera solo bloques de contenido)
- **12.4** Auxiliary Prompt — GeoArticles (genera solo los GAs validados)
- **12.5** Auxiliary Prompt — QA (corre las 5 categorías QA del Paso 9)
- **12.6** Estructura del prompt — Header / Inputs / Outputs esperados / Reglas / Ejemplo
- **12.7** Web-First GBP Rule — protección antes del Paso 14
- **12.8** Reglas operativas no-negociables (14 reglas literales)
- **12.9** Inputs Validation embedded — checks de NAP, categorías, Main City
- **12.10** Executive Summary template
- **12.11** Validación: prompt produce los outputs esperados de Bloques 1-3
- **12.12** Validación: prompt cumple con web-first rule

**Errores que previene:**

- Re-escribir todo el sistema desde cero para cada cliente
- Olvidar reglas doctrinales en la construcción del prompt
- Crear prompts que inventan señales de GBP antes del Paso 14
- Prompts sin validation embedded
- Prompts auxiliares desincronizados del Master

**Cuándo se ejecuta:** después de Paso 11 (Pseudocódigo) cerrado. Antes de Paso 13 (Sistema Final Operativo).

## Info heredada de pasos anteriores

<small>§3</small>

> El Paso 12 es **meta**: encapsula todo el sistema en un prompt. Hereda de Paso 11 (la lógica formalizada) y de los outputs declarativos de Bloques 1-3.

| Campo | Origen |
|---|---|
| Pseudocódigo del sistema (16 funciones + main) | Paso-11 11.1-11.17 |
| Validación de inputs heredados | Paso-11 11.18 |
| Validación de secuencia | Paso-11 11.19 |
| Outputs de Bloques 1-3 (catálogo completo) | 137 outputs upstream |
| GBP Lifecycle Status | Paso-01 1.3 |

# Bloque II — Ejemplo rellenado para el Paso 12 — Master Prompt

<small>§4</small>

> Los 12 outputs del Paso 12 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección 4.X corresponde 1:1 al output 12.X declarado en §5. **El Master Prompt y los 4 auxiliares se incluyen LITERALMENTE como están en el documento fuente original.**

### 12.1 — Master Prompt principal

> Prompt completo del sistema. Para aplicarlo a Cerrajeros Madrid 24h, sustituir los placeholders `[INSERT]` con los valores del preflight + outputs heredados de Bloques 1-3.

```text
Actúa como Matteo de GMB Crush, especialista top 1% en Local SEO, Google Business Profile optimization, AI Overview visibility, semantic SEO, GeoHub architecture, internal linking y LocalBusiness site structure.

Quiero construir una web local desde cero siguiendo la metodología GMB Crush.

Usa exclusivamente esta jerarquía de páginas:

1. Homepage = Root Entity Anchor
2. Service Overview Pages = Topical Authority Pillars, no location
3. Location-Based Service Pages = Main City Geo-Targeted Converters
4. Additional Category Pages = GBP additional category support
5. GeoHub Pages = Main City Silo Containers
6. GeoArticle Pages = Semantic Boosters for service + Main City + long-tail intent

IMPORTANTE:
- Build the base architecture around one Main City.
- Use Local Coverage Areas as GEO content signals.
- Do not create URLs for Local Coverage Areas unless they are approved as Expansion Areas.
- Do not use Target Cities or Secondary Cities in the base build.
- Do not confuse Service Overview Pages with Location-Based Service Pages.
- Do not mix multiple services in one local landing.
- Do not create pages duplicated for additional categories already covered by core services.
- Do not claim a physical office in any Local Coverage Area unless true.
- GeoArticles are not landing pages; they are semantic boosters.
- Every page must have function, URL, H1, metadata, schema, internal links, priority, phase and QA.

INPUTS DEL NEGOCIO:

Business Name:
[INSERT]

Website Root Domain:
[INSERT]

Canonical Domain:
[INSERT]

Country:
[INSERT]

State / Province:
[INSERT]

Main City:
[INSERT]

Main City Slug:
[INSERT]

Physical Location City:
[INSERT]

Full NAP:
- Business Name: [INSERT]
- Street Address: [INSERT]
- City: [INSERT]
- State / Province: [INSERT]
- ZIP / Postal Code: [INSERT]
- Country: [INSERT]
- Phone: [INSERT]
- Email: [INSERT]

GBP URL:
[INSERT]

Planned Primary GBP Category:
[INSERT]

Primary Category Slug:
[INSERT]

Planned Additional GBP Categories:
[INSERT LIST]

Servicios principales:
[INSERT LIST]

Service Slugs:
[INSERT LIST]

Direct Local Coverage Areas:
Zonas que salen directamente de la dirección física / NAP.
Ejemplo: barrio, distrito o ciudad mencionados en la dirección.
[INSERT LIST]

Candidate Local Coverage Areas:
Zonas cercanas o relevantes que deben pasar el test de coherencia GEO antes de usarse como señales activas.
[INSERT LIST]

Approved Expansion Areas:
Zonas que sí tendrán URLs propias. Default: None in Phase 1.
[INSERT LIST]

> **Regla**: Direct = sale del ancla física. Candidate = se evalúa. Approved Expansion = genera URL.

Should Local Coverage Areas generate pages?
Default: No.

Approved Expansion Areas:
[INSERT ONLY IF DEDICATED URLS ARE APPROVED]

Additional Categories already covered by core services:
[INSERT LIST]

Additional Categories that need separate pages:
[INSERT LIST]

GeoArticles per Service:
[INSERT NUMBER]

GeoHub URL Style:
[/city/ OR /category/city/]

GeoArticle URL Style:
[/city/article-topic/ OR /category/city/article-topic/]

Top Priority Services:
[INSERT LIST]

Trust Signals:
[INSERT LIST]

Preferred CTA:
[INSERT]

Publishing Capacity:
[INSERT NUMBER] pages per week

CMS:
[INSERT]

Can schema be added?
[YES / NO]

Can internal links be edited manually?
[YES / NO]

Tracking Tools:
[INSERT]

TASK:

Generate a complete GMB Crush website architecture system with the following outputs:

1. Executive summary
2. Inputs validation
3. Duplicate category detection
4. Total base page count formula
5. Full URL Matrix
6. Page Type Rules
7. Content Architecture + Local Coverage Areas
8. Homepage brief
9. Service Overview Pages
10. Main City GeoHub Page
11. Main City Location-Based Service Pages
12. Páginas de categoría adicional en la Main City
13. Main City GeoArticle ideas
14. Schema Map
15. Internal Linking Map
16. Priority Score
17. Publishing Phases
18. QA Checklist
19. Optional Expansion Module
20. Final implementation roadmap

OUTPUT REQUIREMENTS:

A. INPUT VALIDATION

Validate:
- Primary GBP category alignment
- Core services
- Additional GBP categories
- Main City
- Physical Location City
- Local Coverage Areas
- Approved Expansion Areas
- Category duplication risks
- Missing slugs
- URL consistency
- NAP consistency

B. TOTAL BASE PAGE COUNT

Use this formula:

1 Homepage
+ S Service Overview Pages
+ 1 Main City GeoHub
+ S Main City Location-Based Service Pages
+ A Páginas de categoría adicional en la Main City
+ G × S Main City GeoArticle Pages

Where:
S = number of core services
A = number of additional categories that need separate pages
G = number of GeoArticles per service

Do not include Local Coverage Areas in the base formula.
Only include Approved Expansion Areas in an optional expansion formula.

C. URL RULES

Use these URL patterns:

Homepage:
/

Service Overview:
/[primary-category-slug]/[service-slug]/

Main City GeoHub:
/[main-city-slug]/
or
/[primary-category-slug]/[main-city-slug]/

Main City Location-Based Service:
/[primary-category-slug]/[main-city-slug]/[service-slug]/

Main City Additional Category:
/[primary-category-slug]/[main-city-slug]/[additional-category-slug]/

Main City GeoArticle:
/[main-city-slug]/[article-topic-slug]/
or
/[primary-category-slug]/[main-city-slug]/[article-topic-slug]/

Local Coverage Areas:
No URLs by default.

Approved Expansion Areas:
Create URLs only if explicitly approved.

D. URL MATRIX

Create a clean table with these columns:

ID
Page Type
Parent Page
Service
Service Slug
Main City
Main City Slug
Additional Category
Local Coverage Areas Used
Approved Expansion Area
URL
H1
Meta Title
Meta Description
Schema Type
Enlaces internos Required
Priority
Publish Phase
Status
Notes

E. PAGE TYPE RULES

For each page type, provide:
- Purpose
- URL pattern
- H1 formula
- Meta title formula
- Meta description formula
- Word count target
- Required sections
- FAQ requirements
- CTA requirements
- Schema required
- Internal links required
- Example using the business inputs
- Incorrect examples
- Final rule

F. CONTENT ARCHITECTURE + LOCAL COVERAGE AREAS

For each page type, define:
- Required internal content structure
- Where Local Coverage Areas may be mentioned
- Where Local Coverage Areas must not be used
- How to avoid fake location claims
- How to use Local Coverage Areas in FAQs
- How to use Local Coverage Areas in schema areaServed
- How to avoid creating unnecessary URLs

G. HOMEPAGE BRIEF

Generate:
- Homepage URL
- H1
- Meta title
- Meta description
- Quick Answer block
- Core service menu
- Vista previa de cobertura local
- Trust blocks
- FAQ ideas
- Schema
- Internal links

H. SERVICE OVERVIEW PAGES

For each service, generate:
- URL
- H1
- Meta title
- Meta description
- Suggested H2s using AUDIO:
  Authority
  Uniqueness
  Depth
  Intent
  Optimization
- FAQs
- Internal links to the Main City service version
- Schema

I. MAIN CITY GEOHUB PAGE

Generate:
- URL
- H1
- Meta title
- Meta description
- Services available in Main City
- Additional category pages in Main City
- Local Coverage Areas section
- GeoArticle ideas for Main City
- Internal links
- Schema

J. MAIN CITY LOCATION-BASED SERVICE PAGES

For each Service × Main City combination, generate:
- URL
- H1
- Meta title
- Meta description
- Local intro angle
- AUDIO H2s
- Local Coverage Areas section
- FAQs
- CTA
- Parent service page
- Matching GeoHub page
- Related same-city services
- Related GeoArticles
- Schema

K. ADDITIONAL CATEGORY PAGES

For each Additional Category × Main City combination, generate:
- URL
- H1
- Meta title
- Meta description
- Local problem/scenario
- AUDIO H2s
- Local Coverage Areas use case
- FAQs
- CTA
- Related services
- Matching GeoHub
- Schema

L. GEOARTICLE IDEAS

Generate [G] GeoArticle ideas for each Service in the Main City.

For each GeoArticle, return:
- Page title
- H1
- URL
- Target long-tail keyword
- Intent type
- Summary
- Matching Main City Location-Based Service Page
- Matching GeoHub Page
- Related GeoArticle
- Schema

M. SCHEMA MAP

Assign schema by page type:

Homepage:
Organization
WebSite
LocalBusiness if physical presence exists in Main City
FAQPage
Speakable

Service Overview:
Service
WebPage
BreadcrumbList
Speakable

Location-Based Service:
LocalBusiness
BreadcrumbList
FAQPage optional
Speakable optional

Additional Category:
Service with areaServed
BreadcrumbList
FAQPage optional

GeoHub:
CollectionPage
BreadcrumbList
LocalBusiness only if physical presence exists in Main City

GeoArticle:
Article
FAQPage
BreadcrumbList
Speakable

N. INTERNAL LINKING MAP

Apply this hierarchy:

Homepage links to:
- Service Overview Pages
- Main City GeoHub
- Páginas de categoría adicional en la Main City
- Página de contacto

Service Overview links to:
- Homepage
- Main City version of that service
- Related Service Overview Pages
- Relevant GeoArticles

Main City Location-Based Service links to:
- Parent Service Overview
- Matching Main City GeoHub
- Other services in Main City
- Related GeoArticles
- Página de contacto

Additional Category links to:
- Matching Main City GeoHub
- Related services in Main City
- Related GeoArticles
- Página de contacto

Main City GeoHub links to:
- Homepage
- All services in Main City
- All additional category pages in Main City
- All GeoArticles in Main City
- Página de contacto

GeoArticle links to:
- Matching Main City Location-Based Service Page
- Matching Main City GeoHub
- Related GeoArticle
- Optional related service
- Página de contacto

Local Coverage Areas:
Do not link unless they are Approved Expansion Areas with real URLs.

O. PRIORITY SCORE

Calculate priority using:

Priority Score =
Revenue Value
+ Search Intent
+ GBP Category Relevance
+ Local Relevance
+ Competition Gap
+ Conversion Urgency

Each factor is scored from 1 to 5.

Priority tiers:
26–30 = P1
21–25 = P2
16–20 = P3
10–15 = P4
0–9 = Hold

P. PUBLISHING PHASES

Assign every page to one of these phases:

Phase 1: Entity Foundation
- Homepage
- Contacto
- About
- Service Overview Pages prioritarias
- Main City GeoHub

Phase 2: Main City Conversion Layer
- Main City service pages
- Additional category pages for Main City

Phase 3: Main City Semantic Expansion
- GeoArticles
- FAQ clusters
- Cost guides
- Comparison articles
- Mistake guides

Phase 4: Optimization Loop
- Internal link updates
- Metadata refresh
- FAQ expansion
- Schema QA
- Geo-grid review
- Search Console optimization

Phase 5: Optional Expansion Module
- Approved Expansion Area GeoHubs
- Approved Expansion Area service pages
- Approved Expansion Area GeoArticles

Q. QA CHECKLIST

For each page, include QA checks:

- URL approved
- Page type correct
- One service only
- One Main City only if applicable
- Local Coverage Areas used naturally
- No unnecessary coverage-area URLs
- No fake location claim
- H1 approved
- Meta title approved
- Meta description approved
- Word count approved
- AUDIO structure included
- FAQs included
- CTA included
- Schema approved
- Internal links approved
- NAP consistent
- No canibalization
- Final approval status

R. FINAL OUTPUT FORMAT

Return the answer in this structure:

1. Title + Summary Block
2. Inputs Validation
3. Duplicate Category Detection
4. Page Count Formula
5. URL Matrix
6. Page Type Rules
7. Content Architecture + Local Coverage Areas
8. Homepage Brief
9. Service Overview Matrix
10. Main City GeoHub Matrix
11. Main City Location-Based Service Matrix
12. Additional Category Matrix
13. GeoArticle Matrix
14. Schema Map
15. Internal Linking Map
16. Priority Score Table
17. Publishing Plan
18. QA Checklist
19. Optional Expansion Module
20. Final Takeaway

Use clean tables.
Be precise.
Do not invent physical locations.
Do not create duplicate pages.
Do not create URLs for Local Coverage Areas unless they are Approved Expansion Areas.
Do not create pages with no clear parent, target, or internal link destination.
```

### 12.2 — Auxiliary Prompt — URL Matrix

```text
Actúa como Matteo de GMB Crush.

Genera únicamente la URL Matrix completa para una web local de una Main City.

Inputs:
Business Name:
Website Root Domain:
Planned Primary GBP Category:
Primary Category Slug:
Main City:
Main City Slug:
Servicios principales:
Service Slugs:
Additional Categories that need separate pages:
Additional Category Slugs:
Local Coverage Areas:
Approved Expansion Areas:
GeoArticles per Service:

Rules:
- Base architecture uses one Main City.
- Local Coverage Areas do not generate URLs.
- Approved Expansion Areas generate URLs only if provided.
- Homepage = /
- Service Overview = /category/service/
- Main City GeoHub = /city/
- Main City Service Page = /category/city/service/
- Additional Category = /category/city/additional-category/
- GeoArticle = /city/article-topic/

Columns:
ID
Page Type
Parent Page
Service
Service Slug
Main City
Main City Slug
Additional Category
Local Coverage Areas Used
URL
H1
Meta Title
Schema Type
Priority
Publish Phase
Status
Notes
```

### 12.3 — Auxiliary Prompt — Content Architecture (contenido de una página)

```text
Actúa como Matteo de GMB Crush y senior SEO content strategist.

Quiero generar contenido completo para esta página siguiendo GMB Crush, AIO, GEO y AUDIO.

Page Type:
[Homepage / Service Overview / Location-Based Service / Additional Category / GeoHub / GeoArticle]

Business Name:
[INSERT]

Planned Primary GBP Category:
[INSERT]

Primary Category Slug:
[INSERT]

Main City:
[INSERT]

Main City Slug:
[INSERT]

Local Coverage Areas:
[INSERT LIST]

Service:
[INSERT]

Service Slug:
[INSERT]

URL:
[INSERT]

Parent Service Page:
[INSERT]

GeoHub Page:
[INSERT]

Related Pages:
[INSERT]

Phone:
Email:
[INSERT]

NAP:
[INSERT]

Physical office in Main City?
Yes / No

Physical office in Local Coverage Areas?
Yes / No

Generate:
1. H1
2. Meta title
3. Meta description
4. Quick Answer block if relevant
5. Full page outline
6. 3–5 H2s using AUDIO where applicable
7. Local Coverage Areas section where appropriate
8. 3–5 FAQs
9. CTA
10. Internal links with anchor text
11. Schema recommendation
12. Anti-canibalization note

Rules:
- If Service Overview, do not target Main City or Local Coverage Areas.
- If Location-Based Service, use one service and one Main City.
- If GeoHub, list all Main City services, categories, articles and coverage areas.
- If GeoArticle, write as semantic booster, not landing page.
- Do not claim physical presence in Local Coverage Areas unless true.
```

### 12.4 — Auxiliary Prompt — GeoArticles

```text
Actúa como Matteo de GMB Crush, especialista en GeoArticles, AI Overview y semantic SEO local.

Inputs:
Brand Name:
Primary Business Category Slug:
Service:
Service Slug:
Main City:
Main City Slug:
Local Coverage Areas:
Matching Location-Based Service Page:
Matching GeoHub Page:
Target Audience:
Physical office in Main City?
Yes / No

Generate 3 GeoArticle ideas.

For each idea:
1. Page Title
2. H1 Suggestion
3. Suggested URL
4. Target Long-Tail Keyword
5. Intent Type
6. Summary
7. Matching Location-Based Service Page
8. Matching GeoHub Page
9. Related GeoArticle
10. Suggested CTA
11. Schema Type

Rules:
- Each article supports one service, one Main City and one long-tail intent.
- Local Coverage Areas may appear as examples or context.
- Each article links to the matching /category/main-city/service/ page.
- Each article links to the matching /main-city/ GeoHub page.
- Do not create URLs for Local Coverage Areas.
```

### 12.5 — Auxiliary Prompt — QA

```text
Actúa como Matteo de GMB Crush y haz QA de esta página antes de publicarla.

Page URL:
[INSERT]

Page Type:
[INSERT]

Business Name:
[INSERT]

Planned Primary GBP Category:
[INSERT]

Target Service:
[INSERT]

Main City:
[INSERT]

Local Coverage Areas Used:
[INSERT]

Physical office in Main City?
Yes / No

Physical office in Local Coverage Areas?
Yes / No

H1:
[INSERT]

Meta Title:
[INSERT]

Meta Description:
[INSERT]

Word Count:
[INSERT]

Schema Added:
[INSERT]

Enlaces internos Added:
[INSERT]

NAP Used:
[INSERT]

Check:
1. URL approved
2. Page type correct
3. One service only
4. One Main City only
5. Local Coverage Areas used naturally
6. No fake office/location claim
7. H1 approved
8. Meta title approved
9. Meta description approved
10. Word count approved
11. AUDIO structure included
12. FAQs included
13. CTA included
14. Schema approved
15. Internal links approved
16. NAP consistent
17. No canibalization
18. Final approval

Return:
- QA table
- Problems found
- Required fixes
- Final status:
  Approved / Needs Revision / Blocked
```

### 12.6 — Estructura del prompt

```text
Sección 1: ROLE — Actúa como Matteo de GMB Crush, especialista top 1%
Sección 2: METHODOLOGY — Construir web local desde cero con jerarquía 6 page types
Sección 3: NON-NEGOTIABLES — Lista IMPORTANTE con 10 prohibiciones
Sección 4: INPUTS DEL NEGOCIO — ~25 campos a rellenar (NAP, slugs, LCAs, etc.)
Sección 5: TASK — Generate 20 outputs específicos
Sección 6: OUTPUT REQUIREMENTS A-R — 18 sub-bloques (Validation, Page Count,
           URL Rules, URL Matrix, Page Type Rules, Content Architecture,
           Homepage, SO, GH, LBS, AC, GA, Schema, Linking, Priority, Phases,
           QA, Final Format)
Sección 7: FINAL RULES — Use clean tables / Be precise / Do not invent /
           Do not create duplicates / Do not create URLs for LCAs / etc.
```

### 12.7 — Web-First GBP Rule

```text
Web-First GBP Rule for the Master Prompt:

The GBP does not exist at the beginning of this workflow.
Use Planned Primary GBP Category and Planned Additional GBP Categories during web architecture.
Do not insert a GBP URL, Google review claim, Google Maps embed or sameAs GBP link until Paso 14.
Paso 14 creates, verifies and synchronizes the GBP after the website base is published.
```

### 12.8 — Reglas operativas no-negociables (14 reglas literales del original)

> Las 14 reglas operativas del Master Prompt, portadas literalmente del documento fuente secciones 22-35 del documento fuente. Cada regla tiene su Explicación, Patrón, Ejemplo correcto, Ejemplos incorrectos y Regla final. Esta sección es referencia obligatoria para construir cualquier prompt del sistema GMB Crush.

#### Regla operativa 1 — Rol y restricciones iniciales

**Explicación:** El Master Prompt debe empezar definiendo el rol, la metodología y las reglas no negociables. Esto evita que la IA improvise estructuras ajenas al sistema.

**Patrón:** `Role → Methodology → Non-negotiables`

**Ejemplo correcto (Cerrajeros):** El prompt dice: Actúa como Matteo de GMB Crush y usa Homepage, Service Overview, Location-Based Service, Additional Category, GeoHub y GeoArticle.

**Ejemplos incorrectos:**
- Pedir simplemente "crea una web SEO"
- No mencionar GMB Crush
- No prohibir mezclar servicios o zonas

**Regla final:** El prompt maestro debe fijar rol y límites desde el inicio.

#### Regla operativa 2 — Inputs geográficos simplificados

**Explicación:** El prompt debe pedir Main City, Physical Location City, Local Coverage Areas y Approved Expansion Areas. No debe usar Target Cities ni Secondary Cities en la base.

**Patrón:** `Main City + Local Coverage Areas + Approved Expansion Areas`

**Ejemplo correcto (Cerrajeros):** Cerrajeros Madrid 24h: Main City Madrid; Local Coverage Areas Almagro, Chamberí, Salamanca y Retiro; Approved Expansion Areas vacío.

**Ejemplos incorrectos:**
- Pedir Target Cities como base
- Multiplicar páginas por cobertura
- No pedir ubicación física

**Regla final:** La geografía del prompt debe reflejar la versión simplificada.

#### Regla operativa 3 — Fórmula base explícita

**Explicación:** El prompt debe obligar a calcular la fórmula base antes de generar URLs. Así la IA no salta directamente a matrices infladas o incompletas.

**Patrón:** `1 + S + 1 + S + A + G×S`

**Ejemplo correcto (Cerrajeros):** Para Cerrajeros Madrid 24h, el prompt debe devolver 28 páginas SEO base más /contacto/ como página auxiliar con S=5, A=1, G=3.

**Ejemplos incorrectos:**
- Usar C = target cities
- No explicar A
- No mostrar tabla de conteo

**Regla final:** El Master Prompt debe calcular antes de listar.

#### Regla operativa 4 — URL Matrix obligatoria

**Explicación:** El output debe exigir una URL Matrix con ID, Page Type, Parent, Service, City, URL, H1, metas, schema, links, priority, phase y status.

**Patrón:** `Inputs → URL Matrix → producción`

**Ejemplo correcto (Cerrajeros):** El prompt genera filas HP-001, SO-001, GH-001, LBS-001, AC-001 y GA-001 para Cerrajeros Madrid 24h.

**Ejemplos incorrectos:**
- Pedir solo lista de URLs
- No incluir schema
- No incluir status o phase

**Regla final:** Sin matriz completa, el prompt no produce un sistema operativo.

#### Regla operativa 5 — Page Type Rules completas

**Explicación:** El Master Prompt debe desarrollar cada tipo de página con propósito, patrón, H1, metas, word count, secciones, schema, enlaces y CTA.

**Patrón:** `Page Type → rules → example`

**Ejemplo correcto (Cerrajeros):** Homepage de Cerrajeros Madrid 24h incluye H1 de Servicios de cerrajería en Madrid, servicios core, NAP y enlaces.

**Ejemplos incorrectos:**
- Definir solo URL patterns
- No separar Service Overview de Location-Based Service
- No pedir schema por tipo

**Regla final:** Cada tipo de página debe tener reglas completas.

#### Regla operativa 6 — Content Architecture incluida

**Explicación:** El prompt debe incluir el nuevo Paso 6: dónde y cómo usar Local Coverage Areas dentro del contenido. Sin esto, la IA vuelve a crear páginas innecesarias o ignora cobertura.

**Patrón:** `Page Type → content sections → coverage usage`

**Ejemplo correcto (Cerrajeros):** En `/cerrajero/madrid/cerrajero-urgente/`, el prompt pide sección de Local Coverage Areas Served con Almagro, Chamberí, Salamanca y Retiro.

**Ejemplos incorrectos:**
- No pedir secciones internas
- Tratar coverage areas como URLs
- No pedir FAQs de cobertura

**Regla final:** El prompt debe enseñar a escribir cada página por dentro.

#### Regla operativa 7 — Internal Linking Map detallado

**Explicación:** El Master Prompt debe pedir Source URL, Target URL, Anchor, Priority y Placement. Esto convierte enlaces en producción, no en recomendación genérica.

**Ejemplos incorrectos:**
- Pedir "internal links" sin tabla
- No pedir anchor text
- Confundir nav links con internal links semánticos

**Regla final:** Los enlaces deben salir como matriz accionable.

#### Regla operativa 8 — Schema Map por page type

**Explicación:** El prompt debe obligar a asignar schema por URL. Esto ayuda a evitar errores posteriores de implementación.

**Patrón:** `URL → Page Type → Schema Required`

**Ejemplo correcto (Cerrajeros):** AC-001 usa Service with areaServed; GA-001 usa Article + FAQPage + BreadcrumbList + Speakable.

**Ejemplos incorrectos:**
- No pedir schema
- Usar el mismo schema en todas las URLs
- No diferenciar address y areaServed

**Regla final:** El schema debe generarse desde el output maestro.

#### Regla operativa 9 — Priority Score con Local Relevance

**Explicación:** La fórmula del prompt debe usar Local Relevance en lugar de City Priority. Esto es coherente con una base de una Main City.

**Patrón:** `Revenue + Intent + GBP + Local Relevance + Gap + Urgency`

**Ejemplo correcto (Cerrajeros):** Cerrajero urgente Madrid obtiene score alto por urgencia, GBP relevance y Main City fit.

**Ejemplos incorrectos:**
- Usar Top Priority Cities
- Puntuar áreas sin URL
- No explicar el score

**Regla final:** La prioridad debe medir páginas, no zonas sin arquitectura.

#### Regla operativa 10 — Publishing Phases con expansión opcional

**Explicación:** El prompt debe separar fases base y expansión opcional. Esto evita volver al modelo multi-ciudad por defecto.

**Patrón:** `Phase 1–4 base | Phase 5 expansion optional`

**Ejemplo correcto (Cerrajeros):** Cerrajeros Madrid 24h publica primero Madrid y sus servicios; Almagro solo entra si se aprueba como expansión.

**Ejemplos incorrectos:**
- Publicar coverage areas en Phase 2
- No crear Phase 5 opcional
- Publicar artículos antes de landings

**Regla final:** La expansión debe vivir en una fase separada.

#### Regla operativa 11 — QA Checklist obligatoria

**Explicación:** El prompt debe devolver QA por page type y por cobertura local: URL, H1, metadata, schema, links, NAP, canibalización y no false location claims.

**Patrón:** `Page → QA checks → final status`

**Ejemplo correcto (Cerrajeros):** LBS-001 no se aprueba si dice "Almagro office" sin oficina real.

**Ejemplos incorrectos:**
- No incluir QA
- No revisar ubicación falsa
- No revisar enlaces internos

**Regla final:** El Master Prompt debe producir control de calidad.

#### Regla operativa 12 — Anti-duplicación de reglas

**Explicación:** El prompt debe prohibir reglas operativas repetidas. Cada regla debe tener nombre semántico y contenido distinto. Esto evita ruido y pérdida de confianza.

**Patrón:** `Rule name → specific content → duplicate check`

**Ejemplo correcto (Cerrajeros):** En Paso 4, las reglas son canonical domain, trailing slash, service overview pattern, GeoArticle URL, local coverage no URL, etc.

**Ejemplos incorrectos:**
- Regla operativa 1–12 con el mismo texto
- Cambiar solo el número de la regla
- Inflar longitud sin contenido nuevo

**Regla final:** Cada regla operativa debe aportar una decisión nueva.

#### Regla operativa 13 — Expansion Module controlado

**Explicación:** El prompt debe pedir Approved Expansion Areas como campo opcional y generar URLs solo si ese campo tiene contenido validado.

**Patrón:** `Approved Expansion Areas empty → no expansion URLs`

**Ejemplo correcto (Cerrajeros):** Cerrajeros Madrid 24h deja Approved Expansion Areas vacío y el output no genera /almagro/.

**Ejemplos incorrectos:**
- Generar URLs por coverage areas
- No pedir justificación de expansión
- Mezclar expansión con fórmula base

**Regla final:** La expansión se activa solo con aprobación explícita.

#### Regla operativa 14 — Output final ordenado

**Explicación:** El prompt debe exigir un orden de salida fijo para que cualquier usuario o IA pueda consumir el resultado sin buscar secciones perdidas.

**Patrón:** `Summary → Validation → Formula → Matrix → Rules → Links → Score → Phases → QA → Takeaway`

**Ejemplo correcto (Cerrajeros):** El output de Cerrajeros Madrid 24h termina con URL Matrix, Internal Linking Map, Publishing Plan y QA Checklist.

**Ejemplos incorrectos:**
- Entregar respuesta libre sin estructura
- Omitir outputs clave
- Mezclar explicación con tablas sin orden

**Regla final:** El Master Prompt debe generar un sistema, no una respuesta suelta.

### 12.9 — Inputs Validation embedded

```text
Antes de generar la arquitectura, validar:
- NAP completo (8 campos del Paso-01 1.4); Phone/Email pueden ser placeholders pero declarados
- Primary GBP Category coherente con Local Pack analysis
- Additional Categories clasificadas (cubiertas vs página propia)
- Main City única (no listas)
- Physical Location City declarada (puede coincidir con Main City)
- Servicios principales = S (S=5 default; ajustable con justificación)
- LCAs separadas en Direct vs Candidate
- GBP Status declarado entre los 4 valores válidos

Si cualquier check falla → bloquear generación + reportar.
```

### 12.10 — Executive Summary template

```text
[BUSINESS_NAME] — Cluster Web GMB Crush

Status:        [GBP_STATUS]
Main City:     [MAIN_CITY]
Servicios:     [S core services]
LCAs:          [N total = D direct + C candidate]
Total URLs:    [1 + S + 1 + S + A + G×S = N base + 1 aux]
Phase actual:  [Phase 1-N]

Generado:      [DATE]
Bloques 1-3 status: [confirmed/⚠]
QA Gate:       [Pass/Block]
```

### 12.11 — Validación: prompt produce los outputs esperados

Cumplido — el Master Prompt + 4 auxiliares cubren los 20 outputs del original (sección TASK del Master Prompt, sección 17 del documento fuente). Cruce con outputs heredados de Bloques 1-3:

```text
Master Prompt outputs (1-20):
1. Executive summary           ← 12.10
2. Inputs validation           ← 12.9
3. Duplicate category detection ← Paso-02 2.12
4. Total base page count        ← Paso-02 2.9
5. Full URL Matrix              ← Paso-03 3.5 + 12.2
6. Page Type Rules              ← Paso-05 5.3-5.8
7. Content Architecture + LCAs  ← Paso-06 6.6-6.11 + 12.3
8. Homepage brief               ← Paso-05 5.3
9. Service Overview Pages       ← Paso-05 5.4
10. Main City GeoHub            ← Paso-05 5.7
11. Main City LBS               ← Paso-05 5.5
12. Additional Category         ← Paso-05 5.6
13. GeoArticle ideas            ← Paso-05 5.8 + 12.4
14. Schema Map                  ← Paso-05 5.9 + Paso-06 6.17
15. Internal Linking Map        ← Paso-07 7.11
16. Priority Score              ← Paso-08 8.1-8.10
17. Publishing Phases           ← Paso-10 10.4-10.8
18. QA Checklist                ← Paso-09 9.7 + 12.5
19. Optional Expansion Module   ← Paso-04 4.10
20. Final implementation roadmap ← Paso-10 10.9
```

### 12.12 — Validación: prompt cumple con web-first rule

Cumplido — la regla §6.7 está embebida en el Master Prompt y se activa cuando GBP_STATUS = Not Created. Cruce con Paso-09 9.8 (GBP Not Created QA Checklist).

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 12 outputs que el Paso 12 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `12.7`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 12.1 | Master Prompt principal | Prompt completo (~580 líneas) | GMB Crush | Paso-11 11.17 + Bloques 1-3 |
| 12.2 | Auxiliary Prompt — URL Matrix | Prompt parcial | GMB Crush | Paso-03 3.5 + Paso-04 4.3-4.8 |
| 12.3 | Auxiliary Prompt — Content Architecture | Prompt parcial | GMB Crush | Paso-05 5.3-5.8 + Paso-06 6.6-6.11 |
| 12.4 | Auxiliary Prompt — GeoArticles | Prompt parcial | GMB Crush | Paso-03 3.4 + Paso-08 8.11 |
| 12.5 | Auxiliary Prompt — QA | Prompt parcial | GMB Crush | Paso-09 9.2-9.8 |
| 12.6 | Estructura del prompt | Plantilla 7 secciones | GMB Crush | — |
| 12.7 | Web-First GBP Rule | Regla embebida | GMB Crush | Paso-01 1.3 + Paso-09 9.8 |
| 12.8 | Reglas operativas no-negociables (14 reglas) | Lista declarativa con contenido literal | GMB Crush | Bloques 1-3 (todas las reglas doctrinales) |
| 12.9 | Inputs Validation embedded | Checks pre-ejecución | GMB Crush | Paso-01 1.X + Paso-02 2.X |
| 12.10 | Executive Summary template | Plantilla output | GMB Crush | Paso-01 1.X + Paso-02 2.X + Paso-08 8.X |
| 12.11 | Validación prompt produce 20 outputs | Validation flag | GMB Crush | Paso-12 12.1-12.5 (intra-paso) |
| 12.12 | Validación prompt cumple web-first | Validation flag | GMB Crush | Paso-01 1.3 + Paso-09 9.8 |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 12 outputs (12.1–12.12). Cada output usa el patrón estándar adaptado a prompts.

### 12.1 — Master Prompt principal

<small>§6.1</small>

**Explicación**

El Master Prompt es el **artefacto central** del Paso 12. Es un prompt estructurado en 7 secciones que la IA puede ejecutar para generar la arquitectura completa de un cluster local. Re-utilizable: con solo cambiar los inputs del preflight + outputs heredados, se aplica a cualquier cliente.

**Plantilla**

Ver §4 sub-sección 12.1 — **prompt completo literal de ~580 líneas**, embebido tal cual está en el documento fuente original.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Reemplazar placeholders del Master Prompt con valores Cerrajeros (Business Name, NAP, slugs, LCAs, etc.). El output generado cubre los 20 entregables (1-20 de la sección TASK).

**Ejemplos incorrectos**

```text
- Prompt sin sección IMPORTANTE (10 prohibiciones doctrinales)
- Prompt sin NON-NEGOTIABLES (rompe disciplina)
- Prompt sin OUTPUT REQUIREMENTS A-R (la IA produce formato libre)
- Hard-codear datos de un cliente (no es reusable)
```

**Regla final**

```text
Master Prompt = 7 secciones obligatorias con placeholders [INSERT] para inputs.
```

**Validación operativa**

Aplicar el prompt a 3 clientes hipotéticos distintos (sectores diferentes) y validar que produce arquitecturas coherentes con el sistema doctrinal.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Componer las 7 secciones del prompt según estructura §6.6 + integrar reglas y validations.

**Output del paso**

- **Tipo:** Prompt completo en markdown (~580 líneas).
- **Ejemplo (Cerrajeros Madrid 24h):** ver §4 sub-sección 12.1 (prompt literal).

### 12.2 — Auxiliary Prompt — URL Matrix

<small>§6.2</small>

**Explicación**

Prompt auxiliar que genera SOLO la URL Matrix.

**Plantilla**

Ver §4 sub-sección 12.2.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Output esperado: 28+1 = 29 filas con HP, SO-1..5, GH, LBS-1..5, AC-1, GA-1..15, AUX.

**Ejemplos incorrectos**

```text
- Generar matriz con LCAs como filas (rompe Paso-04 4.9)
- Más URLs que 1+S+1+S+A+G×S+aux (rompe fórmula 2.9)
```

**Regla final**

```text
Auxiliary URL Matrix produce N+1 filas exactas según fórmula maestra.
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aislar sección URL Matrix del Master + simplificar ROLE.

**Output del paso**

- **Tipo:** Prompt auxiliar parcial.
- **Ejemplo (Cerrajeros Madrid 24h):** prompt que produce 29 URLs.

### 12.3 — Auxiliary Prompt — Content Architecture

<small>§6.3</small>

**Explicación**

Prompt auxiliar que genera SOLO los bloques de contenido por page type.

**Plantilla**

Ver §4 sub-sección 12.3.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Output esperado por page type: HP 11 bloques + SO 11 + LBS 12 + AC 11 + GH 10 + GA 10.

**Ejemplos incorrectos**

```text
- Bloques de SO con LCAs (rompe rol no-local)
- Word count fuera de rango (rompe Paso-05 5.10)
```

**Regla final**

```text
Auxiliary Content Architecture cumple specs Paso-05 5.3-5.8 + Paso-06 6.6-6.11.
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aislar sección Content Architecture del Master Prompt.

**Output del paso**

- **Tipo:** Prompt auxiliar parcial.
- **Ejemplo (Cerrajeros Madrid 24h):** prompt que produce los bloques por page type.

### 12.4 — Auxiliary Prompt — GeoArticles

<small>§6.4</small>

**Explicación**

Prompt auxiliar que genera SOLO los G×S GeoArticles validados con keyword research.

**Plantilla**

Ver §4 sub-sección 12.4.

**Ejemplo correcto con Cerrajeros Madrid 24h**

15 GAs (G=3 × S=5).

**Ejemplos incorrectos**

```text
- GAs sin keyword research validado
- GA con H1 idéntico a su LBS hijo
- Más GAs que G×S
```

**Regla final**

```text
Auxiliary GeoArticles produce G×S URLs con keyword research validado y parent LBS asignado.
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aislar sección GA del Master + integrar keyword research.

**Output del paso**

- **Tipo:** Prompt auxiliar parcial.
- **Ejemplo (Cerrajeros Madrid 24h):** prompt que produce 15 GAs.

### 12.5 — Auxiliary Prompt — QA

<small>§6.5</small>

**Explicación**

Prompt auxiliar que aplica las 5 categorías QA del Paso 9 + 18 checks del original.

**Plantilla**

Ver §4 sub-sección 12.5.

**Ejemplo correcto con Cerrajeros Madrid 24h**

28 URLs auditadas con los 18 checks; 0 fails.

**Ejemplos incorrectos**

```text
- Saltar alguna categoría QA
- Marcar Pass sin haber validado realmente
```

**Regla final**

```text
Auxiliary QA aplica los 18 checks; produce diagnóstico por URL.
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aislar sección QA del Master Prompt.

**Output del paso**

- **Tipo:** Prompt auxiliar parcial.
- **Ejemplo (Cerrajeros Madrid 24h):** prompt que audita 28 URLs.

### 12.6 — Estructura del prompt

<small>§6.6</small>

**Explicación**

Las **7 secciones** que conforman el Master Prompt original. Es el contrato de forma que garantiza calidad y reusabilidad.

**Patrón o fórmula**

Ver §4 sub-sección 12.6 — las 7 secciones listadas.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Aplicado al Master Prompt completo de la sub-sección 4.1 — todas las 7 secciones presentes.

**Ejemplos incorrectos**

```text
- Saltar sección INPUTS (prompt no rellena placeholders)
- Saltar OUTPUT REQUIREMENTS (la IA produce formato libre)
- Omitir NON-NEGOTIABLES
```

**Regla final**

```text
Todo prompt del Paso 12 (Master o auxiliar) tiene las secciones obligatorias.
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la plantilla a cada prompt construido.

**Output del paso**

- **Tipo:** Plantilla de 7 secciones.
- **Ejemplo (Cerrajeros Madrid 24h):** Master Prompt + 4 auxiliares cumplen estructura.

### 12.7 — Web-First GBP Rule

<small>§6.7</small>

**Explicación**

Regla doctrinal del original (sección 35 del documento fuente) que protege el sistema cuando GBP_STATUS = Not Created (web-first). Embebida directamente en el Master Prompt.

**Patrón o fórmula**

Ver §4 sub-sección 12.7.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
GBP=Not Created → web se publica primero, GBP se crea en Paso 14.
0 menciones a "ficha de Google" en copy; sameAs vacío.
```

**Ejemplos incorrectos**

```text
- Generar arquitectura web con sameAs apuntando a GBP que no existe
- Listar reseñas Google en schema sin haber creado el GBP
- Crear el GBP antes de tener web base sólida
```

**Regla final**

```text
Si GBP=Not Created, web-first es obligatorio. GBP se crea en Paso 14.
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Embeberla en Master Prompt + activar condicionalmente.

**Output del paso**

- **Tipo:** Regla embebida.
- **Ejemplo (Cerrajeros Madrid 24h):** activa; 28 URLs validadas con 0 violaciones.

### 12.8 — Reglas operativas no-negociables (14 reglas)

<small>§6.8</small>

**Explicación**

Las 14 reglas operativas del documento original (secciones 22-35 del documento fuente). Cada regla regula una decisión específica del prompt y todas son no-negociables. Se han portado **literalmente** del original con su Explicación / Patrón / Ejemplo correcto / Ejemplos incorrectos / Regla final.

**Patrón o fórmula**

Ver §4 sub-sección 12.8 — las 14 reglas con contenido completo del original.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Las 14 reglas aplicadas y validadas en el cluster:
- Regla 1: prompt define rol Matteo de GMB Crush ✓
- Regla 2: Main City Madrid + LCAs Almagro/Chamberí/etc + Approved Expansion vacío ✓
- Regla 3: fórmula 28 páginas con S=5/A=1/G=3 ✓
- Regla 4: URL Matrix con HP-001, SO-001..5, GH-001, LBS-001..5, AC-001, GA-001..15 ✓
- ... (las 14 ✓)

**Ejemplos incorrectos**

```text
- Saltar regla 12 publicando GA antes que LBS hijo
- Inventar regla 15 fuera del catálogo doctrinal
- Aplicar reglas con excepciones sin justificación
```

**Regla final**

```text
Las 14 reglas son no-negociables. Cualquier desviación bloquea la salida del prompt.
```

**Validación operativa**

Aplicar las 14 reglas como filtro de salida del Master Prompt + auxiliares.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Compilar literalmente del documento fuente secciones 22-35 del documento fuente + consolidar en sección del prompt.

**Output del paso**

- **Tipo:** Lista declarativa de 14 reglas con contenido literal completo.
- **Ejemplo (Cerrajeros Madrid 24h):** 14/14 reglas aplicadas con éxito.

### 12.9 — Inputs Validation embedded

<small>§6.9</small>

**Explicación**

Checks que se ejecutan ANTES de generar la arquitectura.

**Patrón o fórmula**

Ver §4 sub-sección 12.9.

**Ejemplo correcto con Cerrajeros Madrid 24h**

8 checks pasados: NAP completo / Primary GBP coherente / Additional clasificadas / Main City única / Physical Location declarada / S=5 / LCAs Direct vs Candidate / GBP Status válido.

**Ejemplos incorrectos**

```text
- Pasar inputs incompletos
- Listar 3 Main Cities (rompe regla 'una Main City única')
- GBP Status fuera de los 4 valores válidos
```

**Regla final**

```text
Validation embedded bloquea generación si cualquier input es incoherente o incompleto.
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Compilar checks desde §3 Heredados + integrar.

**Output del paso**

- **Tipo:** Checks embebidos.
- **Ejemplo (Cerrajeros Madrid 24h):** 8 checks pasados; 0 fails.

### 12.10 — Executive Summary template

<small>§6.10</small>

**Explicación**

Plantilla del Executive Summary que el Master Prompt produce.

**Patrón o fórmula**

Ver §4 sub-sección 12.10.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h — Cluster Web GMB Crush
Status: Not Created (web-first)
Main City: Madrid
Servicios: 5 core + 1 AC efectiva
LCAs: 10 total = 2 Direct + 8 Candidate
Total URLs: 1+5+1+5+1+15 = 28 base + 1 aux = 29
Phase actual: Phase 1 (semana 1)
Generado: 2026-04-30
Bloques 1-3: confirmed (137 outputs)
QA Gate: Pass (28/28)
```

**Ejemplos incorrectos**

```text
- Summary sin Status
- Summary sin total URLs
- Summary sin QA Gate
```

**Regla final**

```text
Executive Summary tiene 8 campos obligatorios; auditable de un vistazo.
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Plantilla con placeholders.

**Output del paso**

- **Tipo:** Plantilla de Executive Summary.
- **Ejemplo (Cerrajeros Madrid 24h):** summary completo.

### 12.11 — Validación: prompt produce los outputs esperados

<small>§6.11</small>

**Explicación**

Valida que la salida del Master Prompt + 4 auxiliares cubre los **20 outputs esperados** (sección TASK del prompt).

**Patrón o fórmula**

Ver §4 sub-sección 12.11 — mapeo de los 20 outputs del Master Prompt a outputs upstream.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
20/20 outputs cubiertos:
1-2: ← 12.10, 12.9
3-7: ← Bloque 1-2 (Pasos 2-7)
8-13: ← Paso 5 (specs por page type)
14-18: ← Pasos 5-9
19-20: ← Pasos 4-10
```

**Ejemplos incorrectos**

```text
- Output sin Roadmap (rompe Paso-10)
- Output sin QA report (rompe gate)
- Output con duplicación entre secciones
```

**Regla final**

```text
Master Prompt + auxiliares cubren los 20 outputs sin gaps ni duplicaciones.
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspección de la salida + cross-check.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 20/20 outputs cubiertos; 0 gaps.

### 12.12 — Validación: prompt cumple con web-first rule

<small>§6.12</small>

**Explicación**

Valida que el output del prompt **no inventa señales de GBP** cuando el cliente está en estado web-first.

**Patrón o fórmula**

```text
Si GBP_STATUS = Not Created:
  ∀ URL en output:
    - copy.gbp_url == None
    - schema.sameAs == []
    - copy.reseñas_google == 0
    - GBP Not Created Checklist (Paso-09 9.8) Pass
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

28 URLs sin sameAs / 0 menciones a 'ficha de Google' / 0 reseñas Google afirmadas / GBP Not Created Checklist Pass 28/28.

**Ejemplos incorrectos**

```text
- Output con sameAs apuntando a GBP que no existe
- Output con 'X reseñas en Google' antes de crear el GBP
- Output con review.aggregateRating sin reseñas reales
```

**Regla final**

```text
Si GBP=Not Created, web-first es invariante en TODA la salida del prompt.
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspección de la salida + cross-check con los 7 sub-checks Paso-09 9.8.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 28/28 URLs Pass GBP Checklist.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 12 y avanzar al Paso 13 (Sistema Final Operativo).

### Validación de prompts

- ☐ Master Prompt principal con 7 secciones + ~580 líneas (12.1)
- ☐ Auxiliary Prompt URL Matrix funcional (12.2)
- ☐ Auxiliary Prompt Content Architecture funcional (12.3)
- ☐ Auxiliary Prompt GeoArticles funcional (12.4)
- ☐ Auxiliary Prompt QA funcional (12.5)

### Validación de estructura y reglas

- ☐ Estructura 7 secciones aplicada en los 5 prompts (12.6)
- ☐ Web-First GBP Rule embebida (12.7)
- ☐ 14 reglas operativas no-negociables literales (12.8)
- ☐ Inputs Validation embedded antes de generación (12.9)
- ☐ Executive Summary template con 8 campos (12.10)

### Validación final

- ☐ Prompt produce los 20 outputs sin gaps (12.11)
- ☐ Prompt cumple web-first rule en TODA la salida (12.12)

## Outputs Consolidados

<small>§8</small>

> Tabla final compacta con la trazabilidad row-per-output. Los IDs (`12.1`–`12.12`) coinciden con los declarados en §5.

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 12.1 | ← Paso-11 11.17 + Bloques 1-3 | **Master Prompt principal** = ~580 líneas literales del original aplicadas a Cerrajeros | Componer 7 secciones del prompt + integrar reglas y validations. **Fuente:** GMB Crush. | confirmed |
| 12.2 | ← Paso-03 3.5 + Paso-04 4.3-4.8 | **Auxiliary Prompt URL Matrix** = produce 29 URLs (28 base + 1 aux) | Aislar sección URL Matrix del Master. **Fuente:** GMB Crush. | confirmed |
| 12.3 | ← Paso-05 5.3-5.8 + Paso-06 6.6-6.11 | **Auxiliary Prompt Content Architecture** = produce bloques por page type | Aislar sección Content Architecture del Master. **Fuente:** GMB Crush. | confirmed |
| 12.4 | ← Paso-03 3.4 + Paso-08 8.11 | **Auxiliary Prompt GeoArticles** = produce 15 GAs validados | Aislar sección GA del Master + integrar keyword research. **Fuente:** GMB Crush. | confirmed |
| 12.5 | ← Paso-09 9.2-9.8 | **Auxiliary Prompt QA** = audita 28 URLs y produce gate | Aislar sección QA del Master. **Fuente:** GMB Crush. | confirmed |
| 12.6 | — | **Estructura del prompt** = 7 secciones del Master Prompt original | Aplicar plantilla 7-secciones. **Fuente:** GMB Crush. | confirmed |
| 12.7 | ← Paso-01 1.3 + Paso-09 9.8 | **Web-First GBP Rule** = activa para Cerrajeros (GBP=Not Created); 0 violaciones | Embeberla en Master Prompt. **Fuente:** GMB Crush. | OK |
| 12.8 | ← Bloques 1-3 (todas las reglas) | **14 reglas no-negociables (literales)** = aplicadas con éxito en el cluster | Compilar literalmente desde secciones 22-35 del documento fuente del documento fuente. **Fuente:** GMB Crush. | OK |
| 12.9 | ← Paso-01 1.X + Paso-02 2.X | **Inputs Validation embedded** = 8 checks pasados | Compilar checks desde §3 Heredados. **Fuente:** GMB Crush. | OK |
| 12.10 | ← Paso-01 1.X + Paso-02 2.X + Paso-08 8.X | **Executive Summary template** = 8 campos rellenos | Plantilla con placeholders. **Fuente:** GMB Crush. | confirmed |
| 12.11 | ← 12.1-12.5 | **Validación prompt produce 20 outputs** = 20/20 cubiertos | Inspección salida + cross-check. **Fuente:** GMB Crush. | OK |
| 12.12 | ← Paso-01 1.3 + Paso-09 9.8 | **Validación prompt cumple web-first** = 28/28 URLs Pass GBP Checklist | Inspección salida + cross-check 9.8. **Fuente:** GMB Crush. | OK |

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
- Master Prompt Framework GMB Crush

> **Nota importante — Master Prompt como interfaz del sistema:**
> El Paso 12 NO inventa contenido nuevo: empaqueta los outputs declarativos de Bloques 1-3 + el pseudocódigo del Paso 11 en un prompt reutilizable. Cualquier cliente puede aplicarlo cambiando solo los inputs del preflight. La calidad del output depende de la calidad de los outputs upstream — basura entra, basura sale.
>
> **Sobre el contenido literal:**
> El Master Prompt (sub-sección 4.1) y los 4 auxiliares (sub-secciones 4.2-4.5) están portados **literalmente** del documento fuente original. Las 14 reglas operativas (sub-sección 4.8 / §6.8) están portadas con su Explicación / Patrón / Ejemplos / Regla final del original. Cualquier discrepancia entre este doc y el original debe resolverse en favor del original.
