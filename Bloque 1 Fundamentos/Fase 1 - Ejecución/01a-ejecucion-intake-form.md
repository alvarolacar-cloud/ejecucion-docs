Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo la estructura fija acordada en la conversación.
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# §1 Paso 1 — Intake Form

# Bloque I — Introducción

## §2 Objetivo del Paso 1

Este paso existe para resolver un problema concreto dentro del sistema GMB Crush: recoger los datos mínimos del negocio antes de generar arquitectura, URLs o contenido.
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
Error que previene: empezar a crear páginas sin conocer la categoría principal del GBP.
Error que previene: confundir ciudad principal con áreas de cobertura local.
Error que previene: crear páginas para zonas donde el negocio no atiende clientes.
Error que previene: usar un NAP diferente al del GBP.
Error que previene: crear servicios sin saber si son core services o categorías adicionales.

## §3 Lo que la IA tiene que rellenar/obtener

```text
Business Name:

Website URL:

Canonical Domain:
Option A: https://www.domain.com
Option B: https://domain.com

GBP Status:
Not Created / Created / Verified / Pending Verification

GBP Creation Timing:
After website launch

GBP Verification Status:
Not Started / Pending / Verified

GBP URL:
Leave blank until the GBP is created in Paso 14.

Full NAP:
- Name:
- Street Address:
- City:
- State / Province:
- ZIP / Postal Code:
- Country:
- Phone:
- Email:

Planned Primary GBP Category:

Planned Additional GBP Categories:
1.
2.
3.

Main City:
The primary city that will generate the base architecture.

Physical Location City:
The city where the business is physically located, if applicable.

Servicios principales:
1.
2.
3.
4.
5.

Direct Local Coverage Areas:
Zonas que salen directamente de la dirección física.

> **Nota para la IA:** Antes de decidir las Local Coverage Areas, consultar el módulo **Interpretación GMB Crush de la dirección física y zonas GEO** al final de este documento. Ese módulo explica cómo se interpreta la dirección física, cómo se eligen las zonas y qué criterios deben cumplir.
1.
2.

Candidate Local Coverage Areas:
Zonas que no salen de la dirección pero pueden tener sentido por proximidad, búsqueda o competencia. Solo se usan como señales GEO activas si pasan el test de coherencia GEO.
1.
2.
3.
4.
5.
6.
7.
8.

Should Local Coverage Areas generate pages?
Default: No.

Approved Expansion Areas:
Optional. Only list areas that deserve their own URLs.
1.
2.
3.

Additional Categories already covered by core services:
1.
2.

Additional Categories that need separate pages:
1.
2.

GeoArticles per Service:
Default: 3

Preferred CTA:
Option A: Llamar ahora
Option B: Reservar online
Option C: Solicitar presupuesto
Option D: Contactar

Trust Signals:
- Years in business:
- Reviews:
- Certifications:
- Awards:
- Guarantees:
- Urgencias / servicio en el mismo día / servicio móvil:

```

## §4 Ejemplo rellenado

```text
Business Name:
Cerrajeros Madrid 24h

Website URL:
https://www.cerrajerosmadrid24h.com

Canonical Domain:
https://www.cerrajerosmadrid24h.com

GBP Status:
Not Created

GBP Creation Timing:
After website launch

GBP Verification Status:
Not Started

GBP URL:
N/A — GBP not created yet

Full NAP:
- Name: Cerrajeros Madrid 24h
- Street Address: Calle Rafael Calvo 12, Barrio Almagro, Distrito Chamberí
- City: Madrid
- State / Province: Comunidad de Madrid
- ZIP / Postal Code: 28010
- Country: España
- Phone: +34 600 000 000
- Email: info@cerrajerosmadrid24h.com

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

Las Candidate Local Coverage Areas solo se usan como señales GEO activas si pasan el test de coherencia GEO.

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
- Reseñas iniciales pendientes de recopilar tras crear y verificar el GBP
- Técnicos cerrajeros cualificados
- Servicio móvil en el mismo día
- Garantía de trabajo

```

# Bloque II — Ejecución por la IA

## §5 Business Name

### §5.1 Explicación

**Explicación**

El nombre del negocio es la entidad base. Debe coincidir con el nombre del GBP cuando se use como NAP, schema o bloque de confianza.

**Patrón o fórmula**

```text
Business Name = nombre oficial de la entidad local
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h
```

**Ejemplos incorrectos**

```text
- Cerrajeros Madrid 24h Madrid
- Cerrajeros Madrid 24h 24/7 Best Cheap
- Cerrajeros Madrid 24h Almagro si ese no es el nombre real
```

**Regla final**

```text
El nombre del negocio debe ser estable, rastreable y consistente.
```

### §5.2 Cómo obtenemos el Business Name

**Fuente:** Input humano.

**Método:** Tomar el nombre legal de la entidad declarado por el cliente en el intake. Validar que coincide con el nombre que se usará en el GBP cuando se cree (Paso 14).

### §5.3 Output del paso

**Tipo:** String — nombre legal de la entidad local.

**Ejemplo (Cerrajeros Madrid 24h):** Cerrajeros Madrid 24h

## §6 Website URL

### §6.1 Explicación

**Explicación**

