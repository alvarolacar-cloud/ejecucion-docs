# Plan de ejecución del Bloque 3 (Pasos 8-10)

> Plantilla del sistema. Vista unificada de los **42 outputs** que producen los pasos 8, 9 y 10 cuando se ejecutan para cualquier cliente. Antes de arrancar, esta tabla muestra qué se va a producir, cómo se decide cada output y qué fuentes hacen falta. Una vez ejecutado, este mismo documento se rellena con los valores reales del cliente y su status (`confirmed` / `⚠ inferido` / `⚠ placeholder`) y se convierte en el consolidado del Bloque 3.

> **Cómo usar esta plantilla:**
> 1. Confirma que los Bloques 1 y 2 están cerrados (los 102 outputs en `confirmed`).
> 2. Rellena la sección "Cliente" si arrancas un cliente nuevo.
> 3. Lee las 3 tablas (Paso 8, 9, 10) para entender qué outputs hay que producir y de dónde viene cada uno.
> 4. Resuelve los bloqueos críticos antes de arrancar la ejecución (sección final).
> 5. Una vez ejecutado, vuelca los valores reales en las columnas o crea un consolidado paralelo en `02 Consolidación Outputs/`.

---

## Cliente

> Datos del preflight (`Bloque 0 Preflight/00preflight.md`). Si vienes de Bloques 1-2, ya están establecidos.

| Campo | Valor |
|---|---|
| 1. Nombre del negocio | `[pendiente]` |
| 2. Qué hace | `[pendiente]` |
| 3. Dirección con CP | `[pendiente]` |
| 4. Estado del GBP | `[pendiente]` |
| 5. Ciudades para análisis Local Pack | `[pendiente]` |

---

## Leyenda de la columna "Fuentes para Decidir"

### Etiquetas operativas

| Etiqueta | Significado |
|---|---|
| `← X.Y` | Hereda del output X.Y de un paso anterior |
| `Datos de búsqueda` | Keyword research / SERP analysis (Ahrefs, Semrush, Google KP) |
| `Local Pack` | Análisis competitivo en Google Maps |
| `Cliente confirma` | Input pendiente del cliente (placeholder hasta confirmación) |
| `Decisión operador` | Elección del que ejecuta el sistema |
| `Doctrina` | Default fijo de los manuales GMB Crush |

> **Nota:** Bloque 3 hereda del estado de Bloques 1 y 2 (102 outputs upstream); además requiere keyword research y Local Pack para los scores de Paso 8 (Search Intent + Competition Gap), input del cliente para capacities en Paso 10, y decisiones operativas para el calendario.

### Catálogo formal de Fuentes del sistema

| Fuente formal | Significado |
|---|---|
| `GMB Crush` | La doctrina del sistema lo dicta |
| `Input humano` | Lo declara el cliente |
| `Decisión de diseño` | Lo decide el operador |
| `Competidores` | Análisis Local Pack del top 5 |
| `Datos de búsqueda` | Keyword research + SERP analysis |
| `IA sin respaldo` | Inferencia IA sin respaldo (último recurso) |
| `GMB Crush + Competidores` | Doctrina + Local Pack |
| `GMB Crush + Datos de búsqueda` | Doctrina + keyword research |
| `GMB Crush + Input humano` | Doctrina + lo declarado por el cliente |

### Mapeo entre ambas

| Etiqueta operativa | Equivale a (Fuente formal) |
|---|---|
| `← X.Y` | (depende — hereda la Fuente del output X.Y) |
| `Datos de búsqueda` | `GMB Crush + Datos de búsqueda` |
| `Local Pack` | `GMB Crush + Competidores` |
| `Cliente confirma` | `Input humano` |
| `Decisión operador` | `Decisión de diseño` |
| `Doctrina` | `GMB Crush` |

---

