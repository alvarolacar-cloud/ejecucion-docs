Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 3 — Priorizacion/paso-09-qa-checklist/`, alineado con los frameworks oficiales GMB Crush.

# Paso 9 — QA Checklist

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 8 outputs del Paso 9 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, obtención de outputs, checklist final y outputs consolidados.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 9

<small>§2</small>

En este paso la IA produce todos los outputs que **validan cada página antes de publicación** — la plantilla operativa de QA, las **5 categorías de QA agrupadas** (Estructural / Local / Contenido / Conexión / Semántico) que cubren las 13 reglas operativas (URL, Page Type, One Service, One City, Local Coverage, No Fake Location, areaServed coherente, Metadata, Word Count, Schema, Internal Links, Breadcrumbs, CTA + Canibalización), el Final Publish Gate de 9 checkpoints binarios y el GBP Not Created QA Checklist específico para clusters web-first. El Paso 9 es el control de calidad que **bloquea la publicación** si falla cualquier check.

**Outputs del paso:**

- **9.1** Plantilla de QA por página — formulario operativo (Page ID, Type, URL, Target Service, Main City, GBP Category, LCAs, Priority, Status, QA Date)
- **9.2** QA Estructural — agrupa URL QA + Page Type QA + One Service Only + One Main City Only (4 sub-checks)
- **9.3** QA Local — agrupa Local Coverage QA + No Fake Location + Schema `areaServed` coherente (3 sub-checks)
- **9.4** QA Contenido — agrupa Metadata QA + Word Count QA + Schema QA (3 sub-checks)
- **9.5** QA Conexión — agrupa Internal Links QA + Breadcrumbs QA + CTA QA (3 sub-checks)
- **9.6** QA Semántico — Canibalización QA (1 sub-check)
- **9.7** Final Publish Gate — 9 checkpoints binarios antes de publicar
- **9.8** GBP Not Created QA Checklist — 7 checks específicos para web-first

**Errores que previene:**

- Publicar URLs que violan el patrón doctrinal del Paso-04
- Crear LBS con múltiples servicios o ciudades como targets
- Mencionar oficinas en LCAs sin sede real
- Publicar landings con thin content (<400 palabras)
- Schema con dirección falsa o NAP inconsistente
- Páginas sin enlaces internos, breadcrumbs incoherentes o sin CTA
- Canibalización por dos URLs cubriendo la misma intención
- Inventar señales de GBP (URL, sameAs, reseñas) antes del Paso 14

**Cuándo se ejecuta:** después de Pasos 1-8 cerrados (intake + fórmula + matriz + URL rules + page types + content arch + linking + priority). Antes de Paso 10 (Producción en Fases) y Paso 18 (deploy).

## Info heredada de pasos anteriores

<small>§3</small>

> Estos campos NO se deciden en Paso 9 — la IA los lee del paso indicado y los usa como input para validar las páginas del Bloque III.

| Campo | Origen |
|---|---|
| Business Name | Paso-01 1.1 |
| GBP Lifecycle Status | Paso-01 1.3 |
| Full NAP | Paso-01 1.4 |
| Planned Primary GBP Category | Paso-01 1.5 |
| Planned Additional GBP Categories | Paso-01 1.6 |
| Main City | Paso-01 1.7 |
| Physical Location City | Paso-01 1.8 |
| Servicios principales (S=5) | Paso-01 1.9 |
| Local Coverage Areas | Paso-01 1.10 |
| Preferred CTA | Paso-01 1.13 |
| URL patterns por page type | Paso-04 4.3 a 4.8 |
| Validación No falsa ubicación | Paso-04 4.14 |
| Validación No duplicar intención | Paso-04 4.15 |
| Spec por page type (9 sub-outputs) | Paso-05 5.3 a 5.8 |
| Validación Schema | Paso-05 5.9 |
| Validación Word count | Paso-05 5.10 |
| Validación CTA | Paso-05 5.11 |
| Validación No false location claims | Paso-05 5.12 |
| Content Architecture por page type | Paso-06 6.6 a 6.11 |
| FAQs con cobertura natural | Paso-06 6.16 |
| Schema `areaServed` coherente | Paso-06 6.17 |
| Anchor text variado | Paso-07 7.9 |
| Matriz de enlaces obligatorios | Paso-07 7.11 |
| Breadcrumbs por page type | Paso-07 7.13 |
| Inbound links esperados | Paso-07 7.14 |
| Inventario priorizado completo | Paso-08 8.14 |

# Bloque II — Ejemplo rellenado para el Paso 9 — QA Checklist

<small>§4</small>

> Los 8 outputs del Paso 9 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 9.X declarado en §5. Los ejemplos usan LBS-1 (`/cerrajero/madrid/cerrajero-urgente/`) como página de referencia.

### 9.1 — Plantilla de QA por página

```text
Page ID:               LBS-1
Page Type:             Location-Based Service
URL:                   /cerrajero/madrid/cerrajero-urgente/
Target Service:        Cerrajero urgente
Main City:             Madrid
GBP Category:          Cerrajero (Primary)
Local Coverage Areas:  Almagro, Chamberí, Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad
Priority:              P1
Phase:                 1
Status:                Approved
QA Date:               2026-04-30
```

### 9.2 — QA Estructural (LBS-1)

```text
☑ URL QA              — `/cerrajero/madrid/cerrajero-urgente/` cumple patrón Paso-04 4.6
☑ Page Type QA        — H1 sigue spec Paso-05 5.5; estructura LBS con Local Pain Points + LCAs Section
☑ One Service Only    — H1 menciona solo `Cerrajero urgente`; sin mezcla
☑ One Main City Only  — H1 menciona solo Madrid; LCAs en sección dedicada
```

### 9.3 — QA Local (LBS-1)

```text
☑ Local Coverage QA          — 10 LCAs en H2 dedicado, sin keyword stuffing
☑ No Fake Location           — Schema address NAP real; 0 menciones a "oficina en [LCA]"
☑ Schema areaServed coherente — Lista 10 LCAs reales (cruza con Paso-06 6.17)
```

### 9.4 — QA Contenido (LBS-1)

```text
☑ Metadata QA   — H1 + Meta Title + Meta Description coherentes con la intención local
☑ Word Count    — 920 palabras (rango LBS doctrinal 800-1,000 ✓)
☑ Schema QA     — JSON-LD válido: LocalBusiness + BreadcrumbList + FAQPage + Speakable
```

### 9.5 — QA Conexión (LBS-1)

```text
☑ Internal Links QA  — 7 enlaces (parent SO + GH + 3 LBS lateral + 2 GAs); cumple matriz 7.11
☑ Breadcrumbs QA     — `Home > Cerrajero > Madrid > Cerrajero urgente` (cumple Paso-07 7.13)
☑ CTA QA             — "Llamar ahora · 24h" mencionando servicio + ciudad
```

### 9.6 — QA Semántico (LBS-1)

```text
☑ Canibalización QA  — Esta URL es la única que cubre intención `cerrajero urgente Madrid`.
                       La SO `/cerrajero/cerrajero-urgente/` no se solapa (no-geolocalizada).