La URL raíz define el dominio canónico sobre el que se generarán todas las páginas. No se deben mezclar variantes con www y sin www.

**Patrón o fórmula**

```text
Canonical Domain = una sola versión del dominio
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
https://www.cerrajerosmadrid24h.com
```

**Ejemplos incorrectos**

```text
- http://cerrajerosmadrid24h.com
- https://cerrajerosmadrid24h.com y https://www.cerrajerosmadrid24h.com mezclados
- /home como página raíz
```

**Regla final**

```text
Una web local debe operar con un solo dominio canónico.
```

### §6.2 Cómo obtenemos el Website URL

**Fuente:** Input humano.

**Método:** Tomar el dominio canónico declarado por el cliente. Una sola versión (con o sin www, siempre con https). El resto de variantes deben redirigir 301 a la canónica.

### §6.3 Output del paso

**Tipo:** URL canónica con protocolo y, si aplica, subdominio www.

**Ejemplo (Cerrajeros Madrid 24h):** https://www.cerrajerosmadrid24h.com

## §7 GBP Lifecycle Status

### §7.1 Explicación

**Explicación**

En esta versión web-first, el Google Business Profile típicamente no existe cuando se ejecuta el Paso 1. La web se publica primero (Pasos 15-18) y el GBP se crea/verifica en el Paso 14. Estos 4 campos capturan el ciclo de vida del GBP en el momento del intake. Si el cliente ya tiene un GBP creado, se declara el estado real.

**Patrón o fórmula**

```text
GBP Status              ∈ {Not Created, Created, Verified, Pending Verification}
GBP Creation Timing     = After website launch (default web-first)
GBP Verification Status ∈ {Not Started, Pending, Verified}
GBP URL                 = blank hasta Paso 14, o URL real si ya existe
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
GBP Status: Not Created
GBP Creation Timing: After website launch
GBP Verification Status: Not Started
GBP URL: N/A — GBP not created yet
```

**Ejemplos incorrectos**

```text
- Marcar GBP Status = Verified sin haberlo creado
- Inventar una GBP URL antes del Paso 14
- Incluir sameAs del GBP en schema cuando no existe
- Afirmar reseñas de Google si el perfil aún no está creado
```

**Regla final**

```text
Hasta que el Paso 14 cree y verifique el GBP, los 4 campos toman valores web-first y la web no afirma señales del GBP (URL, sameAs, reseñas).
```

**Validación operativa**

La doctrina GMB Crush separa estrictamente la fase web-first (Pasos 1-13 + 15-18) de la fase GBP (Paso 14). Cualquier referencia al GBP en schema, contenido o trust signals antes del Paso 14 es invento. Si el cliente declara un GBP ya creado, el operador decide si adelantar el Paso 14 fuera del orden estándar o congelar el GBP existente y sincronizarlo en el momento normal.

### §7.2 Cómo obtenemos el GBP Lifecycle Status

**Fuente:** Input humano + GMB Crush.

**Método:** Preguntar al cliente si ya tiene GBP creado o verificado. Si NO (default web-first): los 4 campos toman los valores fijos del ejemplo. Si SÍ: capturar el estado real y considerar adelantar el Paso 14 fuera del orden estándar.

### §7.3 Output del paso

**Tipo:** 4 valores discretos del ciclo de vida del GBP.

**Ejemplo (Cerrajeros Madrid 24h):** Status: Not Created · Creation Timing: After website launch · Verification: Not Started · URL: N/A (pending Paso 14).

## §8 Full NAP

### §8.1 Explicación

**Explicación**

El NAP es una señal de entidad local. Debe ser igual en homepage, contacto, footer, schema y GBP cuando proceda.

**Patrón o fórmula**

```text
Name + Address + Phone = NAP oficial
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h, Calle Rafael Calvo 12, Barrio Almagro, Distrito Chamberí, Madrid, +34 600 000 000
```

**Ejemplos incorrectos**

```text
- Cambiar el teléfono entre páginas
- Usar direcciones distintas sin explicación
- Ocultar el NAP en imágenes no rastreables
```

**Regla final**

```text
El NAP debe ser visible, consistente y rastreable.
```

**Validación operativa**

El NAP debe quedar definido una sola vez en el intake y reutilizarse sin variaciones en homepage, footer, contact page y schema LocalBusiness. Si cambia entre páginas o entre la web y el GBP que se cree en el Paso 14, la entidad local arranca con una señal débil y se pierde rastreabilidad. El intake convierte el NAP en un dato canónico que después se reutiliza en schema, bloques de confianza y CTAs con teléfono.

### §8.2 Cómo obtenemos el Full NAP

**Fuente:** Input humano.

**Método:** Recoger los 8 campos del NAP completos (Name, Street Address, City, State/Province, ZIP/Postal Code, Country, Phone, Email) y dejarlos como dato canónico reutilizable en homepage, footer, contact page y schema.

### §8.3 Output del paso

**Tipo:** Bloque NAP completo (8 campos) en formato canónico único.

**Ejemplo (Cerrajeros Madrid 24h):** Cerrajeros Madrid 24h, Calle Rafael Calvo 12, Barrio Almagro, Distrito Chamberí, 28010 Madrid, España, +34 600 000 000, info@cerrajerosmadrid24h.com

## §9 Planned Primary GBP Category

