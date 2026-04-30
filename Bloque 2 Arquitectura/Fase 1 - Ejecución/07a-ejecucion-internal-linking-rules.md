Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo la estructura fija acordada en la conversación.
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# §1 Paso 7 — Internal Linking Rules

# Bloque I — Introducción

## §2 Objetivo del Paso 7

Definir **cómo se conectan internamente las páginas del cluster** mediante reglas de enlace, anchors variados y breadcrumbs jerárquicos. Establece qué páginas enlazan a qué, qué anchors usar, dónde colocar los enlaces (contextual vs nav/footer) y qué Local Coverage Areas reciben enlace (solo si tienen URL aprobada). El silo local resultante debe ser navegable por usuario y crawler sin páginas huérfanas ni enlaces a URLs inexistentes.

**Outputs del Paso 7:**

- §5 Regla 1 — Enlazar arriba/abajo/lateral: cada página tiene up + down + lateral links dentro del silo
- §6 Regla 2 — Homepage distribuye autoridad: enlaza a 5 SO + GeoHub Main City + contacto + AC principal
- §7 Regla 3 — Service Overview empuja la versión local: cada SO enlaza a su LBS Main City correspondiente
- §8 Regla 4 — GeoHub organiza la Main City: enlaza a todas las páginas locales (LBS, AC, GAs)
- §9 Regla 5 — LBS conecta servicio y ciudad: enlaza a SO padre, GeoHub, related LBS, GeoArticles
- §10 Regla 6 — Additional Category se integra en el silo local: enlaza a GeoHub + LBS relacionados
- §11 Regla 7 — GeoArticle pasa relevancia a la landing: enlaza a matching LBS + GeoHub
- §12 Regla 8 — LCAs sin URL no reciben enlaces: solo menciones de contenido, nunca anchors a URLs inexistentes
- §13 Regla 9 — Anchor text variado: exact match + partial + branded + CTA + informational + local entity
- §14 Regla 10 — Enlaces contextuales primero: body > nav/footer; placement en intro, FAQs, related resources
- §15 Matriz de enlaces obligatorios por page type — 14 conexiones source → target documentadas
- §16 Ejemplo completo de enlaces — set completo de inbound/outbound + anchors para una LBS modelo
- §17 Breadcrumbs recomendados — jerarquía por page type (Home > Cat > City > Service)
- §18 Inbound links esperados (cross-cutting) — cada page type tiene mapa de inbound mínimo
- §19 Expansion linking separado (cross-cutting) — AEAs crean sub-cluster propio sin contaminar la base

**Errores que previene el Paso 7:**

- Páginas sin enlaces a su padre (huérfanas en el silo)
- Enlaces a Local Coverage Areas sin URL aprobada (anchors rotos a `/almagro/` inexistente)
- Solo enlaces de footer sin contextuales en body (señal débil)
- Anchor text repetido / 100% exact match (apariencia mecánica, riesgo manual penalty)
- GeoArticles sin enlace a la landing comercial (artículo no cumple función booster)
- GeoHub sin enlaces a páginas locales (no organiza el silo Main City)
- Service Overview sin enlace a su LBS local (no transfiere autoridad temática)
- Expansion linking mezclado con la base (sub-cluster contamina el silo principal)
- Breadcrumbs que inventan niveles de cobertura inexistentes

**Cuándo se ejecuta:**

Después del Paso 6 (Estructura de Contenido). El Paso 6 define qué se escribe en cada page type; el Paso 7 define cómo esas páginas se conectan entre sí. El output del Paso 7 alimenta directamente el Paso 8 (Schema Markup) — `WebPage.breadcrumb`, `Article.mentions`, `Service.areaServed` — y el Paso 18 (QA + deploy) usa la matriz de inbound links como referencia de validación.

## §3 Info heredada de pasos anteriores

El Paso 7 toma como input estos elementos generados en pasos previos. La IA no los re-decide aquí; los usa para construir la matriz de enlaces internos del cluster.

