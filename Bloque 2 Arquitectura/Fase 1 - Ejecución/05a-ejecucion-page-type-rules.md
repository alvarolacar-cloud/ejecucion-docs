Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo la estructura fija acordada en la conversación.
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# §1 Paso 5 — Page Type Rules

# Bloque I — Introducción

## §2 Objetivo del Paso 5

Este paso existe para resolver un problema concreto dentro del sistema GMB Crush: definir qué función cumple cada tipo de página antes de escribir contenido o enlazar páginas.
La web local no debe construirse desde la intuición, sino desde una secuencia operativa que conecta entidad, categoría GBP, servicios, ciudad principal, cobertura local, schema, contenido e interlinking.
El objetivo es que cada dato que se recoge o cada página que se crea tenga una función clara dentro del ecosistema local.
Cuando este paso se omite, la arquitectura empieza a crecer de forma desordenada.
Eso produce páginas duplicadas, URLs sin intención, contenidos genéricos, señales locales débiles y problemas de canibalización.
La metodología GMB Crush busca evitar precisamente ese escenario.
Por eso cada paso debe indicar qué se rellena, qué se genera, qué se revisa y qué errores previene.
En la versión simplificada del sistema usamos una Main City como base de arquitectura.
En esta versión web-first, el Google Business Profile no existe todavía: las categorías se tratan como Planned GBP Categories hasta que el Paso 14 cree, verifique y sincronice el GBP con la web.
Esto evita inventar una GBP URL, reseñas de Google o señales de perfil antes de que existan.
Las Local Coverage Areas no generan URLs por defecto.
Las Local Coverage Areas se usan para reforzar el contenido, los ejemplos locales, las FAQs y el schema areaServed.
Solo las Approved Expansion Areas pueden convertirse en URLs propias cuando exista una justificación clara.
Esta separación evita confundir cobertura real con arquitectura obligatoria.
También evita que un negocio local pequeño acabe con cientos de páginas antes de tener una base sólida.
El criterio principal es crear primero las páginas que soportan la entidad, la categoría GBP y la intención comercial.
Después se añaden artículos, enlaces internos, QA y optimización.
Este paso debe ejecutarse antes de avanzar al siguiente.
Si se salta o se rellena mal, los pasos posteriores arrastran errores.
La revisión final debe comprobar que cada elemento tiene una función SEO, una función local y una función de conversión.
Error que previene: confundir Service Overview con Location-Based Service.
Error que previene: convertir GeoArticles en landing pages.
Error que previene: crear Additional Category Pages duplicadas.
Error que previene: usar el mismo schema en todos los tipos de página.
Error que previene: escribir páginas sin word count, CTA, FAQs o estructura AUDIO.

## §3 Lo que la IA tiene que rellenar/obtener

```text
Business Name:

Website Root Domain:

Planned Primary GBP Category:

Primary Category Slug:

Main City:

Main City Slug:

Primary Service:

Servicios principales:
1.
2.
3.
4.
5.

Planned Additional GBP Categories that need pages:
1.
2.
3.

Local Coverage Areas:
1.
2.
3.
4.
5.

Approved Expansion Areas:
Default: None.

Phone:

Email:

GBP URL:

NAP:
- Name:
- Address:
- Phone:

Physical Location City:

Trust Signals:
- Years in business:
- Reviews:
- Certifications:
- Awards:
- Guarantees:
- Urgencias / servicio en el mismo día / servicio móvil:

Preferred CTA:
Option A: Llamar ahora
Option B: Reservar online
Option C: Solicitar presupuesto
Option D: Contactar

Brand tone:
Option A: Professional
Option B: Friendly
Option C: Premium
Option D: Urgente
Option E: Local and conversational
```

## §4 Ejemplo rellenado

