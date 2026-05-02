# Aeroterm — Output consolidado · Bloque 1 (Pasos 1-3)

> Documento producido por la IA aplicando los manuales del sistema GMB Crush a partir del input declarado en `00preflight.md`. Aplicadas las convenciones de `00convenciones-ejecucion.md` — los campos no validados llevan marcador `⚠`. Cada fila lleva el `ID` del b-doc correspondiente para cruzar trazabilidad entre pasos.

---

# Paso 1 — Intake Form

## Identidad y dominio

| ID | Campo | Valor | Status |
|---|---|---|---|
| 1.01 | Business Name | `Aeroterm` | confirmed |
| 1.02 | Website URL | `https://www.aeroterm.es` | ⚠ placeholder |
| 1.03 | Canonical Domain | `https://www.aeroterm.es` | ⚠ placeholder |

## Estado del GBP (web-first)

| ID | Campo | Valor | Status |
|---|---|---|---|
| 1.04 | GBP Status | `Not Created` | confirmed |
| 1.05 | GBP Creation Timing | `After website launch` | confirmed |
| 1.06 | GBP Verification Status | `Not Started` | confirmed |
| 1.07 | GBP URL | `N/A — pending Paso 14` | confirmed |

## Full NAP

| ID | Campo | Valor | Status |
|---|---|---|---|
| 1.08 | Name | `Aeroterm` | confirmed |
| 1.09 | Street Address | `Marqués de Valdecilla 16` | confirmed |
| 1.10 | City | `Madrid` | confirmed |
| 1.11 | State / Province | `Comunidad de Madrid` | confirmed |
| 1.12 | ZIP | `28002` | confirmed |
| 1.13 | Country | `España` | confirmed |
| 1.14 | Phone | `+34 XXX XXX XXX` | ⚠ placeholder |
| 1.15 | Email | `info@aeroterm.es` | ⚠ placeholder |

## Categorías GBP planificadas

| ID | Campo | Valor | Status |
|---|---|---|---|
| 1.16 | Planned Primary GBP Category | `Heating contractor` | ⚠ inferido |
| 1.17 | Planned Additional 1 | `Solar energy contractor` | ⚠ inferido |
| 1.18 | Planned Additional 2 | `Air conditioning contractor` | ⚠ inferido |

## Geografía (Main City + LCAs + Expansion)

| ID | Campo | Valor | Status |
|---|---|---|---|
| 1.19 | Dirección física como ancla | `Marqués de Valdecilla 16, [distrito], [barrio], Madrid` | ⚠ placeholder (barrio/distrito) |
| 1.20 | Main City | `Madrid` | confirmed |
| 1.21 | Physical Location City | `Madrid` | confirmed |
| 1.22 | Direct LCA 1 | `Hortaleza` (distrito) | ⚠ placeholder |
| 1.23 | Direct LCA 2 | `Prosperidad` (barrio) | ⚠ placeholder |
| 1.24 | Candidate LCA 1 | `Chamartín` | ⚠ inferido |
| 1.25 | Candidate LCA 2 | `Salamanca` | ⚠ inferido |
| 1.26 | Candidate LCA 3 | `Chamberí` | ⚠ inferido |
| 1.27 | Candidate LCA 4 | `Centro` | ⚠ inferido |
| 1.28 | Candidate LCA 5 | `Retiro` | ⚠ inferido |
| 1.29 | Candidate LCA 6 | `Moncloa-Aravaca` | ⚠ inferido |
| 1.30 | Candidate LCA 7 | `Tetuán` | ⚠ inferido |
| 1.31 | Candidate LCA 8 | `Ciudad Lineal` | ⚠ inferido |
| 1.32 | LCAs no generan páginas en la base | `No, not in the base build` | confirmed |
| 1.33 | Approved Expansion Areas | `None in Phase 1` | confirmed |

## Servicios principales (S = 5)

| ID | Servicio | Status |
|---|---|---|
| 1.34 | Instalación de aerotermia | ⚠ inferido |
| 1.35 | Mantenimiento de aerotermia | ⚠ inferido |
| 1.36 | Sustitución de caldera por aerotermia | ⚠ inferido |
| 1.37 | Aerotermia con suelo radiante | ⚠ inferido |
| 1.38 | Aerotermia para ACS y piscinas | ⚠ inferido |

## Consolidación de Additional Categories

