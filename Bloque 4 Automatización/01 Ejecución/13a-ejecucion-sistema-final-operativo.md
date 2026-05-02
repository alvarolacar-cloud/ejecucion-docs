Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 4 — Automatizacion/paso-13-sistema-final-operativo/`, alineado con los frameworks oficiales GMB Crush.

# Paso 13 — Sistema Final Operativo

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 14 outputs del Paso 13 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush.

# Bloque I — Introducción

## Objetivo del Paso 13

<small>§2</small>

En este paso la IA produce todos los outputs que **cierran el sistema web antes de la creación del GBP** — el SOP completo del cluster (Standard Operating Procedure), el resumen ejecutivo, el workflow detallado de los 13 pasos, el inventario URL final, las 15 reglas no-negociables, el template de documentación de cambios, el tracking plan, el roadmap final, los pre-requisitos para Paso 14 y las validaciones de cierre. Es el documento que **cierra Bloque 4** y deja el cluster listo para Paso 14 (creación efectiva del GBP).

**Outputs del paso:**

- **13.1** SOP completo del sistema — documento maestro de operación
- **13.2** Resumen ejecutivo del cluster — estado + status + métricas
- **13.3** Workflow detallado — secuencia de los 13 pasos del sistema
- **13.4** Estructura de carpetas y archivos — organización del proyecto del cliente
- **13.5** Inventario URL final consolidado — N+1 URLs con score+tier+phase+QA status
- **13.6** Reglas No Negociables del sistema (15 reglas)
- **13.7** Documentación de Cambios template — cómo registrar expansiones futuras
- **13.8** Tracking Plan — GMB Crush Grid + GSC + GA4 + Rank Tracker
- **13.9** Roadmap final de publicación — calendario consolidado
- **13.10** Pre-requisitos para Paso 14 (creación del GBP)
- **13.11** Sistema como fuente única de verdad — declaración doctrinal
- **13.12** Validación: cluster web completo y ready for GBP
- **13.13** Validación: tracking configurado pre-launch
- **13.14** Cierre de Bloque 4 = sistema operativo listo

**Errores que previene:**

- Crear el GBP sin tener web base sólida (rompe principio web-first)
- Saltar el SOP y dejar el cluster sin documento maestro
- Olvidar configurar tracking antes de publicar
- No declarar pre-requisitos del Paso 14 (creación caótica)
- Permitir cambios futuros sin documentación
- Tener fuentes de verdad múltiples y contradictorias

**Cuándo se ejecuta:** después de Pasos 11 y 12 cerrados (Pseudocódigo + Master Prompt). Es el paso final del Bloque 4 y la antesala del Paso 14 (Bloque 5+ — GBP Creation).

## Info heredada de pasos anteriores

<small>§3</small>

> El Paso 13 es **meta**: consolida TODO el sistema de Bloques 1-4. Lista resumida de los upstream:

| Bloque | Outputs heredados | Cómo se consolidan en el SOP |
|---|---|---|
| Bloque 1 (Pasos 1-3) | 1.1-3.14 (43 outputs) | Sección "Inputs y arquitectura base" del SOP |
| Bloque 2 (Pasos 4-7) | 4.1-7.15 (59 outputs) | Sección "URL rules + Page types + Content arch + Linking" del SOP |
| Bloque 3 (Pasos 8-10) | 8.1-10.13 (35 outputs) | Sección "Priority + QA + Producción en fases" del SOP |
| Bloque 4 (Paso 11-12) | 11.1-12.12 (31 outputs) | Sección "Pseudocódigo + Master Prompt" del SOP |
| GBP Lifecycle Status | Paso-01 1.3 | Determina activación de Paso 14 (forward) |

**Total upstream:** 137 outputs de Bloques 1-3 + 31 outputs de Pasos 11-12 = 168 outputs que el SOP consolida. Tras cerrar Paso 13, Bloque 4 añade sus propios 14 outputs → total sistema Bloques 1-4 = 182 outputs.

# Bloque II — Ejemplo rellenado para el Paso 13 — Sistema Final Operativo

<small>§4</small>

> Los 14 outputs del Paso 13 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 13.X declarado en §5.

### 13.1 — SOP completo del sistema

> SOP completo expandido para Cerrajeros Madrid 24h. Las 11 secciones se rellenan con los outputs de Bloques 1-4 + los outputs 13.2-13.14.

```markdown
# SOP — Cerrajeros Madrid 24h · Cluster GMB Crush

═══════════════════════════════════════════════════════════════════
SECCIÓN 1 — RESUMEN EJECUTIVO (output 13.2)
═══════════════════════════════════════════════════════════════════

Cliente:                Cerrajeros Madrid 24h
Sector:                 Cerrajería urgente
Main City:              Madrid
Categoría primaria:     Cerrajero (Planned)
GBP Status:             Not Created (web-first)
Total URLs:             29 (28 SEO base + 1 auxiliar)
Estructura:             1 HP + 5 SO + 1 GH + 5 LBS + 1 AC + 15 GA + 1 AUX
LCAs:                   10 (2 Direct + 8 Candidate)
Variables:              S=5, A=1, G=3, E=0
Bloques 1-3 status:     confirmed (137 outputs)
Bloque 4 status:        confirmed (45 outputs Pasos 11-13)
Total outputs upstream: 182
QA Gate:                Pass (28/28 URLs)
Phase actual:           Pre-Phase 1 (listos para arrancar)
Tracking:               GSC + GA4 + Rank Tracker (Ahrefs) configurado
Generado:               2026-04-30

═══════════════════════════════════════════════════════════════════
SECCIÓN 2 — WORKFLOW DETALLADO DE LOS 13 PASOS (output 13.3)
═══════════════════════════════════════════════════════════════════

Bloque 1 — Fundamentos (43 outputs):
  Paso 1: Intake Form          → 14 outputs (1.1-1.14)
    · Business Name, Website, GBP Status, Full NAP (8 campos)
    · Primary GBP Category, Additional Categories
    · Main City, Physical Location City, Servicios principales (S=5)
    · Direct + Candidate LCAs, Approved Expansion (E=0)
    · GeoArticles per Service (G=3), Preferred CTA, Trust Signals
  Paso 2: Fórmula Maestra      → 15 outputs (2.1-2.15)
    · Slugs limpios + S_efectiva + Variable A + Total páginas (28)
    · Inventario por tipo + 4 validaciones doctrinales
  Paso 3: Matriz Base           → 14 outputs (3.1-3.14)
    · Spreadsheet Name + GeoHub URL Style (Option A `/madrid/`)
    · URL Matrix completa (29 filas) + Schema Map + Parents
    · GeoArticle Topics (15 validados con keyword research)

Bloque 2 — Arquitectura (59 outputs):
  Paso 4: URL Rules             → 15 outputs (4.1-4.15)
  Paso 5: Page Type Rules       → 12 outputs (5.1-5.12)
  Paso 6: Content + LCAs        → 17 outputs (6.1-6.17)
  Paso 7: Internal Linking      → 15 outputs (7.1-7.15)

Bloque 3 — Priorización (35 outputs):
  Paso 8: Priority Score        → 14 outputs (8.1-8.14)
  Paso 9: QA Checklist          → 8 outputs (9.1-9.8)
  Paso 10: Producción en Fases  → 13 outputs (10.1-10.13)

