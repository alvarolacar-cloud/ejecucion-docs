Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo la estructura fija acordada en la conversación.
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# §1 Paso 2 — Fórmula Maestra de Arquitectura

# Bloque I — Introducción

## §2 Objetivo del Paso 2

Este paso existe para resolver un problema concreto dentro del sistema GMB Crush: calcular el tamaño real de la web antes de crear URLs, contenido o calendario de publicación.
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
Error que previene: crear páginas sin saber cuántas deberían existir.
Error que previene: meter Local Coverage Areas dentro de la fórmula base.
Error que previene: confundir Approved Expansion Areas con cobertura local mencionada en contenido.
Error que previene: duplicar categorías adicionales ya cubiertas por servicios core.
Error que previene: publicar GeoArticles antes de tener las páginas comerciales que apoyan.

## §3 Lo que la IA tiene que rellenar/obtener

```text
Business Name:

Planned Primary GBP Category:

Primary Category Slug:

Main City:

Main City Slug:

Servicios principales:
1.
2.
3.
4.
5.

Service Slugs:
1.
2.
3.
4.
5.

Planned Additional GBP Categories:
1.
2.
3.

Additional Categories already covered by Servicios principales:
1.
2.

Additional Categories that need separate pages:
1.
2.

Local Coverage Areas:
1.
2.
3.
4.
5.

Should Local Coverage Areas generate pages?
Default: No.

Approved Expansion Areas:
1.
2.
3.

Does every service apply to the Main City?
Yes / No

If no, specify exclusions:
- Service:
- Reason:
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

Servicios principales:
1. Cerrajero urgente
2. Apertura de puertas
3. Cambio de cerraduras
4. Cambio de bombines
5. Instalación de cerraduras de seguridad

Service Slugs:
1. cerrajero-urgente
2. apertura-puertas
3. cambio-cerraduras
4. cambio-bombines
5. instalacion-cerraduras-seguridad

Planned Additional GBP Categories:
1. Servicio de cerrajería de urgencia
2. Servicio de duplicado de llaves

Additional Categories already covered by Servicios principales:
1. Servicio de cerrajería de urgencia

Additional Categories that need separate pages:
1. Servicio de duplicado de llaves

Local Coverage Areas:
1. Almagro
2. Chamberí
3. Salamanca
4. Retiro

Should Local Coverage Areas generate pages?
No, not in the base build.

Approved Expansion Areas:
None in Phase 1.

Does every service apply to the Main City?
Yes
```

# Bloque II — Ejecución por la IA

> **Definición operativa — Local Coverage Areas:** zonas, barrios, distritos o landmarks seleccionados desde la dirección física, la Main City, la coherencia GEO, la proximidad, los datos de búsqueda, los competidores y la lógica GMB Crush para reforzar relevancia local dentro del contenido, schema y futuros análisis. No son automáticamente URLs. No son automáticamente páginas propias. No son necesariamente oficinas físicas. Las Local Coverage Areas se usan primero como señales GEO dentro del contenido. No generan URLs por defecto.

## §5 Planned GBP Categories Before GBP Creation

### §5.1 Explicación

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

### §5.2 Cómo obtenemos las Planned GBP Categories

**Fuente:** GMB Crush.

**Método:** Marcar todas las categorías GBP planificadas como `Planned` hasta que el Paso 14 cree y verifique el GBP. La arquitectura web se construye sobre la Planned Primary y solo soporta Planned Additional que necesitan página separada (cruce con §10 Variable A).

### §5.3 Output del paso

**Tipo:** Status declarado de categorías GBP — `Planned` hasta el Paso 14.

**Ejemplo (Cerrajeros Madrid 24h):** Planned Primary: Cerrajero. Planned Additional: Servicio de cerrajería de urgencia (cubierta por core service), Servicio de duplicado de llaves (necesita página propia).

## §6 Slug Generation

### §6.1 Explicación

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

### §6.2 Cómo obtenemos los Slugs

**Fuente:** GMB Crush ← heredados del Paso 1.

**Método:** Aplicar la transformación slugify a Primary Category (Paso 1 §9), Main City (Paso 1 §11) y a cada uno de los servicios principales (Paso 1 §13). Reutilizar los slugs en todas las URLs y schema del Paso 4 en adelante.

### §6.3 Output del paso

**Tipo:** Conjunto de slugs URL-safe (1 Primary + 1 Main City + S Services).

**Ejemplo (Cerrajeros Madrid 24h):** `cerrajero` / `madrid` / `cerrajero-urgente`, `apertura-puertas`, `cambio-cerraduras`, `cambio-bombines`, `instalacion-cerraduras-seguridad`.

## §7 Regla 1 — Fórmula base de una Main City

### §7.1 Explicación

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

### §7.2 Cómo obtenemos la Fórmula base

**Fuente:** GMB Crush.

**Método:** Aplicar la fórmula `1 + S + 1 + S + A + G × S` con los valores de S (§8), A (§10) y G (§11). El resultado da el total de páginas SEO base del cluster Main City. Una sola Main City multiplica — las Local Coverage Areas no entran en la fórmula (§12).

