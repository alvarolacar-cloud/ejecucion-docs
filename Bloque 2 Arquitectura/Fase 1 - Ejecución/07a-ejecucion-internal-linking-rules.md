Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# Paso 7 — Internal Linking Rules

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 15 outputs del Paso 7 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, obtención de outputs, checklist final y outputs consolidados.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 7

<small>§2</small>

Definir **cómo se conectan internamente las páginas del cluster** mediante reglas de enlace, anchors variados y breadcrumbs jerárquicos. Establece qué páginas enlazan a qué, qué anchors usar, dónde colocar los enlaces (contextual vs nav/footer) y qué Local Coverage Areas reciben enlace (solo si tienen URL aprobada). El silo local resultante debe ser navegable por usuario y crawler sin páginas huérfanas ni enlaces a URLs inexistentes.

**Outputs del paso:**

- **7.1** Regla 1 — Enlazar arriba/abajo/lateral: cada página tiene up + down + lateral links dentro del silo
- **7.2** Regla 2 — Homepage distribuye autoridad: enlaza a 5 SO + GeoHub Main City + contacto + AC principal
- **7.3** Regla 3 — Service Overview empuja la versión local: cada SO enlaza a su LBS Main City correspondiente
- **7.4** Regla 4 — GeoHub organiza la Main City: enlaza a todas las páginas locales (LBS, AC, GAs)
- **7.5** Regla 5 — LBS conecta servicio y ciudad: enlaza a SO padre, GeoHub, related LBS, GeoArticles
- **7.6** Regla 6 — Additional Category se integra en el silo local: enlaza a GeoHub + LBS relacionados
- **7.7** Regla 7 — GeoArticle pasa relevancia a la landing: enlaza a matching LBS + GeoHub
- **7.8** Regla 8 — LCAs sin URL no reciben enlaces: solo menciones de contenido, nunca anchors a URLs inexistentes
- **7.9** Regla 9 — Anchor text variado: exact match + partial + branded + CTA + informational + local entity
- **7.10** Regla 10 — Enlaces contextuales primero: body > nav/footer; placement en intro, FAQs, related resources
- **7.11** Matriz de enlaces obligatorios por page type — 14 conexiones source → target documentadas
- **7.12** Ejemplo completo de enlaces para LBS modelo — set inbound/outbound + anchors
- **7.13** Breadcrumbs por page type — jerarquía 6 page types (Home > Cat > City > Service)
- **7.14** Inbound links esperados (cross-cutting) — cada page type tiene mapa de inbound mínimo
- **7.15** Expansion linking separado (cross-cutting) — AEAs crean sub-cluster propio sin contaminar la base

**Errores que previene:**

- Páginas sin enlaces a su padre (huérfanas en el silo)
- Enlaces a Local Coverage Areas sin URL aprobada (anchors rotos a `/almagro/` inexistente)
- Solo enlaces de footer sin contextuales en body (señal débil)
- Anchor text repetido / 100% exact match (apariencia mecánica, riesgo manual penalty)
- GeoArticles sin enlace a la landing comercial (artículo no cumple función booster)
- GeoHub sin enlaces a páginas locales (no organiza el silo Main City)
- Service Overview sin enlace a su LBS local (no transfiere autoridad temática)
- Expansion linking mezclado con la base (sub-cluster contamina el silo principal)
- Breadcrumbs que inventan niveles de cobertura inexistentes

**Cuándo se ejecuta:** Después del Paso 6 (Estructura de Contenido). El Paso 6 define qué se escribe en cada page type; el Paso 7 define cómo esas páginas se conectan entre sí. El output del Paso 7 alimenta directamente el Paso 8 (Schema Markup) — `WebPage.breadcrumb`, `Article.mentions`, `Service.areaServed` — y el Paso 18 (QA + deploy) usa la matriz de inbound links como referencia de validación.

## Info heredada de pasos anteriores

<small>§3</small>

> Estos campos NO se deciden en Paso 7 — la IA los lee del paso indicado y los usa como input para construir la matriz de enlaces internos del cluster.

| # | Input heredado | Origen | Uso en el Paso 7 |
|---|---|---|---|
| 1 | Business Name | Paso-01 1.1 | Anchors de marca (branded anchors) |
| 2 | Website URL / Canonical Domain | Paso-01 1.2 + Paso-04 4.1 | Confirmar dominio único en todos los enlaces internos absolutos |
| 3 | Homepage URL (`/`) | Paso-04 4.3 | Source de enlaces a SO + GeoHub + contacto |
| 4 | Primary Category Slug | Paso-02 2.2 | Segmento `[primary-cat-slug]` en URLs de los enlaces |
| 5 | Main City + slug | Paso-01 1.7 + Paso-02 2.3 | Anchors locales y target geográfico del silo |
| 6 | URL Matrix (28 URLs base) | Paso-03 3.5 | Conjunto cerrado de URLs disponibles para enlazar |
| 7 | Service Overview Pages (S=5) | Paso-04 4.4 + Paso-03 3.5 | Source y target de enlaces SO ↔ LBS |
| 8 | Location-Based Service Pages (S=5) | Paso-04 4.6 + Paso-03 3.5 | Hub principal de enlaces salientes (SO padre, GeoHub, related LBS, GAs) |
| 9 | Additional Category Pages (A=1 efectiva) | Paso-04 4.7 + Paso-03 3.5 | Source/target dentro del silo local |
| 10 | Main City GeoHub (`/madrid/`) | Paso-04 4.5 + Paso-03 3.5 | Hub central que enlaza a todas las páginas locales |
| 11 | GeoArticle Pages (G×S=15) | Paso-04 4.8 + Paso-03 3.5 | Boosters semánticos que enlazan a matching LBS |
| 12 | Local Coverage Areas (Direct + Candidate) | Paso-01 1.10 | Mencionadas en contenido SIN enlace (no tienen URL) |
| 13 | Approved Expansion Areas (E count) | Paso-01 1.11 | Si E≥1 → sub-cluster de linking separado (7.15); E=0 → no aplica |
| 14 | Page Type assignment por URL | Paso 5 (Page Type Rules) | Determina qué reglas de enlace (7.1–7.10) aplican a cada URL |
| 15 | Page-level anchors (CTA, informational, local) | Paso 5 + Paso 6 cross-cutting | Inputs para el catálogo de anchors variados (7.9) |
| 16 | Página de contacto URL (`/contacto/`) | Paso-01 1.4 (NAP — Phone/Email) + Paso-03 3.5 (auxiliar) | Target de CTA desde homepage y todas las LBS |

# Bloque II — Ejemplo rellenado para el Paso 7 — Internal Linking Rules

<small>§4</small>

> Los 15 outputs del Paso 7 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 7.X declarado en §5.

### 7.1 — Regla 1 (Enlazar arriba/abajo/lateral)

Aplicada a todas las 28 URLs del cluster. Cada página tiene mínimo 1 enlace up + 1 down/lateral.

