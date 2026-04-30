Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo la estructura fija acordada en la conversación.
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# Paso 2 — Fórmula Maestra de Arquitectura

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 15 outputs del Paso 2 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, reglas que aplican, checklist final y outputs consolidados.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 2

<small>§2</small>

Calcular el tamaño exacto del cluster aplicando la fórmula maestra `1 + S + 1 + S + A + G × S` sobre los inputs heredados del Paso 1, produciendo el inventario completo de páginas SEO base antes de crear URLs concretas.

**Outputs del paso:**

- **2.1** Planned GBP Categories Status — todas las categorías marcadas como `Planned` hasta el Paso 14
- **2.2** Primary Category Slug — operación slugify aplicada al Planned Primary Category
- **2.3** Main City Slug — operación slugify aplicada a la Main City
- **2.4** Service Slugs (S=5) — operación slugify aplicada a cada core service
- **2.5** Service-to-Main-City Applicability — boolean + lista de exclusiones (default: todos aplican)
- **2.6** Variable S — número de core services aplicables a Main City (S_efectiva)
- **2.7** Variable A — número de Additional Categories que necesitan página propia
- **2.8** Variable G — GeoArticles per Service (heredado del Paso-01 1.12)
- **2.9** Total páginas SEO base — resultado de la fórmula `1 + S + 1 + S + A + G × S`
- **2.10** Inventario por tipo de página — Homepage / SO / GeoHub / LBS / AC / GeoArticles con sus cantidades
- **2.11** Optional Expansion Formula — fórmula adicional para Approved Expansion Areas (default: 0 en Phase 1)
- **2.12** Validación anti-duplicación
- **2.13** Validación dependencias entre páginas
- **2.14** Validación LCAs fuera fórmula
- **2.15** Validación auditabilidad del total

**Errores que previene:**

- Crear páginas sin saber cuántas deberían existir
- Meter Local Coverage Areas dentro de la fórmula base
- Confundir Approved Expansion Areas con cobertura local mencionada en contenido
- Duplicar categorías adicionales ya cubiertas por core services
- Publicar GeoArticles antes de tener las páginas comerciales que apoyan

**Cuándo se ejecuta:** después de Paso 1 cerrado (intake completo). Antes de Paso 3 (Matriz Base de URLs).

## Info heredada de pasos anteriores

<small>§3</small>

> Estos campos NO se deciden en Paso 2 — la IA los lee del paso indicado y los usa como input para aplicar la fórmula y producir el inventario del Bloque II.

| Campo | Origen |
|---|---|
| Business Name | Paso-01 1.1 |
| Planned Primary GBP Category | Paso-01 1.5 |
| Servicios principales (5 core services) | Paso-01 1.9 |
| Planned Additional GBP Categories | Paso-01 1.6 |
| Additional Categories cubiertas por core services | Paso-01 1.6 (consolidación) |
| Additional Categories que necesitan página propia | Paso-01 1.6 (consolidación) |
| Main City | Paso-01 1.7 |
| Local Coverage Areas | Paso-01 1.10 |
| Approved Expansion Areas | Paso-01 1.11 |
| GeoArticles per Service (G) | Paso-01 1.12 |

> Los outputs nuevos que se producen en Paso 2 (Slug Generation y Service-to-Main-City Applicability) tienen sus propias secciones en Bloque III — §6.2 y §6.5.

# Bloque II — Ejemplo rellenado para el Paso 2 — Fórmula Maestra de Arquitectura

<small>§4</small>

> Los 15 outputs del Paso 2 con sus valores reales para Cerrajeros Madrid 24h. Los inputs heredados (Business Name, Categories, Servicios, LCAs, etc.) tienen su ejemplo en sus pasos de origen (§4 de Paso 1).

### 2.1 — Planned GBP Categories Status

| Categoría | Status |
|---|---|
| Planned Primary GBP Category: Cerrajero | `Planned` |
| Planned Additional: Servicio de cerrajería de urgencia | `Planned` |
| Planned Additional: Servicio de duplicado de llaves | `Planned` |

### 2.2 — Primary Category Slug

`cerrajero`

### 2.3 — Main City Slug

`madrid`

### 2.4 — Service Slugs (S=5)

`cerrajero-urgente`, `apertura-puertas`, `cambio-cerraduras`, `cambio-bombines`, `instalacion-cerraduras-seguridad`

### 2.5 — Service-to-Main-City Applicability

| Campo | Valor |
|---|---|
| ¿Todos los servicios aplican a Main City? | Yes |
| Exclusiones | (ninguna) |
| S_efectiva | 5 |

### 2.6 — Variable S

`S = 5` (5 core services declarados en Paso-01 1.9)

### 2.7 — Variable A

`A = 1` (Solo Servicio de duplicado de llaves necesita página propia; Servicio de cerrajería de urgencia queda cubierta por core service Cerrajero urgente)

### 2.8 — Variable G

`G = 3` (heredado del Paso-01 1.12)

### 2.9 — Total páginas SEO base

`1 + 5 + 1 + 5 + 1 + 15 = 28 páginas SEO base`

Aplicación de la fórmula `1 + S + 1 + S + A + (G × S)` con S=5, A=1, G=3.

### 2.10 — Inventario por tipo de página

| Tipo de página | Cantidad | Fórmula |
|---|---:|---|
| Homepage | 1 | constante |
| Service Overview Pages | 5 | S |
| GeoHub Main City | 1 | constante (Madrid) |
| Location-Based Service Pages | 5 | S |
| Additional Category Pages | 1 | A |
| GeoArticles | 15 | G × S |
| **Total SEO base** | **28** | **1 + S + 1 + S + A + (G × S)** |
| `/contacto/` (auxiliar fuera SEO base) | 1 | — |

### 2.11 — Optional Expansion Formula

| Campo | Valor |
|---|---|
| Approved Expansion Areas (E) | 0 (None in Phase 1) |
| Páginas de expansión | 0 |
| Fórmula expansion declarada | `E + S × E + A × E + G × S × E` (lista para futura activación) |

### 2.12 — Validación anti-duplicación

