Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo la estructura fija acordada en la conversación.
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# §1 Paso 6 — Estructura de Contenido + Áreas de Cobertura Local

# Bloque I — Introducción

## §2 Objetivo del Paso 6

Definir **cómo se escribe y organiza el contenido real de cada tipo de página** del cluster, y **cómo se usan las Local Coverage Areas (LCAs) en contenido sin convertirlas en URLs**. Mientras el Paso 5 fija las reglas formales por page type (URL, H1, Meta Title, Schema, Word Count, CTA), el Paso 6 fija la arquitectura interna del contenido (intro, H2s, bloques de apoyo, FAQs, ejemplos, secciones de cobertura) y las reglas cross-cutting (reviews, FAQs con cobertura, schema `areaServed`).

**Outputs del Paso 6:**

- §5 Principio 1 — Main City crea arquitectura: una sola ciudad principal genera URLs base
- §6 Principio 2 — LCAs enriquecen contenido: las áreas de cobertura viven en texto, FAQs y `areaServed`, no en path
- §7 Principio 3 — AEAs crean URLs solo si se aprueban: umbral demanda + competencia + contenido único
- §8 Principio 4 — Mencionar una zona ≠ crear una página: separa señal GEO de contenido vs arquitectura URL
- §9 Principio 5 — No falsa ubicación: nunca afirmar oficina física en zonas donde no se opera
- §10 Homepage Content Architecture: 11 bloques (H1, Intro, Quick Answer, Servicios, Cobertura preview, Trust, FAQ, NAP, CTA, Enlaces, Schema)
- §11 Service Overview Content Architecture: 11 bloques sin segmentación local
- §12 Location-Based Service Content Architecture: 12 bloques con cobertura local nativa
- §13 Additional Category Content Architecture: 11 bloques con casos de uso locales
- §14 GeoHub Content Architecture: 10 bloques con sección explícita de cobertura
- §15 GeoArticle Content Architecture: 10 bloques con LCAs como ejemplos semánticos
- §16 Tabla de uso de LCAs por page type — matriz 6×2
- §17 Ejemplo práctico completo — sección de cobertura redactada para Cerrajeros Madrid 24h
- §18 FAQ ejemplo — pregunta + respuesta con cobertura natural
- §19 Reviews y trust blocks en contenido — regla cross-cutting (no uniforme cross-cluster)
- §20 FAQs con cobertura natural — regla cross-cutting (sin keyword stuffing de zonas)
- §21 Schema `areaServed` coherente — regla cross-cutting (coverage real, no falsas zonas)

**Errores que previene el Paso 6:**

- Crear solo formularios sin cuerpo operativo (thin content)
- Mencionar zonas locales de forma artificial (keyword stuffing de barrios)
- Crear páginas para cada Local Coverage Area sin aprobación (sprawl)
- Usar LCAs como si fueran Main City (señal SEO confusa)
- Olvidar dónde van FAQs, CTAs, reviews, LCAs y enlaces internos por page type
- Inventar oficina física en zonas de cobertura sin sede real (E-E-A-T comprometido)
- Pegar el mismo bloque de reseñas en todas las páginas sin contexto del funnel
- Schema `areaServed` que añade ciudades no atendidas solo por SEO

**Cuándo se ejecuta:**

Después del Paso 5 (Page Type Rules) y antes del Paso 7 (Internal Linking + Crawl). El Paso 5 ya fijó qué tiene cada page type a nivel formal; el Paso 6 fija cómo se rellena el cuerpo de cada page type y cómo se integran las LCAs heredadas del Paso 1 §14. El Paso 7 usa los outputs del Paso 6 para construir el grafo de enlaces internos.

## §3 Info heredada de pasos anteriores

El Paso 6 toma como input estos elementos generados en pasos previos. La IA no los re-decide aquí; los usa para construir la arquitectura interna de contenido por page type y las reglas de uso de LCAs.

