Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 3 — Priorizacion/paso-09-qa-checklist/`, alineado con los frameworks oficiales GMB Crush.

# Paso 9 — QA Checklist

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 15 outputs del Paso 9 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, obtención de outputs, checklist final y outputs consolidados.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 9

<small>§2</small>

En este paso la IA produce todos los outputs que **validan cada página antes de publicación** — la plantilla de QA, las 12 reglas operativas (URL/Page Type/One Service/One City/Local Coverage/No Fake Location/Metadata/Word Count/Schema/Internal Links/Canibalización/CTA), el Final Publish Gate de 9 checkpoints binarios y el GBP Not Created QA Checklist específico para clusters web-first. El Paso 9 es el control de calidad que **bloquea la publicación** si falla cualquier regla.

**Outputs del paso:**

- **9.1** Plantilla de QA por página — formulario operativo (Page ID, Type, URL, Target Service, Main City, GBP Category, LCAs, Priority, Status, QA Date)
- **9.2** Regla 1 — URL QA (cumple patrón estructural de Paso-04)
- **9.3** Regla 2 — Page Type QA (contenido coincide con categorización)
- **9.4** Regla 3 — One Service Only (un único Target Service por página)
- **9.5** Regla 4 — One Main City Only (un Target City claro)
- **9.6** Regla 5 — Local Coverage QA (LCAs reales y naturales)
- **9.7** Regla 6 — No Fake Location (no inventar oficinas)
- **9.8** Regla 7 — Metadata QA (H1 + meta title + description coherentes)
- **9.9** Regla 8 — Word Count QA (rango doctrinal por page type)
- **9.10** Regla 9 — Schema QA (JSON-LD válido y coherente)
- **9.11** Regla 10 — Enlaces Internos QA (matriz Paso-07 cumplida)
- **9.12** Regla 11 — Canibalización QA (una intención = una URL)
- **9.13** Regla 12 — CTA QA (CTA claro y específico)
- **9.14** Final Publish Gate — 9 checkpoints binarios antes de publicar
- **9.15** GBP Not Created QA Checklist — 7 checks específicos para web-first

**Errores que previene:**

- Publicar URLs que violan el patrón doctrinal del Paso-04
- Crear LBS con múltiples servicios o ciudades como targets
- Mencionar oficinas en LCAs sin sede real
- Publicar landings con thin content (<400 palabras)
- Schema con dirección falsa o NAP inconsistente
- Páginas sin enlaces internos o sin CTA
- Canibalización por dos URLs cubriendo la misma intención
- Inventar señales de GBP (URL, sameAs, reseñas) antes del Paso 14

**Cuándo se ejecuta:** después de Pasos 1-8 cerrados (intake + fórmula + matriz + URL rules + page types + content arch + linking + priority). Antes de Paso 10 (Producción en Fases) y Paso 18 (deploy).

## Info heredada de pasos anteriores

<small>§3</small>

> Estos campos NO se deciden en Paso 9 — la IA los lee del paso indicado y los usa como input para validar las páginas del Bloque III.

| Campo | Origen |
|---|---|
| Business Name | Paso-01 1.1 |
| Full NAP | Paso-01 1.4 |
| Planned Primary GBP Category | Paso-01 1.5 |
| Planned Additional GBP Categories | Paso-01 1.6 |
| Main City | Paso-01 1.7 |
| Servicios principales (S=5) | Paso-01 1.9 |
| Local Coverage Areas | Paso-01 1.10 |
| Preferred CTA | Paso-01 1.13 |
| URL patterns por page type | Paso-04 4.3 a 4.8 |
| Validación No falsa ubicación | Paso-04 4.14 |
| Spec por page type (9 sub-outputs) | Paso-05 5.3 a 5.8 |
| Validación Schema | Paso-05 5.9 |
| Validación Word count | Paso-05 5.10 |
| Validación CTA | Paso-05 5.11 |
| Content Architecture por page type | Paso-06 6.6 a 6.11 |
| Schema `areaServed` coherente | Paso-06 6.17 |
| Matriz de enlaces obligatorios | Paso-07 7.11 |
| Inventario priorizado completo | Paso-08 8.14 |

# Bloque II — Ejemplo rellenado para el Paso 9 — QA Checklist

<small>§4</small>

> Los 15 outputs del Paso 9 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 9.X declarado en §5.

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
Status:                Ready for QA
QA Date:               [pendiente]
```

### 9.2 — Regla 1: URL QA (LBS-1)

