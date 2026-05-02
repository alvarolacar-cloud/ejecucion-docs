# Plan de ejecución del Bloque 2 (Pasos 4-7)

> Plantilla del sistema. Vista unificada de los **57 outputs** que producen los pasos 4, 5, 6 y 7 cuando se ejecutan para cualquier cliente. Antes de arrancar, esta tabla muestra qué se va a producir, cómo se decide cada output y qué fuentes hacen falta. Una vez ejecutado, este mismo documento se rellena con los valores reales del cliente y su status (confirmed / ⚠ inferido / ⚠ placeholder) y se convierte en el consolidado del Bloque 2 para ese cliente.

> **Cómo usar esta plantilla:**
> 1. Confirma que el Bloque 1 (Pasos 1-3) está cerrado — sus outputs son la fuente principal de Bloque 2.
> 2. Rellena la sección "Cliente" si arrancas un cliente nuevo (los datos ya están establecidos si vienes de Bloque 1).
> 3. Lee las 4 tablas (Paso 4, 5, 6, 7) para entender qué outputs hay que producir y de dónde viene cada uno.
> 4. Resuelve los bloqueos críticos antes de arrancar la ejecución (sección final).
> 5. Una vez ejecutado, vuelca los valores reales en las columnas o crea un consolidado paralelo en `Fase 3 - Consolidado/`.

---

## Cliente

> Datos del preflight (`Bloque 0 Preflight/00preflight.md`). Si vienes de Bloque 1, ya están establecidos. Si arrancas Bloque 2 aislado para revisión, rellena para contexto.

| Campo | Valor |
|---|---|
| 1. Nombre del negocio | `[pendiente]` |
| 2. Qué hace | `[pendiente]` |
| 3. Dirección con CP | `[pendiente]` |
| 4. Estado del GBP | `[pendiente]` |
| 5. Ciudades para análisis Local Pack | `[pendiente]` |

---

## Leyenda de la columna "Fuentes para Decidir"

### Etiquetas operativas (las que aparecen en las 4 tablas del plan)

| Etiqueta | Significado |
|---|---|
| `← X.Y` | Hereda del output X.Y de un paso anterior (Bloque 1 o intra-Bloque 2) |
| `Cliente confirma` | Input pendiente del cliente (placeholder hasta confirmación) |
| `Decisión operador` | Elección del que ejecuta el sistema |
| `Doctrina` | Default fijo de los manuales GMB Crush |

> **Nota:** Bloque 2 no usa `Preflight N`, `Local Pack` ni `Keyword research` directamente — esos se resolvieron en Bloque 1 y llegan vía heredance `← X.Y`. Bloque 2 es mayoritariamente doctrina + outputs heredados.

### Catálogo formal de Fuentes del sistema

> Vocabulario formal usado en §5 (Outputs a Conseguir) y §8 (Outputs Consolidados) de cada a-doc. Las etiquetas operativas de arriba son atajos que mapean a este catálogo.

| Fuente formal | Significado |
|---|---|
| `GMB Crush` | La doctrina del sistema lo dicta (manuales GMB Crush) |
| `Input humano` | Lo declara el cliente (preflight, intake, confirmación) |
| `Decisión de diseño` | Lo decide el operador con criterio de arquitectura |
| `Competidores` | Se extrae del análisis Local Pack del top 5 |
| `Datos de búsqueda` | Volumen / intent / dificultad obtenidos de keyword research |
| `IA sin respaldo` | Inferencia de la IA sin respaldo de doctrina, cliente o tools (último recurso) |
| `GMB Crush + Competidores` | Doctrina aplicada sobre análisis Local Pack |
| `GMB Crush + Datos de búsqueda` | Doctrina aplicada sobre keyword research |
| `GMB Crush + IA sin respaldo` | Doctrina aplicada con inferencia IA cuando faltan datos |
| `GMB Crush + Input humano` | Doctrina aplicada sobre lo declarado por el cliente |

### Mapeo entre ambas

