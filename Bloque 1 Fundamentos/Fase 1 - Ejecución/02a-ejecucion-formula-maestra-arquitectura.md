Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo la estructura fija acordada en la conversación.
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# Paso 2 — Fórmula Maestra de Arquitectura

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso, qué hereda y qué resultado ejemplo se espera.
> - **Bloque II — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, reglas que aplican, checklist final y outputs consolidados.
> - **Bloque III — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

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
- **2.8** Variable G — GeoArticles per Service (heredado del Paso 1 §16)
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
| Business Name | Paso 1 §5 |
| Planned Primary GBP Category | Paso 1 §9 |
| Servicios principales (5 core services) | Paso 1 §13 |
| Planned Additional GBP Categories | Paso 1 §10 |
| Additional Categories cubiertas por core services | Paso 1 §10 (consolidación) |
| Additional Categories que necesitan página propia | Paso 1 §10 (consolidación) |
| Main City | Paso 1 §11 |
| Local Coverage Areas | Paso 1 §14 |
| Approved Expansion Areas | Paso 1 §15 |
| GeoArticles per Service (G) | Paso 1 §16 |

> Los outputs nuevos que se producen en Paso 2 (Slug Generation y Service-to-Main-City Applicability) tienen sus propias secciones en Bloque II — §6.2 y §6.5.

## Ejemplo rellenado

<small>§4</small>

> Los 15 outputs del Paso 2 con sus valores para Cerrajeros Madrid 24h. Los inputs heredados (Business Name, Categories, Servicios, LCAs, etc.) tienen su ejemplo en sus pasos de origen (§4 de Paso 1).

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

`S = 5` (5 core services declarados en Paso 1 §13)

### 2.7 — Variable A

`A = 1` (Solo Servicio de duplicado de llaves necesita página propia; Servicio de cerrajería de urgencia queda cubierta por core service Cerrajero urgente)

### 2.8 — Variable G

`G = 3` (heredado del Paso 1 §16)

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

# Bloque II — Ejecución por la IA

> **Definición operativa — Local Coverage Areas:** zonas, barrios, distritos o landmarks seleccionados desde la dirección física, la Main City, la coherencia GEO, la proximidad, los datos de búsqueda, los competidores y la lógica GMB Crush para reforzar relevancia local dentro del contenido, schema y futuros análisis. No son automáticamente URLs. No son automáticamente páginas propias. No son necesariamente oficinas físicas. Las Local Coverage Areas se usan primero como señales GEO dentro del contenido. No generan URLs por defecto.

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 15 outputs que el Paso 2 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `2.1`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Origen |
|---|---|---|---|
| 2.1 | Planned GBP Categories Status | Status (`Planned` hasta Paso 14) | GMB Crush ← Paso 1 §9 + Paso 1 §10 |
| 2.2 | Primary Category Slug | URL-safe string | GMB Crush ← Paso 1 §9 |
| 2.3 | Main City Slug | URL-safe string | GMB Crush ← Paso 1 §11 |
| 2.4 | Service Slugs (S=5) | URL-safe strings | GMB Crush ← Paso 1 §13 |
| 2.5 | Service-to-Main-City Applicability | Boolean + exclusiones | GMB Crush + Input humano |
| 2.6 | Variable S (S_efectiva) | Entero | GMB Crush ← Paso 1 §13 |
| 2.7 | Variable A | Entero | GMB Crush ← Paso 1 §10 |
| 2.8 | Variable G | Entero | GMB Crush ← Paso 1 §16 |
| 2.9 | Total páginas SEO base | Entero (28 para Cerrajeros) | Fórmula `1+S+1+S+A+G×S` |
| 2.10 | Inventario por tipo de página | Tabla 6 page types | Aplicación de la fórmula |
| 2.11 | Optional Expansion Formula | Fórmula declarada | GMB Crush |
| 2.12 | Validación anti-duplicación | Validation flag | GMB Crush |
| 2.13 | Validación dependencias | Validation flag | GMB Crush |
| 2.14 | Validación LCAs fuera fórmula | Validation flag | GMB Crush |
| 2.15 | Validación auditabilidad del total | Validation flag | GMB Crush |

## Reglas que Aplican

