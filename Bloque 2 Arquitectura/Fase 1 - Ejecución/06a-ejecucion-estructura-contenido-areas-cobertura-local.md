Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# Paso 6 — Estructura de Contenido + Áreas de Cobertura Local

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 17 outputs del Paso 6 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, obtención de outputs, checklist final y outputs consolidados.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 6

<small>§2</small>

Definir **cómo se escribe y organiza el contenido real de cada tipo de página** del cluster, y **cómo se usan las Local Coverage Areas (LCAs) en contenido sin convertirlas en URLs**. Mientras el Paso 5 fija las reglas formales por page type (URL, H1, Meta Title, Schema, Word Count, CTA), el Paso 6 fija la arquitectura interna del contenido (intro, H2s, bloques de apoyo, FAQs, ejemplos, secciones de cobertura) y las reglas cross-cutting (reviews, FAQs con cobertura, schema `areaServed`).

**Outputs del paso:**

- **6.1** Principio 1 — Main City crea arquitectura: una sola ciudad principal genera URLs base
- **6.2** Principio 2 — LCAs enriquecen contenido: las áreas de cobertura viven en texto, FAQs y `areaServed`, no en path
- **6.3** Principio 3 — AEAs crean URLs solo si se aprueban: umbral demanda + competencia + contenido único
- **6.4** Principio 4 — Mencionar zona ≠ crear página: separa señal GEO de contenido vs arquitectura URL
- **6.5** Principio 5 — No falsa ubicación: nunca afirmar oficina física en zonas donde no se opera
- **6.6** Homepage Content Architecture: 11 bloques (H1, Intro, Quick Answer, Servicios, Cobertura preview, Trust, FAQ, NAP, CTA, Enlaces, Schema)
- **6.7** Service Overview Content Architecture: 11 bloques sin segmentación local
- **6.8** Location-Based Service Content Architecture: 12 bloques con cobertura local nativa
- **6.9** Additional Category Content Architecture: 11 bloques con casos de uso locales
- **6.10** GeoHub Content Architecture: 10 bloques con sección explícita de cobertura
- **6.11** GeoArticle Content Architecture: 10 bloques con LCAs como ejemplos semánticos
- **6.12** Tabla de uso de LCAs por page type — matriz 6×2
- **6.13** Ejemplo práctico completo — sección de cobertura redactada para Cerrajeros Madrid 24h
- **6.14** FAQ ejemplo — pregunta + respuesta con cobertura natural
- **6.15** Reviews y trust blocks en contenido — regla cross-cutting (no uniforme cross-cluster)
- **6.16** FAQs con cobertura natural — regla cross-cutting (sin keyword stuffing de zonas)
- **6.17** Schema `areaServed` coherente — regla cross-cutting (coverage real, no falsas zonas)

**Errores que previene:**

- Crear solo formularios sin cuerpo operativo (thin content)
- Mencionar zonas locales de forma artificial (keyword stuffing de barrios)
- Crear páginas para cada Local Coverage Area sin aprobación (sprawl)
- Usar LCAs como si fueran Main City (señal SEO confusa)
- Olvidar dónde van FAQs, CTAs, reviews, LCAs y enlaces internos por page type
- Inventar oficina física en zonas de cobertura sin sede real (E-E-A-T comprometido)
- Pegar el mismo bloque de reseñas en todas las páginas sin contexto del funnel
- Schema `areaServed` que añade ciudades no atendidas solo por SEO

**Cuándo se ejecuta:** Después del Paso 5 (Page Type Rules) y antes del Paso 7 (Internal Linking + Crawl). El Paso 5 ya fijó qué tiene cada page type a nivel formal; el Paso 6 fija cómo se rellena el cuerpo de cada page type y cómo se integran las LCAs heredadas del Paso 1 §6.10. El Paso 7 usa los outputs del Paso 6 para construir el grafo de enlaces internos.

## Info heredada de pasos anteriores

<small>§3</small>

> Estos campos NO se deciden en Paso 6 — la IA los lee del paso indicado y los usa como input para construir la arquitectura interna de contenido por page type y las reglas de uso de LCAs.

| # | Input heredado | Origen | Uso en el Paso 6 |
|---|---|---|---|
| 1 | Business Name | Paso-01 1.1 | Identidad de marca en H1, intros, NAP y schema |
| 2 | Planned Primary GBP Category + slug | Paso-01 1.5 + Paso-02 2.2 | Pilar temático de Service Overview, segmento `[primary-cat-slug]` en LBS y AC |
| 3 | Main City + slug | Paso-01 1.7 + Paso-02 2.3 | Ciudad principal del cluster, segmento `[main-city-slug]` y target geo de LBS, GeoHub y GeoArticles |
| 4 | Physical Location City (NAP) | Paso-01 1.8 | Validación cruzada del Principio 5 (No falsa ubicación) |
| 5 | Core services (S=5) | Paso-01 1.9 | Lista de servicios para Service Overview, LBS y menú del GeoHub |
| 6 | Direct Local Coverage Areas | Paso-01 1.10 | Zonas con proximidad NAP confirmada → mención principal en cobertura |
| 7 | Candidate Local Coverage Areas | Paso-01 1.10 | Zonas candidatas pendientes test GEO → mención secundaria |
| 8 | Approved Expansion Areas (E count) | Paso-01 1.11 | Determina si aplica el Principio 3 (E=0 → 0 URLs de expansión) |
| 9 | URL Matrix (28 URLs base) | Paso-03 3.5 | URLs concretas a las que aplicar la arquitectura de contenido del Paso 6 |
| 10 | URL patterns (Canonical, Trailing Slash, patrones por page type) | Paso-04 4.1 a 4.15 | Reglas formales que el contenido respeta (no se rompen aquí) |
| 11 | Page Type assignment por URL | Paso 5 (Page Type Rules) | Determina qué arquitectura de contenido (6.6–6.11) aplica a cada URL |
| 12 | Page Type Rules (URL, H1, Meta Title, Schema, Word Count, CTA, etc.) | Paso 5 | El contenido del Paso 6 rellena el body manteniendo las reglas formales del Paso 5 |
| 13 | Brand tone | Paso 5 | Tono aplicado al copywriting de cada page type |
| 14 | Trust Signals declarados | Paso-01 1.14 | Bloques de confianza usados en homepage, LBS, GeoHub |
| 15 | Preferred CTA | Paso-01 1.13 | CTA aplicado en cada page type |

# Bloque II — Ejemplo rellenado para el Paso 6 — Estructura de Contenido + LCAs

<small>§4</small>

> Los 17 outputs del Paso 6 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 6.X declarado en §5.

### 6.1 — Principio 1 (Main City crea arquitectura)

Madrid es la única Main City del cluster. Genera `/madrid/`, `/cerrajero/madrid/...` y `/madrid/...articulo.../`. Validado en toda la arquitectura del Bloque II.

### 6.2 — Principio 2 (LCAs enriquecen contenido)

Almagro, Chamberí, Salamanca, Retiro aparecen en intros, FAQs y `areaServed`. 0 URLs `/almagro/`, `/chamberi/`, etc. Validado.

### 6.3 — Principio 3 (AEAs crean URLs solo si se aprueban)

E=0 en Phase 1 → 0 URLs de expansión generadas. Validado.

### 6.4 — Principio 4 (Mencionar zona ≠ crear página)