`Pass` — `/cerrajero/madrid/cerrajero-urgente/` cumple patrón Paso-04 4.6 (`/[primary-cat]/[main-city]/[service-slug]/`).

### 9.3 — Regla 2: Page Type QA (LBS-1)

`Pass` — H1 sigue spec Paso-05 5.5 (Main City Converter); contenido tiene Local Pain Points + LCAs Section + FAQs locales.

### 9.4 — Regla 3: One Service Only (LBS-1)

`Pass` — H1 menciona solo `Cerrajero urgente`; sin mezcla con cambio de cerraduras u otros servicios.

### 9.5 — Regla 4: One Main City Only (LBS-1)

`Pass` — H1 menciona solo Madrid como Main City; las LCAs aparecen en sección dedicada como áreas servidas, no como targets.

### 9.6 — Regla 5: Local Coverage QA (LBS-1)

`Pass` — Las 10 LCAs aparecen en H2 "Local Coverage Areas Served" naturalmente, sin keyword stuffing en cada párrafo.

### 9.7 — Regla 6: No Fake Location (LBS-1)

`Pass` — Schema LocalBusiness con address NAP real (Calle Rafael Calvo 12, Madrid); 0 menciones a "oficina en Almagro" o similares.

### 9.8 — Regla 7: Metadata QA (LBS-1)

`Pass` — Meta title "Top Cerrajero urgente en Madrid | Cerrajeros Madrid 24h" y meta description alineadas con H1 e intención local.

### 9.9 — Regla 8: Word Count QA (LBS-1)

`Pass` — 920 palabras (dentro del rango doctrinal LBS 800-1,000 de Paso-05 5.10).

### 9.10 — Regla 9: Schema QA (LBS-1)

`Pass` — JSON-LD válido: LocalBusiness + BreadcrumbList + FAQPage + Speakable; areaServed coherente con Paso-06 6.17.

### 9.11 — Regla 10: Enlaces Internos QA (LBS-1)

`Pass` — 7 enlaces internos: parent SO (`/cerrajero/cerrajero-urgente/`), GeoHub (`/madrid/`), 3 LBS lateral, 2 GA hijos. Cumple matriz Paso-07 7.11.

### 9.12 — Regla 11: Canibalización QA (LBS-1)

`Pass` — Esta URL es la única que cubre la intención `cerrajero urgente Madrid`. La SO `/cerrajero/cerrajero-urgente/` no se solapa porque es no-geolocalizada.

### 9.13 — Regla 12: CTA QA (LBS-1)

`Pass` — CTA "Llamar ahora · 24h" mencionando servicio + Main City; coherente con Paso-01 1.13 (Preferred CTA).

### 9.14 — Final Publish Gate (LBS-1)

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

### 9.15 — GBP Not Created QA Checklist (LBS-1)

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

> Tabla declarativa de los 15 outputs que el Paso 9 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `9.7`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 9.1 | Plantilla de QA por página | Formulario operativo (10 campos) | GMB Crush | Paso-08 8.14 |
| 9.2 | Regla 1 — URL QA | Validation flag binario por URL | GMB Crush | Paso-04 4.3-4.8 |
| 9.3 | Regla 2 — Page Type QA | Validation flag binario por URL | GMB Crush | Paso-05 5.3-5.8 |
| 9.4 | Regla 3 — One Service Only | Validation flag binario por URL | GMB Crush | Paso-01 1.9 |
| 9.5 | Regla 4 — One Main City Only | Validation flag binario por URL | GMB Crush | Paso-01 1.7 |
| 9.6 | Regla 5 — Local Coverage QA | Validation flag binario por URL | GMB Crush | Paso-01 1.10 + Paso-06 6.2 |
| 9.7 | Regla 6 — No Fake Location | Validation flag binario por URL | GMB Crush | Paso-01 1.8 + Paso-04 4.14 |
| 9.8 | Regla 7 — Metadata QA | Validation flag binario por URL | GMB Crush | Paso-05 5.3-5.8 |
| 9.9 | Regla 8 — Word Count QA | Validation flag binario por URL | GMB Crush | Paso-05 5.10 |
| 9.10 | Regla 9 — Schema QA | Validation flag binario por URL | GMB Crush | Paso-05 5.9 + Paso-06 6.17 |
| 9.11 | Regla 10 — Enlaces Internos QA | Validation flag binario por URL | GMB Crush | Paso-07 7.11 |
| 9.12 | Regla 11 — Canibalización QA | Validation flag binario por URL | GMB Crush | Paso-04 4.15 |
| 9.13 | Regla 12 — CTA QA | Validation flag binario por URL | GMB Crush | Paso-01 1.13 + Paso-05 5.11 |
| 9.14 | Final Publish Gate | 9 checkpoints binarios + Ready to publish | GMB Crush | Paso-09 9.2-9.13 (intra-paso) |
| 9.15 | GBP Not Created QA Checklist | 7 checks específicos web-first | GMB Crush | Paso-01 1.3 + Paso-14 (forward) |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 15 outputs (9.1–9.15). Cada output usa el patrón estándar adaptado al QA: Explicación / Qué verifica / Ejemplos correctos / Ejemplos incorrectos / Regla / Validación / Cómo se obtiene / Output del paso. Cada sub-sección §6.X corresponde 1:1 al output 9.X declarado en §5.

