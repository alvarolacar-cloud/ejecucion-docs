# Consolidado del Bloque 2 — Arquitectura (Pasos 4-7)

> Plantilla del sistema. Documento de cierre de la Fase 1 (Ejecución) de Bloque 2. Recoge los **59 outputs** producidos por los pasos 4, 5, 6 y 7 con sus valores reales para el cliente y su status (`confirmed` / `⚠ inferido` / `⚠ placeholder` / `validated`).
>
> Bloque 2 hereda 100% del estado de Bloque 1 (outputs 1.X, 2.X, 3.X) — si esos están como `⚠`, sus consecuencias en Bloque 2 también lo estarán hasta que se promuevan.

> **Nota:** este doc tiene 4 tablas (no 3) porque Bloque 2 cubre 4 pasos: 4, 5, 6 y 7. Total **59 outputs** = 15 (Paso 4) + 12 (Paso 5) + 17 (Paso 6) + 15 (Paso 7).

---

## Cliente

| Campo | Valor | Status |
|---|---|---|
| Business Name | `[pendiente]` | ☐ |
| Main City | `[pendiente]` | ☐ |
| Categoría primaria | `[pendiente]` | ☐ |
| Bloque 1 cerrado | ☐ Sí / ☐ No | ☐ |

---

## Paso 4 — URL Rules (15 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 4.1 | Canonical Domain | `[pendiente]` | ☐ |
| 4.2 | Trailing Slash | `[pendiente]` (Yes/No) | ☐ |
| 4.3 | Homepage URL | `/` | ☐ |
| 4.4 | Service Overview URL pattern | `/[primary-cat-slug]/[service-slug]/` → S URLs SO | ☐ |
| 4.5 | Main City GeoHub URL Style | `[pendiente]` (Option A/B) | ☐ |
| 4.6 | LBS URL pattern | `/[primary-cat-slug]/[main-city-slug]/[service-slug]/` → S URLs LBS | ☐ |
| 4.7 | Additional Category URL pattern | `/[primary-cat-slug]/[main-city-slug]/[additional-slug]/` → A URLs AC | ☐ |
| 4.8 | GeoArticle URL pattern | `/[main-city-slug]/[topic-slug]/` → G×S URLs GA | ☐ |
| 4.9 | LCAs no generan URLs | `[N LCAs declaradas → 0 URLs generadas]` | ☐ |
| 4.10 | Approved Expansion URLs | `[pendiente]` (default `None in Phase 1`) | ☐ |
| 4.11 | Validación No "near me" | `[0 URLs con patrones prohibidos]` | ☐ |
| 4.12 | Validación No adjetivos vacíos | `[0 URLs con best/cheap/top-rated]` | ☐ |
| 4.13 | Validación Slugs limpios | `[Todos los slugs cumplen slugify]` | ☐ |
| 4.14 | Validación No falsa ubicación | `[Solo Main City; 0 LCAs como path]` | ☐ |
| 4.15 | Validación No duplicar intención | `[0 pares con duplicación detectada]` | ☐ |

---

## Paso 5 — Page Type Rules (12 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 5.1 | Primary Service | `[pendiente]` | ☐ |
| 5.2 | Brand tone | `[pendiente]` (Professional / Friendly / Premium / Urgente / Local) | ☐ |
| 5.3 | Spec Homepage | 9 sub-outputs aplicados a `/` | ☐ |
| 5.4 | Spec Service Overview | 9 sub-outputs × S instancias (`/[cat]/{service}/`) | ☐ |
| 5.5 | Spec LBS | 9 sub-outputs × S instancias (`/[cat]/[city]/{service}/`) | ☐ |
| 5.6 | Spec Additional Category | 9 sub-outputs × A instancias (`/[cat]/[city]/[additional]/`) | ☐ |
| 5.7 | Spec GeoHub | 9 sub-outputs × 1 instancia (`/[city]/`) | ☐ |
| 5.8 | Spec GeoArticle | 9 sub-outputs × G×S instancias (`/[city]/{topic}/`) | ☐ |
| 5.9 | Validación Schema por tipo | `[6 page types con schema diferenciado]` | ☐ |
| 5.10 | Validación Word count por intención | `[Rangos doctrinales aplicados a 6 page types]` | ☐ |
| 5.11 | Validación CTA adaptado al page type | `[CTAs diferenciados por funnel position]` | ☐ |
| 5.12 | Validación No false location claims | `[0 afirmaciones de oficina en LCAs]` | ☐ |

