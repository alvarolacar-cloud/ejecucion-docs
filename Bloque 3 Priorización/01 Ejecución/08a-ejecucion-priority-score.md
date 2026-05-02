Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 3 — Priorizacion/paso-08-priority-score/`, alineado con los frameworks oficiales GMB Crush.

# Paso 8 — Priority Score

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 14 outputs del Paso 8 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, obtención de outputs, checklist final y outputs consolidados.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 8

<small>§2</small>

En este paso la IA produce todos los outputs que **convierten intuición en orden de publicación operativo** — la fórmula maestra de prioridad, los 6 factores de scoring (cada uno escala 1-5), el score total por página (1-30), los Priority Tiers (P1/P2/P3/P4/Hold), la Publish Phase derivada y las validaciones doctrinales. Todos se generan a partir de los inputs heredados de Pasos 1-7 + research adicional (keyword data, Local Pack, SERP analysis).

**Outputs del paso:**

- **8.1** Priority Score Formula — fórmula maestra que combina los 6 factores
- **8.2** Revenue Value — factor 1, escala 1-5 (margen económico por página)
- **8.3** Search Intent — factor 2, escala 1-5 (proximidad del usuario a conversión)
- **8.4** GBP Category Relevance — factor 3, escala 1-5 (alineación con categorías GBP)
- **8.5** Local Relevance — factor 4, escala 1-5 (refuerzo de Main City)
- **8.6** Competition Gap — factor 5, escala 1-5 (debilidad SERP de competidores)
- **8.7** Conversion Urgency — factor 6, escala 1-5 (sensibilidad temporal del usuario)
- **8.8** Total Score por página — suma de los 6 factores (1-30)
- **8.9** Priority Tiers — clasificación P1/P2/P3/P4/Hold según rangos de score
- **8.10** Publish Phase derivada — orden secuencial de publicación (Phase 1, 2, 3...)
- **8.11** Validación Landing antes que GeoArticle — regla doctrinal de dependencia
- **8.12** Validación Homepage = P1 obligatorio — regla doctrinal de raíz
- **8.13** Validación LCAs sin score — LCAs no generan URLs y no entran al scoring
- **8.14** Inventario priorizado completo — tabla N filas con score + tier + phase

**Errores que previene:**

- Publicar GeoArticles antes que su LBS de soporte
- Inventar prioridad sin fórmula auditable
- Mezclar criterios subjetivos en el orden de publicación
- Tratar LCAs como URLs candidatas a scoring
- Olvidar que Homepage siempre es P1 (Root Entity Anchor)
- Asignar P1 a páginas con Revenue Value bajo y sin urgencia
- Ignorar el Competition Gap y publicar contra SERPs saturados sin diferenciación

**Cuándo se ejecuta:** después de Pasos 1-7 cerrados (intake + fórmula + matriz + URL rules + page types + content arch + linking). Antes de Paso 9 (QA) y Paso 10 (Producción en Fases).

## Info heredada de pasos anteriores

<small>§3</small>

> Estos campos NO se deciden en Paso 8 — la IA los lee del paso indicado y los usa como input para calcular los scores del Bloque III.

| Campo | Origen |
|---|---|
| Planned Primary GBP Category | Paso-01 1.5 |
| Planned Additional GBP Categories | Paso-01 1.6 |
| Main City | Paso-01 1.7 |
| Physical Location City | Paso-01 1.8 |
| Servicios principales (S=5) | Paso-01 1.9 |
| Local Coverage Areas (Direct + Candidate) | Paso-01 1.10 |
| Preferred CTA | Paso-01 1.13 |
| Trust Signals | Paso-01 1.14 |
| Variable A | Paso-02 2.7 |
| Total páginas SEO base | Paso-02 2.9 |
| Inventario por tipo de página | Paso-02 2.10 |
| URL Matrix completa | Paso-03 3.5 |
| Primary Service (hero del cluster) | Paso-05 5.1 |

# Bloque II — Ejemplo rellenado para el Paso 8 — Priority Score

<small>§4</small>

> Los 14 outputs del Paso 8 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 8.X declarado en §5.

### 8.1 — Priority Score Formula

```text
Priority Score = Revenue + Intent + GBP Category + Local Relevance + Competition Gap + Urgency
                 (1-5)    (1-5)   (1-5)          (1-5)            (1-5)            (1-5)
                                = Total entre 6 y 30 puntos
