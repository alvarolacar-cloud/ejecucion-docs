Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo la estructura fija acordada en la conversación.
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# §1 Paso 6 — Estructura de Contenido + Áreas de Cobertura Local

# Bloque I — Introducción

## §2 Objetivo del Paso 6

Este paso existe para resolver un problema concreto dentro del sistema GMB Crush: definir cómo se escribe y organiza el contenido real de cada tipo de página, y cómo se usan las áreas de cobertura local sin convertirlas automáticamente en URLs.
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
Esta separación evita confundir señales GEO de contenido con arquitectura obligatoria.
También evita que un negocio local pequeño acabe con cientos de páginas antes de tener una base sólida.
El criterio principal es crear primero las páginas que soportan la entidad, la categoría GBP y la intención comercial.
Después se añaden artículos, enlaces internos, QA y optimización.
Este paso debe ejecutarse antes de avanzar al siguiente.
Si se salta o se rellena mal, los pasos posteriores arrastran errores.
La revisión final debe comprobar que cada elemento tiene una función SEO, una función local y una función de conversión.
Error que previene: crear solo formularios sin cuerpo operativo.
Error que previene: mencionar zonas locales de forma artificial.
Error que previene: crear páginas para cada área de cobertura sin aprobación.
Error que previene: usar Local Coverage Areas como si fueran Main City.
Error que previene: olvidar dónde van FAQs, CTAs, reviews, Local Coverage Areas y enlaces internos.

## §3 Lo que la IA tiene que rellenar/obtener

```text
Business Name:

Planned Primary GBP Category:

Primary Category Slug:

Main City:

Main City Slug:

Physical Location City:

Servicios principales:
1.
2.
3.
4.
5.

Direct Local Coverage Areas:
Zonas con proximidad directa al NAP y coherencia GEO confirmada.
1.
2.
3.

Candidate Local Coverage Areas:
Zonas candidatas pendientes de validar con el test de coherencia GEO del Paso 1.
1.
2.
3.
4.
5.

Should Local Coverage Areas generate pages?
Default: No.

Approved Expansion Areas:
Optional.
1.
2.
3.

Service Page URL to structure:

Page Type:
Homepage / Service Overview / Location-Based Service / Additional Category / GeoHub / GeoArticle

Target Service:

Target Additional Category:

Matching Parent Page:

Matching GeoHub:

Related GeoArticles:

Preferred CTA:

Trust Signals:

Can the page mention physical office in this area?
Yes / No
```

## §4 Ejemplo rellenado

```text
Business Name:
Cerrajeros Madrid 24h

Planned Primary GBP Category:
Cerrajero

Primary Category Slug:
cerrajero

Main City:
Madrid

Main City Slug:
madrid

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

Service Page URL to structure:
/cerrajero/madrid/cerrajero-urgente/

Page Type:
Location-Based Service

Target Service:
Cerrajero urgente

Target Additional Category:
Servicio de cerrajería de urgencia is already covered by this service.

Matching Parent Page:
/cerrajero/cerrajero-urgente/

Matching GeoHub:
/madrid/

Related GeoArticles:
1. /madrid/cuanto-cuesta-un-cerrajero-urgente/
2. /madrid/que-hacer-si-no-puedes-entrar-casa/
3. /madrid/cuanto-tarda-un-cerrajero/

Preferred CTA:
Llamar ahora

Trust Signals:
- 10+ años de experiencia
- reseñas iniciales pendientes de recopilar tras crear el GBP
- Técnicos cerrajeros cualificados
- Servicio móvil en el mismo día

Can the page mention physical office in this area?
Solo para Madrid, no para Local Coverage Areas salvo que sea cierto.
```

# Bloque II — Ejecución por la IA

> Bloque II tiene 3 secciones: **5 principios** (§5-§9) que rigen toda la arquitectura, **6 content architectures** (§10-§15) por page type con sus 6 subsections preservadas + Validación operativa, y **3 secciones de output** (§16-§18) con tablas y ejemplos.

## §5 Principio 1 — Main City crea arquitectura

### §5.1 Explicación

**Explicación**

