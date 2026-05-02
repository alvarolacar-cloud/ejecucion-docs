Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 3 — Priorizacion/paso-10-produccion-en-fases/`, alineado con los frameworks oficiales GMB Crush.

# Paso 10 — Producción en Fases

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 13 outputs del Paso 10 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, obtención de outputs, checklist final y outputs consolidados.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 10

<small>§2</small>

En este paso la IA produce todos los outputs que **convierten la matriz priorizada en calendario operativo realista** — Publishing Capacity, Content Team, CMS capabilities, las 5 Fases doctrinales (Entity Foundation, Main City Conversion, Semantic Expansion, Optimization Loop, GBP Creation), el calendario semanal, la matriz de dependencias, las 10 reglas operativas y el checklist pre-publicación. Sin este paso, las páginas se publican en orden caótico y se rompe la cascada de autoridad.

**Outputs del paso:**

- **10.1** Publishing Capacity — páginas/semana realistas según team
- **10.2** Content Team composition — composición del equipo (writer, SEO, dev)
- **10.3** CMS + capabilities — plataforma + capacidad de schema, linking, reviews, tracking
- **10.4** Fase 1 — Entity Foundation (HP + SO + GH)
- **10.5** Fase 2 — Main City Conversion Layer (LBS + AC)
- **10.6** Fase 3 — Main City Semantic Expansion (GAs)
- **10.7** Fase 4 — Optimization Loop (continuous post-launch)
- **10.8** Fase 5 — GBP Creation & Website Alignment (web-first sync)
- **10.9** Calendario semanal de publicación
- **10.10** Matriz de dependencias de publicación
- **10.11** Las 10 reglas operativas del paso
- **10.12** Checklist pre-publicación (8 items)
- **10.13** Validación Bloques 1-2 cerrados antes de arrancar Paso 10

**Errores que previene:**

- Publicar GeoArticles antes que su LBS de soporte
- Crear el GBP antes de tener web base sólida
- Saltarse Fase 4 (sin tracking, sin iteración)
- Establecer una velocidad de publicación incompatible con calidad
- Olvidar dependencias: publicar AC sin que GeoHub esté listo
- Lanzar expansión territorial antes de validar la base

**Cuándo se ejecuta:** después de Pasos 1-9 cerrados (intake + fórmula + matriz + URL rules + page types + content arch + linking + priority + QA). Antes del Paso 14 (creación efectiva del GBP) y Paso 18 (deploy).

## Info heredada de pasos anteriores

<small>§3</small>

> Estos campos NO se deciden en Paso 10 — la IA los lee del paso indicado y los usa como input para construir el calendario del Bloque III.

| Campo | Origen |
|---|---|
| Business Name | Paso-01 1.1 |
| Website URL / Canonical Domain | Paso-01 1.2 |
| GBP Lifecycle Status | Paso-01 1.3 |
| Full NAP | Paso-01 1.4 |
| Planned Primary GBP Category | Paso-01 1.5 |
| Planned Additional GBP Categories | Paso-01 1.6 |
| Main City | Paso-01 1.7 |
| Servicios principales (S=5) | Paso-01 1.9 |
| Local Coverage Areas | Paso-01 1.10 |
| Approved Expansion Areas | Paso-01 1.11 |
| Total páginas SEO base | Paso-02 2.9 |
| Inventario por tipo de página | Paso-02 2.10 |
| URL Matrix completa | Paso-03 3.5 |
| Priority y Publish Phase por fila | Paso-03 3.10 |
| Publish Phase derivada | Paso-08 8.10 |
| Inventario priorizado completo | Paso-08 8.14 |
| Final Publish Gate por URL | Paso-09 9.14 |

# Bloque II — Ejemplo rellenado para el Paso 10 — Producción en Fases

<small>§4</small>

> Los 13 outputs del Paso 10 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 10.X declarado en §5.

### 10.1 — Publishing Capacity

`5 páginas/semana`

(team de 1 SEO + 1 writer dedicado parcial; permite calidad con QA por lote).

### 10.2 — Content Team composition

```text
- 1 SEO (40% dedicado): briefs, schema, internal linking, QA
- 1 Writer (60% dedicado): redacción + revisión competitiva
- 0 Dev (CMS no requiere desarrollo custom)
- 1 Operador del sistema (QA gate + decisiones de fase)
```

### 10.3 — CMS + capabilities

```text
CMS:                  WordPress
Schema capability:    Sí (plugin manual + JSON-LD inline)
Internal linking:     Manual editable
Reviews embedding:    Sí (preparado para Paso 14 post-GBP)
Tracking:             GSC + GA4 + Rank Tracker (Ahrefs)
```

### 10.4 — Fase 1 — Entity Foundation (Semanas 1-2)

```text
Páginas: HP + 5 SO + GH = 7 páginas
URLs:    /, /cerrajero/{cerrajero-urgente, apertura-puertas, cambio-cerraduras,
         cambio-bombines, instalacion-cerraduras-seguridad}/, /madrid/