```

### 8.2 — Revenue Value (Cerrajero urgente Madrid LBS)

`5` (servicio de alto margen + ticket alto + urgencia que premia la acción inmediata).

### 8.3 — Search Intent

`5` (la mayoría de queries son transaccionales/urgentes: "cerrajero urgente Madrid", "abrir puerta ya", "cerrajero 24h").

### 8.4 — GBP Category Relevance

`5` (categoría primaria `Cerrajero` aparece en ≥3 perfiles top del Local Pack como primary).

### 8.5 — Local Relevance

`5` (URL `/cerrajero/madrid/cerrajero-urgente/` refuerza Main City + servicio + categoría primaria; NAP alineado).

### 8.6 — Competition Gap

`4` (top 10 SERP tiene 2 LBS dedicadas + 5 directorios débiles + 3 perfiles GBP — hay hueco real).

### 8.7 — Conversion Urgency

`5` (servicio de emergencia 24h, el usuario llama en minutos no en días).

### 8.8 — Total Score (Cerrajero urgente Madrid LBS)

`5 + 5 + 5 + 5 + 4 + 5 = 29` puntos.

### 8.9 — Priority Tiers (rangos)

```text
P1:   26–30 puntos   (publish immediately)
P2:   21–25 puntos   (publish phase 2)
P3:   16–20 puntos   (publish phase 3+)
P4:   10–15 puntos   (queue for later)
Hold:  0–9  puntos   (revisit or deactivate)
```

### 8.10 — Publish Phase derivada

```text
Phase 1: Homepage + LBS Cerrajero urgente Madrid (P1)
Phase 2: Service Overview Pages + GeoHub Madrid + LBS resto (P1-P2)
Phase 3: Additional Category + GeoArticles principales (P2-P3)
Phase 4: GeoArticles long-tail (P3)
```

### 8.11 — Validación Landing antes que GeoArticle

Cumplido — la LBS `/cerrajero/madrid/cerrajero-urgente/` se publica antes que su GeoArticle hijo `/madrid/cuanto-cuesta-un-cerrajero-urgente/`.

### 8.12 — Validación Homepage = P1 obligatorio

Cumplido — Homepage `/` lleva P1 fijo independientemente de su score individual (Regla 10).

### 8.13 — Validación LCAs sin score

Cumplido — las 10 LCAs declaradas (Almagro, Chamberí, Salamanca, etc.) no son URLs y no entran al inventario priorizado.

### 8.14 — Inventario priorizado completo (Cerrajeros Madrid 24h)

| Page ID | URL | Tipo | R | I | G | L | C | U | Score | Tier | Phase |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HP | `/` | Homepage | 5 | 5 | 5 | 5 | 4 | 5 | 29 | P1 | 1 |
| LBS-1 | `/cerrajero/madrid/cerrajero-urgente/` | LBS | 5 | 5 | 5 | 5 | 4 | 5 | 29 | P1 | 1 |
| LBS-3 | `/cerrajero/madrid/cambio-cerraduras/` | LBS | 5 | 4 | 5 | 5 | 4 | 4 | 27 | P1 | 2 |
| LBS-2 | `/cerrajero/madrid/apertura-puertas/` | LBS | 4 | 5 | 5 | 5 | 4 | 5 | 28 | P1 | 2 |
| LBS-4 | `/cerrajero/madrid/cambio-bombines/` | LBS | 4 | 4 | 5 | 5 | 4 | 4 | 26 | P1 | 2 |
| LBS-5 | `/cerrajero/madrid/instalacion-cerraduras-seguridad/` | LBS | 5 | 4 | 5 | 5 | 3 | 3 | 25 | P2 | 2 |
| GH | `/madrid/` | GeoHub | 4 | 4 | 4 | 5 | 4 | 4 | 25 | P2 | 2 |
| SO-1 | `/cerrajero/cerrajero-urgente/` | SO | 4 | 4 | 4 | 3 | 4 | 4 | 23 | P2 | 2 |
| SO-2..5 | `/cerrajero/{service}/` | SO | 3 | 3 | 4 | 3 | 4 | 3 | 20 | P3 | 2 |
| AC-1 | `/cerrajero/madrid/duplicado-llaves/` | AC | 3 | 3 | 4 | 5 | 4 | 2 | 21 | P2 | 3 |
| GA-1..15 | `/madrid/{topic}/` | GA | 3 | 3 | 4 | 5 | 4 | 3 | 22 | P2 | 3-4 |

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 14 outputs que el Paso 8 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `8.5`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 8.1 | Priority Score Formula | Fórmula declarada | GMB Crush | — |
| 8.2 | Revenue Value | Score 1-5 por página | GMB Crush + Input humano | Paso-01 1.9 |
| 8.3 | Search Intent | Score 1-5 por página | GMB Crush + Datos de búsqueda | Paso-01 1.9 + Paso-03 3.4 |
| 8.4 | GBP Category Relevance | Score 1-5 por página | GMB Crush + Competidores | Paso-01 1.5 + 1.6 |
| 8.5 | Local Relevance | Score 1-5 por página | GMB Crush | Paso-01 1.7 + 1.8 + 1.10 |
| 8.6 | Competition Gap | Score 1-5 por página | GMB Crush + Competidores | Paso-01 1.7 + Paso-01 1.9 |
| 8.7 | Conversion Urgency | Score 1-5 por página | GMB Crush | Paso-01 1.9 + 1.13 |
| 8.8 | Total Score por página | Entero (6-30) | GMB Crush | Paso-08 8.2-8.7 (intra-paso) |
| 8.9 | Priority Tiers | Enum (P1/P2/P3/P4/Hold) | GMB Crush | Paso-08 8.8 (intra-paso) |
| 8.10 | Publish Phase derivada | Phase 1-N | GMB Crush | Paso-08 8.9 + Paso-02 2.10 |
| 8.11 | Validación Landing antes que GeoArticle | Validation flag | GMB Crush | Paso-03 3.5 + Paso-08 8.10 |
| 8.12 | Validación Homepage = P1 obligatorio | Validation flag | GMB Crush | — |
| 8.13 | Validación LCAs sin score | Validation flag | GMB Crush | Paso-01 1.10 + Paso-04 4.9 |
| 8.14 | Inventario priorizado completo | Tabla N filas con score + tier + phase | GMB Crush | Paso-03 3.5 + Paso-08 8.8-8.10 |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 14 outputs (8.1–8.14). Los **scores por factor** (8.2–8.7) usan un mini-patrón adaptado: Explicación / Escala 1-5 / Cómo se mide / Ejemplos correctos / Ejemplos incorrectos / Regla / Output. La **fórmula maestra** (8.1), el **total** (8.8), los **tiers** (8.9) y la **publish phase** (8.10) usan el patrón estándar. Las **4 validaciones** (8.11–8.14) usan el patrón estándar.

### 8.1 — Priority Score Formula

<small>§6.1</small>

**Explicación**

La Priority Score Formula es la combinación de 6 factores que sustituye la intuición por una fórmula auditable. Cada factor se puntúa de 1 a 5; la suma da un total entre 6 y 30 que clasifica la página en un Priority Tier (P1-Hold). El operador no decide tier directamente — el tier emerge del scoring.

**Patrón o fórmula**

```text
Priority Score = Revenue + Intent + GBP Category + Local Relevance + Competition Gap + Urgency
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS Cerrajero urgente Madrid: 5 + 5 + 5 + 5 + 4 + 5 = 29 → P1
GeoArticle "cuanto cuesta un cerrajero urgente": 3 + 3 + 4 + 5 + 4 + 3 = 22 → P2
```

**Ejemplos incorrectos**

```text
- Asignar tier directo sin calcular factores
- Inventar un factor adicional fuera de los 6 doctrinales
- Promediar en lugar de sumar (rompe la escala 6-30)
- Usar pesos distintos a 1 para cada factor
```

**Regla final**

```text
Los 6 factores se suman con peso 1; el total cae en uno de los 5 tiers doctrinales.
```

**Validación operativa**

Aplicar la fórmula a las N URLs del inventario SEO base (Paso-03 3.5). Si una URL no llega a 6 puntos sumando los 6 factores, error de medición — revisar.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar la fórmula a cada URL del inventario SEO base; medir cada factor con su método operativo (§6.2-§6.7); sumar los 6 valores.

**Output del paso**

- **Tipo:** Fórmula declarada.
- **Ejemplo (Cerrajeros Madrid 24h):** `Priority Score = R + I + G + L + C + U` (rango 6-30).

### 8.2 — Revenue Value

<small>§6.2</small>

**Explicación**

Mide el **output económico por página** — combinación de margen, ticket medio y volumen comercial. Servicios con alto ticket y alta urgencia premian al máximo; servicios cotidianos de bajo margen puntúan poco.

**Escala 1-5**

```text
1 = Servicio de bajo margen / ticket bajo / volumen incierto
2 = Margen estándar, sin urgencia comercial
3 = Margen medio + ticket razonable
4 = Margen alto + ticket alto, sin emergencia
5 = Alto margen + ticket alto + urgencia que premia acción inmediata
```

**Cómo se mide**

- Analizar coste medio del servicio + margen bruto.
- Comparar con baseline del portfolio del cliente.
- Cruzar con conversion data si existe.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS Cerrajero urgente Madrid → 5 (urgencia + alto ticket + alta tasa de cierre)
LBS Cambio de bombines → 4 (ticket medio-alto, sin emergencia)
GeoArticle "cuanto cuesta un cerrajero" → 3 (informacional pero atrae intención comercial)
```

