Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo la estructura fija acordada en la conversación.
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# §1 Paso 3 — Matriz Base

# Bloque I — Introducción

## §2 Objetivo del Paso 3

Convertir el inventario calculado en Paso 2 en una **URL Matrix operativa** — una tabla donde cada URL del cluster ocupa una fila con todos los campos de producción (URL, H1, Meta Title, Schema, Priority, Phase, Status, Parent Page, Internal links, Notes).

**Outputs del paso:**

- **Spreadsheet Name** — nombre del archivo/spreadsheet que contiene la matriz
- **GeoHub URL Style** — Option A `/city/` o Option B `/category/city/` (decisión de diseño)
- **Additional Category Slugs** — slugs URL-safe para las Additional Categories que necesitan página propia
- **URL Matrix completa** — N filas (28 para Cerrajeros) con todos los campos rellenos
- **IDs por tipo de página** — HP, SO-N, GH, LBS-N, AC-N, GA-N
- **Parent Page declarado por fila** — jerarquía del cluster
- **Schema asignado por fila** — desde la matriz, no en build-time
- **Enlaces internos Required por fila** — linking contractual
- **Priority y Publish Phase por fila** — orden y agrupación
- **Default Page Status** — estado inicial de cada fila (Planned)
- **Notes estratégicas por fila** — decisiones que no encajan en columnas estructuradas
- **GeoArticle Topics propuestos** — 15 topics derivados de servicio + Main City + intención long-tail
- **Validaciones** — LCAs sin filas base, matriz cerrada antes de contenido

**Errores que previene:**

- Crear URLs sin ID ni estado
- Perder la relación entre página padre y página hija
- Generar filas para Local Coverage Areas sin aprobación
- Olvidar schema o enlaces internos en la planificación
- Publicar páginas sin saber qué función cumplen

**Cuándo se ejecuta:** después de Paso 2 cerrado (fórmula aplicada). Antes de Paso 4 (URL Rules) y Paso 15 (Redacción de contenido).

## §3 Info heredada de pasos anteriores

> Estos campos NO se deciden en Paso 3 — la IA los lee del paso indicado y los usa como input para construir la URL Matrix del Bloque II.

| Campo | Origen |
|---|---|
| Website Root Domain | Paso 1 §6 |
| Canonical Domain | Paso 1 §6 |
| Planned Primary GBP Category | Paso 1 §9 |
| Primary Category Slug | Paso 2 §6 |
| Main City | Paso 1 §11 |
| Main City Slug | Paso 2 §6 |
| Servicios principales (5 core services) | Paso 1 §13 |
| Service Slugs | Paso 2 §6 |
| Additional Categories que necesitan página | Paso 1 §10 |
| Local Coverage Areas | Paso 1 §14 |
| Approved Expansion Areas | Paso 1 §15 |
| GeoArticles per Service (G) | Paso 1 §16 |

> Las decisiones nuevas que se toman en Paso 3 (Spreadsheet Name, GeoHub URL Style, Additional Category Slugs) tienen sus propias secciones en Bloque II — §5, §6 y §7. Default Page Status y Default Priority son outputs de §15 y §14 respectivamente.

## §4 Ejemplo rellenado

> Todos los outputs del Paso 3 con sus valores para Cerrajeros Madrid 24h. Los heredados (Domain, Categories, Servicios, etc.) tienen su ejemplo en sus pasos de origen (§4 de Paso 1 y Paso 2).

### Outputs del paso

| Output | Valor |
|---|---|
| Spreadsheet Name | `Cerrajeros Madrid 24h – GMB Crush Website Architecture` |
| GeoHub URL Style | Option A → `/madrid/` |
| Additional Category Slugs | `duplicado-llaves` (1 slug, A=1) |
| Default Page Status | `Planned` (estado inicial de cada fila) |
| Default Priority | P3 (default; sobreescrito por tipo de página) |

### URL Matrix base — 28 filas SEO + 1 auxiliar