### §7.3 Output del paso

**Tipo:** Total de páginas SEO base del cluster Main City.

**Ejemplo (Cerrajeros Madrid 24h):** 1 + 5 + 1 + 5 + 1 + 15 = 28 páginas SEO base.

## §8 Regla 2 — Variable S

### §8.1 Explicación

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

### §8.2 Cómo obtenemos la Variable S

**Fuente:** GMB Crush ← heredado del Paso 1 §13 Servicios principales.

**Método:** Tomar el conteo de core services declarados en el Paso 1. Solo cuentan servicios reales con valor comercial. No inflar con sinónimos, modificadores ni subcasos.

### §8.3 Output del paso

**Tipo:** Entero — número de core services aprobados.

**Ejemplo (Cerrajeros Madrid 24h):** S = 5 (Cerrajero urgente, Apertura de puertas, Cambio de cerraduras, Cambio de bombines, Instalación de cerraduras de seguridad).

## §9 Service-to-Main-City Applicability

### §9.1 Explicación

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

La pregunta debe hacerse explícitamente al cliente. Si todos los servicios aplican (caso default), `S_efectiva = S` y la fórmula queda intacta. Si hay exclusiones, hay que recalcular `S_efectiva` y revisar el inventario LBS y GeoArticles del Bloque II. La exclusión solo aplica a la Main City; servicios excluidos pueden aplicar en Approved Expansion Areas (§13) si las hay.

### §9.2 Cómo obtenemos la Service-to-Main-City Applicability

**Fuente:** Input humano + GMB Crush.

**Método:** Preguntar al cliente «¿Todos los servicios aplican a la Main City?». Si Sí (default web-first): `S_efectiva = S` y la fórmula queda intacta. Si No: registrar las exclusiones con su razón, recalcular `S_efectiva` y propagar al inventario LBS y GeoArticles base.

### §9.3 Output del paso

**Tipo:** Boolean (Yes/No) + lista de exclusiones (si aplica).

**Ejemplo (Cerrajeros Madrid 24h):** Yes — todos los 5 servicios aplican a Madrid. S_efectiva = 5.

## §10 Regla 3 — Variable A

### §10.1 Explicación

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

### §10.2 Cómo obtenemos la Variable A

**Fuente:** GMB Crush ← heredado del Paso 1 §10 Planned Additional GBP Categories.

**Método:** Contar las Planned Additional Categories que NO están cubiertas por core services. Las cubiertas no suman a A (§16 Control anti-duplicación).

### §10.3 Output del paso

**Tipo:** Entero — categorías adicionales efectivas que requieren página propia.

**Ejemplo (Cerrajeros Madrid 24h):** A = 1 (Servicio de duplicado de llaves; Servicio de cerrajería de urgencia queda cubierta por core service).

## §11 Regla 4 — Variable G

### §11.1 Explicación

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

### §11.2 Cómo obtenemos la Variable G

**Fuente:** GMB Crush ← heredado del Paso 1 §16 GeoArticles per Service.

**Método:** Tomar el valor de G capturado en el Paso 1 (default 3). Aplicar `G × S_efectiva` para obtener el total de GeoArticles del cluster Main City. No multiplicar por Local Coverage Areas (§12).

### §11.3 Output del paso

**Tipo:** Entero — GeoArticles por servicio core.

**Ejemplo (Cerrajeros Madrid 24h):** G = 3 → G × S = 15 GeoArticles para Madrid.

## §12 Regla 5 — Local Coverage Areas no entran en la fórmula

### §12.1 Explicación

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

### §12.2 Cómo obtenemos las LCAs (exclusión de la fórmula)

**Fuente:** GMB Crush ← heredado del Paso 1 §14 Local Coverage Areas.

**Método:** Las LCAs (Direct + Candidate) heredadas del Paso 1 NO se usan como multiplicador de la fórmula. Se mencionan en contenido, FAQs, ejemplos locales y schema `areaServed`, pero no generan filas en el inventario base.

### §12.3 Output del paso

**Tipo:** LCAs declaradas como señales de contenido — 0 URLs adicionales en la base.

**Ejemplo (Cerrajeros Madrid 24h):** Almagro, Chamberí, Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad → 0 páginas adicionales en el cluster base.

## §13 Regla 6 — Approved Expansion Areas opcional

### §13.1 Explicación

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

### §13.2 Cómo obtenemos las Approved Expansion Areas

**Fuente:** Decisión de diseño ← heredado del Paso 1 §15 Approved Expansion Areas.

**Método:** Si hay zonas aprobadas en Paso 1 §15, aplicar la fórmula expansión `E + S × E + A × E + G × S × E` (ver §18 Optional Expansion Formula). Por defecto `E = 0` en Phase 1. Cada zona aprobada se calcula aparte de la base, no mezclada.

### §13.3 Output del paso

**Tipo:** Entero — total de páginas de expansión (puede ser 0).

**Ejemplo (Cerrajeros Madrid 24h):** 0 páginas de expansión (Phase 1 sin Approved Expansion).

