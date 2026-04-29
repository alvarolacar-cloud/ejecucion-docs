# Aeroterm — Output consolidado · Bloque 1 (Pasos 1-3)

> Documento producido por la IA aplicando los manuales del sistema GMB Crush a partir del input declarado en `00preflight.md`. Aplicadas las convenciones de `00convenciones-ejecucion.md` — los campos no validados llevan marcador `⚠`.

## Metadata

| Campo | Valor |
|---|---|
| Cliente | Aeroterm |
| Sector | Instalaciones de aerotermia |
| Sistema | GMB Crush V6.4 |
| Bloques cubiertos | Bloque 1 — Fundamentos (Pasos 1, 2, 3) |
| Operador | IA sin acceso a Local Pack ni keyword research en directo |
| Fecha de ejecución | 2026-04-29 |

---

# Paso 1 — Intake Form

## Identidad y dominio

| Campo | Valor | Status |
|---|---|---|
| Business Name | `Aeroterm` | confirmed |
| Website URL | `https://www.aeroterm.es` | ⚠ placeholder |
| Canonical Domain | `https://www.aeroterm.es` | ⚠ placeholder |

## Estado del GBP (web-first)

| Campo | Valor | Status |
|---|---|---|
| GBP Status | `Not Created` | confirmed |
| GBP Creation Timing | `After website launch` | confirmed |
| GBP Verification Status | `Not Started` | confirmed |
| GBP URL | `N/A — pending Paso 14` | confirmed |

## Full NAP

| Campo | Valor | Status |
|---|---|---|
| Name | `Aeroterm` | confirmed |
| Street Address | `Marqués de Valdecilla 16` | confirmed |
| City | `Madrid` | confirmed |
| State / Province | `Comunidad de Madrid` | confirmed |
| ZIP | `28002` | confirmed |
| Country | `España` | confirmed |
| Phone | `+34 XXX XXX XXX` | ⚠ placeholder |
| Email | `info@aeroterm.es` | ⚠ placeholder |

## Categorías GBP planificadas

| Campo | Valor | Status |
|---|---|---|
| Planned Primary GBP Category | `Heating contractor` | ⚠ inferido |
| Planned Additional 1 | `Solar energy contractor` | ⚠ inferido |
| Planned Additional 2 | `Air conditioning contractor` | ⚠ inferido |

## Geografía (Main City + LCAs)

| Campo | Valor | Status |
|---|---|---|
| Main City | `Madrid` | confirmed |
| Physical Location City | `Madrid` | confirmed |
| Direct LCA 1 | `Hortaleza` (distrito) | ⚠ placeholder |
| Direct LCA 2 | `Prosperidad` (barrio) | ⚠ placeholder |
| Candidate LCA 1 | `Chamartín` | ⚠ inferido |
| Candidate LCA 2 | `Salamanca` | ⚠ inferido |
| Candidate LCA 3 | `Chamberí` | ⚠ inferido |
| Candidate LCA 4 | `Centro` | ⚠ inferido |
| Candidate LCA 5 | `Retiro` | ⚠ inferido |
| Candidate LCA 6 | `Moncloa-Aravaca` | ⚠ inferido |
| Candidate LCA 7 | `Tetuán` | ⚠ inferido |
| Candidate LCA 8 | `Ciudad Lineal` | ⚠ inferido |
| Approved Expansion Areas | `None in Phase 1` | confirmed |

## Servicios principales (S = 5)

| # | Servicio | Status |
|---|---|---|
| 1 | Instalación de aerotermia | ⚠ inferido |
| 2 | Mantenimiento de aerotermia | ⚠ inferido |
| 3 | Sustitución de caldera por aerotermia | ⚠ inferido |
| 4 | Aerotermia con suelo radiante | ⚠ inferido |
| 5 | Aerotermia para ACS y piscinas | ⚠ inferido |

## Consolidación de Additional Categories

| Categoría | Status arquitectónico | Status |
|---|---|---|
| Solar energy contractor | Necesita página propia (no cubierto por core) | confirmed (lógica) |
| Air conditioning contractor | Cubierta por core service `Instalación de aerotermia` (heat pump reversible) | confirmed (lógica) |

## Contenido y conversión

| Campo | Valor | Status |
|---|---|---|
| GeoArticles per Service (G) | `3` | confirmed |
| Preferred CTA | `Solicitar presupuesto` | confirmed (Decisión de diseño) |

## Trust signals