Total semana 1: 5 páginas (HP + 4 SO)
Total semana 2: 2 páginas (1 SO restante + GeoHub)
Pre-requisitos: Bloque 1 + Bloque 2 cerrados, Paso 9 QA Pass.
```

### 10.5 — Fase 2 — Main City Conversion Layer (Semanas 2-3)

```text
Páginas: 5 LBS + 1 AC = 6 páginas
URLs:    /cerrajero/madrid/{cerrajero-urgente, apertura-puertas, cambio-cerraduras,
         cambio-bombines, instalacion-cerraduras-seguridad, duplicado-llaves}/
Total semana 2: 3 LBS (P1 priority de Paso-08)
Total semana 3: 2 LBS + 1 AC (resto)
Pre-requisitos: Fase 1 cerrada, GeoHub publicado, QA Pass por URL.
```

### 10.6 — Fase 3 — Main City Semantic Expansion (Semanas 4-6)

```text
Páginas: 15 GAs (G × S = 3 × 5)
URLs:    /madrid/{15 topics validados con keyword research}
Total semana 4: 5 GAs (los principales por intent)
Total semana 5: 5 GAs
Total semana 6: 5 GAs
Pre-requisitos: todas las LBS publicadas (Fase 2 cerrada), GeoHub funcional.
```

### 10.7 — Fase 4 — Optimization Loop (Semanas 6+)

```text
Acciones continuas:
- Revisión semanal de GSC (impressions, clicks, CTR, posición)
- Revisión semanal de GA4 (sessions, conversiones, funnels)
- Refresh trimestral de FAQs y schema según queries reales
- Actualización de internal links según comportamiento
- Identificación de nuevos GeoArticles según búsquedas long-tail emergentes
Pre-requisitos: tracking configurado y datos mínimos (≥30 días post-publicación).
```

### 10.8 — Fase 5 — GBP Creation & Website Alignment (Semanas 7-8)

```text
Acciones:
1. Crear GBP usando web como fuente de verdad (NAP, categorías, servicios)
2. Confirmar Primary Category Cerrajero
3. Añadir Additional Categories: Servicio de duplicado de llaves
4. Conectar URL principal: https://www.cerrajerosmadrid24h.com (Homepage)
5. Listar servicios desde LBS publicadas
6. Subir fotos (instalaciones, equipo, trabajos)
7. Schema sameAs: enlazar HP → GBP (URL post-creación)
8. Solicitar reseñas verificadas reales (no fake)
9. Validar NAP consistency entre web y GBP
10. Sincronizar trust signals
Pre-requisitos: Fases 1-3 publicadas y validadas; datos de GSC mínimos.
```

### 10.9 — Calendario semanal de publicación

| Semana | Fase | Páginas | Detalle (URLs concretas) |
|---|---|---|---|
| 1 | Entity | 5 | `/`, `/cerrajero/cerrajero-urgente/`, `/cerrajero/apertura-puertas/`, `/cerrajero/cambio-cerraduras/`, `/cerrajero/cambio-bombines/` (HP + SO-1..4) |
| 2 | Entity → Conversion | 5 | `/cerrajero/instalacion-cerraduras-seguridad/` (SO-5), `/madrid/` (GH), `/cerrajero/madrid/cerrajero-urgente/` (LBS-1), `/cerrajero/madrid/apertura-puertas/` (LBS-2), `/cerrajero/madrid/cambio-cerraduras/` (LBS-3) |
| 3 | Conversion | 5 | `/cerrajero/madrid/cambio-bombines/` (LBS-4), `/cerrajero/madrid/instalacion-cerraduras-seguridad/` (LBS-5), `/cerrajero/madrid/duplicado-llaves/` (AC-1), QA por lote, buffer |
| 4 | Semantic | 5 | 5 GAs principales (P2) — los de mayor Search Intent |
| 5 | Semantic | 5 | 5 GAs (P2-P3) |
| 6 | Semantic + arranque Optimization | 5 | 5 GAs long-tail |
| 7-8 | GBP Creation | — | Crear GBP + sincronizar (no nuevas páginas) |
| 9+ | Optimization Loop | — | Iteración continua basada en datos |

> **Validación de dependencias por semana** (cumple Regla 6 + matriz §6.10):
> - **Semana 2** publica LBS-1, LBS-2, LBS-3 — sus parent SO-1, SO-2, SO-3 ya están publicados en Semana 1 ✓. Publica también GeoHub (parent = HP, ya en Semana 1 ✓) y SO-5.
> - **Semana 3** publica LBS-4 (parent SO-4 en Semana 1 ✓), LBS-5 (parent SO-5 en Semana 2 ✓), AC-1 (parent GH en Semana 2 ✓).
> - **Semanas 4-6** publican los 15 GAs — todos sus parents LBS están publicados en Semanas 2-3 ✓.

### 10.10 — Matriz de dependencias de publicación

| Página destino | Depende de | Bloqueo si falta |
|---|---|---|
| Service Overview | Homepage publicada | No publicar SO sin HP |
| Main City GeoHub | Homepage publicada | No publicar GH sin HP |
| Location-Based Service | HP + SO + GH publicadas | No publicar LBS sin las 3 anteriores |
| Additional Category | HP + GH + servicios relacionados | No publicar AC sin GH |
| GeoArticle | LBS matching + GH publicadas | No publicar GA sin LBS hijo |
| Expansion Page (Fase 5) | Base completa + Approved Expansion | No expandir sin aprobación |

### 10.11 — Las 10 reglas operativas

1. **Phase 1 Entity:** Construir entidad y pilares antes que cualquier página local.
2. **Phase 2 Conversion:** Landings comerciales preceden a artículos.
3. **Phase 3 Semantic:** GAs requieren LBS destino y GeoHub funcional.
4. **Phase 4 Optimization:** Publicación no es final; medición + iteración continua.
5. **Phase 5 Expansion:** Solo si Approved Expansion Area aprobada y base validada.
6. **Dependencias por lote:** Cada hija requiere padre + GeoHub + targets de enlace existentes.
7. **QA por lote:** Revisar cluster como conjunto (cross-links + breadcrumbs + coherencia).
8. **Capacidad realista:** Velocidad respeta calidad y QA, no sacrificar volumen.
9. **Refresh trimestral:** Revisar artículos cada 3-6 meses con datos y nuevos enlaces.
10. **No expansión prematura:** Esperar base completa + datos + aprobación.

### 10.12 — Checklist pre-publicación (8 items)

```text
☐ 1. ¿Entidad base (HP, SO, GH) planificada primero?
☐ 2. ¿Landings de Main City van antes de artículos?
☐ 3. ¿Cada GA tiene LBS destino?
☐ 4. ¿Tracking (GSC + GA4 + Rank Tracker) configurado?
☐ 5. ¿Expansión territorial separada y con aprobación?
☐ 6. ¿Cada página tiene dependencias documentadas?
☐ 7. ¿Cada lote pasa QA (enlaces, breadcrumbs, schema)?
☐ 8. ¿Internal links mapeados antes de publicar?
```

### 10.13 — Validación Bloques 1-2 cerrados antes de arrancar Paso 10

```text
Bloque 1 (Pasos 1-3):     ✓ confirmed (43 outputs validados)
Bloque 2 (Pasos 4-7):     ✓ confirmed (59 outputs validados)
Bloque 3 Paso 8:          ✓ confirmed (14 outputs)
Bloque 3 Paso 9:          ✓ confirmed (15 outputs, 28 URLs Pass)
Total upstream:           131 outputs en confirmed.
Resultado:                Listo para arrancar Paso 10.
```

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 13 outputs que el Paso 10 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `10.4`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 10.1 | Publishing Capacity | Entero (páginas/semana) | Decisión de diseño | — |
| 10.2 | Content Team composition | Composición del team | Input humano | — |
| 10.3 | CMS + capabilities | CMS + 4 booleans + tracking stack | Input humano | — |
| 10.4 | Fase 1 — Entity Foundation | Lista de páginas + duración + pre-reqs | GMB Crush | Paso-02 2.10 + Paso-08 8.10 |
| 10.5 | Fase 2 — Main City Conversion Layer | Lista de páginas + duración + pre-reqs | GMB Crush | Paso-02 2.10 + Paso-08 8.10 |
| 10.6 | Fase 3 — Main City Semantic Expansion | Lista de páginas + duración + pre-reqs | GMB Crush | Paso-02 2.10 + Paso-08 8.10 |
| 10.7 | Fase 4 — Optimization Loop | Acciones continuas + tracking stack | GMB Crush | Paso-10 10.3 (intra-paso) |
| 10.8 | Fase 5 — GBP Creation & Website Alignment | Lista de acciones GBP + sync schema | GMB Crush | Paso-01 1.3 + Paso-14 (forward) |
| 10.9 | Calendario semanal de publicación | Tabla semana × páginas | GMB Crush | Paso-10 10.1 + 10.4-10.8 |
| 10.10 | Matriz de dependencias de publicación | Tabla destino × dependencias | GMB Crush | Paso-03 3.7 + Paso-08 8.10 |
| 10.11 | Las 10 reglas operativas | Reglas declaradas | GMB Crush | — |
| 10.12 | Checklist pre-publicación (8 items) | 8 checks binarios | GMB Crush | Paso-10 10.4-10.10 (intra-paso) |
| 10.13 | Validación Bloques 1-2 cerrados | Validation flag | GMB Crush | Bloques 1+2 + Pasos 8+9 |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 13 outputs (10.1–10.13). Cada output usa el patrón estándar: Explicación / Patrón / Ejemplos correctos / Ejemplos incorrectos / Regla / Validación / Cómo se obtiene / Output del paso. Las **5 Fases** (10.4–10.8) usan un mini-patrón adaptado: Función / Páginas / Duración / Pre-requisitos / Salida.

### 10.1 — Publishing Capacity

<small>§6.1</small>

**Explicación**

Páginas por semana que el team puede publicar **manteniendo calidad y QA**. Es la velocidad realista, no la máxima teórica. Sub-estimar deja recursos ociosos; sobre-estimar rompe el QA y la calidad.

**Patrón o fórmula**

```text
Capacity ∈ {1-3, 3-5, 5-10, 10+} páginas/semana
Criterio: composición del team × dedicación × experiencia con el cluster
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Team: 1 SEO + 1 Writer (dedicación parcial)
Capacity: 5 páginas/semana
```

**Ejemplos incorrectos**

```text
- Establecer 10 páginas/semana con 1 persona haciendo todo
- 1 página/semana con un team de 4 personas (sub-óptimo)
- No declarar capacity (planning impreciso)
```

**Regla final**

```text
Capacity es honesta y respeta calidad/QA, no es objetivo aspiracional.
```

**Validación operativa**

Aplicar al cluster. Cruzar con N total páginas (Paso-02 2.9) para estimar duración total del proyecto.

**Cómo se obtiene**

- **Fuente:** Decisión de diseño.
- **Método:** Operador declara capacity según composición del team y experiencia.

**Output del paso**

- **Tipo:** Entero (páginas/semana).
- **Ejemplo (Cerrajeros Madrid 24h):** `5 páginas/semana`.

### 10.2 — Content Team composition

<small>§6.2</small>

**Explicación**

Composición del **equipo que ejecuta** el cluster. Incluye SEO, Writer, Dev (si CMS lo necesita) y Operador del sistema (responsable del QA gate). La composición determina capacity (10.1) y cuello de botella.

**Patrón o fórmula**

```text
Team = {SEO, Writer, Dev, Operador} con porcentajes de dedicación
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 10.2.