Bloque 4 — Automatización (45 outputs):
  Paso 11: Pseudocódigo         → 19 outputs (11.1-11.19)
  Paso 12: Master Prompt        → 12 outputs (12.1-12.12)
  Paso 13: Sistema Final Operativo → 14 outputs (13.1-13.14)

Bloque 5+ — Salida a Mercado (forward):
  Paso 14: GBP Creation
  Paso 15: Redacción
  Paso 18: Deploy
  Pasos 16, 17, 19+: optimización post-launch

═══════════════════════════════════════════════════════════════════
SECCIÓN 3 — ESTRUCTURA DE CARPETAS Y ARCHIVOS (output 13.4)
═══════════════════════════════════════════════════════════════════

ejecución/
├── 00 convenciones/
│   ├── 00-esqueleto-paso-a.md           (esqueleto canónico)
│   ├── 00convenciones-ejecucion.md      (convenciones generales)
│   └── _autocheck_paso.py               (validador automatizado)
├── Bloque 0 Preflight/
│   └── 00preflight.md                   (5 campos del cliente)
├── Bloque 1 Fundamentos/
│   ├── 01 Ejecución/
│   │   ├── 00a-plan-ejecucion-bloque-1.md
│   │   ├── 01a-ejecucion-intake-form.md
│   │   ├── 02a-ejecucion-formula-maestra-arquitectura.md
│   │   └── 03a-ejecucion-matriz-base.md
│   └── 02 Consolidación Outputs/
│       └── bloque-1-consolidado.md
├── Bloque 2 Arquitectura/
│   ├── 01 Ejecución/
│   │   ├── 00a-plan-ejecucion-bloque-2.md
│   │   ├── 04a-ejecucion-url-rules.md
│   │   ├── 05a-ejecucion-page-type-rules.md
│   │   ├── 06a-ejecucion-estructura-contenido-areas-cobertura-local.md
│   │   └── 07a-ejecucion-internal-linking-rules.md
│   └── 02 Consolidación Outputs/
│       └── bloque-2-consolidado.md
├── Bloque 3 Priorización/
│   ├── 01 Ejecución/
│   │   ├── 00a-plan-ejecucion-bloque-3.md
│   │   ├── 08a-ejecucion-priority-score.md
│   │   ├── 09a-ejecucion-qa-checklist.md
│   │   └── 10a-ejecucion-produccion-en-fases.md
│   └── 02 Consolidación Outputs/
│       └── bloque-3-consolidado.md
└── Bloque 4 Automatización/
    ├── 01 Ejecución/
    │   ├── 00a-plan-ejecucion-bloque-4.md
    │   ├── 11a-ejecucion-pseudocodigo-sistema.md
    │   ├── 12a-ejecucion-master-prompt.md
    │   └── 13a-ejecucion-sistema-final-operativo.md
    └── 02 Consolidación Outputs/
        └── bloque-4-consolidado.md

Convenciones de naming:
- `00a-` prefix → plantilla pre-execution del Bloque
- `NNa-` (NN=01..13) → a-doc del paso N (sistema)
- `[cliente]-bloque-N-consolidado.md` → output post-execution por cliente
- `bloque-N-consolidado.md` → plantilla genérica del consolidado del Bloque

═══════════════════════════════════════════════════════════════════
SECCIÓN 4 — INVENTARIO URL FINAL CONSOLIDADO (output 13.5)
═══════════════════════════════════════════════════════════════════

Total: 28 SEO base + 1 auxiliar = 29 URLs

| ID    | URL                                                        | Tipo                | Schema                                  | Score | Tier | Phase | QA   |
|-------|------------------------------------------------------------|---------------------|-----------------------------------------|-------|------|-------|------|
| HP    | /                                                          | Homepage            | Org+WebSite+LB+FAQ+Speakable            | 29    | P1   | 1     | Pass |
| SO-1  | /cerrajero/cerrajero-urgente/                              | Service Overview    | Service+WebPage+Bread+Speakable         | 23    | P2   | 2     | Pass |
| SO-2  | /cerrajero/apertura-puertas/                               | Service Overview    | Service+WebPage+Bread+Speakable         | 21    | P2   | 2     | Pass |
| SO-3  | /cerrajero/cambio-cerraduras/                              | Service Overview    | Service+WebPage+Bread+Speakable         | 20    | P3   | 2     | Pass |
| SO-4  | /cerrajero/cambio-bombines/                                | Service Overview    | Service+WebPage+Bread+Speakable         | 19    | P3   | 2     | Pass |
| SO-5  | /cerrajero/instalacion-cerraduras-seguridad/               | Service Overview    | Service+WebPage+Bread+Speakable         | 19    | P3   | 2     | Pass |
| GH    | /madrid/                                                   | GeoHub              | CollectionPage+Bread                    | 25    | P2   | 2     | Pass |
| LBS-1 | /cerrajero/madrid/cerrajero-urgente/                       | LBS                 | LB+Bread+FAQ+Speakable                  | 29    | P1   | 1     | Pass |
| LBS-2 | /cerrajero/madrid/apertura-puertas/                        | LBS                 | LB+Bread+FAQ+Speakable                  | 28    | P1   | 2     | Pass |
| LBS-3 | /cerrajero/madrid/cambio-cerraduras/                       | LBS                 | LB+Bread+FAQ+Speakable                  | 27    | P1   | 2     | Pass |
| LBS-4 | /cerrajero/madrid/cambio-bombines/                         | LBS                 | LB+Bread+FAQ+Speakable                  | 26    | P1   | 2     | Pass |
| LBS-5 | /cerrajero/madrid/instalacion-cerraduras-seguridad/        | LBS                 | LB+Bread+FAQ+Speakable                  | 25    | P2   | 2     | Pass |
| AC-1  | /cerrajero/madrid/duplicado-llaves/                        | Additional Cat      | Service+Bread                            | 21    | P2   | 3     | Pass |
| GA-1  | /madrid/cuanto-cuesta-un-cerrajero-urgente/                | GeoArticle          | Article+FAQ+Bread+Speakable             | 22    | P2   | 3     | Pass |
| GA-2  | /madrid/que-hacer-si-no-puedes-entrar-casa/                | GeoArticle          | Article+FAQ+Bread+Speakable             | 21    | P2   | 3     | Pass |
| GA-3  | /madrid/cuanto-tarda-un-cerrajero/                         | GeoArticle          | Article+FAQ+Bread+Speakable             | 20    | P3   | 3     | Pass |
| ...   | (15 GAs total, P2-P3, Phase 3-4)                          |                     |                                         |       |      |       |      |
| AUX   | /contacto/                                                 | Auxiliar            | ContactPoint                             | —     | —    | 1     | Pass |

Cumple Paso-02 2.9: 1 + 5 + 1 + 5 + 1 + 15 = 28 SEO base.

═══════════════════════════════════════════════════════════════════
SECCIÓN 5 — REGLAS NO NEGOCIABLES DEL SISTEMA (output 13.6)
═══════════════════════════════════════════════════════════════════

1. Una página local = 1 servicio + 1 Main City única
2. LCAs viven en contenido + areaServed; NUNCA generan URLs
3. Approved Expansion requiere aprobación explícita del operador
4. Slugs limpios: lowercase + sin acentos + kebab-case
5. Sin near-me, sin adjetivos vacíos en URLs
6. Schema válido y veraz por page type
7. Word count en rango doctrinal por page type
8. Internal links cumplen matriz Paso-07 7.11
9. Anchors variados (catálogo Paso-07 7.9)
10. Breadcrumbs jerárquicos por page type
11. CTA presente y adaptado al funnel
12. Priority Score con 6 factores (Paso-08 8.1)
13. HP siempre P1 + Phase 1
14. GAs no se publican antes que su LBS hijo (Paso-08 8.11)
15. Web-first si GBP=Not Created (no inventar señales GBP hasta Paso 14)