Cumplido — Servicio de cerrajería de urgencia consolidada con core service Cerrajero urgente (no suma a A).

### 2.13 — Validación dependencias entre páginas

Cumplido — orden Homepage → Service Overview Pages → GeoHub Main City → LBS → Additional Category → GeoArticles validado.

### 2.14 — Validación LCAs fuera fórmula

Cumplido — Almagro, Chamberí, Salamanca, Retiro y demás LCAs NO generan URLs base; viven en contenido y `areaServed`.

### 2.15 — Validación auditabilidad del total

Cumplido — 28 páginas explicables componente a componente: 1 Homepage + 5 SO + 1 GeoHub + 5 LBS + 1 AC + 15 GAs.

# Bloque III — Ejecución por la IA

> **Definición operativa — Local Coverage Areas:** zonas, barrios, distritos o landmarks seleccionados desde la dirección física, la Main City, la coherencia GEO, la proximidad, los datos de búsqueda, los competidores y la lógica GMB Crush para reforzar relevancia local dentro del contenido, schema y futuros análisis. No son automáticamente URLs. No son automáticamente páginas propias. No son necesariamente oficinas físicas. Las Local Coverage Areas se usan primero como señales GEO dentro del contenido. No generan URLs por defecto.

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 15 outputs que el Paso 2 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `2.1`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 2.1 | Planned GBP Categories Status | Status (`Planned` hasta Paso 14) | GMB Crush | Paso-01 1.5 + Paso-01 1.6 |
| 2.2 | Primary Category Slug | URL-safe string | GMB Crush | Paso-01 1.5 |
| 2.3 | Main City Slug | URL-safe string | GMB Crush | Paso-01 1.7 |
| 2.4 | Service Slugs (S=5) | URL-safe strings | GMB Crush | Paso-01 1.9 |
| 2.5 | Service-to-Main-City Applicability | Boolean + exclusiones | GMB Crush + Input humano | — |
| 2.6 | Variable S (S_efectiva) | Entero | GMB Crush | Paso-01 1.9 |
| 2.7 | Variable A | Entero | GMB Crush | Paso-01 1.6 |
| 2.8 | Variable G | Entero | GMB Crush | Paso-01 1.12 |
| 2.9 | Total páginas SEO base | Entero (28 para Cerrajeros) | GMB Crush | Paso-02 2.6 + 2.7 + 2.8 (intra-paso) |
| 2.10 | Inventario por tipo de página | Tabla 6 page types | GMB Crush | Paso-02 2.6 + 2.7 + 2.8 (intra-paso) |
| 2.11 | Optional Expansion Formula | Fórmula declarada | GMB Crush | — |
| 2.12 | Validación anti-duplicación | Validation flag | GMB Crush | — |
| 2.13 | Validación dependencias | Validation flag | GMB Crush | — |
| 2.14 | Validación LCAs fuera fórmula | Validation flag | GMB Crush | — |
| 2.15 | Validación auditabilidad del total | Validation flag | GMB Crush | — |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 15 outputs (2.1–2.15) con el mismo patrón: Explicación / Patrón o fórmula / Ejemplos correctos / Ejemplos incorrectos / Regla final / Validación operativa / Cómo se obtiene / Output del paso. Cada sub-sección §6.X corresponde 1:1 al output 2.X declarado en §5.

### 2.1 — Planned GBP Categories Status
<small>§6.1</small>

**Explicación**

En esta versión el GBP se crea después de la web. Por eso la fórmula usa categorías planificadas, no categorías confirmadas. La arquitectura debe preparar soporte para la categoría principal prevista y para las categorías adicionales previstas, pero la confirmación final se realiza en el Paso 14.

**Patrón o fórmula**

```text
Planned Primary GBP Category → define primary category slug and core architecture
Planned Additional GBP Categories → define additional category support pages when they need separate pages
Confirmed GBP Categories → updated after Paso 14
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Planned Primary GBP Category: Cerrajero
Planned Additional Category that needs page: Servicio de duplicado de llaves
Base page: /cerrajero/madrid/duplicado-llaves/
```

**Ejemplos incorrectos**

```text
- Crear la web sin decidir la categoría principal prevista.
- Crear páginas de categorías adicionales que no se van a usar en el GBP.
- Añadir sameAs del GBP antes de que el perfil exista.
```

**Regla final**

```text
Antes del GBP, la web soporta categorías planificadas; después del Paso 14, se validan y sincronizan con categorías confirmadas.
```

**Validación operativa**

Marcar el status como `Planned` para todas las categorías GBP previstas. La sincronización con categorías confirmadas la hace el Paso 14 cuando crea y verifica el GBP. La arquitectura web del Paso 2 se construye sobre Planned Primary y solo soporta Planned Additional que necesitan página separada (cruce con §6.7 Variable A).

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso-01 1.5 + Paso-01 1.6.
- **Método:** Marcar todas las categorías GBP planificadas como `Planned` hasta que el Paso 14 cree y verifique el GBP. La arquitectura web se construye sobre la Planned Primary y solo soporta Planned Additional que necesitan página separada (cruce con §6.7 Variable A).

**Output del paso**

- **Tipo:** Status declarado de categorías GBP — `Planned` hasta el Paso 14.
- **Ejemplo (Cerrajeros Madrid 24h):** Planned Primary: Cerrajero. Planned Additional: Servicio de cerrajería de urgencia (cubierta por core service), Servicio de duplicado de llaves (necesita página propia).

### 2.2 — Primary Category Slug
<small>§6.2</small>

**Explicación**

El Primary Category Slug es la versión URL-safe de la Planned Primary GBP Category. Es el primer segmento de path de todas las URLs que incluyen categoría (Service Overview, LBS, Additional Category). Se deriva mecánicamente del nombre de la categoría — nunca se inventa.

**Patrón o fórmula**