<small>§6</small>

> Esta sección contiene los 15 outputs operativos del Paso 2. Cada uno se desarrolla con el mismo patrón: Explicación / Patrón o fórmula / Ejemplos / Regla final / Validación operativa / Cómo se obtiene / Output del paso.

### Planned GBP Categories Before GBP Creation
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

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Marcar todas las categorías GBP planificadas como `Planned` hasta que el Paso 14 cree y verifique el GBP. La arquitectura web se construye sobre la Planned Primary y solo soporta Planned Additional que necesitan página separada (cruce con §6.6 Variable A).

**Output del paso**

- **Tipo:** Status declarado de categorías GBP — `Planned` hasta el Paso 14.
- **Ejemplo (Cerrajeros Madrid 24h):** Planned Primary: Cerrajero. Planned Additional: Servicio de cerrajería de urgencia (cubierta por core service), Servicio de duplicado de llaves (necesita página propia).

### Slug Generation
<small>§6.2</small>


**Explicación**

Los slugs son las versiones URL-safe de Business Name, Primary Category, Main City y cada Service core. Se derivan mecánicamente y se reutilizan en URLs (Paso 4), schema canonical, breadcrumbs y internal linking.

**Patrón o fórmula**

```text
slug(text) = lowercase(text)
           → remove_diacritics()
           → replace_non_alphanumeric_with('-')
           → collapse_consecutive_dashes()
           → trim_leading_trailing_dashes()
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Primary Category: Cerrajero          → cerrajero
Main City: Madrid                    → madrid
Service: Cerrajero urgente           → cerrajero-urgente
Service: Apertura de puertas         → apertura-puertas
Service: Cambio de cerraduras        → cambio-cerraduras
Service: Cambio de bombines          → cambio-bombines
Service: Instalación de cerraduras de seguridad → instalacion-cerraduras-seguridad
```

**Ejemplos incorrectos**

```text
- Slugs con tildes (cerrajería)
- Slugs con espacios (cerrajero urgente)
- Slugs con mayúsculas (Cerrajero-Urgente)
- Slugs largos repetitivos (cerrajero-urgente-madrid-cerrajero)
- Slugs inventados que no derivan del nombre original
```

**Regla final**

```text
Los slugs son derivados deterministas de los nombres heredados; nunca se inventan.
```

**Validación operativa**

La transformación es determinista: lowercase + remove diacritics + replace non-alphanumeric con dash + collapse multiple dashes. La IA no inventa slugs; los deriva mecánicamente del Business Name (Paso 1 §5), Primary Category (Paso 1 §9), Main City (Paso 1 §11) y cada Service (Paso 1 §13). Si el cliente exige un slug distinto del derivado, hay que documentarlo como excepción.

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredados del Paso 1.
- **Método:** Aplicar la transformación slugify a Primary Category (Paso 1 §9), Main City (Paso 1 §11) y a cada uno de los servicios principales (Paso 1 §13). Reutilizar los slugs en todas las URLs y schema del Paso 4 en adelante.

**Output del paso**

- **Tipo:** Conjunto de slugs URL-safe (1 Primary + 1 Main City + S Services).
- **Ejemplo (Cerrajeros Madrid 24h):** `cerrajero` / `madrid` / `cerrajero-urgente`, `apertura-puertas`, `cambio-cerraduras`, `cambio-bombines`, `instalacion-cerraduras-seguridad`.

### Fórmula base de una Main City
<small>§6.3</small>


**Explicación**

La versión base no calcula páginas para múltiples ciudades. Calcula una arquitectura sólida para la Main City, que es la ciudad principal del negocio.

**Patrón o fórmula**

```text
1 Homepage + S Service Overview Pages + 1 Main City GeoHub + S Main City Location-Based Service Pages + A Páginas de categoría adicional en la Main City + G × S GeoArticles de la Main City
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Con S = 5, A = 1 y G = 3, Cerrajeros Madrid 24h produce 1 + 5 + 1 + 5 + 1 + 15 = 28 páginas SEO base. Adicionalmente, /contacto/ como página auxiliar fuera del inventario SEO base.
```

**Ejemplos incorrectos**

