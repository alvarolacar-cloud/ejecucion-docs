Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 4 — Automatizacion/paso-12-master-prompt/`, alineado con los frameworks oficiales GMB Crush.

# Paso 12 — Master Prompt

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 12 outputs del Paso 12 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush.

# Bloque I — Introducción

## Objetivo del Paso 12

<small>§2</small>

En este paso la IA produce todos los outputs que **convierten el sistema GMB Crush en un Master Prompt reutilizable** — el prompt principal que genera la arquitectura completa de un cluster web local, los 4 prompts auxiliares (URL Matrix / Content Architecture / GeoArticles / QA), las 14 reglas operativas no-negociables del prompt y la regla web-first que protege el GBP. Permite que la IA aplique el sistema a CUALQUIER cliente con solo cambiar los 5 inputs del preflight.

**Outputs del paso:**

- **12.1** Master Prompt principal — el prompt completo reutilizable
- **12.2** Auxiliary Prompt — URL Matrix (genera solo la matriz)
- **12.3** Auxiliary Prompt — Content Architecture (genera solo bloques de contenido)
- **12.4** Auxiliary Prompt — GeoArticles (genera solo los GAs validados)
- **12.5** Auxiliary Prompt — QA (corre las 5 categorías QA del Paso 9)
- **12.6** Estructura del prompt — Header / Inputs / Outputs esperados / Reglas / Ejemplo
- **12.7** Web-First GBP Rule — protección antes del Paso 14
- **12.8** Reglas operativas no-negociables (14 reglas)
- **12.9** Inputs Validation embedded — checks de NAP, categorías, Main City
- **12.10** Executive Summary template
- **12.11** Validación: prompt produce los outputs esperados de Bloques 1-3
- **12.12** Validación: prompt cumple con web-first rule

**Errores que previene:**

- Re-escribir todo el sistema desde cero para cada cliente
- Olvidar reglas doctrinales en la construcción del prompt
- Crear prompts que inventan señales de GBP antes del Paso 14
- Prompts sin validation embedded (NAP/categorías/Main City no se chequean)
- Prompts auxiliares desincronizados del Master

**Cuándo se ejecuta:** después de Paso 11 (Pseudocódigo) cerrado. Antes de Paso 13 (Sistema Final Operativo).

## Info heredada de pasos anteriores

<small>§3</small>

> El Paso 12 es **meta**: encapsula todo el sistema en un prompt. Hereda de Paso 11 (la lógica formalizada) y de los outputs declarativos de Bloques 1-3.

| Campo | Origen |
|---|---|
| Pseudocódigo del sistema (11 funciones + main) | Paso-11 11.1-11.12 |
| Validación de inputs heredados | Paso-11 11.13 |
| Validación de secuencia | Paso-11 11.14 |
| Outputs de Bloques 1-3 (catálogo completo) | 137 outputs upstream |
| GBP Lifecycle Status | Paso-01 1.3 |

# Bloque II — Ejemplo rellenado para el Paso 12 — Master Prompt

<small>§4</small>

> Los 12 outputs del Paso 12 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 12.X declarado en §5.

### 12.1 — Master Prompt principal

```text
ROLE: Eres una IA experta en SEO local web-first según el sistema GMB Crush.

CONTEXT:
Vas a generar la arquitectura web completa para un cluster local
basándote en los inputs de un cliente y aplicando los 14 pasos del sistema.

INPUTS DEL CLIENTE (preflight):
1. Business Name: [BUSINESS_NAME]
2. Servicio principal: [BUSINESS_DESCRIPTION]
3. Dirección con CP: [STREET], [CITY], [ZIP]
4. GBP Status: [GBP_STATUS] (Not Created / Created / Verified / Pending)
5. Ciudades para Local Pack: [LOCAL_PACK_CITIES]

PROCESS (14 pasos del sistema):
- Pasos 1-3 (Bloque 1): construir intake + fórmula maestra + matriz base
- Pasos 4-7 (Bloque 2): URL rules + page types + content arch + linking
- Pasos 8-10 (Bloque 3): priority score + QA + producción en fases
- Pasos 11-13 (Bloque 4): pseudocódigo + master prompt + sistema final operativo
- Paso 14+ (Bloque 5+): GBP creation + post-launch optimization

OUTPUTS ESPERADOS:
A. Executive Summary del cluster
B. URL Matrix completa con score + tier + phase
C. Content Architecture por page type
D. Internal Linking Map
E. Schema Map por page type
F. QA report con publish_gate por URL
G. Roadmap de publicación en 5 fases

REGLAS NO NEGOCIABLES:
[Las 14 reglas de §6.8 listadas aquí]

WEB-FIRST RULE:
[La regla del §6.7 listada aquí]

VALIDATION EMBEDDED:
[Los checks del §6.9 aquí]