| ID | URL | Tipo | Schema | Priority | Phase | Status |
|---|---|---|---|---|---|---|
| HP | `/` | Homepage | Organization + WebSite + LocalBusiness + FAQPage + Speakable | P1 | 1 | Planned |
| SO-1 | `/cerrajero/cerrajero-urgente/` | Service Overview | Service + WebPage + BreadcrumbList | P1 | 1 | Planned |
| SO-2 | `/cerrajero/apertura-puertas/` | Service Overview | Service + WebPage + BreadcrumbList | P1 | 1 | Planned |
| SO-3 | `/cerrajero/cambio-cerraduras/` | Service Overview | Service + WebPage + BreadcrumbList | P1 | 1 | Planned |
| SO-4 | `/cerrajero/cambio-bombines/` | Service Overview | Service + WebPage + BreadcrumbList | P1 | 1 | Planned |
| SO-5 | `/cerrajero/instalacion-cerraduras-seguridad/` | Service Overview | Service + WebPage + BreadcrumbList | P1 | 1 | Planned |
| GH | `/madrid/` | GeoHub | CollectionPage + BreadcrumbList | P1 | 1 | Planned |
| LBS-1 | `/cerrajero/madrid/cerrajero-urgente/` | LBS | LocalBusiness + BreadcrumbList | P1 | 1 | Planned |
| LBS-2 | `/cerrajero/madrid/apertura-puertas/` | LBS | LocalBusiness + BreadcrumbList | P1 | 1 | Planned |
| LBS-3 | `/cerrajero/madrid/cambio-cerraduras/` | LBS | LocalBusiness + BreadcrumbList | P1 | 1 | Planned |
| LBS-4 | `/cerrajero/madrid/cambio-bombines/` | LBS | LocalBusiness + BreadcrumbList | P1 | 1 | Planned |
| LBS-5 | `/cerrajero/madrid/instalacion-cerraduras-seguridad/` | LBS | LocalBusiness + BreadcrumbList | P1 | 1 | Planned |
| AC-1 | `/cerrajero/madrid/duplicado-llaves/` | Additional Category | Service + BreadcrumbList | P2 | 1 | Planned |
| GA-1 | `/madrid/cuanto-cuesta-un-cerrajero-urgente/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-2 | `/madrid/que-hacer-si-no-puedes-entrar-casa/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-3 | `/madrid/cuanto-tarda-un-cerrajero/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-4 | `/madrid/cuanto-cuesta-abrir-una-puerta/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-5 | `/madrid/que-hacer-si-te-dejas-las-llaves-dentro/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-6 | `/madrid/apertura-de-puertas-sin-romper-cerradura/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-7 | `/madrid/cuando-cambiar-la-cerradura-de-casa/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-8 | `/madrid/cambio-de-cerradura-tras-perder-llaves/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-9 | `/madrid/cerradura-nueva-o-reparacion/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-10 | `/madrid/cuando-cambiar-el-bombin/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-11 | `/madrid/bombin-antibumping-madrid/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-12 | `/madrid/cambio-de-bombin-sin-cambiar-cerradura/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-13 | `/madrid/mejores-cerraduras-de-seguridad-para-viviendas/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-14 | `/madrid/cerraduras-de-seguridad-para-comunidades/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| GA-15 | `/madrid/instalar-cerradura-de-seguridad-en-puerta-blindada/` | GeoArticle | Article + FAQPage + BreadcrumbList | P3 | 2 | Planned |
| AUX | `/contacto/` | Auxiliar | ContactPoint | P4 | 1 | Planned |

### LCAs (no generan filas)

| LCA | Tratamiento en matriz |
|---|---|
| Almagro, Chamberí, Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad | Sin filas URL — viven en contenido y schema `areaServed` |

### Validaciones

| Validación | Resultado para Cerrajeros |
|---|---|
| Una fila por URL | ✅ 28 filas SEO + 1 auxiliar |
| ID único por tipo | ✅ HP, SO-1..5, GH, LBS-1..5, AC-1, GA-1..15, AUX |
| Parent Page declarado | ✅ cada fila apunta a una URL existente o `–` (Homepage root) |
| Schema asignado desde matriz | ✅ no se decide en build-time |
| Internal links Required | ✅ contractual por tipo de página (ver Paso 7) |
| Anti-duplicación | ✅ Servicio de cerrajería de urgencia consolidada con LBS-1 |
| Matriz cerrada antes de contenido | ✅ todos los campos rellenos antes de Paso 15 |

# Bloque II — Ejecución por la IA

## §5 Spreadsheet Name

### §5.1 Explicación

**Explicación**

El nombre del spreadsheet (Google Sheets, Airtable, Notion DB) que contendrá la URL Matrix del cluster. Identifica al cliente y al sistema GMB Crush. Se reutiliza en filenames de exports, referencias internas y handoffs entre operadores.

**Patrón o fórmula**

```text
[Business Name] – GMB Crush Website Architecture
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h – GMB Crush Website Architecture
```

**Ejemplos incorrectos**

```text
- URL Matrix v3 final.xlsx
- Sheet sin nombre
- Cliente1_matriz_2024 (no identifica al cliente real)
- Mezclar varios clientes en un solo spreadsheet
```