Almagro mencionado en `/cerrajero/madrid/cerrajero-urgente/` sin enlace a `/almagro/` (no existe). Validado.

### 6.5 — Principio 5 (No falsa ubicación)

NAP = Madrid; ninguna página afirma oficina en Almagro, Chamberí, Salamanca o Retiro. Validado.

### 6.6 — Homepage Content Architecture (11 bloques)

URL: `/`

Bloques de contenido:
1. H1: "Cerrajeros Madrid 24h – Servicios de cerrajería de confianza en Madrid"
2. Intro
3. Quick Answer
4. Servicios principales (5 SO links)
5. Vista previa de cobertura local (3-5 LCAs ligeras)
6. Bloques de confianza (4 trust signals)
7. Sección FAQ (4 preguntas)
8. Bloque NAP
9. CTA
10. Enlaces internos
11. Schema (Organization + WebSite + LocalBusiness + FAQPage + Speakable)

### 6.7 — Service Overview Content Architecture (11 bloques)

URLs: 5 SO (`/cerrajero/{service}/`)

Bloques de contenido:
1. H1
2. Intro no local (sin Main City como target principal)
3-7. H2 Authority / Uniqueness / Depth / Intent / Optimization
8. Bullet sections
9. FAQs
10. CTA
11. Enlaces internos (incluyendo link a su LBS local)

### 6.8 — Location-Based Service Content Architecture (12 bloques)

URLs: 5 LBS (`/cerrajero/madrid/{service}/`)

Bloques de contenido:
1. H1
2. Intro local 100–150 words
3. Quick Local Answer
4-7. H2 Authority / Uniqueness / Depth / Local Pain Points
8. H2 Local Coverage Areas Served (2-4 LCAs)
9. H2 Related Services in [Main City]
10. FAQs (con cobertura natural)
11. CTA + Schema

### 6.9 — Additional Category Content Architecture (11 bloques)

URL: `/cerrajero/madrid/duplicado-llaves/`

Bloques de contenido:
1. H1
2. Intro con problema local
3-7. H2 Authority / Uniqueness / Depth / Intent / Optimization
8. Local Coverage Use Case (2-4 LCAs como escenarios)
9. FAQs
10. CTA
11. Enlaces internos + Schema

### 6.10 — GeoHub Content Architecture (10 bloques)

URL: `/madrid/`

Bloques de contenido:
1. H1
2. City intro
3. Menú de servicios (5 LBS)
4. Additional Category Menu
5. Local Coverage Areas Section (TODAS las LCAs declaradas)
6. GeoArticle Resources (15 GAs listados)
7. Trust Signals
8. CTA
9. Enlaces internos
10. Schema (CollectionPage + BreadcrumbList)

### 6.11 — GeoArticle Content Architecture (10 bloques)

URLs: 15 GAs (`/madrid/{topic}/`)

Bloques de contenido:
1. H1
2. Intro contextual
3-6. H2 Problem / Local Context / Options-Mistakes / When to Call
7. H2 Local Examples (LCAs como ejemplos semánticos)
8. FAQs
9. CTA
10. Enlaces internos + Schema (Article + FAQPage + BreadcrumbList)

### 6.12 — Tabla de uso de LCAs por page type

| Page Type | ¿Usa LCAs? | Cómo las usa |
|---|---|---|
| Homepage | Sí, ligero | Service area preview |
| Service Overview | No | No debe ser local |
| Location-Based Service | Sí | Intro, pain points, cobertura, FAQs |
| Additional Category | Sí | Escenarios locales y cobertura |
| GeoHub | Sí, recomendado | Sección principal de cobertura local |
| GeoArticle | Sí | Ejemplos, contexto, landmarks, FAQs |

### 6.13 — Ejemplo práctico completo (sección de cobertura)

Aplicado a `/cerrajero/madrid/cerrajero-urgente/`:

```
H2: Cerrajero urgente en Madrid y zonas de cobertura cercanas

Texto:
Cerrajeros Madrid 24h ayuda a clientes en Madrid con aperturas
urgentes, llaves rotas, cambios de bombín y problemas de acceso.
También cubrimos Local Coverage Areas como Almagro, Chamberí,
Salamanca y Retiro según disponibilidad. Estas zonas son señales
GEO de proximidad que refuerzan la relevancia local mientras la
página sigue enfocada en el servicio de cerrajero urgente en Madrid.
```

### 6.14 — FAQ ejemplo

```
Pregunta:
¿Ofrecéis cerrajero urgente en Almagro, Chamberí y Salamanca?

Respuesta:
Sí. Cerrajeros Madrid 24h atiende clientes en Madrid y zonas de
cobertura como Almagro, Chamberí y Salamanca según disponibilidad.
Esta página se centra en el servicio de cerrajero urgente en Madrid
y aclara la cobertura local real.
```

### 6.15 — Reviews y trust blocks contextualizados

Trust signals adaptados al funnel:
- Homepage: 4 signals globales
- LBS: 3 signals + reviews iniciales pendientes
- GeoHub: 4 signals globales

NO uniforme cross-cluster — cada page type usa los trust signals que apoyan su intención.

### 6.16 — FAQs con cobertura natural

FAQs de LBS mencionan Almagro/Chamberí en respuestas reales. 0 FAQs construidas como keyword stuffing de zonas. Cada FAQ responde una pregunta natural del usuario.

### 6.17 — Schema `areaServed` coherente

`areaServed` lista TODAS las LCAs declaradas (Almagro, Chamberí, Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad) + Madrid. 0 ciudades fuera de cobertura.

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 17 outputs que el Paso 6 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `6.1`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 6.1 | Principio 1 — Main City crea arquitectura | Validation flag | GMB Crush | Paso-01 1.7 |
| 6.2 | Principio 2 — LCAs enriquecen contenido | Validation flag | GMB Crush | Paso-01 1.10 |
| 6.3 | Principio 3 — AEAs crean URLs solo si se aprueban | Validation flag | GMB Crush | Paso-01 1.11 |
| 6.4 | Principio 4 — Mencionar zona ≠ crear página | Validation flag | GMB Crush | — |
| 6.5 | Principio 5 — No falsa ubicación | Validation flag | GMB Crush | Paso-01 1.8 |
| 6.6 | Homepage Content Architecture | Estructura de contenido (11 bloques) | GMB Crush | Paso-03 3.5 + Paso 5 |
| 6.7 | Service Overview Content Architecture | Estructura de contenido (11 bloques) | GMB Crush | Paso-03 3.5 + Paso 5 |
| 6.8 | Location-Based Service Content Architecture | Estructura de contenido (12 bloques) | GMB Crush | Paso-03 3.5 + Paso 5 |
| 6.9 | Additional Category Content Architecture | Estructura de contenido (11 bloques) | GMB Crush | Paso-03 3.5 + Paso 5 |
| 6.10 | GeoHub Content Architecture | Estructura de contenido (10 bloques) | GMB Crush | Paso-03 3.5 + Paso 5 |
| 6.11 | GeoArticle Content Architecture | Estructura de contenido (10 bloques) | GMB Crush | Paso-03 3.5 + Paso 5 |
| 6.12 | Tabla de uso de LCAs por page type | Matriz 6×2 | GMB Crush | Paso-01 1.10 |
| 6.13 | Ejemplo práctico completo (sección cobertura) | Texto modelo redactado | GMB Crush | — |
| 6.14 | FAQ ejemplo | Plantilla de FAQ con cobertura natural | GMB Crush | — |
| 6.15 | Reviews y trust blocks contextualizados | Validation flag | GMB Crush | Paso-01 1.14 |
| 6.16 | FAQs con cobertura natural | Validation flag | GMB Crush | — |
| 6.17 | Schema `areaServed` coherente | Validation flag | GMB Crush | Paso-01 1.10 + Paso 8 |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 17 outputs (6.1–6.17). Los **principios** (6.1–6.5) y las **reglas cross-cutting** (6.15–6.17) usan el patrón estándar (Explicación / Patrón / Ejemplos / Regla final / Validación operativa / Cómo se obtiene / Output del paso). Las **content architectures por page type** (6.6–6.11) usan un mini-patrón adaptado (Explicación / Estructura completa / Uso de Local Coverage Areas / Ejemplo correcto / Ejemplos incorrectos / Regla final / Validación operativa). Los **outputs auxiliares** (6.12–6.14) son tablas/ejemplos modelo.