| Etiqueta operativa | Equivale a (Fuente formal) |
|---|---|
| `← X.Y` | (depende — hereda la Fuente del output X.Y) |
| `Cliente confirma` | `Input humano` |
| `Decisión operador` | `Decisión de diseño` |
| `Doctrina` | `GMB Crush` |

---

## Paso 4 — URL Rules (15 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **4.1** Canonical Domain | `← 1.2` | Tomar el dominio del intake; doctrina dicta HTTPS + www |
| **4.2** Trailing Slash | `Decisión operador` | Decisión global (Yes/No); coherente y aplicable a todas las URLs del cluster |
| **4.3** Homepage URL | `Doctrina` | Doctrina — Homepage siempre es raíz `/` |
| **4.4** Service Overview URL pattern | `Doctrina` | Doctrina — pilar temático no geolocalizado bajo categoría primaria: `/[primary-cat-slug]/[service-slug]/` |
| **4.5** Main City GeoHub URL Style | `← 3.2` | Hereda el estilo elegido en Paso-03 3.2 (Option A `/[city]/` o B `/[primary-cat]/[city]/`) |
| **4.6** Location-Based Service URL pattern | `Doctrina` | Doctrina — converter local servicio + Main City: `/[primary-cat-slug]/[main-city-slug]/[service-slug]/` |
| **4.7** Additional Category URL pattern | `Doctrina` | Doctrina — soporte de categoría adicional GBP en Main City: `/[primary-cat-slug]/[main-city-slug]/[additional-slug]/` |
| **4.8** GeoArticle URL pattern | `Doctrina` | Doctrina — booster semántico bajo Main City: `/[main-city-slug]/[topic-slug]/` |
| **4.9** LCAs no generan URLs | `← 1.10` + `Doctrina` | Doctrina — LCAs viven en contenido y `areaServed`, no en path |
| **4.10** Approved Expansion URLs | `← 1.11` + `Decisión operador` | Decisión operador — sin expansión en Phase 1 (default vacío) |
| **4.11** Validación No "near me" | `Doctrina` | Comprobar todas las URLs del cluster contra blacklist `near-me` |
| **4.12** Validación No adjetivos vacíos | `Doctrina` | Comprobar URLs contra blacklist de adjetivos SEO vacíos (best, cheap, top-rated, etc.) |
| **4.13** Validación Slugs limpios | `← 2.2` | Comprobar slugs (lowercase, sin acentos, kebab-case) |
| **4.14** Validación No falsa ubicación | `← 1.8 + 1.11` | Comprobar que las URLs solo usan Main City o Approved Expansion como city |
| **4.15** Validación No duplicar intención | `Doctrina` | Cruzar URLs por intención (servicio + ciudad + topic) y descartar duplicados |

---

## Paso 5 — Page Type Rules (12 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **5.1** Primary Service | `← 1.9` + `Datos de búsqueda` | Top 5 servicios cruzados con keyword research; elegir el de mayor volumen local |
| **5.2** Brand tone | `Decisión operador` | Elegir entre las 5 opciones doctrinales (Professional / Friendly / Premium / Urgente / Local) según sector y comportamiento esperado |
| **5.3** Spec Homepage (Root Entity Anchor) | `← 1.1 + 1.4 + 1.13 + 1.14 + 4.3` | Aplicar la spec con inputs heredados; rellenar templates de H1/Meta con placeholders |
| **5.4** Spec Service Overview (Topical Authority Pillar) | `← 1.9 + 2.4 + 4.4` | Aplicar spec replicada a los S=5 core services; URL = `[primary-cat-slug]/[service-slug]/` |
| **5.5** Spec LBS (Main City Converter) | `← 1.9 + 1.10 + 2.4 + 4.6` | Aplicar spec replicada a S core services × Main City; schema LocalBusiness con `areaServed` = LCAs |
| **5.6** Spec Additional Category (GBP AC Support) | `← 1.6 + 3.3 + 4.7` | Aplicar spec a cada AC con página propia; URL usa slugs de Paso-03 3.3 |
| **5.7** Spec GeoHub (Main City Silo Container) | `← 1.7 + 1.10 + 2.3 + 4.5` | Aplicar spec al GeoHub Main City; listar TODAS las LCAs y enlazar a las páginas hijas |
| **5.8** Spec GeoArticle (Semantic Booster) | `← 1.7 + 3.4 + 4.8` | Aplicar spec a G×S GAs; topic slugs validados con keyword research (Paso-03 3.4) |
| **5.9** Validación Schema por tipo de página | `Doctrina` | Aplicar la regla a las 6 page types como filtro de QA |
| **5.10** Validación Word count por intención | `Doctrina` | Aplicar la regla a las 6 page types como filtro de QA (rangos doctrinales por page type) |
| **5.11** Validación CTA adaptado al page type | `← 1.13` + `Doctrina` | Mapear CTAs a page types según funnel position; el Preferred CTA es default |
| **5.12** Validación No false location claims | `← 1.8 + 1.10 + 4.14` | Validar que `address` schema = NAP físico real y `areaServed` lista solo zonas atendidas |