**Ejemplos incorrectos**

```text
- Solo Writer sin SEO (briefs débiles, schema fallido)
- Solo SEO sin Writer (capacity = 0 páginas reales)
- Sin Operador del sistema (QA gate inexistente)
```

**Regla final**

```text
Mínimo team = 1 SEO + 1 Writer + 1 Operador. Dev opcional según CMS.
```

**Validación operativa**

Aplicar al cluster. Validar que cada rol está cubierto antes de arrancar Fase 1.

**Cómo se obtiene**

- **Fuente:** Input humano.
- **Método:** Cliente o operador declara composición y dedicación.

**Output del paso**

- **Tipo:** Composición team con dedicaciones.
- **Ejemplo (Cerrajeros Madrid 24h):** 1 SEO 40% + 1 Writer 60% + 1 Operador.

### 10.3 — CMS + capabilities

<small>§6.3</small>

**Explicación**

Plataforma CMS + capabilities técnicas necesarias. Schema, internal linking, reviews embedding y tracking son requisitos doctrinales. Si el CMS no los soporta, hay deuda técnica que bloquea Fases 4 y 5.

**Patrón o fórmula**

```text
CMS · Schema · Internal Linking · Reviews · Tracking stack
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 10.3.

**Ejemplos incorrectos**

```text
- CMS sin schema capability (Schema QA falla en Paso 9)
- Internal linking solo automático (rompe matriz Paso-07)
- Sin tracking (Fase 4 imposible)
```

**Regla final**

```text
CMS debe soportar schema manual + internal linking editable + reviews + tracking.
```

**Validación operativa**

Aplicar al cluster. Validar las 4 capabilities antes de arrancar Fase 1.

**Cómo se obtiene**

- **Fuente:** Input humano.
- **Método:** Cliente declara CMS y capabilities; operador valida contra los requisitos doctrinales.

**Output del paso**

- **Tipo:** CMS + 4 booleans + tracking stack.
- **Ejemplo (Cerrajeros Madrid 24h):** WordPress + 4 capabilities + GSC/GA4/Rank Tracker.

### 10.4 — Fase 1 — Entity Foundation

<small>§6.4</small>

**Explicación**

Primera fase: construir la **entidad base** del cluster. Sin esta base, las páginas locales y los artículos quedan huérfanos. Publica HP + S Service Overview + GeoHub.

**Función · Páginas · Duración · Pre-requisitos**

```text
Función:        Construir entidad y pilares temáticos
Páginas:        HP (1) + SO (S=5 en Cerrajeros) + GH (1) = 7 páginas
Duración:       2 semanas (con capacity 5/sem)
Pre-requisitos: Bloque 1 + Bloque 2 cerrados; Paso 9 QA Pass
Salida:         Entity Foundation publicada y ready para Fase 2
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 10.4.