```text
- 1 + 5 ciudades + 25 city-service pages sin validación
- Incluir Almagro, Salamanca y Retiro como URLs por defecto
- Crear artículos para áreas sin página comercial
- Usar C = 5 porque hay cuatro áreas de cobertura
- Crear GeoHubs para todas las zonas sin haber terminado Madrid
- Calcular artículos por cada Local Coverage Area
- Seguir usando la fórmula multi-ciudad de 111 páginas en la base
- No contar GeoArticles y dejar el sistema sin boosters
- Contar Local Coverage Areas como páginas obligatorias
```

**Regla final**

```text
La fórmula base se multiplica por C = 1 Main City. Debe ser simple, completa y publicable, no por toda la cobertura.
```

**Validación operativa**

La versión base del sistema usa una sola Main City. Esto simplifica la arquitectura y evita que el conteo se dispare por áreas de cobertura. La Main City genera el GeoHub, las páginas servicio+ciudad, páginas adicionales y GeoArticles base.

La fórmula debe devolver un inventario ejecutable, no un mapa teórico inmanejable. En una web local base, el resultado debe contener homepage, service overview pages, Main City GeoHub, Main City service pages, additional category pages y GeoArticles.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la fórmula `1 + S + 1 + S + A + G × S` con los valores de S (§6.4), A (§6.6) y G (§6.7). El resultado da el total de páginas SEO base del cluster Main City. Una sola Main City multiplica — las Local Coverage Areas no entran en la fórmula (§6.8).

**Output del paso**

- **Tipo:** Total de páginas SEO base del cluster Main City.
- **Ejemplo (Cerrajeros Madrid 24h):** 1 + 5 + 1 + 5 + 1 + 15 = 28 páginas SEO base.

### Variable S
<small>§6.4</small>


**Explicación**

S representa los servicios principales. Cada servicio core genera una Service Overview Page y una Main City Location-Based Service Page.

**Patrón o fórmula**

```text
S = número de servicios core aprobados
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h tiene S = 5: Cerrajero urgente, Apertura de puertas, Cambio de cerraduras, Cambio de bombines y Instalación de cerraduras de seguridad.
```

**Ejemplos incorrectos**

```text
- Contar categorías adicionales como servicios core duplicados
- Contar cada variación de llaveword como servicio
- Crear un servicio para cada sinónimo
- Contar urgente cerrajero y urgente cerrajero como servicios separados
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

- **Fuente:** GMB Crush ← heredado del Paso 1 §13 Servicios principales.
- **Método:** Tomar el conteo de core services declarados en el Paso 1. Solo cuentan servicios reales con valor comercial. No inflar con sinónimos, modificadores ni subcasos.

**Output del paso**

- **Tipo:** Entero — número de core services aprobados.
- **Ejemplo (Cerrajeros Madrid 24h):** S = 5 (Cerrajero urgente, Apertura de puertas, Cambio de cerraduras, Cambio de bombines, Instalación de cerraduras de seguridad).

### Service-to-Main-City Applicability
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

La pregunta debe hacerse explícitamente al cliente. Si todos los servicios aplican (caso default), `S_efectiva = S` y la fórmula queda intacta. Si hay exclusiones, hay que recalcular `S_efectiva` y revisar el inventario LBS y GeoArticles del Bloque II. La exclusión solo aplica a la Main City; servicios excluidos pueden aplicar en Approved Expansion Areas (§6.9) si las hay.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Input humano.
- **Método:** Preguntar al cliente «¿Todos los servicios aplican a la Main City?». Si Sí (default web-first según doctrina): `S_efectiva = S` y la fórmula queda intacta. Si No: registrar las exclusiones declaradas por el cliente con su razón, recalcular `S_efectiva` y propagar al inventario LBS y GeoArticles base.

**Output del paso**

- **Tipo:** Boolean (Yes/No) + lista de exclusiones (si aplica).
- **Ejemplo (Cerrajeros Madrid 24h):** Yes — todos los 5 servicios aplican a Madrid. S_efectiva = 5.

### Variable A
<small>§6.6</small>


**Explicación**

A representa categorías adicionales que necesitan página separada. Si una categoría adicional ya está cubierta por un core service, no entra en A.

**Patrón o fórmula**

```text
A = categorías adicionales no cubiertas por servicios core
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h tiene dos categorías adicionales, pero A = 1 porque Servicio de cerrajería de urgencia queda cubierta y Servicio de duplicado de llaves sí necesita página.
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