### 7.2 — Regla 2 (Homepage distribuye autoridad)

Homepage `/` enlaza a:
- 5 Service Overview Pages (`/cerrajero/{service}/`)
- 1 Main City GeoHub (`/madrid/`)
- 1 Additional Category (`/cerrajero/madrid/duplicado-llaves/`)
- 1 Página de contacto (`/contacto/`)

Total: **8 outbound mínimos desde Homepage**.

### 7.3 — Regla 3 (SO empuja la versión local)

5 conexiones SO → LBS:
- `/cerrajero/cerrajero-urgente/` → `/cerrajero/madrid/cerrajero-urgente/`
- `/cerrajero/apertura-puertas/` → `/cerrajero/madrid/apertura-puertas/`
- `/cerrajero/cambio-cerraduras/` → `/cerrajero/madrid/cambio-cerraduras/`
- `/cerrajero/cambio-bombines/` → `/cerrajero/madrid/cambio-bombines/`
- `/cerrajero/instalacion-cerraduras-seguridad/` → `/cerrajero/madrid/instalacion-cerraduras-seguridad/`

### 7.4 — Regla 4 (GeoHub organiza Main City)

`/madrid/` enlaza a:
- 5 LBS (`/cerrajero/madrid/{service}/`)
- 1 AC (`/cerrajero/madrid/duplicado-llaves/`)
- 15 GeoArticles (`/madrid/{topic}/`)

Total: **21 outbound desde GeoHub**.

### 7.5 — Regla 5 (LBS conecta servicio y ciudad)

Cada LBS enlaza a:
- 1 SO padre (related Service Overview)
- 1 GeoHub Main City
- 2-3 related LBS (mismo cluster local)
- 3 matching GeoArticles (cada GA del servicio)

Total: **6-7 outbound por LBS** (×5 LBS = 30-35 enlaces total).

### 7.6 — Regla 6 (AC se integra en silo local)

`/cerrajero/madrid/duplicado-llaves/` enlaza a:
- `/madrid/` (GeoHub)
- `/cerrajero/madrid/cambio-cerraduras/` (LBS relacionado)
- `/cerrajero/madrid/instalacion-cerraduras-seguridad/` (LBS relacionado)

### 7.7 — Regla 7 (GeoArticle pasa relevancia a landing)

15 conexiones GA → LBS (1 por GeoArticle). Ejemplo:
- `/madrid/cuanto-cuesta-un-cerrajero-urgente/` → `/cerrajero/madrid/cerrajero-urgente/` + `/madrid/`
- `/madrid/que-hacer-si-no-puedes-entrar-casa/` → `/cerrajero/madrid/cerrajero-urgente/` + `/madrid/`
- ... (resto análogo, cada GA enlaza a su matching LBS + GeoHub)

### 7.8 — Regla 8 (LCAs sin URL no reciben enlaces)

10 LCAs declaradas (Almagro, Chamberí, Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad) → 0 anchors `<a href="/almagro/">` (porque no existen como URLs aprobadas).

Aparecen como **menciones textuales** en contenido de LBS, GeoHub, GAs.

### 7.9 — Regla 9 (Anchor text variado)

6 categorías de anchor aplicadas para Cerrajeros:

| Categoría | Ejemplo |
|---|---|
| Exact match | `cerrajero urgente en Madrid` |
| Partial | `servicios de cerrajería` |
| Branded | `Cerrajeros Madrid 24h` |
| CTA | `Llama hoy` |
| Informational | `Conoce más sobre cerrajero urgente` |
| Local entity | `zonas de cobertura en Madrid` |

### 7.10 — Regla 10 (Enlaces contextuales primero)

Body links > nav/footer. Placement principal:
- Intro / opening paragraph
- FAQs (responses)
- Related resources sections
- CTA blocks

### 7.11 — Matriz de enlaces obligatorios por page type

14 conexiones source → target documentadas:

| # | Source Page | Target | Tipo de enlace | Cantidad (Cerrajeros Madrid 24h) |
|---|---|---|---|---|
| 1 | Homepage | Service Overview Pages | Top-of-funnel | 5 enlaces |
| 2 | Homepage | Main City GeoHub | Geo anchor | 1 enlace (`/madrid/`) |
| 3 | Homepage | Página de contacto | CTA conversión | 1 enlace |
| 4 | Service Overview | Main City LBS Page | Local push | 5 enlaces (1 por SO) |
| 5 | Service Overview | Related Services | Topical | 2-3 enlaces por SO |
| 6 | Main City GeoHub | All Main City Service Pages | Silo organization | 5 enlaces a LBS |
| 7 | Main City GeoHub | Additional Category Pages | GBP support | 1 enlace |
| 8 | Main City GeoHub | GeoArticles | Local resources | 15 enlaces |
| 9 | LBS | Parent Service Overview | Up (topical) | 1 enlace por LBS |
| 10 | LBS | Main City GeoHub | Up (geo) | 1 enlace por LBS |
| 11 | LBS | Related same-city services | Lateral | 2-3 enlaces por LBS |
| 12 | LBS | Matching GeoArticles | Down (depth) | 3 enlaces por LBS |
| 13 | GeoArticle | Matching LBS Page | Authority transfer | 1 enlace por GA |
| 14 | GeoArticle | Main City GeoHub | Geo anchor | 1 enlace por GA |

### 7.12 — Ejemplo completo de enlaces para LBS modelo

Source: `/cerrajero/madrid/cerrajero-urgente/` (LBS-1)

**Required outbound links (6):**
- `/cerrajero/cerrajero-urgente/` (SO padre)
- `/madrid/` (GeoHub)
- `/cerrajero/madrid/apertura-puertas/` (related LBS)
- `/cerrajero/madrid/cambio-cerraduras/` (related LBS)
- `/madrid/cuanto-cuesta-un-cerrajero-urgente/` (matching GA)
- `/contacto/` (CTA)

**Anchor suggestions:**
- "urgente servicios de cerrajería"
- "servicios de cerrajería en Madrid"
- "apertura de puertas en Madrid"
- "servicios de cambio de cerraduras en Madrid"
- "precio de cerrajero urgente en Madrid"
- "llama hoy a Cerrajeros Madrid 24h"

### 7.13 — Breadcrumbs por page type

| Page Type | Breadcrumb (Cerrajeros Madrid 24h) |
|---|---|
| Homepage | `Home` |
| Service Overview | `Home > Cerrajero > Cerrajero urgente` |
| Main City GeoHub | `Home > Madrid` |
| Location-Based Service | `Home > Cerrajero > Madrid > Cerrajero urgente` |
| Additional Category | `Home > Cerrajero > Madrid > Duplicado de llaves` |
| GeoArticle | `Home > Madrid > Cuánto cuesta un cerrajero urgente` |

### 7.14 — Inbound links esperados (cross-cutting)