**Ejemplos incorrectos**

```text
- Publicar LBS en Fase 1 (sin parent SO publicado)
- Saltar GeoHub para acelerar (rompe Fase 2)
- Publicar SO sin HP (rompe la cascada de autoridad)
```

**Regla operativa**

**1. Phase 1 Entity.** Construir entidad y pilares antes que cualquier página local.

**Validación operativa**

Aplicar a la primera fase. Validar que las 7 páginas están publicadas con QA Pass antes de arrancar Fase 2.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Listar las páginas que cumplen page_type ∈ {Homepage, Service Overview, GeoHub} del Paso-02 2.10.

**Output del paso**

- **Tipo:** Lista de páginas + duración + pre-reqs.
- **Ejemplo (Cerrajeros Madrid 24h):** 7 páginas (HP + 5 SO + GH) en 2 semanas.

### 10.5 — Fase 2 — Main City Conversion Layer

<small>§6.5</small>

**Explicación**

Segunda fase: publicar las **landings comerciales** que convierten búsquedas locales (LBS + AC). Son las páginas con mayor Revenue Value y Conversion Urgency (de Paso-08).

**Función · Páginas · Duración · Pre-requisitos**

```text
Función:        Capturar intención servicio+Main City; sustento Local Pack
Páginas:        S LBS (5 en Cerrajeros) + A AC (1 en Cerrajeros) = 6 páginas
Duración:       2 semanas (con capacity 5/sem; Q4 de la 3ª semana en QA + buffer)
Pre-requisitos: Fase 1 cerrada (HP + SO + GH publicadas)
Salida:         Conversion Layer publicada; URLs comerciales activas para Local Pack
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 10.5.

**Ejemplos incorrectos**

```text
- Publicar LBS antes que su SO parent (rompe matriz dependencias)
- Saltar AC si está en el inventario priorizado
- Publicar todas las LBS en una semana sin QA por lote
```

**Regla operativa**

**2. Phase 2 Conversion.** Landings comerciales de Main City preceden a artículos.

**Validación operativa**

Aplicar a la segunda fase. Validar que las 6 páginas están publicadas con QA Pass antes de arrancar Fase 3.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Listar las páginas que cumplen page_type ∈ {LBS, AC} del Paso-02 2.10, ordenadas por Priority Tier de Paso-08 8.9.

**Output del paso**

- **Tipo:** Lista de páginas + duración + pre-reqs.
- **Ejemplo (Cerrajeros Madrid 24h):** 6 páginas (5 LBS + 1 AC) en 2 semanas.

### 10.6 — Fase 3 — Main City Semantic Expansion

<small>§6.6</small>

**Explicación**

Tercera fase: publicar los **GeoArticles** que apoyan semánticamente a las LBS y al GeoHub. Son boosters semánticos, no landings comerciales — apuntan a queries long-tail informacional/comercial.

**Función · Páginas · Duración · Pre-requisitos**

```text
Función:        Reforzar landings + soporte AI Overview + long-tail
Páginas:        G × S GAs (15 en Cerrajeros)
Duración:       3 semanas (con capacity 5/sem)
Pre-requisitos: Fase 2 cerrada (LBS publicadas y QA Pass)
Salida:         Cluster semántico completo; cada GA enlaza a su LBS hijo y al GH
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 10.6.