### 6.1 — Principio 1: Main City crea arquitectura

<small>§6.1</small>

**Explicación**

La Main City es la ciudad principal que genera URLs base. Todo el sistema base se organiza alrededor de esa ciudad. Las LCAs y AEAs son capas separadas (contenido + posibles URLs aprobadas) que NO sustituyen ni compiten con la Main City como eje arquitectónico.

**Patrón o fórmula**

```text
Main City → /city/ + /category/city/service/ + /city/article-topic/
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Madrid genera:
  /madrid/                                        (GeoHub)
  /cerrajero/madrid/cerrajero-urgente/            (LBS)
  /madrid/cuanto-cuesta-un-cerrajero-urgente/     (GeoArticle)
```

**Ejemplos incorrectos**

```text
- Almagro genera URL sin aprobación (no es Main City)
- Salamanca se usa como Main City en una página de Madrid
- Cambiar Main City por cada bloque (inconsistencia)
- Mezclar Main City y LCAs en el mismo nivel jerárquico
```

**Regla final**

```text
La arquitectura del cluster se construye sobre una sola Main City.
```

**Validación operativa**

Aplicar el principio como filtro de QA al revisar la arquitectura del cluster antes de avanzar al Paso 7 (Internal Linking). Validar que ninguna URL generada usa una zona distinta a la Main City como segmento city principal.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar el principio como filtro de QA al revisar la arquitectura del cluster. Cruzar con Paso-01 1.7 (Main City declarada) y Paso-04 4.6 (LBS pattern usa main-city-slug).

**Output del paso**

- **Tipo:** Validation flag — el principio se respeta en toda la arquitectura del Bloque III.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado — Madrid es la única Main City; Almagro/Chamberí no aparecen como city en URLs base.

### 6.2 — Principio 2: LCAs enriquecen contenido

<small>§6.2</small>

**Explicación**

Las Local Coverage Areas son zonas seleccionadas por proximidad al NAP, coherencia GEO y lógica GMB Crush. Se usan para contexto, FAQs, ejemplos, señales locales y schema `areaServed`. NO crean URLs por defecto — viven en el contenido como señales semánticas.

**Patrón o fórmula**

```text
Local Coverage Areas → content + FAQs + examples + areaServed
                     ↛ URLs base (a menos que pasen a AEA)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Almagro, Chamberí, Salamanca y Retiro se mencionan en:
  - Intro de LBS (/cerrajero/madrid/cerrajero-urgente/)
  - Sección de cobertura del GeoHub (/madrid/)
  - FAQs de LBS y GeoHub
  - Schema areaServed
0 URLs `/almagro/`, `/chamberi/` generadas.
```

**Ejemplos incorrectos**

```text
- Crear páginas por cada zona (sprawl arquitectónico)
- Listar zonas donde no se atiende (señal débil)
- Usarlas como H1 principal (canibaliza Main City)
- Mencionar 30 zonas sin contexto (keyword stuffing)
```

**Regla final**

```text
Las LCAs viven en contenido y schema, nunca como segmentos de URL.
```

**Validación operativa**

Aplicar el principio como filtro de QA. Validar que las LCAs declaradas en Paso-01 1.10 aparecen en el contenido de las page types relevantes (LBS, GeoHub, GAs) y NO como URLs base. Cruce con Paso-04 4.9 (LCAs no generan URLs).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar el principio como filtro de QA al revisar la arquitectura del cluster antes de avanzar al Paso 7. Verificar que las LCAs aparecen en contenido y schema, no en URLs.

**Output del paso**

- **Tipo:** Validation flag — el principio se respeta en toda la arquitectura del Bloque III.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado — 10 LCAs (Almagro, Chamberí, Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad) en contenido + `areaServed`; 0 URLs `/{lca}/`.

### 6.3 — Principio 3: Approved Expansion Areas crean URLs solo si se aprueban

<small>§6.3</small>

**Explicación**

Cuando una zona tiene demanda, competencia o valor comercial demostrable, puede pasar a Approved Expansion Area (AEA) y entonces SÍ generar URLs propias. Esta promoción de LCA → AEA es decisión consciente de diseño, no automática.

**Patrón o fórmula**

```text
Local Coverage Area → Approved Expansion Area → URLs aprobadas
Umbral: demanda + competencia + contenido único + valor comercial
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Phase 1: E = 0 → ninguna LCA promovida a AEA.
Hipotético: si Almagro se aprueba después por demanda demostrada,
            puede generar /almagro/, /cerrajero/almagro/cerrajero-urgente/
            como expansión separada de la base.
```

**Ejemplos incorrectos**

```text
- Aprobar todas las zonas (sprawl)
- Crear expansión antes de terminar Madrid
- Crear expansión sin contenido único
- Aprobar AEA solo por keyword research sin valor comercial
- Mezclar AEA con base sin separar el sub-cluster
```

**Regla final**

```text
Approved Expansion Areas se aprueban por umbral demanda + competencia + contenido único, no por defecto.
```

**Validación operativa**

Una Local Coverage Area solo se convierte en Approved Expansion Area si hay demanda, valor comercial, oportunidad competitiva y contenido único. Esta regla protege el sistema de expansión prematura. Cruce con Paso-01 1.11 (AEAs declaradas en intake) y Paso-04 4.10 (Approved Expansion URLs).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar el principio como filtro de QA. Validar que el campo Approved Expansion Areas (Paso-01 1.11) está vacío o contiene solo zonas que cumplen el umbral. En Phase 1 default E=0.

**Output del paso**

- **Tipo:** Validation flag — el principio se respeta en toda la arquitectura del Bloque III.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado — E=0 en Phase 1; 0 URLs de expansión generadas.

### 6.4 — Principio 4: Mencionar una zona no es crear una página

<small>§6.4</small>

**Explicación**

Este principio evita confundir señales GEO de contenido con arquitectura de URLs. Una zona puede mencionarse natural y útilmente en el body, FAQs, schema `areaServed` sin que ello implique crear `/{zona}/` o cualquier URL anidada con esa zona.

**Patrón o fórmula**

```text
Mention en contenido ≠ URL del cluster
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Se menciona Almagro dentro de /cerrajero/madrid/cerrajero-urgente/
sin enlazar a /almagro/ (no existe). El texto:

"Atendemos cerrajería urgente en Madrid, especialmente en zonas
próximas como Almagro y Chamberí, según disponibilidad."
```