INSTRUCTIONS:
1. Validar inputs (NAP, categorías Local Pack, Main City coherente)
2. Aplicar pseudocódigo del Paso 11 paso a paso
3. Producir los 7 outputs (A-G)
4. Bloquear si QA gate falla en cualquier URL
5. Marcar status web-first si GBP_STATUS = Not Created

OUTPUT FORMAT: Markdown estructurado con secciones para cada output.
```

### 12.2 — Auxiliary Prompt — URL Matrix

```text
ROLE: Genera SOLO la URL Matrix del cluster (sin content, sin links, sin scores).

INPUTS: Mismos del Master.

OUTPUT: Tabla con N+1 filas: ID | URL | Page Type | Schema | Priority | Phase | Status.

REGLAS:
- Aplicar fórmula 1+S+1+S+A+G×S
- LCAs no generan filas (Paso-04 4.9)
- Slugs limpios (Paso-04 4.13)
- Sin near-me, sin adjetivos vacíos
```

### 12.3 — Auxiliary Prompt — Content Architecture

```text
ROLE: Genera SOLO la Content Architecture por page type (HP, SO, GH, LBS, AC, GA).

INPUTS: Outputs de Paso 1-7.

OUTPUT: Bloques de contenido por page type (con LCAs en local pages, sin LCAs en SO).

REGLAS:
- Cumplir spec del Paso-05 5.3-5.8
- Word count en rango doctrinal Paso-05 5.10
- LCAs en una sola sección dedicada (Paso-06 6.12)
```

### 12.4 — Auxiliary Prompt — GeoArticles

```text
ROLE: Genera SOLO los G×S GeoArticles validados con keyword research.

INPUTS: core_services + main_city + keyword research data.

OUTPUT: G×S URLs con topic-slug + H1 + meta + intent + parent LBS.

REGLAS:
- Keyword research validado (Paso-03 3.4)
- Cada GA tiene LBS hijo (Paso-08 8.11)
- 1 servicio + 1 Main City + 1 long-tail por GA
```

### 12.5 — Auxiliary Prompt — QA

```text
ROLE: Aplica las 5 categorías QA del Paso 9 a un set de URLs.

INPUTS: Lista de URLs + outputs Bloques 1-3.

OUTPUT: Por URL, los 5 sub-checks + Final Publish Gate.

REGLAS:
- 9.2 Estructural (URL/Page Type/One Service/One City)
- 9.3 Local (Coverage/No Fake/areaServed)
- 9.4 Contenido (Metadata/Word Count/Schema)
- 9.5 Conexión (Links/Breadcrumbs/CTA)
- 9.6 Semántico (Canibalización)
- 9.7 Gate = AND de 5 categorías
```

### 12.6 — Estructura del prompt

```text
Sección 1: ROLE (qué es la IA)
Sección 2: CONTEXT (contexto de la tarea)
Sección 3: INPUTS (5 campos del preflight)
Sección 4: PROCESS (los 14 pasos del sistema)
Sección 5: OUTPUTS ESPERADOS (los 7 entregables A-G)
Sección 6: REGLAS NO NEGOCIABLES (las 14 reglas)
Sección 7: WEB-FIRST RULE
Sección 8: VALIDATION EMBEDDED (checks de calidad)
Sección 9: INSTRUCTIONS (orden de ejecución)
Sección 10: OUTPUT FORMAT (markdown estructurado)
```

### 12.7 — Web-First GBP Rule

```text
WEB-FIRST RULE:
- Si GBP_STATUS = Not Created:
  · La web se publica primero (Bloques 1-4 + producción Bloque 5)
  · El GBP se crea en Paso 14 usando la web como source of truth
  · Aplicar GBP Not Created QA Checklist (Paso-09 9.8) a TODAS las URLs
  · 0 menciones a "ficha de Google" / "reseñas Google" / sameAs URL
  · Schema sin sameAs hasta Paso 14
- Si GBP_STATUS = Created (sin verificar) o Verified:
  · Sincronizar GBP con web ya publicada (orden inverso)
  · sameAs activable
  · Reseñas Google referenciables si existen
```

### 12.8 — Reglas operativas no-negociables (14 reglas)

```text
1. Una página local = 1 servicio + 1 Main City única
2. LCAs son señales de cobertura en contenido + areaServed; NUNCA URLs
3. Approved Expansion Areas requieren aprobación explícita del operador
4. Slugs: lowercase + sin acentos + kebab-case + sin near-me + sin adjetivos
5. Schema válido por page type (Paso-05 5.9)
6. Word count en rango doctrinal por page type (Paso-05 5.10)
7. Internal links cumplen matriz 7.11 + anchors variados 7.9
8. Breadcrumbs jerárquicos según Paso-07 7.13
9. CTA presente y adaptado al funnel del page type (Paso-05 5.11)
10. Priority Score con 6 factores doctrinales (Paso-08 8.1)
11. HP siempre P1 + Phase 1 (Paso-08 8.12)
12. GAs no se publican antes que su LBS hijo (Paso-08 8.11)
13. Final Publish Gate = AND de las 5 categorías QA del Paso 9
14. Web-first si GBP=Not Created (no inventar señales GBP hasta Paso 14)
```

### 12.9 — Inputs Validation embedded

```text
Antes de generar la arquitectura, validar:
- NAP completo (8 campos del Paso-01 1.4); Phone/Email pueden ser placeholders pero declarados
- Primary GBP Category coherente con Local Pack analysis
- Additional Categories clasificadas (cubiertas vs página propia)
- Main City única (no listas)
- Physical Location City declarada (puede coincidir con Main City)
- Servicios principales = 5 (S=5 default; ajustable con justificación)
- LCAs separadas en Direct vs Candidate
- GBP Status declarado entre los 4 valores válidos