```

### 9.7 — Final Publish Gate (LBS-1)

```text
□ URL approved:                 Yes
□ Content approved:             Yes
□ SEO metadata approved:        Yes
□ Schema approved:              Yes
□ Internal links approved:      Yes
□ NAP approved:                 Yes
□ No canibalization:            Yes
□ No false location claim:      Yes
□ CTA approved:                 Yes

→ Ready to publish:             Yes
```

### 9.8 — GBP Not Created QA Checklist (LBS-1)

```text
□ GBP Status:                            ✓ La página reconoce GBP=Not Created
□ Planned Category Support:              ✓ Soporta Planned Primary `Cerrajero` sin afirmar
□ Planned Additional Categories:         ✓ N/A — no hay AC en esta LBS
□ No Invented GBP URL:                   ✓ Sin URL GBP en schema/footer
□ No Invented Reviews:                   ✓ 0 reseñas Google afirmadas
□ sameAs Deferred:                       ✓ Campo sameAs vacío hasta Paso 14
□ Paso 14 Dependency:                    ✓ Marcada para actualización post-GBP
```

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 8 outputs que el Paso 9 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `9.5`) citable desde cualquier doc del sistema. Las **5 categorías de QA** (9.2–9.6) agrupan las 13 reglas operativas en checks ejecutables por categoría.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 9.1 | Plantilla de QA por página | Formulario operativo (10 campos) | GMB Crush | Paso-08 8.14 |
| 9.2 | QA Estructural | 4 sub-checks binarios por URL | GMB Crush | Paso-04 4.3-4.8 + Paso-05 5.3-5.8 + Paso-01 1.7 + 1.9 |
| 9.3 | QA Local | 3 sub-checks binarios por URL | GMB Crush | Paso-01 1.10 + Paso-01 1.8 + Paso-04 4.14 + Paso-06 6.17 |
| 9.4 | QA Contenido | 3 sub-checks binarios por URL | GMB Crush | Paso-05 5.9 + 5.10 + 5.3-5.8 |
| 9.5 | QA Conexión | 3 sub-checks binarios por URL | GMB Crush | Paso-07 7.11 + 7.13 + Paso-05 5.11 + Paso-01 1.13 |
| 9.6 | QA Semántico | 1 sub-check binario por URL | GMB Crush | Paso-04 4.15 |
| 9.7 | Final Publish Gate | 9 checkpoints binarios + Ready to publish | GMB Crush | Paso-09 9.2-9.6 (intra-paso) |
| 9.8 | GBP Not Created QA Checklist | 7 checks específicos web-first | GMB Crush | Paso-01 1.3 + Paso-14 (forward) |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 8 outputs (9.1–9.8). Cada output usa el patrón estándar adaptado al QA: Explicación / Sub-checks / Cómo se mide / Ejemplos correctos / Ejemplos incorrectos / Regla / Validación / Cómo se obtiene / Output del paso. Las **5 categorías de QA** (9.2–9.6) tienen sub-checks binarios listados explícitamente — cada uno mapea a una regla doctrinal.

### 9.1 — Plantilla de QA por página

<small>§6.1</small>

**Explicación**

Formulario operativo que se rellena POR PÁGINA antes de hacer QA. Captura la metadata mínima necesaria para validar las 5 categorías. Sin la plantilla, las reglas se aplican de memoria y las violaciones se escapan.

**Patrón o fórmula**

```text
Page ID · Page Type · URL · Target Service · Main City · GBP Category · LCAs · Priority · Phase · Status · QA Date
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 9.1.