## Paso 8 — Priority Score (14 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **8.1** Priority Score Formula | `Doctrina` | Fórmula maestra fija: R + I + G + L + C + U (rango 6-30) |
| **8.2** Revenue Value | `← 1.9` + `Cliente confirma` | Análisis margen + ticket por servicio + benchmark sectorial; escala 1-5 |
| **8.3** Search Intent | `← 1.9` + `Datos de búsqueda` | Keyword research; calcular % queries transaccionales; escala 1-5 |
| **8.4** GBP Category Relevance | `← 1.5 + 1.6` + `Local Pack` | Cruce categorías declaradas vs Local Pack; escala 1-5 |
| **8.5** Local Relevance | `← 1.7 + 1.8 + 1.10` | Inspección URL + schema + contenido vs NAP/Main City/LCAs; escala 1-5 |
| **8.6** Competition Gap | `← 1.7 + 1.9` + `Local Pack` + `Datos de búsqueda` | SERP analysis manual + DR/UR Ahrefs por keyword; escala 1-5 |
| **8.7** Conversion Urgency | `← 1.9 + 1.13` | Clasificación por ventana de decisión + cruce keyword urgency; escala 1-5 |
| **8.8** Total Score por página | `← 8.2-8.7` | Suma simple de los 6 factores con peso 1 |
| **8.9** Priority Tiers | `← 8.8` | Mapping doctrinal: 26-30=P1, 21-25=P2, 16-20=P3, 10-15=P4, 6-9=Hold |
| **8.10** Publish Phase derivada | `← 8.9 + 2.10` | Cruce Tier × dependencias estructurales (Paso-02 2.13) |
| **8.11** Validación Landing antes que GeoArticle | `← 3.5 + 8.10` | Validar phase(parent) < phase(GA) por fila |
| **8.12** Validación Homepage = P1 obligatorio | `Doctrina` | Forzar tier=P1 y phase=1 en la fila HP |
| **8.13** Validación LCAs sin score | `← 1.10 + 4.9` | Comprobar 0 intersecciones LCA × inventario |
| **8.14** Inventario priorizado completo | `← 3.5 + 8.8-8.10` | Generar tabla N filas con score+tier+phase por URL |

---

## Paso 9 — QA Checklist (15 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **9.1** Plantilla de QA por página | `← 8.14` | Generar formulario 10 campos por URL del inventario priorizado |
| **9.2** Regla 1 — URL QA | `← 4.3-4.8` | Comparar URL con patrón doctrinal del page type |
| **9.3** Regla 2 — Page Type QA | `← 5.3-5.8` | Comparar H1 + estructura + schema vs spec del page type |
| **9.4** Regla 3 — One Service Only | `← 1.9` | Inspeccionar H1 + body de cada URL local |
| **9.5** Regla 4 — One Main City Only | `← 1.7` | Inspeccionar H1 + breadcrumb + sección cobertura |
| **9.6** Regla 5 — Local Coverage QA | `← 1.10 + 6.2` | Inspeccionar contenido + schema vs lista LCAs aprobadas |
| **9.7** Regla 6 — No Fake Location | `← 1.8 + 4.14` | Buscar afirmaciones de ubicación; cruzar con NAP único |
| **9.8** Regla 7 — Metadata QA | `← 5.3-5.8` | Inspeccionar H1 + meta title + meta description + unicidad |
| **9.9** Regla 8 — Word Count QA | `← 5.10` | Contar palabras del cuerpo principal vs rango doctrinal |
| **9.10** Regla 9 — Schema QA | `← 5.9 + 6.17` | Validar JSON-LD + cruce con NAP/areaServed reales |
| **9.11** Regla 10 — Enlaces Internos QA | `← 7.11` | Inspeccionar enlaces vs matriz de Paso-07 + validar URLs target |
| **9.12** Regla 11 — Canibalización QA | `← 4.15` | Comparar H1 + URL + intent de N URLs entre sí |
| **9.13** Regla 12 — CTA QA | `← 1.13 + 5.11` | Inspeccionar presencia + tipo de CTA contra mapeo doctrinal |
| **9.14** Final Publish Gate | `← 9.2-9.13` | Consolidar resultado de las 12 reglas en 9 checkpoints binarios |
| **9.15** GBP Not Created QA Checklist | `← 1.3` | Inspeccionar copy + schema + footer contra los 7 checks específicos web-first |

---