Si cualquier check falla → bloquear generación + reportar.
```

### 12.10 — Executive Summary template

```text
[BUSINESS_NAME] — Cluster Web GMB Crush

Status:        [GBP_STATUS]
Main City:     [MAIN_CITY]
Servicios:     [S core services]
LCAs:          [N total = D direct + C candidate]
Total URLs:    [1 + S + 1 + S + A + G×S = N base + 1 aux]
Phase actual:  [Phase 1-N]

Generado:      [DATE]
Bloques 1-3 status: [confirmed/⚠]
QA Gate:       [Pass/Block]
```

### 12.11 — Validación: prompt produce los outputs esperados

Cumplido — el Master Prompt + 4 auxiliares cubren los 7 outputs A-G:
- A (Executive Summary) ← 12.10
- B (URL Matrix) ← 12.2 + Paso-03 3.5
- C (Content Architecture) ← 12.3 + Paso-06 6.6-6.11
- D (Internal Linking) ← Paso-07 7.11
- E (Schema Map) ← Paso-03 3.8 + Paso-05 5.9
- F (QA report) ← 12.5 + Paso-09 9.7
- G (Roadmap) ← Paso-10 10.4-10.9

### 12.12 — Validación: prompt cumple con web-first rule

Cumplido — la regla §6.7 está embebida en el Master Prompt y se activa cuando GBP_STATUS = Not Created. Cruce con Paso-09 9.8 (GBP Not Created QA Checklist).

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 12 outputs que el Paso 12 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `12.7`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 12.1 | Master Prompt principal | Prompt completo | GMB Crush | Paso-11 11.12 + Bloques 1-3 |
| 12.2 | Auxiliary Prompt — URL Matrix | Prompt parcial | GMB Crush | Paso-03 3.5 + Paso-04 4.3-4.8 |
| 12.3 | Auxiliary Prompt — Content Architecture | Prompt parcial | GMB Crush | Paso-05 5.3-5.8 + Paso-06 6.6-6.11 |
| 12.4 | Auxiliary Prompt — GeoArticles | Prompt parcial | GMB Crush | Paso-03 3.4 + Paso-08 8.11 |
| 12.5 | Auxiliary Prompt — QA | Prompt parcial | GMB Crush | Paso-09 9.2-9.8 |
| 12.6 | Estructura del prompt | Plantilla 10 secciones | GMB Crush | — |
| 12.7 | Web-First GBP Rule | Regla embebida | GMB Crush | Paso-01 1.3 + Paso-09 9.8 |
| 12.8 | Reglas operativas no-negociables (14 reglas) | Lista declarativa | GMB Crush | Bloques 1-3 (todas las reglas doctrinales) |
| 12.9 | Inputs Validation embedded | Checks pre-ejecución | GMB Crush | Paso-01 1.X + Paso-02 2.X |
| 12.10 | Executive Summary template | Plantilla output | GMB Crush | Paso-01 1.X + Paso-02 2.X + Paso-08 8.X |
| 12.11 | Validación prompt produce outputs esperados | Validation flag | GMB Crush | Paso-12 12.1-12.5 (intra-paso) |
| 12.12 | Validación prompt cumple web-first | Validation flag | GMB Crush | Paso-01 1.3 + Paso-09 9.8 |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 12 outputs (12.1–12.12). Cada output usa el patrón estándar adaptado a prompts: Explicación / Plantilla / Ejemplo Cerrajeros / Ejemplos incorrectos / Regla / Validación / Cómo se obtiene / Output del paso.

### 12.1 — Master Prompt principal

<small>§6.1</small>

**Explicación**

El Master Prompt es el **artefacto central** del Paso 12. Es un prompt estructurado en 10 secciones que la IA puede ejecutar para generar la arquitectura completa de un cluster local. Re-utilizable: con solo cambiar los 5 inputs del preflight, se aplica a cualquier cliente.

**Plantilla**

Ver §4 sub-sección 12.1 — estructura completa del prompt con placeholders `[VARIABLE]` para los inputs.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Reemplazar placeholders del Master Prompt con:
[BUSINESS_NAME]       → Cerrajeros Madrid 24h
[BUSINESS_DESCRIPTION] → cerrajería urgente y apertura de puertas
[STREET]              → Calle Rafael Calvo 12
[CITY]                → Madrid
[ZIP]                 → 28010
[GBP_STATUS]          → Not Created
[LOCAL_PACK_CITIES]   → Madrid
```