**Regla final**

```text
El spreadsheet name identifica al cliente y al sistema; reutilizable en filenames y referencias.
```

### §5.2 Cómo obtenemos el Spreadsheet Name

**Fuente:** Decisión de diseño.

**Método:** Aplicar la fórmula `[Business Name] – GMB Crush Website Architecture` usando el Business Name del Paso 1 §5.

### §5.3 Output del paso

**Tipo:** String — nombre del spreadsheet/archivo.

**Ejemplo (Cerrajeros Madrid 24h):** `Cerrajeros Madrid 24h – GMB Crush Website Architecture`.

## §6 GeoHub URL Style

### §6.1 Explicación

**Explicación**

La URL del GeoHub de la Main City puede tener dos formas según preferencia de arquitectura. Esta decisión afecta a TODAS las URLs tipo GeoHub del cluster y debe tomarse antes de generar la matriz. Cambiarla mid-build obliga a regenerar URLs y redirects.

**Patrón o fórmula**

```text
Option A: /city/             → ej: /madrid/         (GeoHub limpio)
Option B: /category/city/    → ej: /cerrajero/madrid/ (GeoHub bajo categoría)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Option A: /madrid/
```

**Ejemplos incorrectos**

```text
- Mezclar Option A y Option B en el mismo cluster
- Cambiar de Option A a Option B después de publicar URLs
- Crear /madrid/ y /cerrajero/madrid/ ambas como GeoHub
```

**Regla final**

```text
Una sola GeoHub URL Style consistente en todo el cluster, decidida antes de generar URLs.
```

### §6.2 Cómo obtenemos el GeoHub URL Style

**Fuente:** Decisión de diseño.

**Método:** Elegir Option A (default) salvo que el cliente tenga razones específicas para anidar el GeoHub bajo la Primary Category (Option B). La decisión debe tomarse antes de generar las URLs base.

### §6.3 Output del paso

**Tipo:** Enum — Option A o Option B.

**Ejemplo (Cerrajeros Madrid 24h):** Option A → `/madrid/`.

## §7 Additional Category Slugs

### §7.1 Explicación

**Explicación**

Las Additional Categories que necesitan página propia (Paso 1 §10) necesitan slugs URL-safe específicos. La transformación es la misma que la del Paso 2 §6 Slug Generation, pero aplicada al subconjunto de Additional Categories no cubiertas por core services.

**Patrón o fórmula**

```text
additional_category_slug = slugify(additional_category_name)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Servicio de duplicado de llaves → duplicado-llaves
```

**Ejemplos incorrectos**

```text
- Slugs largos: servicio-de-duplicado-de-llaves
- Slugs con tildes: cerrajería-urgente
- Slugs duplicados con core service slugs
- Inventar slugs que no derivan del nombre real
```

**Regla final**

```text
Cada Additional Category con página propia tiene un slug derivado limpio y único.
```

### §7.2 Cómo obtenemos los Additional Category Slugs

**Fuente:** GMB Crush ← heredados del Paso 1 §10.

**Método:** Aplicar la transformación slugify (ver Paso 2 §6) a cada Additional Category que necesita página propia. Validar que los slugs no colisionen con Service Slugs ni Primary Category Slug.

### §7.3 Output del paso

**Tipo:** Lista de slugs URL-safe (uno por Additional Category con página propia).

**Ejemplo (Cerrajeros Madrid 24h):** `duplicado-llaves`.

## §8 Cada URL del cluster es una fila

### §8.1 Explicación

**Explicación**

La matriz base convierte arquitectura en producción. Si una página no tiene fila, no existe dentro del sistema operativo.

**Patrón o fórmula**

```text
One URL = one row = one page type = one function
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h tiene una fila para /cerrajero/madrid/cerrajero-urgente/ y no tiene filas para /almagro/ en la fase base.
```

**Ejemplos incorrectos**

```text
- Crear contenido sin fila
- Crear URL fuera de la matriz
- Publicar sin ID
- Crear filas para Almagro, Salamanca y Retiro como cobertura sin aprobación
- Añadir ideas de artículos sin URL
- Duplicar una misma URL con dos IDs
```

**Regla final**

```text
Cada URL real del cluster ocupa exactamente una fila con todos sus campos rellenos.
```

**Validación operativa**

La matriz base no es una lista de ideas; es una tabla de producción. Cada fila debe corresponder a una URL real que se va a crear o mantener. Si una zona solo se menciona dentro del contenido, no debe aparecer como fila.

### §8.2 Cómo obtenemos las filas de la matriz

**Fuente:** GMB Crush.