La Main City es la ciudad principal que genera URLs base. Todo el sistema base se organiza alrededor de esa ciudad.

**Patrón o fórmula**

```text
Main City → /city/ + /category/city/service/ + /city/article-topic/
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Madrid genera /madrid/ y /cerrajero/madrid/cerrajero-urgente/
```

**Ejemplos incorrectos**

```text
- Almagro genera URL sin aprobación
- Salamanca se usa como Main City en una página de Madrid
- Cambiar Main City por cada bloque
```

**Regla final**

```text
La arquitectura del cluster se construye sobre una sola Main City.
```

### §5.2 Cómo aplicamos el Principio 1 (Main City crea arquitectura)

**Fuente:** GMB Crush.

**Método:** Aplicar el principio como filtro de QA al revisar la arquitectura del cluster antes de avanzar al Paso 7.

### §5.3 Output del paso

**Tipo:** Validation flag — el principio se respeta en toda la arquitectura del Bloque II.

**Ejemplo (Cerrajeros Madrid 24h):** Validado.

## §6 Principio 2 — Local Coverage Areas enriquecen contenido

### §6.1 Explicación

**Explicación**

Las Local Coverage Areas son zonas seleccionadas por proximidad al NAP, coherencia GEO y lógica GMB Crush. Se usan para contexto, FAQs, ejemplos, señales locales y schema areaServed.

**Patrón o fórmula**

```text
Local Coverage Areas → content, FAQs, examples, areaServed
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Almagro, Chamberí, Salamanca y Retiro se mencionan en secciones de cobertura
```

**Ejemplos incorrectos**

```text
- Crear páginas por cada zona
- Listar zonas donde no se atiende
- Usarlas como H1 principal
```

**Regla final**

```text
Las LCAs viven en contenido y schema, nunca como segmentos de URL.
```

### §6.2 Cómo aplicamos el Principio 2 (LCAs enriquecen contenido)

**Fuente:** GMB Crush.

**Método:** Aplicar el principio como filtro de QA al revisar la arquitectura del cluster antes de avanzar al Paso 7.

### §6.3 Output del paso

**Tipo:** Validation flag — el principio se respeta en toda la arquitectura del Bloque II.

**Ejemplo (Cerrajeros Madrid 24h):** Validado.

## §7 Principio 3 — Approved Expansion Areas crean URLs solo si se aprueban

### §7.1 Explicación

**Explicación**

Cuando una zona tiene demanda, competencia o valor comercial, puede pasar a expansión.

**Patrón o fórmula**

```text
Local Coverage Area → Approved Expansion Area → URLs
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Almagro podría generar /almagro/ en una fase futura si se aprueba
```

**Ejemplos incorrectos**

```text
- Aprobar todas las zonas
- Crear expansión antes de terminar Madrid
- Crear expansión sin contenido único
```

**Regla final**

```text
Approved Expansion Areas se aprueban por umbral de demanda+competencia+contenido único, no por defecto.
```

**Validación operativa**

Una Local Coverage Area solo se convierte en Approved Expansion Area si hay demanda, valor comercial, oportunidad competitiva y contenido único. Esta regla protege el sistema de expansión prematura.

### §7.2 Cómo aplicamos el Principio 3 (Approved Expansion crean URLs solo si se aprueban)

**Fuente:** GMB Crush.

**Método:** Aplicar el principio como filtro de QA al revisar la arquitectura del cluster antes de avanzar al Paso 7.

### §7.3 Output del paso

**Tipo:** Validation flag — el principio se respeta en toda la arquitectura del Bloque II.

**Ejemplo (Cerrajeros Madrid 24h):** Validado.

## §8 Principio 4 — Mencionar una zona no es crear una página

### §8.1 Explicación

**Explicación**

Este principio evita confundir señales GEO de contenido con arquitectura de URLs.

**Patrón o fórmula**

```text
Mention ≠ URL
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Se menciona Almagro dentro de /cerrajero/madrid/cerrajero-urgente/ sin enlazar a /almagro/
```

**Ejemplos incorrectos**