### §9.1 Explicación

**Explicación**

La categoría principal del GBP manda sobre la arquitectura. Los servicios y páginas deben apoyar esa categoría.

**Patrón o fórmula**

```text
Planned Primary GBP Category → Primary Category Slug → Service Pages
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajero → cerrajero
```

**Ejemplos incorrectos**

```text
- Usar una categoría que no existe en el GBP
- Construir la web alrededor de un servicio secundario
- No crear páginas que soporten la categoría principal
```

**Regla final**

```text
La categoría principal debe verse reflejada en homepage, servicios y páginas locales.
```

**Validación operativa**

La categoría principal del GBP define el eje semántico del sistema y debe tener soporte directo en homepage y servicios core. Si el GBP intenta posicionar `Cerrajero` pero la web habla mayoritariamente de servicios secundarios, la entidad local proyecta dos intenciones distintas y diluye autoridad. Antes de avanzar al Paso 2, validar que los servicios core (§13) realmente apoyan la Primary Category.

### §9.2 Cómo obtenemos la Planned Primary GBP Category

**Fuente:** GMB Crush + Competidores.

**Método:**

1. Buscar en Google Maps `[servicio principal] [main city]` sin login.
2. Anotar la categoría primaria declarada por los 5 negocios mejor posicionados en el Local Pack.
3. Seleccionar la categoría que más se repite (>3 de 5) como Primary Category Planned. Si hay empate, priorizar la más amplia (categoría madre del catálogo GBP).
4. Validar contra el catálogo oficial de GBP. Si la categoría no existe exactamente, escoger la más próxima del catálogo.

### §9.3 Output del paso

**Tipo:** Categoría GBP oficial (Primary).

**Ejemplo (Cerrajeros Madrid 24h):** Cerrajero

## §10 Planned Additional GBP Categories

### §10.1 Explicación

**Explicación**

Las categorías adicionales refuerzan la profundidad de entidad, pero no siempre generan páginas nuevas si ya están cubiertas por un core service.

**Patrón o fórmula**

```text
Additional Category → covered or separate page
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Servicio de cerrajería de urgencia cubierta por Cerrajero urgente; Servicio de duplicado de llaves necesita página propia
```

**Ejemplos incorrectos**

```text
- Crear cerrajero-urgente y cerrajero-urgente como páginas separadas
- Ignorar Servicio de duplicado de llaves
- Crear categorías sin relación con el GBP
```

**Regla final**

```text
Cada categoría adicional se consolida o se convierte en página, pero nunca se duplica.
```

**Validación operativa**

Cada categoría adicional debe clasificarse antes de entrar en la arquitectura. Primero se revisa si ya está cubierta por un servicio core (entonces no genera URL — queda consolidada); si no, se marca como categoría efectiva que necesita página propia. Esta clasificación evita duplicar intenciones, crear páginas casi idénticas y canibalizar la Service Overview Page del core service.

### §10.2 Cómo obtenemos las Planned Additional GBP Categories

**Fuente:** GMB Crush + Competidores.

**Método:**

1. Tras escoger la Primary Category (§9), revisar las categorías adicionales declaradas por los mismos 5 competidores top.
2. Listar todas las categorías secundarias que aparecen en al menos 2 de los 5 competidores.
3. Filtrar las que el cliente realmente ofrece (cruce con servicios reales). Las que no ofrece se descartan.
4. Aplicar la regla de consolidación: si una categoría adicional coincide con un core service, se marca como cubierta. Si no, se marca como “necesita página propia”.

### §10.3 Output del paso

**Tipo:** Lista de categorías clasificadas (cubiertas vs necesitan página propia).

**Ejemplo (Cerrajeros Madrid 24h):** Servicio de cerrajería de urgencia → cubierta por Cerrajero urgente. Servicio de duplicado de llaves → necesita página propia.

## §11 Main City

### §11.1 Explicación

**Explicación**

La Main City es la ciudad que genera la arquitectura base. Es la unidad local principal del sistema simplificado.

**Patrón o fórmula**

```text
Main City = /city/ + /category/city/service/
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Madrid
```

**Ejemplos incorrectos**

```text
- Almagro como Main City si el GBP y el NAP están en Madrid
- Meter cinco ciudades como base
- Cambiar la Main City según la página
```

**Regla final**

```text
La base se construye sobre una sola Main City.
```

**Validación operativa**

La Main City genera URLs base; las Local Coverage Areas (§14) refuerzan contenido y schema sin generar URLs por defecto; las Approved Expansion Areas (§15) son URLs opcionales que requieren aprobación explícita. Estas tres capas deben mantenerse separadas en el intake — mezclarlas vuelve al sistema viejo de target cities y secondary cities con páginas innecesarias.

### §11.2 Cómo obtenemos la Main City

**Fuente:** GMB Crush.

**Método:** Extraer la ciudad directamente del campo City del NAP (§8). Una sola Main City genera la arquitectura base. No se multiplica por barrios ni por zonas de cobertura.

### §11.3 Output del paso

**Tipo:** Ciudad única — la del NAP.

**Ejemplo (Cerrajeros Madrid 24h):** Madrid

## §12 Physical Location City

### §12.1 Explicación

**Explicación**