**Método:** Para cada URL del cluster (heredada de Paso 2 §15 Tabla de inventario base), crear una fila con todos los campos obligatorios (§18 Columnas obligatorias). Una URL = una fila exacta.

### §8.3 Output del paso

**Tipo:** N filas en el spreadsheet (donde N = total de URLs del cluster).

**Ejemplo (Cerrajeros Madrid 24h):** 28 filas (1 Homepage + 5 SO + 1 GeoHub + 5 LBS + 1 Additional + 15 GeoArticles).

## §9 Local Coverage Areas no tienen filas base

### §9.1 Explicación

**Explicación**

Almagro, Chamberí, Salamanca y Retiro son zonas de cobertura en el ejemplo, pero no generan filas mientras no sean Approved Expansion Areas.

**Patrón o fórmula**

```text
Main City → City column | Local Coverage Areas → Notes / Content Brief
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Las filas comerciales de Cerrajeros Madrid 24h usan City = Madrid; Almagro, Chamberí, Salamanca y Retiro quedan en Notes como Local Coverage Areas.
```

**Ejemplos incorrectos**

```text
- GH-002 /almagro/ sin aprobación
- LBS para Salamanca en fase base
- GeoArticle de Retiro sin landing
- Poner Almagro en la columna City sin URL aprobada
- Crear slugs de cobertura en la matriz base
- Mezclar ciudad principal y zonas de cobertura en el mismo campo
```

**Regla final**

```text
Las Local Coverage Areas no generan filas en la matriz base; refuerzan contenido y schema.
```

**Validación operativa**

En la matriz base, el campo City debe corresponder a la Main City. Las Local Coverage Areas pueden aparecer en notas o contenido, pero no como city rows.

### §9.2 Cómo obtenemos la exclusión de LCAs de la matriz

**Fuente:** GMB Crush ← heredado del Paso 1 §14 Local Coverage Areas.

**Método:** No crear filas en la matriz base para LCAs. La columna geográfica usa la Main City (Paso 1 §11). Las LCAs aparecen en contenido y schema `areaServed`, no como URLs.

### §9.3 Output del paso

**Tipo:** 0 filas adicionales por LCA en la matriz base.

**Ejemplo (Cerrajeros Madrid 24h):** 0 filas extra para Almagro, Chamberí, Salamanca, Retiro, etc.

## §10 ID por tipo de página

### §10.1 Explicación

**Explicación**

Los IDs permiten filtrar, auditar y producir por lotes.

**Patrón o fórmula**

```text
HP                    (sin sufijo — solo hay una Homepage)
GH                    (sin sufijo — solo hay un GeoHub Main City)
SO-N, LBS-N, AC-N, GA-N    (correlativo simple, N empieza en 1)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
HP identifica `/`. SO-1 identifica /cerrajero/cerrajero-urgente/.
LBS-1 identifica /cerrajero/madrid/cerrajero-urgente/.
GA-1 identifica /madrid/cuanto-cuesta-un-cerrajero-urgente/.
```

**Ejemplos incorrectos**

```text
- IDs aleatorios
- No usar IDs
- Mismo ID para varias URLs
- Usar IDs aleatorios
- Repetir LBS-001 para varias páginas
- No diferenciar artículos de páginas comerciales
```

**Regla final**

```text
Cada fila tiene un ID único derivado del tipo de página y su contenido.
```

**Validación operativa**

Cada fila necesita un ID legible para controlar producción, QA y enlaces. El ID debe indicar el tipo de página y su orden, sin depender de títulos largos o slugs complejos.

### §10.2 Cómo obtenemos el ID por tipo de página

**Fuente:** GMB Crush.

**Método:** Asignar ID por tipo según la nomenclatura GMB Crush: `HP`, `SO-N`, `GH`, `LBS-N`, `AC-N`, `GA-N`. El número N es secuencial dentro del tipo.

### §10.3 Output del paso

**Tipo:** String único por fila (formato `tipo-N`).

**Ejemplo (Cerrajeros Madrid 24h):** `HP`, `SO-1`, `SO-2`, ..., `LBS-1`, ..., `GA-15`.

## §11 Parent Page obligatorio

### §11.1 Explicación

**Explicación**

Cada página debe tener una relación de dependencia. Esto evita páginas huérfanas.

**Patrón o fórmula**

```text
Page Type → Parent Page → Internal Link Required
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
La página /cerrajero/madrid/cerrajero-urgente/ tiene como parent /cerrajero/cerrajero-urgente/ y como GeoHub /madrid/.
```

**Ejemplos incorrectos**

