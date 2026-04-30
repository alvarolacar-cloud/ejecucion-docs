Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# Paso 5 — Page Type Rules

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 12 outputs del Paso 5 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, obtención de outputs, checklist final y outputs consolidados.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 5

<small>§2</small>

En este paso la IA produce todos los outputs que definen **cómo se construye cada page type del cluster** — outputs globales (Primary Service, Brand tone), specs por page type (Función, URL, H1, Meta Title, Meta Description, Word count, Estructura, Schema, Internal links) y validaciones cross-cutting (Schema por tipo, Word count por intención, CTA por funnel, No false location). Todos se generan a partir de los inputs heredados de Pasos 1-4.

**Outputs del paso:**

- **5.1** Primary Service — servicio único hero del cluster (uno de los 5 core services)
- **5.2** Brand tone — registro lingüístico aplicado a TODA la copy (Professional / Friendly / Premium / Urgente / Local)
- **5.3** Spec Homepage — Root Entity Anchor (9 sub-outputs: Función, Patrón URL, H1, Meta Title, Meta Description, Word count, Estructura, Schema, Internal links)
- **5.4** Spec Service Overview Page — Topical Authority Pillar (9 sub-outputs)
- **5.5** Spec Location-Based Service Page — Main City Converter (9 sub-outputs)
- **5.6** Spec Additional Category Page — GBP Additional Category Support (9 sub-outputs)
- **5.7** Spec GeoHub Page — Main City Silo Container (9 sub-outputs)
- **5.8** Spec GeoArticle Page — Semantic Booster (9 sub-outputs)
- **5.9** Validación Schema por tipo de página (cross-cutting)
- **5.10** Validación Word count por intención (cross-cutting)
- **5.11** Validación CTA adaptado al page type (cross-cutting)
- **5.12** Validación No false location claims (cross-cutting)

**Errores que previene:**

- Confundir Service Overview con Location-Based Service
- Convertir GeoArticles en landing pages
- Crear Additional Category Pages duplicadas con core services
- Usar el mismo schema en todos los tipos de página
- Escribir páginas sin word count, CTA, FAQs ni estructura definida
- Brand tone inconsistente entre page types
- Inventar Primary Service fuera del top 5 heredado

**Cuándo se ejecuta:** después de Pasos 1-4 cerrados (intake + fórmula + matriz + URL rules). Antes de Paso 6 (content architecture) y Paso 15 (redacción).

## Info heredada de pasos anteriores

<small>§3</small>

> Estos campos NO se deciden en Paso 5 — la IA los lee del paso indicado y los usa como input para generar las specs del Bloque III.

| Campo | Origen |
|---|---|
| Business Name | Paso-01 1.1 |
| Website Root Domain | Paso-01 1.2 |
| GBP URL (si aplica) | Paso-01 1.3 |
| Full NAP (Name, Address, Phone, Email) | Paso-01 1.4 |
| Planned Primary GBP Category | Paso-01 1.5 |
| Planned Additional GBP Categories que necesitan página | Paso-01 1.6 |
| Main City | Paso-01 1.7 |
| Physical Location City | Paso-01 1.8 |
| Servicios principales (5 core services) | Paso-01 1.9 |
| Local Coverage Areas (Direct + Candidate) | Paso-01 1.10 |
| Approved Expansion Areas | Paso-01 1.11 |
| Preferred CTA | Paso-01 1.13 |
| Trust Signals | Paso-01 1.14 |
| Primary Category Slug, Main City Slug, Service Slugs | Paso-02 2.2 + 2.3 + 2.4 |
| Additional Category Slugs | Paso-03 3.3 |
| URL patterns por page type | Paso-04 4.3 a 4.8 |

> Los outputs nuevos que produce Paso 5 (Primary Service y Brand tone) se desarrollan en §6.1 y §6.2 del Bloque III — no son inputs heredados sino outputs propios del paso.

# Bloque II — Ejemplo rellenado para el Paso 5 — Page Type Rules

<small>§4</small>

> Los 12 outputs del Paso 5 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 5.X declarado en §5.

### 5.1 — Primary Service

`Cerrajero urgente`

(Heredado del top 5 servicios de Paso-01 1.9; elegido por mayor volumen de búsqueda local + alta intención de emergencia.)

### 5.2 — Brand tone

`Urgente`

(El sector cerrajería urgente tiene comportamiento de emergencia — el cliente busca solución rápida, no contemplación. Aplica a TODA la copy del cluster: H1, Meta Title, Meta Description, body, FAQs, CTA.)

### 5.3 — Spec Homepage (Root Entity Anchor)

| # | Sub-output | Valor |
|---|---|---|
| 1 | Función | Root Entity Anchor — concentra señales de marca y entidad; establece marca, categoría GBP, Main City, servicios, cobertura y contacto |
| 2 | Patrón URL | `/` |
| 3 | H1 | Cerrajeros Madrid 24h – Cerrajero urgente de confianza en Madrid |
| 4 | Meta Title | Cerrajero urgente en Madrid \| Cerrajeros Madrid 24h |
| 5 | Meta Description | ¿Necesitas cerrajero urgente en Madrid? Cerrajeros Madrid 24h ofrece servicio local, soporte experto y respuesta rápida. Llama hoy. |
| 6 | Word count | 900–1,300 |
| 7 | Estructura completa | H1 → Intro con marca + servicio + Main City → Quick Answer → Servicios principales → Vista previa cobertura local → Bloques de confianza → FAQ → Bloque NAP → CTA → Enlaces internos |
| 8 | Schema | Organization + WebSite + LocalBusiness + FAQPage + Speakable |
| 9 | Internal links | Service Overview Pages (5), GeoHub `/madrid/`, Additional Category Page `/cerrajero/madrid/duplicado-llaves/`, `/contacto/` |

### 5.4 — Spec Service Overview Page (Topical Authority Pillar)