```text
primary_category_slug = slugify(Planned Primary GBP Category)

donde slugify(text) = lowercase(text)
                    → remove_diacritics()
                    → replace_non_alphanumeric_with('-')
                    → collapse_consecutive_dashes()
                    → trim_leading_trailing_dashes()
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Planned Primary GBP Category: Cerrajero
Primary Category Slug: cerrajero
Aplicado en URLs: /cerrajero/cerrajero-urgente/, /cerrajero/madrid/duplicado-llaves/
```

**Ejemplos incorrectos**

```text
- Cerrajería (mantiene la tilde)
- CERRAJERO (mayúsculas)
- cerrajero_principal (underscore)
- mejor-cerrajero (modificador inventado)
- Cerrajería_Madrid (combinación de errores)
```

**Regla final**

```text
El Primary Category Slug es derivado determinista del Planned Primary GBP Category mediante slugify. No se inventa.
```

**Validación operativa**

Aplicar slugify a la Planned Primary GBP Category declarada en Paso-01 1.5. Si el cliente pide un slug distinto del derivado, documentar la excepción explícitamente. El slug se reutiliza en TODAS las URLs y schema canonical del Paso 4 en adelante.

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso-01 1.5 Planned Primary GBP Category.
- **Método:** Aplicar slugify(Planned Primary GBP Category). Reutilizar como `[primary-category-slug]` en patrones URL del Paso 4 y schema del Paso 8.

**Output del paso**

- **Tipo:** URL-safe string (1 valor único por web).
- **Ejemplo (Cerrajeros Madrid 24h):** `cerrajero`.

### 2.3 — Main City Slug
<small>§6.3</small>

**Explicación**

El Main City Slug es la versión URL-safe de la Main City. Es el segmento geográfico que aparece en GeoHub (`/madrid/`), LBS (`/cerrajero/madrid/cerrajero-urgente/`), Additional Category (`/cerrajero/madrid/duplicado-llaves/`) y GeoArticles (`/madrid/cuanto-cuesta-un-cerrajero-urgente/`). Se deriva mecánicamente del nombre de la ciudad.

**Patrón o fórmula**

```text
main_city_slug = slugify(Main City)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Main City: Madrid
Main City Slug: madrid
Aplicado en URLs: /madrid/, /cerrajero/madrid/cerrajero-urgente/, /madrid/cuanto-cuesta-un-cerrajero-urgente/
```

**Ejemplos incorrectos**

```text
- Madrid_Capital (subrayado y palabra extra)
- madrid-españa (concatenación con país)
- MAD (abreviatura)
- madrid-centro (modificador subzona)
- ciudad-madrid (prefijo redundante)
```

**Regla final**

```text
El Main City Slug es derivado determinista de la Main City mediante slugify. Una sola Main City = un solo slug en toda la web base.
```

**Validación operativa**

Aplicar slugify a la Main City declarada en Paso-01 1.7. La fórmula base usa una sola Main City (cruce con §6.5 Service-to-Main-City Applicability), por lo que existe un único Main City Slug para todo el cluster base. Las Local Coverage Areas NO generan slugs propios (cruce con §6.14).

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso-01 1.7 Main City.
- **Método:** Aplicar slugify(Main City). Reutilizar como `[main-city-slug]` en patrones URL del Paso 4 (Paso-04 §6 Trailing Slash, Paso-04 §9 GeoHub URL Style, Paso-04 §10 LBS URL pattern, Paso-04 §11 Additional Category URL pattern, Paso-04 §12 GeoArticle URL pattern).

**Output del paso**

- **Tipo:** URL-safe string (1 valor único por web base).
- **Ejemplo (Cerrajeros Madrid 24h):** `madrid`.

### 2.4 — Service Slugs (S=5)
<small>§6.4</small>

**Explicación**

Los Service Slugs son las versiones URL-safe de cada uno de los S core services. Cada slug aparece como segmento final en Service Overview Pages (`/cerrajero/cerrajero-urgente/`) y como segmento `[service-slug]` en LBS (`/cerrajero/madrid/cerrajero-urgente/`). El conjunto tiene cardinalidad S (heredada de §6.6 Variable S).

**Patrón o fórmula**

```text
service_slug[i] = slugify(core_service_name[i])    para cada i ∈ [1..S]
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajero urgente            → cerrajero-urgente
Apertura de puertas          → apertura-puertas
Cambio de cerraduras         → cambio-cerraduras
Cambio de bombines           → cambio-bombines
Instalación de cerraduras de seguridad → instalacion-cerraduras-seguridad
```

**Ejemplos incorrectos**

```text
- cerrajero-urgente-madrid (incluye ciudad innecesariamente)
- urgentee (typos)
- cerrajero_urgente (subrayado)
- mejor-cerrajero-urgente (modificador inventado)
- urgent-locksmith (idioma cambiado)
- cerrajero-urgente-24h (modificador comercial añadido)
```

**Regla final**

```text
Los Service Slugs son derivados deterministas de los nombres de los core services declarados en Paso-01 1.9. Hay exactamente S slugs (uno por core service).
```

**Validación operativa**

Aplicar slugify a cada uno de los S core services declarados en Paso-01 1.9. Si la Service-to-Main-City Applicability (§6.5) excluye algún servicio de Main City, el slug sigue existiendo (se usa en Service Overview general) pero NO genera LBS para esa ciudad. La cardinalidad de service slugs se mantiene en S, no en S_efectiva.

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso-01 1.9 Servicios principales.
- **Método:** Aplicar slugify a cada core service del Paso-01 1.9. Reutilizar como `[service-slug]` en patrones URL del Paso 4 (Paso-04 §8 Service Overview pattern, Paso-04 §10 LBS pattern).

**Output del paso**

- **Tipo:** Lista de S strings URL-safe (1 slug por core service).
- **Ejemplo (Cerrajeros Madrid 24h):** `cerrajero-urgente`, `apertura-puertas`, `cambio-cerraduras`, `cambio-bombines`, `instalacion-cerraduras-seguridad` (S=5).

### 2.5 — Service-to-Main-City Applicability
<small>§6.5</small>

**Explicación**

Por defecto, la fórmula asume que TODOS los servicios core aplican a la Main City. Si el cliente no ofrece un servicio en la Main City (por logística, capacidad o decisión comercial), se excluye y NO genera Location-Based Service Page ni GeoArticles para esa ciudad.