**Ejemplos incorrectos**

```text
- Hacer QA sin plantilla rellenada (validaciones de memoria)
- Omitir LCAs (sin contexto, QA Local no se valida)
- Omitir QA Date (sin trazabilidad de cuándo se aprobó)
```

**Regla final**

```text
Toda página entra a QA con la plantilla rellenada al 100%.
```

**Validación operativa**

Aplicar a las N URLs del inventario priorizado (Paso-08 8.14). Validar que cada fila tiene los 10 campos rellenos.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Generar plantilla por URL cruzando con los outputs heredados (Paso-01 1.X, Paso-08 8.14) + campos de status QA.

**Output del paso**

- **Tipo:** Formulario operativo de 10 campos por página.
- **Ejemplo (Cerrajeros Madrid 24h):** Ver §4 sub-sección 9.1 — plantilla LBS-1 rellena.

### 9.2 — QA Estructural

<small>§6.2</small>

**Explicación**

Categoría que valida que la **estructura básica** de cada página es coherente: URL cumple patrón, page type alineado con contenido, un servicio único, una Main City clara. Cubre las 4 reglas estructurales del paso doctrinal.

**Sub-checks binarios (cada URL pasa o falla cada uno)**

```text
☐ URL QA              — URL cumple patrón estructural Paso-04 4.6 (LBS) / 4.4 (SO) / 4.7 (AC) / 4.5 (GH) / 4.8 (GA) / 4.3 (HP)
                        · Sin near-me, sin adjetivos vacíos, sin LCAs no aprobadas como path
☐ Page Type QA        — H1 sigue spec Paso-05 5.3-5.8 según page type
                        · Secciones esperadas según Paso-06 6.6-6.11
                        · Schema correcto Paso-05 5.9
☐ One Service Only    — Aplicable a LBS, AC, GA: H1 menciona un único Target Service
                        · Copy enfocada en ese servicio (cross-link a otros en sección "Related")
                        · No aplica a SO, GH, HP (multi-service por diseño)
☐ One Main City Only  — Aplicable a LBS, AC, GH, GA: un Target City en H1 + breadcrumb
                        · LCAs aparecen como áreas servidas, no como targets
                        · No aplica a SO (no es local)
```