**Ejemplos incorrectos**

```text
- Publicar GA sin LBS hijo publicada (huérfano comercial)
- Publicar GAs en Fase 1 (rompe la cascada)
- Saltar QA por lote (canibalización entre GAs no detectada)
```

**Regla operativa**

**3. Phase 3 Semantic.** GAs requieren LBS destino y soporte de GeoHub.

**Validación operativa**

Aplicar a la tercera fase. Validar que las G×S páginas están publicadas con QA Pass antes de arrancar Fase 4.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Listar las páginas que cumplen page_type = GeoArticle del Paso-02 2.10, ordenadas por Priority Tier.

**Output del paso**

- **Tipo:** Lista de páginas + duración + pre-reqs.
- **Ejemplo (Cerrajeros Madrid 24h):** 15 GAs en 3 semanas.

### 10.7 — Fase 4 — Optimization Loop

<small>§6.7</small>

**Explicación**

Cuarta fase: **medición continua + iteración**. No es publicación de páginas nuevas; es revisión de datos (GSC, GA4, Rank Tracker) para identificar qué optimizar (CTR, posición, FAQs, schema, internal links).

**Función · Páginas · Duración · Pre-requisitos**

```text
Función:        Medir + iterar contenido + schema + linking
Acciones:       Revisión GSC/GA4 semanal, refresh FAQs trimestral, internal links updates, identificar GAs nuevos según queries emergentes
Duración:       Continuo (mínimo 3-6 meses para datos significativos)
Pre-requisitos: Fases 1-3 publicadas + tracking activo (Paso-10 10.3)
Salida:         Iteración basada en datos reales; cluster en optimización continua
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 10.7.

**Ejemplos incorrectos**

```text
- Saltar Fase 4 ("ya publicamos, terminado")
- Hacer refresh sin haber instalado tracking (sin datos para iterar)
- Refresh sin criterio (cambiar por cambiar, no por GSC)
```

**Regla operativa**

**4. Phase 4 Optimization.** Publicación no es final; medición + iteración continua.

**Validación operativa**

Aplicar a partir de la 6ª semana. Validar que GSC + GA4 + Rank Tracker están reportando datos antes de iterar.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Definir cadencia (semanal/trimestral) según tracking stack del 10.3.

**Output del paso**

- **Tipo:** Acciones continuas + tracking stack.
- **Ejemplo (Cerrajeros Madrid 24h):** Revisión GSC/GA4 semanal + refresh trimestral.

### 10.8 — Fase 5 — GBP Creation & Website Alignment

<small>§6.8</small>

**Explicación**

Quinta fase: **crear el GBP y sincronizarlo con la web**. Solo se ejecuta cuando el GBP Lifecycle Status del Paso-01 1.3 = `Not Created` (web-first). En clusters con GBP existente, esta fase se reduce a sincronización.

**Función · Acciones · Duración · Pre-requisitos**

```text
Función:        Crear GBP usando web como source of truth, sincronizar señales
Acciones:       Crear GBP + confirmar Primary Cat + add Additional Cats + 
                conectar URL + listar servicios + subir fotos + sameAs schema + 
                solicitar reseñas reales + validar NAP consistency + sincronizar trust