---

## Paso 6 — Estructura de Contenido + LCAs (17 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 6.1 | Principio 1 — Main City crea arquitectura | `[Main City única del cluster]` | ☐ |
| 6.2 | Principio 2 — LCAs enriquecen contenido | `[N LCAs en contenido + areaServed; 0 URLs /{lca}/]` | ☐ |
| 6.3 | Principio 3 — AEAs crean URLs solo si se aprueban | `[E=0 → 0 URLs de expansión]` | ☐ |
| 6.4 | Principio 4 — Mencionar zona ≠ crear página | `[LCA mencionada en LBS sin enlace a /{lca}/]` | ☐ |
| 6.5 | Principio 5 — No falsa ubicación | `[NAP único; 0 oficinas en LCAs]` | ☐ |
| 6.6 | Homepage Content Architecture | `1 URL (/) con 11 bloques` | ☐ |
| 6.7 | Service Overview Content Architecture | `S URLs SO con 11 bloques cada una` | ☐ |
| 6.8 | LBS Content Architecture | `S URLs LBS con 12 bloques cada una` | ☐ |
| 6.9 | Additional Category Content Architecture | `A URLs AC con 11 bloques cada una` | ☐ |
| 6.10 | GeoHub Content Architecture | `1 URL ([city]/) con 10 bloques` | ☐ |
| 6.11 | GeoArticle Content Architecture | `G×S URLs GA con 10 bloques cada una` | ☐ |
| 6.12 | Tabla de uso de LCAs por page type | `Matriz 6×2 documentada` | ☐ |
| 6.13 | Ejemplo práctico completo | `Texto modelo redactado para LBS modelo` | ☐ |
| 6.14 | FAQ ejemplo | `Plantilla FAQ con cobertura natural` | ☐ |
| 6.15 | Reviews y trust blocks contextualizados | `Trust signals adaptados al funnel por page type` | ☐ |
| 6.16 | FAQs con cobertura natural | `FAQs naturales sin keyword stuffing` | ☐ |
| 6.17 | Schema `areaServed` coherente | `areaServed con Main City + N LCAs en LocalBusiness` | ☐ |

---

## Paso 7 — Internal Linking Rules (15 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 7.1 | Regla 1 — Enlazar arriba/abajo/lateral | `Aplicada a las 28 URLs (cada una con 3 direcciones)` | ☐ |
| 7.2 | Regla 2 — Homepage distribuye autoridad | `[N] outbound desde / (S SO + 1 GeoHub + A AC + 1 contacto)` | ☐ |
| 7.3 | Regla 3 — SO empuja versión local | `S conexiones SO → LBS` | ☐ |
| 7.4 | Regla 4 — GeoHub organiza Main City | `[N] outbound desde /[city]/ (S LBS + A AC + G×S GAs)` | ☐ |
| 7.5 | Regla 5 — LBS conecta servicio y ciudad | `~30-35 enlaces (6-7 por LBS × S)` | ☐ |
| 7.6 | Regla 6 — AC se integra en silo local | `3 outbound desde cada AC` | ☐ |
| 7.7 | Regla 7 — GeoArticle pasa relevancia a landing | `2×G×S conexiones (GA → LBS + GA → GeoHub)` | ☐ |
| 7.8 | Regla 8 — LCAs sin URL no reciben enlaces | `0 anchors a N LCAs declaradas` | ☐ |
| 7.9 | Regla 9 — Anchor text variado | `Mix 6 categorías aplicado a ~80 enlaces` | ☐ |
| 7.10 | Regla 10 — Enlaces contextuales primero | `Body links priorizados en las 28 URLs` | ☐ |
| 7.11 | Matriz de enlaces obligatorios por page type | `14 conexiones source → target documentadas` | ☐ |
| 7.12 | Ejemplo completo de enlaces para LBS modelo | `6 outbound + 6 anchors para LBS modelo` | ☐ |
| 7.13 | Breadcrumbs por page type | `6 breadcrumbs documentados (1 por page type)` | ☐ |
| 7.14 | Inbound links esperados | `0 páginas huérfanas; mínimos cumplidos por page type` | ☐ |
| 7.15 | Expansion linking separado | `E=0 en Phase 1 → no aplica sub-cluster` | ☐ |