---

## Paso 6 — Estructura de Contenido + LCAs (17 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **6.1** Principio 1 — Main City crea arquitectura | `← 1.7` | Aplicar la regla a la arquitectura del cluster como filtro de QA |
| **6.2** Principio 2 — LCAs enriquecen contenido | `← 1.10` | Aplicar la regla a las URLs como filtro de QA (LCAs en contenido + areaServed; 0 URLs `/{lca}/`) |
| **6.3** Principio 3 — AEAs crean URLs solo si se aprueban | `← 1.11` | Aplicar la regla al inventario URL del cluster |
| **6.4** Principio 4 — Mencionar zona ≠ crear página | `Doctrina` | Aplicar la regla al contenido y enlaces de las URLs |
| **6.5** Principio 5 — No falsa ubicación | `← 1.8` | Aplicar la regla al schema, NAP y contenido de las URLs |
| **6.6** Homepage Content Architecture | `← 3.5 + 5.3` | Aplicar arquitectura de contenido doctrinal Homepage; rellenar bloques con inputs heredados |
| **6.7** Service Overview Content Architecture | `← 3.5 + 5.4` | Aplicar arquitectura de contenido doctrinal SO replicada × S=5 instancias |
| **6.8** Location-Based Service Content Architecture | `← 3.5 + 5.5` | Aplicar arquitectura de contenido doctrinal LBS replicada × S=5 instancias × Main City |
| **6.9** Additional Category Content Architecture | `← 3.5 + 5.6` | Aplicar arquitectura de contenido doctrinal AC × A instancias |
| **6.10** GeoHub Content Architecture | `← 3.5 + 5.7` | Aplicar arquitectura de contenido doctrinal GeoHub a la única instancia del cluster |
| **6.11** GeoArticle Content Architecture | `← 3.5 + 5.8` | Aplicar arquitectura de contenido doctrinal GA × G×S instancias |
| **6.12** Tabla de uso de LCAs por page type | `← 1.10` | Generar matriz fila-por-page-type indicando si usa LCAs y cómo (intro/H2/FAQ/areaServed) |
| **6.13** Ejemplo práctico completo (sección cobertura) | `Doctrina` | Redactar bloque modelo (sección Local Coverage Areas Served) aplicando la arquitectura LBS |
| **6.14** FAQ ejemplo | `Doctrina` | Redactar 4-6 FAQs modelo que mencionen LCAs naturalmente sin keyword stuffing |
| **6.15** Reviews y trust blocks contextualizados | `← 1.14` | Mapear trust signals heredados a cada page type según funnel position |
| **6.16** FAQs con cobertura natural | `Doctrina` | Validar FAQs de las URLs contra blacklist de keyword stuffing |
| **6.17** Schema `areaServed` coherente | `← 1.10` | Validar que `areaServed` del schema lista solo zonas reales (Main City + LCAs declaradas) |