```text
- Crear enlaces a URLs inexistentes
- Usar la zona en breadcrumbs
- Crear páginas por presión de llaveword
```

**Regla final**

```text
Mencionar una zona como cobertura no implica crear una URL para esa zona.
```

**Validación operativa**

Mencionar una zona en el contenido no implica crear una URL. Esta separación es clave para que el sistema base se mantenga enfocado y no genere thin content.

### §8.2 Cómo aplicamos el Principio 4 (Mencionar zona no es crear página)

**Fuente:** GMB Crush.

**Método:** Aplicar el principio como filtro de QA al revisar la arquitectura del cluster antes de avanzar al Paso 7.

### §8.3 Output del paso

**Tipo:** Validation flag — el principio se respeta en toda la arquitectura del Bloque II.

**Ejemplo (Cerrajeros Madrid 24h):** Validado.

## §9 Principio 5 — No falsa ubicación

### §9.1 Explicación

**Explicación**

Si la oficina física está en Madrid, no se afirma oficina en Almagro, Salamanca o Retiro.

**Patrón o fórmula**

```text
Service coverage ≠ physical presence
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Atendemos clientes en Salamanca
```

**Ejemplos incorrectos**

```text
- Nuestra oficina en Salamanca
- Visita nuestra tienda en Almagro
- Schema address en Chamberí
```

**Regla final**

```text
Nunca afirmar oficina física en zonas donde el negocio no opera realmente.
```

### §9.2 Cómo aplicamos el Principio 5 (No falsa ubicación)

**Fuente:** GMB Crush.

**Método:** Aplicar el principio como filtro de QA al revisar la arquitectura del cluster antes de avanzar al Paso 7.

### §9.3 Output del paso

**Tipo:** Validation flag — el principio se respeta en toda la arquitectura del Bloque II.

**Ejemplo (Cerrajeros Madrid 24h):** Validado.

## §10 1. Homepage Content Architecture

### §10.1 Explicación

Este bloque define la arquitectura interna de contenido para este tipo de página. No se limita a H1 y meta title. Incluye intro, H2s, bloques de apoyo, áreas de cobertura local, FAQs, CTA, enlaces internos y schema.

### §10.2 Estructura completa

```text
H1
Intro
Quick Answer
Servicios principales
Vista previa de cobertura local
Bloques de confianza
Sección FAQ
Bloque NAP
CTA
Enlaces internos
Schema
```

### §10.3 Uso de Local Coverage Areas

La homepage puede mencionar 3–5 Local Coverage Areas de forma ligera, normalmente en un bloque de service area preview. No debe convertirse en una lista masiva de zonas ni usar las áreas de cobertura como sustituto de la Main City.

### §10.4 Ejemplo correcto con Cerrajeros Madrid 24h

```text
H1: Cerrajeros Madrid 24h – Servicios de cerrajería de confianza en Madrid
Vista previa de cobertura local: Atendemos clientes en Madrid y zonas de cobertura como Almagro, Chamberí, Salamanca y Retiro según disponibilidad.
Enlaces a servicios principales: /cerrajero/cerrajero-urgente/, /cerrajero/apertura-puertas/, /cerrajero/cambio-bombines/
Enlace al GeoHub: /madrid/
```

### §10.5 Ejemplos incorrectos

```text
- Homepage con 30 zonas listadas sin contexto
- Homepage orientada a Almagro, Salamanca y Retiro al mismo nivel que Madrid
- Homepage sin Servicios principales
- Homepage sin NAP
```

### §10.6 Regla final

```text
La homepage debe reforzar marca, categoría, Main City, servicios y cobertura real sin crear URLs innecesarias.
```

### §10.7 Validación operativa

La homepage puede mencionar Local Coverage Areas, pero no debe convertirse en una lista interminable de zonas. Su prioridad sigue siendo entidad, categoría GBP, Main City, servicios, NAP y confianza.

## §11 2. Service Overview Content Architecture

### §11.1 Explicación

Este bloque define la arquitectura interna de contenido para este tipo de página. No se limita a H1 y meta title. Incluye intro, H2s, bloques de apoyo, áreas de cobertura local, FAQs, CTA, enlaces internos y schema.