Cada URL del cluster con mapa de inbound:
- LBS recibe enlaces de homepage, SO padre, GeoHub, GAs (4 inbound mínimos)
- GeoArticle recibe enlaces de GeoHub + LBS matching (2 inbound mínimos)
- AC recibe enlaces de GeoHub + Homepage (2 inbound mínimos)

**0 páginas huérfanas** detectadas en el cluster.

### 7.15 — Expansion linking separado (cross-cutting)

E=0 en Phase 1 → no aplica sub-cluster de expansión.

Si E≥1 (Phase 2+), AEAs crean su propio sub-cluster de linking aislado de la base.

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 15 outputs que el Paso 7 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `7.1`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 7.1 | Regla 1 — Enlazar arriba/abajo/lateral | Regla operativa | GMB Crush | — |
| 7.2 | Regla 2 — Homepage distribuye autoridad | Regla operativa | GMB Crush | Paso-03 3.5 |
| 7.3 | Regla 3 — SO empuja versión local | Regla operativa | GMB Crush | Paso-03 3.5 |
| 7.4 | Regla 4 — GeoHub organiza Main City | Regla operativa | GMB Crush | Paso-03 3.5 |
| 7.5 | Regla 5 — LBS conecta servicio y ciudad | Regla operativa | GMB Crush | Paso-03 3.5 |
| 7.6 | Regla 6 — AC se integra en silo local | Regla operativa | GMB Crush | Paso-03 3.5 |
| 7.7 | Regla 7 — GeoArticle pasa relevancia a landing | Regla operativa | GMB Crush | Paso-03 3.5 |
| 7.8 | Regla 8 — LCAs sin URL no reciben enlaces | Regla operativa | GMB Crush | Paso-01 1.10 + Paso-04 4.9 |
| 7.9 | Regla 9 — Anchor text variado | Catálogo de 6 categorías de anchor | GMB Crush | Paso-01 1.1 (branded) + Paso-01 1.13 (CTA) |
| 7.10 | Regla 10 — Enlaces contextuales primero | Regla de placement | GMB Crush | — |
| 7.11 | Matriz de enlaces obligatorios por page type | Tabla 14 conexiones | GMB Crush | Paso-03 3.5 |
| 7.12 | Ejemplo completo de enlaces para LBS modelo | Set inbound/outbound + anchors | GMB Crush | Paso-03 3.5 |
| 7.13 | Breadcrumbs por page type | Jerarquía por 6 page types | GMB Crush | Paso-03 3.5 |
| 7.14 | Inbound links esperados (cross-cutting) | Validation flag | GMB Crush | Paso-03 3.5 |
| 7.15 | Expansion linking separado (cross-cutting) | Regla operativa para E≥1 | GMB Crush | Paso-01 1.11 |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 15 outputs (7.1–7.15) con el patrón completo: Explicación / Patrón o fórmula / Ejemplos correctos / Ejemplos incorrectos / Regla final / Validación operativa / Cómo se obtiene / Output del paso. Cada sub-sección §6.X corresponde 1:1 al output 7.X declarado en §5.

### 7.1 — Regla 1: Enlazar hacia arriba, abajo y lateralmente

<small>§6.1</small>

**Explicación**

Cada página debe tener un enlace hacia su padre (up), hacia páginas hijas o de soporte (down), y hacia páginas relacionadas del mismo silo (lateral). Esto garantiza que ninguna página queda huérfana y que el flujo de autoridad recorra el cluster en las tres direcciones.

**Patrón o fórmula**

```text
up + down + lateral links
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS /cerrajero/madrid/cerrajero-urgente/ enlaza a:
  - /cerrajero/cerrajero-urgente/         (UP — SO padre)
  - /madrid/                              (UP — GeoHub geográfico)
  - /cerrajero/madrid/apertura-puertas/   (LATERAL — related LBS)
  - /madrid/cuanto-cuesta-un-cerrajero-urgente/  (DOWN — matching GA)
```

**Ejemplos incorrectos**

```text
- Página local sin link al servicio padre (only lateral)
- GeoArticle sin link a landing comercial (no DOWN)
- GeoHub sin links a servicios (no DOWN — silo roto)
- Página solo con menú/footer (no contextual links)
```

**Regla final**

```text
Todo enlace interno conecta vertical (arriba/abajo) o lateralmente, nunca aleatorio.
```

**Validación operativa**

Para cada page type, comprobar las 3 direcciones: up (a padre), down (a hijos/soporte), lateral (a hermanos del mismo silo). Si una dirección está vacía, revisar si es por diseño (ej. Homepage no tiene up) o falta enlace. Validación cruzada con 7.11 Matriz de enlaces obligatorios.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la regla generando los enlaces internos requeridos para cada page type según la matriz §6.11. Cada page type tiene sus 3 direcciones definidas en la matriz; la IA ejecuta el set para cada URL del cluster.

**Output del paso**

- **Tipo:** Regla operativa por page type.
- **Ejemplo (Cerrajeros Madrid 24h):** Aplicada a las 28 URLs del cluster — cada una con enlaces up/down/lateral según matriz §6.11.

### 7.2 — Regla 2: Homepage distribuye autoridad

<small>§6.2</small>

**Explicación**

La homepage es el punto de entrada principal del cluster y la página con mayor autoridad heredada. Debe enlazar explícitamente a las páginas más importantes: Service Overview Pages (top-of-funnel), GeoHub Main City (geo anchor), Additional Category principal y página de contacto. NO debe enlazar a todas las áreas de cobertura si no tienen URL.

**Patrón o fórmula**

```text
Homepage / → S Service Overview Pages
          + 1 Main City GeoHub
          + A Additional Category Pages (página principal o todas si pocas)
          + 1 Página de contacto
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/ enlaza a:
  - /cerrajero/cerrajero-urgente/
  - /cerrajero/apertura-puertas/
  - /cerrajero/cambio-cerraduras/
  - /cerrajero/cambio-bombines/
  - /cerrajero/instalacion-cerraduras-seguridad/
  - /madrid/
  - /cerrajero/madrid/duplicado-llaves/
  - /contacto/

Total: 8 outbound mínimos.
```

**Ejemplos incorrectos**

```text
- Homepage enlaza a 100 zonas (LCAs sin URL)
- Homepage no enlaza a servicios (sin SO)
- Homepage solo usa enlaces en footer (sin contextuales)
- Homepage enlaza a /almagro/ (LCA sin AEA)
- Homepage no enlaza al GeoHub
- Homepage solo enlaza al contacto
```

**Regla final**

```text
La Homepage debe enlazar a las S SO + GeoHub Main City + AC + contacto como punto de partida del cluster.
```

**Validación operativa**

La homepage debe enlazar a las páginas más importantes de la arquitectura base: Service Overview Pages, Main City GeoHub, Additional Category principal y contacto. No debe enlazar a todas las áreas de cobertura si no tienen URL. Validar contra Paso-03 3.5 (URL Matrix) que todas las URLs target existen.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Tomar la lista de URLs de la URL Matrix (Paso-03 3.5), filtrar SO + GeoHub + AC + contacto, y generar los enlaces internos contextuales en homepage. NO incluir URLs de LCAs sin AEA aprobada.