**Ejemplos incorrectos**

```text
- Asignar 5 a un GeoArticle informacional
- Asignar 1 a la Homepage por no ser una landing concreta
- Usar percepción del operador sin cruzar con datos del cliente
```

**Regla final**

```text
Revenue Value mide ROI esperado por página. Servicios urgentes con alto ticket = 5; informacional = 1-3.
```

**Validación operativa**

Aplicar a las N URLs. Validar que la Homepage tiene 4-5 (es la página de entidad y converge tráfico de marca).

**Cómo se obtiene**

- **Fuente:** GMB Crush + Input humano.
- **Método:** Pedir al cliente ticket medio + margen por servicio (Paso-01 1.9). Asignar score según tabla; si falta dato, inferir con benchmark sectorial.

**Output del paso**

- **Tipo:** Score 1-5 por página.
- **Ejemplo (Cerrajeros Madrid 24h):** Cerrajero urgente LBS = 5; GA = 3.

### 8.3 — Search Intent

<small>§6.3</small>

**Explicación**

Mide la **proximidad del usuario a la conversión**. Queries transaccionales (con modifiers como "urgente", "ya", "precio", "[ciudad]") puntúan alto; informacionales puntúan bajo.

**Escala 1-5**

```text
1 = Mayoría informacional (qué es, cómo funciona)
2 = Informacional con leve interés
3 = Mixto informacional + comercial
4 = Mayoría comercial (precio, comparativa)
5 = ≥60% transaccional (urgente, ya, [ciudad])
```

**Cómo se mide**