| # | Input heredado | Origen | Uso en el Paso 7 |
|---|---|---|---|
| 1 | Business Name | Paso 1 §2 | Anchors de marca (branded anchors) |
| 2 | Website Root Domain + Canonical Domain | Paso 1 §6 + Paso 4 §5 | Confirmar dominio único en todos los enlaces internos absolutos |
| 3 | Homepage URL (`/`) | Paso 4 §7 | Source de enlaces a SO + GeoHub + contacto |
| 4 | Primary Category Slug | Paso 3 §3 | Segmento `[primary-cat-slug]` en URLs de los enlaces |
| 5 | Main City + slug | Paso 1 §11 + Paso 3 §3 | Anchors locales y target geográfico del silo |
| 6 | URL Matrix (28 URLs base) | Paso 3 §3 | Conjunto cerrado de URLs disponibles para enlazar |
| 7 | Service Overview Pages (S=5) | Paso 4 §8 + Paso 3 §3 | Source y target de enlaces SO ↔ LBS |
| 8 | Location-Based Service Pages (S=5) | Paso 4 §10 + Paso 3 §3 | Hub principal de enlaces salientes (SO padre, GeoHub, related LBS, GAs) |
| 9 | Additional Category Pages (A=1 efectiva) | Paso 4 §11 + Paso 3 §3 | Source/target dentro del silo local |
| 10 | Main City GeoHub (`/madrid/`) | Paso 4 §9 + Paso 3 §3 | Hub central que enlaza a todas las páginas locales |
| 11 | GeoArticle Pages (G×S=15) | Paso 4 §12 + Paso 3 §3 | Boosters semánticos que enlazan a matching LBS |
| 12 | Local Coverage Areas (Direct + Candidate) | Paso 1 §14 | Mencionadas en contenido SIN enlace (no tienen URL) |
| 13 | Approved Expansion Areas (E count) | Paso 1 §15 | Si E≥1 → sub-cluster de linking separado (§19); E=0 → no aplica |
| 14 | Page Type assignment por URL | Paso 5 §3 | Determina qué reglas de enlace (§5–§14) aplican a cada URL |
| 15 | Page-level anchors (CTA, informational, local) | Paso 5 §11 + Paso 6 cross-cutting | Inputs para el catálogo de anchors variados (§13) |
| 16 | Página de contacto URL (`/contacto/`) | Paso 1 §6 (NAP) + Paso 3 §3 (auxiliar) | Target de CTA desde homepage y todas las LBS |

## §4 Ejemplo rellenado — Outputs del Paso 7 para Cerrajeros Madrid 24h

Esta sección consolida los outputs del Paso 7 en tablas operativas. Cada output corresponde a una sección §X del Bloque II/III y se valida individualmente.

### §4.1 Reglas de enlace por page type (§5–§12)

| # | Regla | §X | Aplicación (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|---|
| 1 | Enlazar arriba/abajo/lateral | §5 | Todas las 28 URLs del cluster tienen al menos 1 enlace up + 1 down/lateral | confirmed |
| 2 | Homepage distribuye autoridad | §6 | `/` enlaza a 5 SO + `/madrid/` + `/contacto/` + `/cerrajero/madrid/duplicado-llaves/` (8 outbound mínimos) | confirmed |
| 3 | SO empuja la versión local | §7 | Cada `/cerrajero/{service}/` enlaza a su `/cerrajero/madrid/{service}/` correspondiente (5 conexiones SO → LBS) | confirmed |
| 4 | GeoHub organiza la Main City | §8 | `/madrid/` enlaza a 5 LBS + 1 AC + 15 GA (21 outbound) | confirmed |
| 5 | LBS conecta servicio y ciudad | §9 | Cada LBS enlaza a SO padre + `/madrid/` + 2-3 related LBS + 3 matching GAs | confirmed |
| 6 | AC se integra en silo local | §10 | `/cerrajero/madrid/duplicado-llaves/` enlaza a `/madrid/` + LBS relacionados (cambio-cerraduras, instalación-seguridad) | confirmed |
| 7 | GeoArticle pasa relevancia a landing | §11 | Cada GA enlaza a su matching LBS + `/madrid/` (15 conexiones GA → LBS) | confirmed |
| 8 | LCAs sin URL no reciben enlaces | §12 | Almagro, Chamberí, Salamanca, Retiro mencionadas en contenido; 0 anchors `<a href="/almagro/">` | confirmed |