**Ejemplos incorrectos**

```text
- Crear enlaces (anchors) a URLs inexistentes (ej. <a href="/almagro/">)
- Usar la zona en breadcrumbs (Home > Almagro > ...)
- Crear páginas por presión de keyword research sin valor comercial
- Mencionar zona y luego enlazar a búsqueda externa
```

**Regla final**

```text
Mencionar una zona como cobertura no implica crear una URL para esa zona.
```

**Validación operativa**

Mencionar una zona en el contenido no implica crear una URL. Esta separación es clave para que el sistema base se mantenga enfocado y no genere thin content. Cruce con Paso-07 7.8 (LCAs sin URL no reciben enlaces).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar el principio como filtro de QA al revisar el contenido de cada page type. Las LCAs aparecen como menciones textuales puras, NO como anchors hacia URLs inexistentes.

**Output del paso**

- **Tipo:** Validation flag — el principio se respeta en toda la arquitectura del Bloque III.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado — LCAs mencionadas en contenido sin anchors hacia URLs.

### 6.5 — Principio 5: No falsa ubicación

<small>§6.5</small>

**Explicación**

Si la oficina física está en Madrid (NAP), no se afirma oficina en Almagro, Salamanca o Retiro. La cobertura de servicio (areaServed) es distinta de la presencia física (address). Confundirlos es un riesgo E-E-A-T y puede degradar el LocalBusiness en GBP.

**Patrón o fórmula**

```text
Service coverage (zonas atendidas) ≠ physical presence (oficina/sede)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Página /cerrajero/madrid/cerrajero-urgente/:
  CORRECTO: "Atendemos clientes en Madrid y zonas como Almagro,
             Chamberí, Salamanca y Retiro según disponibilidad."

  INCORRECTO: "Nuestra oficina en Almagro abre 24h."
              (no hay oficina en Almagro — NAP es en Madrid)
```

**Ejemplos incorrectos**

```text
- "Nuestra oficina en Salamanca" (no existe)
- "Visita nuestra tienda en Almagro" (no existe)
- Schema address con city = Chamberí (NAP es Madrid)
- "Servicio físico en Retiro" cuando el negocio es móvil sin sede ahí
```

**Regla final**

```text
Nunca afirmar oficina física en zonas donde el negocio no opera realmente.
```

**Validación operativa**

Aplicar el principio como filtro de QA al revisar el contenido de cada page type. Validar que las menciones de LCAs usan lenguaje de cobertura ("atendemos", "cubrimos", "según disponibilidad") y NO de presencia física ("oficina", "tienda", "sede"). Cruce con Paso-01 1.8 (Physical Location City) y Paso-04 4.14 (No falsa ubicación).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar el principio como filtro de QA al revisar el contenido. Para cada mención de LCA, verificar que usa lenguaje de cobertura, no de presencia física.

**Output del paso**

- **Tipo:** Validation flag — el principio se respeta en toda la arquitectura del Bloque III.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado — NAP=Madrid; ninguna página afirma oficina en Almagro, Chamberí, Salamanca o Retiro.

### 6.6 — Homepage Content Architecture

<small>§6.6</small>

**Explicación**

Define la arquitectura interna de contenido para la Homepage del cluster. No se limita a H1 y meta title; incluye todos los bloques de contenido que rellenan la página: intro, H2s, áreas de cobertura local, FAQs, NAP, CTA, enlaces internos y schema. La homepage es el punto de entrada principal — debe reforzar marca, categoría, Main City, servicios y cobertura sin convertirse en lista interminable de zonas.

**Estructura completa (11 bloques)**

```text
1. H1 (Title Case con Brand + Service + Main City)
2. Intro (1-2 párrafos value prop)
3. Quick Answer (resumen de servicios)
4. Servicios principales (5 SO links con descripción breve)
5. Vista previa de cobertura local (3-5 LCAs en bloque service-area-preview)
6. Bloques de confianza (4 trust signals heredados de Paso-01 1.14)
7. Sección FAQ (4 preguntas, FAQPage schema)
8. Bloque NAP (heredado Paso-01 1.4)
9. CTA (heredado Paso-01 1.13 — Llamar ahora)
10. Enlaces internos (8 outbound según Paso-07 7.2)
11. Schema (Organization + WebSite + LocalBusiness + FAQPage + Speakable)
```

**Uso de Local Coverage Areas**

La homepage puede mencionar 3–5 LCAs **de forma ligera**, normalmente en un bloque de service-area-preview. NO debe convertirse en una lista masiva de zonas ni usar las áreas de cobertura como sustituto de la Main City.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
H1: Cerrajeros Madrid 24h – Servicios de cerrajería de confianza en Madrid

Vista previa de cobertura local:
"Atendemos clientes en Madrid y zonas de cobertura como Almagro,
Chamberí, Salamanca y Retiro según disponibilidad."

Enlaces a servicios principales:
  /cerrajero/cerrajero-urgente/
  /cerrajero/apertura-puertas/
  /cerrajero/cambio-bombines/

Enlace al GeoHub: /madrid/
```

**Ejemplos incorrectos**

```text
- Homepage con 30 zonas listadas sin contexto
- Homepage orientada a Almagro, Salamanca y Retiro al mismo nivel que Madrid
- Homepage sin Servicios principales (debilita silo)
- Homepage sin NAP (señal débil de entidad local)
- Homepage sin enlaces a SO (silo desconectado)
```

**Regla final**

```text
La homepage debe reforzar marca, categoría, Main City, servicios y cobertura real sin crear URLs innecesarias.
```

**Validación operativa**

La homepage puede mencionar LCAs, pero no debe convertirse en una lista interminable de zonas. Su prioridad sigue siendo entidad, categoría GBP, Main City, servicios, NAP y confianza. Validar que tiene los 11 bloques + cobertura ligera (3-5 LCAs).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la arquitectura de 11 bloques al contenido de la homepage. Heredar Brand Name, NAP, Trust Signals, Preferred CTA del Paso 1. Mencionar 3-5 LCAs Direct + algunas Candidate ligeras.

**Output del paso**

- **Tipo:** Estructura de contenido (11 bloques) para `/`.
- **Ejemplo (Cerrajeros Madrid 24h):** 1 URL (`/`) con los 11 bloques aplicados.

### 6.7 — Service Overview Content Architecture

<small>§6.7</small>

**Explicación**

Define la arquitectura interna de las 5 Service Overview Pages (SO). Las SO son **pilares temáticos** del servicio sin geolocalización principal. Su función es construir autoridad temática para cada core service y enlazar a la versión local (LBS) correspondiente.

**Estructura completa (11 bloques)**

```text
1. H1 (servicio sin Main City como target principal)
2. Intro no local (descripción del servicio en términos generales)
3. H2 Authority
4. H2 Uniqueness
5. H2 Depth
6. H2 Intent
7. H2 Optimization
8. Bullet sections (sub-temas relacionados)
9. FAQs (sobre el servicio en general, no localizadas)
10. CTA + Enlaces internos (incluye link a LBS de Main City — Paso-07 7.3)
11. Schema (Service + WebPage + BreadcrumbList)
```

**Uso de Local Coverage Areas**

**No se usan** Local Coverage Areas. Esta página NO debe mencionar Madrid, Almagro, Salamanca ni ninguna zona como target principal. Su función es ser pilar temático del servicio.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
URL: /cerrajero/cerrajero-urgente/
H1: "Servicios profesionales de cerrajería urgente"
Intro: "Cerrajeros Madrid 24h ofrece servicios profesionales de
cerrajería urgente: aperturas urgentes, llaves rotas y problemas
de acceso."

Sin segmentación local en H2s ni body principal.

Internal link to local version:
  /cerrajero/madrid/cerrajero-urgente/
```