La ciudad de ubicación física evita falsas señales. Si no hay oficina en un área, no se debe decir que la hay.

**Patrón o fórmula**

```text
Physical Location City = ciudad de presencia real
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Madrid
```

**Ejemplos incorrectos**

```text
- Nuestra oficina en Almagro si no existe
- Visit our Chamberí storefront si no existe
- Schema con address falsa
```

**Regla final**

```text
Nunca se inventa ubicación física.
```

**Validación operativa**

El intake debe indicar la ciudad de presencia física real y si existe atención presencial. Esto controla qué páginas pueden usar LocalBusiness con dirección, mapa o lenguaje de oficina. Nunca afirmar oficinas en áreas de cobertura donde el negocio solo presta servicio móvil — si no hay oficina en Almagro, las páginas de Madrid no deben decir «our Almagro storefront».

### §12.2 Cómo obtenemos la Physical Location City

**Fuente:** Input humano.

**Método:** Tomar la ciudad de presencia física real declarada por el cliente (oficina, almacén o punto de atención). Si el negocio es móvil sin oficina, declarar “móvil” o coincidir con la Main City sin afirmar oficina física.

### §12.3 Output del paso

**Tipo:** Ciudad de presencia física real (puede ser “móvil”).

**Ejemplo (Cerrajeros Madrid 24h):** Madrid

## §13 Servicios principales

### §13.1 Explicación

**Explicación**

Los core services son los servicios principales que generan Service Overview Pages y Páginas de servicio en la Main City.

**Patrón o fórmula**

```text
S = número de core services
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajero urgente, Apertura de puertas, Cambio de cerraduras, Cambio de bombines, Instalación de cerraduras de seguridad
```

**Ejemplos incorrectos**

```text
- Meter servicios irrelevantes
- Crear servicios que no se ofrecen
- Agrupar todos los servicios en una única página
```

**Regla final**

```text
Cada core service importante debe tener página propia.
```

**Validación operativa**

Los core services son los que generan Service Overview Pages y Location-Based Service Pages en la Main City. Deben tener nombres claros, slugs limpios y valor comercial real. Solo entran servicios reales — no microvariantes, no sinónimos, no servicios que el negocio no ofrece. La fórmula del Paso 2 depende de S = número de servicios core; inflar S aquí infla todo el inventario de páginas aguas abajo.

### §13.2 Cómo obtenemos los Servicios principales

**Fuente:** GMB Crush + Competidores.

**Método:**

1. Buscar en Google Maps `[categoría principal] [main city]` y abrir los 5 perfiles GBP mejor posicionados del Local Pack.
2. En cada perfil, abrir la sección «Servicios» del GBP y listar los servicios declarados.
3. Contar la frecuencia de cada servicio entre los 5 competidores. Seleccionar los 5 servicios más frecuentes (top 5 por frecuencia).
4. Cruzar con la oferta real del cliente. Si el cliente no ofrece uno de los servicios top, sustituirlo por el siguiente más frecuente que sí ofrezca.
5. Si hay empate de frecuencia, priorizar el servicio con más volumen de búsqueda local (cruce con keyword research).

### §13.3 Output del paso

**Tipo:** 5 core services (S=5) priorizados.

**Ejemplo (Cerrajeros Madrid 24h):** Cerrajero urgente, Apertura de puertas, Cambio de cerraduras, Cambio de bombines, Instalación de cerraduras de seguridad.

## §14 Local Coverage Areas

### §14.1 Explicación

**Explicación**

Son zonas seleccionadas por proximidad al NAP, coherencia GEO y lógica GMB Crush. Incluyen barrios, distritos, municipios cercanos o áreas de servicio. Se clasifican en Direct (salen del ancla física) y Candidate (requieren validación GEO). No generan URLs por defecto.

**Patrón o fórmula**

```text
Local Coverage Areas = contenido + FAQs + schema areaServed
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Almagro, Chamberí, Salamanca, Retiro
```

**Ejemplos incorrectos**

```text
- Crear /almagro/ por defecto
- Usar áreas donde no se atiende
- Listar 40 zonas sin naturalidad
```

**Regla final**

```text
Las áreas de cobertura refuerzan el contenido; no crean páginas automáticamente.
```

### §14.2 Cómo obtenemos las Local Coverage Areas

**Fuente:** GMB Crush + Competidores.

**Método (Direct LCAs):**

1. Las Direct LCAs salen del propio ancla físico del NAP (§8): barrio y distrito de la dirección. Se registran de forma directa sin más validación.

**Método (Candidate LCAs):**

1. Revisar las áreas de servicio declaradas por los 3-5 competidores top en Google Maps.
2. Listar todas las zonas (barrios, distritos, municipios) que aparecen en al menos 2 competidores y NO están ya en Direct.
3. Para cada zona candidata, aplicar el test de coherencia GEO 3/6 (§24). Si pasa 3 de 6 criterios, queda como Candidate validable. Si no, se descarta.
4. Las Candidate aprobadas entran como contenido en LBS, GeoHub y GeoArticles. Solo generan URL si pasan a Approved Expansion (§15).

### §14.3 Output del paso

**Tipo:** Dos listas — Direct (del NAP) y Candidate (de competidores).

**Ejemplo (Cerrajeros Madrid 24h):** Direct: Almagro, Chamberí. Candidate: Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad.