**Output del paso**

- **Tipo:** Regla operativa para homepage.
- **Ejemplo (Cerrajeros Madrid 24h):** 8 outbound desde `/` (5 SO + 1 GeoHub + 1 AC + 1 contacto).

### 7.3 — Regla 3: Service Overview empuja la versión local

<small>§6.3</small>

**Explicación**

Cada Service Overview Page (SO) debe enlazar a la versión Main City del servicio (LBS correspondiente) para transferir autoridad temática a la página comercial local. Sin ese enlace, la SO queda como pilar temático aislado y la LBS pierde contexto del servicio padre.

**Patrón o fórmula**

```text
/{primary-cat-slug}/{service-slug}/  →  /{primary-cat-slug}/{main-city-slug}/{service-slug}/
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
La página /cerrajero/cerrajero-urgente/ enlaza a /cerrajero/madrid/cerrajero-urgente/
con anchor "cerrajero urgente en Madrid".
```

**Ejemplos incorrectos**

```text
- Service Overview sin versión local
- Enlazar a /almagro/ sin expansión aprobada
- Enlazar solo a blog
- No enlazar a la versión local
- Enlazar a páginas de cobertura inexistentes
- Usar solo anchors genéricos como "haz clic aquí"
```

**Regla final**

```text
Cada Service Overview enlaza a su versión local correspondiente como puente al funnel.
```

**Validación operativa**

Cada Service Overview debe enlazar a la Location-Based Service Page de la Main City para transferir autoridad temática a la página comercial local. La S SO genera S conexiones SO → LBS (en el ejemplo: 5 conexiones).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Para cada Service Overview Page (S=5), generar 1 enlace a su LBS correspondiente. La relación es 1:1 entre SO y LBS según el patrón URL del Paso 4.

**Output del paso**

- **Tipo:** Regla operativa para Service Overview Pages.
- **Ejemplo (Cerrajeros Madrid 24h):** 5 conexiones SO → LBS (cada SO enlaza a su LBS Madrid).

### 7.4 — Regla 4: GeoHub organiza la Main City

<small>§6.4</small>

**Explicación**

El GeoHub Main City debe enlazar a TODAS las páginas locales del cluster: 5 LBS (servicios en Madrid), 1 AC (categoría adicional), 15 GAs (artículos del cluster). Es el índice de la Main City y el hub central de navegación local.

**Patrón o fórmula**

```text
/{main-city-slug}/  →  All Main City service pages + AC + GeoArticles
                    =  S LBS + A AC + (G × S) GeoArticles
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/madrid/ enlaza a:
  - 5 LBS (/cerrajero/madrid/cerrajero-urgente/, ...)
  - 1 AC (/cerrajero/madrid/duplicado-llaves/)
  - 15 GeoArticles (/madrid/cuanto-cuesta-un-cerrajero-urgente/, ...)
Total: 21 outbound desde GeoHub.
```

**Ejemplos incorrectos**

```text
- GeoHub sin service menu
- GeoHub enlaza a zonas sin URL
- GeoHub con solo texto
- GeoHub sin enlaces a servicios
- GeoHub enlaza a cobertura sin URLs aprobadas
- GeoHub solo tiene texto de ciudad
```

**Regla final**

```text
El GeoHub Main City enlaza a TODAS las páginas locales del cluster (LBS, AC, GAs).
```

**Validación operativa**

El GeoHub debe ser el índice de la Main City. Debe enlazar a todas las páginas servicio+ciudad, categorías adicionales y GeoArticles de esa ciudad. Si falta alguno, el silo Main City queda incompleto y la página correspondiente pierde inbound desde el hub geográfico.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Recorrer la URL Matrix (Paso-03 3.5) y filtrar todas las URLs cuya path incluya el `[main-city-slug]`. Generar enlaces desde el GeoHub a todas ellas. Para Cerrajeros Madrid 24h: 21 enlaces.

**Output del paso**

- **Tipo:** Regla operativa para Main City GeoHub.
- **Ejemplo (Cerrajeros Madrid 24h):** 21 outbound desde `/madrid/` (5 LBS + 1 AC + 15 GAs).

### 7.5 — Regla 5: Location-Based Service conecta servicio y ciudad

<small>§6.5</small>

**Explicación**

La página local (LBS) es el corazón comercial del cluster. Conecta el servicio padre (SO) con la ciudad principal (GeoHub) y se relaciona con servicios laterales del mismo cluster + GeoArticles que la apoyan. Es el punto de máxima conversión.

**Patrón o fórmula**

```text
LBS  →  parent SO (UP topical)
     +  GeoHub Main City (UP geo)
     +  related same-city services (LATERAL)
     +  matching GeoArticles (DOWN depth)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/cerrajero/madrid/cerrajero-urgente/ enlaza a:
  UP topical:    /cerrajero/cerrajero-urgente/
  UP geo:        /madrid/
  LATERAL:       /cerrajero/madrid/apertura-puertas/
                 /cerrajero/madrid/cambio-cerraduras/
  DOWN depth:    /madrid/cuanto-cuesta-un-cerrajero-urgente/
                 /madrid/que-hacer-si-no-puedes-entrar-casa/
                 /madrid/cuanto-tarda-un-cerrajero/
```

**Ejemplos incorrectos**

```text
- Landing sin GeoHub (no UP geo)
- Landing sin artículos (no DOWN depth)
- Landing con enlaces a áreas inexistentes (LCAs sin AEA)
- No enlazar al padre (no UP topical)
- Enlazar solo a contacto (sin estructura silo)
- Enlazar a servicios no relacionados (lateral mal escogido)
- Enlazar a todas las páginas sin criterio
- No usar anchors semánticos
```

**Regla final**

```text
LBS enlaza hacia arriba a su SO + GeoHub, lateralmente a otros LBS y AC del cluster, hacia abajo a sus GAs.
```

**Validación operativa**

Una página local debe enlazar a su Service Overview padre y al GeoHub. Esto conecta tópico y geografía, evitando que la landing quede aislada. Las páginas locales deben enlazar a servicios relacionados en la misma Main City para crear cluster comercial. Estos enlaces ayudan al usuario y refuerzan co-ocurrencias de servicio local.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Para cada LBS, generar el set de 6-7 enlaces: 1 SO padre, 1 GeoHub, 2-3 related LBS (mismo silo), 3 matching GAs. Total para 5 LBS: 30-35 enlaces.

**Output del paso**

- **Tipo:** Regla operativa para Location-Based Service Pages.
- **Ejemplo (Cerrajeros Madrid 24h):** 6-7 outbound por LBS × 5 LBS = ~30-35 enlaces.

### 7.6 — Regla 6: Additional Category se integra en el silo local