- Keyword research (Ahrefs / Semrush / Google KP) por URL.
- Contar queries con modifiers transaccionales vs informacionales.
- Calcular porcentaje transaccional → mapear a escala.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS Cerrajero urgente Madrid → 5 (queries dominadas por "urgente", "ya", "Madrid")
GeoArticle "cuándo cambiar la cerradura" → 2 (informacional)
GeoArticle "cuanto cuesta un cerrajero urgente" → 4 (commercial intent claro)
```

**Ejemplos incorrectos**

```text
- Asignar 5 a un GA informacional puro
- Confundir volume con intent (high volume informacional ≠ alta intent)
- Ignorar modifiers locales en el conteo
```

**Regla final**

```text
Search Intent se mide por porcentaje de queries transaccionales en el cluster keyword de la página.
```

**Validación operativa**

Aplicar a las N URLs con keyword research disponible. Cruce con Paso-03 3.4 (GeoArticle Topics) — si el topic no tiene keyword research, el score es ⚠ inferido.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Datos de búsqueda.
- **Método:** Ejecutar keyword research por URL; clasificar queries por modifier; calcular % transaccional; mapear a escala.

**Output del paso**

- **Tipo:** Score 1-5 por página.
- **Ejemplo (Cerrajeros Madrid 24h):** LBS Cerrajero urgente Madrid = 5; GA informacional = 2.

### 8.4 — GBP Category Relevance

<small>§6.4</small>

**Explicación**

Mide la **alineación de la página con la Primary o Additional GBP Category**. Páginas que soportan directamente una categoría real del GBP del cliente puntúan alto; páginas tangenciales puntúan bajo.

**Escala 1-5**

```text
1 = Soporte débil o inexistente (página tangencial a la categoría)
2 = Soporte indirecto (relación lateral)
3 = Soporte parcial (informacional general, sin alineamiento fuerte)
4 = Soporte directo (Additional Category con página propia OR página informacional fuerte alineada con Primary)
5 = Match exacto: la página es el ancla principal de la Primary o Additional GBP Category (LBS/AC en top 5 Local Pack)
```

**Cómo se mide**

- Buscar `[categoría] [Main City]` en Google Maps.
- Contar perfiles del top 5 que muestran esa categoría como primary.
- 5 = página comercial dedicada + ≥3 perfiles competidores tienen esa categoría como primary.
- 4 = AC con página propia, o GA fuerte alineado con Primary (intent comercial).
- 3 = informacional general (cubre el tema sin enfoque fuerte).
- 2 = relación lateral, soporte indirecto.
- 1 = página tangencial sin soporte real.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS Cerrajero urgente Madrid → 5 (categoría primaria 'Cerrajero')
AC Duplicado de llaves Madrid → 4 (Additional Category con página)
GA "cuanto cuesta un cerrajero urgente" → 4 (soporta primary)
```

**Ejemplos incorrectos**

```text
- Asignar 5 a una página de categoría que no aparece en GBP
- Confundir "tema relacionado" con "categoría GBP"
- Dar 1 a una página de Primary Category solo por estar mal optimizada
```

**Regla final**

```text
GBP Category Relevance solo es alto si la categoría coincide con la Primary o Additional declarada del cliente.
```

**Validación operativa**

Aplicar a las N URLs. Validar que toda página con score 4-5 mapea a una categoría real declarada en Paso-01 1.5 o 1.6.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Competidores.
- **Método:** Cruzar URL con categorías declaradas en Paso-01 1.5/1.6 + análisis Local Pack en Maps.

**Output del paso**

- **Tipo:** Score 1-5 por página.
- **Ejemplo (Cerrajeros Madrid 24h):** Cerrajero urgente LBS = 5; AC = 4.

### 8.5 — Local Relevance

<small>§6.5</small>

**Explicación**

Mide cuánto **refuerza la página la Main City + NAP + cobertura local aprobada**. URLs con `[main-city-slug]` en path puntúan alto; páginas no geolocalizadas puntúan bajo. Se penalizan zonas no aprobadas.

**Escala 1-5**

```text
1 = Genérica, sin geo-señal
2 = Mención débil de Main City
3 = Main City en H1/copy pero no en URL
4 = Main City en URL + contenido local sustancial
5 = URL geolocalizada + NAP alineado + LCAs en areaServed/contenido
```

**Cómo se mide**