La variable A no es igual al número total de categorías adicionales del GBP. Solo cuenta las que no están cubiertas por un servicio core. Esto evita duplicaciones y mantiene la fórmula realista.

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso 1 §10 Planned Additional GBP Categories.
- **Método:** Contar las Planned Additional Categories que NO están cubiertas por core services. Las cubiertas no suman a A (ver §6.12 Control anti-duplicación).

**Output del paso**

- **Tipo:** Entero — categorías adicionales efectivas que requieren página propia.
- **Ejemplo (Cerrajeros Madrid 24h):** A = 1 (Servicio de duplicado de llaves; Servicio de cerrajería de urgencia queda cubierta por core service).

### Variable G
<small>§6.7</small>


**Explicación**

G representa cuántos GeoArticles se crean por servicio dentro de la Main City.

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

- **Fuente:** GMB Crush ← heredado del Paso 1 §16 GeoArticles per Service.
- **Método:** Tomar el valor de G capturado en el Paso 1 (default 3). Aplicar `G × S_efectiva` para obtener el total de GeoArticles del cluster Main City. No multiplicar por Local Coverage Areas (§6.8).

**Output del paso**

- **Tipo:** Entero — GeoArticles por servicio core.
- **Ejemplo (Cerrajeros Madrid 24h):** G = 3 → G × S = 15 GeoArticles para Madrid.

### Local Coverage Areas fuera de la fórmula
<small>§6.8</small>


**Explicación**

Las áreas de cobertura local se usan dentro del contenido, FAQs, ejemplos locales y schema areaServed. No crean filas ni URLs por defecto.

**Patrón o fórmula**

```text
Local Coverage Areas → contenido + schema | no → filas de URL
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h menciona Almagro, Chamberí, Salamanca y Retiro en contenido y schema areaServed, pero no las cuenta como GeoHubs base.
```

**Ejemplos incorrectos**

```text
- Crear /almagro/ por defecto
- Multiplicar servicios por áreas de cobertura
- Contar Local Coverage Areas como C
- Crear páginas para cada zona mencionada
- Eliminar las zonas de cobertura porque no generan URLs
- Usar áreas de cobertura como slugs en páginas base
```

**Regla final**

```text
Mencionar una zona como cobertura no crea una URL para esa zona; refuerza contenido y schema, no inventario.
```

**Validación operativa**

Las áreas de cobertura local son importantes, pero no son multiplicadores de páginas. Se usan en contenido, FAQs, ejemplos, schema areaServed y secciones de cobertura. Esta regla evita que cobertura real se convierta automáticamente en arquitectura.

**Cómo se obtiene**

- **Fuente:** GMB Crush ← heredado del Paso 1 §14 Local Coverage Areas.
- **Método:** Las LCAs (Direct + Candidate) heredadas del Paso 1 NO se usan como multiplicador de la fórmula. Se mencionan en contenido, FAQs, ejemplos locales y schema `areaServed`, pero no generan filas en el inventario base.

**Output del paso**

- **Tipo:** LCAs declaradas como señales de contenido — 0 URLs adicionales en la base.
- **Ejemplo (Cerrajeros Madrid 24h):** Almagro, Chamberí, Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad → 0 páginas adicionales en el cluster base.

### Approved Expansion Areas opcional
<small>§6.9</small>


**Explicación**

Si una Local Coverage Area se aprueba como expansión, entonces puede generar su propio hub, service pages y articles.

**Patrón o fórmula**

```text
Optional Expansion = E GeoHubs + S × E Service Pages + A × E Additional Pages + G × S × E Articles
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Si Almagro se aprueba después, Cerrajeros Madrid 24h puede crear /almagro/ y /cerrajero/almagro/cerrajero-urgente/ como expansión, no como base.
```

**Ejemplos incorrectos**

```text
- Mezclar expansión con base
- Aprobar todas las áreas de cobertura
- Expandir antes de terminar Madrid
- Añadir expansión dentro del conteo base
- Aprobar todas las zonas a la vez
- No exigir página padre antes de una expansión
```

