Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo la estructura fija acordada en la conversación.
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# §1 Paso 5 — Page Type Rules

# Bloque I — Introducción

## §2 Objetivo del Paso 5

En este paso la IA toma todas las decisiones que definen cómo se construye cada page type del cluster — decisiones globales (Primary Service, Brand tone), spec por page type (Función, URL, H1, Meta Title, Meta Description, Word count, Estructura, Schema, Internal links) y validaciones cross-cutting (Schema por tipo, Word count por intención, CTA por funnel, No false location). Todas se aplican sobre los inputs heredados de Pasos 1-3.

**Decisiones que se van a tomar en el paso:**

- **Primary Service** elegido (servicio único hero para Homepage, del top 5 heredado)
- **Brand tone** elegido (Professional / Friendly / Premium / Urgente / Local)
- Spec **Homepage** — Root Entity Anchor (Función, URL, H1, Meta Title, Meta Description, Word count, Estructura, Schema, Internal links)
- Spec **Service Overview Page** — Topical Authority Pillar (idem)
- Spec **Location-Based Service Page** — Main City Converter (idem)
- Spec **Additional Category Page** — GBP Additional Category Support (idem)
- Spec **GeoHub Page** — Main City Silo Container (idem)
- Spec **GeoArticle Page** — Semantic Booster (idem)
- Validación cross-cutting (Schema por tipo, Word count por intención, CTA por funnel, No false location)

**Errores que previene:**

- Confundir Service Overview con Location-Based Service
- Convertir GeoArticles en landing pages
- Crear Additional Category Pages duplicadas
- Usar el mismo schema en todos los tipos de página
- Escribir páginas sin word count, CTA, FAQs ni estructura

**Cuándo se ejecuta:** después de Pasos 1-4 cerrados (intake + fórmula + matriz + URL rules). Antes de Paso 6 (content architecture) y Paso 15 (redacción).

## §3 Info heredada de pasos anteriores

> Estos campos NO se deciden en Paso 5 — la IA los lee del paso indicado y los usa como input para generar las specs del Bloque II.

| Campo | Origen |
|---|---|
| Business Name | Paso 1 §5 |
| Website Root Domain | Paso 1 §6 |
| GBP URL (si aplica) | Paso 1 §7 |
| Full NAP (Name, Address, Phone, Email) | Paso 1 §8 |
| Planned Primary GBP Category | Paso 1 §9 |
| Planned Additional GBP Categories que necesitan página | Paso 1 §10 |
| Main City | Paso 1 §11 |
| Physical Location City | Paso 1 §12 |
| Servicios principales (5 core services) | Paso 1 §13 |
| Local Coverage Areas (Direct + Candidate) | Paso 1 §14 |
| Approved Expansion Areas | Paso 1 §15 |
| Preferred CTA | Paso 1 §17 |
| Trust Signals | Paso 1 §18 |
| Primary Category Slug, Main City Slug, Service Slugs | Paso 2 §6 |
| Additional Category Slugs | Paso 3 §7 |

> Las decisiones nuevas que toma Paso 5 (Primary Service y Brand tone) se desarrollan en §5 y §6 del Bloque II — no son inputs heredados sino outputs decisorios del propio paso.

## §4 Ejemplo rellenado

> Solo las decisiones que se toman en Paso 5. Los heredados (Business Name, NAP, Servicios, Categorías GBP, etc.) tienen su ejemplo rellenado en sus pasos de origen (§4 de Paso 1). Las specs por page type tienen su ejemplo en cada `§X.10 Ejemplo rellenado con Cerrajeros Madrid 24h` dentro del Bloque II.

```text
Primary Service:
Cerrajero urgente

Brand tone:
Urgente
```

# Bloque II — Ejecución por la IA

> Bloque II tiene 2 capas: **decisiones globales** (§5 Primary Service, §6 Brand tone) que la IA toma una vez y aplican a todo el cluster; y **page types** (§7-§12) con sus 12 subsections de spec completa + §X.13 Validación operativa.