## §15 Approved Expansion Areas

### §15.1 Explicación

**Explicación**

Son áreas que sí pueden generar URLs propias, pero solo si se aprueban por demanda, competencia o valor comercial.

**Patrón o fórmula**

```text
Approved Expansion Area → optional URLs
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
None in Phase 1
```

**Ejemplos incorrectos**

```text
- Aprobar todas las áreas de cobertura
- Crear una capa de expansión sin contenido único
- Confundir cobertura con arquitectura
```

**Regla final**

```text
Solo las áreas aprobadas generan URLs propias.
```

**Validación operativa**

El sistema base no crea páginas para todas las zonas de cobertura. Solo una Local Coverage Area pasa a Approved Expansion Area si hay demanda, oportunidad, valor comercial y capacidad de escribir contenido único. En el intake base este campo puede estar vacío sin que el sistema quede incompleto — la expansión territorial se aprueba; no se asume.

### §15.2 Cómo obtenemos las Approved Expansion Areas

**Fuente:** Decisión de diseño.

**Método:** Vacío por defecto en Phase 1. Una zona pasa de Candidate LCA (§14) a Approved Expansion solo si cumple los criterios de §27: demanda de búsqueda + competidores trabajándola + contenido único posible + valor comercial + sin fingir oficina física. Cada aprobación es una decisión consciente, no un default.

### §15.3 Output del paso

**Tipo:** Lista de zonas aprobadas (puede estar vacía en Phase 1).

**Ejemplo (Cerrajeros Madrid 24h):** None in Phase 1.

## §16 GeoArticles per Service

### §16.1 Explicación

**Explicación**

G es una variable de la Fórmula Maestra del Paso 2 (`Total = 1 + S + 1 + S + A + G × S`). Define cuántos artículos de blog/GeoArticles se generan por cada servicio core dentro de la Main City. El intake del Paso 1 captura el valor (default 3) para que el Paso 2 lo aplique directamente.

**Patrón o fórmula**

```text
GeoArticles per Service = G ∈ {2, 3, 4, 5}
Default: G = 3
Total GeoArticles del cluster = G × S
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
GeoArticles per Service: 3
G × S = 3 × 5 = 15 GeoArticles para Madrid
```

**Ejemplos incorrectos**

```text
- Usar G = 10 sin capacidad de producción real
- Multiplicar G por cada Local Coverage Area
- G = 0 dejando los core services sin boosters semánticos
```

**Regla final**

```text
G es el default doctrinal (3); ajustable solo si el cliente justifica otra capacidad de producción y refresh.
```

**Validación operativa**

G se decide en Paso 1 y la Fórmula Maestra del Paso 2 lo aplica como multiplicador. Cambiar G aquí cambia el inventario completo del cluster aguas abajo. Si el cliente no tiene capacidad para producir 15 artículos, hay que negociar G más bajo en el intake en lugar de aceptarlo y luego no publicarlos.

### §16.2 Cómo obtenemos los GeoArticles per Service

**Fuente:** Decisión de diseño + GMB Crush.

**Método:** Default `G = 3` según doctrina GMB Crush. Ajustable según capacidad de producción real del cliente y plan de refresh.

### §16.3 Output del paso

**Tipo:** Entero — GeoArticles por servicio core.

**Ejemplo (Cerrajeros Madrid 24h):** G = 3 → 15 GeoArticles totales.

## §17 Preferred CTA

### §17.1 Explicación

**Explicación**

El CTA debe ser coherente con el tipo de negocio y el servicio.

**Patrón o fórmula**

```text
CTA = llamada, reserva, presupuesto o contacto
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Llamar ahora
```

**Ejemplos incorrectos**

```text
- Usar un CTA distinto en cada página sin criterio
- No tener CTA
- CTA genérico sin ciudad ni servicio
```

**Regla final**

```text
Cada página debe tener un CTA claro.
```

### §17.2 Cómo obtenemos el Preferred CTA

**Fuente:** Decisión de diseño.

**Método:** Elegir uno de los 4 CTAs estándar — Llamar ahora / Reservar online / Solicitar presupuesto / Contactar — según el tipo de negocio, urgencia del servicio y comportamiento esperado del usuario. El CTA debe ser consistente en homepage, service pages y LBS.

### §17.3 Output del paso

**Tipo:** Una sola opción de CTA reutilizable en toda la web.

**Ejemplo (Cerrajeros Madrid 24h):** Llamar ahora.

## §18 Trust Signals

### §18.1 Explicación

**Explicación**

Las señales de confianza ayudan al usuario, a Google y a sistemas de IA a validar autoridad.

**Patrón o fórmula**

```text
Reviews + years + certifications + guarantees
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
10+ años de experiencia, reseñas iniciales pendientes tras crear el GBP, técnicos cerrajeros cualificados, servicio móvil en el mismo día, garantía de trabajo
```

**Ejemplos incorrectos**

```text
- Afirmaciones sin base
- Reviews inventadas
- Badges falsos
```

**Regla final**

```text
Los trust signals deben ser reales y reutilizables.
```

**Validación operativa**