## Paso 10 — Producción en Fases (13 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **10.1** Publishing Capacity | `Decisión operador` | Operador declara capacity (1-3 / 3-5 / 5-10 páginas/semana) según team |
| **10.2** Content Team composition | `Cliente confirma` | Cliente/operador declara composición SEO + Writer + Operador (+ Dev opcional) |
| **10.3** CMS + capabilities | `Cliente confirma` | Cliente declara CMS + 4 capabilities + tracking stack |
| **10.4** Fase 1 — Entity Foundation | `← 2.10 + 8.10` | Listar páginas page_type ∈ {HP, SO, GH} del inventario priorizado |
| **10.5** Fase 2 — Main City Conversion Layer | `← 2.10 + 8.10` | Listar páginas page_type ∈ {LBS, AC} ordenadas por Priority Tier |
| **10.6** Fase 3 — Main City Semantic Expansion | `← 2.10 + 8.10` | Listar páginas page_type = GeoArticle ordenadas por Priority Tier |
| **10.7** Fase 4 — Optimization Loop | `← 10.3` | Definir cadencia revisión según tracking stack |
| **10.8** Fase 5 — GBP Creation & Website Alignment | `← 1.3` | Ejecutar 9 acciones secuenciales web-first; activa solo si GBP=Not Created |
| **10.9** Calendario semanal de publicación | `← 10.1 + 10.4-10.8` | Distribuir páginas de las 5 fases por semana respetando Capacity |
| **10.10** Matriz de dependencias de publicación | `← 3.7 + 8.10` | Cruzar Parent Page + Publish Phase por URL |
| **10.11** Las 10 reglas operativas | `Doctrina` | Doctrina GMB Crush — declaración fija de los 10 principios |
| **10.12** Checklist pre-publicación (8 items) | `← 10.4-10.10` | Validar cada check contra outputs heredados |
| **10.13** Validación Bloques 1-2 cerrados antes de arrancar Paso 10 | `← Bloques 1+2 + Pasos 8+9` | Cruzar status de cada output upstream y validar 100% confirmed |

---

## Resumen — qué necesita la IA antes de ejecutar

### Inputs heredados de Bloques 1-2 (deben estar `confirmed` antes de arrancar)

- ☐ **Outputs 1.X** (Paso 1 Intake) — críticos: 1.3 (GBP status), 1.5 (Primary Cat), 1.6 (Additional Cats), 1.7 (Main City), 1.8 (Physical), 1.9 (Servicios), 1.10 (LCAs), 1.13 (CTA), 1.14 (Trust)
- ☐ **Outputs 2.X** (Paso 2 Fórmula) — críticos: 2.4 (Service Slugs), 2.7 (A), 2.9 (Total páginas), 2.10 (Inventario por tipo), 2.13 (dependencias)
- ☐ **Outputs 3.X** (Paso 3 Matriz) — críticos: 3.4 (GA Topics), 3.5 (URL Matrix), 3.7 (Parent Pages), 3.10 (Priority Phase)
- ☐ **Outputs 4.X-7.X** (Bloque 2 Arquitectura) — críticos: 4.3-4.8 (URL patterns), 4.9 (LCAs), 4.14 (no falsa ubicación), 4.15 (no duplicar), 5.3-5.8 (specs), 5.9-5.11 (validations), 6.2 (LCAs enriquecen), 6.6-6.11 (content arch), 6.17 (areaServed), 7.9 (anchors), 7.11 (matriz enlaces)

### Tools externos

- ☐ **Keyword research** (Ahrefs / Semrush / Google KP) — para outputs `8.3` Search Intent y `8.6` Competition Gap. También parcialmente `5.1` Primary Service del Bloque 2.
- ☐ **Google Maps Local Pack** — para output `8.4` GBP Category Relevance y `8.6` Competition Gap.
- ☐ **SERP analysis** — para `8.6` Competition Gap (top 10 análisis manual).

### Inputs del cliente (Paso 10)

- ☐ Composición real del team que ejecutará (output 10.2)
- ☐ CMS y sus capabilities (output 10.3): schema, internal linking, reviews, tracking
- ☐ Tracking stack disponible: GSC, GA4, Rank Tracker (output 10.3)

### Decisiones del operador (3-4 nuevas en Bloque 3)

- ☐ Publishing Capacity (output 10.1) — páginas/semana realistas
- ☐ Conversion Urgency thresholds para servicios mixtos (output 8.7)
- ☐ Refresh cadence en Fase 4 (output 10.7)
- ☐ Activación de Fase 5 expansión territorial (solo si Approved Expansion ≠ vacío)

### Defaults doctrinales (no requieren input)