## §5 Primary Service

### §5.1 Explicación

**Explicación**

El Primary Service es el servicio único elegido como hero del cluster — protagoniza el H1 y Meta Title de la Homepage. Es uno de los 5 core services heredados del Paso 1 §13.

**Patrón o fórmula**

```text
Primary Service ∈ Servicios principales (Paso 1 §13)
Criterio de elección: el de mayor volumen de búsqueda local del top 5
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Primary Service: Cerrajero urgente
(es el más demandado del top 5 — alta intención + alto volumen)
```

**Ejemplos incorrectos**

```text
- Inventar un servicio que no está en el top 5 heredado
- Elegir el menos demandado por motivos personales
- Cambiar Primary Service mid-build (rompe H1, Meta Title, breadcrumbs)
- Usar un servicio adicional (de Paso 1 §10) en lugar de un core service
```

**Regla final**

```text
El Primary Service es uno de los 5 core services heredados y se mantiene constante durante toda la construcción del cluster.
```

### §5.2 Cómo decidimos el Primary Service

**Fuente:** Decisión de diseño + Datos de búsqueda.

**Método:** Tomar el top 5 servicios del Paso 1 §13. Cruzar con keyword research local para identificar cuál tiene mayor volumen de búsqueda mensual en la Main City. Elegir ese como Primary Service.

### §5.3 Decisión registrada

**Tipo:** String — uno de los 5 core services heredados.

**Ejemplo (Cerrajeros Madrid 24h):** `Cerrajero urgente`.

## §6 Brand tone

### §6.1 Explicación

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
Razón: el sector cerrajería urgente tiene comportamiento de emergencia — el cliente busca solución rápida, no contemplación
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

### §6.2 Cómo decidimos el Brand tone

**Fuente:** Decisión de diseño.

**Método:** Elegir entre las 5 opciones según sector y comportamiento esperado del cliente:

- `Professional` — B2B, servicios técnicos, asesoría
- `Friendly` — servicios cotidianos, comunidad, repetición
- `Premium` — alto ticket, experiencia, exclusividad
- `Urgente` — emergencia, urgencias, respuesta inmediata
- `Local and conversational` — servicios de barrio, proximidad

### §6.3 Decisión registrada

**Tipo:** Enum — una de las 5 opciones.

**Ejemplo (Cerrajeros Madrid 24h):** `Urgente`.

## §7 Homepage — Root Entity Anchor

### §7.1 Función

La homepage es la raíz de entidad del negocio. Debe establecer quién es la marca, qué categoría GBP soporta, cuál es la Main City, qué servicios ofrece, qué cobertura local tiene y cómo contactar. No es una página decorativa ni un simple escaparate.

### §7.2 Patrón URL

```text
/
```

### §7.3 H1

```text
[Brand Name] – [Primary Service] de confianza en [Main City]
```

### §7.4 Meta Title

```text
[Primary Service] en [Main City] | [Brand Name]
```

### §7.5 Meta Description

```text
¿Necesitas [Primary Service] en [Main City]? [Brand Name] ofrece servicio local, soporte experto y respuesta rápida. Llama hoy.
```

### §7.6 Word count recomendado

```text
900–1,300 words
```

### §7.7 Estructura completa

```text
H1
Intro with brand + service + Main City
Quick Answer
Servicios principales
Vista previa de cobertura local
Bloques de confianza
Sección FAQ
Bloque NAP
CTA
Enlaces internos
```

### §7.8 Schema requerido

```text
Organization
WebSite
LocalBusiness if physical presence exists in Main City
FAQPage
Speakable
```

### §7.9 Enlaces internos requeridos

```text
Service Overview Pages
Main City GeoHub
Páginas de categoría adicional en la Main City
Página de contacto
```

### §7.10 Ejemplo rellenado con Cerrajeros Madrid 24h