---

## Resumen de status

| Status | Cantidad | % |
|---|---:|---:|
| ☐ pendiente | 59 | 100% |
| ✓ confirmed | 0 | 0% |
| ⚠ inferido | 0 | 0% |
| ⚠ placeholder | 0 | 0% |
| **Total** | **59** | **100%** |

> Actualizar esta tabla al cerrar la Fase 1 de Bloque 2 con los conteos reales del cliente.

---

## Acciones pendientes para promover ☐ → confirmed / validated

> Si Bloque 1 no está cerrado, todas las acciones de Bloque 1 son pre-requisito antes de cualquier acción de Bloque 2.

### Bloque A — Decisiones del operador (resuelve 3 outputs)

| ID | Output | Acción |
|---|---|---|
| 4.2 | Trailing Slash | Decidir Yes/No global del cluster (default `Yes`) |
| 4.10 | Approved Expansion URLs | Confirmar `None in Phase 1` o lista activa |
| 5.2 | Brand tone | Elegir entre las 5 opciones doctrinales según sector |

### Bloque B — Validar Primary Service con datos de búsqueda (resuelve 1 output)

| ID | Output | Acción |
|---|---|---|
| 5.1 | Primary Service | Cruzar top 5 de Paso-01 1.9 con keyword research; confirmar el de mayor volumen local |

### Bloque C — Cascada automática (resuelve 55 outputs)

> Outputs deterministas que se cierran solos al aplicar la doctrina sobre los outputs heredados de Bloque 1 + las decisiones de Bloque A. No requieren input externo adicional.

- Paso 4: 4.1, 4.3-4.9, 4.11-4.15 (12 outputs)
- Paso 5: 5.3-5.12 (10 outputs)
- Paso 6: 6.1-6.17 completo (17 outputs)
- Paso 7: 7.1-7.15 completo (15 outputs)

> Total automático: 54 outputs. Resto: 4.2 + 4.10 + 5.1 + 5.2 = 4 outputs requieren input humano.

---

## Bloqueo de publicación

> Por la regla del sistema, este documento NO puede pasar a Paso 18 (QA y deploy) mientras existan marcadores `⚠` o `☐ pendiente`. La publicación se desbloquea cuando todos los outputs de Bloque 2 estén `confirmed` o `validated`.

**Pre-requisitos antes de cerrar Bloque 2:**

- ☐ Bloque 1 cerrado (todos los outputs 1.X, 2.X, 3.X confirmed/validated)
- ☐ Bloque A resuelto (Trailing Slash, Expansion URLs, Brand tone)
- ☐ Bloque B resuelto (Primary Service validado con keyword research)
- ☐ Bloque C cerrado (los 54 outputs automáticos generados y validados)

---

> **Cruce con el plan de ejecución:** este consolidado es el **output** de ejecutar `00a-plan-ejecucion-bloque-2.md`. Los IDs (4.X, 5.X, 6.X, 7.X) coinciden 1:1 con los del plan. Para validar trazabilidad, abrir el plan correspondiente y comparar `Cómo Decidimos` con el valor producido aquí.