<small>§6.6</small>

**Explicación**

La página de categoría adicional (AC) NO debe quedar como página secundaria aislada. Tiene que enlazar al GeoHub Main City y a servicios relacionados del mismo silo para formar parte de la jerarquía local.

**Patrón o fórmula**

```text
Additional Category  →  GeoHub
                     +  related local services (LBS relacionados)
                     +  otras AC (si las hay)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/cerrajero/madrid/duplicado-llaves/ enlaza a:
  - /madrid/                                            (GeoHub)
  - /cerrajero/madrid/cambio-cerraduras/                (LBS relacionado: cambio-llaves vs cambio-cerradura)
  - /cerrajero/madrid/instalacion-cerraduras-seguridad/ (LBS relacionado: contexto seguridad)
```

**Ejemplos incorrectos**

```text
- Categoría adicional huérfana
- Sin conexión a GeoHub
- Duplicada con servicio core (canibalización)
- Página adicional sin enlaces internos
- Enlazar solo a homepage (sin silo local)
- No conectarla con servicios relacionados
```

**Regla final**

```text
Additional Category enlaza al silo local: GeoHub, LBS relacionados, otras AC si las hay.
```

**Validación operativa**

La página de categoría adicional debe enlazar al GeoHub y a servicios relacionados para no quedar como página secundaria aislada. La selección de "related LBS" debe basarse en proximidad temática (qué servicios consumen los mismos clientes).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Para cada AC efectiva, generar enlaces a 1 GeoHub + 2-3 LBS relacionados (proximidad temática). Para Cerrajeros con A=1: 3 enlaces (GeoHub + 2 LBS).

**Output del paso**

- **Tipo:** Regla operativa para Additional Category Pages.
- **Ejemplo (Cerrajeros Madrid 24h):** 3 outbound desde AC duplicado-llaves.

### 7.7 — Regla 7: GeoArticle pasa relevancia a la landing

<small>§6.7</small>

**Explicación**

Cada GeoArticle (GA) debe enlazar prominentemente a la landing comercial servicio+Main City que apoya. Sin ese enlace, el artículo no cumple su función de booster semántico — queda como contenido informativo aislado sin conversión.

**Patrón o fórmula**

```text
GeoArticle  →  matching LBS (autoridad → conversión)
            +  GeoHub Main City (geo anchor)
            +  related article (opcional, si existe relación temática)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/madrid/cuanto-cuesta-un-cerrajero-urgente/ enlaza a:
  - /cerrajero/madrid/cerrajero-urgente/   (matching LBS — autoridad pasa)
  - /madrid/                               (GeoHub geo anchor)
```

**Ejemplos incorrectos**

```text
- Artículo sin CTA interno
- Artículo sin enlace comercial
- Artículo enlazando a área sin URL
- Artículo sin enlace a landing
- Artículo enlaza solo a homepage (sin silo)
- Artículo apunta a una URL inexistente
```

**Regla final**

```text
Cada GeoArticle enlaza prominentemente a su landing comercial principal.
```

**Validación operativa**

Cada GeoArticle debe enlazar a la página comercial servicio+Main City que quiere reforzar. Sin ese enlace, el artículo no cumple su función de booster. Validar que el matching LBS está correctamente identificado en la URL Matrix (Paso-03 3.5).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Para cada GA, identificar la matching LBS según el `[topic-slug]` (cada topic está asociado a un servicio core). Generar 2 enlaces: matching LBS + GeoHub. Total para G×S=15 GAs: 30 enlaces.

**Output del paso**

- **Tipo:** Regla operativa para GeoArticle Pages.
- **Ejemplo (Cerrajeros Madrid 24h):** 15 conexiones GA → LBS + 15 conexiones GA → GeoHub = 30 enlaces totales.

### 7.8 — Regla 8: LCAs sin URL no reciben enlaces

<small>§6.8</small>

**Explicación**

Las Local Coverage Areas (LCAs) que NO han pasado a Approved Expansion Areas (AEAs) no tienen URLs propias. Pueden mencionarse en contenido (texto, FAQs, schema `areaServed`) pero NUNCA recibir anchors (`<a href="/almagro/">`) hacia URLs inexistentes. Crear esos anchors genera errores 404, anchors rotos y degradación de la experiencia de crawl.

**Patrón o fórmula**

```text
Local Coverage Area sin URL  →  mención textual en contenido
                              +  schema areaServed
                              ↛  NO link / NO anchor
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h menciona "Almagro" en el contenido de
/cerrajero/madrid/cerrajero-urgente/, pero NO crea
<a href="/almagro/">Almagro</a> hasta que /almagro/ sea AEA aprobada.

10 LCAs declaradas → 0 anchors hacia ellas.
```

**Ejemplos incorrectos**

```text
- <a href="/almagro/">Almagro</a> sin que /almagro/ exista
- Breadcrumb con Salamanca > ... (sin URL para Salamanca)
- Footer con enlaces a áreas sin página
- Crear anchors rotos hacia /chamberi/
- Simular páginas de cobertura con hashtags
- Enlazar a búsquedas externas en vez de URLs propias
```

**Regla final**

```text
Si una LCA no tiene URL aprobada (no es AEA), NO recibe enlaces internos — solo menciones de contenido.
```

**Validación operativa**

Si una Local Coverage Area no es Approved Expansion Area, no debe recibir enlaces internos. Puede mencionarse en texto, pero no como anchor hacia una página inexistente. La validación cruzada con Paso-04 4.9 (LCAs no generan URLs) y Paso-01 1.10 (Local Coverage Areas) confirma que las 10 LCAs declaradas no aparecen como anchors.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Antes de generar enlaces, validar para cada anchor que el target existe en la URL Matrix (Paso-03 3.5). Si la zona referenciada no tiene URL en la matriz, NO generar el anchor — solo mantener mención textual.

**Output del paso**

- **Tipo:** Validación operativa — 0 anchors a URLs inexistentes.
- **Ejemplo (Cerrajeros Madrid 24h):** Almagro, Chamberí, Salamanca, Retiro, etc. → 0 anchors `<a href="/{lca}/">`. Solo menciones textuales.

### 7.9 — Regla 9: Anchor text variado

<small>§6.9</small>

**Explicación**

Los anchors deben variar entre 6 categorías (exact match, partial, branded, CTA, informational, local entity). Usar el mismo anchor 20 veces o solo exact match parece mecánico, reduce calidad editorial y aumenta riesgo de manual penalty por sobre-optimización.

**Patrón o fórmula**

```text
Distribución de anchors recomendada:
  Exact match           ~15%
  Partial match         ~25%
  Branded               ~15%
  CTA                   ~15%
  Informational         ~20%
  Local entity          ~10%
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Exact match:     "cerrajero urgente en Madrid"
Partial:         "servicios de cerrajería"
Branded:         "Cerrajeros Madrid 24h"
CTA:             "Llama hoy"
Informational:   "Conoce más sobre cerrajero urgente"
Local entity:    "zonas de cobertura en Madrid"
```