Las 14 primeras vienen del Paso-12 12.8. La 15ª se añade aquí: "Sistema es fuente única de verdad" (output 13.11).

═══════════════════════════════════════════════════════════════════
SECCIÓN 6 — DOCUMENTACIÓN DE CAMBIOS (output 13.7)
═══════════════════════════════════════════════════════════════════

Template para registrar cualquier cambio futuro al cluster post-deploy.

Campos obligatorios por entrada:
1. Fecha
2. Tipo: [Expansion / Refresh / Correction / GBP Update / Other]
3. Descripción: [qué cambia + URLs afectadas]
4. Outputs upstream afectados: [lista de IDs Paso-NN N.X]
5. Razón: [por qué se cambia ahora + datos que justifican]
6. Aprobado por: [Operador]
7. Validado QA: [Sí + fecha / No + razones]

Ejemplo Cerrajeros Madrid 24h:

Cambio #001 — 2026-06-15
Tipo:           Expansion
Descripción:    Aprobar Approved Expansion Area 'Toledo' tras 6 meses de datos GSC
URLs afectadas: 21 nuevas (1 GH + 5 LBS + 15 GAs en Toledo)
Outputs:        1.11 (Paso 1), 4.10 (Paso 4), 7.15 (Paso 7), 11.11 (Paso 11)
Razón:          Cliente aprueba expansión tras 6 meses con datos GSC sólidos
                en Madrid (CTR > 8%, posiciones top 3 en 12 keywords core)
Aprobado por:   Operador
Validado QA:    Sí — 2026-06-20

═══════════════════════════════════════════════════════════════════
SECCIÓN 7 — TRACKING PLAN (output 13.8)
═══════════════════════════════════════════════════════════════════