- Inspeccionar URL: ¿lleva `[main-city-slug]` o `[lca-slug]` no aprobado?
- Inspeccionar contenido: ¿menciona Main City + LCAs aprobadas naturalmente?
- Inspeccionar schema: ¿`areaServed` lista solo zonas aprobadas?

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS /cerrajero/madrid/cerrajero-urgente/ → 5 (URL + NAP + areaServed)
SO /cerrajero/cerrajero-urgente/ → 3 (sin geo en URL pero pilar temático)
GA /madrid/cuanto-cuesta-un-cerrajero-urgente/ → 5 (URL geolocalizada + LCAs en cuerpo)
```

**Ejemplos incorrectos**

```text
- Asignar 5 a una SO no geolocalizada (su rol es pilar, no converter)
- Penalizar a 1 una Homepage que tiene NAP correcto y Main City
- Dar 5 a una URL con LCA no aprobada como path
```

**Regla final**

```text
Local Relevance solo llega a 5 si URL + NAP + schema + contenido están alineados con Main City o LCA aprobada.
```

**Validación operativa**

Aplicar a las N URLs. Cruce con Paso-04 4.14 (no falsa ubicación) y Paso-06 6.2 (LCAs enriquecen contenido).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar URL + schema + contenido contra los outputs heredados de NAP (1.4), Main City (1.7), LCAs (1.10).

**Output del paso**

- **Tipo:** Score 1-5 por página.
- **Ejemplo (Cerrajeros Madrid 24h):** LBS = 5, SO = 3, GH = 5, GA = 5.

### 8.6 — Competition Gap

<small>§6.6</small>

**Explicación**

Mide la **debilidad de los competidores en la SERP** para la combinación servicio + Main City de la página. Si el top 10 está dominado por LBS dedicadas y reviews fuertes, el gap es bajo (1-2). Si dominan directorios genéricos y thin content, el gap es alto (4-5).

**Escala 1-5**

```text
1 = SERP saturada con LBS fuertes + reviews + autoridad
2 = ≥5 LBS dedicadas en top 10
3 = 3-4 LBS dedicadas + el resto directorios
4 = ≤2 LBS dedicadas; resto thin content / agregadores
5 = ≤2 competidores fuertes; SERP dominada por contenido débil
```

**Cómo se mide**

- Buscar `[servicio] [main-city]` en Google.
- Analizar top 10 orgánico: ¿cuántos son LBS dedicadas? ¿cuántos directorios?
- Cruzar con DR/UR/Backlinks (Ahrefs) para validar fortaleza.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS Cerrajero urgente Madrid → 4 (2 LBS dedicadas + 5 directorios + 3 GBPs en top 10)
LBS Cambio de bombines Madrid → 4 (similar competition)
GeoArticle "cuanto cuesta cerrajero" → 4 (top 10 con artículos genéricos)
```

**Ejemplos incorrectos**

```text
- Asignar 5 sin haber abierto la SERP
- Confundir "pocos competidores" con "competidores débiles" — pueden ser pocos pero fuertes
- Ignorar GBPs en el top (cuentan como competencia local)
```

**Regla final**

```text
Competition Gap se mide ejecutando la SERP real, no por intuición.
```

**Validación operativa**

Aplicar a las N URLs principales (LBS + GAs). En SO, score por defecto 4 (suelen tener menos competencia local fuerte).

**Cómo se obtiene**

- **Fuente:** GMB Crush + Competidores.
- **Método:** SERP analysis manual + soporte Ahrefs/Semrush (DR/UR del top 10) por keyword principal de cada URL.

**Output del paso**

- **Tipo:** Score 1-5 por página.
- **Ejemplo (Cerrajeros Madrid 24h):** LBS = 4, GA = 4, SO = 4.

### 8.7 — Conversion Urgency

<small>§6.7</small>

**Explicación**

Mide la **sensibilidad temporal del usuario**. Servicios de emergencia 24h puntúan al máximo (el usuario llama en minutos). Servicios planificables puntúan bajo (el usuario investiga durante días o semanas).

**Escala 1-5**

```text
1 = Investigación / planificación (el usuario tarda semanas)
2 = Planificable, decisión a días
3 = Decisión a 24-48h
4 = Decisión a horas
5 = Emergencia (decisión en minutos)
```

**Cómo se mide**