```text
URL: /
H1: Cerrajeros Madrid 24h – Servicios de cerrajería de confianza en Madrid
Meta Title: Cerrajero en Madrid | Cerrajeros Madrid 24h
Servicios principales: Cerrajero urgente, apertura de puertas, cambio de cerraduras, cambio de bombines e instalación de cerraduras de seguridad
Vista previa de cobertura local: Almagro, Chamberí, Salamanca, Retiro
Schema: Organization, WebSite, LocalBusiness, FAQPage, Speakable
```

### §7.11 Ejemplos incorrectos

```text
- Homepage with no services
- Homepage targeting five cities equally
- Homepage without NAP
- Homepage without links to service pages
```

### §7.12 Regla final

```text
1. Homepage — Root Entity Anchor debe cumplir su función específica y no debe mezclarse con otro tipo de página.
```

### §7.13 Validación operativa

La homepage no es una página decorativa. Es el contenedor principal de la entidad local y debe establecer marca, categoría GBP, servicio principal, Main City, NAP, señales de confianza y enlaces a las páginas clave.

## §8 Service Overview Page — Topical Authority Pillar

### §8.1 Función

Esta página educa sobre un servicio sin geolocalización. Es el pilar temático que soporta la versión local del servicio en la Main City y cualquier futura expansión aprobada.

### §8.2 Patrón URL

```text
/[primary-category-slug]/[service-slug]/
```

### §8.3 H1

```text
Servicios profesionales de [Service] por [Brand Name]
```

### §8.4 Meta Title

```text
[Service] por [Brand Name] | Expertos en [Primary Category]
```

### §8.5 Meta Description

```text
¿Necesitas [Service] de confianza? [Brand Name] ofrece soluciones expertas, rápidas y cuidadosas. Consulta el proceso completo y sus beneficios.
```

### §8.6 Word count recomendado

```text
850–1,000 words
```

### §8.7 Estructura completa

```text
H1
Intro no local
H2 Authority
H2 Uniqueness
H2 Depth
H2 Intent
H2 Optimization
Bullet sections
FAQs
CTA
Enlaces internos
```

### §8.8 Schema requerido

```text
Service
WebPage
BreadcrumbList
Speakable
```

### §8.9 Enlaces internos requeridos

```text
Homepage
Related Service Overview Pages
Main City Location-Based Service Page
Relevant GeoArticle
```

### §8.10 Ejemplo rellenado con Cerrajeros Madrid 24h

```text
URL: /cerrajero/cerrajero-urgente/
H1: Servicios profesionales de cerrajería urgente por Cerrajeros Madrid 24h
Meta Title: Cerrajero urgente por Cerrajeros Madrid 24h | Expertos en cerrajería
Enlaces internos: /, /cerrajero/apertura-puertas/, /cerrajero/madrid/cerrajero-urgente/, /madrid/cuanto-cuesta-un-cerrajero-urgente/
```

### §8.11 Ejemplos incorrectos

```text
- Mentioning Madrid as the primary target
- Using /cerrajero/madrid/cerrajero-urgente/ as service overview
- No links to local version
- Thin content under 400 words
```

### §8.12 Regla final

```text
2. Service Overview Page — Topical Authority Pillar debe cumplir su función específica y no debe mezclarse con otro tipo de página.
```

### §8.13 Validación operativa

La Service Overview Page crea autoridad temática sobre un servicio sin enfocarse en ciudad. Debe explicar el servicio, proceso, problemas resueltos, FAQs y enlaces a su versión Main City.

## §9 Location-Based Service Page — Main City Converter

### §9.1 Función

Esta página convierte búsquedas locales de alta intención para una combinación exacta: servicio + Main City. Es una de las páginas más importantes para soporte GBP y Local Pack.

### §9.2 Patrón URL

```text
/[primary-category-slug]/[main-city-slug]/[service-slug]/
```

### §9.3 H1