```text
- GeoArticle sin service page
- Additional Category sin GeoHub
- Service Overview sin homepage
- Dejar Parent Page vacío en páginas locales
- Asignar homepage como padre de todos los artículos
- Usar una página inexistente como parent
```

**Regla final**

```text
Cada fila debe declarar Parent Page existente; no hay páginas huérfanas en la matriz.
```

**Validación operativa**

Cada página que no sea homepage necesita una página padre o una página de soporte. Esto ayuda a construir el silo y a saber desde dónde se enlazará cada URL.

### §11.2 Cómo obtenemos el Parent Page

**Fuente:** GMB Crush.

**Método:** Cada fila declara explícitamente su Parent Page (la URL padre en la jerarquía). Homepage es root (parent vacío o `–`); el resto debe apuntar a una URL existente en la propia matriz.

### §11.3 Output del paso

**Tipo:** String — URL del parent (vacío solo para Homepage).

**Ejemplo (Cerrajeros Madrid 24h):** Homepage parent = `–`. SO Cerrajero urgente parent = `/`. LBS Cerrajero urgente Madrid parent = `/cerrajero/cerrajero-urgente/`.

## §12 Schema asignado desde la matriz

### §12.1 Explicación

**Explicación**

La matriz debe definir el schema antes de producir contenido.

**Patrón o fórmula**

```text
Page Type → Schema Required → QA Schema
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-001 usa LocalBusiness y BreadcrumbList; GA-001 usa Article, FAQPage, BreadcrumbList y Speakable.
```

**Ejemplos incorrectos**

```text
- Schema decidido al final
- Mismo schema para todo
- Sin schema en GeoArticles
- Dejar schema vacío hasta el final
- Usar Article schema en una landing comercial
- Usar LocalBusiness con dirección falsa en una zona de cobertura
```

**Regla final**

```text
Cada fila tiene Schema Type asignado desde la matriz; el implementador no decide schema.
```

**Validación operativa**

La matriz debe incluir schema requerido por tipo de página para que el equipo no lo decida al final. Esto evita que páginas locales salgan sin LocalBusiness, Service, Article o BreadcrumbList.

### §12.2 Cómo obtenemos el Schema asignado

**Fuente:** GMB Crush.

**Método:** Cada fila declara Schema Type según el page type (Homepage → Organization + LocalBusiness; SO → Service; GeoHub → Place; LBS → Service + LocalBusiness; AC → Service; GA → Article). El implementador no decide schema en build time.

### §12.3 Output del paso

**Tipo:** Schema Type(s) por fila (uno o más, separados por `+`).

**Ejemplo (Cerrajeros Madrid 24h):** Homepage → `Organization + LocalBusiness`. SO → `Service`. LBS → `Service + LocalBusiness`.

## §13 Enlaces internos Required

### §13.1 Explicación

**Explicación**

La matriz debe listar enlaces obligatorios para evitar páginas aisladas.

**Patrón o fórmula**

```text
Source URL → Required Links → QA de enlaces
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-001 requiere enlaces a /cerrajero/cerrajero-urgente/, /madrid/, páginas relacionadas en Madrid y GeoArticles.
```

**Ejemplos incorrectos**

```text
- Solo footer links
- Sin enlace al GeoHub
- Sin enlace al servicio padre
- Publicar páginas sin enlaces obligatorios
- Enlazar a áreas de cobertura sin URL
- Usar solo enlaces de footer
```

**Regla final**

```text
Cada fila lista los enlaces internos requeridos; el linking es contractual, no opcional.
```

**Validación operativa**

La matriz debe listar enlaces obligatorios para cada URL. Sin esta columna, las páginas pueden publicarse aisladas y el sistema pierde fuerza de silo.

### §13.2 Cómo obtenemos los enlaces internos Required

**Fuente:** GMB Crush.

**Método:** Cada fila lista los enlaces internos obligatorios (internal_links_required) según el internal linking framework (Paso 7). El linking es contractual: ausentes los enlaces, la página queda incompleta.

### §13.3 Output del paso

**Tipo:** Lista de URLs internas obligatorias por fila.

**Ejemplo (Cerrajeros Madrid 24h):** SO Cerrajero urgente → enlaces a `/`, `/madrid/`, `/cerrajero/madrid/cerrajero-urgente/`, otras SO.

## §14 Priority y Publish Phase

### §14.1 Explicación

**Explicación**

Cada fila debe tener prioridad y fase. La matriz no es solo inventario, también es cola de producción.

**Patrón o fórmula**

