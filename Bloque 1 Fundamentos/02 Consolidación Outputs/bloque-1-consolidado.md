# Consolidado del Bloque 1 — Fundamentos (Pasos 1-3)

> Plantilla del sistema. Documento de cierre de la Fase 1 (Ejecución) de Bloque 1. Recoge los **43 outputs** producidos por los pasos 1, 2 y 3 con sus valores reales para el cliente y su status (`confirmed` / `⚠ inferido` / `⚠ placeholder` / `validated`).
>
> Bloque 1 es la base del sistema — todo lo que se ejecute después (Bloque 2 y siguientes) depende de que estos 43 outputs estén cerrados y validados.

> **Tabla de pasos cubiertos:** Total **43 outputs** = 14 (Paso 1 Intake) + 15 (Paso 2 Fórmula Maestra) + 14 (Paso 3 Matriz Base).

---

## Cliente

| Campo | Valor | Status |
|---|---|---|
| Business Name | `[pendiente]` | ☐ |
| Main City | `[pendiente]` | ☐ |
| Categoría primaria | `[pendiente]` | ☐ |
| Preflight rellenado | ☐ Sí / ☐ No | ☐ |

---

## Paso 1 — Intake Form (14 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 1.1 | Business Name | `[pendiente]` | ☐ |
| 1.2 | Website URL / Canonical Domain | `[pendiente]` (HTTPS + www + trailing slash) | ☐ |
| 1.3 | GBP Lifecycle Status | `[pendiente]` (default web-first: Not Created / After website launch / Not Started / N/A) | ☐ |
| 1.4 | Full NAP (8 campos) | Name `[pendiente]` · Street `[pendiente]` · City `[pendiente]` · State `[pendiente]` · ZIP `[pendiente]` · Country `[pendiente]` · Phone `[pendiente]` · Email `[pendiente]` | ☐ |
| 1.5 | Planned Primary GBP Category | `[pendiente]` (categoría más repetida en top 5 Local Pack) | ☐ |
| 1.6 | Planned Additional GBP Categories | `[pendiente]` (clasificadas: cubiertas por core service / página propia) | ☐ |
| 1.7 | Main City | `[pendiente]` | ☐ |
| 1.8 | Physical Location City | `[pendiente]` | ☐ |
| 1.9 | Servicios principales (S=5) | `[pendiente]` (top 5 Local Pack + cliente confirma oferta) | ☐ |
| 1.10 | Direct + Candidate LCAs | Direct: `[pendiente]` · Candidate: `[pendiente]` | ☐ |
| 1.11 | Approved Expansion Areas | `[pendiente]` (default `None in Phase 1`) | ☐ |
| 1.12 | GeoArticles per Service (G) | `[pendiente]` (default `G=3`) | ☐ |
| 1.13 | Preferred CTA | `[pendiente]` (Llamar / WhatsApp / Solicitar presupuesto / Email) | ☐ |
| 1.14 | Trust Signals | `[pendiente]` (4-7 señales reales del negocio + benchmarking competidores) | ☐ |

---

## Paso 2 — Fórmula Maestra (15 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 2.1 | Planned GBP Categories Status | `[Planned hasta Paso 14]` | ☐ |
| 2.2 | Primary Category Slug | `[pendiente]` (slugify de 1.5) | ☐ |
| 2.3 | Main City Slug | `[pendiente]` (slugify de 1.7) | ☐ |
| 2.4 | Service Slugs (S=5) | `[pendiente]` (slugify × 5 core services) | ☐ |
| 2.5 | Service-to-Main-City Applicability | `[Yes / 0 exclusiones / S_efectiva = 5]` | ☐ |
| 2.6 | Variable S | `[pendiente]` | ☐ |
| 2.7 | Variable A | `[pendiente]` (Additional Categories que necesitan página propia) | ☐ |
| 2.8 | Variable G | `[3]` (default) | ☐ |
| 2.9 | Total páginas SEO base | `[pendiente]` (`1 + S + 1 + S + A + G×S`) | ☐ |
| 2.10 | Inventario por tipo de página | `[pendiente]` (Homepage=1 / SO=S / GH=1 / LBS=S / AC=A / GAs=G×S) | ☐ |
| 2.11 | Optional Expansion Formula | `[E=0 → 0 páginas (declarada para activación futura)]` | ☐ |
| 2.12 | Validación anti-duplicación | `[Cruce Additional vs core services validado]` | ☐ |
| 2.13 | Validación dependencias | `[Orden HP → SO → GH → LBS → AC → GAs validado]` | ☐ |
| 2.14 | Validación LCAs fuera fórmula | `[N LCAs declaradas → 0 páginas adicionales]` | ☐ |
| 2.15 | Validación auditabilidad del total | `[Total explicable componente a componente]` | ☐ |

---