**Patrón o fórmula**

```text
Default: applicability(service, main_city) = true ∀ service ∈ S
Si exclusiones: S_efectiva = S − count(exclusiones)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
¿Todos los servicios aplican a Madrid? Yes
Exclusiones: ninguna
S_efectiva = 5
```

**Ejemplos incorrectos**

```text
- Asumir applicability sin preguntar al cliente
- Generar LBS de un servicio que el cliente no ofrece en Main City
- Excluir un servicio sin documentar la razón comercial
- Aplicar exclusiones de Main City a Approved Expansion Areas sin reevaluar
```

**Regla final**

```text
Por defecto todos los servicios aplican a la Main City; las exclusiones reducen S efectiva en la fórmula base.
```

**Validación operativa**

La pregunta debe hacerse explícitamente al cliente. Si todos los servicios aplican (caso default), `S_efectiva = S` y la fórmula queda intacta. Si hay exclusiones, hay que recalcular `S_efectiva` y revisar el inventario LBS y GeoArticles del Bloque III. La exclusión solo aplica a la Main City; servicios excluidos pueden aplicar en Approved Expansion Areas (§6.11) si las hay.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Input humano.
- **Método:** Preguntar al cliente «¿Todos los servicios aplican a la Main City?». Si Sí (default web-first según doctrina): `S_efectiva = S` y la fórmula queda intacta. Si No: registrar las exclusiones declaradas por el cliente con su razón, recalcular `S_efectiva` y propagar al inventario LBS y GeoArticles base.

**Output del paso**

- **Tipo:** Boolean (Yes/No) + lista de exclusiones (si aplica).
- **Ejemplo (Cerrajeros Madrid 24h):** Yes — todos los 5 servicios aplican a Madrid. S_efectiva = 5.

### 2.6 — Variable S
<small>§6.6</small>

**Explicación**

S representa los servicios principales (core services). Cada servicio core genera una Service Overview Page y una Main City Location-Based Service Page. S es el multiplicador principal de la fórmula base.

**Patrón o fórmula**

```text
S = número de core services aprobados (Paso-01 1.9)
S_efectiva = S − count(exclusiones declaradas en §6.5)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h tiene S = 5: Cerrajero urgente, Apertura de puertas, Cambio de cerraduras, Cambio de bombines y Instalación de cerraduras de seguridad.
Sin exclusiones → S_efectiva = 5.
```

**Ejemplos incorrectos**

```text
- Contar categorías adicionales como servicios core duplicados
- Contar cada variación de llaveword como servicio
- Crear un servicio para cada sinónimo
- Contar urgente cerrajero y cerrajero urgente como servicios separados
- Incluir duplicado de llaves en S si se tratará como categoría adicional
- Contar servicios que no tienen valor comercial suficiente
```

**Regla final**

```text
S solo incluye servicios core reales y principales que merecen página propia.
```

**Validación operativa**

La variable S solo cuenta servicios principales reales. Esta regla evita que sinónimos, modificadores o subcasos inflen la fórmula. Si un servicio no merece una página general y una página local, probablemente no debe entrar como servicio core en la fórmula base.

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso-01 1.9 Servicios principales.
- **Método:** Tomar el conteo de core services declarados en el Paso 1. Solo cuentan servicios reales con valor comercial. No inflar con sinónimos, modificadores ni subcasos. Aplicar S_efectiva si hay exclusiones (§6.5).

**Output del paso**

- **Tipo:** Entero — número de core services aprobados.
- **Ejemplo (Cerrajeros Madrid 24h):** S = 5 (Cerrajero urgente, Apertura de puertas, Cambio de cerraduras, Cambio de bombines, Instalación de cerraduras de seguridad).

### 2.7 — Variable A
<small>§6.7</small>

**Explicación**

A representa categorías adicionales que necesitan página separada. Si una categoría adicional ya está cubierta por un core service, no entra en A. A es el multiplicador secundario de la fórmula base, dependiente de las Planned Additional GBP Categories.

**Patrón o fórmula**

```text
A = count(Planned Additional Categories) − count(cubiertas por core services)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h tiene 2 Planned Additional Categories:
- Servicio de cerrajería de urgencia → cubierta por core service Cerrajero urgente → NO suma a A
- Servicio de duplicado de llaves → no cubierta → suma a A
A = 1
```

**Ejemplos incorrectos**

```text
- A = 2 contando Servicio de cerrajería de urgencia dos veces
- A = 0 ignorando Servicio de duplicado de llaves
- Crear páginas sin relación con GBP
- A = 2 aunque una categoría sea duplicada
- Crear páginas separadas para urgente cerrajero y urgente cerrajero service
- Ignorar categorías adicionales que sí necesitan soporte
```

**Regla final**

```text
A cuenta categorías adicionales efectivas, no etiquetas repetidas ni cubiertas por core services.
```

**Validación operativa**

La variable A no es igual al número total de categorías adicionales del GBP. Solo cuenta las que no están cubiertas por un servicio core. Esto evita duplicaciones y mantiene la fórmula realista. La consolidación se hace mediante el control anti-duplicación (§6.12).

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso-01 1.6 Planned Additional GBP Categories.
- **Método:** Contar las Planned Additional Categories que NO están cubiertas por core services. Las cubiertas no suman a A (ver §6.12 Control anti-duplicación).

**Output del paso**

- **Tipo:** Entero — categorías adicionales efectivas que requieren página propia.
- **Ejemplo (Cerrajeros Madrid 24h):** A = 1 (Servicio de duplicado de llaves; Servicio de cerrajería de urgencia queda cubierta por core service).

### 2.8 — Variable G
<small>§6.8</small>

**Explicación**

G representa cuántos GeoArticles se crean por servicio dentro de la Main City. Es el multiplicador de profundidad semántica del cluster base.

**Patrón o fórmula**

```text
G × S = GeoArticles base de la Main City
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Con G = 3 y S = 5, Cerrajeros Madrid 24h genera 15 GeoArticles para Madrid.
```