| # | Sub-output | Valor |
|---|---|---|
| 1 | Función | Topical Authority Pillar — pilar temático no geolocalizado |
| 2 | Patrón URL | `/cerrajero/[service-slug]/` (5 instancias: cerrajero-urgente, apertura-puertas, cambio-cerraduras, cambio-bombines, instalacion-cerraduras-seguridad) |
| 3 | H1 (template) | Servicios profesionales de [Service] por Cerrajeros Madrid 24h |
| 4 | Meta Title (template) | [Service] por Cerrajeros Madrid 24h \| Expertos en cerrajería |
| 5 | Meta Description (template) | ¿Necesitas [Service] de confianza? Cerrajeros Madrid 24h ofrece soluciones expertas, rápidas y cuidadosas. Consulta el proceso completo y sus beneficios. |
| 6 | Word count | 850–1,000 |
| 7 | Estructura completa | H1 → Intro no local → H2 Authority → H2 Uniqueness → H2 Depth → H2 Intent → H2 Optimization → Bullet sections → FAQs → CTA → Enlaces internos |
| 8 | Schema | Service + WebPage + BreadcrumbList + Speakable |
| 9 | Internal links | Homepage, otras Service Overview, LBS correspondiente en Madrid, GeoArticle relevante |

### 5.5 — Spec Location-Based Service Page (Main City Converter)

| # | Sub-output | Valor |
|---|---|---|
| 1 | Función | Main City Converter — convierte búsquedas locales servicio + Main City |
| 2 | Patrón URL | `/cerrajero/madrid/[service-slug]/` (5 instancias) |
| 3 | H1 (template) | Cerrajeros Madrid 24h – [Service] en Madrid |
| 4 | Meta Title (template) | Top [Service] en Madrid \| Cerrajeros Madrid 24h |
| 5 | Meta Description (template) | ¿Necesitas [Service] en Madrid? Cerrajeros Madrid 24h ayuda con [problema 1], [problema 2] y [problema 3]. Llama para recibir soporte local. |
| 6 | Word count | 800–1,000 |
| 7 | Estructura completa | H1 → Intro local → Quick Local Answer → H2 Authority → H2 Uniqueness → H2 Depth → H2 Local Pain Points → H2 Local Coverage Areas Served (Almagro, Chamberí, Salamanca, Retiro mencionadas naturalmente) → H2 Related Services in Madrid → FAQs → CTA → Enlaces internos |
| 8 | Schema | LocalBusiness + BreadcrumbList + FAQPage (opcional) + Speakable (opcional) |
| 9 | Internal links | Parent Service Overview (`/cerrajero/[service]/`), GeoHub `/madrid/`, otras LBS Madrid, GeoArticles relacionados, `/contacto/` |

### 5.6 — Spec Additional Category Page (GBP Additional Category Support)

| # | Sub-output | Valor |
|---|---|---|
| 1 | Función | GBP Additional Category Support — soporta categoría adicional GBP no cubierta por core service |
| 2 | Patrón URL | `/cerrajero/madrid/duplicado-llaves/` (1 instancia: A=1) |
| 3 | H1 | Cerrajeros Madrid 24h – Duplicado de llaves experto en Madrid |
| 4 | Meta Title | Duplicado de llaves en Madrid \| Cerrajeros Madrid 24h |
| 5 | Meta Description | ¿Necesitas duplicado de llaves en Madrid? Cerrajeros Madrid 24h ofrece ayuda fiable para [caso 1], [caso 2] y [caso 3]. Llama hoy. |
| 6 | Word count | 800–1,000 |
| 7 | Estructura completa | H1 → Intro con problema local → H2 Authority → H2 Uniqueness → H2 Depth → H2 Intent → H2 Optimization → Local Coverage Use Case → FAQs → CTA → Enlaces internos |
| 8 | Schema | Service (con `areaServed`) + BreadcrumbList + FAQPage (opcional) + Speakable (opcional) |
| 9 | Internal links | GeoHub `/madrid/`, LBS Madrid relacionadas (cambio-cerraduras, instalacion-cerraduras-seguridad), GeoArticles relevantes, `/contacto/` |

### 5.7 — Spec GeoHub Page (Main City Silo Container)

| # | Sub-output | Valor |
|---|---|---|
| 1 | Función | Main City Silo Container — agrupa todas las señales de la Main City |
| 2 | Patrón URL | `/madrid/` (Option A — heredado de Paso-03 3.2) |
| 3 | H1 | Cerrajeros Madrid 24h – Servicios de cerrajería en Madrid |
| 4 | Meta Title | Servicios de cerrajería en Madrid \| Cerrajeros Madrid 24h |
| 5 | Meta Description | Descubre servicios de cerrajería de confianza en Madrid de Cerrajeros Madrid 24h. Servicios locales, recursos útiles, áreas de cobertura y formas de contactar. |
| 6 | Word count | 700–1,100 |
| 7 | Estructura completa | H1 → City Intro → Menú de servicios (5 LBS) → Additional Category Menu (Duplicado de llaves) → Local Coverage Areas Section (Almagro, Chamberí, Salamanca, Retiro, etc.) → GeoArticle Resources (15 GA) → Trust Signals → CTA → Enlaces internos |
| 8 | Schema | CollectionPage + BreadcrumbList + LocalBusiness (opcional si presencia física) |
| 9 | Internal links | Homepage, las 5 LBS de Madrid, AC Page (Duplicado de llaves), los 15 GeoArticles de Madrid, `/contacto/` |

### 5.8 — Spec GeoArticle Page (Semantic Booster)

| # | Sub-output | Valor |
|---|---|---|
| 1 | Función | Semantic Booster — apoya servicio + Main City + intención long-tail; no es landing comercial |
| 2 | Patrón URL | `/madrid/[article-topic-slug]/` (15 instancias = G × S = 3 × 5) |
| 3 | H1 (ejemplo de un GA) | Precio de cerrajero urgente en Madrid |
| 4 | Meta Title (ejemplo) | Precio de cerrajero urgente en Madrid \| Cerrajeros Madrid 24h |
| 5 | Meta Description (ejemplo) | Aprende sobre el precio de cerrajero urgente en Madrid: qué esperar, errores comunes, factores locales y cuándo llamar a Cerrajeros Madrid 24h. |
| 6 | Word count | 1,000–1,500 |
| 7 | Estructura completa | H1 → Intro contextual → H2 Problem → H2 Local Context → H2 Options / Mistakes → H2 When to Call → H2 Local Examples → FAQs → CTA → Enlaces internos |
| 8 | Schema | Article + FAQPage + BreadcrumbList + Speakable |
| 9 | Internal links | Matching LBS Madrid (`/cerrajero/madrid/cerrajero-urgente/`), GeoHub `/madrid/`, GeoArticles relacionados, `/contacto/` |