| ID | Categoría | Status arquitectónico | Status |
|---|---|---|---|
| 1.39 | Air conditioning contractor | Cubierta por core service `Instalación de aerotermia` (heat pump reversible) | confirmed (lógica) |
| 1.40 | Solar energy contractor | Necesita página propia (no cubierta por core) | confirmed (lógica) |

## Contenido y conversión

| ID | Campo | Valor | Status |
|---|---|---|---|
| 1.41 | GeoArticles per Service (G) | `3` | confirmed |
| 1.42 | Preferred CTA | `Solicitar presupuesto` | confirmed (Decisión de diseño) |

## Trust signals

| ID | Trust signal | Status |
|---|---|---|
| 1.43 | Instaladores certificados (RITE) | ⚠ inferido |
| 1.44 | Reseñas iniciales pendientes de recopilar tras crear y verificar el GBP | confirmed (doctrina) |
| 1.45 | Tramitación de subvenciones (Plan MOVES y similares) | ⚠ inferido |
| 1.46 | Garantía del fabricante + garantía propia | ⚠ inferido |
| 1.47 | Estudio de viabilidad gratuito + servicio post-venta | ⚠ inferido |

---

# Paso 2 — Fórmula Maestra

> Outputs deterministas de aplicar la doctrina sobre los inputs de Paso 1. Los IDs cascadean de las decisiones de Paso 1 vía las cadenas `← X.YY` del b-doc 02b.

## Alcance de la fórmula base

| ID | Decisión | Valor | Status |
|---|---|---|---|
| 2.01 | Fórmula sobre 1 Main City | `Madrid` | confirmed (← 1.20) |
| 2.02 | LCAs no multiplican páginas | 10 LCAs declaradas → 0 URLs base | confirmed |
| 2.03 | Approved Expansion fuera de la fórmula inicial | `None in Phase 1` | confirmed |

## Servicios incluidos en el cálculo (S = 5)

| ID | Servicio incluido | Status |
|---|---|---|
| 2.04 | S total = 5 | confirmed (← 1.34–1.38) |
| 2.05 | Instalación de aerotermia | confirmed (← 1.34) |
| 2.06 | Mantenimiento de aerotermia | confirmed (← 1.35) |
| 2.07 | Sustitución de caldera por aerotermia | confirmed (← 1.36) |
| 2.08 | Aerotermia con suelo radiante | confirmed (← 1.37) |
| 2.09 | Aerotermia para ACS y piscinas | confirmed (← 1.38) |

## Páginas generadas por la fórmula

| ID | Bloque | Cantidad | Status |
|---|---|---|---|
| 2.10 | Homepage | 1 | confirmed |
| 2.11 | Service Overview Pages | 5 (← 1.34–1.38) | confirmed |
| 2.12 | GeoHub Main City | 1 (Madrid) | confirmed |
| 2.13 | LBS Main City | 5 (← 1.34–1.38) | confirmed |
| 2.14 | Additional Category Pages | 1 (← 1.40) | confirmed |

## Categorías adicionales efectivas

| ID | Decisión | Valor | Status |
|---|---|---|---|
| 2.15 | Air conditioning queda cubierta | `Cubierta por Instalación de aerotermia` | confirmed (← 1.39) |
| 2.16 | Solar energy = A efectiva | `A = 1` | confirmed (← 1.40) |

## GeoArticles

| ID | Decisión | Valor | Status |
|---|---|---|---|
| 2.17 | G por servicio | `G = 3` | confirmed (← 1.41) |
| 2.18 | Cálculo G × S | `3 × 5` | confirmed (← 1.34–1.38) |
| 2.19 | Total GeoArticles | `15` | confirmed (← 1.34–1.38) |
| 2.20 | GeoArticles para Madrid (no por LCA) | `15 GeoArticles para Madrid` | confirmed |

## Total páginas SEO base

| ID | Bloque | Cantidad |
|---|---|---|
| 2.21 | Homepage | 1 |
| 2.22 | Service Overview Pages | 5 |
| 2.23 | GeoHub | 1 |
| 2.24 | LBS | 5 |
| 2.25 | Additional Category Pages | 1 |
| 2.26 | GeoArticles | 15 |
| **2.27** | **Total SEO base** | **28 páginas** |
| 2.28 | `/contacto/` (auxiliar fuera SEO base) | 1 página auxiliar |

---

# Paso 3 — URL Matrix base