### §11.2 Estructura completa

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
Schema
```

### §11.3 Uso de Local Coverage Areas

No se usan Local Coverage Areas. Esta página no debe mencionar Madrid, Almagro, Salamanca ni ninguna zona como target principal. Su función es ser pilar temático del servicio.

### §11.4 Ejemplo correcto con Cerrajeros Madrid 24h

```text
URL: /cerrajero/cerrajero-urgente/
Intro: Cerrajeros Madrid 24h ofrece servicios profesionales de cerrajería urgente: aperturas urgentes, llaves rotas y problemas de acceso.
Sin segmentación local.
Internal link to local version: /cerrajero/madrid/cerrajero-urgente/
```

### §11.5 Ejemplos incorrectos

```text
- Mencionar Almagro en el H1
- Crear un bloque de cobertura local en service overview
- Usar /madrid/ como target principal
- No enlazar a la versión local
```

### §11.6 Regla final

```text
Service Overview = servicio sin localización.
```

### §11.7 Validación operativa

Las páginas de servicio general deben evitar Main City y Local Coverage Areas como objetivo principal. Su trabajo es explicar el servicio de forma no geolocalizada y actuar como pilar temático.

## §12 3. Location-Based Service Content Architecture

### §12.1 Explicación

Este bloque define la arquitectura interna de contenido para este tipo de página. No se limita a H1 y meta title. Incluye intro, H2s, bloques de apoyo, áreas de cobertura local, FAQs, CTA, enlaces internos y schema.

### §12.2 Estructura completa

```text
H1
Intro local 100–150 words
Quick Local Answer
H2 Authority
H2 Uniqueness
H2 Depth
H2 Local Pain Points
H2 Local Coverage Areas Served
H2 Related Services in [Main City]
FAQs
CTA
Enlaces internos
Schema
```

### §12.3 Uso de Local Coverage Areas

Sí se usan Local Coverage Areas. Deben aparecer de forma natural en la intro, en una sección de cobertura, en ejemplos locales y en FAQs. La página sigue siendo de Main City, no de cada área mencionada.

### §12.4 Ejemplo correcto con Cerrajeros Madrid 24h

```text
URL: /cerrajero/madrid/cerrajero-urgente/
H2: Ayuda de cerrajero urgente en Madrid y áreas de cobertura local
Texto: Cerrajeros Madrid 24h ayuda a clientes en Madrid con aperturas urgentes, llaves rotas y problemas de acceso. También atendemos zonas de cobertura como Almagro, Chamberí, Salamanca y Retiro cuando el servicio está disponible.
FAQ: ¿Ofrecéis cerrajero urgente en Almagro y Chamberí?
Respuesta: Sí, atendemos esas zonas según disponibilidad, mientras esta página sigue enfocada en el servicio de cerrajero urgente en Madrid.
```

### §12.5 Ejemplos incorrectos

```text
- H1: Cerrajero urgente en Almagro, Madrid y Salamanca
- Crear un párrafo por cada zona con texto duplicado
- Claim office in Retiro
- Link to /almagro/ when that URL does not exist
```

### §12.6 Regla final

```text
Una Location-Based Service Page menciona cobertura local sin dejar de ser service + Main City.
```

### §12.7 Validación operativa

La página servicio+Main City debe abrir con una intro localizada de 100–150 palabras. Aquí se puede mencionar 2–4 Local Coverage Areas de forma natural si refuerzan el contexto, pero sin desplazar la Main City.

Las páginas locales pueden incluir una sección específica de cobertura. Esta sección permite mencionar barrios, distritos o municipios seleccionados como señales GEO sin crear páginas propias ni URLs artificiales.

## §13 4. Additional Category Content Architecture

### §13.1 Explicación

Este bloque define la arquitectura interna de contenido para este tipo de página. No se limita a H1 y meta title. Incluye intro, H2s, bloques de apoyo, áreas de cobertura local, FAQs, CTA, enlaces internos y schema.

### §13.2 Estructura completa

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
Schema
```

### §13.3 Uso de Local Coverage Areas

