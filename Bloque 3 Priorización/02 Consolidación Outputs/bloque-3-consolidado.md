# Consolidado del Bloque 3 — Priorización (Pasos 8-10)

> Plantilla del sistema. Documento de cierre de la Fase 1 (Ejecución) de Bloque 3. Recoge los **35 outputs** producidos por los pasos 8, 9 y 10 con sus valores reales para el cliente y su status (`confirmed` / `⚠ inferido` / `⚠ placeholder` / `validated`).
>
> Bloque 3 hereda 100% del estado de Bloques 1+2 — si esos están como `⚠`, sus consecuencias en Bloque 3 también lo estarán. El Paso 9 actúa como **gate doctrinal**: cualquier URL con Final Publish Gate fallido bloquea el avance al Paso 10 (Producción en Fases) y al Paso 18 (Deploy).

> **Tabla de pasos cubiertos:** Total **35 outputs** = 14 (Paso 8) + 8 (Paso 9) + 13 (Paso 10).

---

## Cliente

| Campo | Valor | Status |
|---|---|---|
| Business Name | `[pendiente]` | ☐ |
| Main City | `[pendiente]` | ☐ |
| GBP Lifecycle Status | `[pendiente]` | ☐ |
| Bloques 1+2 cerrados | ☐ Sí / ☐ No | ☐ |

---

## Paso 8 — Priority Score (14 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 8.1 | Priority Score Formula | `R + I + G + L + C + U` (rango 6-30) | ☐ |
| 8.2 | Revenue Value | `[pendiente]` (LBS Primary `5`, GA `3`, etc.) | ☐ |
| 8.3 | Search Intent | `[pendiente]` (LBS Primary `5`, GA informacional `2`, etc.) | ☐ |
| 8.4 | GBP Category Relevance | `[pendiente]` (LBS Primary `5`, AC `4`, etc.) | ☐ |
| 8.5 | Local Relevance | `[pendiente]` (LBS `5`, SO `3`, GH `5`, GA `5`) | ☐ |
| 8.6 | Competition Gap | `[pendiente]` (depende SERP analysis) | ☐ |
| 8.7 | Conversion Urgency | `[pendiente]` (LBS urgente `5`, planificable `3`) | ☐ |
| 8.8 | Total Score por página | `[pendiente]` (suma de los 6 factores por URL) | ☐ |
| 8.9 | Priority Tiers | `[pendiente]` (HP `P1`, LBS Primary `P1`, GA `P2-P3`) | ☐ |
| 8.10 | Publish Phase derivada | `[pendiente]` (HP `Phase 1`, LBS `Phase 1-2`, GAs `Phase 3-4`) | ☐ |
| 8.11 | Validación Landing antes que GeoArticle | `[N GAs validados; 0 violaciones]` | ☐ |
| 8.12 | Validación Homepage = P1 obligatorio | `HP en P1 + Phase 1` | ☐ |
| 8.13 | Validación LCAs sin score | `[N LCAs; 0 filas en inventario priorizado]` | ☐ |
| 8.14 | Inventario priorizado completo | `[N+1 URLs priorizadas con score+tier+phase]` | ☐ |

---

## Paso 9 — QA Checklist (15 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 9.1 | Plantilla de QA por página | `Formulario 10 campos × N URLs` | ☐ |
| 9.2 | QA Estructural (URL + Page Type + One Service + One City) | `[N/N URLs Pass]` (4 sub-checks) | ☐ |
| 9.3 | QA Local (Local Coverage + No Fake Location + areaServed) | `[URLs locales/URLs locales Pass]` (3 sub-checks) | ☐ |
| 9.4 | QA Contenido (Metadata + Word Count + Schema) | `[N/N URLs Pass]` (3 sub-checks) | ☐ |
| 9.5 | QA Conexión (Internal Links + Breadcrumbs + CTA) | `[N/N URLs Pass]` (3 sub-checks) | ☐ |
| 9.6 | QA Semántico (Canibalización) | `[0 pares solapados]` (1 sub-check) | ☐ |
| 9.7 | Final Publish Gate | `[N URLs aprobadas, M bloqueadas]` | ☐ |
| 9.8 | GBP Not Created QA Checklist | `[N URLs validadas, 0 violaciones]` | ☐ |

---

## Paso 10 — Producción en Fases (13 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 10.1 | Publishing Capacity | `[pendiente]` (páginas/semana) | ☐ |
| 10.2 | Content Team composition | `[pendiente]` (SEO + Writer + Operador + Dev opcional) | ☐ |
| 10.3 | CMS + capabilities | `[pendiente]` (CMS + 4 capabilities + tracking stack) | ☐ |
| 10.4 | Fase 1 — Entity Foundation | `[HP + S SO + GH = 1+S+1 páginas en 2 semanas]` | ☐ |
| 10.5 | Fase 2 — Main City Conversion Layer | `[S LBS + A AC = S+A páginas en 2 semanas]` | ☐ |
| 10.6 | Fase 3 — Main City Semantic Expansion | `[G×S GAs en 3 semanas]` | ☐ |
| 10.7 | Fase 4 — Optimization Loop | `Revisión GSC/GA4 semanal + refresh trimestral` | ☐ |
| 10.8 | Fase 5 — GBP Creation & Website Alignment | `9 acciones en 2 semanas; GBP verificado` | ☐ |
| 10.9 | Calendario semanal de publicación | `[pendiente]` (tabla semana × páginas) | ☐ |
| 10.10 | Matriz de dependencias de publicación | `6 reglas de dependencia documentadas` | ☐ |
| 10.11 | Las 10 reglas operativas | `10 reglas aplicadas` | ☐ |
| 10.12 | Checklist pre-publicación (8 items) | `8/8 ✓ tras cerrar upstream` | ☐ |
| 10.13 | Validación Bloques 1-2 cerrados | `[101 outputs upstream en confirmed]` | ☐ |