```text
Business Name:
Cerrajeros Madrid 24h

Website URL:
https://www.cerrajerosmadrid24h.com

Canonical Domain:
https://www.cerrajerosmadrid24h.com

Full NAP:
- Name: Cerrajeros Madrid 24h
- Street Address: Calle Rafael Calvo 12, Barrio Almagro, Distrito Chamberí
- City: Madrid
- State / Province: Comunidad de Madrid
- ZIP / Postal Code: 28010
- Country: España
- Phone: +34 600 000 000

Planned Primary GBP Category:
Cerrajero

Planned Additional GBP Categories:
1. Servicio de cerrajería de urgencia
2. Servicio de duplicado de llaves

Main City:
Madrid

Physical Location City:
Madrid

Servicios principales:
1. Cerrajero urgente
2. Apertura de puertas
3. Cambio de cerraduras
4. Cambio de bombines
5. Instalación de cerraduras de seguridad

Direct Local Coverage Areas:
1. Almagro
2. Chamberí

Candidate Local Coverage Areas:
1. Salamanca
2. Retiro
3. Centro
4. Tetuán
5. Chamartín
6. Arganzuela
7. Moncloa
8. Prosperidad

Should Local Coverage Areas generate pages?
No, not in the base build.

Approved Expansion Areas:
None in Phase 1.

Additional Categories already covered by core services:
1. Servicio de cerrajería de urgencia

Additional Categories that need separate pages:
1. Servicio de duplicado de llaves

GeoArticles per Service:
3

Preferred CTA:
Llamar ahora

Trust Signals:
- 10+ años de experiencia
- reseñas iniciales pendientes de recopilar tras crear el GBP
- Técnicos cerrajeros cualificados
- Servicio móvil en el mismo día
- Garantía de trabajo

GBP URL:
N/A — GBP not created yet

Phone:
+34 600 000 000

Email:
info@cerrajerosmadrid24h.com

Brand tone:
Friendly, professional, local and urgente when needed
```

# Bloque II — Ejecución por la IA · Page Types

> Cada page type tiene 12 subsections que cubren la spec completa (Función, Patrón URL, H1, Meta Title, Meta Description, Word count, Estructura completa, Schema, Enlaces internos, Ejemplo, Ejemplos incorrectos, Regla final). Plus §X.13 Validación operativa que absorbe la regla operativa pareja del original.

## §5 Homepage — Root Entity Anchor

### §5.1 Función

La homepage es la raíz de entidad del negocio. Debe establecer quién es la marca, qué categoría GBP soporta, cuál es la Main City, qué servicios ofrece, qué cobertura local tiene y cómo contactar. No es una página decorativa ni un simple escaparate.

### §5.2 Patrón URL

```text
/
```

### §5.3 H1

```text
[Brand Name] – [Primary Service] de confianza en [Main City]
```

### §5.4 Meta Title

```text
[Primary Service] en [Main City] | [Brand Name]
```

### §5.5 Meta Description

```text
¿Necesitas [Primary Service] en [Main City]? [Brand Name] ofrece servicio local, soporte experto y respuesta rápida. Llama hoy.
```

### §5.6 Word count recomendado

```text
900–1,300 words
```

### §5.7 Estructura completa

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

### §5.8 Schema requerido

```text
Organization
WebSite
LocalBusiness if physical presence exists in Main City
FAQPage
Speakable
```

### §5.9 Enlaces internos requeridos

```text
Service Overview Pages
Main City GeoHub
Páginas de categoría adicional en la Main City
Página de contacto
```

### §5.10 Ejemplo rellenado con Cerrajeros Madrid 24h

```text
URL: /
H1: Cerrajeros Madrid 24h – Servicios de cerrajería de confianza en Madrid
Meta Title: Cerrajero en Madrid | Cerrajeros Madrid 24h
Servicios principales: Cerrajero urgente, apertura de puertas, cambio de cerraduras, cambio de bombines e instalación de cerraduras de seguridad
Vista previa de cobertura local: Almagro, Chamberí, Salamanca, Retiro
Schema: Organization, WebSite, LocalBusiness, FAQPage, Speakable
```

### §5.11 Ejemplos incorrectos

```text
- Homepage with no services
- Homepage targeting five cities equally
- Homepage without NAP
- Homepage without links to service pages
```

### §5.12 Regla final

```text
1. Homepage — Root Entity Anchor debe cumplir su función específica y no debe mezclarse con otro tipo de página.
```

### §5.13 Validación operativa

La homepage no es una página decorativa. Es el contenedor principal de la entidad local y debe establecer marca, categoría GBP, servicio principal, Main City, NAP, señales de confianza y enlaces a las páginas clave.

## §6 Service Overview Page — Topical Authority Pillar

### §6.1 Función

Esta página educa sobre un servicio sin geolocalización. Es el pilar temático que soporta la versión local del servicio en la Main City y cualquier futura expansión aprobada.

### §6.2 Patrón URL