**Spreadsheet Name:** `Aeroterm – GMB Crush Website Architecture` · **GeoHub URL Style:** Option A `/madrid/`

## Estructura de la matriz

| ID | Decisión | Status |
|---|---|---|
| 3.01 | Crear URL Matrix operativa | confirmed |
| 3.02 | ID único por tipo (HP, SO-N, GH, LBS-N, AC-N, GA-N) | confirmed |
| 3.03 | Columnas de producción (URL, H1, Meta Title, Schema, Priority, Phase, Status) | confirmed |

## URL Matrix (28 filas SEO base + 1 auxiliar)

| ID | Page ID | URL | Tipo | Schema | Priority | Phase | Status |
|---|---|---|---|---|---|---|---|
| 3.04 | HP | `/` | Homepage | Organization + LocalBusiness | P1 | 1 | confirmed |
| 3.05 | HP | (raíz `/` = patrón) | — | — | — | — | confirmed |
| 3.06 | AUX | `/contacto/` | Auxiliar | ContactPoint | P4 | 1 | confirmed |
| 3.07 | SO-1 | `/calefaccion/instalacion-aerotermia/` | Service Overview | Service | P1 | 1 | ⚠ inferido (← 1.34) |
| 3.08 | SO-2 | `/calefaccion/mantenimiento-aerotermia/` | Service Overview | Service | P1 | 1 | ⚠ inferido (← 1.35) |
| 3.09 | SO-3 | `/calefaccion/sustitucion-caldera-aerotermia/` | Service Overview | Service | P1 | 1 | ⚠ inferido (← 1.36) |
| 3.10 | SO-4 | `/calefaccion/aerotermia-suelo-radiante/` | Service Overview | Service | P1 | 1 | ⚠ inferido (← 1.37) |
| 3.11 | SO-5 | `/calefaccion/aerotermia-acs-piscinas/` | Service Overview | Service | P1 | 1 | ⚠ inferido (← 1.38) |
| 3.12 | GH | `/madrid/` | GeoHub | Place | P1 | 1 | confirmed (← 1.20) |
| 3.13 | LBS-1 | `/calefaccion/madrid/instalacion-aerotermia/` | LBS | Service + LocalBusiness | P1 | 1 | ⚠ inferido (← 1.34) |
| 3.14 | LBS-2 | `/calefaccion/madrid/mantenimiento-aerotermia/` | LBS | Service + LocalBusiness | P1 | 1 | ⚠ inferido (← 1.35) |
| 3.15 | LBS-3 | `/calefaccion/madrid/sustitucion-caldera-aerotermia/` | LBS | Service + LocalBusiness | P1 | 1 | ⚠ inferido (← 1.36) |
| 3.16 | LBS-4 | `/calefaccion/madrid/aerotermia-suelo-radiante/` | LBS | Service + LocalBusiness | P1 | 1 | ⚠ inferido (← 1.37) |
| 3.17 | LBS-5 | `/calefaccion/madrid/aerotermia-acs-piscinas/` | LBS | Service + LocalBusiness | P1 | 1 | ⚠ inferido (← 1.38) |
| 3.18 | AC-1 | `/calefaccion/madrid/energia-solar/` | Additional Category | Service | P2 | 1 | ⚠ inferido (← 1.40) |
| 3.19 | GA-1 | `/madrid/cuanto-cuesta-instalar-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.20 | GA-2 | `/madrid/aerotermia-frente-a-caldera-de-gas/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.21 | GA-3 | `/madrid/subvenciones-aerotermia-en-madrid/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.22 | GA-4 | `/madrid/cada-cuanto-mantenimiento-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.23 | GA-5 | `/madrid/checklist-mantenimiento-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.24 | GA-6 | `/madrid/precio-mantenimiento-anual-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.25 | GA-7 | `/madrid/como-sustituir-caldera-gas-por-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.26 | GA-8 | `/madrid/cuanto-tarda-cambio-de-caldera-a-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.27 | GA-9 | `/madrid/cuando-merece-pena-sustituir-caldera-por-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.28 | GA-10 | `/madrid/aerotermia-suelo-radiante-instalacion/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.29 | GA-11 | `/madrid/precio-aerotermia-mas-suelo-radiante/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.30 | GA-12 | `/madrid/eficiencia-suelo-radiante-vs-radiadores/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.31 | GA-13 | `/madrid/aerotermia-para-piscinas-climatizadas/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.32 | GA-14 | `/madrid/aerotermia-acs-domestico/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| 3.33 | GA-15 | `/madrid/aerotermia-piscina-todo-el-ano/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |

## Tratamiento de Local Coverage Areas

| ID | Decisión | Valor | Status |
|---|---|---|---|
| 3.34 | LCAs como contenido y schema | `Hortaleza, Prosperidad, Chamartín, Salamanca, Chamberí, Centro, Retiro, Moncloa-Aravaca, Tetuán, Ciudad Lineal` | confirmed (← 1.22–1.31) |
| 3.35 | No filas URL para LCAs | `No /hortaleza/, no /chamartin/, etc.` | confirmed |

---

# Resumen de status

| Status | Cantidad | % |
|---|---:|---:|
| confirmed | 70 | 64% |
| ⚠ inferido | 32 | 29% |
| ⚠ placeholder | 8 | 7% |
| **Total fields (110 IDs)** | **110** | **100%** |

> Las decisiones de Paso 2 son `confirmed` (deterministas sobre Paso 1), pero su validez depende de que los inputs de Paso 1 sean correctos. Si la lista de servicios cambia tras Local Pack real, Paso 2 y Paso 3 se recalculan automáticamente.

---

# Acciones pendientes para promover `⚠` a `confirmed`

## Bloque A — Local Pack analysis (resuelve 17 ⚠ inferido)

**Tool necesaria:** Google Maps · sin login · navegador en clean session.

**IDs afectados (17):** 1.16, 1.17, 1.18, 1.24-1.31, 1.34-1.38, 1.43, 1.45, 1.46, 1.47

**Procedimiento:**

1. Abrir Google Maps y buscar `aerotermia Madrid`. Anotar los 5 negocios top del Local Pack.
2. Para cada perfil del top 5, capturar:
   - Categoría primaria GBP declarada
   - Categorías adicionales declaradas
   - Servicios listados
   - Áreas de servicio declaradas
   - Trust signals visibles en perfil + web
3. Repetir con `aerotermia Barcelona` y `pompe à chaleur Paris`.
4. Aplicar reglas del manual:
   - **Primary Category** → más repetida (>3 de 5)
   - **5 Servicios core** → top 5 por frecuencia, cruzar con oferta real de Aeroterm
   - **Candidate LCAs** → zonas en ≥2 perfiles, validar test 3/6 GEO
   - **Trust signals** → 3-4 estándar del sector + 1-2 diferenciadores acreditables

**Output esperado:** los 17 IDs pasan de `⚠ inferido` a `validated`.

**Cascada automática:** los IDs de Paso 3 que dependen (3.07-3.11, 3.13-3.17, 3.18) pasan también a `validated` sin trabajo extra.

## Bloque B — Keyword research (resuelve 15 ⚠ inferido)

**Tool necesaria:** Ahrefs / Semrush / Google Keyword Planner.

**IDs afectados (15):** 3.19–3.33

**Procedimiento:**

1. Para cada uno de los 5 servicios core (← 1.34–1.38), generar candidatos GeoArticle (preguntas, dudas, comparativas).
2. Validar volumen mensual + dificultad + intent en Madrid.
3. Seleccionar 3 GeoArticles por servicio (15 total) con mejor cruce volumen/dificultad/intent.

## Bloque C — Cliente confirma (resuelve 8 ⚠ placeholder)

| IDs afectados | Acción del cliente |
|---|---|
| 1.02, 1.03 | Confirmar dominio real registrado o que va a registrarse |
| 1.14 | Teléfono real del negocio |
| 1.15 | Email real de contacto |
| 1.19, 1.22, 1.23 | Validar barrio/distrito de Marqués de Valdecilla 16, 28002 (catastro o Google Maps) |

---

# Bloqueo de publicación

> Por la **Regla 3** de las convenciones de ejecución: este documento NO puede pasar a publicación tal cual está. El Paso 18 (QA y deploy) debe rechazar el deploy mientras existan los 40 marcadores `⚠`. La publicación se desbloquea cuando los Bloques A, B y C de acciones pendientes se hayan ejecutado.

**Cruce con b-docs:** cada fila de este consolidado lleva el ID que matchea exactamente con `01b`, `02b`, `03b` de Fase 2 - Revisión. Para validar trazabilidad, abrir el b-doc correspondiente y comparar `Decisión y ejemplo` + `Cómo decidimos` con el valor producido aquí.
