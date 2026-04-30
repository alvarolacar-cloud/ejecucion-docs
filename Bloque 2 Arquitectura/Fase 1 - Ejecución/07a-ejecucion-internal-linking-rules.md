Versión literal del chat · Sistema GMB Crush para webs locales
Documento regenerado siguiendo la estructura fija acordada en la conversación.
Proveniencia: sistema construido paso a paso en el chat y alineado con los frameworks oficiales GMB Crush.

# §1 Paso 7 — Internal Linking Rules

# Bloque I — Introducción

## §2 Objetivo del Paso 7

Este paso existe para resolver un problema concreto dentro del sistema GMB Crush: definir cómo se conectan las páginas para crear un silo local claro, sin enlaces caóticos ni páginas huérfanas.
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
Error que previene: crear páginas sin enlaces hacia sus padres.
Error que previene: enlazar a Local Coverage Areas sin URL aprobada.
Error que previene: usar solo enlaces de footer.
Error que previene: no variar anchor text.
Error que previene: dejar GeoArticles sin enlace a la landing comercial.

## §3 Lo que la IA tiene que rellenar/obtener

```text
Business Name:

Website Root Domain:

Homepage URL:

Planned Primary GBP Category:

Primary Category Slug:

Main City:

Main City GeoHub URL:

Service Overview Pages:
1.
2.
3.
4.
5.

Main City Location-Based Service Pages:
1.
2.
3.
4.
5.

Páginas de categoría adicional en la Main City:
1.
2.
3.

Main City GeoArticle Pages:
1.
2.
3.
4.
5.

Local Coverage Areas:
1.
2.
3.
4.
5.

Do Local Coverage Areas have URLs?
Default: No

Approved Expansion Areas with URLs:
1.
2.
3.

Página de contacto URL:

GBP URL:

Top Priority Services:
1.
2.
3.

Preferred CTA Anchor:

Preferred Informational Anchor:

Preferred Local Anchor:
```

## §4 Ejemplo rellenado

```text
Business Name:
Cerrajeros Madrid 24h

Website Root Domain:
https://www.cerrajerosmadrid24h.com

Homepage URL:
/

Planned Primary GBP Category:
Cerrajero

Primary Category Slug:
cerrajero

Main City:
Madrid

Main City GeoHub URL:
/madrid/

Service Overview Pages:
1. /cerrajero/cerrajero-urgente/
2. /cerrajero/apertura-puertas/
3. /cerrajero/cambio-cerraduras/
4. /cerrajero/cambio-bombines/
5. /cerrajero/instalacion-cerraduras-seguridad/

Main City Location-Based Service Pages:
1. /cerrajero/madrid/cerrajero-urgente/
2. /cerrajero/madrid/apertura-puertas/
3. /cerrajero/madrid/cambio-cerraduras/
4. /cerrajero/madrid/cambio-bombines/
5. /cerrajero/madrid/instalacion-cerraduras-seguridad/

Páginas de categoría adicional en la Main City:
1. /cerrajero/madrid/duplicado-llaves/

Main City GeoArticle Pages:
1. /madrid/cuanto-cuesta-un-cerrajero-urgente/
2. /madrid/que-hacer-si-no-puedes-entrar-casa/
3. /madrid/cuanto-tarda-un-cerrajero/

Local Coverage Areas:
1. Almagro
2. Chamberí
3. Salamanca
4. Retiro

Do Local Coverage Areas have URLs?
No, not in the base build.

Approved Expansion Areas with URLs:
None in Phase 1.

Página de contacto URL:
/contacto/

GBP URL:
N/A — GBP not created yet

Top Priority Services:
1. Cerrajero urgente
2. Apertura de puertas
3. Cambio de bombines

Preferred CTA Anchor:
Llama a Cerrajeros Madrid 24h hoy

Preferred Informational Anchor:
Conoce más sobre servicios de cerrajería urgente

Preferred Local Anchor:
servicios de cerrajería en Madrid
```

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

# Bloque V — Outputs

## §21 Outputs del Paso 7

- Mapa de enlaces internos por tipo de página
- Anchors sugeridos
- Enlaces obligatorios
- Breadcrumbs
- Reglas para Local Coverage Areas sin URL
- Reglas de expansión si existe
- Checklist anti-páginas huérfanas

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