```text
[Brand Name] – [Service] en [Main City]
```

### §9.4 Meta Title

```text
Top [Service] en [Main City] | [Brand Name]
```

### §9.5 Meta Description

```text
¿Necesitas [Service] en [Main City]? [Brand Name] ayuda con [problema], [problema] y [problema]. Llama para recibir soporte local.
```

### §9.6 Word count recomendado

```text
800–1,000 words
```

### §9.7 Estructura completa

```text
H1
Intro local
Quick Local Answer
H2 Authority
H2 Uniqueness
H2 Depth
H2 Local Pain Points
H2 Local Coverage Areas Served
H2 Related Services in Main City
FAQs
CTA
Enlaces internos
```

### §9.8 Schema requerido

```text
LocalBusiness
BreadcrumbList
FAQPage optional
Speakable optional
```

### §9.9 Enlaces internos requeridos

```text
Parent Service Overview
Main City GeoHub
Other services in Main City
Related GeoArticles
Contacto
```

### §9.10 Ejemplo rellenado con Cerrajeros Madrid 24h

```text
URL: /cerrajero/madrid/cerrajero-urgente/
H1: Cerrajeros Madrid 24h – Cerrajero urgente en Madrid
Local Coverage Areas: Almagro, Chamberí, Salamanca, Retiro mencionadas de forma natural
Enlaces: /cerrajero/cerrajero-urgente/, /madrid/, /cerrajero/madrid/apertura-puertas/, /madrid/cuanto-cuesta-un-cerrajero-urgente/
```

### §9.11 Ejemplos incorrectos

```text
- Mezclar Madrid and Almagro as equal targets
- Crear una página por cada zona de cobertura sin aprobación
- Afirmar una oficina en Salamanca
- Combinar apertura de puertas y cambio de cerraduras en una sola landing local
```

### §9.12 Regla final

```text
3. Location-Based Service Page — Main City Converter debe cumplir su función específica y no debe mezclarse con otro tipo de página.
```

### §9.13 Validación operativa

La Location-Based Service Page es la página comercial más importante para una combinación servicio + Main City. Debe tener intención local, CTA, reviews, contenido GEO y enlaces a padre, GeoHub y artículos.

## §10 Additional Category Page — GBP Additional Category Support

### §10.1 Función

Esta página soporta una categoría adicional real del GBP que no está cubierta por un servicio core. Refuerza la profundidad de entidad y la relevancia semántica.

### §10.2 Patrón URL

```text
/[primary-category-slug]/[main-city-slug]/[additional-category-slug]/
```

### §10.3 H1

```text
[Brand Name] – Expert [Service] en [Main City]
```

### §10.4 Meta Title

```text
[Service] en [Main City] | [Brand Name]
```

### §10.5 Meta Description

```text
¿Necesitas [Service] en [Main City]? [Brand Name] ofrece ayuda fiable para [problema], [caso de uso] y [caso de uso]. Llama hoy.
```

### §10.6 Word count recomendado

```text
800–1,000 words
```

### §10.7 Estructura completa

```text
H1
Intro con problema local
H2 Authority
H2 Uniqueness
H2 Depth
H2 Intent
H2 Optimization
Local Coverage Use Case
FAQs
CTA
Enlaces internos
```

### §10.8 Schema requerido

```text
Service with areaServed
BreadcrumbList
FAQPage optional
Speakable optional
```

### §10.9 Enlaces internos requeridos

```text
Main City GeoHub
Related Location-Based Service Pages
Related GeoArticles
Contacto
```

### §10.10 Ejemplo rellenado con Cerrajeros Madrid 24h

```text
URL: /cerrajero/madrid/duplicado-llaves/
H1: Cerrajeros Madrid 24h – Duplicado de llaves experto en Madrid
Meta Title: Duplicado de llaves en Madrid | Cerrajeros Madrid 24h
Enlaces: /madrid/, /cerrajero/madrid/cambio-cerraduras/, /cerrajero/madrid/instalacion-cerraduras-seguridad/
```