| # | Input heredado | Origen | Uso en el Paso 6 |
|---|---|---|---|
| 1 | Business Name | Paso 1 §2 | Identidad de marca en H1, intros, NAP y schema |
| 2 | Planned Primary GBP Category + slug | Paso 1 §8 + Paso 3 §3 | Pilar temático de Service Overview, segmento `[primary-cat-slug]` en LBS y AC |
| 3 | Main City + slug | Paso 1 §11 + Paso 3 §3 | Ciudad principal del cluster, segmento `[main-city-slug]` y target geo de LBS, GeoHub y GeoArticles |
| 4 | Physical Location City (NAP) | Paso 1 §12 | Validación cruzada del Principio 5 (No falsa ubicación) |
| 5 | Core services (S = 5) | Paso 1 §13 | Lista de servicios para Service Overview, LBS y menú del GeoHub |
| 6 | Direct Local Coverage Areas | Paso 1 §14 | Zonas con proximidad NAP confirmada → mención principal en cobertura |
| 7 | Candidate Local Coverage Areas | Paso 1 §14 | Zonas candidatas pendientes test GEO → mención secundaria |
| 8 | Approved Expansion Areas (E count) | Paso 1 §15 | Determina si aplica el Principio 3 (E=0 → 0 URLs de expansión) |
| 9 | URL Matrix (28 URLs base) | Paso 3 §3 | URLs concretas a las que aplicar la arquitectura de contenido del Paso 6 |
| 10 | URL patterns (Canonical, Trailing Slash, patrones por page type) | Paso 4 §5–§19 | Reglas formales que el contenido respeta (no se rompen aquí) |
| 11 | Page Type assignment por URL | Paso 5 §3 | Determina qué arquitectura de contenido (§10–§15) aplica a cada URL |
| 12 | Page Type Rules (URL, H1, Meta Title, Schema, Word Count, CTA, etc.) | Paso 5 §7–§12 | El contenido del Paso 6 rellena el body manteniendo las reglas formales del Paso 5 |
| 13 | Brand tone | Paso 5 §6 | Tono aplicado al copywriting de cada page type |
| 14 | Trust Signals declarados | Paso 1 §17 | Bloques de confianza usados en homepage, LBS, GeoHub |
| 15 | Preferred CTA por page type | Paso 5 §11 | CTA aplicado en cada page type |

## §4 Ejemplo rellenado — Outputs del Paso 6 para Cerrajeros Madrid 24h

Esta sección consolida los outputs del Paso 6 en tablas operativas. Cada output corresponde a una sección §X del Bloque II/III y se valida individualmente.

### §4.1 Principios rectores de cobertura local (§5–§9)

| # | Principio | §X | Aplicación (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|---|
| 1 | Main City crea arquitectura | §5 | Madrid es la única Main City del cluster; genera `/madrid/`, `/cerrajero/madrid/...` y `/madrid/...articulo.../` | confirmed |
| 2 | LCAs enriquecen contenido | §6 | Almagro, Chamberí, Salamanca, Retiro aparecen en intros, FAQs y `areaServed`; 0 URLs `/almagro/`, `/chamberi/`, etc. | confirmed |
| 3 | AEAs crean URLs solo si se aprueban | §7 | E=0 en Phase 1 → 0 URLs de expansión generadas | confirmed |
| 4 | Mencionar zona ≠ crear página | §8 | Almagro mencionado en `/cerrajero/madrid/cerrajero-urgente/` sin enlace a `/almagro/` (no existe) | confirmed |
| 5 | No falsa ubicación | §9 | NAP = Madrid; ninguna página afirma oficina en Almagro, Chamberí, Salamanca o Retiro | confirmed |

### §4.2 Content Architecture por page type (§10–§15)

| # | Page Type | §X | Bloques de contenido | URLs aplicadas (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|---|---|
| 1 | Homepage | §10 | H1, Intro, Quick Answer, Servicios principales, Cobertura preview, Trust, FAQ, NAP, CTA, Enlaces, Schema (11 bloques) | `/` (1 URL) | confirmed |
| 2 | Service Overview | §11 | H1, Intro no local, H2 Authority/Uniqueness/Depth/Intent/Optimization, Bullets, FAQs, CTA, Enlaces, Schema (11 bloques) | 5 URLs (`/cerrajero/{service}/`) | confirmed |
| 3 | Location-Based Service | §12 | H1, Intro local 100–150w, Quick Local Answer, H2 Authority/Uniqueness/Depth, H2 Local Pain Points, H2 LCA Served, H2 Related Services, FAQs, CTA, Enlaces, Schema (12 bloques) | 5 URLs (`/cerrajero/madrid/{service}/`) | confirmed |
| 4 | Additional Category | §13 | H1, Intro problema local, H2 Authority/Uniqueness/Depth/Intent/Optimization, Local Coverage Use Case, FAQs, CTA, Enlaces, Schema (11 bloques) | 1 URL (`/cerrajero/madrid/duplicado-llaves/`) | confirmed |
| 5 | GeoHub | §14 | H1, City intro, Menú servicios, AC Menu, LCA Section, GeoArticle Resources, Trust, CTA, Enlaces, Schema (10 bloques) | 1 URL (`/madrid/`) | confirmed |
| 6 | GeoArticle | §15 | H1, Intro contextual, H2 Problem, H2 Local Context, H2 Options/Mistakes, H2 When to Call, H2 Local Examples, FAQs, CTA, Enlaces, Schema (10 bloques) | 15 URLs (`/madrid/{topic}/`) | ⚠ inferido (topics requieren keyword research real, ver §24.1) |

### §4.3 Uso de Local Coverage Areas por page type (§16)