Las Local Coverage Areas se usan para explicar casos de uso locales relacionados con la categoría adicional. No deben crear páginas propias si no están aprobadas.

### §13.4 Ejemplo correcto con Cerrajeros Madrid 24h

```text
URL: /cerrajero/madrid/duplicado-llaves/
H2: Duplicado de llaves en zonas de cobertura de Madrid
Texto: Clientes en Madrid y zonas como Almagro, Chamberí y Salamanca pueden necesitar llaves de repuesto para familiares, empleados, inquilinos o accesos urgentes.
Enlaces: /madrid/, /cerrajero/madrid/cambio-cerraduras/, /cerrajero/madrid/instalacion-cerraduras-seguridad/
```

### §13.5 Ejemplos incorrectos

```text
- Crear /cerrajero/almagro/duplicado-llaves/ sin aprobación
- No conectar con GeoHub
- Tratar duplicado de llaves como servicio core si no está definido
- Copiar contenido de la página de cambio de bombines
```

### §13.6 Regla final

```text
La categoría adicional se contextualiza localmente, pero no se multiplica por zonas no aprobadas.
```

### §13.7 Validación operativa

Las páginas de categorías adicionales deben usar Local Coverage Areas solo cuando ayuden a explicar escenarios reales del servicio. El foco sigue siendo servicio adicional + Main City.

## §14 5. GeoHub Content Architecture

### §14.1 Explicación

Este bloque define la arquitectura interna de contenido para este tipo de página. No se limita a H1 y meta title. Incluye intro, H2s, bloques de apoyo, áreas de cobertura local, FAQs, CTA, enlaces internos y schema.

### §14.2 Estructura completa

```text
H1
City intro
Menú de servicios
Additional Category Menu
Local Coverage Areas Section
GeoArticle Resources
Trust Signals
CTA
Enlaces internos
Schema
```

### §14.3 Uso de Local Coverage Areas

El GeoHub es el lugar más natural para una sección explícita de Local Coverage Areas. Aquí se puede explicar la cobertura de la empresa sin crear URLs por cada zona.

### §14.4 Ejemplo correcto con Cerrajeros Madrid 24h

```text
URL: /madrid/
H2: Zonas de cobertura de cerrajería en Madrid
Texto: Cerrajeros Madrid 24h ofrece servicios de cerrajería en Madrid con cobertura en zonas como Almagro, Chamberí, Salamanca y Retiro. Estas áreas son señales GEO seleccionadas por proximidad y coherencia, y ayudan al usuario a entender dónde puede estar disponible el servicio.
Menú de servicios: urgente, apertura de puertas, cambio de cerraduras, cambio de bombines, instalación de cerraduras de seguridad.
```

### §14.5 Ejemplos incorrectos

```text
- GeoHub sin lista de servicios
- GeoHub como artículo sobre la ciudad
- Enlaces a áreas inexistentes
- Cobertura local escrita como si hubiese oficinas en cada zona
```

### §14.6 Regla final

```text
El GeoHub organiza Main City, servicios y cobertura local real.
```

### §14.7 Validación operativa

El GeoHub es el mejor lugar para explicar la cobertura local. Debe tener una sección clara de áreas de posicionamiento local (Direct y Candidate LCA), conectada con servicios y sin transformar cada zona en URL si no está aprobada.

## §15 6. GeoArticle Content Architecture

### §15.1 Explicación

Este bloque define la arquitectura interna de contenido para este tipo de página. No se limita a H1 y meta title. Incluye intro, H2s, bloques de apoyo, áreas de cobertura local, FAQs, CTA, enlaces internos y schema.