### 5.9 — Validación Schema por tipo de página

Cumplido — cada page type lleva su schema obligatorio:

| Page Type | Schema |
|---|---|
| Homepage | Organization + WebSite + LocalBusiness + FAQPage + Speakable |
| Service Overview | Service + WebPage + BreadcrumbList + Speakable |
| Location-Based Service | LocalBusiness + BreadcrumbList + FAQPage (opc) + Speakable (opc) |
| Additional Category | Service (con areaServed) + BreadcrumbList + FAQPage (opc) + Speakable (opc) |
| GeoHub | CollectionPage + BreadcrumbList + LocalBusiness (opc) |
| GeoArticle | Article + FAQPage + BreadcrumbList + Speakable |

### 5.10 — Validación Word count por intención

Cumplido — rangos alineados con funnel:

| Page Type | Word count | Razón |
|---|---|---|
| Homepage | 900–1,300 | Page de entidad — necesita profundidad |
| Service Overview | 850–1,000 | Pilar temático sin geo — depth pero sin local context |
| Location-Based Service | 800–1,000 | Conversión rápida con local context |
| Additional Category | 800–1,000 | Similar a LBS pero categoría secundaria |
| GeoHub | 700–1,100 | Hub navegacional, less prose |
| GeoArticle | 1,000–1,500 | Long-tail informacional, máxima depth |

### 5.11 — Validación CTA adaptado al page type

Cumplido — CTA adaptado al funnel:

| Page Type | CTA | Razón |
|---|---|---|
| Homepage | Llamar ahora | Alta intención de conversión |
| Service Overview | Solicitar presupuesto | Media intención (consultivo) |
| Location-Based Service | Llamar ahora | Alta intención de conversión local |
| Additional Category | Solicitar presupuesto | Media intención |
| GeoHub | Llamar ahora | Alta intención (hub local) |
| GeoArticle | Leer LBS / Llamar | Navegación al funnel comercial |

### 5.12 — Validación No false location claims

Cumplido — todas las URLs usan Main City `madrid` o slug-funcional. Ninguna implica oficina física en LCAs (Almagro, Chamberí, Salamanca, Retiro solo se mencionan en contenido y schema `areaServed`).

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 12 outputs que el Paso 5 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `5.3`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 5.1 | Primary Service | String (1 de 5 core services) | GMB Crush + Datos de búsqueda | Paso-01 1.9 |
| 5.2 | Brand tone | Enum (5 opciones) | Decisión de diseño | — |
| 5.3 | Spec Homepage | 9 sub-outputs (Función, URL, H1, Meta Title, Meta Description, Word count, Estructura, Schema, Internal links) | GMB Crush | Paso-01 1.1 + 1.4 + 1.13 + 1.14 + Paso-04 4.3 |
| 5.4 | Spec Service Overview | 9 sub-outputs × S=5 instancias | GMB Crush | Paso-01 1.9 + Paso-02 2.4 + Paso-04 4.4 |
| 5.5 | Spec Location-Based Service | 9 sub-outputs × S=5 instancias | GMB Crush | Paso-01 1.9 + 1.10 + Paso-02 2.4 + Paso-04 4.6 |
| 5.6 | Spec Additional Category | 9 sub-outputs × A=1 instancia | GMB Crush | Paso-01 1.6 + Paso-03 3.3 + Paso-04 4.7 |
| 5.7 | Spec GeoHub | 9 sub-outputs (instancia única) | GMB Crush | Paso-01 1.7 + 1.10 + Paso-02 2.3 + Paso-04 4.5 |
| 5.8 | Spec GeoArticle | 9 sub-outputs × G×S=15 instancias | GMB Crush | Paso-01 1.7 + Paso-03 3.4 + Paso-04 4.8 |
| 5.9 | Validación Schema por tipo de página | Validation flag | GMB Crush | — |
| 5.10 | Validación Word count por intención | Validation flag | GMB Crush | — |
| 5.11 | Validación CTA adaptado al page type | Validation flag | GMB Crush | Paso-01 1.13 |
| 5.12 | Validación No false location claims | Validation flag | GMB Crush | Paso-01 1.8 + 1.10 + Paso-04 4.14 |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 12 outputs (5.1–5.12). Los outputs **5.1 Primary Service** y **5.2 Brand tone** usan el patrón estándar (Explicación / Patrón / Ejemplos / Regla final / Validación operativa / Cómo se obtiene / Output del paso). Las **6 specs por page type** (5.3–5.8) usan un mini-patrón adaptado: **Función / 9 sub-outputs (URL, H1, Meta Title, Meta Description, Word count, Estructura, Schema, Internal links) / Ejemplos incorrectos / Regla operativa / Output del paso**. Las **4 validaciones cross-cutting** (5.9–5.12) usan el patrón estándar.

### 5.1 — Primary Service

<small>§6.1</small>

**Explicación**

El Primary Service es el servicio único elegido como **hero del cluster** — protagoniza el H1 y Meta Title de la Homepage y guía la voz del cluster entero. Es uno de los 5 core services heredados del Paso-01 1.9, escogido por mayor volumen de búsqueda local + alta intención.

**Patrón o fórmula**

```text
Primary Service ∈ Servicios principales (Paso-01 1.9)
Criterio de elección: el de mayor volumen de búsqueda local del top 5
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Primary Service: Cerrajero urgente
Razón: el más demandado del top 5 — alta intención de emergencia + alto volumen
```

**Ejemplos incorrectos**

```text
- Inventar un servicio que no está en el top 5 heredado
- Elegir el menos demandado por motivos personales
- Cambiar Primary Service mid-build (rompe H1, Meta Title, breadcrumbs)
- Usar un servicio adicional (de Paso-01 1.6) en lugar de un core service
```

**Regla final**

```text
El Primary Service es uno de los 5 core services heredados y se mantiene constante durante toda la construcción del cluster.
```

**Validación operativa**

El Primary Service decidido aquí se hereda al H1 y Meta Title de la Homepage (5.3), aparece en bloques de presentación de servicios y guía las decisiones de Brand tone (5.2). Cambiarlo después de empezar la construcción rompe la consistencia del cluster.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Datos de búsqueda.
- **Método:** La doctrina dicta tomar el top 5 servicios del Paso-01 1.9 y elegir el de mayor volumen de búsqueda local. Cruzar con keyword research (Ahrefs, Semrush, Google Keyword Planner) para identificar volúmenes mensuales en la Main City. Elegir el de mayor volumen como Primary Service.