- Clasificar el servicio según ventana típica de decisión.
- Cruzar con keyword data (modifiers "urgente", "ya", "ahora").

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS Cerrajero urgente Madrid → 5 (cerrajería 24h = emergencia)
LBS Apertura de puertas Madrid → 5 (emergencia, usuario fuera de casa)
LBS Cambio de cerraduras Madrid → 4 (urgencia post-incidente, decisión a horas/día)
LBS Cambio de bombines Madrid → 4 (urgencia post-incidente, decisión a horas/día)
LBS Instalación de cerraduras de seguridad → 3 (preventivo planificado)
GA "cuándo cambiar la cerradura" → 1-2 (investigación)
```

**Ejemplos incorrectos**

```text
- Asignar 5 a un GA informacional
- Tratar todos los servicios del cluster con mismo score
- Confundir Conversion Urgency con Search Intent (urgency = ventana de decisión, intent = % transaccional)
```

**Regla final**

```text
Conversion Urgency mide ventana de decisión, no intención de búsqueda. Emergencias = 5.
```

**Validación operativa**

Aplicar a las N URLs. Validar que la Homepage hereda el score más alto de los core services (es la entrada genérica + tiene más urgency que un GA).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Clasificación del servicio por ventana de decisión típica + cruce con keyword research.

**Output del paso**

- **Tipo:** Score 1-5 por página.
- **Ejemplo (Cerrajeros Madrid 24h):** LBS Cerrajero urgente = 5; LBS Apertura puertas = 5; LBS Bombines = 4; LBS Cambio cerraduras = 4; LBS Instalación seguridad = 3; GA = 1-3.

### 8.8 — Total Score por página

<small>§6.8</small>

**Explicación**

Suma de los 6 factores (8.2 a 8.7) para cada página. Rango entre 6 y 30 puntos. Es el output que alimenta directamente la asignación de Priority Tier (8.9).

**Patrón o fórmula**

```text
Total Score (URL_i) = R_i + I_i + G_i + L_i + C_i + U_i
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
HP            = 5+5+5+5+4+5 = 29
LBS Cerrajero urgente Madrid = 5+5+5+5+4+5 = 29
GA "cuanto cuesta cerrajero urgente" = 3+3+4+5+4+3 = 22
SO Cerrajero urgente = 4+4+4+3+4+4 = 23
```

**Ejemplos incorrectos**

```text
- Sumar con pesos distintos a 1 (la fórmula es suma simple)
- Promediar en lugar de sumar
- Aplicar redondeos creativos
```

**Regla final**

```text
Total Score = suma simple de los 6 factores con peso 1 cada uno.
```

**Validación operativa**

Aplicar a las N URLs. Validar que el Total cae en [6, 30] — si excede, error de medición.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Sumar los 6 valores producidos en §6.2-§6.7 por URL.

**Output del paso**

- **Tipo:** Entero (6-30).
- **Ejemplo (Cerrajeros Madrid 24h):** HP=29, LBS-1=29, GA=22.

### 8.9 — Priority Tiers

<small>§6.9</small>

**Explicación**

Clasificación del Total Score en 5 tiers doctrinales que dictan el orden de publicación. P1 publica inmediatamente; Hold se revisa o se desactiva.

**Patrón o fórmula**

```text
Score 26-30 → P1   (publish immediately)
Score 21-25 → P2   (publish phase 2)
Score 16-20 → P3   (publish phase 3+)
Score 10-15 → P4   (queue for later)
Score  6-9  → Hold (revisit or deactivate)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Score 29 → P1 (HP, LBS Cerrajero urgente Madrid)
Score 22 → P2 (GA principal)
Score 18 → P3 (GA long-tail)
```

**Ejemplos incorrectos**

```text
- Asignar tier directo sin calcular score
- Cambiar los rangos doctrinales
- Promover páginas Hold sin validar mejora del scoring
```

**Regla final**

```text
Tier emerge del score; nunca al revés.
```

**Validación operativa**

Aplicar a las N URLs. Validar que la Homepage termina como P1 (con Regla 8.12 forzando P1 si por score quedara P2).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Mapear el Total Score (8.8) al rango doctrinal.

**Output del paso**

- **Tipo:** Enum P1/P2/P3/P4/Hold por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** HP=P1, LBS-1=P1, GA principal=P2.

### 8.10 — Publish Phase derivada

<small>§6.10</small>

**Explicación**

Orden secuencial de publicación. Phase 1 = primero (Homepage + LBS de Primary Service). Phase 2 = segundo bloque (resto de LBS + Service Overview + GeoHub). Phase 3+ = AC + GAs. La Phase respeta tanto el Tier como las dependencias estructurales (Paso-02 2.13).

**Patrón o fórmula**

```text
Phase 1: HP (P1) + LBS Primary Service (P1)
Phase 2: SO (P1-P2) + GeoHub (P2) + LBS resto (P1-P2)
Phase 3: AC (P2-P3) + GAs principales (P2-P3)
Phase 4: GAs long-tail (P3-P4)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Phase 1: HP, LBS Cerrajero urgente Madrid
Phase 2: GeoHub Madrid, 5 SO, 4 LBS restantes
Phase 3: AC Duplicado de llaves, 5-7 GAs principales
Phase 4: 8-10 GAs long-tail
```

**Ejemplos incorrectos**

```text
- Publicar GAs en Phase 1 sin haber publicado su LBS hijo
- Saltar Phase 2 directamente a Phase 4
- Ignorar el orden HP → SO → GH → LBS → AC → GAs (Paso-02 2.13)
```

**Regla final**

```text
La Phase respeta tanto el Tier como las dependencias estructurales del inventario.
```

**Validación operativa**

Aplicar a las N URLs. Cruce con Paso-02 2.13 (orden de dependencias) y Paso-08 8.11 (landing antes que GA).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Cruzar el Tier (8.9) con las dependencias estructurales (Paso-02 2.13) para asignar Phase 1-N.

**Output del paso**

- **Tipo:** Phase 1-N por URL.
- **Ejemplo (Cerrajeros Madrid 24h):** HP=Phase 1, LBS-1=Phase 1, GeoHub=Phase 2, GAs=Phase 3-4.

### 8.11 — Validación Landing antes que GeoArticle

<small>§6.11</small>

**Explicación**

Regla doctrinal: una **LBS o SO siempre se publica antes que cualquier GeoArticle que la apoya**. Si publicas un GA antes que su LBS, el GA queda huérfano comercialmente y no transfiere autoridad porque su destino no existe.

**Patrón o fórmula**

```text
Para cada GA G:
  Si parent(G) ∈ {LBS, SO}, entonces phase(parent) < phase(G)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS /cerrajero/madrid/cerrajero-urgente/ → Phase 1