**Ejemplos incorrectos**

```text
- Mencionar Almagro en el H1 (debilita pilar temático)
- Crear un bloque de cobertura local en service overview (rol incorrecto)
- Usar /madrid/ como target principal (canibaliza la LBS)
- No enlazar a la versión local (silo roto, sin push to LBS)
- Repetir contenido de la LBS Madrid (canibalización)
```

**Regla final**

```text
Service Overview = servicio sin localización.
```

**Validación operativa**

Las páginas de servicio general deben evitar Main City y LCAs como objetivo principal. Su trabajo es explicar el servicio de forma no geolocalizada y actuar como pilar temático. Validar que el H1 y los H2s no incluyen city principal. Validar que enlaza a su LBS Madrid (Paso-07 7.3).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la arquitectura de 11 bloques a cada SO. NO incluir city en H1 ni H2 principales. Enlazar a LBS Main City como puente al funnel.

**Output del paso**

- **Tipo:** Estructura de contenido (11 bloques) para 5 SO.
- **Ejemplo (Cerrajeros Madrid 24h):** 5 URLs SO (`/cerrajero/{service}/`) con 11 bloques cada una.

### 6.8 — Location-Based Service Content Architecture

<small>§6.8</small>

**Explicación**

Define la arquitectura interna de las 5 LBS — el **corazón comercial** del cluster. Combina servicio + Main City + cobertura local. Es donde la conversión sucede, donde los clientes potenciales aterrizan tras una búsqueda local.

**Estructura completa (12 bloques)**

```text
1. H1 (servicio + Main City)
2. Intro local 100–150 words (mencionando 2-4 LCAs naturalmente)
3. Quick Local Answer
4. H2 Authority
5. H2 Uniqueness
6. H2 Depth
7. H2 Local Pain Points (problemas frecuentes en Main City + LCAs)
8. H2 Local Coverage Areas Served (sección dedicada de cobertura)
9. H2 Related Services in [Main City] (link a otras LBS Madrid)
10. FAQs (2-3 con cobertura natural)
11. CTA + Enlaces internos (Paso-07 7.5)
12. Schema (LocalBusiness + BreadcrumbList con areaServed)
```

**Uso de Local Coverage Areas**

**Sí se usan** Local Coverage Areas. Deben aparecer **de forma natural** en la intro, en una sección de cobertura, en ejemplos locales y en FAQs. La página sigue siendo de Main City, no de cada área mencionada.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
URL: /cerrajero/madrid/cerrajero-urgente/
H1: "Cerrajero urgente en Madrid"

Intro local (100-150w):
"Cerrajeros Madrid 24h ayuda a clientes en Madrid con aperturas
urgentes, llaves rotas y problemas de acceso. También atendemos
zonas de cobertura como Almagro, Chamberí, Salamanca y Retiro
cuando el servicio está disponible..."

H2: Ayuda de cerrajero urgente en Madrid y áreas de cobertura local
Texto: "...también cubrimos Local Coverage Areas como Almagro,
Chamberí, Salamanca y Retiro según disponibilidad."

FAQ:
P: ¿Ofrecéis cerrajero urgente en Almagro y Chamberí?
R: "Sí, atendemos esas zonas según disponibilidad, mientras esta
   página sigue enfocada en el servicio de cerrajero urgente en Madrid."
```

**Ejemplos incorrectos**

```text
- H1: "Cerrajero urgente en Almagro, Madrid y Salamanca" (canibaliza)
- Crear un párrafo por cada zona con texto duplicado
- Affirmar oficina en Retiro (falsa ubicación)
- Link a /almagro/ when that URL does not exist
- Mencionar 10 LCAs en el H1 (keyword stuffing)
```

**Regla final**

```text
Una Location-Based Service Page menciona cobertura local sin dejar de ser service + Main City.
```

**Validación operativa**

La LBS debe abrir con una intro localizada de 100–150 palabras. Aquí se puede mencionar 2–4 LCAs de forma natural si refuerzan el contexto, pero sin desplazar la Main City. Las páginas locales pueden incluir una sección específica de cobertura (H2 dedicado). Esta sección permite mencionar barrios, distritos o municipios seleccionados como señales GEO sin crear páginas propias ni URLs artificiales.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la arquitectura de 12 bloques a cada LBS. Incluir H2 Local Coverage Areas Served con 2-4 LCAs naturales. FAQs con cobertura natural (Paso 6.16). Schema LocalBusiness con `areaServed` poblado (Paso 6.17).

**Output del paso**

- **Tipo:** Estructura de contenido (12 bloques) para 5 LBS.
- **Ejemplo (Cerrajeros Madrid 24h):** 5 URLs LBS (`/cerrajero/madrid/{service}/`) con 12 bloques cada una.

### 6.9 — Additional Category Content Architecture

<small>§6.9</small>

**Explicación**

Define la arquitectura interna de las páginas de **categoría adicional** (AC). Las AC apoyan categorías GBP secundarias que no encajan como core service. Necesitan presencia local pero NO el mismo peso que las LBS.

**Estructura completa (11 bloques)**

```text
1. H1 (categoría adicional + Main City)
2. Intro con problema local (escenarios donde aplica el servicio)
3. H2 Authority
4. H2 Uniqueness
5. H2 Depth
6. H2 Intent
7. H2 Optimization
8. Local Coverage Use Case (escenarios locales con 2-4 LCAs)
9. FAQs (sobre la categoría adicional + cobertura)
10. CTA + Enlaces internos (link a GeoHub + LBS relacionados — Paso-07 7.6)
11. Schema (Service + BreadcrumbList)
```

**Uso de Local Coverage Areas**

Las LCAs se usan para **explicar casos de uso locales** relacionados con la categoría adicional. NO deben crear páginas propias si no están aprobadas como AEA.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
URL: /cerrajero/madrid/duplicado-llaves/
H1: "Duplicado de llaves experto en Madrid"

H2: Duplicado de llaves en zonas de cobertura de Madrid
Texto: "Clientes en Madrid y zonas como Almagro, Chamberí y
Salamanca pueden necesitar llaves de repuesto para familiares,
empleados, inquilinos o accesos urgentes."

Enlaces:
  /madrid/                                            (GeoHub)
  /cerrajero/madrid/cambio-cerraduras/                (LBS related)
  /cerrajero/madrid/instalacion-cerraduras-seguridad/ (LBS related)
```

**Ejemplos incorrectos**

```text
- Crear /cerrajero/almagro/duplicado-llaves/ sin aprobación
- No conectar con GeoHub
- Tratar duplicado de llaves como servicio core (es categoría adicional)
- Copiar contenido de la página de cambio de bombines (canibalización)
```

**Regla final**

```text
La categoría adicional se contextualiza localmente, pero no se multiplica por zonas no aprobadas.
```

**Validación operativa**