**Ejemplos incorrectos**

```text
- Prompt sin sección REGLAS NO NEGOCIABLES (rompe disciplina)
- Prompt sin VALIDATION EMBEDDED (acepta inputs sucios)
- Prompt sin WEB-FIRST RULE (puede inventar GBP)
- Hard-codear datos de un cliente (no es reusable)
```

**Regla final**

```text
Master Prompt = 10 secciones obligatorias con placeholders para inputs del preflight.
```

**Validación operativa**

Aplicar el prompt a 3 clientes hipotéticos distintos (sectores diferentes) y validar que produce arquitecturas coherentes con el sistema doctrinal.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Componer las 10 secciones del prompt según estructura §6.6 + integrar reglas y validations.

**Output del paso**

- **Tipo:** Prompt completo en markdown.
- **Ejemplo (Cerrajeros Madrid 24h):** Master Prompt con placeholders rellenos para Cerrajeros (ver §4 sub-sección 12.1).

### 12.2 — Auxiliary Prompt — URL Matrix

<small>§6.2</small>

**Explicación**

Prompt auxiliar que genera SOLO la URL Matrix (sin content, sin links, sin scores). Útil cuando el operador quiere validar la matriz antes de proceder.

**Plantilla**

Ver §4 sub-sección 12.2.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Output esperado: 28+1 = 29 filas
ID | URL | Page Type | Schema | Priority | Phase | Status
HP | / | Homepage | Org+WebSite+LocalBusiness+FAQPage | P1 | 1 | Planned
SO-1 | /cerrajero/cerrajero-urgente/ | Service Overview | Service+WebPage+BreadcrumbList | P1 | 2 | Planned
... (29 filas)
```

**Ejemplos incorrectos**

```text
- Generar matriz con LCAs como filas (rompe Paso-04 4.9)
- Más URLs que 1+S+1+S+A+G×S+aux (rompe fórmula 2.9)
- Slugs sucios (con acentos, mayúsculas, near-me)
```

**Regla final**

```text
Auxiliary URL Matrix produce N+1 filas exactas según fórmula maestra.
```

**Validación operativa**

Comparar output del prompt con el output esperado del Paso-03 3.5 cruzado con Paso-08 8.14 (priority).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aislar la sección de URL Matrix del Master Prompt + simplificar el ROLE.

**Output del paso**

- **Tipo:** Prompt auxiliar parcial.
- **Ejemplo (Cerrajeros Madrid 24h):** prompt que produce 29 URLs.

### 12.3 — Auxiliary Prompt — Content Architecture

<small>§6.3</small>

**Explicación**

Prompt auxiliar que genera SOLO los bloques de contenido por page type. Útil cuando el operador quiere refinar la copy sin re-generar el resto.

**Plantilla**

Ver §4 sub-sección 12.3.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Output esperado por page type:
- HP: 11 bloques (intro+services+coverage+trust+FAQ+NAP+CTA+links)
- SO: 11 bloques (intro no-local + Authority/Uniqueness/Depth/Intent/Optimization + bullets + FAQs + CTA + links)
- LBS: 12 bloques (intro local + Quick Answer + Authority + Uniqueness + Depth + Pain + Coverage + Related + FAQs + CTA + links)
- AC: 11 bloques
- GH: 10 bloques (city intro + services menu + AC menu + LCAs + GAs resources + trust + CTA + links)
- GA: 10 bloques (intro + Problem + Local Context + Options/Mistakes + When + Examples + FAQs + CTA + links)
```

**Ejemplos incorrectos**

```text
- Bloques de SO con LCAs (rompe rol no-local)
- Word count fuera de rango (rompe Paso-05 5.10)
- Bloques duplicados entre page types
- Saltar la sección Coverage en LBS (rompe Paso-06 6.2)
```

**Regla final**

```text
Auxiliary Content Architecture cumple specs Paso-05 5.3-5.8 + Paso-06 6.6-6.11.
```

**Validación operativa**

Cruce con Paso-05 (specs por page type) y Paso-06 (Content Architecture).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aislar la sección de Content Architecture del Master Prompt.

**Output del paso**

- **Tipo:** Prompt auxiliar parcial.
- **Ejemplo (Cerrajeros Madrid 24h):** prompt que produce los bloques por page type.

### 12.4 — Auxiliary Prompt — GeoArticles

<small>§6.4</small>

**Explicación**

Prompt auxiliar que genera SOLO los G×S GeoArticles validados con keyword research. Útil cuando el operador quiere refinar topics antes de redactar.

**Plantilla**