---

## Paso 7 — Internal Linking Rules (15 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **7.1** Regla 1 — Enlazar arriba/abajo/lateral | `Doctrina` | Aplicar la regla a las URLs como filtro de QA (cada URL con 3 direcciones) |
| **7.2** Regla 2 — Homepage distribuye autoridad | `← 3.5` | Aplicar la regla al outbound de Homepage según matriz 7.11 |
| **7.3** Regla 3 — SO empuja versión local | `← 3.5` | Aplicar la regla a las S Service Overview según matriz 7.11 |
| **7.4** Regla 4 — GeoHub organiza Main City | `← 3.5` | Aplicar la regla al outbound del GeoHub según matriz 7.11 |
| **7.5** Regla 5 — LBS conecta servicio y ciudad | `← 3.5` | Aplicar la regla a las S LBS según matriz 7.11 (parent SO + GeoHub + lateral + GAs + contacto) |
| **7.6** Regla 6 — AC se integra en silo local | `← 3.5` | Aplicar la regla a las A AC según matriz 7.11 |
| **7.7** Regla 7 — GeoArticle pasa relevancia a landing | `← 3.5` | Aplicar la regla a los G×S GAs según matriz 7.11 |
| **7.8** Regla 8 — LCAs sin URL no reciben enlaces | `← 1.10 + 4.9` | Validar que ninguna URL del cluster enlaza a `/{lca}/` |
| **7.9** Regla 9 — Anchor text variado | `← 1.1 + 1.13` | Aplicar catálogo de anchors (branded / exact / partial / topic / generic / CTA) con distribución equilibrada |
| **7.10** Regla 10 — Enlaces contextuales primero | `Doctrina` | Aplicar la regla al placement: enlaces inline en body antes que en footer |
| **7.11** Matriz de enlaces obligatorios por page type | `← 3.5` | Generar matriz fila-por-conexión con source, target, anchor y direction |
| **7.12** Ejemplo completo de enlaces para LBS modelo | `← 3.5` | Redactar ejemplo aplicado a una LBS modelo (inbound + outbound + anchors) |
| **7.13** Breadcrumbs por page type | `← 3.5` | Aplicar jerarquía Home > [Categoría] > [Ciudad] > [Servicio] según page type |
| **7.14** Inbound links esperados (cross-cutting) | `← 3.5` | Validar que cada URL recibe el mínimo de inbound según matriz 7.11 |
| **7.15** Expansion linking separado (cross-cutting) | `← 1.11` | Aplicar la regla solo si E≥1; sub-cluster de expansion linking aislado del cluster base |

---

## Resumen — qué necesita la IA antes de ejecutar

### Inputs heredados de Bloque 1 (deben estar `confirmed` antes de arrancar)

- ☐ **Outputs 1.X** — Intake Form (los 14 outputs de Paso 1, con foco en 1.1, 1.4, 1.7, 1.8, 1.9, 1.10, 1.11, 1.13, 1.14)
- ☐ **Outputs 2.X** — Fórmula Maestra (los 15 outputs, con foco en 2.2, 2.3, 2.4)
- ☐ **Outputs 3.X** — Matriz Base (los 14 outputs, con foco en 3.2, 3.3, 3.4, 3.5)

### Decisiones del operador (3 nuevas en Bloque 2)

- ☐ Trailing Slash (output 4.2) — Yes/No global del cluster (default Yes)
- ☐ Brand tone (output 5.2) — Professional / Friendly / Premium / Urgente / Local (default según sector)
- ☐ Approved Expansion URLs (output 4.10) — confirma `None in Phase 1` o lista activa

### Defaults doctrinales (no requieren input)

- Patrones URL por page type (outputs 4.3, 4.4, 4.6, 4.7, 4.8) — fijos por doctrina
- Specs por page type con sus 9 sub-outputs (outputs 5.3-5.8) — plantillas doctrinales con placeholders
- Validaciones cross-cutting (outputs 4.11, 4.12, 4.15, 5.9, 5.10, 6.4, 6.16, 7.1, 7.10) — reglas fijas
- Content Architectures por page type (outputs 6.6-6.11) — bloques doctrinales
- Catálogo de anchors (output 7.9) — 6 categorías fijas