**Ejemplos incorrectos**

```text
- G × S × C con C = varias ciudades en base
- Crear 75 artículos antes de tener landings
- Crear artículos sin destino interno
- Crear 3 artículos por servicio y por cada cobertura local
- Publicar artículos antes de crear la página servicio+ciudad
- Usar G = 10 sin capacidad de producción o refresh
```

**Regla final**

```text
Los GeoArticles base refuerzan Main City + servicio. No se multiplican por Local Coverage Areas.
```

**Validación operativa**

La variable G representa cuántos GeoArticles se crean por servicio en la Main City. No debe multiplicarse por áreas de cobertura en la base. Esto permite tener profundidad semántica sin producir decenas de artículos antes de tener landings comerciales sólidas.

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso-01 1.12 GeoArticles per Service.
- **Método:** Tomar el valor de G capturado en el Paso 1 (default 3). Aplicar `G × S_efectiva` para obtener el total de GeoArticles del cluster Main City. No multiplicar por Local Coverage Areas (§6.14).

**Output del paso**

- **Tipo:** Entero — GeoArticles por servicio core.
- **Ejemplo (Cerrajeros Madrid 24h):** G = 3 → G × S = 15 GeoArticles para Madrid.

### 2.9 — Total páginas SEO base
<small>§6.9</small>

**Explicación**

El total de páginas SEO base es el resultado de aplicar la fórmula maestra `1 + S + 1 + S + A + G × S` con los valores efectivos de S (§6.6), A (§6.7) y G (§6.8) del cluster Main City. Es el handoff principal hacia el Paso 3 (URL Matrix). El total debe ser auditable componente a componente — si no se puede explicar por descomposición, no está listo para producción (validación cruzada con §6.15).

**Patrón o fórmula**

```text
Total = 1 (Homepage)
      + S (Service Overview Pages)
      + 1 (Main City GeoHub)
      + S (Main City Location-Based Service Pages)
      + A (Páginas de categoría adicional en la Main City)
      + (G × S) (GeoArticles de la Main City)

Forma compacta: 1 + S + 1 + S + A + (G × S)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
S = 5, A = 1, G = 3
Total = 1 + 5 + 1 + 5 + 1 + (3 × 5)
      = 1 + 5 + 1 + 5 + 1 + 15
      = 28 páginas SEO base

Adicionalmente: /contacto/ como página auxiliar fuera del inventario SEO base.
```

**Ejemplos incorrectos**

```text
- 1 + 5 ciudades + 25 city-service pages sin validación (multi-ciudad en base)
- Incluir Almagro, Salamanca y Retiro como URLs por defecto (LCAs)
- Usar C = 4 porque hay cuatro Local Coverage Areas
- Crear GeoHubs para todas las zonas sin haber terminado Madrid
- Calcular artículos por cada Local Coverage Area
- Seguir usando la fórmula multi-ciudad de 111 páginas en la base
- No contar GeoArticles y dejar el sistema sin boosters
- Publicar 28 páginas sin desglose auditable
- Confundir el Total con un calendario de publicación
```

**Regla final**

```text
El Total es el resultado de la fórmula maestra `1 + S + 1 + S + A + G × S` aplicada con C = 1 Main City. Debe entregarse acompañado de su descomposición auditable (ver §6.10 Inventario y §6.15 Validación auditabilidad).
```

**Validación operativa**

El cálculo se hace con S_efectiva (§6.5) cuando hay exclusiones. El Total NO incluye páginas de expansión (§6.11) ni la página auxiliar `/contacto/`. Si el resultado no se puede explicar componente a componente, hay que revisar el cálculo antes de pasar al Paso 3.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la fórmula `1 + S + 1 + S + A + G × S` con los valores S (§6.6), A (§6.7), G (§6.8). Acompañar siempre del desglose en §6.10 (Inventario) y validar con §6.15 (Auditabilidad). Las Local Coverage Areas (§6.14) NO entran. Las Approved Expansion Areas (§6.11) se calculan aparte.

**Output del paso**

- **Tipo:** Entero — total de páginas SEO base del cluster Main City.
- **Ejemplo (Cerrajeros Madrid 24h):** Total = 1 + 5 + 1 + 5 + 1 + 15 = **28 páginas SEO base**.

### 2.10 — Inventario por tipo de página
<small>§6.10</small>

**Explicación**

El inventario es la presentación tabular del Total (§6.9) desglosada por tipo de página. Es el handoff directo al Paso 3 (URL Matrix), que consume esta tabla para generar las URLs concretas. Sirve también como mapa de contenido para los pasos posteriores (Paso 4 patterns, Paso 5 page type rules, Paso 6 content architecture, Paso 7 internal linking).

**Patrón o fórmula**