Ver §4 sub-sección 12.4.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Output esperado: 15 GAs (G=3 × S=5)
- 3 por servicio Cerrajero urgente: cuanto-cuesta-... / que-hacer-si-no-puedes-... / cuanto-tarda-...
- 3 por servicio Apertura de puertas: cuanto-cuesta-abrir-... / que-hacer-si-te-dejas-llaves / apertura-sin-romper-cerradura
- 3 por servicio Cambio cerraduras: cuando-cambiar-... / cambio-tras-perder-llaves / cerradura-nueva-o-reparacion
- 3 por servicio Cambio bombines: cuando-cambiar-bombin / bombin-antibumping-madrid / cambio-bombin-sin-cambiar-cerradura
- 3 por servicio Instalación seguridad: mejores-cerraduras-seguridad-viviendas / cerraduras-comunidades / cerradura-seguridad-puerta-blindada
```

**Ejemplos incorrectos**

```text
- GAs sin keyword research validado (Paso-03 3.4 ⚠ inferido)
- GA con H1 idéntico a su LBS hijo (canibalización)
- Más GAs que G×S (rompe fórmula)
- GAs sin parent LBS asignado (rompe Paso-08 8.11)
```

**Regla final**

```text
Auxiliary GeoArticles produce G×S URLs con keyword research validado y parent LBS asignado.
```

**Validación operativa**

Cruce con Paso-03 3.4 (GeoArticle Topics validados) + Paso-08 8.11 (Landing antes que GA).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aislar la sección de GA del Master Prompt + integrar keyword research.

**Output del paso**

- **Tipo:** Prompt auxiliar parcial.
- **Ejemplo (Cerrajeros Madrid 24h):** prompt que produce 15 GAs validados.

### 12.5 — Auxiliary Prompt — QA

<small>§6.5</small>

**Explicación**

Prompt auxiliar que aplica las 5 categorías QA del Paso 9 a un set de URLs. Útil para auditar URLs ya construidas antes de publicarlas.

**Plantilla**

Ver §4 sub-sección 12.5.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Input: 28 URLs del cluster
Output:
- Por URL, los 5 sub-checks:
  · QA Estructural: 4 sub-checks
  · QA Local: 3 sub-checks
  · QA Contenido: 3 sub-checks
  · QA Conexión: 3 sub-checks
  · QA Semántico: 1 sub-check
- Final Publish Gate por URL: AND de los 5 (Yes/No)
- Si gbp=Not Created: GBP Checklist con 7 sub-checks adicional
```

**Ejemplos incorrectos**

```text
- Saltar alguna categoría QA (rompe gate doctrinal)
- Omitir GBP Checklist si gbp=Not Created
- Marcar Pass sin haber validado realmente cada sub-check
```

**Regla final**

```text
Auxiliary QA aplica las 5 categorías + gate; produce diagnóstico por URL.
```

**Validación operativa**

Cruce con Paso-09 9.2-9.8.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aislar la sección de QA del Master Prompt + estructurar output diagnóstico.

**Output del paso**

- **Tipo:** Prompt auxiliar parcial.
- **Ejemplo (Cerrajeros Madrid 24h):** prompt que audita 28 URLs y produce gate por URL.

### 12.6 — Estructura del prompt

<small>§6.6</small>

**Explicación**

Las **10 secciones** que conforman cualquier prompt del Paso 12 (Master + auxiliares). Es el contrato de forma que garantiza calidad y reusabilidad.

**Patrón o fórmula**

Ver §4 sub-sección 12.6 — las 10 secciones listadas.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Aplicado al Master Prompt:
1. ROLE: IA experta en SEO local web-first GMB Crush
2. CONTEXT: generar arquitectura para Cerrajeros Madrid 24h
3. INPUTS: los 5 campos del preflight (Cerrajeros)
4. PROCESS: 14 pasos del sistema (referenciados)
5. OUTPUTS: A-G entregables
6. REGLAS NO NEGOCIABLES: 14 reglas
7. WEB-FIRST RULE: activa (GBP=Not Created)
8. VALIDATION EMBEDDED: NAP, Categorías, Main City
9. INSTRUCTIONS: orden de ejecución
10. OUTPUT FORMAT: markdown estructurado
```

**Ejemplos incorrectos**

```text
- Saltar sección INPUTS (prompt no rellena placeholders)
- Combinar varias secciones (PROCESS + INSTRUCTIONS confusas)
- Saltar OUTPUT FORMAT (la IA produce formato libre)
- Omitir REGLAS NO NEGOCIABLES (sistema sin disciplina)
```

**Regla final**

```text
Todo prompt del Paso 12 (Master o auxiliar) tiene las 10 secciones obligatorias.
```

**Validación operativa**

Aplicar checklist a cada prompt (Master + 4 auxiliares); validar que las 10 secciones están presentes.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la plantilla 10-secciones a cada prompt construido.

**Output del paso**

- **Tipo:** Plantilla de 10 secciones.
- **Ejemplo (Cerrajeros Madrid 24h):** Master Prompt + 4 auxiliares = 5 prompts × 10 secciones = 50 sub-secciones validadas.

### 12.7 — Web-First GBP Rule

<small>§6.7</small>

**Explicación**

Regla que protege el sistema cuando GBP_STATUS = Not Created (web-first). Embebida directamente en el Master Prompt y aplicada a TODOS los outputs producidos.

**Patrón o fórmula**

Ver §4 sub-sección 12.7.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Para Cerrajeros (GBP=Not Created):
- Web se publica en Phase 1-3 (Bloques 1-4 + producción)
- GBP se crea en Phase 5 (Paso 14) usando web como source
- GBP Not Created Checklist (Paso-09 9.8) activo en las 28 URLs
- 0 menciones a "ficha de Google" en copy
- sameAs vacío en schema hasta Paso 14
```