**Ejemplos incorrectos**

```text
- Mismo anchor 20 veces ("cerrajero urgente Madrid" en cada link)
- Solo exact match (100% optimización agresiva)
- Anchors genéricos como "haz clic aquí" / "click here"
- Repetir "urgente cerrajero Madrid" en todos los enlaces
- Usar solo "haz clic aquí"
- Usar anchors irrelevantes ("información importante")
```

**Regla final**

```text
Anchor text variado y descriptivo; nunca repetir el mismo anchor en múltiples enlaces.
```

**Validación operativa**

Los anchors deben ser naturales y variados. Usar siempre el exact match puede parecer mecánico y reduce calidad editorial. La distribución por categoría se valida durante QA (Paso 18) — si ≥40% de anchors son exact match, revisar y diversificar.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Para cada enlace generado por las reglas 1-8, escoger una de las 6 categorías de anchor según el contexto (ej. en intro: descriptivo o local entity; en CTA: CTA branded; en related sections: partial match). Usar el Brand Name (Paso-01 1.1) para branded, Preferred CTA (Paso-01 1.13) para CTA, etc.

**Output del paso**

- **Tipo:** Catálogo de 6 categorías de anchor con distribución recomendada.
- **Ejemplo (Cerrajeros Madrid 24h):** Mix de 6 categorías aplicado a los ~80 enlaces internos del cluster.

### 7.10 — Regla 10: Enlaces contextuales primero

<small>§6.10</small>

**Explicación**

Los enlaces dentro del cuerpo del contenido (intro, párrafos, FAQs, related resources) tienen más valor SEO y UX que repetir todo en footer/menú. El footer y menú son enlaces estructurales (presentes en todas las páginas, baja autoridad por enlace); los contextuales (en body) tienen más peso temático.

**Patrón o fórmula**

```text
Placement de enlaces (priorizado):
  1. Intro / opening paragraph (high value)
  2. Body / main content sections (medium-high)
  3. FAQs (responses) (medium-high)
  4. Related resources / further reading (medium)
  5. CTA blocks (medium-high)
  6. Sidebar / aside (low-medium)
  7. Footer / menú (structural, low por link)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
En el body de /cerrajero/madrid/cerrajero-urgente/:
  "Atendemos llamadas de cerrajería urgente las 24 horas en
  [Madrid](/madrid/), con cobertura adicional en zonas como
  Almagro y Chamberí. Si necesitas también [apertura de puertas
  no urgente](/cerrajero/madrid/apertura-puertas/), también lo
  cubrimos."

Aquí los enlaces a /madrid/ y /cerrajero/madrid/apertura-puertas/
están en contexto natural — no es un bloque de "enlaces relacionados"
genérico al final.
```

**Ejemplos incorrectos**

```text
- Solo footer (todos los enlaces fuera del body)
- Solo menú (sin enlaces contextuales)
- Bloques de enlaces sin contexto (lista pelada al final)
- Pestañas / tabs sin texto contextual
```

**Regla final**

```text
Enlaces dentro del cuerpo (contextuales) primero; enlaces de navegación / footer después.
```

**Validación operativa**

Cada page type debe tener ≥3 enlaces contextuales (en body) además del menú/footer estructural. Validar durante QA del Paso 18 que las páginas no son solo "todo footer/menú".

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Al generar el contenido de cada page type (Paso 6 — Estructura de Contenido), incluir los enlaces internos requeridos (de las reglas 1-9) integrados en intros, párrafos, FAQs, related resources. NO dejar todos los enlaces para footer/sidebar.

**Output del paso**

- **Tipo:** Regla de placement de enlaces.
- **Ejemplo (Cerrajeros Madrid 24h):** Body links priorizados sobre nav/footer en las 28 URLs del cluster.

### 7.11 — Matriz de enlaces obligatorios por page type

<small>§6.11</small>

**Explicación**

La matriz consolidada de las 14 conexiones source → target obligatorias del cluster. Es el handoff principal al Paso 18 (QA + deploy) que valida cada enlace contra esta matriz. Si un enlace de la matriz falta en una página, el QA lo marca como "missing required link" y bloquea publish hasta corrección.

**Patrón o fórmula (la matriz consolidada)**

| # | Source Page | Target | Tipo de enlace | Cantidad |
|---|---|---|---|---|
| 1 | Homepage | Service Overview Pages | Top-of-funnel | S enlaces |
| 2 | Homepage | Main City GeoHub | Geo anchor | 1 |
| 3 | Homepage | Página de contacto | CTA conversión | 1 |
| 4 | Service Overview | Main City LBS Page | Local push | S × 1 |
| 5 | Service Overview | Related Services | Topical | S × 2-3 |
| 6 | Main City GeoHub | All Main City Service Pages | Silo organization | S |
| 7 | Main City GeoHub | Additional Category Pages | GBP support | A |
| 8 | Main City GeoHub | GeoArticles | Local resources | G × S |
| 9 | LBS | Parent Service Overview | Up (topical) | S × 1 |
| 10 | LBS | Main City GeoHub | Up (geo) | S × 1 |
| 11 | LBS | Related same-city services | Lateral | S × 2-3 |
| 12 | LBS | Matching GeoArticles | Down (depth) | S × G |
| 13 | GeoArticle | Matching LBS Page | Authority transfer | G × S × 1 |
| 14 | GeoArticle | Main City GeoHub | Geo anchor | G × S × 1 |

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar las 10 reglas (7.1-7.10) a la URL Matrix del Paso 3 y consolidar las conexiones source → target en una sola tabla. La matriz queda lista para QA del Paso 18.

**Output del paso**

- **Tipo:** Tabla consolidada de 14 conexiones source → target.
- **Ejemplo (Cerrajeros Madrid 24h):** Aplicado con S=5, A=1, G=3 → ~80 enlaces totales en el cluster.

### 7.12 — Ejemplo completo de enlaces para LBS modelo

<small>§6.12</small>

**Explicación**

Set ejemplar de enlaces inbound + outbound + anchors para una LBS modelo, sirve como referencia visual para validar las reglas 1-10 aplicadas correctamente. La IA puede tomar este ejemplo como template para generar el set de cualquier otra LBS del cluster.

**Patrón (set ejemplar)**