### §4.2 Reglas de anchor text y placement (§13–§14)

| # | Regla | §X | Catálogo aplicado (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|---|
| 1 | Anchor text variado | §13 | 6 categorías de anchor: exact match (`cerrajero urgente en Madrid`), partial (`servicios de cerrajería`), branded (`Cerrajeros Madrid 24h`), CTA (`Llama hoy`), informational (`Conoce más sobre cerrajero urgente`), local entity (`zonas de cobertura en Madrid`) | confirmed |
| 2 | Enlaces contextuales primero | §14 | Body links > nav/footer; placement principal en intro, FAQs y related resources sections | confirmed |

### §4.3 Matriz de enlaces obligatorios (§15)

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

### §4.4 Outputs auxiliares (§16–§17)

| # | Output | §X | Contenido (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|---|
| 1 | Ejemplo completo de enlaces para LBS modelo | §16 | Source `/cerrajero/madrid/cerrajero-urgente/` con 6 outbound + 6 anchor suggestions | confirmed |
| 2 | Breadcrumbs por page type | §17 | Homepage: Home / SO: Home > Cerrajero > Cerrajero urgente / GeoHub: Home > Madrid / LBS: Home > Cerrajero > Madrid > Cerrajero urgente / AC: Home > Cerrajero > Madrid > Duplicado de llaves / GA: Home > Madrid > {topic} | confirmed |

### §4.5 Reglas cross-cutting (§18–§19)

| # | Regla cross-cutting | §X | Aplicación (Cerrajeros Madrid 24h) | Status |
|---|---|---|---|---|
| 1 | Inbound links esperados | §18 | Cada URL del cluster con mapa de inbound: LBS recibe enlaces de homepage, SO padre, GeoHub, GAs (4 inbound mínimos); 0 páginas huérfanas | confirmed |
| 2 | Expansion linking separado | §19 | E=0 en Phase 1 → no aplica sub-cluster de expansión | confirmed |

### §4.6 Validaciones cruzadas con otros pasos

| Validación | Origen | Comprobación en Paso 7 | Status |
|---|---|---|---|
| Todos los target URLs existen en URL Matrix | Paso 3 §3 | 28 URLs aprobadas; 0 enlaces a URLs fuera de la matriz | OK |
| Patrones de URL respetados en cada anchor | Paso 4 §5–§19 | Todos los enlaces internos usan canonical domain + trailing slash uniforme | OK |
| 0 enlaces a Local Coverage Areas sin URL | Paso 1 §14 + Paso 4 §13 | Almagro, Chamberí, Salamanca, Retiro mencionadas en texto, 0 anchors hacia ellas | OK |
| Página de contacto auxiliar enlazada desde homepage y LBS | Paso 3 §3 (URL aux) | `/contacto/` recibe enlaces desde `/` y desde las 5 LBS | OK |
| Brand tone respetado en anchors CTA | Paso 5 §6 | Anchors CTA siguen brand tone declarado en Paso 5 | OK |

# Bloque II — Ejecución por la IA

## §5 Regla 1 — Enlazar hacia arriba, abajo y lateralmente

### §5.1 Explicación

**Explicación**

Cada página debe tener un enlace hacia su padre, hacia páginas hijas o de soporte, y hacia páginas relacionadas del mismo silo.

**Patrón o fórmula**

```text
up + down + lateral links
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS /cerrajero/madrid/cerrajero-urgente/ enlaza a /cerrajero/cerrajero-urgente/, /madrid/, servicios relacionados y artículos
```

**Ejemplos incorrectos**

```text
- Página local sin link al servicio padre
- GeoArticle sin link a landing
- GeoHub sin links a servicios
```

**Regla final**

```text
Todo enlace interno conecta vertical (arriba/abajo) o lateralmente, nunca aleatorio.
```

### §5.2 Cómo aplicamos la Regla 1 (Enlazar arriba/abajo/lateral)

**Fuente:** GMB Crush.