```text
/[primary-category-slug]/[service-slug]/
```

### §6.3 H1

```text
Servicios profesionales de [Service] por [Brand Name]
```

### §6.4 Meta Title

```text
[Service] por [Brand Name] | Expertos en [Primary Category]
```

### §6.5 Meta Description

```text
¿Necesitas [Service] de confianza? [Brand Name] ofrece soluciones expertas, rápidas y cuidadosas. Consulta el proceso completo y sus beneficios.
```

### §6.6 Word count recomendado

```text
850–1,000 words
```

### §6.7 Estructura completa

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

### §6.8 Schema requerido

```text
Service
WebPage
BreadcrumbList
Speakable
```

### §6.9 Enlaces internos requeridos

```text
Homepage
Related Service Overview Pages
Main City Location-Based Service Page
Relevant GeoArticle
```

### §6.10 Ejemplo rellenado con Cerrajeros Madrid 24h

```text
URL: /cerrajero/cerrajero-urgente/
H1: Servicios profesionales de cerrajería urgente por Cerrajeros Madrid 24h
Meta Title: Cerrajero urgente por Cerrajeros Madrid 24h | Expertos en cerrajería
Enlaces internos: /, /cerrajero/apertura-puertas/, /cerrajero/madrid/cerrajero-urgente/, /madrid/cuanto-cuesta-un-cerrajero-urgente/
```

### §6.11 Ejemplos incorrectos

```text
- Mentioning Madrid as the primary target
- Using /cerrajero/madrid/cerrajero-urgente/ as service overview
- No links to local version
- Thin content under 400 words
```

### §6.12 Regla final

```text
2. Service Overview Page — Topical Authority Pillar debe cumplir su función específica y no debe mezclarse con otro tipo de página.
```

### §6.13 Validación operativa

La Service Overview Page crea autoridad temática sobre un servicio sin enfocarse en ciudad. Debe explicar el servicio, proceso, problemas resueltos, FAQs y enlaces a su versión Main City.

## §7 Location-Based Service Page — Main City Converter

### §7.1 Función

Esta página convierte búsquedas locales de alta intención para una combinación exacta: servicio + Main City. Es una de las páginas más importantes para soporte GBP y Local Pack.

### §7.2 Patrón URL

```text
/[primary-category-slug]/[main-city-slug]/[service-slug]/
```

### §7.3 H1

```text
[Brand Name] – [Service] en [Main City]
```

### §7.4 Meta Title

```text
Top [Service] en [Main City] | [Brand Name]
```

### §7.5 Meta Description

```text
¿Necesitas [Service] en [Main City]? [Brand Name] ayuda con [problema], [problema] y [problema]. Llama para recibir soporte local.
```

### §7.6 Word count recomendado

```text
800–1,000 words
```

### §7.7 Estructura completa

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

### §7.8 Schema requerido

```text
LocalBusiness
BreadcrumbList
FAQPage optional
Speakable optional
```

### §7.9 Enlaces internos requeridos

```text
Parent Service Overview
Main City GeoHub
Other services in Main City
Related GeoArticles
Contacto
```

### §7.10 Ejemplo rellenado con Cerrajeros Madrid 24h

```text
URL: /cerrajero/madrid/cerrajero-urgente/
H1: Cerrajeros Madrid 24h – Cerrajero urgente en Madrid
Local Coverage Areas: Almagro, Chamberí, Salamanca, Retiro mencionadas de forma natural
Enlaces: /cerrajero/cerrajero-urgente/, /madrid/, /cerrajero/madrid/apertura-puertas/, /madrid/cuanto-cuesta-un-cerrajero-urgente/
```

### §7.11 Ejemplos incorrectos

```text
- Mezclar Madrid and Almagro as equal targets
- Crear una página por cada zona de cobertura sin aprobación
- Afirmar una oficina en Salamanca
- Combinar apertura de puertas y cambio de cerraduras en una sola landing local
```

### §7.12 Regla final

```text
3. Location-Based Service Page — Main City Converter debe cumplir su función específica y no debe mezclarse con otro tipo de página.
```

### §7.13 Validación operativa

La Location-Based Service Page es la página comercial más importante para una combinación servicio + Main City. Debe tener intención local, CTA, reviews, contenido GEO y enlaces a padre, GeoHub y artículos.

## §8 Additional Category Page — GBP Additional Category Support

### §8.1 Función

