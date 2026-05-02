# Consolidado del Bloque 4 — Automatización (Pasos 11-13)

> Plantilla del sistema. Documento de cierre de la Fase 1 (Ejecución) de Bloque 4. Recoge los **45 outputs** producidos por los pasos 11, 12 y 13 con sus valores reales para el cliente y su status (`confirmed` / `⚠ inferido` / `⚠ placeholder` / `validated`).
>
> Bloque 4 hereda 100% del estado de Bloques 1-3 — si esos están como `⚠`, sus consecuencias en Bloque 4 también lo estarán. El cierre del Bloque 4 desbloquea el Paso 14 (GBP Creation, Bloque 5+).

> **Tabla de pasos cubiertos:** Total **45 outputs** = 19 (Paso 11) + 12 (Paso 12) + 14 (Paso 13).

---

## Cliente

| Campo | Valor | Status |
|---|---|---|
| Business Name | `[pendiente]` | ☐ |
| Main City | `[pendiente]` | ☐ |
| GBP Lifecycle Status | `[pendiente]` | ☐ |
| Bloques 1-3 cerrados (137 outputs upstream) | ☐ Sí / ☐ No | ☐ |

---

## Paso 11 — Pseudocódigo del Sistema (19 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 11.1 | Función `load_inputs()` | `[dict con variables del cluster]` | ☐ |
| 11.2 | Función `normalize_slugs()` | `[dict con slugs normalizados]` | ☐ |
| 11.3 | Función `validate_categories()` | `[lista effective_additional]` (A=?) | ☐ |
| 11.4 | Función `generate_homepage()` | `[1 HP con spec 5.3]` | ☐ |
| 11.5 | Función `generate_service_overview()` | `[S SO no-locales con spec 5.4]` | ☐ |
| 11.6 | Función `generate_geohub()` | `[1 GeoHub Main City con spec 5.7]` | ☐ |
| 11.7 | Función `generate_lbs()` | `[S LBS con spec 5.5 + LCAs]` | ☐ |
| 11.8 | Función `generate_additional_category()` | `[A AC con spec 5.6]` | ☐ |
| 11.9 | Función `generate_geoarticles()` | `[G×S GAs con spec 5.8]` | ☐ |
| 11.10 | Función `inject_local_coverage()` | `[N páginas locales con LCAs en areaServed]` | ☐ |
| 11.11 | Función `generate_expansion()` | `[]` (Phase 1 default E=0) | ☐ |
| 11.12 | Función `assign_internal_links()` | `[~N enlaces según matriz 7.11]` | ☐ |
| 11.13 | Función `score_priority()` | `[N URLs con score+tier+phase]` | ☐ |
| 11.14 | Función `check_dependencies()` | `[N URLs validadas, M Blocked]` | ☐ |
| 11.15 | Función `run_qa()` | `[N URLs con publish_gate]` | ☐ |
| 11.16 | Función `output_matrices()` | `[3 matrices: URL/Schema/Link]` | ☐ |
| 11.17 | Pseudocódigo principal `main()` | `[orquestador con 16 llamadas]` | ☐ |
| 11.18 | Validación cobertura inputs heredados | `[137 outputs upstream cubiertos; 0 inputs inventados]` | ☐ |
| 11.19 | Validación secuencia respeta dependencias | `[0 inversiones de orden detectadas]` | ☐ |

---

## Paso 12 — Master Prompt (12 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 12.1 | Master Prompt principal | `[prompt 10 secciones aplicado al cluster]` | ☐ |
| 12.2 | Auxiliary Prompt URL Matrix | `[prompt aislado para URL Matrix]` | ☐ |
| 12.3 | Auxiliary Prompt Content Architecture | `[prompt aislado para Content]` | ☐ |
| 12.4 | Auxiliary Prompt GeoArticles | `[prompt aislado para GAs validados]` | ☐ |
| 12.5 | Auxiliary Prompt QA | `[prompt aislado para QA gate]` | ☐ |
| 12.6 | Estructura del prompt | `10 secciones obligatorias aplicadas` | ☐ |
| 12.7 | Web-First GBP Rule | `[activa/inactiva según GBP Status]` | ☐ |
| 12.8 | 14 reglas no-negociables | `[14/14 reglas aplicadas]` | ☐ |
| 12.9 | Inputs Validation embedded | `[8 checks pasados; 0 fails]` | ☐ |
| 12.10 | Executive Summary template | `[15 campos rellenos]` | ☐ |
| 12.11 | Validación prompt produce 7 outputs | `[7/7 outputs A-G cubiertos]` | ☐ |
| 12.12 | Validación prompt cumple web-first | `[N/N URLs Pass GBP Checklist]` | ☐ |

---

## Paso 13 — Sistema Final Operativo (14 outputs)