Las páginas de categorías adicionales deben usar LCAs solo cuando ayuden a explicar escenarios reales del servicio. El foco sigue siendo servicio adicional + Main City. Validar que la AC enlaza a GeoHub + LBS relacionados (Paso-07 7.6).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la arquitectura de 11 bloques a cada AC efectiva (Paso-01 1.6 + Paso-02 2.7 → A=1 para Cerrajeros). Usar LCAs como escenarios donde aplica el servicio adicional.

**Output del paso**

- **Tipo:** Estructura de contenido (11 bloques) para A AC efectivas.
- **Ejemplo (Cerrajeros Madrid 24h):** 1 URL AC (`/cerrajero/madrid/duplicado-llaves/`) con 11 bloques.

### 6.10 — GeoHub Content Architecture

<small>§6.10</small>

**Explicación**

Define la arquitectura interna del GeoHub Main City — el **índice geográfico** del cluster. El GeoHub es el lugar más natural para una sección explícita de Local Coverage Areas. Aquí se puede explicar la cobertura de la empresa con todas las LCAs declaradas, sin crear URLs por cada zona.

**Estructura completa (10 bloques)**

```text
1. H1 (Brand + Service + Main City)
2. City intro (presentación de la ciudad y servicio)
3. Menú de servicios (5 LBS links con descripción breve)
4. Additional Category Menu (AC links si A>0)
5. Local Coverage Areas Section (TODAS las LCAs declaradas — Direct + Candidate)
6. GeoArticle Resources (15 GAs listados como recursos)
7. Trust Signals (4-5 globales)
8. CTA
9. Enlaces internos (21 outbound según Paso-07 7.4)
10. Schema (CollectionPage + BreadcrumbList con areaServed completo)
```

**Uso de Local Coverage Areas**

El GeoHub es el lugar **más natural para una sección explícita** de Local Coverage Areas. Aquí se puede explicar la cobertura de la empresa SIN crear URLs por cada zona. Es la "casa" semántica de las LCAs.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
URL: /madrid/
H1: "Cerrajeros Madrid 24h – Servicios de cerrajería en Madrid"

H2: Zonas de cobertura de cerrajería en Madrid

Texto: "Cerrajeros Madrid 24h ofrece servicios de cerrajería en
Madrid con cobertura en zonas como Almagro, Chamberí, Salamanca,
Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa y Prosperidad.
Estas áreas son señales GEO seleccionadas por proximidad y
coherencia, y ayudan al usuario a entender dónde puede estar
disponible el servicio."

Menú de servicios:
  - Cerrajero urgente
  - Apertura de puertas
  - Cambio de cerraduras
  - Cambio de bombines
  - Instalación de cerraduras de seguridad
```

**Ejemplos incorrectos**

```text
- GeoHub sin lista de servicios (solo texto de ciudad)
- GeoHub como artículo sobre la ciudad (sin estructura de hub)
- Enlaces a áreas inexistentes (anchors a /almagro/)
- Cobertura local escrita como si hubiese oficinas en cada zona
- GeoHub sin enlace a GeoArticles (silo desconectado)
```

**Regla final**

```text
El GeoHub organiza Main City, servicios y cobertura local real.
```

**Validación operativa**

El GeoHub es el mejor lugar para explicar la cobertura local. Debe tener una sección clara de áreas de posicionamiento local (Direct y Candidate LCA), conectada con servicios y sin transformar cada zona en URL si no está aprobada. Validar que enlaza a TODAS las LBS, AC y GAs (Paso-07 7.4).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la arquitectura de 10 bloques al GeoHub. Listar TODAS las LCAs (Direct + Candidate) en sección dedicada. Enlazar a TODAS las páginas locales (5 LBS + A AC + G×S GAs). Schema CollectionPage con areaServed completo.

**Output del paso**

- **Tipo:** Estructura de contenido (10 bloques) para 1 GeoHub Main City.
- **Ejemplo (Cerrajeros Madrid 24h):** 1 URL (`/madrid/`) con los 10 bloques.

### 6.11 — GeoArticle Content Architecture

<small>§6.11</small>

**Explicación**

Define la arquitectura interna de los 15 GeoArticles (G×S=15). Los GAs son **boosters semánticos** que aportan profundidad temática + señales locales. NO son landings comerciales — son contenido de soporte que enlaza a la LBS comercial.

**Estructura completa (10 bloques)**

```text
1. H1 (long-tail topic + opcionalmente Main City)
2. Intro contextual (problema/pregunta del usuario)
3. H2 Problem (descripción del problema)
4. H2 Local Context (Madrid + LCAs como contexto)
5. H2 Options / Mistakes (opciones reales o errores comunes)
6. H2 When to Call (cuándo llamar al cerrajero)
7. H2 Local Examples (ejemplos con LCAs como landmarks)
8. FAQs (3-4 sobre el topic con menciones locales naturales)
9. CTA + Enlaces internos (link a matching LBS — Paso-07 7.7)
10. Schema (Article + FAQPage + BreadcrumbList)
```

**Uso de Local Coverage Areas**

Las LCAs se usan como **ejemplos semánticos y contexto real**. NO se usan para fingir presencia física ni para crear intención principal distinta. La intención principal sigue siendo el topic + matching LBS.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
URL: /madrid/cuanto-cuesta-un-cerrajero-urgente/
H1: "¿Cuánto cuesta un cerrajero urgente en Madrid?"

Texto:
"El precio de un cerrajero urgente en Madrid puede variar según
el tipo de cerradura, la hora, la urgencia y la zona de cobertura.
Una apertura sencilla en un piso de Madrid puede ser diferente de
un aviso nocturno en Almagro, Chamberí o Salamanca según
disponibilidad y condiciones de desplazamiento."

Enlaces:
  /cerrajero/madrid/cerrajero-urgente/        (matching LBS — Paso-07 7.7)
  /madrid/                                    (GeoHub)
  /madrid/que-hacer-si-no-puedes-entrar-casa/ (related GA opcional)
```

**Ejemplos incorrectos**

```text
- Article targeting Almagro as primary location without page
- No link to service page (matching LBS)
- Fake office statement (afirma presencia física en LCA)
- Article written as sales landing (debería ser informacional)
- GA huérfano (sin matching LBS asignado)
```

**Regla final**

```text
GeoArticles use local coverage as context and send authority back to the Main City service page.
```

**Validación operativa**

Los GeoArticles pueden usar LCAs como ejemplos semánticos: tipos de vivienda, zonas cercanas, landmarks o escenarios. Eso ayuda a NLP y AIO sin convertir el artículo en página de zona. Validar que cada GA enlaza a su matching LBS + GeoHub (Paso-07 7.7).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la arquitectura de 10 bloques a cada GA (G×S=15 para Cerrajeros). Usar LCAs como ejemplos semánticos en H2 Local Context y H2 Local Examples. Enlazar a matching LBS para transferir autoridad.

**Output del paso**

- **Tipo:** Estructura de contenido (10 bloques) para G×S GAs.
- **Ejemplo (Cerrajeros Madrid 24h):** 15 URLs GA (`/madrid/{topic}/`) con 10 bloques cada una.

### 6.12 — Tabla de uso de LCAs por page type

<small>§6.12</small>

**Explicación**

Output consolidado que documenta cómo se usan las Local Coverage Areas en cada uno de los 6 page types. Es una matriz de referencia para QA y para el implementador del contenido — sirve para validar que cada page type usa las LCAs según el patrón documentado.