### Inputs externos NO requeridos

> Bloque 2 NO necesita Local Pack ni Keyword research adicionales. Esos se resolvieron en Bloque 1 (outputs 1.5, 1.6, 1.9, 1.10, 1.14, 3.4) y llegan a Bloque 2 vía heredance.

---

## Cascada de dependencias (qué bloquea qué)

```
Bloque 1 cerrado (outputs 1.X, 2.X, 3.X confirmed)
    │
    ├─► Paso 4 (URL Rules)
    │       │
    │       ├── 4.1 ← 1.2 (dominio)
    │       ├── 4.5 ← 3.2 (GeoHub style)
    │       ├── 4.13 ← 2.2 (slugs)
    │       └── 4.14 ← 1.8 + 1.11 (no falsa ubicación)
    │
    ├─► Paso 5 (Page Type Rules)
    │       │
    │       ├── 5.1 ← 1.9 + datos búsqueda (Primary Service)
    │       ├── 5.3-5.8 ← 1.X + 2.X + 4.X (specs por page type)
    │       └── 5.11 ← 1.13 (CTA por funnel)
    │
    ├─► Paso 6 (Content Architecture + LCAs)
    │       │
    │       ├── 6.1-6.5 ← 1.X (principios)
    │       ├── 6.6-6.11 ← 3.5 + 5.X (content architecture)
    │       └── 6.15 ← 1.14 (trust blocks)
    │
    └─► Paso 7 (Internal Linking)
            │
            ├── 7.2-7.7, 7.11-7.14 ← 3.5 (matriz URL)
            ├── 7.8 ← 1.10 + 4.9 (LCAs sin URL)
            ├── 7.9 ← 1.1 + 1.13 (anchors)
            └── 7.15 ← 1.11 (expansion linking)
```

---

## Bloqueos antes de ejecutar

> Si alguno de estos bloqueos no se resuelve, los outputs de Bloque 2 quedarán como `⚠ inferido`. Bloque 2 hereda directamente del estado de Bloque 1 — si Bloque 1 tiene ⚠, Bloque 2 los hereda.

| Bloqueo | Outputs que quedan ⚠ | Cómo se desbloquea |
|---|---|---|
| Bloque 1 sin cerrar | TODOS los 57 outputs de Bloque 2 | Cerrar Pasos 1-3 antes de arrancar Bloque 2 |
| Operador no decide Brand tone | 5.2 + cualquier copy generada en Paso 15 | Decisión del operador |
| Operador no decide Trailing Slash | 4.2 + todas las URLs del cluster | Decisión del operador (default Yes) |
| Operador no confirma Expansion URLs | 4.10, 7.15 | Decisión del operador (default vacío en Phase 1) |
| GeoHub URL Style sin decidir en Paso-03 3.2 | 4.5 (cascada desde 3.2) y por extensión 5.7, 6.10 | Volver a Paso-03 3.2 |
| Primary Service sin keyword research validado | 5.1 (queda inferido) | Validar volumen con keyword research o aceptar como inferido temporal |

---

> **Cuándo arrancar la ejecución:** una vez Bloque 1 esté cerrado y los outputs 1.X, 2.X, 3.X estén `confirmed` (o al menos los críticos: 1.4 NAP, 1.7 Main City, 1.9 Servicios, 1.10 LCAs, 2.2-2.4 slugs, 2.6-2.9 fórmula, 3.2 GeoHub style, 3.4 GeoArticle topics, 3.5 URL Matrix). Las 3 decisiones nuevas del operador (Trailing Slash, Brand tone, Expansion URLs) se pueden tomar en paralelo a la ejecución — la IA dejará los outputs afectados como `⚠ inferido` y se promueven a `confirmed` cuando lleguen.