**Cómo se mide**

- Comparar URL contra patrón doctrinal del page type.
- Inspeccionar H1 + estructura + schema vs spec.
- Inspeccionar H1 + body de cada URL local para single-service focus.
- Inspeccionar H1 + breadcrumb + sección cobertura para single-city focus.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 9.2 — los 4 sub-checks de LBS-1 (`/cerrajero/madrid/cerrajero-urgente/`) en `☑`.

**Ejemplos incorrectos**

```text
- /cerrajero-urgente-cerca-de-mi/ (URL con near-me prohibido)
- LBS escrita como GA informacional (rompe Page Type)
- H1 "Cerrajero urgente y cambio de cerraduras en Madrid" (rompe One Service)
- Breadcrumb con Madrid + Almagro + Salamanca como nodos paralelos (rompe One Main City)
```

**Regla final**

```text
QA Estructural exige los 4 sub-checks en pass para que la URL avance al Final Publish Gate.
```

**Validación operativa**

Aplicar a las N URLs del inventario priorizado (Paso-08 8.14). Las 4 sub-validaciones cubren las reglas 1, 2, 3 y 4 del paso doctrinal del manual original.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar URL + H1 + breadcrumb + estructura por URL contra los outputs heredados.

**Output del paso**

- **Tipo:** 4 sub-checks binarios (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs validadas; 4×28 = 112 sub-checks; 0 fails.

### 9.3 — QA Local

<small>§6.3</small>

**Explicación**

Categoría que valida la **coherencia local** de cada página: que las LCAs declaradas son reales y aparecen naturalmente, que ninguna mención de ubicación es falsa, y que el schema `areaServed` lista solo zonas reales atendidas.

**Sub-checks binarios**

```text
☐ Local Coverage QA          — LCAs en cuerpo coinciden con lista Paso-01 1.10
                                · Mención natural (no se repite cada párrafo)
                                · 0 URLs `/[lca-slug]/` creadas (cumple Paso-04 4.9)
☐ No Fake Location           — 0 menciones tipo "oficina en [LCA]" si no existe sede
                                · Schema `address` = NAP físico real (Paso-01 1.4 + 1.8)
                                · 0 mapas embebidos con ubicación falsa
☐ Schema `areaServed` coherente — `areaServed` lista solo Main City + LCAs aprobadas
                                · Cruza directamente con Paso-06 6.17
                                · Sin zonas inventadas o no aprobadas
```

**Cómo se mide**

- Inspeccionar contenido + schema vs lista LCAs aprobadas.
- Buscar afirmaciones de ubicación; cruzar con NAP único.
- Validar que `areaServed` del schema coincide con outputs heredados.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 9.3 — los 3 sub-checks de LBS-1 en `☑`.

**Ejemplos incorrectos**

```text
- Mencionar Almagro en cada párrafo (keyword stuffing)
- "Nuestra oficina en Salamanca" sin sede real
- Schema LocalBusiness con city = "Salamanca" cuando NAP = Madrid
- areaServed con Aranjuez (LCA no aprobada)
```

**Regla final**

```text
QA Local exige los 3 sub-checks en pass; la web no afirma cobertura/ubicación que no es real.
```

**Validación operativa**

Aplicar a las N URLs locales (LBS, AC, GH, GA). Cruce con Paso-04 4.14 + Paso-05 5.12 + Paso-06 6.2 + 6.17.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar contenido + schema + footer por URL local contra outputs heredados de NAP/LCAs.

**Output del paso**

- **Tipo:** 3 sub-checks binarios (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 22 URLs locales × 3 sub-checks = 66 validaciones; 0 fails.

### 9.4 — QA Contenido

<small>§6.4</small>

**Explicación**

Categoría que valida la **calidad del contenido** entregable: metadata coherente con la intención, profundidad alineada con el page type, schema válido y veraz.

**Sub-checks binarios**

```text
☐ Metadata QA  — H1 sigue spec del page type (Paso-05 5.3-5.8)
                  · Meta title incluye Service + Main City (en LBS) o Service (en SO)
                  · Meta description coherente con H1; persigue misma intención
                  · Sin duplicación entre páginas
☐ Word Count   — Profundidad dentro del rango doctrinal (Paso-05 5.10):
                  · Homepage 900-1,300 / Service Overview 850-1,000
                  · LBS 800-1,000 / Additional Category 800-1,000
                  · GeoHub 700-1,100 / GeoArticle 1,000-1,500
                  · Sin filler ni keyword stuffing
☐ Schema QA    — JSON-LD válido (validador estructurado de Google)
                  · Tipo correcto por page type (Paso-05 5.9)
                  · NAP coherente con footer + Paso-01 1.4
                  · URL canónica presente
                  · Sin sameAs GBP hasta Paso 14
```

**Cómo se mide**

- Inspeccionar los 3 elementos meta por URL; validar coherencia + unicidad.
- Contar palabras del cuerpo principal vs rango doctrinal.
- Validar JSON-LD con tool de Google + cruce con NAP/areaServed reales.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 9.4 — los 3 sub-checks de LBS-1 en `☑`.

**Ejemplos incorrectos**

```text
- H1 "Our Services" (genérico, sin servicio ni ciudad)
- LBS de 320 palabras (thin content)
- Article schema en una landing comercial
- LocalBusiness con address falso
```

**Regla final**

```text
QA Contenido exige los 3 sub-checks en pass; el contenido tiene profundidad real, metadata única y schema veraz.
```

**Validación operativa**

Aplicar a las N URLs del inventario. Cruce con Paso-05 5.3-5.10 + Paso-06 6.17.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar metadata + count + schema por URL contra outputs heredados de specs y validations.

**Output del paso**

- **Tipo:** 3 sub-checks binarios (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs × 3 sub-checks = 84 validaciones; 0 fails.

### 9.5 — QA Conexión

<small>§6.5</small>

**Explicación**

Categoría que valida la **conexión de la página con el resto del cluster**: enlaces internos cumplen la matriz, breadcrumbs siguen jerarquía, y CTA está presente y adaptado al funnel.

**Sub-checks binarios**

```text
☐ Internal Links QA  — Enlaces Required por page type según matriz Paso-07 7.11
                        · Mínimo 5 enlaces internos en LBS
                        · URLs target existen en inventario priorizado (Paso-08 8.14)
                        · Anchors variados (Paso-07 7.9)
                        · Enlaces inline en body, no solo footer
☐ Breadcrumbs QA     — Jerarquía coherente con Paso-07 7.13:
                        · Homepage:        `Home`
                        · Service Overview: `Home > [Categoría] > [Servicio]`
                        · LBS:             `Home > [Categoría] > [Ciudad] > [Servicio]`
                        · Additional Cat:   `Home > [Categoría] > [Ciudad] > [AC-Slug]`
                        · GeoHub:          `Home > [Ciudad]`
                        · GeoArticle:      `Home > [Ciudad] > [Topic]`
                        · BreadcrumbList schema sincronizado con UI
☐ CTA QA             — CTA presente en cada URL (mínimo 1, idealmente 2-3)
                        · Menciona servicio y/o ciudad cuando aplique
                        · Adaptado al funnel (Paso-05 5.11):
                          - LBS = "Llamar"; GA = "Leer LBS / Llamar"
                          - SO = "Solicitar presupuesto"; HP/GH = "Llamar ahora"
                        · Coherente con Preferred CTA del Paso-01 1.13
```

**Cómo se mide**

- Inspeccionar enlaces internos vs matriz Paso-07 7.11; validar URLs target existentes.
- Validar breadcrumb UI + BreadcrumbList schema coinciden con jerarquía Paso-07 7.13.
- Inspeccionar presencia + tipo de CTA contra mapeo doctrinal Paso-05 5.11.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 9.5 — los 3 sub-checks de LBS-1 en `☑`.

**Ejemplos incorrectos**

```text
- LBS con 1 enlace en footer (insuficiente)
- Enlaces a URLs no creadas (rotos)
- Breadcrumb LBS sin nodo Madrid (rompe jerarquía Paso-07 7.13)
- BreadcrumbList schema desincronizado de la UI
- CTA "Contact us" (genérico, sin servicio ni ciudad)
```

**Regla final**

```text
QA Conexión exige los 3 sub-checks en pass; la página está conectada al cluster con anchors, breadcrumbs y CTA coherentes.
```

**Validación operativa**

Aplicar a las N URLs. Cruce con Paso-07 7.9 + 7.11 + 7.13 + 7.14 + Paso-05 5.11.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar enlaces + breadcrumb (UI + schema) + CTA por URL contra matriz y mapeo doctrinal.

**Output del paso**

- **Tipo:** 3 sub-checks binarios (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs × 3 sub-checks = 84 validaciones; 0 fails.

### 9.6 — QA Semántico

<small>§6.6</small>

**Explicación**

Categoría que valida que **no existen 2 URLs cubriendo la misma intención principal**. Si hay solapamiento, una de las dos debe redirigir o reescribirse para perseguir intención distinta.

**Sub-checks binarios**

```text
☐ Canibalización QA  — Cada URL cubre intención única (servicio + ciudad + topic combo)
                        · 0 pares de URLs con H1 duplicado o casi duplicado
                        · 0 GAs con H1 idéntico a su LBS hijo
                        · Cruza con Paso-04 4.15 (no duplicar intención)
```

**Cómo se mide**

- Comparar H1 + URL + intent de las N URLs entre sí.
- Identificar pares con overlap.
- Cruzar con Paso-04 4.15.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 9.6 — el sub-check de LBS-1 en `☑` confirma que no se solapa con la SO no-geolocalizada.

**Ejemplos incorrectos**

```text
- /madrid/cerrajero-urgente/ + /cerrajero/madrid/cerrajero-urgente/ (mismo intento)
- GA con H1 "Cerrajero urgente en Madrid" idéntico a LBS
- 2 LBS para el mismo servicio en la misma Main City
```

**Regla final**

```text
Una intención principal = una URL principal. Sin solapamientos.
```

**Validación operativa**

Aplicar al inventario completo. Cruce con Paso-04 4.15 (no duplicar intención).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Comparar H1 + URL + intent de las N URLs entre sí; identificar pares con overlap.

**Output del paso**

- **Tipo:** 1 sub-check binario (Pass/Fail) por URL + matriz de pares revisados.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs; 0 pares solapados; QA Semántico Pass en 28/28.

### 9.7 — Final Publish Gate

<small>§6.7</small>

**Explicación**

Gate de cierre antes de publicar. **9 checkpoints binarios** que consolidan las 5 categorías QA anteriores en un único bloqueo. Si cualquiera falla, "Ready to publish" = No y la página vuelve a Needs Revision.

**Patrón o fórmula**

```text
□ URL approved              (de QA Estructural · sub-check URL QA)
□ Content approved          (de QA Estructural · 3 sub-checks Page Type/One Service/One City + QA Contenido · sub-check Word Count)
□ SEO metadata approved     (de QA Contenido · sub-check Metadata QA)
□ Schema approved           (de QA Contenido · sub-check Schema QA + QA Local · sub-check areaServed)
□ Internal links approved   (de QA Conexión · sub-check Internal Links + Breadcrumbs)
□ NAP approved              (de QA Local · sub-check No Fake Location + Paso-01 1.4)
□ No canibalization         (de QA Semántico · sub-check Canibalización)
□ No false location claim   (de QA Local · sub-check No Fake Location)
□ CTA approved              (de QA Conexión · sub-check CTA)

→ Ready to publish: AND de los 9
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 9.7 — gate LBS-1 con los 9 checks en Yes.

**Ejemplos incorrectos**

```text
- Publicar con 1-2 checks en No (forzar deploy)
- Marcar todos en Yes sin haber validado realmente las 5 categorías
- Saltar el gate y publicar directo
```

**Regla final**

```text
Ningún URL se publica con menos de 9/9 Yes en el gate.
```

**Validación operativa**

Aplicar a las N URLs. Una página con cualquier No vuelve a "Needs Revision" o "Blocked" según severidad.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Consolidar resultado de las 5 categorías QA (9.2-9.6) en los 9 checkpoints.

**Output del paso**

- **Tipo:** 9 checkpoints binarios + Ready to publish (AND).
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs aprobadas, 0 bloqueadas.

### 9.8 — GBP Not Created QA Checklist

<small>§6.8</small>

**Explicación**

Checklist específico para clusters **web-first** (GBP=Not Created en Paso-01 1.3). Previene que las páginas inventen señales de GBP que no existen todavía. Aplica hasta que el Paso 14 cree el GBP real.

**Patrón o fórmula**

```text
□ GBP Status                  → reconoce GBP=Not Created
□ Planned Category Support    → soporta Planned sin afirmar
□ Planned Additional          → AC respeta categorías Planned
□ No Invented GBP URL         → 0 URLs GBP en schema/footer
□ No Invented Reviews         → 0 reseñas afirmadas
□ sameAs Deferred             → campo sameAs vacío
□ Paso 14 Dependency          → marcada para actualización post-GBP
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 9.8 — checklist LBS-1 con los 7 checks.

**Ejemplos incorrectos**

```text
- "Visita nuestra ficha de Google" + URL falsa
- "10 reseñas en Google" cuando GBP no existe
- sameAs apuntando a GBP inventado
- Schema LocalBusiness con campo "review.aggregateRating" sin reseñas reales
```

**Regla final**

```text
Antes del Paso 14, ninguna página afirma señales de GBP que todavía no existen.
```

**Validación operativa**

Aplicar a las N URLs. Activo solo si Paso-01 1.3 = `Not Created` o `Pending Verification`.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar copy + schema + footer de cada URL contra los 7 checks.

**Output del paso**

- **Tipo:** 7 checks binarios por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs validadas, 0 violaciones.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 9 y avanzar al Paso 10 (Producción en Fases).

### Validación de la plantilla

- ☐ Plantilla QA rellenada al 100% para las N URLs (9.1)

### Validación de las 5 categorías QA

- ☐ QA Estructural pasada en N URLs — 4 sub-checks (9.2)
- ☐ QA Local pasada en URLs locales — 3 sub-checks (9.3)
- ☐ QA Contenido pasada en N URLs — 3 sub-checks (9.4)
- ☐ QA Conexión pasada en N URLs — 3 sub-checks incluyendo Breadcrumbs (9.5)
- ☐ QA Semántico pasada en inventario completo — 1 sub-check (9.6)

### Validación final

- ☐ Final Publish Gate cerrado para N URLs — 9 checkpoints binarios (9.7)
- ☐ GBP Not Created QA Checklist cerrado para N URLs (9.8)
- ☐ Cero URLs con status "Blocked" antes de avanzar a Paso 10

## Outputs Consolidados

<small>§8</small>

> Tabla final compacta con la trazabilidad row-per-output. Los IDs (`9.1`–`9.8`) coinciden con los declarados en §5. Esta tabla es la fuente única de la trazabilidad consolidada del paso (sustituye al antiguo b-doc).

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 9.1 | ← Paso-08 8.14 | **Plantilla de QA por página** = formulario 10 campos × 28 URLs | Generar por URL cruzando outputs heredados con campos de status QA. **Fuente:** GMB Crush. | confirmed |
| 9.2 | ← Paso-04 4.3-4.8 + Paso-05 5.3-5.8 + Paso-01 1.7 + 1.9 | **QA Estructural** = `28/28 URLs Pass` (4 sub-checks: URL/Page Type/One Service/One City) | Inspeccionar URL + H1 + breadcrumb + estructura por URL contra outputs heredados. **Fuente:** GMB Crush. | OK |
| 9.3 | ← Paso-01 1.10 + 1.8 + Paso-04 4.14 + Paso-06 6.17 | **QA Local** = `22/22 URLs locales Pass` (3 sub-checks: Local Coverage/No Fake Location/areaServed) | Inspeccionar contenido + schema + footer vs LCAs/NAP aprobadas. **Fuente:** GMB Crush. | OK |
| 9.4 | ← Paso-05 5.9 + 5.10 + 5.3-5.8 | **QA Contenido** = `28/28 URLs Pass` (3 sub-checks: Metadata/Word Count/Schema) | Inspeccionar metadata + count + JSON-LD por URL contra specs doctrinales. **Fuente:** GMB Crush. | OK |
| 9.5 | ← Paso-07 7.11 + 7.13 + Paso-05 5.11 + Paso-01 1.13 | **QA Conexión** = `28/28 URLs Pass` (3 sub-checks: Internal Links/Breadcrumbs/CTA) | Inspeccionar enlaces + breadcrumb (UI+schema) + CTA contra matrices doctrinales. **Fuente:** GMB Crush. | OK |
| 9.6 | ← Paso-04 4.15 | **QA Semántico** = `0 pares solapados` (1 sub-check: Canibalización) | Comparar H1 + URL + intent de N URLs entre sí. **Fuente:** GMB Crush. | OK |
| 9.7 | ← 9.2-9.6 | **Final Publish Gate** = `28 URLs aprobadas, 0 bloqueadas` | Consolidar resultado de las 5 categorías en 9 checkpoints binarios. **Fuente:** GMB Crush. | OK |
| 9.8 | ← Paso-01 1.3 | **GBP Not Created QA Checklist** = `28 URLs validadas, 0 violaciones` | Inspeccionar copy + schema + footer contra los 7 checks específicos web-first. **Fuente:** GMB Crush. | OK |

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
- QA Framework — 13 reglas operativas agrupadas en 5 categorías + Publish Gate

> **Nota importante — Bloqueo de publicación:**
> El Paso 9 es **gate doctrinal**. Si una URL falla cualquier sub-check, no avanza al Paso 10 (Producción en Fases) ni al Paso 18 (Deploy). El operador no puede saltarse el gate por urgencia comercial — la regla protege la salud de SEO local del cluster.
>
> **Mapeo categorías QA → reglas operativas del manual original:**
> - QA Estructural (9.2) cubre Reglas 1, 2, 3, 4 (URL / Page Type / One Service / One City)
> - QA Local (9.3) cubre Reglas 5, 6 + areaServed (Local Coverage / No Fake Location / Schema areaServed)
> - QA Contenido (9.4) cubre Reglas 7, 8, 9 (Metadata / Word Count / Schema)
> - QA Conexión (9.5) cubre Reglas 10, 12 + Breadcrumbs (Internal Links / CTA + Breadcrumbs nuevo)
> - QA Semántico (9.6) cubre Regla 11 (Canibalización)