```text
Source: LBS modelo
Required outbound links:
  - SO padre (1)
  - GeoHub Main City (1)
  - related LBS (2-3)
  - matching GAs (3)
  - contacto/auxiliar (1)

Anchor distribution:
  - branded ×1
  - exact match ×1
  - partial ×2
  - informational ×1
  - CTA ×1
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Source: /cerrajero/madrid/cerrajero-urgente/

Required outbound links (6):
  - /cerrajero/cerrajero-urgente/         (SO padre, anchor: "servicios de cerrajería urgente")
  - /madrid/                              (GeoHub, anchor: "zonas de cobertura en Madrid")
  - /cerrajero/madrid/apertura-puertas/   (related LBS, anchor: "apertura de puertas")
  - /cerrajero/madrid/cambio-cerraduras/  (related LBS, anchor: "cambio de cerraduras en Madrid")
  - /madrid/cuanto-cuesta-un-cerrajero-urgente/  (matching GA, anchor: "precio de cerrajero urgente")
  - /contacto/                            (CTA, anchor: "Llama hoy a Cerrajeros Madrid 24h")

Anchor suggestions:
  - "urgente servicios de cerrajería"
  - "servicios de cerrajería en Madrid"
  - "apertura de puertas en Madrid"
  - "servicios de cambio de cerraduras en Madrid"
  - "precio de cerrajero urgente en Madrid"
  - "llama hoy a Cerrajeros Madrid 24h"
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Tomar la LBS principal del cluster (en Cerrajeros: cerrajero-urgente Madrid) y aplicar las reglas 1-10 generando el set ejemplar. Documentar como template para que la IA lo replique en las otras 4 LBS del cluster (más las del expansion si las hay).

**Output del paso**

- **Tipo:** Set inbound/outbound + anchors para 1 LBS modelo.
- **Ejemplo (Cerrajeros Madrid 24h):** 6 outbound + 6 anchor suggestions documentados para `/cerrajero/madrid/cerrajero-urgente/`.

### 7.13 — Breadcrumbs por page type

<small>§6.13</small>

**Explicación**

Los breadcrumbs ayudan a usuarios y motores de búsqueda a entender la jerarquía del cluster. Cada page type tiene un breadcrumb específico que refleja su posición en la arquitectura. Los breadcrumbs NO deben inventar niveles de cobertura inexistentes (ej. no incluir "Almagro" en breadcrumb si Almagro no es AEA).

**Patrón (breadcrumbs por page type)**

```text
Homepage:               Home
Service Overview:       Home > {Primary Category} > {Service Name}
Main City GeoHub:       Home > {Main City}
Location-Based Service: Home > {Primary Category} > {Main City} > {Service Name}
Additional Category:    Home > {Primary Category} > {Main City} > {Additional Category Name}
GeoArticle:             Home > {Main City} > {Article Topic Title}
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

| Page Type | Breadcrumb |
|---|---|
| Homepage | `Home` |
| Service Overview | `Home > Cerrajero > Cerrajero urgente` |
| Main City GeoHub | `Home > Madrid` |
| Location-Based Service | `Home > Cerrajero > Madrid > Cerrajero urgente` |
| Additional Category | `Home > Cerrajero > Madrid > Duplicado de llaves` |
| GeoArticle | `Home > Madrid > Cuánto cuesta un cerrajero urgente` |

**Ejemplos incorrectos**

```text
- Breadcrumb con Almagro (LCA sin AEA)
- Breadcrumb solo con Home > Article (sin estructura)
- Breadcrumb que no refleja la URL real
- Breadcrumb con niveles inventados (ej. "Home > Servicios > Cerrajeros > Madrid")
```

**Regla final**

```text
Cada page type tiene un breadcrumb específico que refleja su posición en la arquitectura.
```

**Validación operativa**

Los breadcrumbs ayudan a usuarios y motores a entender jerarquía. Deben reflejar el page type y NO inventar niveles de cobertura inexistentes. La implementación schema (BreadcrumbList) se hace en Paso 8 — esta sección entrega los textos.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Para cada page type, aplicar el patrón con los nombres heredados (Primary Category, Main City, Service, Additional Category, Article Topic). El último item del breadcrumb es siempre la página actual (sin link).

**Output del paso**

- **Tipo:** Jerarquía de breadcrumbs por 6 page types.
- **Ejemplo (Cerrajeros Madrid 24h):** 6 breadcrumbs documentados en tabla.

### 7.14 — Inbound links esperados (cross-cutting)

<small>§6.14</small>

**Explicación**

Cada page type tiene un mapa de **inbound links mínimos esperados** desde otras páginas del cluster. Si una página no recibe los inbound mínimos, queda como página huérfana o débil. Esta validación complementa las reglas 1-10 (que se enfocan en outbound) — aquí miramos al revés: ¿quién enlaza a esta página?

**Patrón (inbound mínimos por page type)**

```text
Homepage:           ∞ inbound (todos los links del menú apuntan aquí)
Service Overview:   1 (Homepage) + S-1 (otras SO related)
Main City GeoHub:   1 (Homepage) + S (LBS apuntan up) + A (AC) + G×S (GAs apuntan up)
LBS:                1 (Homepage) + 1 (SO padre) + 1 (GeoHub) + S-1 (related LBS) + G (matching GAs)
Additional Category: 1 (Homepage) + 1 (GeoHub) + LBS related (depende)
GeoArticle:         1 (GeoHub) + 1 (matching LBS) (mínimo)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS /cerrajero/madrid/cerrajero-urgente/ recibe enlaces desde:
  - Homepage
  - SO padre /cerrajero/cerrajero-urgente/
  - GeoHub /madrid/
  - 4 related LBS (apertura, cambio-cerraduras, etc.)
  - 3 matching GeoArticles (cuanto-cuesta, que-hacer, cuanto-tarda)
Total: 9 inbound mínimos.

GeoArticle /madrid/cuanto-cuesta-un-cerrajero-urgente/:
  - GeoHub /madrid/
  - matching LBS /cerrajero/madrid/cerrajero-urgente/
Total: 2 inbound mínimos.
```

**Ejemplos incorrectos**

```text
- Crear páginas sin inbound links (huérfanas)
- Depender solo del menú principal (estructural, no contextual)
- No revisar enlaces entrantes en QA
- LBS con solo Homepage como inbound (silo roto, sin SO padre)
```

**Regla final**

```text
Cada page type tiene un mapa de inbound links esperado documentado en la matriz.
```

**Validación operativa**

La matriz de outbound (7.11) genera implícitamente el mapa de inbound: si A enlaza a B, entonces B recibe inbound de A. La validación cross-cutting consiste en invertir la matriz: por cada page type target, listar los page types source que deben enlazar a él. Si falta alguno, la página queda huérfana o débil.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar como filtro de QA al validar el internal linking del cluster antes de Paso 18 (deploy). Para cada URL de la matriz, contar inbound y comparar con el mínimo esperado por page type. Si falta, alertar y corregir.

**Output del paso**

- **Tipo:** Validation flag — todas las URLs tienen inbound mínimos esperados.
- **Ejemplo (Cerrajeros Madrid 24h):** 0 páginas huérfanas detectadas. Cluster con linking completo.

### 7.15 — Expansion linking separado (cross-cutting)

<small>§6.15</small>

**Explicación**

Cuando una Approved Expansion Area (AEA) genera URLs propias, se añade una capa de linking propia (sub-cluster) que NO debe contaminar la matriz base hasta que el cluster expansion exista publicado. Mantener el linking de expansión separado evita errores 404 y simplifica el QA mientras se construye el AEA cluster.