**Patrón (matriz consolidada 6×2)**

| Page Type | ¿Usa LCAs? | Cómo las usa |
|---|---|---|
| Homepage | Sí, ligero | Service area preview |
| Service Overview | No | No debe ser local |
| Location-Based Service | Sí | Intro, pain points, cobertura, FAQs |
| Additional Category | Sí | Escenarios locales y cobertura |
| GeoHub | Sí, recomendado | Sección principal de cobertura local |
| GeoArticle | Sí | Ejemplos, contexto, landmarks, FAQs |

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Consolidar los outputs 6.6-6.11 (content architectures) en una tabla 6×2 que resume el uso de LCAs por page type. Es un output derivado.

**Output del paso**

- **Tipo:** Matriz 6×2 de uso de LCAs por page type.
- **Ejemplo (Cerrajeros Madrid 24h):** Tabla aplicada a las 28 URLs del cluster (1 Homepage + 5 SO + 1 GeoHub + 5 LBS + 1 AC + 15 GAs).

### 6.13 — Ejemplo práctico completo

<small>§6.13</small>

**Explicación**

Output ejemplar que muestra una sección de cobertura redactada completamente para una LBS modelo de Cerrajeros Madrid 24h. Sirve como template visual para que la IA pueda replicar la estructura en otras LBS del cluster (5 servicios) y en GeoArticles, GeoHub.

**Patrón (set ejemplar para LBS modelo)**

```text
Main City: Madrid
Service: Cerrajero urgente
Direct LCAs: Almagro, Chamberí
Candidate LCAs: Salamanca, Retiro, Centro, Tetuán, Chamartín,
                Arganzuela, Moncloa, Prosperidad

URL: /cerrajero/madrid/cerrajero-urgente/

Sección H2: Cerrajero urgente en Madrid y zonas de cobertura cercanas

Texto:
"Cerrajeros Madrid 24h ayuda a clientes en Madrid con aperturas
urgentes, llaves rotas, cambios de bombín y problemas de acceso.
También cubrimos Local Coverage Areas como Almagro, Chamberí,
Salamanca y Retiro según disponibilidad. Estas zonas son señales
GEO de proximidad que refuerzan la relevancia local mientras la
página sigue enfocada en el servicio de cerrajero urgente en Madrid."
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Tomar la LBS principal del cluster (cerrajero-urgente Madrid) y aplicar el output 6.8 (LBS Content Architecture) para generar el set ejemplar. Documentar como template para que la IA lo replique en las otras 4 LBS + AC + GAs.

**Output del paso**

- **Tipo:** Texto modelo redactado (sección de cobertura para LBS).
- **Ejemplo (Cerrajeros Madrid 24h):** Texto ejemplar para `/cerrajero/madrid/cerrajero-urgente/`.

### 6.14 — FAQ ejemplo

<small>§6.14</small>

**Explicación**

Output ejemplar que muestra una FAQ con cobertura natural para LBS o GeoHub. Sirve como template visual para que la IA pueda replicar la estructura en las FAQs de cada page type, asegurando que las menciones de LCAs son naturales (sin keyword stuffing).

**Patrón (FAQ ejemplar)**

```text
Pregunta:
[Pregunta real del usuario que mencione naturalmente cobertura]

Respuesta:
[Respuesta que confirma cobertura sin afirmar oficina física,
 que mantiene foco en Main City + servicio principal]
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Pregunta:
¿Ofrecéis cerrajero urgente en Almagro, Chamberí y Salamanca?

Respuesta:
Sí. Cerrajeros Madrid 24h atiende clientes en Madrid y zonas de
cobertura como Almagro, Chamberí y Salamanca según disponibilidad.
Esta página se centra en el servicio de cerrajero urgente en Madrid
y aclara la cobertura local real.
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Generar 1-2 FAQs ejemplares por LBS y GeoHub que muestren la pauta correcta: pregunta natural sobre cobertura + respuesta que confirma sin inventar oficina física.

**Output del paso**

- **Tipo:** Plantilla de FAQ con cobertura natural.
- **Ejemplo (Cerrajeros Madrid 24h):** FAQ ejemplar documentada para LBS de cerrajero urgente.

### 6.15 — Reviews y trust blocks contextualizados (cross-cutting)

<small>§6.15</small>

**Explicación**

Las reseñas y señales de confianza deben colocarse donde apoyan la intención de cada page type: homepage (entidad global), landings locales (LBS — pruebas locales), GeoHub (autoridad ciudad) y, ocasionalmente, artículos. NO deben inventarse ni repetirse como bloque genérico sin contexto. Los trust signals heredados del Paso-01 1.14 NO son uniforme cross-cluster.

**Patrón o fórmula**

```text
Trust signal → sección adecuada según funnel position → servicio o Main City

Por page type:
  Homepage         → 4 trust signals globales (entidad)
  Service Overview → no críticos (pilar temático)
  GeoHub           → 4-5 trust signals globales (autoridad ciudad)
  LBS              → 3 trust signals + reviews iniciales pendientes
  Additional Cat.  → similar a LBS
  GeoArticle       → 1-2 trust signals si encajan
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h usa "reseñas iniciales pendientes de
recopilar tras crear el GBP" en homepage y en LBS principales
como prueba local pendiente de validar.

Trust signals heredados (Paso-01 1.14):
  - 10+ años de experiencia
  - Técnicos cerrajeros cualificados
  - Servicio móvil en el mismo día
  - Garantía de trabajo
  - Reseñas iniciales pendientes (post-Paso 14)
```

**Ejemplos incorrectos**

```text
- Pegar el mismo bloque de reseñas en todas las páginas sin contexto
- Usar reseñas de una zona como si fueran de otra
- Inventar certificaciones (E-E-A-T comprometido)
- Reviews schema sin reviews reales (riesgo Google penalty)
```

**Regla final**

```text
Reviews y trust blocks van en cada page type según su rol del funnel; no son uniforme cross-cluster.
```

**Validación operativa**

Aplicar la regla en cada page type del Bloque III como filtro de QA antes de cerrar la spec del cluster. Validar que los trust signals están adaptados al rol de cada page type, no copiados uniformemente.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la regla en cada page type del Bloque III como filtro de QA. Mapear los Trust Signals heredados (Paso-01 1.14) al page type donde aportan más (homepage, GeoHub, LBS).

**Output del paso**

- **Tipo:** Validation flag — la regla se cumple en todas las page types.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado en las 6 page types del Bloque III.

### 6.16 — FAQs con cobertura natural (cross-cutting)

<small>§6.16</small>

**Explicación**

Las FAQs pueden mencionar Local Coverage Areas si responden preguntas reales de usuarios. Deben sonar naturales y NO funcionar como keyword stuffing de zonas. Una FAQ por cada zona sin valor nuevo es spam temático.

**Patrón o fórmula**

```text
Pregunta real (búsqueda real del usuario) → Main City + cobertura → respuesta útil

NO: una FAQ por LCA con texto repetido cambiando solo el nombre
SÍ: FAQs que agrupan zonas si la respuesta es similar
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
P: ¿Atendéis emergencias de cerrajería en Almagro y Chamberí?
R: "Sí, Cerrajeros Madrid 24h atiende solicitudes en Madrid y
   zonas de cobertura cercanas según disponibilidad."
```