Stack:
- Google Search Console (GSC):
  · Configurar pre-Phase 1
  · Verificar dominio canonical (https://www.cerrajerosmadrid24h.com)
  · Subir sitemap.xml
  · Cadencia revisión: semanal Phase 1-3, bi-semanal Phase 4+

- Google Analytics 4 (GA4):
  · Configurar pre-Phase 1
  · Eventos de conversión: call_click, form_submit, email_click
  · Audiencias: visitors_madrid, returning_visitors, mobile_emergency
  · Cadencia revisión: semanal Phase 1-3, mensual Phase 4+

- Rank Tracker (Ahrefs):
  · Keywords core: 50+ (cerrajero urgente Madrid, cerrajero 24h Madrid, etc.)
  · Keywords LCAs: ~30 (cerrajero Almagro, cerrajero Chamberí, etc.)
  · Keywords long-tail: 15+ (cuanto cuesta cerrajero urgente Madrid, etc.)
  · Cadencia revisión: semanal Phase 1-3, bi-semanal Phase 4+

- GMB Crush Grid:
  · Pendiente Paso 14 (cuando exista el GBP)
  · Configurar tras GBP verificado
  · Geo grid 5×5 alrededor del NAP físico
  · Cadencia revisión: mensual desde Paso 14

═══════════════════════════════════════════════════════════════════
SECCIÓN 8 — ROADMAP FINAL DE PUBLICACIÓN (output 13.9)
═══════════════════════════════════════════════════════════════════

| Fase | Semanas | Páginas                          | Pre-req crítico                       |
|------|---------|----------------------------------|---------------------------------------|
| 1    | 1-2     | HP + 5 SO + GH (7)              | Bloques 1-4 cerrados; QA Gate Pass    |
| 2    | 2-3     | 5 LBS + 1 AC (6)                | Fase 1 publicada                      |
| 3    | 4-6     | 15 GAs                          | Fase 2 publicada                      |
| 4    | 6+      | (sin nuevas; iteración)         | Tracking activo, datos ≥ 30 días GSC  |
| 5    | 7-8     | (Paso 14 — creación GBP)        | Fases 1-3 publicadas + datos GSC      |

Dependencias estructurales (matriz Paso-10 10.10):
- SO requiere HP publicada
- GH requiere HP publicada
- LBS requiere HP + SO + GH publicadas
- AC requiere HP + GH publicadas
- GA requiere LBS matching + GH publicadas
- Expansion requiere base completa + Approved Expansion

═══════════════════════════════════════════════════════════════════
SECCIÓN 9 — PRE-REQUISITOS PARA PASO 14 (output 13.10)
═══════════════════════════════════════════════════════════════════

Antes de crear el GBP en Paso 14, validar los 7 pre-requisitos:

☐ 1. Bloques 1-4 cerrados al 100% (182 outputs upstream confirmed)
☐ 2. Fases 1-3 publicadas (28 URLs SEO base activas)
☐ 3. Final Publish Gate Pass en 28/28 URLs
☐ 4. GBP Not Created QA Checklist Pass en 28/28 URLs
☐ 5. Tracking configurado y reportando datos (mínimo 30 días GSC)
☐ 6. NAP coherente entre web + cualquier directorio existente
☐ 7. Decisión del operador: arrancar Paso 14 (GBP Creation)

Si cualquier pre-requisito falla, NO se arranca Paso 14.

═══════════════════════════════════════════════════════════════════
SECCIÓN 10 — SISTEMA COMO FUENTE ÚNICA DE VERDAD (output 13.11)
═══════════════════════════════════════════════════════════════════

Cualquier discrepancia entre:
- Web publicada
- GBP (cuando se cree en Paso 14)
- Materiales de marketing (folletos, ads, redes sociales)
- Comunicaciones del cliente

Se resuelve consultando este SOP + outputs upstream de Bloques 1-4.

El SOP es la SOURCE OF TRUTH del cluster. Cualquier cambio que afecte a
la arquitectura debe:
1. Registrarse en Documentación de Cambios (sección 6)
2. Actualizar el output upstream correspondiente
3. Re-correr el QA Gate (Paso-09 9.7)
4. Re-publicar el SOP con el cambio

Múltiples SOPs paralelos están prohibidos. Un cluster = un SOP.

═══════════════════════════════════════════════════════════════════
SECCIÓN 11 — VALIDACIONES DE CIERRE (outputs 13.12 + 13.13 + 13.14)
═══════════════════════════════════════════════════════════════════

Validación 1 — Cluster web ready for GBP (output 13.12):
☐ 28 SEO base URLs publicadas
☐ Final Publish Gate Pass: 28/28
☐ GBP Not Created Checklist Pass: 28/28
☐ Internal links cumplen matriz: ~80 enlaces validados
☐ Schema válido en todas las URLs
☐ NAP coherente (web + footer + schema)
☐ Roadmap Phase 1-3 ejecutado
☐ Tracking activo: GSC + GA4 + Rank Tracker

Validación 2 — Tracking configurado pre-launch (output 13.13):
☐ Google Search Console: dominio verificado, sitemap subido
☐ Google Analytics 4: eventos call/form/email configurados
☐ Rank Tracker: 50+ keywords core + LCAs + long-tail configurados
☐ GMB Crush Grid: pendiente Paso 14 (lógico)

Validación 3 — Cierre de Bloque 4 (output 13.14):
☐ Paso 11 (Pseudocódigo): 19/19 outputs confirmed
☐ Paso 12 (Master Prompt): 12/12 outputs confirmed
☐ Paso 13 (Sistema Final Operativo): 14/14 outputs confirmed
☐ Total Bloque 4: 45 outputs confirmed
☐ Total sistema (Bloques 1-4): 182 outputs confirmed
☐ Cluster Cerrajeros Madrid 24h en estado "Operativo"
→ Bloque 4 closure: COMPLETE
→ Avanzar a Bloque 5 (GBP Creation + Salida a mercado): UNLOCKED
```

### 13.2 — Resumen ejecutivo del cluster

```text
Cerrajeros Madrid 24h — SOP cluster GMB Crush
═══════════════════════════════════════════════
Cliente:                Cerrajeros Madrid 24h
Sector:                 Cerrajería urgente
Main City:              Madrid
Categoría primaria:     Cerrajero (Planned)
GBP Status:             Not Created (web-first)
Total URLs:             29 (28 SEO base + 1 auxiliar)
Estructura:             1 HP + 5 SO + 1 GH + 5 LBS + 1 AC + 15 GA + 1 AUX
LCAs:                   10 (2 Direct + 8 Candidate)
Variables:              S=5, A=1, G=3, E=0
Bloques 1-3 status:     confirmed (137 outputs)
Bloque 4 status:        confirmed (31 outputs Pasos 11-12)
Total outputs upstream: 168 (Bloques 1-3 + Pasos 11-12)
QA Gate:                Pass (28/28 URLs)
Phase actual:           Pre-Phase 1 (listos para arrancar)
Tracking:               GSC + GA4 + Rank Tracker (Ahrefs) configurado
Generado:               2026-04-30
```

### 13.3 — Workflow detallado

```text
Bloque 1 — Fundamentos:
  Paso 1: Intake Form          → 14 outputs (1.1-1.14)
  Paso 2: Fórmula Maestra      → 15 outputs (2.1-2.15)
  Paso 3: Matriz Base           → 14 outputs (3.1-3.14)

Bloque 2 — Arquitectura:
  Paso 4: URL Rules             → 15 outputs (4.1-4.15)
  Paso 5: Page Type Rules       → 12 outputs (5.1-5.12)
  Paso 6: Content + LCAs        → 17 outputs (6.1-6.17)
  Paso 7: Internal Linking      → 15 outputs (7.1-7.15)

Bloque 3 — Priorización:
  Paso 8: Priority Score        → 14 outputs (8.1-8.14)
  Paso 9: QA Checklist          → 8 outputs (9.1-9.8)
  Paso 10: Producción en Fases  → 13 outputs (10.1-10.13)

Bloque 4 — Automatización:
  Paso 11: Pseudocódigo         → 14 outputs (11.1-11.14)
  Paso 12: Master Prompt        → 12 outputs (12.1-12.12)
  Paso 13: Sistema Final Operativo → 14 outputs (13.1-13.14)

Bloque 5+ — Salida a Mercado:
  Paso 14: GBP Creation (forward)
  Paso 15: Redacción
  Paso 18: Deploy
  Pasos 16, 17, 19+: optimización post-launch
```

### 13.4 — Estructura de carpetas y archivos

```text
ejecución/
├── 00 convenciones/
├── Bloque 0 Preflight/00preflight.md
├── Bloque 1 Fundamentos/
│   ├── 01 Ejecución/{00a-plan, 01a, 02a, 03a}.md
│   └── 02 Consolidación Outputs/bloque-1-consolidado.md
├── Bloque 2 Arquitectura/
│   ├── 01 Ejecución/{00a-plan, 04a, 05a, 06a, 07a}.md
│   └── 02 Consolidación Outputs/bloque-2-consolidado.md
├── Bloque 3 Priorización/
│   ├── 01 Ejecución/{00a-plan, 08a, 09a, 10a}.md
│   └── 02 Consolidación Outputs/bloque-3-consolidado.md
└── Bloque 4 Automatización/
    ├── 01 Ejecución/{00a-plan, 11a, 12a, 13a}.md
    └── 02 Consolidación Outputs/bloque-4-consolidado.md
```

### 13.5 — Inventario URL final consolidado (Cerrajeros Madrid 24h)

| ID | URL | Page Type | Schema | Score | Tier | Phase | QA |
|---|---|---|---|---|---|---|---|
| HP | `/` | Homepage | Org+WebSite+LB+FAQ | 29 | P1 | 1 | Pass |
| SO-1 | `/cerrajero/cerrajero-urgente/` | Service Overview | Service+WebPage+Bread | 23 | P2 | 2 | Pass |
| SO-2 a 5 | `/cerrajero/{service}/` | Service Overview | Service+WebPage+Bread | 19-20 | P3 | 2 | Pass |
| GH | `/madrid/` | GeoHub | CollectionPage+Bread | 25 | P2 | 2 | Pass |
| LBS-1 | `/cerrajero/madrid/cerrajero-urgente/` | LBS | LB+Bread+FAQ | 29 | P1 | 1 | Pass |
| LBS-2 | `/cerrajero/madrid/apertura-puertas/` | LBS | LB+Bread+FAQ | 28 | P1 | 2 | Pass |
| LBS-3 | `/cerrajero/madrid/cambio-cerraduras/` | LBS | LB+Bread+FAQ | 27 | P1 | 2 | Pass |
| LBS-4 | `/cerrajero/madrid/cambio-bombines/` | LBS | LB+Bread+FAQ | 26 | P1 | 2 | Pass |
| LBS-5 | `/cerrajero/madrid/instalacion-cerraduras-seguridad/` | LBS | LB+Bread+FAQ | 25 | P2 | 2 | Pass |
| AC-1 | `/cerrajero/madrid/duplicado-llaves/` | Additional Cat | Service+Bread | 21 | P2 | 3 | Pass |
| GA-1 a 15 | `/madrid/{topic}/` | GeoArticle | Article+FAQ+Bread | 19-22 | P2-P3 | 3-4 | Pass |
| AUX | `/contacto/` | Auxiliar | ContactPoint | — | — | 1 | Pass |

**Total: 28 SEO base + 1 auxiliar = 29 URLs**

### 13.6 — Reglas No Negociables del sistema (15 reglas)

```text
1. Una página local = 1 servicio + 1 Main City única
2. LCAs viven en contenido + areaServed; NUNCA generan URLs
3. Approved Expansion requiere aprobación explícita del operador
4. Slugs limpios: lowercase + sin acentos + kebab-case
5. Sin near-me, sin adjetivos vacíos en URLs
6. Schema válido y veraz por page type
7. Word count en rango doctrinal por page type
8. Internal links cumplen matriz Paso-07 7.11
9. Anchors variados (catálogo Paso-07 7.9)
10. Breadcrumbs jerárquicos por page type
11. CTA presente y adaptado al funnel
12. Priority Score con 6 factores (Paso-08 8.1)
13. HP siempre P1 + Phase 1
14. GAs no se publican antes que su LBS hijo (Paso-08 8.11)
15. Web-first si GBP=Not Created (no inventar señales GBP hasta Paso 14)
```

### 13.7 — Documentación de Cambios template

```text
═══════════════════════════════════════════════════
REGISTRO DE CAMBIOS — [BUSINESS_NAME]
═══════════════════════════════════════════════════

Cambio #001 — [DATE]
Tipo:           [Expansion / Refresh / Correction / GBP Update]
Descripción:    [Qué cambia]
Outputs afectados: [IDs de outputs upstream]
Razón:          [Por qué se cambia ahora]
Aprobado por:   [Operador]
Validado QA:    [Sí/No + fecha]

Cambio #002 — ...
```

### 13.8 — Tracking Plan

```text
Tracking Stack:
- Google Search Console: configurar antes de Phase 1; verificar dominio canonical
- Google Analytics 4: pre-launch; eventos de conversión configurados (call/form/email)
- Rank Tracker (Ahrefs): keywords core × Main City + LCAs
- GMB Crush Grid: post Paso 14 (cuando GBP exista)

Cadencia revisión:
- GSC + GA4: semanal durante Phase 1-3; mensual durante Phase 4+
- Rank Tracker: semanal durante Phase 1-3; bi-semanal Phase 4+
- GMB Crush Grid: mensual desde Paso 14
```

### 13.9 — Roadmap final de publicación

| Fase | Semanas | Páginas | Pre-req crítico |
|---|---|---|---|
| 1 Entity Foundation | 1-2 | HP + 5 SO + GH | Bloques 1-4 cerrados; QA Gate Pass |
| 2 Conversion Layer | 2-3 | 5 LBS + 1 AC | Fase 1 publicada |
| 3 Semantic Expansion | 4-6 | 15 GAs | Fase 2 publicada |
| 4 Optimization Loop | 6+ | (sin nuevas; iteración) | Tracking activo |
| 5 GBP Creation | 7-8 | (Paso 14) | Fases 1-3 publicadas + datos GSC mínimos |

### 13.10 — Pre-requisitos para Paso 14

```text
Antes de crear el GBP:
☐ Bloques 1-4 cerrados al 100% (182 outputs upstream confirmed)
☐ Fases 1-3 publicadas (28 URLs SEO base activas)
☐ Final Publish Gate Pass en 28/28 URLs
☐ GBP Not Created QA Checklist Pass en 28/28 URLs
☐ Tracking configurado y reportando datos (mínimo 30 días GSC)
☐ NAP coherente entre web + cualquier directorio existente
☐ Decisión del operador: arrancar Paso 14 (GBP Creation)
```

### 13.11 — Sistema como fuente única de verdad

```text
Cualquier discrepancia entre:
- Web publicada
- GBP (cuando se cree en Paso 14)
- Materiales de marketing (folletos, ads, redes)

Se resuelve consultando el SOP del Paso 13 + outputs upstream de Bloques 1-4.

El SOP es la SOURCE OF TRUTH. Cualquier cambio que afecte a la arquitectura debe:
1. Registrarse en Documentación de Cambios (13.7)
2. Actualizar el output upstream correspondiente
3. Re-correr el QA Gate (Paso-09 9.7)
4. Re-publicar el SOP con el cambio
```

### 13.12 — Validación: cluster web completo y ready for GBP

```text
Cluster Cerrajeros Madrid 24h:
☑ 28 SEO base URLs publicadas
☑ Final Publish Gate Pass: 28/28
☑ GBP Not Created Checklist Pass: 28/28
☑ Internal links cumplen matriz: ~80 enlaces validados
☑ Schema válido en todas las URLs
☑ NAP coherente (web + footer + schema)
☑ Roadmap Phase 1-3 ejecutado
☑ Tracking activo: GSC + GA4 + Rank Tracker
→ Ready for Paso 14: Yes
```

### 13.13 — Validación: tracking configurado pre-launch

```text
Tracking pre-launch:
☑ Google Search Console: dominio verificado, sitemap subido
☑ Google Analytics 4: eventos call/form/email configurados
☑ Rank Tracker: 50+ keywords core + LCAs configurados
☑ GMB Crush Grid: pendiente Paso 14 (lógico)
→ Tracking ready: Yes (excepto GMB Grid, esperando Paso 14)
```

### 13.14 — Cierre de Bloque 4 = sistema operativo listo

```text
Bloque 4 cerrado:
☑ Paso 11 (Pseudocódigo): 14/14 outputs confirmed
☑ Paso 12 (Master Prompt): 12/12 outputs confirmed
☑ Paso 13 (Sistema Final Operativo): 14/14 outputs confirmed
☑ Total Bloque 4: 45 outputs confirmed
☑ Total sistema (Bloques 1-4): 182 outputs confirmed
☑ Cluster Cerrajeros Madrid 24h en estado "Operativo"
→ Bloque 4 closure: COMPLETE
→ Avanzar a Bloque 5 (GBP Creation + Salida a mercado): UNLOCKED
```

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 14 outputs que el Paso 13 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `13.5`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 13.1 | SOP completo del sistema | Documento maestro | GMB Crush | Bloques 1-4 (todos los outputs) |
| 13.2 | Resumen ejecutivo del cluster | Sección summary | GMB Crush | Paso-01 1.X + Paso-02 2.X + Paso-08 8.X + Paso-12 12.10 |
| 13.3 | Workflow detallado de los 13 pasos | Sección procedimental | GMB Crush | Bloques 1-4 (estructura) |
| 13.4 | Estructura de carpetas y archivos | Sección operacional | GMB Crush | — |
| 13.5 | Inventario URL final consolidado | Tabla N+1 filas | GMB Crush | Paso-03 3.5 + Paso-08 8.14 + Paso-09 9.7 |
| 13.6 | Reglas No Negociables (15 reglas) | Lista declarativa | GMB Crush | Bloques 1-3 (todas las reglas) + Paso-12 12.8 |
| 13.7 | Documentación de Cambios template | Plantilla | GMB Crush | — |
| 13.8 | Tracking Plan | Configuración tools | Decisión de diseño | Paso-10 10.3 + 10.7 |
| 13.9 | Roadmap final de publicación | Calendario consolidado | GMB Crush | Paso-10 10.4-10.9 |
| 13.10 | Pre-requisitos para Paso 14 | Checklist | GMB Crush | Paso-09 9.7 + 9.8 + Paso-10 10.13 |
| 13.11 | Sistema como fuente única de verdad | Declaración doctrinal | GMB Crush | — |
| 13.12 | Validación cluster ready for GBP | Validation flag | GMB Crush | Paso-09 9.7 + Paso-13 13.10 |
| 13.13 | Validación tracking configurado | Validation flag | GMB Crush | Paso-13 13.8 |
| 13.14 | Cierre de Bloque 4 = sistema operativo listo | Validation flag | GMB Crush | Paso-11 + Paso-12 + Paso-13 (intra-bloque) |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 14 outputs (13.1–13.14). Cada output usa el patrón estándar adaptado al SOP: Explicación / Sección / Ejemplo Cerrajeros / Ejemplos incorrectos / Regla / Validación / Cómo se obtiene / Output del paso.

### 13.1 — SOP completo del sistema

<small>§6.1</small>

**Explicación**

El SOP es el **documento maestro** que cierra el Bloque 4 y prepara el Bloque 5. Consolida 11 secciones (los outputs 13.2-13.14 + el propio resumen ejecutivo). Es la fuente única de verdad del cluster.

**Sección**

Ver §4 sub-sección 13.1 — esqueleto del SOP con 11 secciones.

**Ejemplo correcto con Cerrajeros Madrid 24h**

SOP de Cerrajeros con las 11 secciones rellenas; total ~30-50 páginas de documento dependiendo de detalle.

**Ejemplos incorrectos**

```text
- SOP sin sección Pre-requisitos para Paso 14 (no hay gate)
- SOP sin Reglas No Negociables (sistema sin disciplina)
- SOP que duplica info de Bloques 1-3 en lugar de referenciar
- Múltiples SOPs paralelos (rompe fuente única)
```

**Regla final**

```text
Un solo SOP por cluster, con las 11 secciones obligatorias.
```

**Validación operativa**

Aplicar checklist a las 11 secciones; verificar todas presentes.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Componer las 11 secciones referenciando outputs upstream + outputs 13.2-13.14.

**Output del paso**

- **Tipo:** Documento maestro markdown.
- **Ejemplo (Cerrajeros Madrid 24h):** SOP completo con 11 secciones rellenas.

### 13.2 — Resumen ejecutivo del cluster

<small>§6.2</small>

**Explicación**

Sección de apertura del SOP. Resume el estado del cluster en ~15 campos auditable de un vistazo.

**Sección**

Ver §4 sub-sección 13.2 — formato del resumen ejecutivo con 15 campos.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 13.2 — resumen completo con todos los campos rellenos.

**Ejemplos incorrectos**

```text
- Resumen sin Total URLs (no auditable)
- Resumen sin GBP Status (no se sabe si web-first)
- Resumen sin status de Bloques (no se sabe si todo confirmed)
```

**Regla final**

```text
Resumen ejecutivo cubre los 15 campos clave del cluster.
```

**Validación operativa**

Aplicar checklist 15 campos al resumen del SOP.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Plantilla con placeholders rellenados desde outputs upstream.

**Output del paso**

- **Tipo:** Sección summary del SOP.
- **Ejemplo (Cerrajeros Madrid 24h):** 15 campos rellenos.

### 13.3 — Workflow detallado de los 13 pasos

<small>§6.3</small>

**Explicación**

Sección que documenta el orden y los outputs de cada paso. Útil para onboarding de nuevos operadores y para auditar el sistema.

**Sección**

Ver §4 sub-sección 13.3.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 13.3 — workflow con 13 pasos + sus outputs counts.

**Ejemplos incorrectos**

```text
- Workflow incompleto (saltar Paso 11 o 12)
- Sin counts de outputs (sin contexto de magnitud)
- Workflow desactualizado tras cambios upstream
```

**Regla final**

```text
Workflow lista los 13 pasos con outputs counts y dependencias entre Bloques.
```

**Validación operativa**

Cruce con outputs declarados en §5 de cada a-doc upstream.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Compilar desde §5 de los 13 a-docs anteriores.

**Output del paso**

- **Tipo:** Sección procedimental del SOP.
- **Ejemplo (Cerrajeros Madrid 24h):** workflow con 13 pasos + 182 outputs counted.

### 13.4 — Estructura de carpetas y archivos

<small>§6.4</small>

**Explicación**

Sección que documenta el layout del proyecto del cliente — qué carpetas hay, qué archivos contiene cada una.

**Sección**

Ver §4 sub-sección 13.4.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 13.4.

**Ejemplos incorrectos**

```text
- Estructura desactualizada tras renombramientos
- Sin convención de naming (00a-, 01a-, plantillas, consolidados)
- Múltiples copias del mismo doc en carpetas distintas
```

**Regla final**

```text
Estructura de carpetas refleja exactamente el filesystem; sin ambigüedades.
```

**Validación operativa**

Cruce con `find` o `tree` del repo del cliente; las dos vistas deben coincidir.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Captura del filesystem del proyecto + documentar convención.

**Output del paso**

- **Tipo:** Sección operacional del SOP.
- **Ejemplo (Cerrajeros Madrid 24h):** árbol de carpetas con 4 Bloques + sus archivos.

### 13.5 — Inventario URL final consolidado

<small>§6.5</small>

**Explicación**

Tabla N+1 filas con TODAS las URLs del cluster + sus columnas operativas: Page Type, Schema, Score, Tier, Phase, QA status. Es la vista única que cualquier operador necesita para trabajar.

**Sección**

Ver §4 sub-sección 13.5.

**Ejemplo correcto con Cerrajeros Madrid 24h**

29 URLs (28 SEO + 1 aux) con todos los campos operativos.

**Ejemplos incorrectos**

```text
- Inventario sin columna QA (no se sabe estado actual)
- Inventario con URLs en blanco o slugs sucios
- Total URLs ≠ fórmula 1+S+1+S+A+G×S (descuadre)
```

**Regla final**

```text
Inventario URL final = N+1 filas exactas con todas las columnas operativas rellenas.
```

**Validación operativa**

Cruce con Paso-03 3.5 (URL Matrix) + Paso-08 8.14 (Inventario priorizado) + Paso-09 9.7 (Final Publish Gate).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Join de las matrices de los pasos upstream en una sola tabla consolidada.

**Output del paso**

- **Tipo:** Tabla N+1 filas consolidada.
- **Ejemplo (Cerrajeros Madrid 24h):** 29 URLs con score+tier+phase+QA.

### 13.6 — Reglas No Negociables del sistema (15 reglas)

<small>§6.6</small>

**Explicación**

Lista consolidada de las 15 reglas doctrinales que rigen TODO el sistema. Ninguna es negociable; cualquier desviación bloquea el deploy.

**Sección**

Ver §4 sub-sección 13.6.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Las 15 reglas aplicadas y validadas en el cluster (cruce con Paso-12 12.8 que tiene 14 — la 15ª se añade aquí: "Sistema es fuente única de verdad").

**Ejemplos incorrectos**

```text
- Reglas con excepciones documentadas (rompe disciplina)
- Inventar regla 16 fuera del catálogo
- Saltar regla por urgencia comercial
```

**Regla final**

```text
Las 15 reglas son no-negociables; cualquier violación bloquea Paso 14 y Paso 18.
```

**Validación operativa**

Aplicar las 15 reglas como filtro de cierre del SOP. Cualquier violación → bloqueo.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Compilar desde Paso-12 12.8 (14 reglas) + añadir 15ª (fuente única de verdad).

**Output del paso**

- **Tipo:** Lista declarativa de 15 reglas.
- **Ejemplo (Cerrajeros Madrid 24h):** 15/15 reglas aplicadas con éxito.

### 13.7 — Documentación de Cambios template

<small>§6.7</small>

**Explicación**

Plantilla para registrar **cualquier cambio futuro** al cluster después del deploy. Asegura que las modificaciones (expansiones territoriales, refresh de contenido, correcciones) están trazadas.

**Sección**

Ver §4 sub-sección 13.7.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Cambio #001 — 2026-06-15
Tipo: Expansion
Descripción: Aprobar Approved Expansion Area 'Toledo' tras validación
Outputs afectados: 1.11 (Paso 1), 4.10 (Paso 4), 7.15 (Paso 7), 11.6 (Paso 11)
Razón: Cliente aprueba expansión tras 6 meses de datos GSC sólidos
Aprobado por: Operador
Validado QA: Sí — 2026-06-20
```

**Ejemplos incorrectos**

```text
- Cambio sin Aprobado por (anónimo)
- Cambio sin Outputs afectados (no auditable)
- Cambio sin Validado QA (rompe gate)
- Múltiples cambios fusionados en una sola entrada
```

**Regla final**

```text
Cada cambio = 1 entrada con 6 campos obligatorios.
```

**Validación operativa**

Aplicar al inicio de cualquier modificación post-deploy.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Plantilla con 6 campos.

**Output del paso**

- **Tipo:** Plantilla template.
- **Ejemplo (Cerrajeros Madrid 24h):** plantilla rellenada con cambio #001 hipotético.

### 13.8 — Tracking Plan

<small>§6.8</small>

**Explicación**

Sección que documenta el stack de tracking del cluster: qué tools, cuándo configurarlos, cadencia de revisión.

**Sección**

Ver §4 sub-sección 13.8.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 13.8 — stack GSC + GA4 + Rank Tracker + GMB Crush Grid (post Paso 14).

**Ejemplos incorrectos**

```text
- Tracking solo GA4 (sin GSC = sin queries data)
- Sin cadencia de revisión (datos no se accionan)
- GMB Crush Grid antes de Paso 14 (no tiene sentido)
- Sin Rank Tracker (sin posiciones)
```

**Regla final**

```text
Tracking Plan completo = GSC + GA4 + Rank Tracker pre-launch + GMB Grid post-Paso 14.
```

**Validación operativa**

Cruce con Paso-10 10.3 (CMS + capabilities) + 10.7 (Optimization Loop).

**Cómo se obtiene**

- **Fuente:** Decisión de diseño.
- **Método:** Plantilla del stack + cadencia operativa basada en page types y phases.

**Output del paso**

- **Tipo:** Configuración tools + cadencia.
- **Ejemplo (Cerrajeros Madrid 24h):** stack completo configurado pre-Phase 1.

### 13.9 — Roadmap final de publicación

<small>§6.9</small>

**Explicación**

Calendario consolidado que une las 5 fases del Paso-10 + el cierre de Pasos 11-13. Es el roadmap end-to-end.

**Sección**

Ver §4 sub-sección 13.9.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 13.9 — roadmap 5 fases con semanas y pre-requisitos.

**Ejemplos incorrectos**

```text
- Roadmap sin Pre-req crítico por fase (no hay gate)
- Saltar Phase 4 Optimization (publicación no es final)
- Crear GBP en Phase 1 (rompe web-first)
```

**Regla final**

```text
Roadmap respeta orden 5 fases + pre-requisitos por fase + dependencias estructurales.
```

**Validación operativa**

Cruce con Paso-10 10.4-10.9 (5 fases + calendario + dependencias).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Consolidar las 5 fases del Paso-10 en una vista de roadmap.

**Output del paso**

- **Tipo:** Calendario consolidado.
- **Ejemplo (Cerrajeros Madrid 24h):** 5 fases × ~9 semanas con pre-reqs por fase.

### 13.10 — Pre-requisitos para Paso 14

<small>§6.10</small>

**Explicación**

Checklist explícita de los 7 pre-requisitos que deben cumplirse antes de arrancar el Paso 14 (creación efectiva del GBP).

**Sección**

Ver §4 sub-sección 13.10.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Para Cerrajeros antes del Paso 14:
☑ Bloques 1-4 cerrados (182 outputs confirmed) — pendiente cuando Bloque 4 cierre
☑ Fases 1-3 publicadas (28 URLs SEO base activas) — pendiente cuando publication loop ejecute
☑ Final Publish Gate Pass — pendiente
☑ GBP Not Created Checklist Pass — pendiente
☑ Tracking GSC mínimo 30 días — pendiente
☑ NAP coherente — actual
☑ Operador aprueba Paso 14 — pendiente
```

**Ejemplos incorrectos**

```text
- Saltar pre-requisito de Tracking 30 días (Paso 14 sin datos para sincronizar)
- Crear GBP sin Final Publish Gate Pass (publica con QA fallido)
- Aprobar Paso 14 sin operador (rompe disciplina de aprobación)
```

**Regla final**

```text
Paso 14 NO se arranca sin los 7 pre-requisitos en ✓.
```

**Validación operativa**

Aplicar checklist al cierre del Bloque 4. Bloquear Paso 14 si falla cualquier item.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Compilar checklist desde Paso-09 9.7 + 9.8 + Paso-10 10.13.

**Output del paso**

- **Tipo:** Checklist 7 items.
- **Ejemplo (Cerrajeros Madrid 24h):** 7 items pendientes (a completar durante Phase 1-3).

### 13.11 — Sistema como fuente única de verdad

<small>§6.11</small>

**Explicación**

Declaración doctrinal que establece que el SOP del Paso 13 es la **única fuente de verdad** del cluster. Cualquier discrepancia se resuelve consultando este SOP + outputs upstream.

**Sección**

Ver §4 sub-sección 13.11.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
Si en el futuro hay discrepancia entre:
- Web Cerrajeros Madrid 24h (publicada)
- GBP de Cerrajeros (post Paso 14)
- Materiales de marketing

→ Resolver consultando el SOP del Paso 13 + outputs Bloques 1-4.
SOP es source of truth.
```

**Ejemplos incorrectos**

```text
- Múltiples SOPs paralelos (rompe fuente única)
- Cambio en marketing sin actualizar SOP (deriva)
- GBP con NAP distinto al SOP (rompe coherencia)
```

**Regla final**

```text
Un cluster = un SOP = una fuente única de verdad.
```

**Validación operativa**

Aplicar como principio doctrinal a cualquier decisión futura sobre el cluster.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Declaración doctrinal embebida en el SOP.

**Output del paso**

- **Tipo:** Declaración.
- **Ejemplo (Cerrajeros Madrid 24h):** SOP de Cerrajeros declarado source of truth del cluster.

### 13.12 — Validación: cluster web completo y ready for GBP

<small>§6.12</small>

**Explicación**

Validación de cierre que confirma que el cluster web está listo para arrancar el Paso 14 (GBP Creation).

**Patrón o fórmula**

```text
Ready for Paso 14 = AND(
  Bloques 1-4 cerrados (182 outputs upstream confirmed),
  Fases 1-3 publicadas,
  Final Publish Gate Pass en N URLs,
  GBP Not Created Checklist Pass en N URLs,
  Tracking activo y reportando datos,
  NAP coherente,
  Operador aprueba arranque Paso 14
)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 13.12 — todos los checks ✓ tras cierre de Bloque 4 + ejecución de Fases 1-3.

**Ejemplos incorrectos**

```text
- Pasar a Paso 14 con outputs ⚠ inferido upstream
- Crear GBP con tracking sin configurar
- Saltar el gate de aprobación del operador
```

**Regla final**

```text
Cluster web está ready for GBP solo si los 7 checks están en Pass.
```

**Validación operativa**

Aplicar tras cierre de Bloque 4 + completar Phase 1-3.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Cruzar 7 checks contra outputs upstream.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** ready: pendiente (estamos en pre-Phase 1).

### 13.13 — Validación: tracking configurado pre-launch

<small>§6.13</small>

**Explicación**

Validación de que el stack de tracking está configurado y listo para reportar datos desde la primera publicación.

**Patrón o fórmula**

```text
Tracking ready = AND(
  GSC: dominio verificado + sitemap subido,
  GA4: eventos call/form/email configurados,
  Rank Tracker: keywords core + LCAs configurados,
  GMB Crush Grid: pendiente Paso 14 (lógico)
)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 13.13 — 3/4 ✓ (GMB Grid esperando Paso 14).

**Ejemplos incorrectos**

```text
- GSC sin sitemap (bot no descubre URLs)
- GA4 sin eventos (sin medición de conversiones)
- Rank Tracker sin keywords LCAs (sin medición local)
```

**Regla final**

```text
Tracking pre-launch = GSC + GA4 + Rank Tracker configurados; GMB Grid post-Paso 14.
```

**Validación operativa**

Aplicar antes de Phase 1.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Auditar cada herramienta del stack.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** tracking ready: 3/4 configurados; GMB Grid esperando.

### 13.14 — Cierre de Bloque 4 = sistema operativo listo

<small>§6.14</small>

**Explicación**

Validación final que confirma el cierre del Bloque 4 y el desbloqueo del Bloque 5+ (GBP Creation, post-launch).

**Patrón o fórmula**

```text
Bloque 4 closure = AND(
  Paso 11 (14 outputs) confirmed,
  Paso 12 (12 outputs) confirmed,
  Paso 13 (14 outputs) confirmed
) → Bloques 1-4 total = 182 outputs confirmed → Bloque 5 UNLOCKED
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 13.14 — Bloque 4 cerrado, sistema completo, Bloque 5 desbloqueado.

**Ejemplos incorrectos**

```text
- Pasar a Paso 14 sin Paso 13 cerrado
- Saltar Paso 11 o 12 ("ya tengo el SOP, no necesito pseudocódigo")
- Bloque 4 cerrado pero Bloques 1-3 con ⚠ pendiente
```

**Regla final**

```text
Bloque 4 cerrado solo cuando los 3 pasos (11+12+13) están confirmed = 45 outputs nuevos del Bloque 4.
```

**Validación operativa**

Aplicar al final de Paso 13. Cruce con outputs upstream Bloques 1-3.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Validación de los 3 pasos del Bloque 4.

**Output del paso**

- **Tipo:** Validation flag de cierre de Bloque.
- **Ejemplo (Cerrajeros Madrid 24h):** Bloque 4 closure: COMPLETE; Bloque 5 UNLOCKED.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 13 y avanzar al Paso 14 (GBP Creation, Bloque 5+).

### Validación del SOP

- ☐ SOP completo con las 11 secciones (13.1)
- ☐ Resumen ejecutivo con 15 campos (13.2)
- ☐ Workflow detallado de los 13 pasos (13.3)
- ☐ Estructura de carpetas documentada (13.4)
- ☐ Inventario URL final consolidado (N+1 filas) (13.5)
- ☐ Reglas No Negociables (15) listadas (13.6)

### Validación operacional

- ☐ Documentación de Cambios template lista (13.7)
- ☐ Tracking Plan completo (13.8)
- ☐ Roadmap final 5 fases con pre-reqs (13.9)
- ☐ Pre-requisitos para Paso 14 (7 items) listos (13.10)
- ☐ Sistema declarado fuente única de verdad (13.11)

### Validación final

- ☐ Cluster ready for GBP (13.12)
- ☐ Tracking configurado pre-launch (13.13)
- ☐ Cierre de Bloque 4 = sistema operativo listo; Bloque 5 unlocked (13.14)

## Outputs Consolidados

<small>§8</small>

> Tabla final compacta con la trazabilidad row-per-output. Los IDs (`13.1`–`13.14`) coinciden con los declarados en §5. Esta tabla es la fuente única de la trazabilidad consolidada del paso (sustituye al antiguo b-doc).

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 13.1 | ← Bloques 1-4 (todos los outputs) | **SOP completo del sistema** = documento maestro 11 secciones para Cerrajeros | Componer 11 secciones referenciando outputs upstream + outputs 13.2-13.14. **Fuente:** GMB Crush. | confirmed |
| 13.2 | ← Paso-01 1.X + Paso-02 2.X + Paso-08 8.X + Paso-12 12.10 | **Resumen ejecutivo** = 15 campos rellenos (Cliente, Sector, Main City, Status, Total URLs, etc.) | Plantilla con placeholders rellenados desde outputs upstream. **Fuente:** GMB Crush. | confirmed |
| 13.3 | ← Bloques 1-4 (estructura) | **Workflow detallado** = 13 pasos × outputs counts (182 outputs total) | Compilar desde §5 de los 13 a-docs anteriores. **Fuente:** GMB Crush. | confirmed |
| 13.4 | — | **Estructura de carpetas y archivos** = árbol con 4 Bloques + carpetas 01/02 + archivos | Captura del filesystem + documentar convención. **Fuente:** GMB Crush. | confirmed |
| 13.5 | ← Paso-03 3.5 + Paso-08 8.14 + Paso-09 9.7 | **Inventario URL final** = 29 URLs (28 SEO + 1 aux) con score+tier+phase+QA | Join de las matrices de los pasos upstream en una tabla consolidada. **Fuente:** GMB Crush. | confirmed |
| 13.6 | ← Bloques 1-3 (todas las reglas) + Paso-12 12.8 | **15 Reglas No Negociables** = aplicadas con éxito en el cluster | Compilar desde Paso-12 12.8 (14 reglas) + añadir 15ª "fuente única de verdad". **Fuente:** GMB Crush. | OK |
| 13.7 | — | **Documentación de Cambios template** = plantilla 6 campos (Tipo / Descripción / Outputs / Razón / Aprobado por / Validado QA) | Plantilla con 6 campos obligatorios. **Fuente:** GMB Crush. | confirmed |
| 13.8 | ← Paso-10 10.3 + 10.7 | **Tracking Plan** = GSC + GA4 + Rank Tracker pre-launch + GMB Crush Grid post-Paso 14 | Plantilla del stack + cadencia operativa por page types y phases. **Fuente:** Decisión de diseño. | confirmed |
| 13.9 | ← Paso-10 10.4-10.9 | **Roadmap final** = 5 fases × ~9 semanas con pre-reqs por fase | Consolidar las 5 fases del Paso-10 en una vista de roadmap. **Fuente:** GMB Crush. | confirmed |
| 13.10 | ← Paso-09 9.7 + 9.8 + Paso-10 10.13 | **Pre-requisitos para Paso 14** = 7 items checklist (Bloques 1-4 / Fases 1-3 / QA Pass / GBP Checklist Pass / Tracking 30d / NAP / Aprobación operador) | Compilar checklist desde outputs upstream. **Fuente:** GMB Crush. | confirmed |
| 13.11 | — | **Sistema como fuente única de verdad** = SOP de Cerrajeros declarado source of truth | Declaración doctrinal embebida en el SOP. **Fuente:** GMB Crush. | OK |
| 13.12 | ← Paso-09 9.7 + 13.10 | **Validación cluster ready for GBP** = pendiente (a completar tras Phase 1-3) | Cruzar 7 checks contra outputs upstream. **Fuente:** GMB Crush. | OK (pendiente ejecución) |
| 13.13 | ← 13.8 | **Validación tracking configurado** = 3/4 ✓ (GMB Grid esperando Paso 14) | Auditar cada herramienta del stack. **Fuente:** GMB Crush. | OK (pendiente ejecución) |
| 13.14 | ← Paso-11 + Paso-12 + Paso-13 | **Cierre de Bloque 4** = 45 outputs nuevos confirmed; Bloque 5 UNLOCKED | Validación de los 3 pasos del Bloque 4. **Fuente:** GMB Crush. | OK |

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
- Sistema Final Operativo SOP Framework

> **Nota importante — SOP como cierre del Bloque 4:**
> El Paso 13 cierra el sistema **antes de la creación efectiva del GBP** (Paso 14). Después del Paso 14, el SOP se actualiza para reflejar que el GBP existe (sameAs activable, reseñas Google referenciables, GMB Grid configurable). Hasta entonces, el sistema opera en modo web-first y el SOP refleja ese estado.