GA /madrid/cuanto-cuesta-un-cerrajero-urgente/ → Phase 3
(LBS antes que GA: OK)
```

**Ejemplos incorrectos**

```text
- Publicar GA en Phase 2 cuando su LBS está en Phase 3
- Tratar GA como landing comercial autónoma
- Olvidar el parent del GA al asignar phase
```

**Regla final**

```text
Ningún GA se publica antes que su LBS/SO de soporte.
```

**Validación operativa**

Aplicar a los G×S GeoArticles. Cruce con Paso-03 3.7 (Parent Page por fila) y Paso-07 7.7 (GA pasa relevancia a landing).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Validar fila a fila del inventario (8.14) que phase(parent) < phase(GA).

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 15 GAs validados; 0 violaciones.

### 8.12 — Validación Homepage = P1 obligatorio

<small>§6.12</small>

**Explicación**

Regla doctrinal: la **Homepage siempre lleva P1 fijo** independientemente de su score individual. La Homepage es el Root Entity Anchor del cluster — sin ella publicada, ninguna otra página renta. Por eso se publica primero, en Phase 1, sin importar si el scoring devolvería P2.

**Patrón o fórmula**

```text
phase(HP) = 1
tier(HP) = P1
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
HP score = 29 → tier P1 → phase 1 (consistente con la regla)
HP score = 22 (hipotético) → forzado a P1 + phase 1 (Regla 8.12)
```

**Ejemplos incorrectos**

```text
- Publicar Homepage en Phase 2 porque otra página tiene mayor score
- Asignar P2 a Homepage para "balancear" la fase
- Tratar Homepage como una landing más
```

**Regla final**

```text
Homepage siempre P1 + Phase 1, sin excepciones.
```

**Validación operativa**

Aplicar al inventario. Validar que la fila HP tiene tier=P1 y phase=1.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Forzar tier=P1 y phase=1 en la fila HP del inventario priorizado.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** HP en P1 + Phase 1; OK.

### 8.13 — Validación LCAs sin score

<small>§6.13</small>

**Explicación**

Las **Local Coverage Areas no son URLs** y no entran al inventario priorizado. Mencionar Almagro o Chamberí en el contenido de una LBS no genera una fila scored — esas zonas viven en `areaServed` y en cuerpo de página, no como path independiente. Esta validación previene el error común de tratarlas como URLs candidatas a publicación.

**Patrón o fórmula**

```text
Para cada LCA L:
  L ∉ inventario priorizado
  L NO tiene URL `/{slug-LCA}/`
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LCAs: Almagro, Chamberí, Salamanca, Retiro, Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad
Inventario priorizado: 28 URLs (HP + 5 SO + GH + 5 LBS + 1 AC + 15 GAs + AUX)
0 filas LCA en el inventario.
```

**Ejemplos incorrectos**

```text
- Crear /almagro/ en el inventario y asignarle score
- Tratar Almagro como una LBS candidata
- Confundir mención en areaServed con URL publicable
```

**Regla final**

```text
LCAs nunca entran al inventario priorizado del Paso 8.
```

**Validación operativa**

Aplicar al inventario completo. Validar que ninguna fila tiene una LCA como path. Cruce con Paso-04 4.9 (LCAs no generan URLs) y Paso-06 6.2 (LCAs enriquecen contenido).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Comparar el inventario (Paso-03 3.5) con la lista de LCAs (Paso-01 1.10) y validar 0 intersecciones.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 10 LCAs; 0 filas en inventario priorizado.

### 8.14 — Inventario priorizado completo

<small>§6.14</small>

**Explicación**

Tabla final con las **N URLs del inventario SEO base** (Paso-02 2.10), enriquecidas con los 6 factores, el Total Score, el Tier y la Publish Phase. Este es el output que alimenta directamente al Paso 9 (QA) y al Paso 10 (Producción en Fases).

**Patrón o fórmula**

```text
Para cada URL_i en Paso-03 3.5:
  Output_i = (URL, Tipo, R, I, G, L, C, U, Score, Tier, Phase)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 8.14 — tabla con las 28 URLs priorizadas.

**Ejemplos incorrectos**

```text
- Publicar el inventario sin haber calculado los 6 factores
- Omitir la columna Phase (rompe el Paso 10)
- Mezclar URLs de Approved Expansion con la base inicial
```

**Regla final**

```text
Inventario priorizado = todas las N URLs base con score + tier + phase calculados.
```

**Validación operativa**

Aplicar a las N URLs. Validar que la tabla cubre el 100% de Paso-03 3.5 sin omisiones.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Generar tabla cruzando Paso-03 3.5 (URLs) con los outputs 8.2-8.10 (scores, tier, phase) por fila.

**Output del paso**

- **Tipo:** Tabla N filas con score + tier + phase.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs priorizadas (ver §4 sub-sección 8.14).

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 8 y avanzar al Paso 9 (QA Checklist).

### Validación de la fórmula y los 6 factores

- ☐ Priority Score Formula declarada y aplicada (8.1)
- ☐ Revenue Value medido con criterio operativo (8.2)
- ☐ Search Intent medido con keyword research (8.3)
- ☐ GBP Category Relevance medido con Local Pack analysis (8.4)
- ☐ Local Relevance medido vs URL + NAP + schema (8.5)
- ☐ Competition Gap medido con SERP analysis (8.6)
- ☐ Conversion Urgency clasificada por ventana de decisión (8.7)

### Validación de scores y tiers