| Page Type | ¿Usa LCAs? | Cómo las usa | Cantidad típica |
|---|---|---|---|
| Homepage | Sí, ligero | Service area preview en bloque dedicado | 3–5 LCAs mencionadas |
| Service Overview | No | NO debe ser local; pilar temático sin geo | 0 LCAs |
| Location-Based Service | Sí | Intro, pain points, sección cobertura, FAQs | 2–4 LCAs naturales |
| Additional Category | Sí | Escenarios locales y cobertura de la categoría | 2–4 LCAs |
| GeoHub | Sí, recomendado | Sección principal de cobertura local (TODAS las LCAs) | All Direct + Candidate |
| GeoArticle | Sí | Ejemplos, contexto, landmarks, FAQs | 2–4 LCAs como ejemplos |

### §4.4 Reglas cross-cutting de contenido (§19–§21)

| # | Regla | §X | Validación (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|---|
| 1 | Reviews y trust blocks contextualizados por page type | §19 | Trust signals adaptados al funnel: homepage (4 signals), LBS (3 signals + reviews iniciales pendientes), GeoHub (4 signals globales) — no uniforme cross-cluster | confirmed |
| 2 | FAQs con cobertura natural | §20 | FAQs de LBS mencionan Almagro/Chamberí en respuestas reales; 0 FAQs construidas como keyword stuffing de zonas | confirmed |
| 3 | Schema `areaServed` coherente | §21 | `areaServed` lista TODAS las LCAs declaradas (Almagro, Chamberí, Salamanca, Retiro) + Madrid; 0 ciudades fuera de cobertura | confirmed |

### §4.5 Outputs auxiliares (§16–§18)

| # | Output | §X | Tipo | Status |
|---|---|---|---|---|
| 1 | Tabla de uso de LCAs por page type | §16 | Matriz 6×2 | confirmed |
| 2 | Ejemplo práctico completo (sección de cobertura) | §17 | Texto modelo redactado | confirmed |
| 3 | FAQ ejemplo (pregunta + respuesta) | §18 | Plantilla de FAQ con cobertura natural | confirmed |

### §4.6 Validaciones cruzadas con otros pasos

| Validación | Origen | Comprobación en Paso 6 | Status |
|---|---|---|---|
| Servicios mencionados = core services del Paso 1 §13 | Paso 1 §13 | 5 servicios en homepage y GeoHub coinciden con core services | OK |
| LCAs mencionadas = Direct + Candidate LCAs del Paso 1 §14 | Paso 1 §14 | Almagro, Chamberí (Direct) + Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad (Candidate) | OK |
| URLs referenciadas en contenido existen en URL Matrix (Paso 3 §3) | Paso 3 §3 | Todos los enlaces internos apuntan a URLs aprobadas; 0 enlaces a `/almagro/` u otras inexistentes | OK |
| Reglas formales del Paso 5 (H1, Meta Title, Word Count) respetadas | Paso 5 §7–§12 | Bloques de contenido del Paso 6 cumplen los caps formales del Paso 5 | OK |
| `areaServed` del schema (Paso 5 §X.7) lista LCAs declaradas | Paso 5 + Paso 1 §14 | Schema coherente: Madrid en `address`, LCAs en `areaServed` | OK |

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

# Bloque V — Outputs consolidados

## §23 Outputs del Paso 6

| # | Output | §X | Tipo |
|---|---|---|---|
| 1 | Principio 1 — Main City crea arquitectura | §5 | Validation flag |
| 2 | Principio 2 — LCAs enriquecen contenido | §6 | Validation flag |
| 3 | Principio 3 — AEAs crean URLs solo si se aprueban | §7 | Validation flag |
| 4 | Principio 4 — Mencionar zona ≠ crear página | §8 | Validation flag |
| 5 | Principio 5 — No falsa ubicación | §9 | Validation flag |
| 6 | Homepage Content Architecture | §10 | Estructura de contenido (11 bloques) |
| 7 | Service Overview Content Architecture | §11 | Estructura de contenido (11 bloques) |
| 8 | Location-Based Service Content Architecture | §12 | Estructura de contenido (12 bloques) |
| 9 | Additional Category Content Architecture | §13 | Estructura de contenido (11 bloques) |
| 10 | GeoHub Content Architecture | §14 | Estructura de contenido (10 bloques) |
| 11 | GeoArticle Content Architecture | §15 | Estructura de contenido (10 bloques) |
| 12 | Tabla de uso de LCAs por page type | §16 | Matriz 6×2 |
| 13 | Ejemplo práctico completo | §17 | Texto modelo |
| 14 | FAQ ejemplo | §18 | Plantilla |
| 15 | Reviews y trust blocks contextualizados | §19 | Validation flag |
| 16 | FAQs con cobertura natural | §20 | Validation flag |
| 17 | Schema `areaServed` coherente | §21 | Validation flag |

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