Esta página soporta una categoría adicional real del GBP que no está cubierta por un servicio core. Refuerza la profundidad de entidad y la relevancia semántica.

### §8.2 Patrón URL

```text
/[primary-category-slug]/[main-city-slug]/[additional-category-slug]/
```

### §8.3 H1

```text
[Brand Name] – Expert [Service] en [Main City]
```

### §8.4 Meta Title

```text
[Service] en [Main City] | [Brand Name]
```

### §8.5 Meta Description

```text
¿Necesitas [Service] en [Main City]? [Brand Name] ofrece ayuda fiable para [problema], [caso de uso] y [caso de uso]. Llama hoy.
```

### §8.6 Word count recomendado

```text
800–1,000 words
```

### §8.7 Estructura completa

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

### §8.8 Schema requerido

```text
Service with areaServed
BreadcrumbList
FAQPage optional
Speakable optional
```

### §8.9 Enlaces internos requeridos

```text
Main City GeoHub
Related Location-Based Service Pages
Related GeoArticles
Contacto
```

### §8.10 Ejemplo rellenado con Cerrajeros Madrid 24h

```text
URL: /cerrajero/madrid/duplicado-llaves/
H1: Cerrajeros Madrid 24h – Duplicado de llaves experto en Madrid
Meta Title: Duplicado de llaves en Madrid | Cerrajeros Madrid 24h
Enlaces: /madrid/, /cerrajero/madrid/cambio-cerraduras/, /cerrajero/madrid/instalacion-cerraduras-seguridad/
```

### §8.11 Ejemplos incorrectos

```text
- Crear /cerrajero/madrid/cerrajero-urgente/ when urgente is already covered
- No local context
- No links to GeoHub
- Category page with no relation to GBP
```

### §8.12 Regla final

```text
4. Additional Category Page — GBP Additional Category Support debe cumplir su función específica y no debe mezclarse con otro tipo de página.
```

### §8.13 Validación operativa

Las Additional Category Pages existen para soportar categorías adicionales reales del GBP que no estén ya cubiertas por servicios core. Su formato es local porque refuerzan relevancia de categoría en la Main City.

## §9 GeoHub Page — Main City Silo Container

### §9.1 Función

El GeoHub agrupa todas las señales de la Main City. Es el índice local del sitio: servicios, categorías adicionales, artículos, cobertura local, confianza y contacto.

### §9.2 Patrón URL

```text
/[main-city-slug]/ OR /[primary-category-slug]/[main-city-slug]/
```

### §9.3 H1

```text
[Brand Name] – [Industry] Services in [Main City]
```

### §9.4 Meta Title

```text
[Industry] Services in [Main City] | [Brand Name]
```

### §9.5 Meta Description

```text
Explore trusted [Industry] services in [Main City] from [Brand Name]. View local services, helpful resources, coverage areas, and ways to contact our team.
```

### §9.6 Word count recomendado

```text
700–1,100 words
```

### §9.7 Estructura completa

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

### §9.8 Schema requerido

```text
CollectionPage
BreadcrumbList
LocalBusiness optional if physical presence exists
```

### §9.9 Enlaces internos requeridos

```text
Homepage
All Páginas de servicio en la Main City
Páginas de categoría adicional en la Main City
GeoArticles de la Main City
Página de contacto
```

### §9.10 Ejemplo rellenado con Cerrajeros Madrid 24h

```text
URL: /madrid/
H1: Cerrajeros Madrid 24h – Servicios de cerrajería en Madrid
Menú de servicios: urgente, apertura de puertas, cambio de cerraduras, cambio de bombines, instalación de cerraduras de seguridad
Sección de cobertura: Almagro, Chamberí, Salamanca, Retiro
Enlaces: /cerrajero/madrid/cerrajero-urgente/, /cerrajero/madrid/duplicado-llaves/, /madrid/cuanto-cuesta-un-cerrajero-urgente/
```

### §9.11 Ejemplos incorrectos

```text
- GeoHub with only generic city text
- No links to service pages
- Treating Almagro as a child page without approval
- No CTA
```

### §9.12 Regla final

```text
5. GeoHub Page — Main City Silo Container debe cumplir su función específica y no debe mezclarse con otro tipo de página.
```

### §9.13 Validación operativa

El GeoHub organiza todas las señales de la Main City: servicios, categorías adicionales, GeoArticles, cobertura local, confianza y contacto. No es una landing de un servicio concreto.