### §15.2 Estructura completa

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
Schema
```

### §15.3 Uso de Local Coverage Areas

Las Local Coverage Areas se usan como ejemplos semánticos y contexto real. No se usan para fingir presencia física ni para crear intención principal distinta.

### §15.4 Ejemplo correcto con Cerrajeros Madrid 24h

```text
URL: /madrid/cuanto-cuesta-un-cerrajero-urgente/
Texto: El precio de un cerrajero urgente en Madrid puede variar según el tipo de cerradura, la hora, la urgencia y la zona de cobertura. Una apertura sencilla en un piso de Madrid puede ser diferente de un aviso nocturno en Almagro, Chamberí o Salamanca según disponibilidad y condiciones de desplazamiento.
Enlaces: /cerrajero/madrid/cerrajero-urgente/, /madrid/, /madrid/que-hacer-si-no-puedes-entrar-casa/
```

### §15.5 Ejemplos incorrectos

```text
- Article targeting Almagro as primary location without page
- No link to service page
- Fake office statement
- Article written as sales landing
```

### §15.6 Regla final

```text
GeoArticles use local coverage as context and send authority back to the Main City service page.
```

### §15.7 Validación operativa

Los GeoArticles pueden usar Local Coverage Areas como ejemplos semánticos: tipos de vivienda, zonas cercanas, landmarks o escenarios. Eso ayuda a NLP y AIO sin convertir el artículo en página de zona.

## §16 Tabla de uso de Local Coverage Areas por tipo de página

| Page Type | ¿Usa Local Coverage Areas? | Cómo las usa |
|---|---|---|
| Homepage | Sí, ligero | Service area preview |
| Service Overview | No | No debe ser local |
| Location-Based Service | Sí | Intro, pain points, cobertura, FAQs |
| Additional Category | Sí | Escenarios locales y cobertura |
| GeoHub | Sí, recomendado | Sección principal de cobertura local |
| GeoArticle | Sí | Ejemplos, contexto, landmarks, FAQs |

## §17 Ejemplo práctico completo

```text
Main City:
Madrid

Service:
Cerrajero urgente

Direct Local Coverage Areas:
Almagro, Chamberí

Candidate Local Coverage Areas:
Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad

URL:
/cerrajero/madrid/cerrajero-urgente/

Sección:
H2: Cerrajero urgente en Madrid y zonas de cobertura cercanas

Texto:
Cerrajeros Madrid 24h ayuda a clientes en Madrid con aperturas urgentes, llaves rotas, cambios de bombín y problemas de acceso. También cubrimos Local Coverage Areas como Almagro, Chamberí, Salamanca y Retiro según disponibilidad. Estas zonas son señales GEO de proximidad que refuerzan la relevancia local mientras la página sigue enfocada en el servicio de cerrajero urgente en Madrid.
```

## §18 FAQ ejemplo

```text
Pregunta:
¿Ofrecéis cerrajero urgente en Almagro, Chamberí y Salamanca?