| ID | Output | Valor (cliente) | Status |
|---|---|---|---|
| 13.1 | SOP completo del sistema | `[documento maestro 11 secciones]` | ☐ |
| 13.2 | Resumen ejecutivo del cluster | `[15 campos rellenos]` | ☐ |
| 13.3 | Workflow detallado de los 13 pasos | `[177 outputs counted]` | ☐ |
| 13.4 | Estructura de carpetas y archivos | `[árbol filesystem documentado]` | ☐ |
| 13.5 | Inventario URL final consolidado | `[N+1 URLs con score+tier+phase+QA]` | ☐ |
| 13.6 | 15 Reglas No Negociables | `[15/15 reglas aplicadas]` | ☐ |
| 13.7 | Documentación de Cambios template | `[plantilla 6 campos]` | ☐ |
| 13.8 | Tracking Plan | `[GSC + GA4 + Rank Tracker pre-launch + GMB Grid post-Paso 14]` | ☐ |
| 13.9 | Roadmap final de publicación | `[5 fases × N semanas con pre-reqs]` | ☐ |
| 13.10 | Pre-requisitos para Paso 14 | `[7 items checklist]` | ☐ |
| 13.11 | Sistema como fuente única de verdad | `[SOP declarado source of truth]` | ☐ |
| 13.12 | Validación cluster ready for GBP | `[7 checks status]` | ☐ |
| 13.13 | Validación tracking configurado | `[3-4 tools status]` | ☐ |
| 13.14 | Cierre de Bloque 4 | `[45 outputs confirmed; Bloque 5 UNLOCKED]` | ☐ |

---

## Resumen de status

| Status | Cantidad | % |
|---|---:|---:|
| ☐ pendiente | 45 | 100% |
| ✓ confirmed | 0 | 0% |
| ⚠ inferido | 0 | 0% |
| ⚠ placeholder | 0 | 0% |
| **Total** | **45** | **100%** |

> Actualizar esta tabla al cerrar la Fase 1 de Bloque 4 con los conteos reales del cliente.

---

## Acciones pendientes para promover ☐ → confirmed / validated

> Si Bloques 1-3 no están cerrados, todas las acciones son pre-requisito antes de cualquier acción de Bloque 4.

### Bloque A — Decisiones del operador (resuelve 2 outputs)

| ID | Output | Acción |
|---|---|---|
| 13.7 | Documentación de Cambios template | Operador define formato del template (6 campos por defecto) |
| 13.8 | Tracking Plan | Operador define stack (GSC/GA4/Rank Tracker) y cadencia (semanal/trimestral) |

### Bloque B — Cascada automática (resuelve 43 outputs)

> Los 43 outputs restantes son enteramente deterministas — se derivan de los 137 outputs upstream de Bloques 1-3 + Paso 11 + Paso 12. Cero research externo, cero tools nuevos.

- Paso 11: 11.1-11.19 completos (19 outputs, derivados de Bloques 1-3, incluye 6 funciones individuales por page type)
- Paso 12: 12.1-12.12 completos (12 outputs, derivados de Bloques 1-3 + Paso 11)
- Paso 13: 13.1-13.6, 13.9-13.14 (12 outputs, derivados de Bloques 1-3 + Pasos 11-12)

> Total automático: 43 outputs. Resto: 2 outputs requieren decisión del operador (Bloque A).

---

## Bloqueo de publicación

> Por la regla del sistema, este documento NO puede pasar a Paso 14 (GBP Creation) mientras existan marcadores `⚠` o `☐ pendiente`. Adicionalmente, el output `13.10 Pre-requisitos para Paso 14` actúa como **gate doctrinal**: los 7 items deben estar en ✓ antes de arrancar el Paso 14.

**Pre-requisitos antes de cerrar Bloque 4:**

- ☐ Bloques 1-3 cerrados (137 outputs upstream en confirmed)
- ☐ Bloque A resuelto (Tracking Plan + Documentación template)
- ☐ Bloque B cerrado (43 outputs derivados confirmados)
- ☐ Paso 11 cerrado (19 outputs)
- ☐ Paso 12 cerrado (12 outputs)
- ☐ Paso 13 cerrado (14 outputs incl. SOP completo)
- ☐ Pre-requisitos para Paso 14 (7 items en `13.10`) listos para checklist post-Phase 1-3

**Pre-requisitos antes de arrancar Paso 14 (post Phase 1-3 publicadas):**

- ☐ Bloques 1-4 cerrados (177 outputs en confirmed)
- ☐ Fases 1-3 publicadas (28 URLs SEO base activas)
- ☐ Final Publish Gate Pass en N URLs
- ☐ GBP Not Created Checklist Pass en N URLs
- ☐ Tracking GSC mínimo 30 días
- ☐ NAP coherente
- ☐ Operador aprueba arranque Paso 14

---

> **Cruce con el plan de ejecución:** este consolidado es el **output** de ejecutar `00a-plan-ejecucion-bloque-4.md`. Los IDs (11.X, 12.X, 13.X) coinciden 1:1 con los del plan.
>
> **Cascada hacia Paso 14 (forward):** el cierre del Bloque 4 (output 13.14) marca el desbloqueo del Bloque 5+. El Paso 14 (GBP Creation) usa el SOP del Paso 13 como source of truth para crear el GBP coherente con la web ya publicada.