### §10.11 Ejemplos incorrectos

```text
- Crear /cerrajero/madrid/cerrajero-urgente/ when urgente is already covered
- No local context
- No links to GeoHub
- Category page with no relation to GBP
```

### §10.12 Regla final

```text
4. Additional Category Page — GBP Additional Category Support debe cumplir su función específica y no debe mezclarse con otro tipo de página.
```

### §10.13 Validación operativa

Las Additional Category Pages existen para soportar categorías adicionales reales del GBP que no estén ya cubiertas por servicios core. Su formato es local porque refuerzan relevancia de categoría en la Main City.

## §11 GeoHub Page — Main City Silo Container

### §11.1 Función

El GeoHub agrupa todas las señales de la Main City. Es el índice local del sitio: servicios, categorías adicionales, artículos, cobertura local, confianza y contacto.

### §11.2 Patrón URL

```text
/[main-city-slug]/ OR /[primary-category-slug]/[main-city-slug]/
```

### §11.3 H1

```text
[Brand Name] – [Industry] Services in [Main City]
```

### §11.4 Meta Title

```text
[Industry] Services in [Main City] | [Brand Name]
```

### §11.5 Meta Description

```text
Explore trusted [Industry] services in [Main City] from [Brand Name]. View local services, helpful resources, coverage areas, and ways to contact our team.
```

### §11.6 Word count recomendado

```text
700–1,100 words
```

### §11.7 Estructura completa

```text
H1
City Intro
Menú de servicios
Additional Category Menu
Local Coverage Areas Section
GeoArticle Resources
Trust Signals
CTA
Enlaces internos
```

### §11.8 Schema requerido

```text
CollectionPage
BreadcrumbList
LocalBusiness optional if physical presence exists
```

### §11.9 Enlaces internos requeridos

```text
Homepage
All Páginas de servicio en la Main City
Páginas de categoría adicional en la Main City
GeoArticles de la Main City
Página de contacto
```

### §11.10 Ejemplo rellenado con Cerrajeros Madrid 24h

```text
URL: /madrid/
H1: Cerrajeros Madrid 24h – Servicios de cerrajería en Madrid
Menú de servicios: urgente, apertura de puertas, cambio de cerraduras, cambio de bombines, instalación de cerraduras de seguridad
Sección de cobertura: Almagro, Chamberí, Salamanca, Retiro
Enlaces: /cerrajero/madrid/cerrajero-urgente/, /cerrajero/madrid/duplicado-llaves/, /madrid/cuanto-cuesta-un-cerrajero-urgente/
```

### §11.11 Ejemplos incorrectos

```text
- GeoHub with only generic city text
- No links to service pages
- Treating Almagro as a child page without approval
- No CTA
```

### §11.12 Regla final

```text
5. GeoHub Page — Main City Silo Container debe cumplir su función específica y no debe mezclarse con otro tipo de página.
```

### §11.13 Validación operativa

El GeoHub organiza todas las señales de la Main City: servicios, categorías adicionales, GeoArticles, cobertura local, confianza y contacto. No es una landing de un servicio concreto.

## §12 GeoArticle Page — Semantic Booster

### §12.1 Función

El GeoArticle no es una landing comercial. Es un booster semántico para un servicio, una Main City y una intención long-tail. Su misión es apoyar la página comercial y el GeoHub.

### §12.2 Patrón URL

```text
/[main-city-slug]/[article-topic-slug]/
```

### §12.3 H1

```text
[Article Topic] in [Main City]
```

### §12.4 Meta Title

```text
[Article Topic] in [Main City] | [Brand Name]
```

### §12.5 Meta Description

```text
Learn about [Article Topic] in [Main City], including what to expect, common mistakes, local factors, and when to call [Brand Name].
```

### §12.6 Word count recomendado