**Patrón o fórmula**

```text
Si E ≥ 1 (AEA aprobada):
  Sub-cluster expansion:
    Approved Expansion GeoHub  →  expansion service pages
                               →  expansion AC pages
                               →  expansion GAs (related al servicio en zona)

  Expansion → base linking:
    expansion service pages  →  parent SO de la base
                             ←  GeoHub base (opcional, si proximidad geográfica justifica)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Phase 1: E = 0 (None in Phase 1) → no aplica sub-cluster de expansión.

Hipotético si Almagro se aprueba como AEA:
  /almagro/  (Expansion GeoHub) enlaza a:
    - /cerrajero/almagro/cerrajero-urgente/  (Expansion LBS)
    - /cerrajero/almagro/duplicado-llaves/   (Expansion AC)
    - /almagro/cuanto-cuesta-un-cerrajero-urgente/  (Expansion GA)

  /cerrajero/almagro/cerrajero-urgente/ enlaza a:
    - /cerrajero/cerrajero-urgente/  (parent SO de la base)
    - /almagro/                      (Expansion GeoHub, no /madrid/)
```

**Ejemplos incorrectos**

```text
- Enlazar expansión antes de publicar páginas
- Mezclar expansión con cobertura textual
- No enlazar la expansión al servicio padre
- Expansion LBS enlaza a /madrid/ en vez de /almagro/ (silo roto)
- Mezclar ambos sub-clusters en el QA antes de validar cada uno
```

**Regla final**

```text
Approved Expansion Areas crean su propio sub-cluster de linking, separado del base.
```

**Validación operativa**

Si E ≥ 1 (AEAs aprobadas), aplicar la matriz de enlaces obligatorios (7.11) AISLADAMENTE para el sub-cluster expansion. Las únicas conexiones cruzadas permitidas son:
- Expansion LBS → SO padre de la base (compartido)
- Expansion GA → matching expansion LBS (intra-sub-cluster)

NO permitir: Expansion LBS → /madrid/ (GeoHub base) o Expansion GA → matching LBS de la base.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Si E ≥ 1, aplicar reglas 1-10 al sub-cluster expansion como si fuera un cluster independiente, con la única excepción de que las Expansion LBS pueden enlazar UP a la SO padre de la base (compartida).

**Output del paso**

- **Tipo:** Regla operativa para sub-cluster de expansion.
- **Ejemplo (Cerrajeros Madrid 24h):** Phase 1: E=0 → no aplica. Si Phase 2 con Almagro: 1 sub-cluster con sus propios 21 enlaces internos (1 GeoHub + 5 LBS + 1 AC + 15 GAs).

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 7 y avanzar al Paso 8 (Schema Markup) o Paso 18 (QA + deploy).

### Validación de reglas operativas

- ☐ Regla 1 — Todas las páginas tienen up + down + lateral links (7.1)
- ☐ Regla 2 — Homepage enlaza a S SO + GeoHub + AC + contacto (7.2)
- ☐ Regla 3 — Cada SO enlaza a su LBS Main City (7.3)
- ☐ Regla 4 — GeoHub enlaza a TODAS las páginas locales (7.4)
- ☐ Regla 5 — LBS enlaza a SO padre + GeoHub + related + GAs (7.5)
- ☐ Regla 6 — AC enlaza a GeoHub + LBS relacionados (7.6)
- ☐ Regla 7 — Cada GA enlaza a matching LBS + GeoHub (7.7)
- ☐ Regla 8 — Cero anchors a LCAs sin URL aprobada (7.8)
- ☐ Regla 9 — Anchor text variado (mix de 6 categorías) (7.9)
- ☐ Regla 10 — Body links priorizados sobre nav/footer (7.10)

### Validación de matriz consolidada

- ☐ Matriz de 14 conexiones source → target completa (7.11)
- ☐ Ejemplo completo de enlaces para LBS modelo documentado (7.12)
- ☐ Breadcrumbs definidos para los 6 page types (7.13)

### Validación cross-cutting

- ☐ Inbound links mínimos cumplidos para cada page type (7.14)
- ☐ 0 páginas huérfanas en el cluster
- ☐ Expansion linking separado (si E ≥ 1) (7.15)

### Validación de targets

- ☐ Todos los target URLs existen en la URL Matrix (Paso-03 3.5)
- ☐ Patrones de URL respetados en cada anchor (Paso-04 4.1-4.15)
- ☐ 0 enlaces a Local Coverage Areas sin URL (Paso-01 1.10 + Paso-04 4.9)

## Outputs Consolidados

<small>§8</small>

> Tabla final con valores reales para Cerrajeros Madrid 24h y status de cada output. Los IDs (`7.1`–`7.15`) coinciden con los declarados en §5.

| ID | Output | Valor (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|
| 7.1 | Regla 1 — Enlazar arriba/abajo/lateral | Aplicada a 28 URLs (cada una con 3 direcciones) | confirmed |
| 7.2 | Regla 2 — Homepage distribuye autoridad | 8 outbound desde `/` (5 SO + 1 GeoHub + 1 AC + 1 contacto) | confirmed |
| 7.3 | Regla 3 — SO empuja versión local | 5 conexiones SO → LBS | confirmed |
| 7.4 | Regla 4 — GeoHub organiza Main City | 21 outbound desde `/madrid/` (5 LBS + 1 AC + 15 GAs) | confirmed |
| 7.5 | Regla 5 — LBS conecta servicio y ciudad | ~30-35 enlaces (6-7 por LBS × 5) | confirmed |
| 7.6 | Regla 6 — AC se integra en silo local | 3 outbound desde AC duplicado-llaves | confirmed |
| 7.7 | Regla 7 — GeoArticle pasa relevancia a landing | 30 conexiones (15 GA → LBS + 15 GA → GeoHub) | confirmed |
| 7.8 | Regla 8 — LCAs sin URL no reciben enlaces | 0 anchors a 10 LCAs declaradas | OK |
| 7.9 | Regla 9 — Anchor text variado | Mix 6 categorías aplicado a ~80 enlaces | confirmed |
| 7.10 | Regla 10 — Enlaces contextuales primero | Body links priorizados en 28 URLs | confirmed |
| 7.11 | Matriz de enlaces obligatorios | 14 conexiones source → target documentadas | confirmed |
| 7.12 | Ejemplo completo de enlaces LBS modelo | 6 outbound + 6 anchors para `/cerrajero/madrid/cerrajero-urgente/` | confirmed |
| 7.13 | Breadcrumbs por page type | 6 breadcrumbs documentados (1 por page type) | confirmed |
| 7.14 | Inbound links esperados | 0 páginas huérfanas; mínimos cumplidos por page type | OK |
| 7.15 | Expansion linking separado | E=0 en Phase 1 → no aplica sub-cluster | OK |

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