Duración:       2 semanas (verificación GBP + sincronización schema/sameAs)
Pre-requisitos: Fases 1-3 publicadas + datos GSC mínimos
Salida:         GBP verificado, sincronizado con web, listo para Local Pack
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 10.8.

**Ejemplos incorrectos**

```text
- Crear el GBP antes de tener web base (rompe principio web-first)
- Inventar reseñas en lugar de solicitar reales
- No sincronizar sameAs (pierde señal de entidad)
- Crear GBP con categoría distinta a la Primary planificada
```

**Regla operativa**

**5. Phase 5 Expansion / GBP Creation.** Expansión solo si Approved Expansion aprobada y base validada; GBP se crea con web ya sólida.

**Validación operativa**

Aplicar tras Fase 3 cerrada. Cruce con Paso-09 9.15 (GBP Not Created Checklist desactivado tras Paso 14).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Ejecutar las 9 acciones secuenciales de creación + sincronización GBP↔web.

**Output del paso**

- **Tipo:** Lista de acciones GBP + sync schema.
- **Ejemplo (Cerrajeros Madrid 24h):** 9 acciones en 2 semanas; GBP verificado.

### 10.9 — Calendario semanal de publicación

<small>§6.9</small>

**Explicación**

Tabla operativa **semana × páginas publicadas**, derivada de las 5 fases + Capacity. Es el output que la IA o el operador usan para sincronizar trabajo del team.

**Patrón o fórmula**

```text
Tabla: filas = semanas, columnas = (Fase, Páginas, Detalle)
Total semanas = N páginas / Capacity + buffer QA (1-2 semanas)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 10.9.

**Ejemplos incorrectos**

```text
- Calendario sin holguras de QA (sobre-optimista)
- Distribuir LBS y GAs en la misma semana (rompe dependencias)
- Olvidar la semana de buffer entre Fase 2 y Fase 3
```

**Regla final**

```text
El calendario respeta las 5 fases + dependencias + capacity, con buffer QA por lote.
```

**Validación operativa**

Aplicar al cluster. Validar que la suma de páginas/semana × N semanas = total páginas SEO base (Paso-02 2.9).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Distribuir páginas de las 5 fases por semana respetando Capacity.

**Output del paso**

- **Tipo:** Tabla semana × páginas.
- **Ejemplo (Cerrajeros Madrid 24h):** 9 semanas (1-6 publicación + 7-8 GBP + 9+ Optimization Loop).

### 10.10 — Matriz de dependencias de publicación

<small>§6.10</small>

**Explicación**

Tabla **destino × dependencias** que prohíbe publicar una página si sus pre-requisitos no están publicados. Es el guard-rail que impide arquitectura desordenada.

**Patrón o fórmula**

```text
Para cada página destino:
  destino requiere {parent + GeoHub + targets de enlace publicados}
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 10.10.

**Ejemplos incorrectos**

```text
- Publicar LBS sin SO parent
- Publicar GA sin LBS hijo
- Publicar AC sin GeoHub
- Publicar Expansion sin aprobación
```

**Regla operativa**

**6. Dependencias por lote.** Cada hija requiere padre + GeoHub + targets de enlace existentes.

**Validación operativa**

Aplicar antes de publicar cada lote. Validar que las dependencias están en status `Published` (no `Draft` ni `Ready for QA`).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Cruzar Paso-03 3.7 (Parent Page por fila) + Paso-08 8.10 (Publish Phase) por URL.

**Output del paso**

- **Tipo:** Tabla destino × dependencias.
- **Ejemplo (Cerrajeros Madrid 24h):** Ver §4 sub-sección 10.10 — 6 reglas de dependencia.