```text
1,000–1,500 words
```

### §12.7 Estructura completa

```text
H1
Intro contextual
H2 Problem
H2 Local Context
H2 Options / Mistakes
H2 When to Call
H2 Local Examples
FAQs
CTA
Enlaces internos
```

### §12.8 Schema requerido

```text
Article
FAQPage
BreadcrumbList
Speakable
```

### §12.9 Enlaces internos requeridos

```text
Matching Main City Service Page
Main City GeoHub
Related GeoArticle
Contacto
```

### §12.10 Ejemplo rellenado con Cerrajeros Madrid 24h

```text
URL: /madrid/cuanto-cuesta-un-cerrajero-urgente/
H1: Precio de cerrajero urgente en Madrid
Enlaces: /cerrajero/madrid/cerrajero-urgente/, /madrid/, /madrid/que-hacer-si-no-puedes-entrar-casa/
```

### §12.11 Ejemplos incorrectos

```text
- Writing as a generic landing page
- No link to service page
- No local examples
- Pretending physical location in every coverage area
```

### §12.12 Regla final

```text
6. GeoArticle Page — Semantic Booster debe cumplir su función específica y no debe mezclarse con otro tipo de página.
```

### §12.13 Validación operativa

El GeoArticle no es una landing comercial. Debe cubrir un tema long-tail de servicio + Main City y enlazar a la página comercial correspondiente y al GeoHub.

# Bloque III — Reglas Cross-Cutting

> Reglas que aplican a TODAS las page types como filtro de QA. Siguen el patrón 3-subsecciones (Explicación / Cómo aplicamos / Decisión registrada).

## §13 Schema por tipo de página

### §13.1 Explicación

**Explicación**

Cada tipo de página tiene un schema esperado. La homepage usa Organization y WebSite; servicios usan Service; landings locales usan LocalBusiness; artículos usan Article y FAQPage.

**Patrón o fórmula**

```text
Page Type → Schema Required → QA
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-001 usa LocalBusiness + BreadcrumbList; GA-001 usa Article + FAQPage + BreadcrumbList + Speakable.
```

**Ejemplos incorrectos**

```text
- Usar Article schema en una landing
- Usar LocalBusiness con ubicación falsa
- No añadir BreadcrumbList
```

**Regla final**

```text
Cada tipo de página declara su Schema obligatorio; el implementador no decide en build time.
```

### §13.2 Cómo aplicamos la regla "Schema por tipo de página"

**Fuente:** GMB Crush.

**Método:** Aplicar la regla a TODAS las page types del Bloque II como filtro de QA antes de cerrar el spec de cada página.

### §13.3 Decisión registrada

**Tipo:** Validation flag — la regla cumple en todas las page types.

**Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque II.

## §14 Word count por intención

### §14.1 Explicación

**Explicación**

El contenido debe tener suficiente profundidad según el tipo de página. No se trata de inflar palabras, sino de cubrir intención, proceso, beneficios, FAQs, enlaces y contexto local.

**Patrón o fórmula**

```text
Page Type → word count objetivo → contenido completo
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Una Location-Based Service Page de Cerrajeros Madrid 24h tiene 800–1.000 palabras; un GeoArticle tiene 1.000–1.500.
```

**Ejemplos incorrectos**

```text
- Publicar landings de 250 palabras
- Crear artículos de 400 palabras sin profundidad
- Repetir bloques para llegar al word count
```

**Regla final**

```text
Word count se ajusta a la intención del page type, no a un número fijo arbitrario.
```

### §14.2 Cómo aplicamos la regla "Word count por intención"

**Fuente:** GMB Crush.

**Método:** Aplicar la regla a TODAS las page types del Bloque II como filtro de QA antes de cerrar el spec de cada página.

### §14.3 Decisión registrada

**Tipo:** Validation flag — la regla cumple en todas las page types.

**Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque II.

## §15 CTA adaptado al page type

### §15.1 Explicación