**Ejemplos incorrectos**

```text
- Generar arquitectura web con sameAs apuntando a GBP que no existe
- Listar reseñas Google en schema sin haber creado el GBP
- Crear el GBP antes de tener web base sólida (rompe principio web-first)
```

**Regla final**

```text
Si GBP=Not Created, web-first es obligatorio. GBP se crea en Paso 14, no antes.
```

**Validación operativa**

Aplicar a las N URLs si gbp=Not Created. Cruce con Paso-09 9.8 (GBP Not Created QA Checklist).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Embeberla en el Master Prompt + activar condicionalmente según GBP_STATUS.

**Output del paso**

- **Tipo:** Regla embebida.
- **Ejemplo (Cerrajeros Madrid 24h):** activa; 28 URLs validadas con 0 violaciones.

### 12.8 — Reglas operativas no-negociables (14 reglas)

<small>§6.8</small>

**Explicación**

Lista consolidada de las 14 reglas que rigen toda generación de arquitectura. Todas son doctrinales y vienen de pasos anteriores de Bloques 1-3.

**Patrón o fórmula**

Ver §4 sub-sección 12.8.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Las 14 reglas aplicadas al cluster:
1. ✓ LBS-1 = solo Cerrajero urgente + solo Madrid
2. ✓ 10 LCAs en areaServed; 0 URLs por LCA
3. ✓ Approved Expansion = []
4. ✓ Slugs limpios (cerrajero-urgente, etc.)
5. ✓ Schema correcto por page type
6. ✓ Word count en rango por tipo
7. ✓ ~80 enlaces internos con anchors variados
8. ✓ Breadcrumbs Home > Cerrajero > Madrid > Servicio
9. ✓ CTA "Llamar ahora" en LBS, "Solicitar presupuesto" en SO
10. ✓ Priority Score con 6 factores
11. ✓ HP = P1 + Phase 1
12. ✓ GAs en Phase 3-4, después de LBS en Phase 1-2
13. ✓ Final Publish Gate AND de las 5 categorías
14. ✓ Web-first activo (GBP=Not Created)
```

**Ejemplos incorrectos**

```text
- Saltar regla 12 publicando GA antes que LBS hijo
- Inventar regla 15 fuera del catálogo doctrinal
- Aplicar reglas con excepciones sin justificación
```

**Regla final**

```text
Las 14 reglas son no-negociables. Cualquier desviación bloquea la salida del prompt.
```

**Validación operativa**

Aplicar las 14 reglas como filtro de salida del Master Prompt + auxiliares.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Compilar las 14 reglas desde sus pasos origen (Bloques 1-3) y consolidarlas en una sección del prompt.

**Output del paso**

- **Tipo:** Lista declarativa de 14 reglas.
- **Ejemplo (Cerrajeros Madrid 24h):** 14/14 reglas aplicadas con éxito.

### 12.9 — Inputs Validation embedded

<small>§6.9</small>

**Explicación**

Checks que se ejecutan ANTES de generar la arquitectura. Validan que los inputs heredados son completos y coherentes. Si fallan, el prompt no procede.

**Patrón o fórmula**

Ver §4 sub-sección 12.9.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Validations applied:
- NAP: ✓ 8 campos completos (Phone/Email pueden ser placeholders pero declarados)
- Primary GBP Category: ✓ 'Cerrajero' coherente con Local Pack análisis
- Additional Categories: ✓ clasificadas (cubierta vs página propia)
- Main City: ✓ 'Madrid' única
- Physical Location City: ✓ 'Madrid' coincide con Main City
- Servicios principales: ✓ S=5
- LCAs: ✓ 2 Direct + 8 Candidate
- GBP Status: ✓ 'Not Created' válido
```

**Ejemplos incorrectos**

```text
- Pasar inputs incompletos (algún campo NAP en blanco no marcado)
- Listar 3 Main Cities (rompe regla 'una Main City única')
- GBP Status fuera de los 4 valores válidos
```

**Regla final**

```text
Validation embedded bloquea generación si cualquier input es incoherente o incompleto.
```

**Validación operativa**

Aplicar antes de cualquier prompt. Cruce con Paso-01 1.X + Paso-02 2.X.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Compilar checks desde los §3 Heredados de Bloques 1-3 + integrar en sección 8 del prompt.