- ☐ Total Score por página calculado (8.8)
- ☐ Priority Tiers asignados según rangos doctrinales (8.9)
- ☐ Publish Phase asignada respetando tier + dependencias (8.10)

### Validación de reglas doctrinales

- ☐ Landing antes que GeoArticle (8.11)
- ☐ Homepage = P1 obligatorio (8.12)
- ☐ LCAs sin score (8.13)

### Validación final

- ☐ Inventario priorizado completo cubre el 100% de Paso-03 3.5 (8.14)
- ☐ Cero violaciones de las 3 reglas doctrinales

## Outputs Consolidados

<small>§8</small>

> Tabla final compacta con la trazabilidad row-per-output. Los IDs (`8.1`–`8.14`) coinciden con los declarados en §5. Esta tabla es la fuente única de la trazabilidad consolidada del paso (sustituye al antiguo b-doc).

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 8.1 | — | **Priority Score Formula** = `R + I + G + L + C + U` (rango 6-30) | Doctrina GMB Crush — fórmula maestra de los 6 factores. **Fuente:** GMB Crush. | confirmed |
| 8.2 | ← Paso-01 1.9 | **Revenue Value** = LBS Cerrajero urgente Madrid `5`; LBS Bombines `4`; GA `3` | Análisis margen + ticket por servicio + benchmark sectorial. **Fuente:** GMB Crush + Input humano. | confirmed |
| 8.3 | ← Paso-01 1.9 + Paso-03 3.4 | **Search Intent** = LBS Cerrajero urgente Madrid `5`; GA informacional `2` | Keyword research por URL; calcular % queries transaccionales. **Fuente:** GMB Crush + Datos de búsqueda. | confirmed |
| 8.4 | ← Paso-01 1.5 + 1.6 | **GBP Category Relevance** = LBS Cerrajero urgente Madrid `5`; AC `4`; SO `4` | Cruce categorías declaradas vs Local Pack en Maps. **Fuente:** GMB Crush + Competidores. | confirmed |
| 8.5 | ← Paso-01 1.7 + 1.8 + 1.10 | **Local Relevance** = LBS `5`; SO `3`; GH `5`; GA `5` | Inspección URL + schema + contenido contra NAP/Main City/LCAs. **Fuente:** GMB Crush. | confirmed |
| 8.6 | ← Paso-01 1.7 + 1.9 | **Competition Gap** = LBS `4`; GA `4`; SO `4` | SERP analysis manual + DR/UR Ahrefs por keyword principal. **Fuente:** GMB Crush + Competidores. | confirmed |
| 8.7 | ← Paso-01 1.9 + 1.13 | **Conversion Urgency** = LBS Cerrajero urgente Madrid `5`; LBS Apertura puertas `5`; LBS Bombines `4`; LBS Cambio cerraduras `4`; LBS Instalación seguridad `3`; GA `1-3` | Clasificación por ventana de decisión típica + cruce keyword. **Fuente:** GMB Crush. | confirmed |
| 8.8 | ← 8.2-8.7 | **Total Score por página** = HP `29`; LBS-1 `29`; GA principal `22`; SO `23` | Suma simple de los 6 factores con peso 1. **Fuente:** GMB Crush. | confirmed |
| 8.9 | ← 8.8 | **Priority Tiers** = HP `P1`; LBS-1 `P1`; GA `P2`; SO `P3` | Mapping del Total Score a rango doctrinal P1-Hold. **Fuente:** GMB Crush. | confirmed |
| 8.10 | ← 8.9 + Paso-02 2.10 | **Publish Phase derivada** = HP `Phase 1`; LBS-1 `Phase 1`; GH `Phase 2`; GAs `Phase 3-4` | Cruce Tier × dependencias estructurales (Paso-02 2.13). **Fuente:** GMB Crush. | confirmed |
| 8.11 | ← Paso-03 3.5 + 8.10 | **Validación Landing antes que GeoArticle** = `15 GAs validados; 0 violaciones` | Validar phase(parent) < phase(GA) por fila. **Fuente:** GMB Crush. | OK |
| 8.12 | — | **Validación Homepage = P1 obligatorio** = `HP en P1 + Phase 1` | Forzar tier=P1 y phase=1 en la fila HP. **Fuente:** GMB Crush. | OK |
| 8.13 | ← Paso-01 1.10 + Paso-04 4.9 | **Validación LCAs sin score** = `10 LCAs; 0 filas en inventario priorizado` | Comprobar 0 intersecciones LCA × inventario. **Fuente:** GMB Crush. | OK |
| 8.14 | ← Paso-03 3.5 + 8.8-8.10 | **Inventario priorizado completo** = `28 URLs priorizadas (ver §4 sub-sección 8.14)` | Generar tabla N filas con score+tier+phase por URL. **Fuente:** GMB Crush. | confirmed |

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
- Priority Score Framework (sistema de 6 factores GMB Crush)

> **Nota importante — Priority Score como contrato del sistema:**
> Los 6 factores no son negociables ni se sustituyen por intuición. Cualquier cliente, sector o cluster aplica los mismos 6 factores con la misma escala 1-5. Si un caso de uso particular pareciera "no encajar", la respuesta es ajustar la medición de los factores existentes — nunca añadir un 7º factor o cambiar los pesos.