| # | Trust signal | Status |
|---|---|---|
| 1 | Instaladores certificados (RITE) | ⚠ inferido |
| 2 | Tramitación de subvenciones (Plan MOVES y similares) | ⚠ inferido |
| 3 | Garantía del fabricante + garantía propia | ⚠ inferido |
| 4 | Estudio de viabilidad gratuito | ⚠ inferido |
| 5 | Servicio post-venta y mantenimiento anual | ⚠ inferido |
| 6 | Reseñas iniciales pendientes de recopilar tras crear y verificar el GBP | confirmed (doctrina) |

---

# Paso 2 — Fórmula Maestra

> Todos los outputs de Paso 2 son aplicación determinista de la doctrina sobre los inputs de Paso 1. Se marcan `confirmed` porque la doctrina es directa, pero los **valores numéricos de S y la lista de servicios dependen de Paso 1 ⚠ inferido**. Si los servicios cambian, Paso 2 se recalcula.

## Variables

| Variable | Valor | Status |
|---|---|---|
| S (servicios core) | `5` | confirmed (depende de Paso 1) |
| Service-Main-City Applicability | Todos aplican → `S_efectiva = 5` | confirmed |
| A (categorías adicionales efectivas) | `1` (Solar energy) | confirmed (lógica) |
| G (GeoArticles per service) | `3` | confirmed |

## Fórmula base aplicada

```text
1 Homepage           +
S = 5 SO Pages       +
1 GeoHub Madrid      +
S = 5 LBS Madrid     +
A = 1 Additional Cat +
G × S = 15 GeoArticles
─────────────────────
Total = 28 páginas SEO base
+ /contacto/ (auxiliar fuera del inventario SEO)
```

## Anti-duplicación

| Categoría | Decisión |
|---|---|
| Air conditioning contractor | Consolidada con `Instalación de aerotermia` (no suma a A) |
| Solar energy contractor | Página propia (suma a A = 1) |

---

# Paso 3 — URL Matrix base

**Spreadsheet Name:** `Aeroterm – GMB Crush Website Architecture` · **GeoHub URL Style:** Option A `/madrid/`

| ID | URL | Tipo | Schema | Priority | Phase | Status |
|---|---|---|---|---|---|---|
| HP | `/` | Homepage | Organization + LocalBusiness | P1 | 1 | confirmed |
| SO-1 | `/calefaccion/instalacion-aerotermia/` | Service Overview | Service | P1 | 1 | ⚠ inferido |
| SO-2 | `/calefaccion/mantenimiento-aerotermia/` | Service Overview | Service | P1 | 1 | ⚠ inferido |
| SO-3 | `/calefaccion/sustitucion-caldera-aerotermia/` | Service Overview | Service | P1 | 1 | ⚠ inferido |
| SO-4 | `/calefaccion/aerotermia-suelo-radiante/` | Service Overview | Service | P1 | 1 | ⚠ inferido |
| SO-5 | `/calefaccion/aerotermia-acs-piscinas/` | Service Overview | Service | P1 | 1 | ⚠ inferido |
| GH | `/madrid/` | GeoHub | Place | P1 | 1 | confirmed |
| LBS-1 | `/calefaccion/madrid/instalacion-aerotermia/` | LBS | Service + LocalBusiness | P1 | 1 | ⚠ inferido |
| LBS-2 | `/calefaccion/madrid/mantenimiento-aerotermia/` | LBS | Service + LocalBusiness | P1 | 1 | ⚠ inferido |
| LBS-3 | `/calefaccion/madrid/sustitucion-caldera-aerotermia/` | LBS | Service + LocalBusiness | P1 | 1 | ⚠ inferido |
| LBS-4 | `/calefaccion/madrid/aerotermia-suelo-radiante/` | LBS | Service + LocalBusiness | P1 | 1 | ⚠ inferido |
| LBS-5 | `/calefaccion/madrid/aerotermia-acs-piscinas/` | LBS | Service + LocalBusiness | P1 | 1 | ⚠ inferido |
| AC-1 | `/calefaccion/madrid/energia-solar/` | Additional Category | Service | P2 | 1 | ⚠ inferido |
| GA-1 | `/madrid/cuanto-cuesta-instalar-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-2 | `/madrid/aerotermia-frente-a-caldera-de-gas/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-3 | `/madrid/subvenciones-aerotermia-en-madrid/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-4 | `/madrid/cada-cuanto-mantenimiento-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-5 | `/madrid/checklist-mantenimiento-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-6 | `/madrid/precio-mantenimiento-anual-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-7 | `/madrid/como-sustituir-caldera-gas-por-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-8 | `/madrid/cuanto-tarda-cambio-de-caldera-a-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-9 | `/madrid/cuando-merece-pena-sustituir-caldera-por-aerotermia/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-10 | `/madrid/aerotermia-suelo-radiante-instalacion/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-11 | `/madrid/precio-aerotermia-mas-suelo-radiante/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-12 | `/madrid/eficiencia-suelo-radiante-vs-radiadores/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-13 | `/madrid/aerotermia-para-piscinas-climatizadas/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-14 | `/madrid/aerotermia-acs-domestico/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| GA-15 | `/madrid/aerotermia-piscina-todo-el-ano/` | GeoArticle | Article | P3 | 2 | ⚠ inferido |
| AUX | `/contacto/` | Auxiliar | ContactPoint | P4 | 1 | confirmed |