**Output del paso**

- **Tipo:** String — uno de los 5 core services heredados.
- **Ejemplo (Cerrajeros Madrid 24h):** `Cerrajero urgente`.

### 5.2 — Brand tone

<small>§6.2</small>

**Explicación**

El Brand tone es el registro lingüístico que rige TODA la copy del cluster — H1, Meta Title, Meta Description, body content, FAQs, CTA. Una sola elección consistente entre las 5 opciones disponibles.

**Patrón o fórmula**

```text
Brand tone ∈ {Professional, Friendly, Premium, Urgente, Local and conversational}
Criterio: alinear con el sector y el comportamiento esperado del cliente
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Brand tone: Urgente
Razón: el sector cerrajería urgente tiene comportamiento de emergencia —
       el cliente busca solución rápida, no contemplación
```

**Ejemplos incorrectos**

```text
- Mezclar tonos en page types (Premium en Homepage + Urgente en LBS)
- Elegir Premium para un negocio de servicios urgentes
- No declarar Brand tone (deja al redactor inventar tono inconsistente)
- Cambiar Brand tone mid-build
```

**Regla final**

```text
Un solo Brand tone aplica a TODA la copy del cluster, decidido antes de empezar redacción.
```

**Validación operativa**

El Brand tone se aplica desde la Homepage hasta los GeoArticles. Si se permite que page types distintos tengan tonos distintos, la entidad proyecta inconsistencia. Validar que H1, Meta Title, Meta Description, body, FAQs y CTA de las 28 URLs del cluster siguen el tono declarado.

**Cómo se obtiene**

- **Fuente:** Decisión de diseño.
- **Método:** Elegir entre las 5 opciones según sector y comportamiento esperado del cliente:
  - `Professional` — B2B, servicios técnicos, asesoría
  - `Friendly` — servicios cotidianos, comunidad, repetición
  - `Premium` — alto ticket, experiencia, exclusividad
  - `Urgente` — emergencia, urgencias, respuesta inmediata
  - `Local and conversational` — servicios de barrio, proximidad

**Output del paso**

- **Tipo:** Enum — una de las 5 opciones.
- **Ejemplo (Cerrajeros Madrid 24h):** `Urgente`.

### 5.3 — Spec Homepage (Root Entity Anchor)

<small>§6.3</small>

**Explicación**

La homepage es la **raíz de entidad** del negocio. Establece quién es la marca, qué categoría GBP soporta, cuál es la Main City, qué servicios ofrece, qué cobertura local tiene y cómo contactar. NO es una página decorativa ni un simple escaparate — es el contenedor principal de la entidad local.

**9 sub-outputs de la spec**

```text
1. Función:                  Root Entity Anchor
2. Patrón URL:               /
3. H1 (template):            [Brand Name] – [Primary Service] de confianza en [Main City]
4. Meta Title:               [Primary Service] en [Main City] | [Brand Name]
5. Meta Description:         ¿Necesitas [Primary Service] en [Main City]? [Brand Name] ofrece servicio local, soporte experto y respuesta rápida. Llama hoy.
6. Word count:               900–1,300
7. Estructura completa:      H1 → Intro con marca + servicio + Main City → Quick Answer → Servicios principales → Vista previa cobertura local → Bloques de confianza → Sección FAQ → Bloque NAP → CTA → Enlaces internos
8. Schema:                   Organization + WebSite + LocalBusiness (si physical presence) + FAQPage + Speakable
9. Internal links:           Service Overview Pages (S), Main City GeoHub, Additional Category Pages, Página de contacto
```

**Ejemplos incorrectos**

```text
- Homepage with no services
- Homepage targeting five cities equally
- Homepage without NAP
- Homepage without links to service pages
```

**Regla operativa**

**1. Homepage — Root Entity Anchor.** La homepage no es una página decorativa. Es el contenedor principal de la entidad local y debe establecer marca, categoría GBP, servicio principal, Main City, NAP, señales de confianza y enlaces a las páginas clave.

**Validación operativa**

Aplicar la spec a la Homepage del cluster. Validar los 9 sub-outputs. Cruce con Paso 6 §6.6 (Homepage Content Architecture) que define el body content y Paso 7 §6.2 (Homepage distribuye autoridad) que valida los enlaces internos.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la spec con los inputs heredados — Brand Name (Paso-01 1.1), NAP (Paso-01 1.4), Primary Service (5.1), Main City (Paso-01 1.7), Trust Signals (Paso-01 1.14), Preferred CTA (Paso-01 1.13). Generar H1, Meta Title, Meta Description con templates rellenando placeholders.

**Output del paso**

- **Tipo:** Spec completa de Homepage — 9 sub-outputs (Función, Patrón URL, H1, Meta Title, Meta Description, Word count, Estructura completa, Schema, Internal links).
- **Ejemplo (Cerrajeros Madrid 24h):** Ver §4 sub-sección 5.3 — tabla con los 9 sub-outputs rellenos.

### 5.4 — Spec Service Overview Page (Topical Authority Pillar)

<small>§6.4</small>

**Explicación**

Esta página educa sobre un servicio **sin geolocalización**. Es el pilar temático que soporta la versión local del servicio en la Main City y cualquier futura expansión aprobada. Hay S instancias (S=5 para Cerrajeros).

**9 sub-outputs de la spec**

```text
1. Función:                  Topical Authority Pillar
2. Patrón URL:               /[primary-category-slug]/[service-slug]/
3. H1 (template):            Servicios profesionales de [Service] por [Brand Name]
4. Meta Title:               [Service] por [Brand Name] | Expertos en [Primary Category]
5. Meta Description:         ¿Necesitas [Service] de confianza? [Brand Name] ofrece soluciones expertas, rápidas y cuidadosas. Consulta el proceso completo y sus beneficios.
6. Word count:               850–1,000
7. Estructura completa:      H1 → Intro no local → H2 Authority → H2 Uniqueness → H2 Depth → H2 Intent → H2 Optimization → Bullet sections → FAQs → CTA → Enlaces internos
8. Schema:                   Service + WebPage + BreadcrumbList + Speakable
9. Internal links:           Homepage, otras Service Overview Pages, LBS Main City correspondiente, GeoArticle relevante
```