---

## Resumen de status

| Status | Cantidad | % |
|---|---:|---:|
| ☐ pendiente | 35 | 100% |
| ✓ confirmed | 0 | 0% |
| ⚠ inferido | 0 | 0% |
| ⚠ placeholder | 0 | 0% |
| **Total** | **35** | **100%** |

> Actualizar esta tabla al cerrar la Fase 1 de Bloque 3 con los conteos reales del cliente.

---

## Acciones pendientes para promover ☐ → confirmed / validated

> Si Bloques 1+2 no están cerrados, todas las acciones de Bloques 1+2 son pre-requisito antes de cualquier acción de Bloque 3.

### Bloque A — Keyword research (resuelve 2 outputs)

> **Tool:** Ahrefs / Semrush / Google KP.

| ID | Output | Acción |
|---|---|---|
| 8.3 | Search Intent por URL | Extraer queries de cada URL; calcular % transaccional |
| 8.6 | Competition Gap (parcial) | DR/UR del top 10 SERP por keyword principal |

### Bloque B — Local Pack analysis (resuelve 1 output)

> **Tool:** Google Maps en clean session.

| ID | Output | Acción |
|---|---|---|
| 8.4 | GBP Category Relevance por URL | Validar categorías del top 5 perfiles para cada combinación servicio + Main City |

### Bloque C — SERP analysis manual (resuelve 1 output)

> **Tool:** Google + Ahrefs/Semrush para fortaleza del top 10.

| ID | Output | Acción |
|---|---|---|
| 8.6 | Competition Gap | Analizar top 10 manualmente: contar LBS dedicadas vs directorios; mapear a escala 1-5 |

### Bloque D — Cliente confirma (resuelve 4 outputs)

| ID | Output | Acción |
|---|---|---|
| 8.2 | Revenue Value | Cliente confirma ticket medio + margen por servicio (Paso-01 1.9) |
| 10.2 | Content Team | Cliente declara composición real |
| 10.3 | CMS + capabilities | Cliente declara CMS + valida 4 capabilities + tracking stack |
| (general) | Calidad upstream | Cliente confirma datos críticos del NAP, dominio, oferta servicios |

### Bloque E — Decisiones del operador (resuelve 3 outputs)

| ID | Output | Acción |
|---|---|---|
| 10.1 | Publishing Capacity | Operador declara capacity realista (1-3 / 3-5 / 5-10 páginas/semana) |
| 10.7 | Optimization Loop cadence | Operador define cadencia revisión semanal/trimestral |
| 8.7 | Conversion Urgency | Operador clasifica servicios por ventana de decisión típica |

### Bloque F — Cascada automática (resuelve 31 outputs)

> Outputs deterministas que se cierran solos al aplicar la doctrina sobre los outputs heredados de Bloques 1-2 + Bloques A-E. No requieren input externo adicional.

- Paso 8: 8.1, 8.5, 8.8-8.14 (9 outputs)
- Paso 9: 9.1-9.8 completo (8 outputs con 13 sub-checks — los QA pasan al aplicar las reglas; las violaciones se identifican y se corrigen)
- Paso 10: 10.4-10.6, 10.8-10.13 (9 outputs deterministas tras 10.1-10.3 confirmados)

> Total automático: 26 outputs (algunos del Paso 9 pueden detectar violaciones; en ese caso pasan a `Needs Revision`). Resto: 9 outputs requieren acción humana (Bloques A-E).

---

## Bloqueo de publicación

> Por la regla del sistema, este documento NO puede pasar a Paso 18 (QA y deploy) mientras existan marcadores `⚠` o `☐ pendiente`. Adicionalmente, **el Paso 9 actúa como gate doctrinal**: cualquier URL con Final Publish Gate fallido bloquea el avance al Paso 10.

**Pre-requisitos antes de cerrar Bloque 3:**

- ☐ Bloques 1+2 cerrados (101 outputs upstream en confirmed)
- ☐ Bloque A resuelto (Keyword research ejecutado para outputs 8.3, 8.6)
- ☐ Bloque B resuelto (Local Pack analysis para output 8.4)
- ☐ Bloque C resuelto (SERP analysis para output 8.6)
- ☐ Bloque D resuelto (Cliente confirma Revenue / Team / CMS)
- ☐ Bloque E resuelto (Decisiones del operador: Capacity, Cadence, Urgency thresholds)
- ☐ Paso 8 cerrado (inventario priorizado con score + tier + phase)
- ☐ Paso 9 cerrado (Final Publish Gate Pass en N/N URLs)
- ☐ Paso 10 cerrado (Calendario semanal + Matriz dependencias listas)

---

> **Cruce con el plan de ejecución:** este consolidado es el **output** de ejecutar `00a-plan-ejecucion-bloque-3.md`. Los IDs (8.X, 9.X, 10.X) coinciden 1:1 con los del plan.
>
> **Cascada hacia Paso 14 (forward):** la Fase 5 GBP Creation (output 10.8) marca el inicio del Paso 14 — crear el GBP usando la web ya publicada como source of truth. El GBP Not Created QA Checklist (output 9.8) se desactiva tras Paso 14.