**Explicación**

Cada página debe tener un CTA, pero no todos los CTAs cumplen la misma función. Homepage y landings deben convertir; Service Overview puede ser más consultivo; GeoArticle debe enlazar contextual y suavemente al servicio.

**Patrón o fórmula**

```text
Page Type → CTA intent → enlace o acción
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
En /cerrajero/madrid/cerrajero-urgente/ el CTA es llamar ahora; en /madrid/cuanto-cuesta-un-cerrajero-urgente/ el CTA invita a consultar la página de Cerrajero urgente en Madrid.
```

**Ejemplos incorrectos**

```text
- Usar el mismo CTA genérico en todo el sitio
- No incluir CTA en artículos
- Hacer CTAs agresivos en contenido informativo
```

**Regla final**

```text
El CTA se adapta a la fase del funnel del page type — no es uniforme en todo el cluster.
```

### §15.2 Cómo aplicamos la regla "CTA adaptado al page type"

**Fuente:** GMB Crush.

**Método:** Aplicar la regla a TODAS las page types del Bloque II como filtro de QA antes de cerrar el spec de cada página.

### §15.3 Decisión registrada

**Tipo:** Validation flag — la regla cumple en todas las page types.

**Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque II.

## §16 No false location claims

### §16.1 Explicación

**Explicación**

Cualquier page type puede mencionar cobertura local, pero ninguno debe inventar oficina física. Esta regla protege la confianza local y evita contradicciones con GBP, NAP y schema.

**Patrón o fórmula**

```text
Local Coverage Area → servir clientes | no → oficina ficticia
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h puede decir que atiende Almagro, pero no que tiene oficina en Almagro si su ubicación física es Madrid.
```

**Ejemplos incorrectos**

```text
- Nuestra oficina en Almagro si no existe
- Mapa de una ubicación no real
- LocalBusiness address en zona de cobertura sin sede
```

**Regla final**

```text
Nunca afirmar ubicación física en zonas donde el negocio no opera realmente.
```

### §16.2 Cómo aplicamos la regla "No false location claims"

**Fuente:** GMB Crush.

**Método:** Aplicar la regla a TODAS las page types del Bloque II como filtro de QA antes de cerrar el spec de cada página.

### §16.3 Decisión registrada

**Tipo:** Validation flag — la regla cumple en todas las page types.

**Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque II.

# Bloque IV — Checklist Final

## §17 Checklist final del Paso 5

| Check | Pregunta | Estado |
|---|---|---|
| Homepage | ¿Funciona como Root Entity Anchor? | ✅ / ⬜ |
| Service Overview | ¿No tiene intención local principal? | ✅ / ⬜ |
| Location-Based Service | ¿Es un servicio + Main City? | ✅ / ⬜ |
| Additional Category | ¿Soporta una categoría adicional real y no duplicada? | ✅ / ⬜ |
| GeoHub | ¿Agrupa todos los elementos de la Main City? | ✅ / ⬜ |
| GeoArticle | ¿Es booster semántico y no landing? | ✅ / ⬜ |
| Schema | ¿Cada tipo de página tiene schema correcto? | ✅ / ⬜ |
| CTA | ¿Cada tipo de página tiene CTA definido? | ✅ / ⬜ |
| Enlaces internos | ¿Cada tipo tiene enlaces obligatorios? | ✅ / ⬜ |
| No mezcla | ¿No se mezclan servicios ni zonas sin aprobación? | ✅ / ⬜ |

# Bloque V — Decisiones consolidadas

## §18 Decisiones consolidadas del Paso 5

- Reglas de tipo de página definidas
- URLs por tipo de página confirmadas
- H1 y metadata por tipo de página
- Word count por tipo
- Schema por tipo
- Internal links base por tipo
- Errores frecuentes documentados

---

# Bloque VI — Fuentes Internas GMB Crush Usadas

# §19 Fuentes internas GMB Crush usadas

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