**Ejemplos incorrectos**

```text
- Mentioning Madrid as the primary target
- Using /cerrajero/madrid/cerrajero-urgente/ as service overview
- No links to local version
- Thin content under 400 words
```

**Regla operativa**

**2. Service Overview Page — Topical Authority Pillar.** La Service Overview Page crea autoridad temática sobre un servicio sin enfocarse en ciudad. Debe explicar el servicio, proceso, problemas resueltos, FAQs y enlaces a su versión Main City.

**Validación operativa**

Aplicar la spec a las S=5 instancias de Service Overview Page (una por core service). Validar que NINGUNA SO menciona Madrid como target principal — su rol es pilar temático. Cruce con Paso 6 §6.7 (SO Content Architecture) y Paso 7 §6.3 (SO empuja la versión local).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la spec replicada a los S core services. Generar H1, Meta Title, Meta Description rellenando [Service] con cada uno de los 5 core services heredados (Paso-01 1.9). URL pattern usa `[primary-category-slug]` (Paso-02 2.2) + `[service-slug]` (Paso-02 2.4).

**Output del paso**

- **Tipo:** Spec completa de Service Overview Page — 9 sub-outputs replicados para los S=5 core services.
- **Ejemplo (Cerrajeros Madrid 24h):** Ver §4 sub-sección 5.4 — tabla con los 9 sub-outputs rellenos. 5 instancias (cerrajero-urgente, apertura-puertas, cambio-cerraduras, cambio-bombines, instalacion-cerraduras-seguridad).

### 5.5 — Spec Location-Based Service Page (Main City Converter)

<small>§6.5</small>

**Explicación**

Esta página convierte búsquedas locales de alta intención para una combinación exacta: **servicio + Main City**. Es una de las páginas más importantes para soporte GBP y Local Pack. Hay S instancias (S=5).

**9 sub-outputs de la spec**

```text
1. Función:                  Main City Converter
2. Patrón URL:               /[primary-category-slug]/[main-city-slug]/[service-slug]/
3. H1 (template):            [Brand Name] – [Service] en [Main City]
4. Meta Title:               Top [Service] en [Main City] | [Brand Name]
5. Meta Description:         ¿Necesitas [Service] en [Main City]? [Brand Name] ayuda con [problema 1], [problema 2] y [problema 3]. Llama para recibir soporte local.
6. Word count:               800–1,000
7. Estructura completa:      H1 → Intro local → Quick Local Answer → H2 Authority → H2 Uniqueness → H2 Depth → H2 Local Pain Points → H2 Local Coverage Areas Served → H2 Related Services in [Main City] → FAQs → CTA → Enlaces internos
8. Schema:                   LocalBusiness + BreadcrumbList + FAQPage (opcional) + Speakable (opcional)
9. Internal links:           Parent Service Overview, Main City GeoHub, otras LBS Main City, GeoArticles relacionados, Contacto
```

**Ejemplos incorrectos**

```text
- Mezclar Madrid and Almagro as equal targets
- Crear una página por cada zona de cobertura sin aprobación
- Afirmar una oficina en Salamanca
- Combinar apertura de puertas y cambio de cerraduras en una sola landing local
```

**Regla operativa**

**3. Location-Based Service Page — Main City Converter.** La Location-Based Service Page es la página comercial más importante para una combinación servicio + Main City. Debe tener intención local, CTA, reviews, contenido GEO y enlaces a padre, GeoHub y artículos.

**Validación operativa**

Aplicar la spec a las S=5 instancias de LBS. Validar que cada LBS tiene una H2 Local Coverage Areas Served con LCAs heredadas (Paso-01 1.10) mencionadas naturalmente — sin afirmar oficinas físicas en zonas sin sede. Cruce con Paso 6 §6.8 (LBS Content Architecture) y Paso 7 §6.5 (LBS conecta servicio y ciudad).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la spec replicada a los S core services × Main City. URL pattern usa `[primary-category-slug]/[main-city-slug]/[service-slug]/`. Schema LocalBusiness incluye `areaServed` con TODAS las LCAs declaradas (Paso-01 1.10).

**Output del paso**

- **Tipo:** Spec completa de Location-Based Service Page — 9 sub-outputs replicados para los S=5 core services en la Main City.
- **Ejemplo (Cerrajeros Madrid 24h):** Ver §4 sub-sección 5.5 — tabla con los 9 sub-outputs rellenos. 5 instancias (cerrajero-urgente, apertura-puertas, cambio-cerraduras, cambio-bombines, instalacion-cerraduras-seguridad) en Madrid.

### 5.6 — Spec Additional Category Page (GBP Additional Category Support)

<small>§6.6</small>

**Explicación**

Esta página soporta una **categoría adicional real del GBP** que NO está cubierta por un servicio core. Refuerza la profundidad de entidad y la relevancia semántica. Hay A instancias (A=1 para Cerrajeros — solo "Duplicado de llaves").

**9 sub-outputs de la spec**

```text
1. Función:                  GBP Additional Category Support
2. Patrón URL:               /[primary-category-slug]/[main-city-slug]/[additional-category-slug]/
3. H1 (template):            [Brand Name] – [Additional Service] experto en [Main City]
4. Meta Title:               [Additional Service] en [Main City] | [Brand Name]
5. Meta Description:         ¿Necesitas [Additional Service] en [Main City]? [Brand Name] ofrece ayuda fiable para [caso 1], [caso 2] y [caso 3]. Llama hoy.
6. Word count:               800–1,000
7. Estructura completa:      H1 → Intro con problema local → H2 Authority → H2 Uniqueness → H2 Depth → H2 Intent → H2 Optimization → Local Coverage Use Case → FAQs → CTA → Enlaces internos
8. Schema:                   Service (con areaServed) + BreadcrumbList + FAQPage (opcional) + Speakable (opcional)
9. Internal links:           Main City GeoHub, LBS Main City relacionadas, GeoArticles relevantes, Contacto
```

**Ejemplos incorrectos**

```text
- Crear /cerrajero/madrid/cerrajero-urgente/ when urgente is already covered
- No local context
- No links to GeoHub
- Category page with no relation to GBP
```

**Regla operativa**