Las señales de confianza recogidas en el intake se reutilizan en homepage, páginas de servicio, GeoHub, CTAs y QA. Años de experiencia, reseñas, certificaciones, garantías y servicio móvil sostienen autoridad sin inventar contenido. Toda señal debe ser real, reutilizable y verificable — no inventar certificaciones, no usar reseñas sin fuente, no usar badges falsos.

### §18.2 Cómo obtenemos los Trust Signals

**Fuente:** GMB Crush + Competidores.

**Método:**

1. Revisar las homepages y LBS de los 5 competidores top del Local Pack.
2. Listar los trust signals que aparecen en al menos 3 de los 5 competidores (el «estándar» del sector).
3. Listar los trust signals que aparecen en 1 o 2 competidores (los «diferenciadores» que pocos usan).
4. Confirmar con el cliente cuáles puede acreditar como reales (años, certificaciones, garantías, equipo cualificado). Filtrar los que no puede demostrar.
5. Resultado: 3-5 trust signals que sean del estándar del sector + 1-2 diferenciadores acreditables.

### §18.3 Output del paso

**Tipo:** Lista de 4-7 trust signals reales y reutilizables.

**Ejemplo (Cerrajeros Madrid 24h):** 10+ años de experiencia, técnicos cerrajeros cualificados, servicio móvil en el mismo día, garantía de trabajo, reseñas iniciales pendientes de recopilar tras crear el GBP.

# Bloque III — Módulo doctrinal: Interpretación de la dirección física y zonas GEO

# §19 Módulo — Interpretación GMB Crush de la dirección física y zonas GEO

> **Definición operativa — Local Coverage Areas:** zonas, barrios, distritos o landmarks seleccionados desde la dirección física, la Main City, la coherencia GEO, la proximidad, los datos de búsqueda, los competidores y la lógica GMB Crush para reforzar relevancia local dentro del contenido, schema y futuros análisis. No son automáticamente URLs. No son automáticamente páginas propias. No son necesariamente oficinas físicas. Las Local Coverage Areas se usan primero como señales GEO dentro del contenido. No generan URLs por defecto.

Este módulo se añade dentro del **Paso 1 — Intake Form**, justo después de recoger el **Physical Address / NAP** y antes de definir:

```text
Main City
Local Coverage Areas
Approved Expansion Areas
```

La función de este bloque es dejar claro cómo se interpreta una dirección física concreta dentro de la lógica GMB Crush.

---

## §20 Interpretación GMB Crush de la dirección física

A partir de una dirección concreta como:

```text
Rafael Calvo 40, Madrid
```

GMB Crush nos dice que hagamos esto:

| Orden | Qué hacer | Resultado |
|---:|---|---|
| 1 | Usar la dirección como **Physical Address / NAP** | Nombre, dirección, ciudad, teléfono y país quedan como datos base del negocio. El Analysis Framework pide Physical Address y Service Areas como input inicial. |
| 2 | Extraer la **Main City** desde la dirección | Main City = **Madrid**. |
| 3 | Construir la arquitectura sobre la ciudad, no sobre la calle | La unidad base no es "Rafael Calvo", sino **Madrid**. |
| 4 | Crear la homepage como entidad raíz | `/` con H1 tipo `[Brand] + [Primary Service] + Madrid`, NAP visible, servicios core y enlaces internos. |
| 5 | Crear páginas de servicio sin ciudad | `/cerrajero/apertura-puertas/`, `/cerrajero/cerrajero-urgente/`, etc. Estas páginas son pilares temáticos, no páginas locales. |
| 6 | Crear páginas servicio + ciudad | `/cerrajero/madrid/apertura-puertas/`, `/cerrajero/madrid/cerrajero-urgente/`, etc. GMB Crush define este patrón como `/category/city/service/`. |
| 7 | Crear GeoHub de ciudad | `/madrid/`, como contenedor de todos los servicios, categorías y artículos de Madrid. |
| 8 | Usar barrios, zonas cercanas o landmarks solo como señales GEO dentro del contenido | Se pueden mencionar barrios, zonas o landmarks en intro, H2s, FAQs, GeoHub y GeoArticles, pero no generan páginas por defecto. El framework permite "neighborhood coverage" en GeoHub y referencias locales en GeoArticles. |
| 9 | No fingir ubicación física en otras zonas | Puedes decir que el contenido referencia zonas locales, pero no "tenemos oficina en X" si no es verdad. Los GeoArticles indican expresamente no fingir ubicación física. |
| 10 | Usar `areaServed` en schema | En páginas locales, el schema `LocalBusiness` debe incluir `areaServed`, URL, teléfono, email y `sameAs` si existe. |

### §20.1 En una frase

GMB Crush no dice:

```text
Tengo una dirección en Rafael Calvo 40 → creo páginas por barrios automáticamente.
```

Dice:

```text
Tengo una dirección física → fijo NAP y Main City → construyo homepage, servicios, páginas servicio+Madrid, GeoHub Madrid y GeoArticles → uso barrios/zonas como señales GEO dentro del contenido, no como URLs por defecto.
```

### §20.2 Aplicado al ejemplo

```text
Dirección:
Rafael Calvo 40, Madrid

Main City:
Madrid
```

Arquitectura base:

```text
/
/cerrajero/apertura-puertas/
/cerrajero/cerrajero-urgente/
/madrid/
/cerrajero/madrid/apertura-puertas/
/cerrajero/madrid/cerrajero-urgente/
/madrid/cuanto-cuesta-un-cerrajero-urgente/
```