### 10.11 — Las 10 reglas operativas

<small>§6.11</small>

**Explicación**

Conjunto consolidado de las **10 reglas operativas** del paso. Son los principios que rigen la producción en fases. Cada regla mapea a una validación o a una decisión del operador.

**Patrón o fórmula**

```text
1. Phase 1 Entity                   → 6.4
2. Phase 2 Conversion               → 6.5
3. Phase 3 Semantic                 → 6.6
4. Phase 4 Optimization             → 6.7
5. Phase 5 Expansion / GBP          → 6.8
6. Dependencias por lote            → 6.10
7. QA por lote                      → 6.10 + Paso-09
8. Capacidad realista               → 6.1
9. Refresh trimestral               → 6.7
10. No expansión prematura          → 6.8
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 10.11 — las 10 reglas listadas.

**Ejemplos incorrectos**

```text
- Romper Regla 6 publicando LBS sin SO
- Saltar Regla 8 forzando 10 páginas/semana sin QA
- Ignorar Regla 9 sin refresh trimestral
```

**Regla final**

```text
Las 10 reglas son no-negociables. Cualquier desviación bloquea Paso 18 (deploy).
```

**Validación operativa**

Aplicar a las 5 fases. Validar las 10 reglas como filtro de QA antes de publicar cada lote.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Doctrina del Paso 10 — declaración fija.

**Output del paso**

- **Tipo:** 10 reglas declaradas.
- **Ejemplo (Cerrajeros Madrid 24h):** Las 10 reglas aplicadas y validadas.

### 10.12 — Checklist pre-publicación (8 items)

<small>§6.12</small>

**Explicación**

8 checks binarios que **gate la entrada al Paso 10**. Si cualquiera falla, no se arranca producción. Es el contrato entre Bloques 1-2 + Pasos 8-9 y el inicio del Paso 10.

**Patrón o fórmula**

Ver §4 sub-sección 10.12.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Los 8 items en `☐ pendiente` hasta que se rellenen al cerrar Bloques 1-2 + Pasos 8-9. Una vez todos en `✓`, se arranca Fase 1.

**Ejemplos incorrectos**

```text
- Arrancar Fase 1 con check 4 (tracking) en ☐ → no podrá ejecutarse Fase 4
- Saltar el checklist por urgencia comercial
- Marcar todos en ✓ sin haber validado realmente
```

**Regla final**

```text
Cero ☐ en el checklist antes de arrancar Fase 1.
```

**Validación operativa**

Aplicar antes de la semana 1. Si algún check falla, volver al paso correspondiente.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Validar cada uno de los 8 checks contra los outputs heredados de Bloques 1-2 + Pasos 8-9.

**Output del paso**

- **Tipo:** 8 checks binarios.
- **Ejemplo (Cerrajeros Madrid 24h):** 8/8 ✓ tras cerrar Bloques 1-2 + Pasos 8-9.

### 10.13 — Validación Bloques 1-2 cerrados antes de arrancar Paso 10

<small>§6.13</small>

**Explicación**

Validación final que **bloquea el arranque del Paso 10** si Bloques 1-2 + Pasos 8-9 no están en `confirmed`. Esto garantiza que la producción arranca con base sólida y no con outputs `⚠`.

**Patrón o fórmula**

```text
Para arrancar Fase 1:
  AND(
    Bloque 1 (Pasos 1-3): 43/43 outputs confirmed,
    Bloque 2 (Pasos 4-7): 59/59 outputs confirmed,
    Paso 8: 14/14 outputs confirmed,
    Paso 9: 15/15 outputs confirmed (Final Publish Gate Pass)
  )
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 10.13.

**Ejemplos incorrectos**

```text
- Arrancar con Bloque 1 en 35/43 (8 outputs en ⚠ inferido)
- Saltar Paso 9 QA y arrancar producción directamente
- Ignorar que el Paso 8 tiene scoring incompleto
```

**Regla final**

```text
Cero outputs en ⚠ en upstream antes de arrancar Fase 1.
```

**Validación operativa**

Aplicar antes de la semana 1. Si algún output upstream está en ⚠, volver al paso correspondiente y resolverlo.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Cruzar status de cada output upstream (Bloques 1-2 + Pasos 8-9) y validar 100% en confirmed/OK.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 131 outputs upstream en confirmed; listo para arrancar.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 10 y avanzar a la ejecución de la Fase 1 (semana 1 de publicación).

### Validación de capacities y team

- ☐ Publishing Capacity declarada (10.1)
- ☐ Content Team composition completa con SEO + Writer + Operador (10.2)
- ☐ CMS + 4 capabilities + tracking stack confirmados (10.3)

### Validación de las 5 fases