**Método:** Aplicar la regla generando los enlaces internos requeridos para cada page type según la matriz §15.

### §5.3 Output del paso

**Tipo:** Lista de enlaces internos requeridos por page type.

**Ejemplo (Cerrajeros Madrid 24h):** Generados según la matriz de enlaces obligatorios.

## §6 Regla 2 — Homepage distribuye autoridad

### §6.1 Explicación

**Explicación**

La homepage enlaza a servicios core, GeoHub de Main City, additional category principal y contacto.

**Patrón o fórmula**

```text
Homepage → Service Overview + Main City GeoHub + Contacto
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h enlaza desde / a /cerrajero/cerrajero-urgente/, /cerrajero/apertura-puertas/, /madrid/ y /contacto/.
```

**Ejemplos incorrectos**

```text
- Homepage enlaza a 100 zonas
- Homepage no enlaza a servicios
- Homepage solo usa enlaces en footer
- Homepage enlaza a zonas sin página
- Homepage no enlaza al GeoHub
- Homepage solo enlaza al contacto
```

**Regla final**

```text
La Homepage debe enlazar a las 5 SO + GeoHub Main City como punto de partida del cluster.
```

**Validación operativa**

La homepage debe enlazar a las páginas más importantes de la arquitectura base: Service Overview Pages, Main City GeoHub, Additional Category principal y contacto. No debe enlazar a todas las áreas de cobertura si no tienen URL.

### §6.2 Cómo aplicamos la Regla 2 (Homepage distribuye autoridad)

**Fuente:** GMB Crush.

**Método:** Aplicar la regla generando los enlaces internos requeridos para cada page type según la matriz §15.

### §6.3 Output del paso

**Tipo:** Lista de enlaces internos requeridos por page type.

**Ejemplo (Cerrajeros Madrid 24h):** Generados según la matriz de enlaces obligatorios.

## §7 Regla 3 — Service Overview empuja la versión local

### §7.1 Explicación

**Explicación**

Cada Service Overview debe enlazar a la versión Main City del servicio.

**Patrón o fórmula**

```text
/category/service/ → /category/main-city/service/
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
La página /cerrajero/cerrajero-urgente/ enlaza a /cerrajero/madrid/cerrajero-urgente/ con anchor cerrajero urgente en Madrid.
```

**Ejemplos incorrectos**

```text
- Service Overview sin versión local
- Enlazar a Almagro sin expansión
- Enlazar solo a blog
- No enlazar a la versión local
- Enlazar a páginas de cobertura inexistentes
- Usar solo anchors genéricos como haz clic aquí
```

**Regla final**

```text
Cada Service Overview enlaza a su versión local correspondiente como puente al funnel.
```

**Validación operativa**

Cada Service Overview debe enlazar a la Location-Based Service Page de la Main City para transferir autoridad temática a la página comercial local.

### §7.2 Cómo aplicamos la Regla 3 (SO empuja la versión local)

**Fuente:** GMB Crush.

**Método:** Aplicar la regla generando los enlaces internos requeridos para cada page type según la matriz §15.

### §7.3 Output del paso

**Tipo:** Lista de enlaces internos requeridos por page type.

**Ejemplo (Cerrajeros Madrid 24h):** Generados según la matriz de enlaces obligatorios.

## §8 Regla 4 — GeoHub organiza la Main City

### §8.1 Explicación

**Explicación**

El GeoHub debe enlazar a todas las páginas de servicio, categoría adicional y artículos de la Main City.

**Patrón o fórmula**