**4. Additional Category Page — GBP Additional Category Support.** Las Additional Category Pages existen para soportar categorías adicionales reales del GBP que no estén ya cubiertas por servicios core. Su formato es local porque refuerzan relevancia de categoría en la Main City.

**Validación operativa**

Aplicar la spec a las A instancias de AC efectivas (las que necesitan página propia según Paso-01 1.6 + Paso-02 2.7). Validar que cada AC NO duplica un core service ya existente. Cruce con Paso 6 §6.9 (AC Content Architecture) y Paso 7 §6.6 (AC se integra en silo local).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la spec a cada Additional Category con página propia. URL pattern usa `[primary-category-slug]/[main-city-slug]/[additional-category-slug]/` con slugs heredados de Paso-03 3.3.

**Output del paso**

- **Tipo:** Spec completa de Additional Category Page — 9 sub-outputs replicados para A categorías efectivas.
- **Ejemplo (Cerrajeros Madrid 24h):** Ver §4 sub-sección 5.6 — tabla con los 9 sub-outputs rellenos. 1 instancia (Duplicado de llaves; A=1).

### 5.7 — Spec GeoHub Page (Main City Silo Container)

<small>§6.7</small>

**Explicación**

El GeoHub agrupa todas las **señales de la Main City**. Es el índice local del sitio: servicios, categorías adicionales, artículos, cobertura local, confianza y contacto. Es el hub de navegación local del cluster.

**9 sub-outputs de la spec**

```text
1. Función:                  Main City Silo Container
2. Patrón URL:               /[main-city-slug]/  (Option A — heredado Paso-03 3.2)
                             OR /[primary-category-slug]/[main-city-slug]/  (Option B)
3. H1 (template):            [Brand Name] – [Industry] Services in [Main City]
4. Meta Title:               [Industry] Services in [Main City] | [Brand Name]
5. Meta Description:         Descubre servicios de [Industry] de confianza en [Main City] de [Brand Name]. Servicios locales, recursos útiles, áreas de cobertura y formas de contactar.
6. Word count:               700–1,100
7. Estructura completa:      H1 → City Intro → Menú de servicios (S LBS) → Additional Category Menu (A AC) → Local Coverage Areas Section → GeoArticle Resources (G×S GAs) → Trust Signals → CTA → Enlaces internos
8. Schema:                   CollectionPage + BreadcrumbList + LocalBusiness (opcional si physical presence)
9. Internal links:           Homepage, las S LBS de Main City, A AC Pages, los G×S GeoArticles, Página de contacto
```

**Ejemplos incorrectos**

```text
- GeoHub with only generic city text
- No links to service pages
- Treating Almagro as a child page without approval
- No CTA
```

**Regla operativa**

**5. GeoHub Page — Main City Silo Container.** El GeoHub organiza todas las señales de la Main City: servicios, categorías adicionales, GeoArticles, cobertura local, confianza y contacto. No es una landing de un servicio concreto.

**Validación operativa**

Aplicar la spec a la única instancia de GeoHub (1 por cluster). Validar que la Local Coverage Areas Section lista TODAS las LCAs declaradas (Direct + Candidate). Cruce con Paso 6 §6.10 (GeoHub Content Architecture) y Paso 7 §6.4 (GeoHub organiza Main City).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la spec al GeoHub Main City. URL Option A o B según decisión del Paso-03 3.2. Listar TODAS las LCAs (Paso-01 1.10) en sección dedicada. Internal links a las 21 páginas hijas (5 LBS + 1 AC + 15 GAs en Cerrajeros).

**Output del paso**

- **Tipo:** Spec completa de GeoHub Page — 9 sub-outputs (instancia única por cluster).
- **Ejemplo (Cerrajeros Madrid 24h):** Ver §4 sub-sección 5.7 — tabla con los 9 sub-outputs rellenos. 1 instancia (`/madrid/`).

### 5.8 — Spec GeoArticle Page (Semantic Booster)

<small>§6.8</small>

**Explicación**

El GeoArticle NO es una landing comercial. Es un **booster semántico** para un servicio + Main City + intención long-tail. Su misión es apoyar la página comercial (matching LBS) y el GeoHub. Hay G×S instancias (15 para Cerrajeros).

**9 sub-outputs de la spec**

```text
1. Función:                  Semantic Booster
2. Patrón URL:               /[main-city-slug]/[article-topic-slug]/
3. H1 (template):            [Article Topic] in [Main City]
4. Meta Title:               [Article Topic] in [Main City] | [Brand Name]
5. Meta Description:         Aprende sobre [Article Topic] en [Main City]: qué esperar, errores comunes, factores locales y cuándo llamar a [Brand Name].
6. Word count:               1,000–1,500
7. Estructura completa:      H1 → Intro contextual → H2 Problem → H2 Local Context → H2 Options / Mistakes → H2 When to Call → H2 Local Examples → FAQs → CTA → Enlaces internos
8. Schema:                   Article + FAQPage + BreadcrumbList + Speakable
9. Internal links:           Matching Main City Service Page (LBS), Main City GeoHub, GeoArticle relacionado, Contacto
```

**Ejemplos incorrectos**

```text
- Writing as a generic landing page
- No link to service page
- No local examples
- Pretending physical location in every coverage area
```

**Regla operativa**

**6. GeoArticle Page — Semantic Booster.** El GeoArticle no es una landing comercial. Debe cubrir un tema long-tail de servicio + Main City y enlazar a la página comercial correspondiente y al GeoHub.

**Validación operativa**

Aplicar la spec a las G×S=15 instancias (3 por core service). Validar que cada GA enlaza a su matching LBS (Paso 7 §6.7) y al GeoHub. Cruce con Paso 6 §6.11 (GeoArticle Content Architecture) y Paso-03 3.4 (GeoArticle Topics validados con keyword research).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la spec a cada uno de los G×S=15 GeoArticles. URL pattern usa `[main-city-slug]/[article-topic-slug]/`. Topic slugs validados con keyword research (Paso-03 3.4 — método doctrinal de extracción).

**Output del paso**

- **Tipo:** Spec completa de GeoArticle Page — 9 sub-outputs replicados para G×S=15 GAs.
- **Ejemplo (Cerrajeros Madrid 24h):** Ver §4 sub-sección 5.8 — tabla con los 9 sub-outputs rellenos. 15 instancias (3 por servicio × 5 servicios).