## Paso 3 — Matriz Base (14 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 3.1 | Spreadsheet Name | `[Cliente] – GMB Crush Website Architecture` | ☐ |
| 3.2 | GeoHub URL Style | `[pendiente]` (Option A `/[city]/` o B `/[primary-cat]/[city]/`) | ☐ |
| 3.3 | Additional Category Slugs | `[pendiente]` (slugify × A categorías) | ☐ |
| 3.4 | GeoArticle Topics propuestos | `[pendiente]` (G×S topics validados con keyword research) | ☐ |
| 3.5 | URL Matrix completa | `[pendiente]` (N filas SEO + 1 auxiliar = N+1 filas) | ☐ |
| 3.6 | IDs por tipo de página | `HP, SO-1..S, GH, LBS-1..S, AC-1..A, GA-1..(G×S), AUX` | ☐ |
| 3.7 | Parent Page declarado por fila | `[Mapeo padre→hijo doctrinal aplicado]` | ☐ |
| 3.8 | Schema asignado desde matriz | `[Mapping doctrinal aplicado a N+1 filas]` | ☐ |
| 3.9 | Enlaces internos Required por fila | `[Listado contractual por page type]` | ☐ |
| 3.10 | Priority y Publish Phase por fila | `[P1-P4 + Phase 1-2 según page type]` | ☐ |
| 3.11 | Default Page Status | `Planned` (todas las filas) | ☐ |
| 3.12 | Notes estratégicas por fila | `[Decisión operador, opcional]` | ☐ |
| 3.13 | Validación LCAs sin filas base | `[0 filas extra para N LCAs]` | ☐ |
| 3.14 | Validación matriz cerrada antes de contenido | `[N+1 filas × 20 columnas = M celdas rellenas]` | ☐ |

---

## Resumen de status

| Status | Cantidad | % |
|---|---:|---:|
| ☐ pendiente | 43 | 100% |
| ✓ confirmed | 0 | 0% |
| ⚠ inferido | 0 | 0% |
| ⚠ placeholder | 0 | 0% |
| **Total** | **43** | **100%** |

> Actualizar esta tabla al cerrar la Fase 1 de Bloque 1 con los conteos reales del cliente.

---

## Acciones pendientes para promover ☐ → confirmed / validated

### Bloque A — Local Pack analysis (resuelve 5 outputs)

> **Tool:** Google Maps en clean session, sin login.

| ID | Output | Acción |
|---|---|---|
| 1.5 | Primary Category | Categoría más repetida en top 5 perfiles |
| 1.6 | Additional Categories | Categorías secundarias frecuentes; clasificar cubierta/página propia |
| 1.9 | Servicios principales (S=5) | Top 5 frecuencia × oferta real cliente |
| 1.10 | Candidate LCAs | Zonas declaradas por ≥2 competidores top |
| 1.14 | Trust Signals | Estándar sector + diferenciadores acreditables del cliente |

### Bloque B — Keyword research (resuelve 1 output)

> **Tool:** Ahrefs / Semrush / Google Keyword Planner.

| ID | Output | Acción |
|---|---|---|
| 3.4 | GeoArticle Topics | G × S topics validados con volumen + intent + dificultad en Main City |

### Bloque C — Inputs / confirmaciones del cliente (resuelve 4 outputs)

| ID | Output | Acción |
|---|---|---|
| 1.2 | Canonical Domain | Cliente confirma dominio a registrar |
| 1.4 | Phone, Email | Cliente confirma datos reales (no placeholders) |
| 1.4 (Street) | Barrio/distrito del NAP | Validar en catastro o Google Maps |
| 1.9 (oferta) | Servicios reales | Cliente confirma o ajusta el top 5 inferido |

### Bloque D — Decisiones del operador (resuelve 4 outputs)

| ID | Output | Acción |
|---|---|---|
| 1.11 | Approved Expansion Areas | Confirmar `None in Phase 1` o lista activa |
| 1.13 | Preferred CTA | Elegir entre Llamar / WhatsApp / Solicitar presupuesto / Email |
| 3.2 | GeoHub URL Style | Option A `/[city]/` (default) o B `/[primary-cat]/[city]/` |
| 3.12 | Notes estratégicas por fila | Opcional, contexto operativo por fila |

### Bloque E — Cascada automática (resuelve 29 outputs)

> Outputs deterministas que se cierran solos al aplicar la doctrina sobre los outputs de Bloques A-D + el preflight. No requieren input externo adicional.

- Paso 1: 1.1, 1.3, 1.4 (Name/City/State/ZIP/Country), 1.7, 1.8, 1.12 → 9 outputs
- Paso 2: 2.1-2.3, 2.5-2.15 → 14 outputs (deterministas tras 1.X cerrado)
- Paso 3: 3.1, 3.3, 3.5-3.11, 3.13-3.14 → 6 outputs

> Total automático: 29 outputs. Resto: 5 (Bloque A) + 1 (Bloque B) + 4 (Bloque C) + 4 (Bloque D) = 14 outputs requieren acción humana.

---

## Bloqueo de publicación

> Por la regla del sistema, este documento NO puede pasar a Paso 18 (QA y deploy) mientras existan marcadores `⚠` o `☐ pendiente`. La publicación se desbloquea cuando todos los outputs de Bloque 1 estén `confirmed` o `validated`.

**Pre-requisitos antes de cerrar Bloque 1:**

- ☐ Preflight rellenado (5 campos)
- ☐ Bloque A resuelto (Local Pack ejecutado en `Preflight 5` ciudades)
- ☐ Bloque B resuelto (Keyword research ejecutado para los G×S topics)
- ☐ Bloque C resuelto (cliente confirma dominio, phone, email, oferta)
- ☐ Bloque D resuelto (Expansion / CTA / GeoHub style / Notes)
- ☐ Bloque E cerrado (29 outputs automáticos generados y validados)

---

> **Cruce con el plan de ejecución:** este consolidado es el **output** de ejecutar `00a-plan-ejecucion-bloque-1.md`. Los IDs (1.X, 2.X, 3.X) coinciden 1:1 con los del plan. Para validar trazabilidad, abrir el plan correspondiente y comparar `Cómo Decidimos` con el valor producido aquí.
>
> **Cascada hacia Bloque 2:** todos los outputs validados aquí alimentan el Bloque 2 (Pasos 4-7). Si Bloque 1 cierra con ⚠, los 59 outputs de Bloque 2 heredan esos ⚠.