**Regla final**

```text
La expansión se calcula aparte de la base y solo con zonas aprobadas explícitamente.
```

**Validación operativa**

Si una zona de cobertura se aprueba para expansión, se calcula con un módulo separado. Esto mantiene la base limpia y permite escalar con control. Las Expansion Areas no deben mezclarse con la fórmula base.

**Cómo se obtiene**

- **Fuente:** Decisión de diseño ← heredado del Paso 1 §15 Approved Expansion Areas.
- **Método:** Si hay zonas aprobadas en Paso 1 §15, aplicar la fórmula expansión `E + S × E + A × E + G × S × E` (ver §6.14 Optional Expansion Formula). Por defecto `E = 0` en Phase 1. Cada zona aprobada se calcula aparte de la base, no mezclada.

**Output del paso**

- **Tipo:** Entero — total de páginas de expansión (puede ser 0).
- **Ejemplo (Cerrajeros Madrid 24h):** 0 páginas de expansión (Phase 1 sin Approved Expansion).

### Dependencias entre páginas
<small>§6.10</small>


**Explicación**

El cálculo debe reflejar dependencias. Un GeoArticle necesita una página comercial que apoyar.

**Patrón o fórmula**

```text
Página hija → página padre existente → enlace interno posible
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
El artículo /madrid/cuanto-cuesta-un-cerrajero-urgente/ se programa después de /cerrajero/madrid/cerrajero-urgente/ y /madrid/.
```

**Ejemplos incorrectos**

```text
- Publicar artículo sin landing
- Crear guía de Almagro sin expansión aprobada
- Crear artículos antes del GeoHub
- Contar artículos sin landings de destino
- Crear una página local sin Service Overview
- Publicar GeoHub sin enlazar a servicios
```

**Regla final**

```text
Cada página contada debe tener padre publicable y destino de enlace interno; ningún artículo va antes de su landing.
```

**Validación operativa**

El conteo no solo mide cantidad; también debe prever dependencias. Una GeoArticle no debería existir si no existe la página local que apoya. Una Location-Based Service Page necesita Service Overview y GeoHub.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Validar dependencias antes de cerrar el inventario. Jerarquía obligatoria: Homepage → Service Overview Pages → GeoHub Main City → Location-Based Service Pages → Additional Category Pages → GeoArticles. Cada página hija debe tener padre publicable y destino de enlace interno.

**Output del paso**

- **Tipo:** Mapa de dependencias resuelto — orden de publicación viable.
- **Ejemplo (Cerrajeros Madrid 24h):** `/madrid/cuanto-cuesta-un-cerrajero-urgente/` se programa después de `/cerrajero/madrid/cerrajero-urgente/` y `/madrid/`.

### Resultado total auditable
<small>§6.11</small>


**Explicación**

La fórmula calcula la cantidad potencial. No obliga a publicar todo a la vez.

**Patrón o fórmula**

```text
Tipo de página → fórmula → cantidad → total
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h muestra 1 Homepage, 5 Service Overview, 1 GeoHub, 5 Páginas de servicio en la Main City, 1 Additional Category Page y 15 GeoArticles.
```

**Ejemplos incorrectos**

```text
- Publicar 28 páginas SEO base (29 con /contacto/ como página auxiliar) sin QA
- No priorizar
- Confundir inventario con calendario
- Dar un total sin desglose
- No explicar por qué A = 1
- No separar base de expansión
```

**Regla final**

```text
El conteo final debe entregarse como tabla transparente y auditable componente a componente. Crea mapa, no calendario de publicación.
```

**Validación operativa**

La fórmula debe terminar con una tabla clara de cantidades por tipo de página. Si el número total no se puede explicar por componentes, no está listo para producción.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Entregar el resultado como tabla por tipo de página con fórmula y cantidad (ver §6.13 Tabla de inventario base). NO entregar como calendario de publicación — el orden y ritmo se decide en el Paso 10 (Producción en fases). El total debe ser explicable componente a componente.

**Output del paso**