**Output del paso**

- **Tipo:** Checks embebidos en el prompt.
- **Ejemplo (Cerrajeros Madrid 24h):** 8 checks pasados; 0 fails.

### 12.10 — Executive Summary template

<small>§6.10</small>

**Explicación**

Plantilla del Executive Summary que el Master Prompt produce como primer entregable. Resume estado del cluster en 8 campos clave.

**Patrón o fórmula**

Ver §4 sub-sección 12.10.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cerrajeros Madrid 24h — Cluster Web GMB Crush

Status:        Not Created (web-first)
Main City:     Madrid
Servicios:     5 core + 1 AC efectiva
LCAs:          10 total = 2 Direct + 8 Candidate
Total URLs:    1+5+1+5+1+15 = 28 base + 1 aux = 29
Phase actual:  Phase 1 (semana 1)
Generado:      2026-04-30
Bloques 1-3:   confirmed (137 outputs)
QA Gate:       Pass (28/28)
```

**Ejemplos incorrectos**

```text
- Summary sin Status (ambiguo qué fase)
- Summary sin total URLs (no auditable)
- Summary sin QA Gate (no se sabe si está listo para deploy)
```

**Regla final**

```text
Executive Summary tiene 8 campos obligatorios; auditable de un vistazo.
```

**Validación operativa**

Aplicar al inicio del output del Master Prompt. Cruce con outputs heredados de Bloques 1-3.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Plantilla con placeholders rellenados por el prompt.

**Output del paso**

- **Tipo:** Plantilla de Executive Summary.
- **Ejemplo (Cerrajeros Madrid 24h):** summary completo con 8 campos rellenos.

### 12.11 — Validación: prompt produce los outputs esperados

<small>§6.11</small>

**Explicación**

Valida que la salida del Master Prompt + 4 auxiliares cubre los **7 outputs esperados (A-G)** sin gaps.

**Patrón o fórmula**

```text
Outputs Master Prompt:
A. Executive Summary       ← 12.10
B. URL Matrix              ← 12.2 + 3.5
C. Content Architecture    ← 12.3 + 5.3-5.8
D. Internal Linking Map    ← 7.11
E. Schema Map              ← 3.8 + 5.9
F. QA report               ← 12.5 + 9.7
G. Roadmap publicación     ← 10.4-10.9