### 5.9 — Validación Schema por tipo de página

<small>§6.9</small>

**Explicación**

Cada tipo de página tiene un **schema esperado**. La homepage usa Organization y WebSite; servicios usan Service; landings locales usan LocalBusiness; artículos usan Article y FAQPage. Confundir schema entre page types degrada las señales semánticas que Google y otros consumen.

**Patrón o fórmula**

```text
Page Type → Schema Required → QA gate
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-001 (/cerrajero/madrid/cerrajero-urgente/):
  → LocalBusiness + BreadcrumbList + FAQPage (opcional) + Speakable (opcional)

GA-001 (/madrid/cuanto-cuesta-un-cerrajero-urgente/):
  → Article + FAQPage + BreadcrumbList + Speakable
```

**Ejemplos incorrectos**

```text
- Usar Article schema en una landing comercial
- Usar LocalBusiness con ubicación falsa (Almagro sin sede)
- No añadir BreadcrumbList en páginas internas
- Schema decidido en build-time (no en spec del Paso 5)
```

**Regla final**

```text
Cada tipo de página declara su Schema obligatorio; el implementador no decide en build-time.
```

**Validación operativa**

Aplicar la regla a TODAS las page types del Bloque III como filtro de QA antes de cerrar el spec de cada página. Si una page type publicada lleva schema distinto del declarado, alertar antes del Paso 18 (deploy).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la regla a TODAS las page types del Bloque III como filtro de QA. La doctrina dicta el schema por page type — no es decisión del implementador.

**Output del paso**

- **Tipo:** Validation flag — la regla se cumple en las 6 page types.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque III.

### 5.10 — Validación Word count por intención

<small>§6.10</small>

**Explicación**

El contenido debe tener **suficiente profundidad según el tipo de página**. No se trata de inflar palabras, sino de cubrir intención, proceso, beneficios, FAQs, enlaces y contexto local. Los rangos están alineados con el rol del page type en el funnel.

**Patrón o fórmula**

```text
Page Type → word count objetivo → contenido completo

Rangos doctrinales:
  Homepage:               900–1,300
  Service Overview:       850–1,000
  Location-Based Service: 800–1,000
  Additional Category:    800–1,000
  GeoHub:                 700–1,100
  GeoArticle:             1,000–1,500
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS de Cerrajeros Madrid 24h: 800–1,000 palabras
GA de Cerrajeros Madrid 24h: 1,000–1,500 palabras
Homepage: 900–1,300 palabras
```

**Ejemplos incorrectos**

```text
- Publicar landings de 250 palabras (thin content)
- Crear artículos de 400 palabras sin profundidad
- Repetir bloques para llegar al word count (keyword stuffing)
- Word count fijo (ej. 1,000 para todo) sin alinear con intención
```

**Regla final**

```text
Word count se ajusta a la intención del page type, no a un número fijo arbitrario.
```

**Validación operativa**

Aplicar la regla a TODAS las page types del Bloque III como filtro de QA antes de cerrar el spec de cada página. En Paso 15 (Redacción) se valida el word count real contra el rango doctrinal.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la regla a TODAS las page types del Bloque III como filtro de QA. Los rangos están en cada spec por page type (5.3-5.8).

**Output del paso**

- **Tipo:** Validation flag — la regla se cumple en las 6 page types.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque III.

### 5.11 — Validación CTA adaptado al page type

<small>§6.11</small>

**Explicación**

Cada página debe tener un CTA, pero **no todos los CTAs cumplen la misma función**. Homepage y landings deben convertir; Service Overview puede ser más consultivo; GeoArticle debe enlazar contextual y suavemente al servicio.

**Patrón o fórmula**

```text
Page Type → CTA intent → enlace o acción

Mapeo doctrinal:
  Homepage:               Llamar ahora (alta intención conversión)
  Service Overview:       Solicitar presupuesto (consultivo)
  Location-Based Service: Llamar ahora (alta intención local)
  Additional Category:    Solicitar presupuesto (consultivo)
  GeoHub:                 Llamar ahora (hub local)
  GeoArticle:             Leer LBS / Llamar (navegación al funnel)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
En /cerrajero/madrid/cerrajero-urgente/ (LBS) el CTA es "Llamar ahora"
En /madrid/cuanto-cuesta-un-cerrajero-urgente/ (GA) el CTA invita a
  consultar la página de Cerrajero urgente en Madrid.
```

**Ejemplos incorrectos**

```text
- Usar el mismo CTA genérico en todo el sitio
- No incluir CTA en artículos
- Hacer CTAs agresivos en contenido informativo (GeoArticle)
- Repetir "Llama hoy" en 28 páginas sin variación
```

**Regla final**

```text
El CTA se adapta a la fase del funnel del page type — no es uniforme en todo el cluster.
```

**Validación operativa**

Aplicar la regla a TODAS las page types del Bloque III como filtro de QA antes de cerrar el spec de cada página. El Preferred CTA del Paso-01 1.13 es el default, pero se adapta por page type según el funnel.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la regla a TODAS las page types del Bloque III como filtro de QA. Mapear CTAs a page types según funnel position.

**Output del paso**

- **Tipo:** Validation flag — la regla se cumple en las 6 page types.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque III.

### 5.12 — Validación No false location claims

<small>§6.12</small>

**Explicación**

Cualquier page type puede mencionar cobertura local, pero **ninguno debe inventar oficina física**. Esta regla protege la confianza local y evita contradicciones con GBP, NAP y schema.

**Patrón o fórmula**

```text
Local Coverage Area → servir clientes (areaServed) | NO → oficina ficticia (address)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h puede decir que atiende Almagro, Chamberí, Salamanca y Retiro.
Pero NO puede decir que tiene oficina en Almagro si su ubicación física es Madrid.
```

**Ejemplos incorrectos**

```text
- "Nuestra oficina en Almagro" si no existe
- Mapa de una ubicación no real
- LocalBusiness address en zona de cobertura sin sede
- Schema con city = Salamanca cuando NAP es Madrid
```

**Regla final**

```text
Nunca afirmar ubicación física en zonas donde el negocio no opera realmente.
```

**Validación operativa**