| Tipo de página | Fórmula | Ejemplo Cerrajeros Madrid 24h |
|---|---:|---:|
| Homepage | 1 | 1 |
| Service Overview Pages | S | 5 |
| Main City GeoHub | 1 | 1 |
| Main City Location-Based Service Pages | S | 5 |
| Páginas de categoría adicional en la Main City | A | 1 |
| GeoArticles de la Main City | G × S | 15 |
| **Total base** | — | **28** |
| `/contacto/` (auxiliar fuera SEO base) | 1 | 1 |

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
1 Homepage
+ 5 Service Overview Pages (uno por core service)
+ 1 Main City GeoHub (/madrid/)
+ 5 Location-Based Service Pages (uno por core service en Madrid)
+ 1 Additional Category Page (duplicado de llaves)
+ 15 GeoArticles (3 por core service × 5 servicios)
= 28 páginas SEO base
+ 1 página auxiliar (/contacto/)
```

**Ejemplos incorrectos**

```text
- Dar el total 28 sin desglosar por tipo
- Mezclar /contacto/ dentro del conteo SEO base
- Confundir inventario con calendario de publicación
- No explicar por qué A = 1
- Mezclar páginas de expansión con base
- Listar URLs concretas en lugar de cantidades por tipo (eso es el Paso 3)
```

**Regla final**

```text
El inventario debe entregarse como tabla auditable componente a componente, una fila por tipo de página. NO es un calendario de publicación.
```

**Validación operativa**

La tabla termina con el Total base (§6.9) y, separado, la página auxiliar `/contacto/`. El orden y ritmo de publicación se decide en el Paso 10 (Producción en fases), no aquí. Si la tabla no es explicable componente a componente, falla la validación auditabilidad (§6.15) y hay que revisar.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar S (§6.6), A (§6.7), G (§6.8) a la fórmula base (§6.9) y desplegar en tabla. El handoff al Paso 3 es la tabla, no solo el número total.

**Output del paso**

- **Tipo:** Tabla de inventario por page type (6 page types + auxiliar).
- **Ejemplo (Cerrajeros Madrid 24h):** Homepage=1 / SO=5 / GeoHub=1 / LBS=5 / AC=1 / GAs=15 / Total=28 / +1 `/contacto/`.

### 2.11 — Optional Expansion Formula
<small>§6.11</small>

**Explicación**

La fórmula de expansión opcional declara cómo escalar el cluster cuando una Local Coverage Area pasa a Approved Expansion Area (Paso-01 1.11). Cada zona aprobada genera su propio sub-cluster (GeoHub + LBS + Additional Category + GeoArticles) calculado APARTE de la base. En Phase 1 default `E = 0`, por lo que la fórmula está declarada pero no genera páginas. Es decisión de diseño del cliente activar expansión.

**Patrón o fórmula**

```text
Solo si una Local Coverage Area pasa a Approved Expansion Area:

Total expansion = E × (1 + S + A + G × S)
                = E Expansion GeoHubs
                + S × E Expansion Service Pages
                + A × E Expansion Additional Category Pages
                + G × S × E Expansion GeoArticles

donde E = count(Approved Expansion Areas).
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Phase 1: E = 0 (None in Phase 1)
→ 0 páginas de expansión generadas
→ Fórmula declarada y lista para activación futura

Hipotético Phase 2 (si Almagro se aprueba como AEA):
E = 1, S = 5, A = 1, G = 3

Páginas extra para Almagro:
1 GeoHub (/almagro/)
+ 5 Service Pages (/cerrajero/almagro/cerrajero-urgente/, ...)
+ 1 Additional Category Page (/cerrajero/almagro/duplicado-llaves/)
+ 15 GeoArticles (/almagro/cuanto-cuesta-un-cerrajero-urgente/, ...)
= 22 páginas extra (módulo separado de la base)
```

**Ejemplos incorrectos**

```text
- Mezclar expansión con la fórmula base (sumar al Total de §6.9)
- Aprobar todas las Local Coverage Areas como AEA por defecto
- Expandir antes de terminar el cluster Main City
- No exigir página padre publicable antes de generar expansión
- Activar AEA sin demanda comercial verificada
- Publicar /almagro/ sin haber definido sus core services aplicables
- Calcular expansión por cada LCA mencionada en contenido (eso son señales GEO, no AEA)
```

**Regla final**

```text
La expansión se calcula APARTE de la base y solo con zonas aprobadas explícitamente como Approved Expansion Areas. La fórmula está declarada en este paso pero su activación es decisión de diseño futura.
```

**Validación operativa**

Si E = 0 (default Phase 1), la fórmula queda como spec lista para activar sin re-deducir el sistema. Si E ≥ 1, cada AEA aprobada genera sub-cluster propio que se entrega COMO MÓDULO separado al Paso 3 — no se mezcla con el inventario base. La distinción AEA vs LCA (§6.14) es crítica: las LCAs viven en contenido y schema, NO generan URLs.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Declarar la fórmula `E × (1 + S + A + G × S)` aunque E=0 en Phase 1. Si Paso-01 1.11 reporta AEAs aprobadas, aplicar la fórmula con E = count(AEAs) y entregar sub-cluster aparte. Por defecto en web-first la decisión de expansión queda diferida hasta tener el cluster base sólido.

**Output del paso**

- **Tipo:** Fórmula declarada (paramétrica en E) + (opcional) cálculo de páginas de expansión.
- **Ejemplo (Cerrajeros Madrid 24h):** Phase 1: E = 0 → 0 páginas de expansión. Fórmula declarada lista para activación futura.

### 2.12 — Validación anti-duplicación
<small>§6.12</small>

**Explicación**

Antes de cerrar el conteo, el Paso 2 debe detectar duplicados entre core services y categorías adicionales. Si no se hace, el Total parece completo pero incluye páginas que compiten entre sí en la misma intención local. La validación protege contra inflación artificial de A (§6.7).

**Patrón o fórmula**

```text
Para cada Planned Additional Category (Paso-01 1.6):
  Si su intención comercial coincide con un core service (Paso-01 1.9):
    Categoría = "cubierta" → NO suma a A
  Si no:
    Categoría = "necesita página propia" → suma a A

Resultado: A = count(categorías que necesitan página propia, sin duplicar core).
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Planned Additional Categories:
- Servicio de cerrajería de urgencia → coincide con core service "Cerrajero urgente"
  → cubierta → NO suma a A
- Servicio de duplicado de llaves → no coincide con ningún core service
  → necesita página propia → suma a A