Cobertura: ¿los 7 outputs A-G están en la salida del prompt?
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
A: ✓ summary 8 campos
B: ✓ 29 URLs en matriz
C: ✓ bloques por page type
D: ✓ ~80 enlaces internos
E: ✓ schema map por page type
F: ✓ QA report con 28 URLs Pass
G: ✓ roadmap 5 fases con 9 semanas
```

**Ejemplos incorrectos**

```text
- Output sin Roadmap (rompe Paso-10)
- Output sin QA report (rompe gate)
- Output con duplicación entre A y E (resúmenes repetidos)
```

**Regla final**

```text
Master Prompt + auxiliares cubren los 7 outputs A-G sin gaps ni duplicaciones.
```

**Validación operativa**

Auditar la salida del Master Prompt; verificar las 7 secciones presentes.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspección de la salida del prompt + cross-check contra los 7 outputs esperados.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 7/7 outputs cubiertos; 0 gaps.

### 12.12 — Validación: prompt cumple con web-first rule

<small>§6.12</small>

**Explicación**

Valida que el output del prompt **no inventa señales de GBP** cuando el cliente está en estado web-first (GBP=Not Created).

**Patrón o fórmula**

```text
Si GBP_STATUS = Not Created:
  ∀ URL en output:
    - copy.gbp_url == None
    - schema.sameAs == []
    - copy.reseñas_google == 0
    - GBP Not Created Checklist (Paso-09 9.8) Pass
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
GBP_STATUS = Not Created
- 28 URLs sin sameAs en schema
- 0 menciones a 'ficha de Google' en copy
- 0 reseñas Google afirmadas
- GBP Not Created Checklist Pass en 28/28 URLs
```

**Ejemplos incorrectos**

```text
- Output con sameAs apuntando a GBP que no existe
- Output con 'X reseñas en Google' antes de crear el GBP
- Output con review.aggregateRating sin reseñas reales
```

**Regla final**

```text
Si GBP=Not Created, web-first es invariante en TODA la salida del prompt.
```

**Validación operativa**

Aplicar tras generación. Cruce con Paso-09 9.8 (GBP Not Created QA Checklist).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspección de la salida + cross-check con los 7 sub-checks del Paso-09 9.8.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 28/28 URLs Pass GBP Checklist.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 12 y avanzar al Paso 13 (Sistema Final Operativo).

### Validación de prompts

- ☐ Master Prompt principal con 10 secciones (12.1)
- ☐ Auxiliary Prompt URL Matrix funcional (12.2)
- ☐ Auxiliary Prompt Content Architecture funcional (12.3)
- ☐ Auxiliary Prompt GeoArticles funcional (12.4)
- ☐ Auxiliary Prompt QA funcional (12.5)

### Validación de estructura y reglas

- ☐ Estructura 10 secciones aplicada en los 5 prompts (12.6)
- ☐ Web-First GBP Rule embebida (12.7)
- ☐ 14 reglas operativas no-negociables presentes (12.8)
- ☐ Inputs Validation embedded antes de generación (12.9)
- ☐ Executive Summary template con 8 campos (12.10)

### Validación final

- ☐ Prompt produce los 7 outputs A-G sin gaps (12.11)
- ☐ Prompt cumple web-first rule en TODA la salida (12.12)

## Outputs Consolidados

<small>§8</small>

> Tabla final compacta con la trazabilidad row-per-output. Los IDs (`12.1`–`12.12`) coinciden con los declarados en §5. Esta tabla es la fuente única de la trazabilidad consolidada del paso (sustituye al antiguo b-doc).

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 12.1 | ← Paso-11 11.12 + Bloques 1-3 | **Master Prompt principal** = prompt 10 secciones aplicado a Cerrajeros (rellena 5 placeholders del preflight) | Componer 10 secciones del prompt + integrar reglas y validations. **Fuente:** GMB Crush. | confirmed |
| 12.2 | ← Paso-03 3.5 + Paso-04 4.3-4.8 | **Auxiliary Prompt URL Matrix** = produce 29 URLs (28 base + 1 aux) | Aislar sección URL Matrix del Master + simplificar ROLE. **Fuente:** GMB Crush. | confirmed |
| 12.3 | ← Paso-05 5.3-5.8 + Paso-06 6.6-6.11 | **Auxiliary Prompt Content Architecture** = produce bloques por page type (HP 11 + SO 11 + LBS 12 + AC 11 + GH 10 + GA 10) | Aislar sección Content Architecture del Master. **Fuente:** GMB Crush. | confirmed |
| 12.4 | ← Paso-03 3.4 + Paso-08 8.11 | **Auxiliary Prompt GeoArticles** = produce 15 GAs validados (G=3 × S=5) | Aislar sección GA del Master + integrar keyword research. **Fuente:** GMB Crush. | confirmed |
| 12.5 | ← Paso-09 9.2-9.8 | **Auxiliary Prompt QA** = audita 28 URLs y produce gate por URL | Aislar sección QA del Master + estructurar output diagnóstico. **Fuente:** GMB Crush. | confirmed |
| 12.6 | — | **Estructura del prompt** = 10 secciones obligatorias (ROLE/CONTEXT/INPUTS/PROCESS/OUTPUTS/REGLAS/WEB-FIRST/VALIDATION/INSTRUCTIONS/FORMAT) | Aplicar plantilla 10-secciones a cada prompt. **Fuente:** GMB Crush. | confirmed |
| 12.7 | ← Paso-01 1.3 + Paso-09 9.8 | **Web-First GBP Rule** = activa para Cerrajeros (GBP=Not Created); 0 violaciones | Embeberla en Master Prompt + activar condicionalmente. **Fuente:** GMB Crush. | OK |
| 12.8 | ← Bloques 1-3 (todas las reglas) | **14 reglas no-negociables** = aplicadas con éxito en el cluster | Compilar reglas desde pasos origen y consolidar en sección del prompt. **Fuente:** GMB Crush. | OK |
| 12.9 | ← Paso-01 1.X + Paso-02 2.X | **Inputs Validation embedded** = 8 checks pasados (NAP/Categorías/Main City/etc.) | Compilar checks desde §3 Heredados + integrar en sección 8 del prompt. **Fuente:** GMB Crush. | OK |
| 12.10 | ← Paso-01 1.X + Paso-02 2.X + Paso-08 8.X | **Executive Summary template** = 8 campos rellenos (Status / Main City / Servicios / LCAs / URLs / Phase / Date / QA Gate) | Plantilla con placeholders rellenados por el prompt. **Fuente:** GMB Crush. | confirmed |
| 12.11 | ← 12.1-12.5 | **Validación prompt produce 7 outputs** = 7/7 outputs A-G cubiertos | Inspección de salida del prompt + cross-check con outputs esperados. **Fuente:** GMB Crush. | OK |
| 12.12 | ← Paso-01 1.3 + Paso-09 9.8 | **Validación prompt cumple web-first** = 28/28 URLs Pass GBP Checklist | Inspección de salida + cross-check con 7 sub-checks Paso-09 9.8. **Fuente:** GMB Crush. | OK |

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
- Master Prompt Framework GMB Crush

> **Nota importante — Master Prompt como interfaz del sistema:**
> El Paso 12 NO inventa contenido nuevo: empaqueta los outputs declarativos de Bloques 1-3 + el pseudocódigo del Paso 11 en un prompt reutilizable. Cualquier cliente puede aplicarlo cambiando solo los 5 inputs del preflight. La calidad del output depende de la calidad de los outputs upstream — basura entra, basura sale.