- ☐ Fase 1 — Entity Foundation definida con páginas, duración y pre-reqs (10.4)
- ☐ Fase 2 — Main City Conversion Layer definida (10.5)
- ☐ Fase 3 — Main City Semantic Expansion definida (10.6)
- ☐ Fase 4 — Optimization Loop definida con tracking activo (10.7)
- ☐ Fase 5 — GBP Creation & Website Alignment definida (10.8)

### Validación de operativa

- ☐ Calendario semanal de publicación generado (10.9)
- ☐ Matriz de dependencias de publicación documentada (10.10)
- ☐ Las 10 reglas operativas aplicadas (10.11)
- ☐ Checklist pre-publicación 8/8 ✓ (10.12)

### Validación de cierre

- ☐ Bloques 1-2 + Pasos 8-9 cerrados al 100% (10.13)
- ☐ Cero outputs upstream en ⚠

## Outputs Consolidados

<small>§8</small>

> Tabla final compacta con la trazabilidad row-per-output. Los IDs (`10.1`–`10.13`) coinciden con los declarados en §5. Esta tabla es la fuente única de la trazabilidad consolidada del paso (sustituye al antiguo b-doc).

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 10.1 | — | **Publishing Capacity** = `5 páginas/semana` | Operador declara capacity según team y experiencia. **Fuente:** Decisión de diseño. | confirmed |
| 10.2 | — | **Content Team composition** = `1 SEO 40% + 1 Writer 60% + 1 Operador` | Cliente/operador declara composición. **Fuente:** Input humano. | confirmed |
| 10.3 | — | **CMS + capabilities** = `WordPress + Schema + Linking manual + Reviews + GSC/GA4/Rank Tracker` | Cliente declara CMS y capabilities; operador valida vs requisitos doctrinales. **Fuente:** Input humano. | confirmed |
| 10.4 | ← Paso-02 2.10 + Paso-08 8.10 | **Fase 1 — Entity Foundation** = `7 páginas (HP + 5 SO + GH) en 2 semanas` | Listar páginas de page_type ∈ {HP, SO, GH} del inventario. **Fuente:** GMB Crush. | confirmed |
| 10.5 | ← Paso-02 2.10 + Paso-08 8.10 | **Fase 2 — Main City Conversion Layer** = `6 páginas (5 LBS + 1 AC) en 2 semanas` | Listar páginas de page_type ∈ {LBS, AC} ordenadas por Priority Tier. **Fuente:** GMB Crush. | confirmed |
| 10.6 | ← Paso-02 2.10 + Paso-08 8.10 | **Fase 3 — Main City Semantic Expansion** = `15 GAs en 3 semanas` | Listar páginas de page_type = GeoArticle ordenadas por Priority Tier. **Fuente:** GMB Crush. | confirmed |
| 10.7 | ← 10.3 | **Fase 4 — Optimization Loop** = `Revisión GSC/GA4 semanal + refresh trimestral` | Definir cadencia de revisión según tracking stack. **Fuente:** GMB Crush. | confirmed |
| 10.8 | ← Paso-01 1.3 | **Fase 5 — GBP Creation & Website Alignment** = `9 acciones en 2 semanas; GBP verificado` | Ejecutar las 9 acciones secuenciales de creación + sincronización. **Fuente:** GMB Crush. | confirmed |
| 10.9 | ← 10.1 + 10.4-10.8 | **Calendario semanal de publicación** = `9 semanas (1-6 publicación + 7-8 GBP + 9+ Optimization)` | Distribuir páginas de las 5 fases por semana respetando Capacity. **Fuente:** GMB Crush. | confirmed |
| 10.10 | ← Paso-03 3.7 + Paso-08 8.10 | **Matriz de dependencias de publicación** = `6 reglas de dependencia documentadas` | Cruzar Parent Page (Paso-03 3.7) + Publish Phase (Paso-08 8.10) por URL. **Fuente:** GMB Crush. | confirmed |
| 10.11 | — | **Las 10 reglas operativas** = `10 reglas aplicadas` | Doctrina GMB Crush — declaración fija de los 10 principios. **Fuente:** GMB Crush. | OK |
| 10.12 | ← 10.4-10.10 | **Checklist pre-publicación (8 items)** = `8/8 ✓ tras cerrar upstream` | Validar cada check contra outputs heredados. **Fuente:** GMB Crush. | OK |
| 10.13 | ← Bloques 1+2 + Pasos 8+9 | **Validación Bloques 1-2 cerrados** = `131 outputs upstream en confirmed; listo` | Cruzar status de cada output upstream y validar 100% confirmed. **Fuente:** GMB Crush. | OK |

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
- Production Phase Framework — 5 fases doctrinales

> **Nota importante — Web-first como invariante:**
> El Paso 10 reproduce el principio web-first del sistema: la web base se publica completa antes de crear el GBP. La Fase 5 (GBP Creation) usa la web como **source of truth** — la categoría primaria, los servicios listados, las áreas servidas y el NAP del GBP se derivan de la web ya publicada y validada (Pasos 1-9). Crear el GBP antes invierte el flujo y rompe la coherencia local.