```text
Priority Tier + Dependency → Publish Phase
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
GA-001 puede ser P3, pero queda en Phase 3 porque primero deben existir /madrid/ y /cerrajero/madrid/cerrajero-urgente/.
```

**Ejemplos incorrectos**

```text
- Todas P1
- Sin fase
- Publicar según intuición
- Publicar GeoArticles P3 antes de landings P1
- Confundir score alto con listo para publicar
- No marcar páginas bloqueadas por dependencia
```

**Regla final**

```text
Priority y Publish Phase son campos separados; nunca se confunden ni se mezclan.
```

**Validación operativa**

La prioridad mide importancia estratégica; la fase mide cuándo se publica. Una página P1 puede estar bloqueada si su padre no existe. La matriz debe incluir ambos campos para evitar publicar por impulso.

### §14.2 Cómo obtenemos la Priority y Publish Phase

**Fuente:** GMB Crush.

**Método:** Priority captura el orden de importancia (P1 alta → P4 baja); Publish Phase captura cuándo se publica (Phase 1, 2, 3...). Default Priority del intake aplica a filas sin override explícito. Son dos campos independientes que NUNCA se mezclan.

### §14.3 Output del paso

**Tipo:** Priority (P1-P4) + Publish Phase (Phase 1-N) por fila.

**Ejemplo (Cerrajeros Madrid 24h):** Homepage = P1, Phase 1. SO core services = P1, Phase 1. GeoArticles = P3, Phase 2.

## §15 Default Page Status

### §15.1 Explicación

**Explicación**

El estado permite saber si una página está planificada, en borrador, en QA o publicada.

**Patrón o fórmula**

```text
Planned → Draft → Ready for QA → Approved → Published
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h marca /cerrajero/madrid/cerrajero-urgente/ como Planned hasta que el contenido y links estén listos.
```

**Ejemplos incorrectos**

```text
- Publicada sin QA
- Borrador sin responsable
- Estado vacío
- Usar estados vagos como “en proceso”
- Publicar sin pasar por Ready for QA
- No actualizar estado después de QA
```

**Regla final**

```text
Status refleja el estado real de cada fila a lo largo del ciclo de vida de la página.
```

**Validación operativa**

Cada URL necesita un estado para controlar el flujo de producción. Planned, Draft, Ready for QA, Approved y Published son estados suficientes para saber qué hacer con cada fila.

### §15.2 Cómo obtenemos el Default Page Status

**Fuente:** GMB Crush.

**Método:** Status refleja el estado real de cada fila a lo largo del ciclo de vida (Planned → Draft → Published). Default Page Status del intake aplica a filas nuevas; se actualiza manualmente al avanzar de fase.

### §15.3 Output del paso

**Tipo:** Enum — Planned / Draft / Published.

**Ejemplo (Cerrajeros Madrid 24h):** Default Page Status = `Planned`. Cada fila arranca como Planned hasta que se redacte.

## §16 Notes para decisiones estratégicas

### §16.1 Explicación

**Explicación**

La columna Notes debe registrar por qué una página existe, qué categoría soporta, si consolida una categoría adicional o qué cobertura local debe mencionarse. Esto ayuda a evitar repetir discusiones.

**Patrón o fórmula**

```text
Decisión estratégica → Notes → trazabilidad
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
La fila /cerrajero/madrid/cerrajero-urgente/ indica que soporta Primary Category Cerrajero y Additional Category Servicio de cerrajería de urgencia.
```

**Ejemplos incorrectos**

```text
- Dejar notas vacías en páginas complejas
- No documentar por qué una categoría adicional se consolida
- No indicar Local Coverage Areas relevantes
```

**Regla final**

```text
Las Notes capturan decisiones estratégicas que no encajan en columnas estructuradas.
```

**Validación operativa**

La columna Notes debe registrar por qué una página existe, qué categoría soporta, si consolida una categoría adicional o qué cobertura local debe mencionarse. Esto ayuda a evitar repetir discusiones.

### §16.2 Cómo obtenemos las Notes estratégicas

**Fuente:** Decisión de diseño.

**Método:** Cada fila tiene un campo Notes opcional para capturar decisiones que no encajan en columnas estructuradas: razón de un Priority anómalo, dependencia con otro paso, observación del cliente, excepción a la doctrina, etc.

### §16.3 Output del paso

**Tipo:** String libre, opcional, por fila.

**Ejemplo (Cerrajeros Madrid 24h):** Homepage Notes = `Cliente solicita H1 con 'Madrid 24h' literal por reconocimiento de marca`.

## §17 Matriz base antes de contenido

### §17.1 Explicación

**Explicación**