### 9.1 — Plantilla de QA por página

<small>§6.1</small>

**Explicación**

Formulario operativo que se rellena POR PÁGINA antes de hacer QA. Captura la metadata mínima necesaria para validar las 12 reglas. Sin la plantilla, las reglas se aplican de memoria y las violaciones se escapan.

**Patrón o fórmula**

```text
Page ID · Page Type · URL · Target Service · Main City · GBP Category · LCAs · Priority · Phase · Status · QA Date
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 9.1.

**Ejemplos incorrectos**

```text
- Hacer QA sin plantilla rellenada (validaciones de memoria)
- Omitir LCAs (sin contexto, Regla 5 no se valida)
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

### 9.2 — Regla 1: URL QA

<small>§6.2</small>

**Explicación**

Verifica que la URL de la página cumple el **patrón estructural doctrinal** del Paso-04 según su page type. Una URL fuera del patrón rompe la arquitectura del cluster y bloquea publicación.

**Qué verifica**

- LBS: `/[primary-cat]/[main-city]/[service-slug]/`
- SO: `/[primary-cat]/[service-slug]/`
- AC: `/[primary-cat]/[main-city]/[additional-slug]/`
- GeoHub: `/[main-city]/` o `/[primary-cat]/[main-city]/`
- GeoArticle: `/[main-city]/[topic-slug]/`
- Sin near-me, sin adjetivos vacíos, sin LCAs no aprobadas como path.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
/cerrajero/madrid/cerrajero-urgente/  → Pass (LBS pattern)
/madrid/                              → Pass (GeoHub Option A)
/cerrajero/cerrajero-urgente/         → Pass (SO pattern)
```

**Ejemplos incorrectos**

```text
- /cerrajero-urgente-madrid/ (orden incorrecto)
- /cerrajero-urgente-cerca-de-mi/ (near-me prohibido)
- /almagro/cerrajero-urgente/ (LCA como path, prohibido)
```

**Regla final**

```text
URL = patrón doctrinal del page type, sin desviaciones.
```

**Validación operativa**

Aplicar a las N URLs del inventario. Cruce con Paso-04 4.3-4.8 (URL patterns) y 4.11-4.14 (validaciones).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Comparar cada URL con su patrón doctrinal según page type.

**Output del paso**

- **Tipo:** Validation flag (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs validadas, 0 fails.

### 9.3 — Regla 2: Page Type QA

<small>§6.3</small>

**Explicación**

Verifica que el **contenido estructural** de la página coincide con su categorización (page type). Una LBS escrita como GeoArticle, o una SO con targeting local, viola la arquitectura semántica.

**Qué verifica**

- H1 sigue la fórmula del page type (Paso-05 5.3-5.8).
- Secciones esperadas presentes (Content Architecture, Paso-06 6.6-6.11).
- Tone alineado (LBS = comercial; GA = informacional; SO = autoridad temática no local).
- Schema correcto (Paso-05 5.9).

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1 (Cerrajero urgente Madrid):
  - H1 sigue spec 5.5: "Cerrajeros Madrid 24h – Cerrajero urgente en Madrid"
  - Contenido: Local Pain Points + Coverage Areas + FAQs locales
  - Schema: LocalBusiness ✓
```

**Ejemplos incorrectos**

```text
- LBS escrita como artículo informacional (sin CTA, sin schema LocalBusiness)
- SO con targeting local agresivo (rompe rol de pilar temático)
- GA con H1 idéntico al de su LBS (rompe canibalización + rol)
```

**Regla final**