- **Tipo:** Tabla auditable — desglose por tipo de página + total.
- **Ejemplo (Cerrajeros Madrid 24h):** 1 Homepage + 5 SO + 1 GeoHub + 5 LBS + 1 Additional + 15 GeoArticles = 28 páginas SEO base.

### Control anti-duplicación
<small>§6.12</small>


**Explicación**

Antes de cerrar el conteo, la fórmula debe detectar duplicados entre servicios core y categorías adicionales. Si no se hace, el total parece completo pero incluye páginas que compiten entre sí.

**Patrón o fórmula**

```text
Servicio + intención + ciudad → una sola URL
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Servicio de cerrajería de urgencia no suma una página adicional porque /cerrajero/madrid/cerrajero-urgente/ ya cubre esa intención.
```

**Ejemplos incorrectos**

```text
- Sumar cerrajero-urgente como página adicional
- Crear dos URLs para la misma intención comercial
- Contar duplicados como oportunidades nuevas
```

**Regla final**

```text
Una intención local debe tener una sola URL principal.
```

**Validación operativa**

La validación se aplica antes de cerrar el conteo. La IA recorre las Planned Additional Categories (intake §3, Paso 1 §10) y descarta las que coinciden en intención comercial con un core service. El número final de A debe ser explicable por exclusión, no por inflación.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Antes de cerrar el conteo, comparar cada Planned Additional Category con la lista de core services. Si una categoría adicional coincide en intención comercial con un core service, NO suma a A. La regla aplica también entre LBS y Additional Category Pages: una intención comercial = una URL principal.

**Output del paso**

- **Tipo:** Lista de duplicados detectados y consolidados.
- **Ejemplo (Cerrajeros Madrid 24h):** Servicio de cerrajería de urgencia → consolidado con core service Cerrajero urgente (no suma a A).

### Tabla de inventario base
<small>§6.13</small>


**Explicación**

Resultado tabular del cálculo. Es el output principal que el Paso 3 (URL Matrix) consume directamente para generar URLs concretas.

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

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar S, A, G a la fórmula base (§6.3) y desplegar en tabla. La tabla es el handoff al Paso 3.

**Output del paso**

- **Tipo:** Tabla de inventario por page type.
- **Ejemplo (Cerrajeros Madrid 24h):** Tabla anterior con totales 1 + 5 + 1 + 5 + 1 + 15 = 28.

### Optional Expansion Formula
<small>§6.14</small>


**Explicación**

Fórmula declarada para futura activación si una zona de cobertura pasa a Approved Expansion Area. No se ejecuta en Phase 1 si E=0.

**Patrón o fórmula**

```text
Solo si una Local Coverage Area pasa a Approved Expansion Area:

+ E Expansion GeoHubs
+ S × E Expansion Service Pages
+ A × E Expansion Additional Category Pages
+ G × S × E Expansion GeoArticles
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Declarar la fórmula en el documento aunque E=0 en Phase 1. Lista para activación futura sin re-deducir el sistema.

**Output del paso**

- **Tipo:** Fórmula declarada (paramétrica en E).
- **Ejemplo (Cerrajeros Madrid 24h):** E = 0 → 0 páginas de expansión. Fórmula lista para activar si E ≥ 1 en Phase 2.

### Ejemplo de expansión opcional
<small>§6.15</small>


**Explicación**

Ilustración del cálculo de expansión con valores hipotéticos para Almagro como Approved Expansion Area.

**Patrón o fórmula**

```text
Approved Expansion Area:
Almagro

E = 1
S = 5
A = 1
G = 3

Extra pages:
1 Almagro GeoHub
+ 5 Almagro service pages
+ 1 Almagro additional category page
+ 15 Almagro GeoArticles
= 22 páginas extra
```

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar §6.14 con valores E=1 y los mismos S, A, G del cluster base. El resultado se publica como módulo separado (no se suma al cluster base).

**Output del paso**

- **Tipo:** Cálculo paramétrico de expansión (ejemplo ilustrativo).
- **Ejemplo (Cerrajeros Madrid 24h):** No aplica en Phase 1 (E=0). Si Almagro se aprueba, se generan 22 páginas adicionales en módulo de expansión.

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

# Bloque III — Fuentes Internas GMB Crush usadas

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