No se debe escribir contenido página por página sin haber cerrado la matriz. La matriz es el contrato operativo entre arquitectura, contenido, schema, enlaces y publicación.

**Patrón o fórmula**

```text
URL Matrix aprobada → briefs → contenido → QA
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h aprueba primero sus 28 URLs base antes de redactar los textos de homepage, servicios, GeoHub y GeoArticles.
```

**Ejemplos incorrectos**

```text
- Redactar páginas sin saber si existen en la matriz
- Crear nuevos slugs durante escritura
- Cambiar page type sin actualizar matriz
```

**Regla final**

```text
La matriz base se cierra antes de empezar contenido; un cambio aguas abajo obliga a reabrirla.
```

**Validación operativa**

No se debe escribir contenido página por página sin haber cerrado la matriz. La matriz es el contrato operativo entre arquitectura, contenido, schema, enlaces y publicación.

### §17.2 Cómo obtenemos el cierre de la matriz base

**Fuente:** GMB Crush.

**Método:** La URL Matrix se cierra (todos los campos rellenos para todas las filas) ANTES de empezar redacción de contenido (Paso 15) o construcción (Paso 17). Cualquier cambio aguas abajo obliga a reabrir la matriz y reaplicar QA.

### §17.3 Output del paso

**Tipo:** Boolean implícito — matriz cerrada (sí/no).

**Ejemplo (Cerrajeros Madrid 24h):** Matriz cerrada con 28 filas, todos los campos rellenos, antes de iniciar Paso 15 Redacción.

## §18 Columnas obligatorias de la URL Matrix

| Columna | Nombre | Función |
|---|---|---|
| A | ID | Identificador único |
| B | Page Type | Tipo de página GMB Crush |
| C | Parent Page | Página padre |
| D | Service | Servicio |
| E | Service Slug | Slug del servicio |
| F | Main City | Ciudad principal |
| G | Main City Slug | Slug de la ciudad |
| H | Additional Category | Categoría adicional, si aplica |
| I | Local Coverage Areas | Zonas mencionadas en contenido |
| J | Approved Expansion Area | Solo si aplica |
| K | URL | URL final |
| L | H1 | H1 recomendado |
| M | Meta Title | Title SEO |
| N | Meta Description | Descripción SEO |
| O | Schema Type | Schema recomendado |
| P | Enlaces internos Required | Enlaces obligatorios |
| Q | Priority | P1/P2/P3/P4 |
| R | Publish Phase | Fase |
| S | Status | Estado |
| T | Notes | Notas estratégicas |

## §19 Ejemplo de URL Matrix base

### Patrones URL por tipo de página

Antes del ejemplo, la matriz se construye aplicando estos patrones URL por tipo. Todos derivan de los slugs declarados en §6 (GeoHub URL Style) y §7 (Additional Category Slugs) + heredados de Paso 2 §6 (Slug Generation).

```text
Homepage             /
Service Overview     /{primary-cat-slug}/{service-slug}/
GeoHub Main City     /{main-city-slug}/                                  (si Option A; si Option B → /{primary-cat-slug}/{main-city-slug}/)
LBS                  /{primary-cat-slug}/{main-city-slug}/{service-slug}/
Additional Category  /{primary-cat-slug}/{main-city-slug}/{additional-slug}/
GeoArticle           /{main-city-slug}/{topic-slug}/
```

> **Regla:** Additional Category Pages siguen el mismo patrón que LBS (`/cat/city/slug/`), NO el patrón GeoArticle (`/city/slug/`). Esto las mantiene como páginas comerciales bajo la categoría principal, con la ciudad como nivel intermedio.

### Ejemplo aplicado a Cerrajeros Madrid 24h

| ID | Page Type | URL | H1 | Schema | Priority | Phase |
|---|---|---|---|---|---|---|
| HP | Homepage | `/` | Cerrajeros Madrid 24h – Servicios de cerrajería de confianza en Madrid | Organization, WebSite, LocalBusiness | P1 | Phase 1 |
| SO-1 | Service Overview | `/cerrajero/cerrajero-urgente/` | Servicios profesionales de cerrajería urgente por Cerrajeros Madrid 24h | Service, WebPage, BreadcrumbList | P1 | Phase 1 |
| GH | GeoHub | `/madrid/` | Cerrajeros Madrid 24h – Servicios de cerrajería en Madrid | CollectionPage, BreadcrumbList | P1 | Phase 1 |
| LBS-1 | Location-Based Service | `/cerrajero/madrid/cerrajero-urgente/` | Cerrajeros Madrid 24h – Cerrajero urgente en Madrid | LocalBusiness, BreadcrumbList | P1 | Phase 2 |
| AC-1 | Additional Category | `/cerrajero/madrid/duplicado-llaves/` | Cerrajeros Madrid 24h – Duplicado de llaves experto en Madrid | Service, BreadcrumbList | P3 | Phase 2 |
| GA-1 | GeoArticle | `/madrid/cuanto-cuesta-un-cerrajero-urgente/` | Precio de cerrajero urgente en Madrid | Article, FAQPage, BreadcrumbList | P3 | Phase 3 |