```text
Estructura del contenido = rol del page type, sin mezcla.
```

**Validación operativa**

Aplicar a las N URLs. Cruce con Paso-05 (specs por page type) y Paso-06 (Content Architecture).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Comparar H1 + estructura + schema contra spec del page type.

**Output del paso**

- **Tipo:** Validation flag (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs, 0 fails.

### 9.4 — Regla 3: One Service Only

<small>§6.4</small>

**Explicación**

Verifica que cada página local tiene **un único Target Service** en el H1 y la copy. Mezclar 2-3 servicios en una misma URL diluye la intención y rompe el ranking.

**Qué verifica**

- Un solo Target Service en H1.
- Copy enfocada en ese servicio (sin saltos a otros core services).
- Las menciones a otros servicios viven en sección "Related Services" (cross-link), no en el cuerpo principal.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1: Target Service = "Cerrajero urgente"
H1: "Cerrajeros Madrid 24h – Cerrajero urgente en Madrid"
Copy: 100% sobre cerrajería urgente.
```

**Ejemplos incorrectos**

```text
- H1 "Cerrajero urgente y cambio de cerraduras en Madrid" (dos servicios)
- LBS que en intro pivota a apertura de puertas
- Mezclar duplicado de llaves con cerrajero urgente en una sola URL
```

**Regla final**

```text
Una URL local = un servicio principal. El cross-link va en sección dedicada.
```

**Validación operativa**

Aplicar a LBS, AC y GA (las páginas con servicio único). SO y GH están exentas (multi-service por diseño).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar H1 + intro + body de cada URL local.

**Output del paso**

- **Tipo:** Validation flag (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 5 LBS + 1 AC + 15 GAs = 21 URLs validadas, 0 fails.

### 9.5 — Regla 4: One Main City Only

<small>§6.5</small>

**Explicación**

Verifica que cada página local tiene **una Main City clara**. Listar 5 zonas como "targets" en el H1 dispersa la señal local. Las LCAs aparecen en sección dedicada como áreas servidas, no como targets equivalentes.

**Qué verifica**

- Un solo Target City en H1.
- Breadcrumb con Main City única.
- LCAs aparecen en sección "Local Coverage Areas Served", no en H1 ni breadcrumb.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1:
  H1: "...en Madrid"
  Breadcrumb: Home > Cerrajero > Madrid > Cerrajero urgente
  Sección "LCAs Served": Almagro, Chamberí, Salamanca... (10 zonas)
```

**Ejemplos incorrectos**

```text
- H1 "...en Madrid, Almagro, Chamberí, Salamanca y Retiro"
- Breadcrumb con 5 zonas como nodos paralelos
- LCAs presentadas como targets equivalentes a Main City
```

**Regla final**

```text
Una URL local = una Main City. Las LCAs son áreas servidas, no targets.
```

**Validación operativa**

Aplicar a LBS, AC, GH y GA. SO está exenta (no es local).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar H1 + breadcrumb + sección de cobertura local.

**Output del paso**

- **Tipo:** Validation flag (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 22 URLs locales validadas, 0 fails.

### 9.6 — Regla 5: Local Coverage QA

<small>§6.6</small>

**Explicación**

Verifica que las **LCAs declaradas son reales y aparecen de forma natural** en el contenido. Sin keyword stuffing, sin zonas inventadas, sin URLs creadas para LCAs (ya validado en Paso-04 4.9).

**Qué verifica**

- LCAs en cuerpo coinciden con la lista de Paso-01 1.10.
- Mención natural (no se repite cada párrafo).
- 0 URLs `/[lca-slug]/` creadas.
- `areaServed` schema lista solo LCAs aprobadas.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1 menciona Almagro, Chamberí, Salamanca, Retiro en sección dedicada (1 párrafo + 1 H2).
0 URLs por LCA.
areaServed = [Madrid, Almagro, Chamberí, Salamanca, Retiro, ...] (10 zonas reales).
```

**Ejemplos incorrectos**

```text
- Mencionar Almagro en cada párrafo (keyword stuffing)
- Listar zonas no aprobadas (Chinchón, Aranjuez sin justificación)
- Crear /almagro/ en el inventario
```

**Regla final**

```text
LCAs aparecen una vez por sección, sin stuffing, sin generar URLs.
```

**Validación operativa**

Aplicar a las N URLs locales. Cruce con Paso-01 1.10 + Paso-06 6.2 + Paso-06 6.16.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar contenido + schema vs lista LCAs aprobadas.

**Output del paso**

- **Tipo:** Validation flag (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 22 URLs locales, 0 fails.

### 9.7 — Regla 6: No Fake Location

<small>§6.7</small>

**Explicación**

Verifica que la página **no afirma oficina física, ubicación o presencia comercial** en zonas donde el cliente no opera realmente. Esta regla protege la confianza local y evita contradicciones con GBP, NAP y schema.

**Qué verifica**

- 0 menciones tipo "Nuestra oficina en [LCA]" si no existe sede.
- Schema `address` = NAP físico real (Paso-01 1.4).
- 0 mapas embebidos con ubicación falsa.
- LocalBusiness schema con `address` único (no múltiples).

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h dice "Servimos Almagro, Chamberí, Salamanca..." (cobertura real).
Schema address = "Calle Rafael Calvo 12, 28010 Madrid" (NAP único real).
0 menciones "oficina en [zona]".
```

**Ejemplos incorrectos**

```text
- "Nuestra oficina en Almagro" (sin sede)
- Mapa embedido en Salamanca apuntando a sede ficticia
- LocalBusiness schema con city = "Salamanca" cuando NAP = Madrid
```

**Regla final**

```text
Ubicación física afirmada = NAP único real. Cobertura ≠ oficina.
```

**Validación operativa**

Aplicar a las N URLs. Cruce con Paso-01 1.8 + Paso-04 4.14 + Paso-05 5.12.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Buscar en copy + schema cualquier afirmación de ubicación; cruzar con NAP único.

**Output del paso**

- **Tipo:** Validation flag (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs, 0 fails.

### 9.8 — Regla 7: Metadata QA

<small>§6.8</small>

**Explicación**

Verifica que **H1 + meta title + meta description** reflejan la **misma intención única** y son coherentes entre sí. Un H1 genérico con un meta title persiguiendo otra intención dispersa la señal y dispara CTR bajo.

**Qué verifica**

- H1 sigue spec del page type (Paso-05).
- Meta title incluye Service + Main City (en LBS) o Service (en SO).
- Meta description coherente con H1; persigue misma intención.
- Sin duplicación entre páginas (cada URL tiene meta title/description únicos).

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1:
  H1:           Cerrajeros Madrid 24h – Cerrajero urgente en Madrid
  Meta title:   Top Cerrajero urgente en Madrid | Cerrajeros Madrid 24h
  Meta desc:    ¿Necesitas cerrajero urgente en Madrid? Cerrajeros Madrid 24h ayuda con apertura, cambio y emergencias. Llama para soporte local.
```

**Ejemplos incorrectos**

```text
- H1 "Our Services" (genérico, sin servicio ni ciudad)
- Meta title sin Main City en LBS
- Meta description copiada de otra LBS (duplicación)
```

**Regla final**

```text
H1 + Meta Title + Meta Description = misma intención, sin duplicación cross-página.
```

**Validación operativa**

Aplicar a las N URLs. Cruce con specs por page type (Paso-05 5.3-5.8) y validación general (Paso-05 5.10/5.11).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar los 3 elementos por URL; validar coherencia + unicidad.

**Output del paso**

- **Tipo:** Validation flag (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs, 0 fails.

### 9.9 — Regla 8: Word Count QA

<small>§6.9</small>

**Explicación**

Verifica que la **profundidad del contenido** entra en el rango doctrinal del page type. Sin inflar palabras (keyword stuffing), sin thin content (<400 palabras), sin contenido genérico de relleno.

**Qué verifica**

Rangos doctrinales (Paso-05 5.10):
- Homepage: 900-1,300 palabras
- Service Overview: 850-1,000
- Location-Based Service: 800-1,000
- Additional Category: 800-1,000
- GeoHub: 700-1,100
- GeoArticle: 1,000-1,500

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1: 920 palabras → Pass (rango LBS 800-1,000)
GA principal: 1,180 palabras → Pass (rango GA 1,000-1,500)
Homepage: 1,050 palabras → Pass (rango HP 900-1,300)
```

**Ejemplos incorrectos**

```text
- LBS de 320 palabras (thin content)
- GA de 2,400 palabras (overhang sin justificación)
- Repetir bloques para alcanzar el rango (filler)
```

**Regla final**

```text
Word count entra en el rango doctrinal del page type, sin filler.
```

**Validación operativa**

Aplicar a las N URLs. Validar cada page type contra su rango.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Contar palabras del cuerpo principal (excluyendo footer, navegación, schema).

**Output del paso**

- **Tipo:** Validation flag (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs, 0 fails.

### 9.10 — Regla 9: Schema QA

<small>§6.10</small>

**Explicación**

Verifica que el **JSON-LD schema** es válido, coherente con el page type y con NAP/areaServed reales. Un schema con address falso o tipo incorrecto degrada las señales semánticas que Google consume.

**Qué verifica**

- Schema válido (sin errores en validador estructurado de Google).
- Tipo correcto por page type (Paso-05 5.9).
- NAP coherente con footer y Paso-01 1.4.
- `areaServed` solo lista zonas reales (Paso-06 6.17).
- URL canónica presente.
- Sin `sameAs` GBP hasta Paso 14 (web-first).

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1: LocalBusiness + BreadcrumbList + FAQPage + Speakable
  - address: Calle Rafael Calvo 12, 28010 Madrid (real)
  - areaServed: Madrid + 10 LCAs (reales)
  - sameAs: [] (vacío hasta Paso 14)
```

**Ejemplos incorrectos**

```text
- Article schema en una landing comercial
- LocalBusiness con address falso (Salamanca)
- areaServed con zonas no aprobadas
- sameAs apuntando a un GBP que no existe
```

**Regla final**

```text
Schema válido, coherente con page type, con datos reales y sin GBP hasta Paso 14.
```

**Validación operativa**

Aplicar a las N URLs. Cruce con Paso-05 5.9 + Paso-06 6.17 + Paso-09 9.15 (GBP Not Created).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Validar JSON-LD con tool de Google + cruce con NAP/areaServed reales.

**Output del paso**

- **Tipo:** Validation flag (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs, 0 fails.

### 9.11 — Regla 10: Enlaces Internos QA

<small>§6.11</small>

**Explicación**

Verifica que cada página cumple su **mapa de enlaces obligatorios** según la matriz del Paso-07 7.11. Sin enlaces internos en footer-only, con URLs existentes y anchors naturales.

**Qué verifica**

- Presencia de los enlaces Required por page type (matriz Paso-07 7.11).
- Mínimo 5 enlaces internos en LBS (parent SO, GH, lateral, GAs, contacto).
- URLs target existen en el inventario priorizado (Paso-08 8.14).
- Anchors variados (Paso-07 7.9), no todos branded.
- Enlaces inline en body, no solo en footer.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1: 7 enlaces internos (cumple mínimo 5):
  - Parent SO: /cerrajero/cerrajero-urgente/
  - GeoHub: /madrid/
  - 3 LBS lateral: /cerrajero/madrid/{cambio-cerraduras, apertura-puertas, cambio-bombines}/
  - 2 GAs: /madrid/cuanto-cuesta-un-cerrajero-urgente/, /madrid/que-hacer-si-no-puedes-entrar-casa/
Anchors: 3 branded + 2 partial + 2 generic.
```

**Ejemplos incorrectos**

```text
- LBS con 1 enlace en footer (insuficiente)
- Enlaces a URLs no creadas (rotos)
- Todos los anchors branded ("Cerrajeros Madrid 24h" × 7)
```

**Regla final**

```text
Cada URL cumple su matriz Paso-07 7.11 con anchors variados y URLs reales.
```

**Validación operativa**

Aplicar a las N URLs. Cruce con Paso-07 7.11 + Paso-07 7.9 (anchors) + Paso-07 7.14 (inbound).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar enlaces internos + cruce con matriz de Paso-07 + validar URLs target en inventario.

**Output del paso**

- **Tipo:** Validation flag (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs, 0 fails.

### 9.12 — Regla 11: Canibalización QA

<small>§6.12</small>

**Explicación**

Verifica que **no existen 2 URLs cubriendo la misma intención principal**. Si hay solapamiento, una de las dos debe redirigir o reescribirse para perseguir intención distinta.

**Qué verifica**

- Cada URL cubre intención única (servicio + ciudad + topic combo).
- 0 pares de URLs con H1 duplicado o casi duplicado.
- 0 GAs con H1 idéntico a su LBS hijo.
- Cruce con Paso-04 4.15 (no duplicar intención).

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1 (/cerrajero/madrid/cerrajero-urgente/) cubre intención "cerrajero urgente Madrid".
GA-1 (/madrid/cuanto-cuesta-un-cerrajero-urgente/) cubre intención "precio cerrajero urgente Madrid".
Distintas intenciones → 0 canibalización.
```

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

Aplicar al inventario completo. Cruce con Paso-04 4.15.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Comparar H1 + URL + intent de las N URLs entre sí; identificar pares con overlap.

**Output del paso**

- **Tipo:** Validation flag (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs, 0 pares solapados.

### 9.13 — Regla 12: CTA QA

<small>§6.13</small>

**Explicación**

Verifica que **toda página tiene CTA claro, específico, adaptado al funnel**. Sin CTA = página inerte. CTA genérico = baja conversión. CTA agresivo en GA informacional = ruido.

**Qué verifica**

- Presencia de CTA en cada URL (mínimo 1, idealmente 2-3).
- CTA menciona servicio y/o ciudad cuando aplique.
- CTA adaptado al funnel (Paso-05 5.11): LBS = "Llamar"; GA = "Leer LBS / Llamar"; SO = "Solicitar presupuesto".
- Coherente con Preferred CTA del Paso-01 1.13.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1: CTA "Llamar ahora · Madrid 24h" + botón teléfono
GA principal: CTA "Lee la página de Cerrajero urgente en Madrid" → /cerrajero/madrid/cerrajero-urgente/
SO: CTA "Solicitar presupuesto"
```

**Ejemplos incorrectos**

```text
- CTA "Contact us" (genérico, sin servicio ni ciudad)
- LBS sin CTA (página inerte)
- GA informacional con CTA agresivo "Llama YA YA YA" (ruido)
```

**Regla final**

```text
Toda URL = CTA presente, específico y adaptado al funnel del page type.
```

**Validación operativa**

Aplicar a las N URLs. Cruce con Paso-05 5.11 (CTA por page type) + Paso-01 1.13.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar presencia + tipo de CTA por URL contra mapeo doctrinal.

**Output del paso**

- **Tipo:** Validation flag (Pass/Fail) por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs, 0 fails.

### 9.14 — Final Publish Gate

<small>§6.14</small>

**Explicación**

Gate de cierre antes de publicar. **9 checkpoints binarios** que consolidan las 12 reglas anteriores en un único bloqueo. Si cualquiera falla, "Ready to publish" = No y la página vuelve a Needs Revision.

**Patrón o fórmula**

```text
□ URL approved              (Regla 1)
□ Content approved          (Reglas 2, 3, 4, 5)
□ SEO metadata approved     (Regla 7)
□ Schema approved           (Regla 9)
□ Internal links approved   (Regla 10)
□ NAP approved              (Regla 6 + Paso-01 1.4)
□ No canibalization         (Regla 11)
□ No false location claim   (Regla 6)
□ CTA approved              (Regla 12)

→ Ready to publish: AND de los 9
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 9.14 — gate LBS-1 con los 9 checks en Yes.

**Ejemplos incorrectos**

```text
- Publicar con 1-2 checks en No (forzar deploy)
- Marcar todos en Yes sin haber validado realmente
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
- **Método:** Consolidar resultado de las 12 reglas (9.2-9.13) en los 9 checkpoints.

**Output del paso**

- **Tipo:** 9 checkpoints binarios + Ready to publish (AND).
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs aprobadas, 0 bloqueadas.

### 9.15 — GBP Not Created QA Checklist

<small>§6.15</small>

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

Ver §4 sub-sección 9.15 — checklist LBS-1 con los 7 checks.

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

### Validación de las 12 reglas QA

- ☐ Regla 1 — URL QA pasada en N URLs (9.2)
- ☐ Regla 2 — Page Type QA pasada en N URLs (9.3)
- ☐ Regla 3 — One Service Only en URLs locales (9.4)
- ☐ Regla 4 — One Main City Only en URLs locales (9.5)
- ☐ Regla 5 — Local Coverage QA en URLs locales (9.6)
- ☐ Regla 6 — No Fake Location en N URLs (9.7)
- ☐ Regla 7 — Metadata QA en N URLs (9.8)
- ☐ Regla 8 — Word Count QA en N URLs (9.9)
- ☐ Regla 9 — Schema QA en N URLs (9.10)
- ☐ Regla 10 — Enlaces Internos QA en N URLs (9.11)
- ☐ Regla 11 — Canibalización QA en inventario completo (9.12)
- ☐ Regla 12 — CTA QA en N URLs (9.13)

### Validación final

- ☐ Final Publish Gate cerrado para N URLs (9.14)
- ☐ GBP Not Created QA Checklist cerrado para N URLs (9.15)
- ☐ Cero URLs con status "Blocked" antes de avanzar a Paso 10

## Outputs Consolidados

<small>§8</small>

> Tabla final compacta con la trazabilidad row-per-output. Los IDs (`9.1`–`9.15`) coinciden con los declarados en §5. Esta tabla es la fuente única de la trazabilidad consolidada del paso (sustituye al antiguo b-doc).

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 9.1 | ← Paso-08 8.14 | **Plantilla de QA por página** = formulario 10 campos × 28 URLs | Generar por URL cruzando outputs heredados con campos de status QA. **Fuente:** GMB Crush. | confirmed |
| 9.2 | ← Paso-04 4.3-4.8 | **Regla 1 — URL QA** = `28/28 URLs Pass` | Comparar URL con patrón doctrinal del page type. **Fuente:** GMB Crush. | OK |
| 9.3 | ← Paso-05 5.3-5.8 | **Regla 2 — Page Type QA** = `28/28 URLs Pass` | Comparar H1 + estructura + schema vs spec del page type. **Fuente:** GMB Crush. | OK |
| 9.4 | ← Paso-01 1.9 | **Regla 3 — One Service Only** = `21/21 URLs locales Pass` | Inspeccionar H1 + body de cada URL local. **Fuente:** GMB Crush. | OK |
| 9.5 | ← Paso-01 1.7 | **Regla 4 — One Main City Only** = `22/22 URLs locales Pass` | Inspeccionar H1 + breadcrumb + sección cobertura. **Fuente:** GMB Crush. | OK |
| 9.6 | ← Paso-01 1.10 + Paso-06 6.2 | **Regla 5 — Local Coverage QA** = `22/22 URLs locales Pass` | Inspeccionar contenido + schema vs lista LCAs aprobadas. **Fuente:** GMB Crush. | OK |
| 9.7 | ← Paso-01 1.8 + Paso-04 4.14 | **Regla 6 — No Fake Location** = `28/28 URLs Pass` | Buscar afirmaciones de ubicación; cruzar con NAP único. **Fuente:** GMB Crush. | OK |
| 9.8 | ← Paso-05 5.3-5.8 | **Regla 7 — Metadata QA** = `28/28 URLs Pass` | Inspeccionar H1 + meta title + meta description + unicidad. **Fuente:** GMB Crush. | OK |
| 9.9 | ← Paso-05 5.10 | **Regla 8 — Word Count QA** = `28/28 URLs Pass` | Contar palabras del cuerpo principal vs rango doctrinal. **Fuente:** GMB Crush. | OK |
| 9.10 | ← Paso-05 5.9 + Paso-06 6.17 | **Regla 9 — Schema QA** = `28/28 URLs Pass` | Validar JSON-LD + cruce con NAP/areaServed reales. **Fuente:** GMB Crush. | OK |
| 9.11 | ← Paso-07 7.11 | **Regla 10 — Enlaces Internos QA** = `28/28 URLs Pass` | Inspeccionar enlaces vs matriz de Paso-07 + validar URLs target. **Fuente:** GMB Crush. | OK |
| 9.12 | ← Paso-04 4.15 | **Regla 11 — Canibalización QA** = `0 pares solapados` | Comparar H1 + URL + intent de N URLs entre sí. **Fuente:** GMB Crush. | OK |
| 9.13 | ← Paso-01 1.13 + Paso-05 5.11 | **Regla 12 — CTA QA** = `28/28 URLs Pass` | Inspeccionar presencia + tipo de CTA contra mapeo doctrinal. **Fuente:** GMB Crush. | OK |
| 9.14 | ← 9.2-9.13 | **Final Publish Gate** = `28 URLs aprobadas, 0 bloqueadas` | Consolidar resultado de las 12 reglas en 9 checkpoints binarios. **Fuente:** GMB Crush. | OK |
| 9.15 | ← Paso-01 1.3 | **GBP Not Created QA Checklist** = `28 URLs validadas, 0 violaciones` | Inspeccionar copy + schema + footer contra los 7 checks. **Fuente:** GMB Crush. | OK |

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
- QA Framework — 12 reglas operativas + Publish Gate

> **Nota importante — Bloqueo de publicación:**
> El Paso 9 es **gate doctrinal**. Si una URL falla cualquier regla, no avanza al Paso 10 (Producción en Fases) ni al Paso 18 (Deploy). El operador no puede saltarse el gate por urgencia comercial — la regla protege la salud de SEO local del cluster.