Si luego queremos crear páginas por zona o barrio, eso ya es una **expansión**, no la base GMB Crush.

---

## §21 Qué dice GMB Crush sobre elegir barrios, zonas o landmarks

GMB Crush **no da una fórmula cerrada tipo "elige estos 3 barrios"**.

Lo que sí dice es:

1. **El input inicial debe incluir Physical Address y Service Areas.**

   Es decir, la dirección física y las áreas relevantes son datos base de análisis local.

2. **La arquitectura base se construye con ciudad, no con barrio.**

   La homepage usa:

   ```text
   [Brand] + [Primary Service] + [Main City]
   ```

   Las páginas locales usan:

   ```text
   /category/city/service/
   ```

   Y el GeoHub es:

   ```text
   /city/
   ```

3. **Los barrios, zonas o landmarks se usan dentro del contenido como señales GEO.**

   GMB Crush los menciona en tres sitios:

   ```text
   Location-Based Service Pages:
   opening geo-specific con neighborhood / local issues

   GeoHub Pages:
   neighborhood coverage opcional

   GeoArticles:
   local references, landmarks, neighborhoods
   ```

4. **No se debe fingir ubicación física en esas zonas.**

   GeoArticles dice expresamente que deben enviar señales geográficas sin pretender que el negocio está físicamente ubicado allí si no es verdad.

---

## §22 Entonces, ¿cómo se deciden las zonas?

Según GMB Crush, se deciden así:

| Orden | Criterio | Qué significa |
|---:|---|---|
| 1 | **Dirección física** | Primero extraes la ciudad, barrio, distrito o zona que salen directamente del NAP. |
| 2 | **Main City** | La ciudad de la dirección se convierte en la base de la arquitectura. |
| 3 | **Service Areas / zonas relevantes** | Se identifican zonas que tienen sentido como señales GEO dentro de la ciudad o área principal. |
| 4 | **Neighborhood coverage** | Se usan barrios o zonas en GeoHub, páginas locales y artículos como cobertura semántica. |
| 5 | **Local issues / landmarks** | Se añaden referencias locales reales para dar contexto humano y GEO. |
| 6 | **No URLs automáticas** | Esas zonas no generan páginas por defecto. Solo se mencionan como señales GEO. |

### §22.1 Aplicado a Rafael Calvo 40, Madrid

| Paso | Resultado |
|---|---|
| Dirección física | Rafael Calvo 40, Madrid |
| Main City | Madrid |
| Zonas derivadas directas | Si la dirección está en Almagro / Chamberí, esas zonas son las primeras referencias GEO |
| Zonas cercanas o representativas | Se pueden usar como neighborhood coverage si son coherentes: Salamanca, Retiro, Centro, etc. |
| Uso en arquitectura | No crean URLs por defecto |
| Uso en contenido | Intro local, H2s, FAQs, GeoHub, GeoArticles, schema `areaServed` |

---

## §23 Regla final sobre barrios, zonas y landmarks

GMB Crush no dice:

```text
Crea páginas por barrios.
```

GMB Crush dice:

```text
Usa la dirección física para fijar Main City, crea páginas city+service, y usa barrios, zonas o landmarks como señales GEO dentro del contenido.
```

Y para elegir esas zonas:

```text
Empieza por las zonas derivadas directamente de la dirección física.
Después añade zonas cercanas o relevantes solo si tienen sentido GEO, semántico o competitivo.
No las conviertas en URLs salvo que pasen a una fase de expansión aprobada.
```

---

## §24 Test GMB Crush para saber si una zona tiene sentido

Una zona se puede añadir como señal GEO si cumple **al menos 3 de estos 6 criterios**.

| Criterio | Pregunta | Si la respuesta es sí |
|---|---|---|
| 1. Ancla física | ¿La zona sale directamente de la dirección? | Entra casi seguro |
| 2. Main City | ¿La zona pertenece claramente a la Main City? | Puede usarse como señal GEO |
| 3. Proximidad | ¿Está cerca o conectada al punto físico? | Puede usarse como zona candidata |
| 4. Intención local | ¿La zona ayuda a explicar una necesidad local real del servicio? | Puede aparecer en contenido |
| 5. Demanda o competencia | ¿Hay búsquedas o competidores trabajando esa zona? | Refuerza su inclusión |
| 6. No falsa ubicación | ¿Podemos mencionarla sin decir que tenemos oficina allí? | Es segura para contenido |

Si una zona solo cumple 1 criterio débil, no la metemos.

---

## §25 Regla práctica

### §25.1 Entra directamente

Zonas que salen de la dirección física.

Ejemplo:

```text
Dirección:
Calle Rafael Calvo 40, Barrio Almagro, Distrito Chamberí, Madrid
```

Entonces:

```text
Madrid = Main City
Almagro = zona GEO directa
Chamberí = zona GEO directa
```

Estas son coherentes porque salen del propio ancla físico.

### §25.2 Entra como candidata

Zonas que no salen de la dirección, pero pueden tener sentido por proximidad, búsqueda o competencia.

Ejemplo:

```text
Salamanca
Retiro
Centro
Tetuán
Chamartín
Arganzuela
Moncloa
Prosperidad
```

Estas no deberían añadirse automáticamente. Solo entran si podemos justificar que:

```text
están conectadas geográficamente
o tienen demanda
o aparecen en competencia
o ayudan a explicar contexto local real
```

### §25.3 No entra

Una zona no entra si:

```text
no sale de la dirección
no está conectada a la Main City
no aporta contexto local
no hay búsqueda ni competencia
solo se añade para inflar contenido
obliga a fingir ubicación física
```

Ejemplo incorrecto:

```text
"Cerrajero en Valencia" dentro de una página de Madrid.
```

Ejemplo también débil:

```text
Meter 20 barrios de Madrid en todas las páginas sin relación concreta.
```

---

## §26 Cómo se usa una zona aprobada

Una zona aprobada primero se usa como **señal GEO**, no como URL.

### §26.1 Correcto

```text
/cerrajero/madrid/cerrajero-urgente/
```

Dentro del contenido:

```text
Atendemos situaciones habituales de cerrajería urgente en Madrid, especialmente en zonas próximas al eje Almagro-Chamberí y otras áreas urbanas donde son frecuentes los problemas de acceso en viviendas, oficinas y comunidades.
```

### §26.2 Incorrecto

```text
/cerrajero/almagro/cerrajero-urgente/
```

si Almagro no está aprobada como Expansion Area.

---

## §27 Cuándo una zona pasa a página propia

Una zona solo puede pasar de "señal GEO" a "URL propia" si cumple criterios más fuertes:

| Criterio | Necesario para página propia |
|---|---|
| Está geográficamente clara | Sí |
| Tiene demanda de búsqueda | Muy recomendable |
| Competidores la trabajan | Muy recomendable |
| Puede tener contenido único | Sí |
| No duplica la página de Madrid | Sí |
| No finge oficina física | Obligatorio |
| Tiene valor comercial | Sí |

Ejemplo:

```text
/madrid/chamberi/
```

o:

```text
/cerrajero/madrid/chamberi/cerrajero-urgente/
```

solo si Chamberí pasa a **Approved Expansion Area**.

---

## §28 Aplicado a Rafael Calvo 40, Madrid

| Zona | Decisión correcta |
|---|---|
| Madrid | Crea arquitectura base |
| Almagro | Señal GEO directa |
| Chamberí | Señal GEO directa |
| Salamanca | Candidata, validar proximidad/demanda/competencia |
| Retiro | Candidata, validar antes de usar fuerte |
| Centro | Candidata, no automática |
| Tetuán | Candidata, no automática |
| Chamartín | Candidata, no automática |
| Arganzuela | Candidata, no automática |

---

## §29 Fórmula final

```text
Dirección física → Main City → zonas directas → zonas candidatas → validación → uso en contenido → expansión solo si procede
```

En una frase:

```text
Una zona tiene sentido GEO si sale del ancla física o ayuda a reforzar la relevancia local de la Main City sin crear una falsa ubicación, y si además puede justificarse por proximidad, demanda, competencia o contexto real del servicio.
```

---

# Bloque IV — Checklist Final

## §30 Checklist final del Paso 1

| Check | Pregunta | Estado |
|---|---|---|
| Business Name | ¿El nombre coincide con la entidad real y el GBP? | ✅ / ⬜ |
| Canonical Domain | ¿Hay una sola versión canónica del dominio? | ✅ / ⬜ |
| NAP | ¿El NAP es completo y consistente? | ✅ / ⬜ |
| Primary Category | ¿La categoría principal GBP está clara? | ✅ / ⬜ |
| Additional Categories | ¿Se detectaron categorías cubiertas y categorías que necesitan página? | ✅ / ⬜ |
| Main City | ¿La Main City está definida y no se mezcla con áreas de cobertura? | ✅ / ⬜ |
| Local Coverage Areas | ¿Las áreas de cobertura son reales y no generan URLs por defecto? | ✅ / ⬜ |
| Approved Expansion Areas | ¿Las zonas con página propia están aprobadas o vacías en fase base? | ✅ / ⬜ |
| Servicios principales | ¿Los servicios principales están listados y priorizados? | ✅ / ⬜ |
| CTA | ¿El CTA principal está definido? | ✅ / ⬜ |

# Bloque V — Outputs

## §31 Outputs del Paso 1

Los outputs del Paso 1 son los valores generados en la subsección `.3 Output del paso` de cada concepto del Bloque II — Ejecución por la IA:

- §5.3 Output de Business Name
- §6.3 Output de Website URL
- §8.3 Output de Full NAP
- §9.3 Output de Planned Primary GBP Category
- §10.3 Output de Planned Additional GBP Categories
- §11.3 Output de Main City
- §12.3 Output de Physical Location City
- §13.3 Output de Servicios principales
- §14.3 Output de Local Coverage Areas
- §15.3 Output de Approved Expansion Areas
- §17.3 Output de Preferred CTA
- §18.3 Output de Trust Signals

Para ver los valores rellenados completos del ejemplo Cerrajeros Madrid 24h, ir a §4 Ejemplo rellenado.

# Bloque VI — Fuentes Internas GMB Crush Usadas

# §32 Fuentes internas GMB Crush usadas

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