## §20 Filas que NO se generan en la base

```text
/almagro/
/cerrajero/almagro/cerrajero-urgente/
/chamberi/
/cerrajero/salamanca/apertura-puertas/
/retiro/cuanto-cuesta-un-cerrajero-urgente/
```

Estas URLs solo se generarían si esas zonas pasan a Approved Expansion Areas.

# Bloque III — Módulo doctrinal: GeoArticle Topics

## §21 GeoArticle Topics — método de extracción

### §21.1 Explicación

Los topics de GeoArticle no se inventan: se extraen mediante keyword research por servicio core. La fórmula maestra del Paso 2 fija la cantidad (G × S = N artículos), pero los temas concretos requieren validación con datos reales de búsqueda antes de producirse. Sin keyword research el GeoArticle nace sin demanda real y se vuelve thin content.

### §21.2 Patrón o método

```text
Por cada core service (paso-01 §14, filas 1.34–1.38):

1. Ejecutar keyword research con volumen ≥ X impresiones/mes
   y dificultad ≤ Y (umbrales del cliente / sector).
2. Filtrar queries con intent informativo:
   - cómo, qué, cuándo, por qué, cuánto, dónde, cuál, mejor.
3. Excluir queries con intent transaccional o que coincidan
   con la query de la LBS (anti-canibalización paso-04 §21).
4. Seleccionar G topics por servicio (G=3 por defecto, paso-02 §11):
   - Priorizar volumen alto + dificultad baja.
   - Asegurar complementariedad: cada topic responde una intención
     distinta dentro del mismo servicio.
5. Generar el slug del topic:
   - Base = la query como apareció en keyword research.
   - Normalizar siguiendo paso-04 §17–§19 (lowercase, sin acentos,
     guiones medios, sin adjetivos SEO vacíos).
6. Construir la URL del GeoArticle:
   - Patrón: /[main-city]/[topic-slug]/ (paso-04 §14).
```

### §21.3 Ejemplo correcto con Cerrajeros Madrid 24h

15 GeoArticles = 5 servicios core × G=3 topics. Ver listado completo en §24.1.

### §21.4 Ejemplos incorrectos

```text
- Inventar topics por intuición sin datos de búsqueda
- Usar el mismo topic para varios servicios (canibalización)
- Crear GeoArticles con intent transaccional que ya cubre la LBS
- Topics con dificultad muy alta sin volumen que la justifique
- Slug que no es la query real (manipulado para SEO)
- GeoArticles sin servicio core asignado (huérfanos)
```

### §21.5 Regla final

```text
Los topics de GeoArticle se descubren con keyword research por servicio
core. Cantidad fija por fórmula, contenido validado por datos reales.
```

# Bloque IV — Checklist Final

## §22 Checklist final del Paso 3

| Check | Pregunta | Estado |
|---|---|---|
| ID | ¿Cada página tiene identificador único? | ✅ / ⬜ |
| Page Type | ¿Cada fila tiene tipo de página correcto? | ✅ / ⬜ |
| Parent Page | ¿Cada página tiene dependencia clara? | ✅ / ⬜ |
| Main City | ¿La base usa solo la Main City? | ✅ / ⬜ |
| Local Coverage Areas | ¿Se documentan sin generar URLs? | ✅ / ⬜ |
| URL | ¿La URL sigue el patrón del Paso 4? | ✅ / ⬜ |
| Schema | ¿El schema está asignado? | ✅ / ⬜ |
| Enlaces internos | ¿Los enlaces obligatorios están listados? | ✅ / ⬜ |
| Priority | ¿La prioridad está definida? | ✅ / ⬜ |
| Status | ¿El estado de producción está claro? | ✅ / ⬜ |

# Bloque V — Outputs consolidados

## §23 Outputs consolidados del Paso 3

- URL Matrix creada
- Filas base generadas
- Local Coverage Areas documentadas como contenido
- IDs asignados
- Parent pages definidos
- Schema inicial asignado
- Internal links requeridos añadidos
- Prioridades y fases preparadas

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

---