- Priority Score Formula con 6 factores fijos (output 8.1)
- Priority Tiers con rangos doctrinales (output 8.9)
- Las 12 reglas QA del Paso 9 (outputs 9.2-9.13)
- Final Publish Gate con 9 checkpoints (output 9.14)
- GBP Not Created QA Checklist con 7 checks (output 9.15)
- Las 10 reglas operativas del Paso 10 (output 10.11)
- Las 5 fases doctrinales y sus dependencias (outputs 10.4-10.8)

---

## Cascada de dependencias (qué bloquea qué)

```
Bloques 1+2 cerrados (102 outputs confirmed)
    │
    ├─► Paso 8 (Priority Score)
    │       │
    │       ├── 8.2 ← 1.9 + Cliente confirma (Revenue)
    │       ├── 8.3 ← 1.9 + Keyword research (Intent)
    │       ├── 8.4 ← 1.5 + 1.6 + Local Pack (GBP Relevance)
    │       ├── 8.5 ← 1.7 + 1.8 + 1.10 (Local Relevance)
    │       ├── 8.6 ← Local Pack + Datos búsqueda (Competition)
    │       ├── 8.7 ← 1.9 + 1.13 (Urgency)
    │       └── 8.8-8.14 derivados (Score / Tiers / Phase / Inventario)
    │
    ├─► Paso 9 (QA Checklist)
    │       │
    │       ├── 9.1 ← 8.14 (plantilla por URL del inventario priorizado)
    │       ├── 9.2-9.13 las 12 reglas vs outputs upstream del cluster
    │       ├── 9.14 ← 9.2-9.13 (Final Publish Gate)
    │       └── 9.15 ← 1.3 (GBP Not Created activo solo si web-first)
    │
    └─► Paso 10 (Producción en Fases)
            │
            ├── 10.1-10.3 ← Cliente/operador (Capacity, Team, CMS)
            ├── 10.4-10.8 ← Inventario priorizado + Phase derivada
            ├── 10.9 ← 10.1 + 10.4-10.8 (calendario)
            ├── 10.10 ← 3.7 + 8.10 (matriz dependencias)
            ├── 10.11 declarada (10 reglas)
            ├── 10.12 ← 10.4-10.10 (checklist pre-publicación)
            └── 10.13 gate final: validar todo upstream
```

---

## Bloqueos antes de ejecutar

> Si alguno de estos bloqueos no se resuelve, los outputs de Bloque 3 quedarán como `⚠ inferido`. La publicación queda bloqueada por las reglas del Paso 9 (Final Publish Gate) hasta que pasen a `confirmed`.

| Bloqueo | Outputs que quedan ⚠ | Cómo se desbloquea |
|---|---|---|
| Bloques 1+2 sin cerrar | TODOS los 42 outputs de Bloque 3 | Cerrar Pasos 1-7 antes de arrancar Bloque 3 |
| Sin keyword research | 8.3 Search Intent, 8.6 Competition Gap (parcial) | Ejecutar research en Ahrefs/Semrush/Google KP por URL |
| Sin SERP analysis manual | 8.6 Competition Gap | Analizar top 10 SERPs por keyword principal |
| Sin Local Pack analysis | 8.4 GBP Category Relevance | Buscar `[categoría] [Main City]` en Google Maps |
| Sin Cliente confirma capacity | 10.1 Publishing Capacity | Operador declara capacity realista |
| Sin Cliente confirma CMS | 10.3 CMS + capabilities | Cliente declara CMS y validar 4 capabilities |
| Sin tracking configurado | 10.7 Optimization Loop | Configurar GSC + GA4 + Rank Tracker antes de Fase 1 |
| Cualquier output Paso 9 falla | Final Publish Gate bloquea Fase 1 | Volver a Paso correspondiente, fix, re-QA |

---

> **Cuándo arrancar la ejecución:** una vez Bloques 1-2 estén cerrados (102 outputs confirmed) y los tools externos preparados (keyword research listo, Local Pack ejecutado en Paso-01 reutilizado). El Paso 8 se puede ejecutar inmediatamente; el Paso 9 espera a tener URLs candidatas a publicar (en Cerrajeros: las 28 URLs del inventario); el Paso 10 cierra el Bloque y arranca la producción real (semana 1 de Fase 1).