**Ejemplos incorrectos**

```text
- Crear una FAQ por cada zona sin valor nuevo (10 FAQs casi idénticas)
- Usar preguntas repetidas cambiando solo el área
- Responder con promesas de oficina inexistente
- FAQ keyword-stuffed con 8 LCAs concatenadas
```

**Regla final**

```text
Las FAQs incorporan menciones de cobertura naturales — sin forzar la zona en cada respuesta.
```

**Validación operativa**

Aplicar la regla en cada page type que tenga FAQs (Homepage, LBS, AC, GeoHub, GAs). Validar que las FAQs son naturales y NO repetitivas. Cruce con Paso-08 (FAQPage schema) — solo FAQs que aportan valor entran al schema.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la regla en cada page type del Bloque III como filtro de QA antes de cerrar la spec del cluster. Validar que cada FAQ tiene una pregunta real y una respuesta útil, sin repetición artificial.

**Output del paso**

- **Tipo:** Validation flag — la regla se cumple en todas las page types con FAQs.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado en Homepage (4 FAQs), LBS (2-3 FAQs), GeoHub, GAs.

### 6.17 — Schema `areaServed` coherente (cross-cutting)

<small>§6.17</small>

**Explicación**

Las Local Coverage Areas pueden reflejarse en el campo `areaServed` del schema LocalBusiness si representan cobertura real. El schema debe diferenciar **cobertura** (areaServed) de **dirección física** (address) y NO añadir áreas falsas solo por SEO.

**Patrón o fórmula**

```text
Real coverage → areaServed (lista de Place objects)
Physical address → address (1 dirección única, NAP-compatible)

areaServed = [Main City] + [TODAS las LCAs declaradas]
address = NAP físico real (Paso-01 1.4 + 1.8)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Schema LocalBusiness:
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Calle Rafael Calvo 12",
    "addressLocality": "Madrid",
    "postalCode": "28010",
    "addressCountry": "ES"
  },
  "areaServed": [
    "Madrid",          (Main City)
    "Almagro",         (Direct LCA)
    "Chamberí",        (Direct LCA)
    "Salamanca",       (Candidate LCA)
    "Retiro",          (Candidate LCA)
    "Centro", "Tetuán", "Chamartín",
    "Arganzuela", "Moncloa", "Prosperidad"
  ]
```

**Ejemplos incorrectos**

```text
- Poner Almagro como address sin sede (falsa ubicación)
- Añadir ciudades no atendidas en areaServed (Valencia, Barcelona)
- Omitir areaServed si la cobertura es clave (señal débil)
- areaServed con solo Madrid sin las LCAs declaradas
```

**Regla final**

```text
El campo `areaServed` del schema LocalBusiness lista TODAS las LCAs declaradas + Main City.
```

**Validación operativa**

Aplicar la regla en cada page type que use schema LocalBusiness (Homepage, LBS, GeoHub). Validar que `areaServed` lista TODAS las LCAs declaradas en Paso-01 1.10 y que el `address` corresponde al NAP físico real (Paso-01 1.4). Cruce con Paso 8 (Schema Markup).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la regla en cada page type del Bloque III como filtro de QA antes de cerrar la spec del cluster. Generar `areaServed` con la lista completa de LCAs heredadas + Main City. Mantener `address` como NAP físico único.

**Output del paso**

- **Tipo:** Validation flag — la regla se cumple en todas las page types con schema LocalBusiness.
- **Ejemplo (Cerrajeros Madrid 24h):** Validado — `areaServed` con Madrid + 10 LCAs en homepage, LBS y GeoHub.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 6 y avanzar al Paso 7 (Internal Linking).

### Validación de principios

- ☐ Principio 1 — Main City crea arquitectura (6.1)
- ☐ Principio 2 — LCAs enriquecen contenido sin URL (6.2)
- ☐ Principio 3 — AEAs crean URLs solo si se aprueban (6.3)
- ☐ Principio 4 — Mencionar zona ≠ crear página (6.4)
- ☐ Principio 5 — No falsa ubicación (6.5)

### Validación de content architectures

- ☐ Homepage con 11 bloques + 3-5 LCAs ligeras (6.6)
- ☐ Service Overview con 11 bloques sin Main City como target (6.7)
- ☐ LBS con 12 bloques incluyendo H2 LCA Section (6.8)
- ☐ Additional Category con 11 bloques + Local Use Case (6.9)
- ☐ GeoHub con 10 bloques + sección completa de LCAs (6.10)
- ☐ GeoArticle con 10 bloques + LCAs como ejemplos (6.11)

### Validación de outputs auxiliares

- ☐ Tabla de uso de LCAs por page type documentada (6.12)
- ☐ Ejemplo práctico completo redactado (6.13)
- ☐ FAQ ejemplo con cobertura natural (6.14)

### Validación cross-cutting

- ☐ Reviews y trust blocks contextualizados por page type (6.15)
- ☐ FAQs con cobertura natural sin repetición (6.16)
- ☐ Schema `areaServed` coherente con TODAS las LCAs (6.17)

## Outputs Consolidados

<small>§8</small>

> Tabla final con valores reales para Cerrajeros Madrid 24h y status de cada output. Los IDs (`6.1`–`6.17`) coinciden con los declarados en §5.

| ID | Output | Valor (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|
| 6.1 | Principio 1 — Main City crea arquitectura | Madrid es la única Main City del cluster | OK |
| 6.2 | Principio 2 — LCAs enriquecen contenido | 10 LCAs en contenido + areaServed; 0 URLs `/{lca}/` | OK |
| 6.3 | Principio 3 — AEAs crean URLs solo si se aprueban | E=0 → 0 URLs de expansión | OK |
| 6.4 | Principio 4 — Mencionar zona ≠ crear página | Almagro mencionado en LBS sin enlace a `/almagro/` | OK |
| 6.5 | Principio 5 — No falsa ubicación | NAP=Madrid; ninguna afirmación de oficina en LCAs | OK |
| 6.6 | Homepage Content Architecture | 1 URL (`/`) con 11 bloques | confirmed |
| 6.7 | Service Overview Content Architecture | 5 URLs SO con 11 bloques cada una | confirmed |
| 6.8 | Location-Based Service Content Architecture | 5 URLs LBS con 12 bloques cada una | confirmed |
| 6.9 | Additional Category Content Architecture | 1 URL AC con 11 bloques | confirmed |
| 6.10 | GeoHub Content Architecture | 1 URL (`/madrid/`) con 10 bloques | confirmed |
| 6.11 | GeoArticle Content Architecture | 15 URLs GA con 10 bloques cada una | confirmed |
| 6.12 | Tabla de uso de LCAs por page type | Matriz 6×2 documentada | confirmed |
| 6.13 | Ejemplo práctico completo | Texto modelo para LBS Cerrajero urgente Madrid | confirmed |
| 6.14 | FAQ ejemplo | Plantilla FAQ con cobertura natural | confirmed |
| 6.15 | Reviews y trust blocks contextualizados | Trust signals adaptados al funnel por page type | OK |
| 6.16 | FAQs con cobertura natural | FAQs naturales sin keyword stuffing en LBS, GeoHub, GAs | OK |
| 6.17 | Schema `areaServed` coherente | `areaServed` con Madrid + 10 LCAs en LocalBusiness | OK |

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