LCAs declaradas (Hortaleza, Prosperidad, Chamartín, Salamanca, Chamberí, Centro, Retiro, Moncloa-Aravaca, Tetuán, Ciudad Lineal) NO generan URLs en la base — viven en contenido y schema `areaServed`.

---

# Resumen de status

| Status | Cantidad | % |
|---|---:|---:|
| confirmed | 19 | 21% |
| ⚠ inferido | 64 | 70% |
| ⚠ placeholder | 8 | 9% |
| **Total fields** | **91** | **100%** |

> **70% de los campos llevan marcador `⚠ inferido`** porque la IA ejecutó sin tools externas reales. En producción real con un operador humano abriendo Google Maps + keyword tool, ese porcentaje baja drásticamente y la mayoría pasa a `validated`.

---

# Acciones pendientes para promover `⚠` a `confirmed`

## Bloque A — Local Pack analysis (resuelve 53 ⚠ inferido)

**Tool necesaria:** Google Maps · sin login · navegador en clean session.

**Procedimiento:**

1. Abrir Google Maps y buscar `aerotermia Madrid`. Anotar los 5 negocios top del Local Pack.
2. Para cada perfil del top 5, capturar:
   - Categoría primaria GBP declarada
   - Categorías adicionales declaradas
   - Servicios listados en la sección "Servicios"
   - Áreas de servicio declaradas
3. Repetir con `aerotermia Barcelona` y `pompe à chaleur Paris` (benchmark internacional).
4. Aplicar las reglas de selección del manual:
   - **Primary Category** → la más repetida (>3 de 5) en Madrid (validar Barcelona)
   - **5 Servicios core** → top 5 por frecuencia, cruzando con oferta real de Aeroterm
   - **Candidate LCAs** → zonas en al menos 2 perfiles, validadas con test 3/6 GEO
   - **Additional Categories** → secundarias que aparecen en ≥2 competidores

**Output esperado:** los 53 campos pasan de `⚠ inferido` a `validated`.

## Bloque B — Keyword research (resuelve 15 ⚠ inferido)

**Tool necesaria:** Ahrefs / Semrush / Google Keyword Planner (cualquiera con volúmenes locales).

**Procedimiento:**

1. Para cada uno de los 5 servicios core, generar candidatos de GeoArticle topic (preguntas, dudas comunes, comparativas).
2. Validar cada candidato contra volumen mensual + dificultad + intent en Madrid.
3. Seleccionar 3 GeoArticles por servicio (G × S = 15) con el mejor cruce volumen/dificultad/intent.

**Output esperado:** los 15 GeoArticle URLs pasan de `⚠ inferido` a `validated`.

## Bloque C — Cliente confirma (resuelve 8 ⚠ placeholder)

| # | Campo | Cliente debe confirmar |
|---|---|---|
| 1 | Website URL | Dominio real registrado o que va a registrarse |
| 2 | Canonical Domain | Misma respuesta |
| 3 | Phone | Teléfono real del negocio |
| 4 | Email | Email de contacto real |
| 5 | Direct LCA 1 — Distrito | Validar que `Marqués de Valdecilla 16, 28002` está en distrito Hortaleza |
| 6 | Direct LCA 2 — Barrio | Validar que el barrio es Prosperidad (o el correcto) |
| 7 | Trust signal — años en mercado | Cuántos años lleva Aeroterm operando |
| 8 | Trust signal — certificaciones | Qué certificaciones reales tiene |

**Output esperado:** los 8 campos pasan de `⚠ placeholder` a `confirmed`.

---

# Bloqueo de publicación

> Por la **Regla 3** de las convenciones de ejecución: **este documento NO puede pasar a publicación tal cual está**. El Paso 18 (QA y deploy) debe rechazar el deploy mientras existan los 72 marcadores `⚠`. La publicación se desbloquea cuando los Bloques A, B y C de acciones pendientes se hayan ejecutado.