## §10 GeoArticle Page — Semantic Booster

### §10.1 Función

El GeoArticle no es una landing comercial. Es un booster semántico para un servicio, una Main City y una intención long-tail. Su misión es apoyar la página comercial y el GeoHub.

### §10.2 Patrón URL

```text
/[main-city-slug]/[article-topic-slug]/
```

### §10.3 H1

```text
[Article Topic] in [Main City]
```

### §10.4 Meta Title

```text
[Article Topic] in [Main City] | [Brand Name]
```

### §10.5 Meta Description

```text
Learn about [Article Topic] in [Main City], including what to expect, common mistakes, local factors, and when to call [Brand Name].
```

### §10.6 Word count recomendado

```text
1,000–1,500 words
```

### §10.7 Estructura completa

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

### §10.8 Schema requerido

```text
Article
FAQPage
BreadcrumbList
Speakable
```

### §10.9 Enlaces internos requeridos

```text
Matching Main City Service Page
Main City GeoHub
Related GeoArticle
Contacto
```

### §10.10 Ejemplo rellenado con Cerrajeros Madrid 24h

```text
URL: /madrid/cuanto-cuesta-un-cerrajero-urgente/
H1: Precio de cerrajero urgente en Madrid
Enlaces: /cerrajero/madrid/cerrajero-urgente/, /madrid/, /madrid/que-hacer-si-no-puedes-entrar-casa/
```

### §10.11 Ejemplos incorrectos

```text
- Writing as a generic landing page
- No link to service page
- No local examples
- Pretending physical location in every coverage area
```

### §10.12 Regla final

```text
6. GeoArticle Page — Semantic Booster debe cumplir su función específica y no debe mezclarse con otro tipo de página.
```

### §10.13 Validación operativa

El GeoArticle no es una landing comercial. Debe cubrir un tema long-tail de servicio + Main City y enlazar a la página comercial correspondiente y al GeoHub.

# Bloque III — Reglas Cross-Cutting

> Reglas que aplican a TODAS las page types como filtro de QA. Siguen el patrón 3-subsecciones (Explicación / Cómo aplicamos / Output).

## §11 Schema por tipo de página

### §11.1 Explicación

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

### §11.2 Cómo aplicamos la regla "Schema por tipo de página"

**Fuente:** GMB Crush.

**Método:** Aplicar la regla a TODAS las page types del Bloque II como filtro de QA antes de cerrar el spec de cada página.

### §11.3 Output del paso

**Tipo:** Validation flag — la regla cumple en todas las page types.

**Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque II.

## §12 Word count por intención

### §12.1 Explicación

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

### §12.2 Cómo aplicamos la regla "Word count por intención"

**Fuente:** GMB Crush.

**Método:** Aplicar la regla a TODAS las page types del Bloque II como filtro de QA antes de cerrar el spec de cada página.

### §12.3 Output del paso

**Tipo:** Validation flag — la regla cumple en todas las page types.

**Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque II.

## §13 CTA adaptado al page type

### §13.1 Explicación

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

### §13.2 Cómo aplicamos la regla "CTA adaptado al page type"

**Fuente:** GMB Crush.

**Método:** Aplicar la regla a TODAS las page types del Bloque II como filtro de QA antes de cerrar el spec de cada página.

### §13.3 Output del paso

**Tipo:** Validation flag — la regla cumple en todas las page types.

**Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque II.

## §14 No false location claims

### §14.1 Explicación

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

### §14.2 Cómo aplicamos la regla "No false location claims"

**Fuente:** GMB Crush.

**Método:** Aplicar la regla a TODAS las page types del Bloque II como filtro de QA antes de cerrar el spec de cada página.

### §14.3 Output del paso

**Tipo:** Validation flag — la regla cumple en todas las page types.

**Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque II.

# Bloque IV — Checklist Final

## §15 Checklist final del Paso 5

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

# Bloque V — Outputs

## §16 Outputs del Paso 5

- Reglas de tipo de página definidas
- URLs por tipo de página confirmadas
- H1 y metadata por tipo de página
- Word count por tipo
- Schema por tipo
- Internal links base por tipo
- Errores frecuentes documentados

---

# Bloque VI — Fuentes Internas GMB Crush Usadas

# §17 Fuentes internas GMB Crush usadas

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