Aplicar la regla a TODAS las page types del Bloque III como filtro de QA antes de cerrar el spec de cada página. Cruce con Paso-01 1.8 (Physical Location City), Paso-01 1.10 (LCAs) y Paso-04 4.14 (No falsa ubicación).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la regla a TODAS las page types del Bloque III como filtro de QA. Validar que el `address` del schema corresponde al NAP físico real y que el `areaServed` lista solo zonas atendidas.

**Output del paso**

- **Tipo:** Validation flag — la regla se cumple en las 6 page types.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque III.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 5 y avanzar al Paso 6 (Estructura de Contenido) o Paso 15 (Redacción).

### Validación de outputs globales

- ☐ Primary Service elegido del top 5 heredado (5.1)
- ☐ Brand tone declarado y aplicable a TODA la copy (5.2)

### Validación de specs por page type

- ☐ Homepage spec con 9 sub-outputs completos (5.3)
- ☐ Service Overview spec con 9 sub-outputs × S instancias (5.4)
- ☐ Location-Based Service spec con 9 sub-outputs × S instancias (5.5)
- ☐ Additional Category spec con 9 sub-outputs × A instancias (5.6)
- ☐ GeoHub spec con 9 sub-outputs (1 instancia) (5.7)
- ☐ GeoArticle spec con 9 sub-outputs × G×S instancias (5.8)

### Validación cross-cutting

- ☐ Schema por tipo de página validado (5.9)
- ☐ Word count por intención validado (5.10)
- ☐ CTA adaptado al page type validado (5.11)
- ☐ No false location claims validado (5.12)

### Validación de doctrina

- ☐ Service Overview no menciona Main City como target principal
- ☐ Location-Based Service combina servicio + Main City
- ☐ GeoArticle es semantic booster (no landing comercial)
- ☐ Schema diferenciado por page type
- ☐ Word count alineado con intención del funnel

## Outputs Consolidados

<small>§8</small>

> Tabla final compacta con la trazabilidad row-per-output. Los IDs (`5.1`–`5.12`) coinciden con los declarados en §5. Esta tabla es la fuente única de la trazabilidad consolidada del paso (sustituye al antiguo b-doc).

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 5.1 | ← Paso-01 1.9 | **Primary Service** = `Cerrajero urgente` | Top 5 servicios cruzados con keyword research; elegir el de mayor volumen local. **Fuente:** GMB Crush + Datos de búsqueda. | confirmed |
| 5.2 | — | **Brand tone** = `Urgente` | Elegir entre las 5 opciones doctrinales según sector y comportamiento esperado. **Fuente:** Decisión de diseño. | confirmed |
| 5.3 | ← Paso-01 1.1 + 1.4 + 1.13 + 1.14 + Paso-04 4.3 | **Spec Homepage (Root Entity Anchor)** = 9 sub-outputs aplicados a `/` | Aplicar la spec con inputs heredados; rellenar templates de H1/Meta con placeholders. **Fuente:** GMB Crush. | confirmed |
| 5.4 | ← Paso-01 1.9 + Paso-02 2.4 + Paso-04 4.4 | **Spec Service Overview (Topical Authority Pillar)** = 9 sub-outputs × 5 instancias (`/cerrajero/{service}/`) | Aplicar spec replicada a los S=5 core services; URL = `[primary-category-slug]/[service-slug]/`. **Fuente:** GMB Crush. | confirmed |
| 5.5 | ← Paso-01 1.9 + 1.10 + Paso-02 2.4 + Paso-04 4.6 | **Spec LBS (Main City Converter)** = 9 sub-outputs × 5 instancias (`/cerrajero/madrid/{service}/`) | Aplicar spec replicada a S core services × Main City; schema LocalBusiness con `areaServed` = LCAs. **Fuente:** GMB Crush. | confirmed |
| 5.6 | ← Paso-01 1.6 + Paso-03 3.3 + Paso-04 4.7 | **Spec Additional Category (GBP AC Support)** = 9 sub-outputs × 1 instancia (`/cerrajero/madrid/duplicado-llaves/`) | Aplicar spec a cada AC con página propia; URL usa slugs de Paso-03 3.3. **Fuente:** GMB Crush. | confirmed |
| 5.7 | ← Paso-01 1.7 + 1.10 + Paso-02 2.3 + Paso-04 4.5 | **Spec GeoHub (Main City Silo Container)** = 9 sub-outputs × 1 instancia (`/madrid/`) | Aplicar spec al GeoHub Main City; listar TODAS las LCAs y enlazar a las 21 páginas hijas. **Fuente:** GMB Crush. | confirmed |
| 5.8 | ← Paso-01 1.7 + Paso-03 3.4 + Paso-04 4.8 | **Spec GeoArticle (Semantic Booster)** = 9 sub-outputs × 15 instancias (`/madrid/{topic}/`) | Aplicar spec a G×S=15 GAs; topic slugs validados con keyword research (Paso-03 3.4). **Fuente:** GMB Crush. | confirmed |
| 5.9 | — | **Validación Schema por tipo de página** = 6 page types con schema diferenciado | Aplicar la regla a las 6 page types del Bloque III como filtro de QA. **Fuente:** GMB Crush. | OK |
| 5.10 | — | **Validación Word count por intención** = Rangos aplicados (Homepage 900-1,300 … GA 1,000-1,500) | Aplicar la regla a las 6 page types del Bloque III como filtro de QA. **Fuente:** GMB Crush. | OK |
| 5.11 | ← Paso-01 1.13 | **Validación CTA adaptado al page type** = CTAs diferenciados por funnel position | Mapear CTAs a page types según funnel position; el Preferred CTA es default. **Fuente:** GMB Crush. | OK |
| 5.12 | ← Paso-01 1.8 + 1.10 + Paso-04 4.14 | **Validación No false location claims** = 0 afirmaciones de oficina en LCAs | Validar que `address` schema = NAP físico real y `areaServed` lista solo zonas atendidas. **Fuente:** GMB Crush. | OK |

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

> **Nota importante — GBP Services ≠ core services del sitio web:**
> Las categorías adicionales del Google Business Profile (como "Servicio de duplicado de llaves") pueden tener página propia en la web, pero **no forman parte de `core_services`**. La variable `core_services` define los 5 servicios principales que generan Service Overview, LBS y GeoArticles. Las Additional Categories con página propia se gestionan por separado mediante `additional_categories_with_page`. No mezclar ambos conjuntos.