## §14 Regla 7 — Páginas comerciales antes que artículos (dependencias)

### §14.1 Explicación

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

### §14.2 Cómo obtenemos las dependencias entre páginas

**Fuente:** GMB Crush.

**Método:** Validar dependencias antes de cerrar el inventario. Jerarquía obligatoria: Homepage → Service Overview Pages → GeoHub Main City → Location-Based Service Pages → Additional Category Pages → GeoArticles. Cada página hija debe tener padre publicable y destino de enlace interno.

### §14.3 Output del paso

**Tipo:** Mapa de dependencias resuelto — orden de publicación viable.

**Ejemplo (Cerrajeros Madrid 24h):** `/madrid/cuanto-cuesta-un-cerrajero-urgente/` se programa después de `/cerrajero/madrid/cerrajero-urgente/` y `/madrid/`.

## §15 Regla 8 — Resultado total como inventario auditable

### §15.1 Explicación

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

### §15.2 Cómo obtenemos el Resultado final

**Fuente:** GMB Crush.

**Método:** Entregar el resultado como tabla por tipo de página con fórmula y cantidad (ver §17 Tabla de inventario base). NO entregar como calendario de publicación — el orden y ritmo se decide en el Paso 10 (Producción en fases). El total debe ser explicable componente a componente.

### §15.3 Output del paso

**Tipo:** Tabla auditable — desglose por tipo de página + total.

**Ejemplo (Cerrajeros Madrid 24h):** 1 Homepage + 5 SO + 1 GeoHub + 5 LBS + 1 Additional + 15 GeoArticles = 28 páginas SEO base.

## §16 Regla 9 — Control anti-duplicación

### §16.1 Explicación

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

### §16.2 Cómo obtenemos el Control anti-duplicación

**Fuente:** GMB Crush.

**Método:** Antes de cerrar el conteo, comparar cada Planned Additional Category con la lista de core services. Si una categoría adicional coincide en intención comercial con un core service, NO suma a A. La regla aplica también entre LBS y Additional Category Pages: una intención comercial = una URL principal.

### §16.3 Output del paso

**Tipo:** Lista de duplicados detectados y consolidados.

**Ejemplo (Cerrajeros Madrid 24h):** Servicio de cerrajería de urgencia → consolidado con core service Cerrajero urgente (no suma a A).

## §17 Tabla de inventario base

| Tipo de página | Fórmula | Ejemplo Cerrajeros Madrid 24h |
|---|---:|---:|
| Homepage | 1 | 1 |
| Service Overview Pages | S | 5 |
| Main City GeoHub | 1 | 1 |
| Main City Location-Based Service Pages | S | 5 |
| Páginas de categoría adicional en la Main City | A | 1 |
| GeoArticles de la Main City | G × S | 15 |
| **Total base** | — | **28** |

## §18 Optional Expansion Formula

```text
Solo si una Local Coverage Area pasa a Approved Expansion Area:

+ E Expansion GeoHubs
+ S × E Expansion Service Pages
+ A × E Expansion Additional Category Pages
+ G × S × E Expansion GeoArticles
```

## §19 Ejemplo de expansión opcional

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

# Bloque III — Checklist Final

## §20 Checklist final del Paso 2

| Check | Pregunta | Estado |
|---|---|---|
| Fórmula base | ¿La fórmula usa una sola Main City? | ✅ / ⬜ |
| Servicios | ¿S cuenta solo core services reales? | ✅ / ⬜ |
| Categorías adicionales | ¿A excluye categorías ya cubiertas? | ✅ / ⬜ |
| GeoArticles | ¿G se calcula por servicio dentro de la Main City? | ✅ / ⬜ |
| Local Coverage Areas | ¿No están generando URLs por defecto? | ✅ / ⬜ |
| Approved Expansion | ¿La expansión está separada de la base? | ✅ / ⬜ |
| Dependencias | ¿Los artículos dependen de páginas comerciales? | ✅ / ⬜ |
| Total base | ¿El total de páginas está claro? | ✅ / ⬜ |
| No duplicación | ¿Se evitaron duplicados de intención? | ✅ / ⬜ |

# Bloque IV — Outputs

## §21 Outputs del Paso 2

- Fórmula base calculada
- Variables S, A y G definidas
- Total de páginas base
- Categorías duplicadas detectadas
- Local Coverage Areas excluidas del conteo de URLs
- Optional Expansion Formula preparada
- Inventario base de páginas
- Dependencias iniciales claras

---

# Bloque V — Fuentes Internas GMB Crush Usadas

# §22 Fuentes internas GMB Crush usadas

- Analysis Framework.pdf
- GMB CRUSH Universal AI Local SEO Framework Template
- Website Homepage AI Optimization Prompts/Framework
- Service Pages AI Optimization Prompts/Framework
- Location Pages AI Optimization Prompts/Framework
- GeoHub Pages AI Framework
- GeoArticle Pages AI Framework
- Additional Categories Pages AI Framework

### §22.1 GeoArticles completos (15)

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