Respuesta:
Sí. Cerrajeros Madrid 24h atiende clientes en Madrid y zonas de cobertura como Almagro, Chamberí y Salamanca según disponibilidad. Esta página se centra en el servicio de cerrajero urgente en Madrid y aclara la cobertura local real.
```

# Bloque III — Reglas Cross-Cutting

> Reglas que aplican a TODOS los page types del Bloque II como filtro de QA. Patrón 3-subsections (Explicación / Cómo aplicamos / Output).

## §19 Reviews y trust blocks en contenido

### §19.1 Explicación

**Explicación**

Las reseñas y señales de confianza deben colocarse donde apoyan la intención: homepage, landings locales, GeoHub y, ocasionalmente, artículos. No deben inventarse ni repetirse como bloque genérico sin contexto.

**Patrón o fórmula**

```text
Trust signal → sección adecuada → servicio o Main City
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h usa reseñas iniciales pendientes de recopilar tras crear el GBP en homepage y en /cerrajero/madrid/cerrajero-urgente/ como prueba local.
```

**Ejemplos incorrectos**

```text
- Pegar el mismo bloque de reseñas en todas las páginas sin contexto
- Usar reseñas de una zona como si fueran de otra
- Inventar certificaciones
```

**Regla final**

```text
Reviews y trust blocks van en cada page type según su rol del funnel; no son uniforme cross-cluster.
```

### §19.2 Cómo aplicamos la regla "Reviews y trust blocks en contenido"

**Fuente:** GMB Crush.

**Método:** Aplicar la regla en cada page type del Bloque II como filtro de QA antes de cerrar la spec del cluster.

### §19.3 Output del paso

**Tipo:** Validation flag — la regla se cumple en todas las page types.

**Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque II.

## §20 FAQs con cobertura natural

### §20.1 Explicación

**Explicación**

Las FAQs pueden mencionar Local Coverage Areas si responden preguntas reales de usuarios. Deben sonar naturales y no funcionar como llaveword stuffing de zonas.

**Patrón o fórmula**

```text
Pregunta real → Main City + coverage area → respuesta útil
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
¿Atendéis emergencias de cerrajería en Almagro y Chamberí? Sí, Cerrajeros Madrid 24h atiende solicitudes en Madrid y zonas de cobertura cercanas según disponibilidad.
```

**Ejemplos incorrectos**

```text
- Crear una FAQ por cada zona sin valor nuevo
- Usar preguntas repetidas cambiando solo el área
- Responder con promesas de oficina inexistente
```

**Regla final**

```text
Las FAQs incorporan menciones de cobertura naturales — sin forzar la zona en cada respuesta.
```

### §20.2 Cómo aplicamos la regla "FAQs con cobertura natural"

**Fuente:** GMB Crush.

**Método:** Aplicar la regla en cada page type del Bloque II como filtro de QA antes de cerrar la spec del cluster.

### §20.3 Output del paso

**Tipo:** Validation flag — la regla se cumple en todas las page types.

**Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque II.

## §21 Schema areaServed coherente

### §21.1 Explicación

**Explicación**

Las Local Coverage Areas pueden reflejarse en areaServed si representan cobertura real. El schema debe diferenciar cobertura de dirección física y no añadir áreas falsas solo por SEO.

**Patrón o fórmula**

```text
Real coverage → areaServed | Physical address → address
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h usa Madrid como address si es su ubicación y puede incluir Almagro, Chamberí, Salamanca y Retiro en areaServed.
```

**Ejemplos incorrectos**

```text
- Poner Almagro como address sin sede
- Añadir ciudades no atendidas en areaServed
- Omitir areaServed si la cobertura es clave
```

**Regla final**

```text
El campo `areaServed` del schema LocalBusiness lista TODAS las LCAs declaradas + Main City.
```

### §21.2 Cómo aplicamos la regla "Schema areaServed coherente"

**Fuente:** GMB Crush.

**Método:** Aplicar la regla en cada page type del Bloque II como filtro de QA antes de cerrar la spec del cluster.

### §21.3 Output del paso

**Tipo:** Validation flag — la regla se cumple en todas las page types.

**Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque II.

# Bloque IV — Checklist Final

## §22 Checklist final del Paso 6

| Check | Pregunta | Estado |
|---|---|---|
| Main City | ¿La página mantiene clara la Main City? | ✅ / ⬜ |
| Local Coverage Areas | ¿Las zonas mencionadas son Direct o Candidate LCA validadas por el test GEO del Paso 1? | ✅ / ⬜ |
| Uso natural | ¿Las áreas aparecen de forma natural y no forzada? | ✅ / ⬜ |
| No URLs innecesarias | ¿No se crearon páginas para áreas no aprobadas? | ✅ / ⬜ |
| No fake office | ¿No se afirma oficina donde no existe? | ✅ / ⬜ |
| FAQs | ¿Las FAQs usan cobertura local cuando aporta valor? | ✅ / ⬜ |
| CTA | ¿El CTA está contextualizado? | ✅ / ⬜ |
| Schema | ¿areaServed refleja cobertura real? | ✅ / ⬜ |
| Enlaces internos | ¿Solo se enlaza a URLs existentes? | ✅ / ⬜ |
| One service | ¿La página mantiene un solo servicio principal cuando aplica? | ✅ / ⬜ |

# Bloque V — Outputs

## §23 Outputs del Paso 6

- Arquitectura interna por tipo de página
- Reglas de uso de Local Coverage Areas
- Ejemplos de secciones de cobertura
- FAQs modelo
- Reglas anti-error
- Bloques de contenido listos para briefs
- Checklist de cobertura local

---

# Bloque VI — Fuentes Internas GMB Crush Usadas

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