A = 1 (no A = 2).
URL única para la intención "cerrajería de urgencia": /cerrajero/madrid/cerrajero-urgente/
```

**Ejemplos incorrectos**

```text
- Sumar cerrajero-urgente como página adicional cuando ya es core service
- Crear /cerrajero/madrid/urgencias-cerrajero/ + /cerrajero/madrid/cerrajero-urgente/ (dos URLs misma intención)
- Contar duplicados como oportunidades nuevas
- Inflar A para tener más páginas
```

**Regla final**

```text
Una intención comercial = una sola URL principal. La consolidación se hace ANTES de cerrar el conteo, no después.
```

**Validación operativa**

La IA recorre las Planned Additional Categories del Paso-01 1.6 y descarta las que coinciden en intención comercial con un core service. El número final de A debe ser explicable POR EXCLUSIÓN, no por inflación. La regla aplica también entre LBS y Additional Category Pages: si dos URLs apuntan a la misma intención, consolidar y redirigir 301 la perdedora.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Antes de cerrar el conteo, comparar cada Planned Additional Category con la lista de core services. Si una categoría adicional coincide en intención comercial con un core service, NO suma a A. Documentar las consolidaciones realizadas.

**Output del paso**

- **Tipo:** Validation flag + lista de duplicados detectados y consolidados.
- **Ejemplo (Cerrajeros Madrid 24h):** Servicio de cerrajería de urgencia → consolidado con core service Cerrajero urgente (no suma a A). Validación: OK.

### 2.13 — Validación dependencias entre páginas
<small>§6.13</small>

**Explicación**

El cálculo del cluster no solo mide cantidad: también valida dependencias jerárquicas. Una GeoArticle no debe existir antes de su página padre (LBS). Una LBS necesita Service Overview y GeoHub publicables. Si las dependencias no se respetan, el sitio publica páginas hijas huérfanas que no pueden enlazar a su padre.

**Patrón o fórmula**

```text
Jerarquía obligatoria de publicación:
Homepage
  → Service Overview Pages
  → GeoHub Main City
  → Location-Based Service Pages
  → Additional Category Pages
  → GeoArticles

Cada página hija requiere su padre publicable Y destino de enlace interno.
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
El artículo /madrid/cuanto-cuesta-un-cerrajero-urgente/
se programa después de:
  - /cerrajero/madrid/cerrajero-urgente/ (LBS padre)
  - /madrid/ (GeoHub padre)
  - /cerrajero/cerrajero-urgente/ (SO abuelo)
```

**Ejemplos incorrectos**

```text
- Publicar artículo sin landing comercial creada
- Crear guía de Almagro sin expansión aprobada (no existe /almagro/)
- Publicar GeoHub sin enlazar a servicios
- Crear LBS sin Service Overview
- Contar artículos sin landings de destino
- Empezar la producción por GeoArticles "porque hay 15"
```

**Regla final**

```text
Cada página contada debe tener padre publicable y destino de enlace interno; ningún artículo va antes de su landing.
```

**Validación operativa**

El conteo no solo mide cantidad; también prevé dependencias. Antes de cerrar el inventario (§6.10), validar que el orden Homepage → SO → GeoHub → LBS → AC → GAs es respetable. Esto se traduce al calendario en Paso 10 (Producción en fases).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Validar dependencias antes de cerrar el inventario. Para cada page type contado, verificar que su padre jerárquico también está contado y publicable. Documentar el orden viable.

**Output del paso**

- **Tipo:** Validation flag + mapa de dependencias resuelto.
- **Ejemplo (Cerrajeros Madrid 24h):** Orden Homepage → SO → GeoHub → LBS → AC → GAs validado. `/madrid/cuanto-cuesta-un-cerrajero-urgente/` se programa después de `/cerrajero/madrid/cerrajero-urgente/` y `/madrid/`. Validación: OK.

### 2.14 — Validación LCAs fuera fórmula
<small>§6.14</small>

**Explicación**

Las Local Coverage Areas (Paso-01 1.10) son zonas, barrios o landmarks seleccionados como señales GEO. Se usan dentro del CONTENIDO (FAQs, ejemplos locales, schema `areaServed`), pero NO crean filas en el inventario base ni URLs propias. La validación garantiza que el conteo no se infla por incluirlas como multiplicadores.

**Patrón o fórmula**

```text
Local Coverage Areas → contenido (FAQs, ejemplos, areaServed)
                     ↛ filas de inventario
                     ↛ URLs propias en la base

count(LCAs) NO entra como multiplicador en la fórmula `1 + S + 1 + S + A + G × S`.
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LCAs declaradas (Paso-01 1.10):
- Direct: Almagro, Chamberí
- Candidate: Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad

Total LCAs = 10
Páginas adicionales generadas por LCAs = 0
Las LCAs aparecen en:
  - Contenido textual de LBS y GeoHub (Paso 6)
  - Schema areaServed (Paso 8)
  - FAQs (Paso 6)
  - NO en URLs base
```

**Ejemplos incorrectos**

```text
- Crear /almagro/ por defecto porque está en LCAs
- Multiplicar servicios por áreas de cobertura (S × C con C = LCAs)
- Contar Local Coverage Areas como C en la fórmula
- Crear páginas para cada zona mencionada en contenido
- Eliminar las LCAs del paso porque "no generan URLs" (sí aparecen, en contenido)
- Usar LCAs como slugs de URLs base
```

**Regla final**

```text
Mencionar una zona como LCA refuerza contenido y schema. NO crea inventario. Para que una LCA genere URLs, debe pasar a Approved Expansion Area (§6.11).
```

**Validación operativa**

Las LCAs son importantes pero no son multiplicadores. El paso de LCA → AEA es decisión de diseño explícita (Paso-01 1.11), no automática. Esta regla evita que cobertura real se convierta automáticamente en arquitectura. Validar antes de cerrar el inventario que NO hay LCAs sumando a la fórmula.

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso-01 1.10 Local Coverage Areas.
- **Método:** Las LCAs (Direct + Candidate) heredadas del Paso 1 NO se usan como multiplicador. Validar explícitamente que el inventario (§6.10) NO contiene filas extras por LCAs. Documentar las LCAs como señales de contenido para Paso 6 y Paso 8.

**Output del paso**

- **Tipo:** Validation flag — 0 URLs adicionales en la base por LCAs.
- **Ejemplo (Cerrajeros Madrid 24h):** Almagro, Chamberí, Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad → 0 páginas adicionales en cluster base. Validación: OK.

### 2.15 — Validación auditabilidad del total
<small>§6.15</small>

**Explicación**

El Total (§6.9) y el Inventario (§6.10) deben ser AUDITABLES — explicables componente a componente con la fórmula `1 + S + 1 + S + A + G × S` y los valores S, A, G heredados del Paso 1. Si el número final no se puede descomponer fila por fila, no está listo para producción. Esta validación es la última puerta antes de pasar al Paso 3 (URL Matrix).

**Patrón o fórmula**

```text
Para cada page type del inventario, verificar:
  - Su cantidad es expresable como función de S, A o G
  - Su componente en la fórmula es identificable
  - Su contribución al Total es trazable