```text
/main-city/ → all Main City service pages + articles
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/madrid/ enlaza a /cerrajero/madrid/cerrajero-urgente/, /cerrajero/madrid/apertura-puertas/ y /madrid/cuanto-cuesta-un-cerrajero-urgente/.
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

El GeoHub debe ser el índice de la Main City. Debe enlazar a todas las páginas servicio+ciudad, categorías adicionales y GeoArticles de esa ciudad.

### §8.2 Cómo aplicamos la Regla 4 (GeoHub organiza Main City)

**Fuente:** GMB Crush.

**Método:** Aplicar la regla generando los enlaces internos requeridos para cada page type según la matriz §15.

### §8.3 Output del paso

**Tipo:** Lista de enlaces internos requeridos por page type.

**Ejemplo (Cerrajeros Madrid 24h):** Generados según la matriz de enlaces obligatorios.

## §9 Regla 5 — Location-Based Service conecta servicio y ciudad

### §9.1 Explicación

**Explicación**

La landing local conecta el servicio padre, el GeoHub, servicios relacionados y artículos.

**Patrón o fórmula**

```text
LBS → parent service + GeoHub + same-city services + articles
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/cerrajero/madrid/cerrajero-urgente/ enlaza a /cerrajero/madrid/apertura-puertas/ y /cerrajero/madrid/instalacion-cerraduras-seguridad/.
```

**Ejemplos incorrectos**

```text
- Landing sin GeoHub
- Landing sin artículos
- Landing con enlaces a áreas inexistentes
- No enlazar al padre
- No enlazar al GeoHub
- Enlazar solo a contacto
- Enlazar a servicios no relacionados
- Enlazar a todas las páginas sin criterio
- No usar anchors semánticos
```

**Regla final**

```text
LBS enlaza hacia arriba a su SO + GeoHub, lateralmente a otros LBS y AC del cluster.
```

**Validación operativa**

Una página local debe enlazar a su Service Overview padre y al GeoHub. Esto conecta tópico y geografía, evitando que la landing quede aislada.

Las páginas locales deben enlazar a servicios relacionados en la misma Main City para crear cluster comercial. Estos enlaces ayudan al usuario y refuerzan co-ocurrencias de servicio local.

### §9.2 Cómo aplicamos la Regla 5 (LBS conecta servicio y ciudad)

**Fuente:** GMB Crush.

**Método:** Aplicar la regla generando los enlaces internos requeridos para cada page type según la matriz §15.

### §9.3 Output del paso

**Tipo:** Lista de enlaces internos requeridos por page type.

**Ejemplo (Cerrajeros Madrid 24h):** Generados según la matriz de enlaces obligatorios.

## §10 Regla 6 — Additional Category se integra en el silo local

### §10.1 Explicación

**Explicación**

La categoría adicional debe enlazar al GeoHub, servicios relacionados y contenido útil.

**Patrón o fórmula**

```text
Additional Category → GeoHub + related local services
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/cerrajero/madrid/duplicado-llaves/ enlaza a /madrid/, /cerrajero/madrid/cambio-cerraduras/ y /cerrajero/madrid/instalacion-cerraduras-seguridad/.
```

**Ejemplos incorrectos**

```text
- Categoría adicional huérfana
- Sin conexión a GeoHub
- Duplicada con servicio core
- Página adicional sin enlaces internos
- Enlazar solo a homepage
- No conectarla con servicios relacionados
```

**Regla final**

```text
Additional Category enlaza al silo local: GeoHub, LBS, otras AC.
```

**Validación operativa**

La página de categoría adicional debe enlazar al GeoHub y a servicios relacionados para no quedar como página secundaria aislada.

### §10.2 Cómo aplicamos la Regla 6 (AC se integra en silo local)

**Fuente:** GMB Crush.

**Método:** Aplicar la regla generando los enlaces internos requeridos para cada page type según la matriz §15.

### §10.3 Output del paso

**Tipo:** Lista de enlaces internos requeridos por page type.

**Ejemplo (Cerrajeros Madrid 24h):** Generados según la matriz de enlaces obligatorios.

## §11 Regla 7 — GeoArticle pasa relevancia a la landing

### §11.1 Explicación

**Explicación**

Cada GeoArticle debe enlazar a su landing comercial y al GeoHub.

**Patrón o fórmula**

```text
GeoArticle → matching LBS + GeoHub + related article
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/madrid/cuanto-cuesta-un-cerrajero-urgente/ enlaza a /cerrajero/madrid/cerrajero-urgente/ y /madrid/.
```

**Ejemplos incorrectos**

```text
- Artículo sin CTA interno
- Artículo sin enlace comercial
- Artículo enlazando a área sin URL
- Artículo sin enlace a landing
- Artículo enlaza solo a homepage
- Artículo apunta a una URL inexistente
```

**Regla final**

```text
Cada GeoArticle enlaza prominentemente a su landing comercial principal.
```

**Validación operativa**

Cada GeoArticle debe enlazar a la página comercial servicio+Main City que quiere reforzar. Sin ese enlace, el artículo no cumple su función de booster.

### §11.2 Cómo aplicamos la Regla 7 (GeoArticle pasa relevancia a landing)

**Fuente:** GMB Crush.

**Método:** Aplicar la regla generando los enlaces internos requeridos para cada page type según la matriz §15.

### §11.3 Output del paso

**Tipo:** Lista de enlaces internos requeridos por page type.

**Ejemplo (Cerrajeros Madrid 24h):** Generados según la matriz de enlaces obligatorios.

## §12 Regla 8 — Local Coverage Areas no reciben enlaces si no tienen URLs

### §12.1 Explicación

**Explicación**

Las áreas de cobertura se mencionan en texto, pero no se enlazan si no existe página aprobada.

**Patrón o fórmula**

```text
Local Coverage Area sin URL → mención textual | no link
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h menciona Almagro en contenido, pero no crea anchor a /almagro/ hasta que esa URL sea aprobada.
```

**Ejemplos incorrectos**

```text
- Anchor a /almagro/ inexistente
- Breadcrumb con Salamanca
- Footer con enlaces a áreas sin página
- Crear anchors rotos hacia /almagro/
- Simular páginas de cobertura con hashtags
- Enlazar a búsquedas externas en vez de URLs propias
```

**Regla final**

```text
Si una LCA no tiene URL aprobada, NO recibe enlaces internos — solo menciones de contenido.
```

**Validación operativa**

Si una Local Coverage Area no es Approved Expansion Area, no debe recibir enlaces internos. Puede mencionarse en texto, pero no como anchor hacia una página inexistente.

### §12.2 Cómo aplicamos la Regla 8 (LCAs no reciben enlaces sin URL)

**Fuente:** GMB Crush.

**Método:** Aplicar la regla generando los enlaces internos requeridos para cada page type según la matriz §15.

### §12.3 Output del paso

**Tipo:** Lista de enlaces internos requeridos por page type.

**Ejemplo (Cerrajeros Madrid 24h):** Generados según la matriz de enlaces obligatorios.

## §13 Regla 9 — Anchor text variado

### §13.1 Explicación

**Explicación**

Los anchors deben variar entre exact match, partial, branded, CTA, local entity e informacional.

**Patrón o fórmula**

```text
Exact match + partial match + branded + CTA + informational
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Usar cerrajero urgente en Madrid, ayuda urgente de apertura de puertas en Madrid, Cerrajeros Madrid 24h y consulta precios de cerrajero urgente.
```

**Ejemplos incorrectos**

```text
- Mismo anchor 20 veces
- Solo exact match
- Anchors genéricos como haz clic aquí
- Repetir urgente cerrajero Madrid en todos los enlaces
- Usar solo haz clic aquí
- Usar anchors irrelevantes
```

**Regla final**

```text
Anchor text variado y descriptivo; nunca repetir el mismo anchor en múltiples enlaces.
```

**Validación operativa**

Los anchors deben ser naturales y variados. Usar siempre el exact match puede parecer mecánico y reduce calidad editorial.

### §13.2 Cómo aplicamos la Regla 9 (Anchor text variado)

**Fuente:** GMB Crush.

**Método:** Aplicar la regla generando los enlaces internos requeridos para cada page type según la matriz §15.

### §13.3 Output del paso

**Tipo:** Lista de enlaces internos requeridos por page type.

**Ejemplo (Cerrajeros Madrid 24h):** Generados según la matriz de enlaces obligatorios.

## §14 Regla 10 — Enlaces contextuales primero

### §14.1 Explicación

**Explicación**

Los enlaces en cuerpo tienen más sentido que repetirlo todo en footer.

**Patrón o fórmula**

```text
Intro/body/service blocks/FAQs/related resources/CTA
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Enlace a /madrid/ dentro de la intro local
```

**Ejemplos incorrectos**

```text
- Solo footer
- Solo menú
- Bloques de enlaces sin contexto
```

**Regla final**

```text
Enlaces dentro del cuerpo (contextuales) primero; enlaces de navegación / footer después.
```

### §14.2 Cómo aplicamos la Regla 10 (Enlaces contextuales primero)

**Fuente:** GMB Crush.

**Método:** Aplicar la regla generando los enlaces internos requeridos para cada page type según la matriz §15.

### §14.3 Output del paso

**Tipo:** Lista de enlaces internos requeridos por page type.

**Ejemplo (Cerrajeros Madrid 24h):** Generados según la matriz de enlaces obligatorios.

## §15 Matriz de enlaces obligatorios por tipo de página

| Source Page | Debe enlazar a | Objetivo |
|---|---|---|
| Homepage | Service Overview Pages | Reforzar servicios principales |
| Homepage | Main City GeoHub | Reforzar ciudad principal |
| Homepage | Página de contacto | Conversión y NAP |
| Service Overview | Main City Service Page | Empujar landing local |
| Service Overview | Related Services | Autoridad temática |
| Main City GeoHub | All Páginas de servicio en la Main City | Organizar silo local |
| Main City GeoHub | Additional Category Pages | Soporte GBP |
| Main City GeoHub | GeoArticles | Recursos locales |
| Location-Based Service | Parent Service Overview | Relación temática |
| Location-Based Service | Main City GeoHub | Relación geográfica |
| Location-Based Service | Related same-city services | Cluster local |
| Location-Based Service | GeoArticles | Profundidad semántica |
| GeoArticle | Matching Location-Based Service Page | Pasar autoridad |
| GeoArticle | Main City GeoHub | Reforzar ciudad |

## §16 Ejemplo completo de enlaces

```text
Source:
/cerrajero/madrid/cerrajero-urgente/