Resultado esperado:
  Total = Σ (cantidad por page type) = 1 + S + 1 + S + A + G × S
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Auditando el Total = 28:
  1 Homepage         ← constante
  5 SO Pages         ← S = 5 (§6.6)
  1 Main City GeoHub ← constante
  5 LBS Pages        ← S = 5 (§6.6)
  1 Additional Cat.  ← A = 1 (§6.7)
  15 GeoArticles     ← G × S = 3 × 5 = 15 (§6.8 × §6.6)
  ────────────────
  Total = 1 + 5 + 1 + 5 + 1 + 15 = 28

Cada componente trazable. Validación: OK.
```

**Ejemplos incorrectos**

```text
- Dar el Total = 28 sin desglose
- Decir "más o menos 30 páginas" sin componente exacto
- No explicar por qué A = 1 (debería remitir al control anti-duplicación §6.12)
- Mezclar páginas de expansión en el Total (eso es §6.11, separado)
- Confundir el Total con calendario de publicación (eso es Paso 10)
- Dar un número distinto al de la fórmula sin justificar la divergencia
```

**Regla final**

```text
El Total debe ser explicable componente a componente con la fórmula maestra. Si no se puede auditar, no se entrega al Paso 3.
```

**Validación operativa**

La validación auditabilidad es un gate antes del handoff al Paso 3. Para cada page type del inventario (§6.10), confirmar que su cantidad coincide con la fórmula correspondiente (1, S, A o G×S). Si hay divergencias (ej. "tenemos 4 SO pages pero S=5"), investigar antes de avanzar. La validación se complementa con §6.12 (anti-duplicación), §6.13 (dependencias) y §6.14 (LCAs fuera fórmula) — las cuatro juntas son las puertas de calidad del Paso 2.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Recorrer el inventario (§6.10) row por row y verificar que cada cantidad es función de las variables declaradas (S §6.6, A §6.7, G §6.8). Confirmar que el Total = suma de todas las cantidades = aplicación directa de la fórmula maestra. Documentar la traza.

**Output del paso**

- **Tipo:** Validation flag — Total auditable componente a componente.
- **Ejemplo (Cerrajeros Madrid 24h):** Total 28 = 1 + 5 + 1 + 5 + 1 + 15 = 1 + S + 1 + S + A + (G × S). Validación: OK.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 2 y avanzar al Paso 3 (URL Matrix). Cada ☐ es un check que debe pasar antes del handoff.

### Validación de outputs

- ☐ Todos los outputs de §5 tienen valor calculado para el negocio
- ☐ Slugs derivados con slugify estándar (sin tildes, lowercase, dashes)
- ☐ S_efectiva calculada y aplicada a la fórmula
- ☐ A excluye categorías cubiertas por core services
- ☐ G × S calculado correctamente para Main City

### Validación de reglas

- ☐ Una sola Main City multiplica
- ☐ LCAs NO multiplican (mencionadas en contenido y schema, no en URL)
- ☐ AEAs NO entran en la fórmula base (separadas en Optional Expansion)
- ☐ Dependencias resueltas (orden Homepage → SO → GeoHub → LBS → AC → GAs)
- ☐ Anti-duplicación validada (intención = una URL)

### Validación de auditabilidad

- ☐ Total componente a componente explicable
- ☐ Tabla de inventario base completa
- ☐ Optional Expansion Formula declarada (aunque E=0)

## Outputs Consolidados

<small>§8</small>

> Tabla final con valores reales para Cerrajeros Madrid 24h y status de cada output. Los IDs (`2.1`–`2.15`) coinciden con los declarados en §5.

| ID | Output | Valor (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|
| 2.1 | Planned GBP Categories Status | Cerrajero (Planned) + 2 Additional (Planned) | confirmed |
| 2.2 | Primary Category Slug | `cerrajero` | confirmed |
| 2.3 | Main City Slug | `madrid` | confirmed |
| 2.4 | Service Slugs (5) | `cerrajero-urgente`, `apertura-puertas`, `cambio-cerraduras`, `cambio-bombines`, `instalacion-cerraduras-seguridad` | confirmed |
| 2.5 | Service-to-Main-City Applicability | Yes / 0 exclusiones / S_efectiva = 5 | confirmed |
| 2.6 | Variable S | 5 | confirmed |
| 2.7 | Variable A | 1 (Servicio de duplicado de llaves) | confirmed |
| 2.8 | Variable G | 3 | confirmed |
| 2.9 | Total páginas SEO base | 1 + 5 + 1 + 5 + 1 + 15 = **28** | confirmed |
| 2.10 | Inventario por tipo de página | Homepage=1 / SO=5 / GeoHub=1 / LBS=5 / AC=1 / GAs=15 | confirmed |
| 2.11 | Optional Expansion Formula | E=0 → 0 páginas (declarada para activación futura) | confirmed |
| 2.12 | Validación anti-duplicación | Servicio de cerrajería de urgencia consolidada con core service Cerrajero urgente | OK |
| 2.13 | Validación dependencias | Orden Homepage → SO → GeoHub → LBS → AC → GAs validado | OK |
| 2.14 | Validación LCAs fuera fórmula | Almagro, Chamberí, Salamanca, Retiro, etc. → 0 páginas adicionales | OK |
| 2.15 | Validación auditabilidad del total | 28 explicable componente a componente | OK |

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

### GeoArticles completos (15)

<small>§9.1</small>

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

> **Nota importante — GBP Services ≠ core services del sitio web:**
> Las categorías adicionales del Google Business Profile (como "Servicio de duplicado de llaves") pueden tener página propia en la web, pero **no forman parte de `core_services`**. La variable `core_services` define los 5 servicios principales que generan Service Overview, LBS y GeoArticles. Las Additional Categories con página propia se gestionan por separado mediante `additional_categories_with_page`. No mezclar ambos conjuntos.