Required links:
- /cerrajero/cerrajero-urgente/
- /madrid/
- /cerrajero/madrid/apertura-puertas/
- /cerrajero/madrid/cambio-cerraduras/
- /madrid/cuanto-cuesta-un-cerrajero-urgente/
- /contacto/

Anchor suggestions:
- urgente servicios de cerrajería
- servicios de cerrajería en Madrid
- apertura de puertas en Madrid
- servicios de cambio de cerraduras en Madrid
- precio de cerrajero urgente en Madrid
- llama hoy a Cerrajeros Madrid 24h
```

## §17 Breadcrumbs recomendados

```text
Homepage:
Home

Service Overview:
Home > Cerrajero > Cerrajero urgente

Main City GeoHub:
Home > Madrid

Location-Based Service:
Home > Cerrajero > Madrid > Cerrajero urgente

Additional Category:
Home > Cerrajero > Madrid > Duplicado de llaves

GeoArticle:
Home > Madrid > Cerrajero urgente Cost Guide
```

### §17.1 Validación operativa

Los breadcrumbs ayudan a usuarios y motores a entender jerarquía. Deben reflejar el page type y no inventar niveles de cobertura inexistentes.

# Bloque III — Reglas Cross-Cutting

> Reglas que aplican a TODO el internal linking del cluster como filtro de QA. Patrón 3-subsections.

## §18 Inbound links esperados

### §18.1 Explicación

**Explicación**

La matriz debe prever desde qué páginas recibirá enlaces cada URL importante. Esto evita páginas huérfanas y permite QA de silo.

**Patrón o fórmula**

```text
Target URL → inbound sources mínimas
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/cerrajero/madrid/cerrajero-urgente/ recibe enlaces desde homepage, Service Overview, GeoHub y GeoArticles.
```

**Ejemplos incorrectos**

```text
- Crear páginas sin inbound links
- Depender solo del menú principal
- No revisar enlaces entrantes en QA
```

**Regla final**

```text
Cada page type tiene un mapa de inbound links esperado documentado en la matriz.
```

### §18.2 Cómo aplicamos la regla "Inbound links esperados"

**Fuente:** GMB Crush.

**Método:** Aplicar como filtro de QA al validar el internal linking del cluster antes de Paso 18 deploy.

### §18.3 Output del paso

**Tipo:** Validation flag.

**Ejemplo (Cerrajeros Madrid 24h):** Validado.

## §19 Expansion linking separado

### §19.1 Explicación

**Explicación**

Cuando una Approved Expansion Area genera URLs, se añade una capa de linking propia. No debe contaminar la base hasta que exista el cluster.

**Patrón o fórmula**

```text
Approved Expansion GeoHub → expansion service pages → related articles
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Si Almagro se aprueba, /almagro/ enlaza a /cerrajero/almagro/cerrajero-urgente/ y esa página vuelve a /cerrajero/cerrajero-urgente/.
```

**Ejemplos incorrectos**

```text
- Enlazar expansión antes de publicar páginas
- Mezclar expansión con cobertura textual
- No enlazar la expansión al servicio padre
```

**Regla final**

```text
Approved Expansion Areas crean su propio sub-cluster de linking, separado del base.
```

### §19.2 Cómo aplicamos la regla "Expansion linking separado"

**Fuente:** GMB Crush.

**Método:** Aplicar como filtro de QA al validar el internal linking del cluster antes de Paso 18 deploy.

### §19.3 Output del paso

**Tipo:** Validation flag.

**Ejemplo (Cerrajeros Madrid 24h):** Validado.

# Bloque IV — Checklist Final

## §20 Checklist final del Paso 7

| Check | Pregunta | Estado |
|---|---|---|
| Homepage links | ¿La homepage enlaza a servicios, GeoHub y contacto? | ✅ / ⬜ |
| Service Overview links | ¿Cada servicio enlaza a su landing de Main City? | ✅ / ⬜ |
| GeoHub links | ¿El GeoHub enlaza a todas las páginas de Main City? | ✅ / ⬜ |
| LBS links | ¿Cada landing enlaza a servicio padre, GeoHub y artículos? | ✅ / ⬜ |
| GeoArticle links | ¿Cada artículo enlaza a landing y GeoHub? | ✅ / ⬜ |
| Local Coverage links | ¿No se enlaza a áreas sin URL aprobada? | ✅ / ⬜ |
| Anchors | ¿Hay variación natural de anchor text? | ✅ / ⬜ |
| Placement | ¿Los enlaces están en contenido contextual? | ✅ / ⬜ |
| Breadcrumbs | ¿La ruta de navegación es lógica? | ✅ / ⬜ |

# Bloque V — Outputs consolidados

## §21 Outputs del Paso 7

| # | Output | §X | Tipo |
|---|---|---|---|
| 1 | Regla 1 — Enlazar arriba/abajo/lateral | §5 | Regla operativa por page type |
| 2 | Regla 2 — Homepage distribuye autoridad | §6 | Regla operativa |
| 3 | Regla 3 — Service Overview empuja la versión local | §7 | Regla operativa |
| 4 | Regla 4 — GeoHub organiza la Main City | §8 | Regla operativa |
| 5 | Regla 5 — LBS conecta servicio y ciudad | §9 | Regla operativa |
| 6 | Regla 6 — Additional Category se integra en silo local | §10 | Regla operativa |
| 7 | Regla 7 — GeoArticle pasa relevancia a la landing | §11 | Regla operativa |
| 8 | Regla 8 — LCAs sin URL no reciben enlaces | §12 | Regla operativa |
| 9 | Regla 9 — Anchor text variado | §13 | Catálogo de 6 categorías de anchor |
| 10 | Regla 10 — Enlaces contextuales primero | §14 | Regla de placement |
| 11 | Matriz de enlaces obligatorios por page type | §15 | Tabla 14 conexiones source → target |
| 12 | Ejemplo completo de enlaces | §16 | Set inbound/outbound + anchors |
| 13 | Breadcrumbs por page type | §17 | Jerarquía 6 page types |
| 14 | Inbound links esperados (cross-cutting) | §18 | Validation flag |
| 15 | Expansion linking separado (cross-cutting) | §19 | Regla operativa para E≥1 |

---

# Bloque VI — Fuentes Internas GMB Crush Usadas

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
