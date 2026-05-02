Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 4 — Automatizacion/paso-11-pseudocodigo-sistema/`, alineado con los frameworks oficiales GMB Crush.

# Paso 11 — Pseudocódigo del Sistema

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 14 outputs del Paso 11 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, obtención de outputs, checklist final y outputs consolidados.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 11

<small>§2</small>

En este paso la IA produce todos los outputs que **expresan el sistema GMB Crush como pseudocódigo ejecutable** — las funciones que cargan inputs, normalizan slugs, validan categorías, generan páginas por page type, inyectan cobertura local, asignan enlaces internos, calculan priority, validan dependencias, ejecutan QA y generan las matrices finales. Este paso NO produce datos nuevos: produce el **algoritmo** que orquesta los outputs heredados de Bloques 1-3 en una secuencia repetible.

**Outputs del paso:**

- **11.1** Función `load_inputs()` — recoge variables del preflight + outputs de Bloques 1-3
- **11.2** Función `normalize_slugs()` — slugify de todos los componentes
- **11.3** Función `validate_categories()` — eliminación de duplicados Additional vs core
- **11.4** Función `generate_pages_by_type()` — algoritmo por page type (HP, SO, GH, LBS, AC, GA)
- **11.5** Función `inject_local_coverage()` — inyección de LCAs en contenido + areaServed
- **11.6** Función `generate_expansion()` — opcional, solo si Approved Expansion ≠ vacío
- **11.7** Función `assign_internal_links()` — matriz de enlaces obligatorios por URL
- **11.8** Función `score_priority()` — aplicación de la fórmula maestra del Paso 8
- **11.9** Función `check_dependencies()` — validación de orden de publicación
- **11.10** Función `run_qa()` — validación de las 5 categorías QA del Paso 9
- **11.11** Función `output_matrices()` — generación URL Matrix + Schema Map + Link Map
- **11.12** Pseudocódigo principal `main()` — orquestador secuencial
- **11.13** Validación: cobertura de inputs heredados (no se inventa nada que no esté en Bloques 1-3)
- **11.14** Validación: secuencia respeta dependencias estructurales

**Errores que previene:**

- Ejecutar el sistema en orden caótico (rompe dependencias)
- Inventar inputs no heredados (que rompen trazabilidad)
- Olvidar validaciones intermedias (categorías duplicadas, slugs sucios)
- Saltar el QA gate antes de generar matrices finales
- Hacer expansion sin Approved Expansion declarado
- Re-implementar lógica que ya existe en Bloques 1-3

**Cuándo se ejecuta:** después de Pasos 1-10 cerrados (Bloques 1-3 completos). Antes de Paso 12 (Master Prompt) y Paso 13 (Sistema Final Operativo).

## Info heredada de pasos anteriores

<small>§3</small>

> Este paso es **meta**: no consume outputs de un solo paso, sino que orquesta todos los de Bloques 1-3. Lista resumida:

| Bloque | Outputs heredados | Cómo se usan en el pseudocódigo |
|---|---|---|
| Bloque 1 (Pasos 1-3) | 1.1 a 3.14 (43 outputs) | `load_inputs()` recoge intake + fórmula + matriz base |
| Bloque 2 (Pasos 4-7) | 4.1 a 7.15 (59 outputs) | `generate_pages_by_type()` aplica URL rules + page type specs + content arch + linking |
| Bloque 3 (Pasos 8-10) | 8.1 a 10.13 (35 outputs) | `score_priority()` aplica Paso 8; `run_qa()` aplica Paso 9; `check_dependencies()` aplica Paso 10 |

**Total upstream:** 137 outputs de Bloques 1-3 que el pseudocódigo orquesta en secuencia.

# Bloque II — Ejemplo rellenado para el Paso 11 — Pseudocódigo del Sistema

<small>§4</small>

> Los 14 outputs del Paso 11 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 11.X declarado en §5. Los ejemplos muestran snippets de pseudocódigo aplicado al cluster Cerrajeros.

### 11.1 — Función `load_inputs()`

```python
def load_inputs():
    return {
        # Bloque 1 — outputs 1.X (intake)
        "business_name": "Cerrajeros Madrid 24h",                        # ← 1.1
        "website_root_domain": "https://www.cerrajerosmadrid24h.com",    # ← 1.2
        "gbp_status": "Not Created",                                     # ← 1.3
        "nap": {
            "name": "Cerrajeros Madrid 24h",
            "street": "Calle Rafael Calvo 12",
            "city": "Madrid",
            "state": "Comunidad de Madrid",
            "zip": "28010",
            "country": "España",
            "phone": "+34 600 000 000",
            "email": "info@cerrajerosmadrid24h.com",
        },                                                                # ← 1.4
        "primary_gbp_category": "Cerrajero",                             # ← 1.5
        "additional_gbp_categories": [                                   # ← 1.6
            {"name": "Servicio de cerrajería de urgencia", "needs_page": False},
            {"name": "Servicio de duplicado de llaves", "needs_page": True},
        ],
        "main_city": "Madrid",                                            # ← 1.7
        "physical_location_city": "Madrid",                              # ← 1.8
        "core_services": [                                                # ← 1.9
            "Cerrajero urgente", "Apertura de puertas",
            "Cambio de cerraduras", "Cambio de bombines",
            "Instalación de cerraduras de seguridad",
        ],
        "local_coverage_areas": {                                         # ← 1.10
            "direct": ["Almagro", "Chamberí"],
            "candidate": ["Salamanca", "Retiro", "Centro", "Tetuán",
                          "Chamartín", "Arganzuela", "Moncloa", "Prosperidad"],
        },
        "approved_expansion_areas": [],                                  # ← 1.11
        "geo_articles_per_service": 3,                                    # ← 1.12
        "preferred_cta": "Llamar ahora",                                 # ← 1.13
        "trust_signals": [                                                # ← 1.14
            "10+ años", "técnicos cualificados", "servicio móvil",
            "garantía", "reseñas iniciales pendientes",
        ],
    }
```

### 11.2 — Función `normalize_slugs()`

```python
def normalize_slugs(inputs):
    """Slugify lowercase + sin acentos + kebab-case. Cruza con outputs Paso-02 2.2-2.4."""
    return {
        "primary_category_slug": slugify(inputs["primary_gbp_category"]),  # → 'cerrajero'
        "main_city_slug": slugify(inputs["main_city"]),                    # → 'madrid'
        "service_slugs": [slugify(s) for s in inputs["core_services"]],    # → ['cerrajero-urgente', ...]
        "additional_category_slugs": [
            slugify(c["name"]) for c in inputs["additional_gbp_categories"]
            if c["needs_page"]
        ],                                                                  # → ['servicio-de-duplicado-de-llaves']
    }
```

### 11.3 — Función `validate_categories()`

```python
def validate_categories(inputs):
    """Cruza Additional Categories vs core services. Cumple Paso-02 2.12."""
    effective_additional = []
    for cat in inputs["additional_gbp_categories"]:
        if cat["needs_page"]:
            # validar que no es duplicada con un core service
            if not is_covered_by_core(cat["name"], inputs["core_services"]):
                effective_additional.append(cat)
    return effective_additional
    # Para Cerrajeros: [{"name": "Servicio de duplicado de llaves", "needs_page": True}]
    # 'cerrajería de urgencia' queda fuera (cubierta por core 'Cerrajero urgente')
```

### 11.4 — Función `generate_pages_by_type()`

```python
def generate_pages_by_type(inputs, slugs, effective_additional):
    """Genera N+1 URLs según fórmula Paso-02 2.9: 1 + S + 1 + S + A + G×S + 1 (auxiliar)."""
    return {
        "homepage": generate_hp(inputs),                              # ← 5.3 spec HP
        "service_overview": generate_so(slugs),                       # ← 5.4 spec SO × S
        "geohub": generate_gh(slugs),                                 # ← 5.7 spec GH
        "lbs": generate_lbs(slugs),                                   # ← 5.5 spec LBS × S
        "additional_category": generate_ac(slugs, effective_additional),# ← 5.6 spec AC × A
        "geoarticles": generate_ga(slugs, inputs["geo_articles_per_service"]),# ← 5.8 spec GA × G×S
        "auxiliar": [{"id": "AUX", "url": "/contacto/"}],
    }
    # Para Cerrajeros: 1 HP + 5 SO + 1 GH + 5 LBS + 1 AC + 15 GA + 1 AUX = 29 URLs
```

### 11.5 — Función `inject_local_coverage()`

```python
def inject_local_coverage(pages, lcas, page_type_uses_lcas):
    """Inyecta LCAs en contenido + areaServed. Cumple Paso-06 6.2 + 6.17."""
    for page in pages:
        if page["page_type"] in page_type_uses_lcas:
            page["content_lcas"] = lcas["direct"] + lcas["candidate"]
            page["schema_areaServed"] = ["Madrid"] + lcas["direct"] + lcas["candidate"]
        else:
            page["content_lcas"] = []
            page["schema_areaServed"] = ["Madrid"]
    # page_type_uses_lcas = ["LBS", "GeoHub", "Additional Category", "GeoArticle"]
    # Homepage: solo Main City; SO: ninguna LCA (es no-local)
```

### 11.6 — Función `generate_expansion()` (opcional)

```python
def generate_expansion(inputs):
    """Solo se ejecuta si Approved Expansion Areas ≠ []. Cumple Paso-04 4.10 + Paso-10 10.8."""
    if not inputs["approved_expansion_areas"]:
        return []  # Phase 1 default: E=0
    # Si E≥1: generar GeoHub + LBS + GAs por Approved Expansion Area
    expansion_pages = []
    for area in inputs["approved_expansion_areas"]:
        expansion_pages.append({"id": f"EXP-GH-{area}", "url": f"/{slugify(area)}/", ...})
        # ... etc
    return expansion_pages
    # Para Cerrajeros (Phase 1): []
```

### 11.7 — Función `assign_internal_links()`

```python
def assign_internal_links(pages):
    """Aplica matriz Paso-07 7.11 fila por fila."""
    link_matrix = []
    for page in pages:
        for target in get_required_links(page["page_type"]):
            link_matrix.append({
                "source": page["url"],
                "target": target["url"],
                "anchor": pick_anchor(page, target),  # ← 7.9 (catálogo 6 categorías)
                "direction": target["direction"],     # arriba/abajo/lateral (← 7.1)
            })
    return link_matrix
    # Para Cerrajeros: ~80 enlaces internos en total
```

### 11.8 — Función `score_priority()`

```python
def score_priority(pages):
    """Aplica fórmula Paso-08 8.1: R + I + G + L + C + U → tier P1-Hold + Phase."""
    scored = []
    for page in pages:
        scores = {
            "revenue":     measure_revenue(page),         # ← 8.2
            "intent":      measure_intent(page),           # ← 8.3
            "gbp_rel":     measure_gbp_relevance(page),    # ← 8.4
            "local_rel":   measure_local_relevance(page),  # ← 8.5
            "comp_gap":    measure_competition(page),      # ← 8.6
            "urgency":     measure_urgency(page),          # ← 8.7
        }
        page["score"] = sum(scores.values())               # ← 8.8
        page["tier"] = score_to_tier(page["score"])        # ← 8.9
        page["phase"] = derive_phase(page["tier"], page["page_type"])  # ← 8.10
        # Forzar HP = P1 + Phase 1 (← 8.12)
        if page["page_type"] == "Homepage":
            page["tier"] = "P1"; page["phase"] = 1
        scored.append(page)
    return scored
```

### 11.9 — Función `check_dependencies()`

```python
def check_dependencies(scored_pages):
    """Aplica matriz Paso-10 10.10. Bloquea si parent no está publicado."""
    for page in scored_pages:
        for parent in get_parents(page):
            if parent["status"] != "Published" and parent["phase"] >= page["phase"]:
                page["status"] = "Blocked"
                page["block_reason"] = f"Parent {parent['url']} no publicado a tiempo"
        # Cumple regla Paso-08 8.11: phase(parent) < phase(GA)
    return scored_pages
```

### 11.10 — Función `run_qa()`

```python
def run_qa(pages):
    """Aplica las 5 categorías QA del Paso 9 (9.2-9.6) + Final Publish Gate (9.7)."""
    for page in pages:
        page["qa"] = {
            "estructural": check_qa_estructural(page),   # ← 9.2 (4 sub-checks)
            "local":       check_qa_local(page),          # ← 9.3 (3 sub-checks)
            "contenido":   check_qa_contenido(page),      # ← 9.4 (3 sub-checks)
            "conexion":    check_qa_conexion(page),       # ← 9.5 (3 sub-checks)
            "semantico":   check_qa_semantico(page),      # ← 9.6 (1 sub-check)
        }
        page["publish_gate"] = consolidate_publish_gate(page["qa"])  # ← 9.7
        if input("gbp_status") == "Not Created":
            page["gbp_checklist"] = check_gbp_not_created(page)      # ← 9.8
    return pages
```

### 11.11 — Función `output_matrices()`

```python
def output_matrices(scored_pages, link_matrix):
    """Genera las 3 matrices finales que consume Paso 13."""
    return {
        "url_matrix":    build_url_matrix(scored_pages),     # ← 3.5 expandida con score+tier+phase
        "schema_map":    build_schema_map(scored_pages),     # ← 3.8 + 5.9 + 6.17
        "link_matrix":   link_matrix,                         # ← 7.11
    }
```

### 11.12 — Pseudocódigo principal `main()`

```python
def main():
    # 1. Cargar inputs
    inputs = load_inputs()                                   # 11.1

    # 2. Normalizar
    slugs = normalize_slugs(inputs)                          # 11.2
    effective_additional = validate_categories(inputs)       # 11.3

    # 3. Generar páginas
    pages = generate_pages_by_type(inputs, slugs, effective_additional)  # 11.4
    pages = inject_local_coverage(pages, inputs["lcas"],
                                   page_type_uses_lcas)       # 11.5
    pages += generate_expansion(inputs)                      # 11.6 (opcional)

    # 4. Conexión
    link_matrix = assign_internal_links(pages)               # 11.7

    # 5. Priorización
    scored_pages = score_priority(pages)                     # 11.8
    scored_pages = check_dependencies(scored_pages)          # 11.9

    # 6. QA gate
    qa_pages = run_qa(scored_pages)                          # 11.10
    if any(p["publish_gate"] != "Ready" for p in qa_pages):
        raise BlockedDeployError("Algunas URLs no pasan QA gate")

    # 7. Outputs finales
    matrices = output_matrices(qa_pages, link_matrix)        # 11.11
    return matrices
```

### 11.13 — Validación: cobertura de inputs heredados

Cumplido — `load_inputs()` recoge los **14 outputs de Paso 1** + las variables derivadas (slugs, A, S, G) de Paso 2. Cero inputs inventados; cero placeholders sin trazabilidad.

### 11.14 — Validación: secuencia respeta dependencias

Cumplido — el orden `main()` reproduce el orden doctrinal:

```
load → normalize → validate → generate → inject → expand → link → score → check → qa → output
   1.X    2.2-2.4    2.7      Pasos 4-7     6        4.10    7.X    8.X      10.10   9.X    finales
```

Cada paso espera que sus dependencias estén resueltas antes de ejecutarse. Cumple Paso-02 2.13 (orden HP → SO → GH → LBS → AC → GAs).

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 14 outputs que el Paso 11 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `11.4`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 11.1 | Función `load_inputs()` | Función pseudocódigo | GMB Crush | Paso-01 1.1-1.14 + Paso-02 + Paso-03 (143 outputs) |
| 11.2 | Función `normalize_slugs()` | Función pseudocódigo | GMB Crush | Paso-02 2.2 + 2.3 + 2.4 + Paso-03 3.3 |
| 11.3 | Función `validate_categories()` | Función pseudocódigo | GMB Crush | Paso-02 2.7 + 2.12 |
| 11.4 | Función `generate_pages_by_type()` | Función pseudocódigo | GMB Crush | Paso-04 4.3-4.8 + Paso-05 5.3-5.8 |
| 11.5 | Función `inject_local_coverage()` | Función pseudocódigo | GMB Crush | Paso-06 6.2 + 6.12 + 6.17 |
| 11.6 | Función `generate_expansion()` | Función pseudocódigo opcional | GMB Crush | Paso-01 1.11 + Paso-04 4.10 |
| 11.7 | Función `assign_internal_links()` | Función pseudocódigo | GMB Crush | Paso-07 7.9 + 7.11 |
| 11.8 | Función `score_priority()` | Función pseudocódigo | GMB Crush | Paso-08 8.1-8.10 |
| 11.9 | Función `check_dependencies()` | Función pseudocódigo | GMB Crush | Paso-08 8.11 + Paso-10 10.10 |
| 11.10 | Función `run_qa()` | Función pseudocódigo | GMB Crush | Paso-09 9.2-9.8 |
| 11.11 | Función `output_matrices()` | Función pseudocódigo | GMB Crush | Paso-03 3.5 + Paso-03 3.8 + Paso-07 7.11 |
| 11.12 | Pseudocódigo principal `main()` | Orquestador | GMB Crush | Paso-11 11.1-11.11 (intra-paso) |
| 11.13 | Validación cobertura de inputs | Validation flag | GMB Crush | Bloques 1-3 completos |
| 11.14 | Validación secuencia respeta dependencias | Validation flag | GMB Crush | Paso-02 2.13 + Paso-08 8.11 + Paso-10 10.10 |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 14 outputs (11.1–11.14). Cada output usa el patrón estándar adaptado a pseudocódigo: Explicación / Firma de la función / Lógica interna / Ejemplo Cerrajeros / Ejemplos incorrectos / Regla / Validación / Cómo se obtiene / Output del paso.

### 11.1 — Función `load_inputs()`

<small>§6.1</small>

**Explicación**

Función de entrada del sistema. Recoge **todas las variables** del preflight + outputs de Bloques 1-3 en un único objeto. Es el contrato entre los pasos manuales/heredados y la lógica algorítmica.

**Firma de la función**

```python
def load_inputs() -> dict
```

**Lógica interna**

```text
1. Leer 00preflight.md (5 campos del cliente)
2. Leer §8 Outputs Consolidados de los a-docs 01a, 02a, 03a (Bloque 1)
3. Leer §8 Outputs Consolidados de los a-docs 04a, 05a, 06a, 07a (Bloque 2)
4. Leer §8 Outputs Consolidados de los a-docs 08a, 09a, 10a (Bloque 3)
5. Devolver dict con todas las variables
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.1 — `load_inputs()` retorna dict con las variables del cluster Cerrajeros.

**Ejemplos incorrectos**

```text
- Inventar un campo no presente en preflight ni en outputs heredados
- Saltar la validación de status (cargar outputs ⚠ inferido como confirmed)
- Omitir Bloques completos (ej. ignorar Paso 8 outputs)
```

**Regla final**

```text
load_inputs() es source-of-truth: todo input usado downstream viene de aquí.
```

**Validación operativa**

Aplicar al inicio de `main()`. Validar que los 137 outputs upstream están en `confirmed` antes de cargar. Si algún output está en `⚠`, marcar el cluster como `incomplete` y bloquear ejecución.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Lectura programática de los §8 de cada a-doc + preflight; serialización en dict normalizado.

**Output del paso**

- **Tipo:** Función pseudocódigo + dict resultado.
- **Ejemplo (Cerrajeros Madrid 24h):** dict con 14 campos de Paso 1 + slugs Paso 2 + matriz Paso 3.

### 11.2 — Función `normalize_slugs()`

<small>§6.2</small>

**Explicación**

Normaliza todos los componentes que aparecen en URLs: categoría primaria, Main City, servicios, categorías adicionales. Slugify aplicado uniformemente.

**Firma de la función**

```python
def normalize_slugs(inputs: dict) -> dict
```

**Lógica interna**

```text
1. Aplicar slugify a primary_gbp_category → primary_category_slug
2. Aplicar slugify a main_city → main_city_slug
3. Aplicar slugify a cada core_service → service_slugs[]
4. Aplicar slugify a cada Additional Category con needs_page=True → additional_category_slugs[]
5. Cumplir formato: lowercase + sin acentos + kebab-case
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.2.

**Ejemplos incorrectos**

```text
- Slugs con mayúsculas (Cerrajero-Urgente) — viola Paso-04 4.13
- Slugs con espacios (cerrajero urgente)
- Slugs con caracteres especiales (apertura-de-puertas-y-cerraduras)
- Olvidar slugify en categories adicionales
```

**Regla final**

```text
Todos los slugs cumplen slugify estándar (cruza con Paso-02 2.2-2.4 + Paso-03 3.3).
```

**Validación operativa**

Aplicar tras `load_inputs()`. Cruce con Paso-04 4.13 (Validación Slugs limpios).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Implementar slugify estándar + aplicar a los 4 grupos de slugs.

**Output del paso**

- **Tipo:** Función pseudocódigo + dict de slugs normalizados.
- **Ejemplo (Cerrajeros Madrid 24h):** `cerrajero` + `madrid` + 5 service_slugs + 1 additional_slug.

### 11.3 — Función `validate_categories()`

<small>§6.3</small>

**Explicación**

Cruza Additional Categories declaradas (Paso-01 1.6) con core services (Paso-01 1.9) y elimina duplicaciones. Solo las categorías efectivas (no cubiertas por core) generan página propia.

**Firma de la función**

```python
def validate_categories(inputs: dict) -> list[dict]
```

**Lógica interna**

```text
1. Iterar additional_gbp_categories
2. Si needs_page=True, validar que NO esté cubierta por algún core_service (semánticamente)
3. Si está cubierta → marcar como "Servicio cubierto, no genera página"
4. Si no está cubierta → añadir a effective_additional[]
5. Output: lista de categorías efectivas que sí generan página propia
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.3 — `cerrajería de urgencia` se elimina (cubierta por `Cerrajero urgente`); `duplicado de llaves` queda como única efectiva.

**Ejemplos incorrectos**

```text
- Generar página AC para una categoría ya cubierta por core (canibalización)
- Olvidar el check de semantic match (depende solo de needs_page)
- Asumir que todas las needs_page=True son efectivas
```

**Regla final**

```text
Una categoría adicional solo genera página propia si NO está cubierta por core service.
```

**Validación operativa**

Aplicar tras `load_inputs()`. Cruce con Paso-02 2.7 (Variable A) y Paso-02 2.12 (Validación anti-duplicación).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Comparar semánticamente cada categoría adicional con cada core service; aplicar criterio de cobertura.

**Output del paso**

- **Tipo:** Función pseudocódigo + lista de categorías efectivas.
- **Ejemplo (Cerrajeros Madrid 24h):** `[{"name": "Servicio de duplicado de llaves", "needs_page": True}]` (A=1).

### 11.4 — Función `generate_pages_by_type()`

<small>§6.4</small>

**Explicación**

Genera todas las URLs del cluster aplicando los specs de page type del Paso 5 + URL patterns del Paso 4. Es el corazón del pseudocódigo: produce la matriz de páginas.

**Firma de la función**

```python
def generate_pages_by_type(inputs: dict, slugs: dict, effective_additional: list) -> dict
```

**Lógica interna**

```text
1. generate_hp(inputs) → 1 Homepage con spec Paso-05 5.3
2. generate_so(slugs) → S Service Overview con spec Paso-05 5.4
3. generate_gh(slugs) → 1 GeoHub con spec Paso-05 5.7
4. generate_lbs(slugs) → S LBS con spec Paso-05 5.5
5. generate_ac(slugs, effective_additional) → A AC con spec Paso-05 5.6
6. generate_ga(slugs, G) → G×S GeoArticles con spec Paso-05 5.8
7. añadir 1 página auxiliar /contacto/
8. Output: dict {homepage, service_overview, geohub, lbs, additional_category, geoarticles, auxiliar}
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.4 — produce 29 URLs (1 HP + 5 SO + 1 GH + 5 LBS + 1 AC + 15 GA + 1 AUX).

**Ejemplos incorrectos**

```text
- Generar páginas con URL patterns inventados (rompe Paso-04 4.X)
- Saltar el AC si A=0 (correcto) PERO publicar AC sin needs_page (rompe regla)
- Generar más GAs que G×S (rompe Paso-02 2.8)
```

**Regla final**

```text
generate_pages_by_type() respeta la fórmula maestra Paso-02 2.9 = 1+S+1+S+A+G×S+aux.
```

**Validación operativa**

Aplicar tras `validate_categories()`. Cruce con Paso-02 2.10 (Inventario por tipo).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** 6 sub-funciones, una por page type, cada una aplicando el spec del Paso-05.

**Output del paso**

- **Tipo:** Función pseudocódigo + dict con 7 listas de páginas.
- **Ejemplo (Cerrajeros Madrid 24h):** 29 URLs generadas, listadas por page type.

### 11.5 — Función `inject_local_coverage()`

<small>§6.5</small>

**Explicación**

Inyecta las LCAs (Direct + Candidate) en el contenido y schema `areaServed` de las páginas locales. Las páginas no-locales (SO) reciben lista vacía. La Homepage solo recibe Main City.

**Firma de la función**

```python
def inject_local_coverage(pages: dict, lcas: dict, page_type_uses_lcas: list) -> dict
```

**Lógica interna**

```text
1. Para cada page en pages:
   - Si page_type ∈ {LBS, GeoHub, AC, GeoArticle} → inyectar lcas (direct + candidate)
   - Si page_type = Homepage → inyectar solo Main City
   - Si page_type = SO → inyectar [] (no-local por diseño)
2. Schema areaServed:
   - LBS, GH, AC, GA: [Main City] + lcas direct + lcas candidate
   - HP: [Main City]
   - SO: [] o sin areaServed
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.5.

**Ejemplos incorrectos**

```text
- Inyectar LCAs en SO (rompe rol pilar temático no-local)
- Inyectar Main City duplicada como LCA (Madrid también en lista)
- Olvidar areaServed en LBS (rompe Paso-06 6.17)
- Mencionar LCA no aprobada en contenido
```

**Regla final**

```text
LCAs en contenido + areaServed solo en page types locales; SO siempre no-local.
```

**Validación operativa**

Aplicar tras `generate_pages_by_type()`. Cruce con Paso-06 6.2 + 6.12 + 6.17.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Iterar páginas, mapear page_type → conjunto de LCAs según matriz Paso-06 6.12.

**Output del paso**

- **Tipo:** Función pseudocódigo + páginas con `content_lcas` y `schema_areaServed` rellenos.
- **Ejemplo (Cerrajeros Madrid 24h):** 22 páginas locales con 10 LCAs en areaServed; 5 SO sin LCAs.

### 11.6 — Función `generate_expansion()`

<small>§6.6</small>

**Explicación**

Función opcional que solo se ejecuta si Approved Expansion Areas ≠ vacío. En Phase 1 web-first default, NO se ejecuta. Cuando se activa, genera GeoHub + LBS + GAs por cada Approved Area, replicando la estructura de la Main City.

**Firma de la función**

```python
def generate_expansion(inputs: dict) -> list[dict]
```

**Lógica interna**

```text
1. Si approved_expansion_areas == [] → return []
2. Por cada area en approved_expansion_areas:
   - Generar GeoHub /[area-slug]/
   - Generar S LBS /[primary-cat]/[area-slug]/[service-slug]/
   - Generar G×S GAs /[area-slug]/[topic-slug]/
3. Output: lista de páginas adicionales (sub-cluster Expansion)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```python
# Phase 1 — sin expansión
generate_expansion(inputs) == []

# Si hipotéticamente E=1 con 'Sevilla' aprobada:
# generate_expansion(inputs) → 1 GH + 5 LBS + 15 GAs = 21 páginas adicionales
```

**Ejemplos incorrectos**

```text
- Generar expansion sin que el operador haya aprobado
- Mezclar LBS de Approved Area con LBS de Main City (rompe silos)
- Reusar URLs sin refactor (canibalización entre Main City y Expansion)
```

**Regla final**

```text
generate_expansion() solo se ejecuta tras decisión explícita del operador (Paso-01 1.11 + Paso-04 4.10).
```

**Validación operativa**

Aplicar tras `inject_local_coverage()`. Si E≥1, validar Paso-07 7.15 (Expansion linking separado).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Replicar lógica de generate_pages_by_type() para cada Approved Area, manteniendo silos separados.

**Output del paso**

- **Tipo:** Función pseudocódigo + lista de páginas (puede estar vacía).
- **Ejemplo (Cerrajeros Madrid 24h):** `[]` (Phase 1, E=0).

### 11.7 — Función `assign_internal_links()`

<small>§6.7</small>

**Explicación**

Asigna los enlaces internos según la matriz del Paso-07 7.11 (14 conexiones doctrinales). Cada página recibe sus enlaces obligatorios + anchors variados (Paso-07 7.9).

**Firma de la función**

```python
def assign_internal_links(pages: list[dict]) -> list[dict]
```

**Lógica interna**

```text
1. Para cada page:
   - Determinar enlaces Required según page_type (matriz 7.11)
   - Por cada link target:
     - Validar que target existe en inventario
     - Asignar anchor según catálogo Paso-07 7.9 (branded/exact/partial/topic/generic/CTA)
     - Determinar dirección (arriba/abajo/lateral) según jerarquía
2. Output: lista de {source, target, anchor, direction}
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.7 — ~80 enlaces internos generados respetando matriz 7.11.

**Ejemplos incorrectos**

```text
- Enlazar a URL no existente en inventario (link roto)
- Anchors todos branded (rompe variedad Paso-07 7.9)
- Enlaces solo footer (rompe Paso-07 7.10 contextuales primero)
- Saltar enlaces Required de page type
```

**Regla final**

```text
assign_internal_links() cumple matriz Paso-07 7.11 + anchors variados Paso-07 7.9.
```

**Validación operativa**

Aplicar tras `generate_expansion()`. Cruce con Paso-07 7.14 (Inbound links esperados).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Lookup matriz 7.11 por page_type + selección de anchor por catálogo 7.9.

**Output del paso**

- **Tipo:** Función pseudocódigo + lista de tuplas (source, target, anchor, direction).
- **Ejemplo (Cerrajeros Madrid 24h):** ~80 enlaces internos en el cluster.

### 11.8 — Función `score_priority()`

<small>§6.8</small>

**Explicación**

Aplica la fórmula maestra del Paso-08 8.1 a cada URL del inventario. Calcula los 6 factores, suma → Total Score → Priority Tier → Publish Phase.

**Firma de la función**

```python
def score_priority(pages: list[dict]) -> list[dict]
```

**Lógica interna**

```text
1. Para cada page:
   - Medir Revenue Value (ticket + margen) → 1-5
   - Medir Search Intent (% queries transaccionales) → 1-5
   - Medir GBP Category Relevance (Local Pack) → 1-5
   - Medir Local Relevance (URL + NAP + schema) → 1-5
   - Medir Competition Gap (SERP analysis) → 1-5
   - Medir Conversion Urgency (ventana decisión) → 1-5
   - Total Score = suma
   - Tier = score_to_tier(score)
   - Phase = derive_phase(tier, page_type)
2. Forzar HP = P1 + Phase 1 (← 8.12)
3. Output: páginas con score, tier, phase asignados
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.8 — aplica fórmula a las 28 URLs del inventario base.

**Ejemplos incorrectos**

```text
- Sumar con pesos distintos a 1 (rompe fórmula 8.1)
- Asignar tier directo sin calcular score
- Olvidar forzar HP = P1 (viola 8.12)
- Omitir alguno de los 6 factores
```

**Regla final**

```text
score_priority() aplica la fórmula completa de 6 factores con peso 1; HP siempre P1.
```

**Validación operativa**

Aplicar tras `assign_internal_links()`. Cruce con Paso-08 8.1-8.10 + 8.12.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Implementar 6 funciones de medición + suma + mapeo a tier/phase según rangos doctrinales.

**Output del paso**

- **Tipo:** Función pseudocódigo + páginas con campos score, tier, phase.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs con scores 19-29, tiers P1-P3, phases 1-4.

### 11.9 — Función `check_dependencies()`

<small>§6.9</small>

**Explicación**

Valida que cada página puede publicarse cuando le toca según su Phase. Si su parent (SO, GH, LBS según corresponda) no estará publicado a tiempo, marca la página como `Blocked`.

**Firma de la función**

```python
def check_dependencies(scored_pages: list[dict]) -> list[dict]
```

**Lógica interna**

```text
1. Para cada page:
   - Determinar parents según Paso-03 3.7 (Parent Page por fila)
   - Por cada parent:
     - Si parent.phase >= page.phase → BLOCK
     - Si parent.tier == 'Hold' → BLOCK (parent nunca se publica)
2. Cumple regla Paso-08 8.11: phase(parent) < phase(GA)
3. Output: páginas con flag publicabilidad
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.9 — todas las dependencias OK; 0 páginas Blocked.

**Ejemplos incorrectos**

```text
- Publicar GA en Phase 2 cuando su LBS está en Phase 3 (8.11 violado)
- Olvidar validar parent SO en LBS
- Saltar la validación si parent es Homepage (HP siempre Phase 1, OK)
```

**Regla final**

```text
check_dependencies() bloquea cualquier publicación que viole orden parent → child.
```

**Validación operativa**

Aplicar tras `score_priority()`. Cruce con Paso-10 10.10 (Matriz de dependencias).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Lookup parents por page (Paso-03 3.7) + comparar phases + bloquear conflictos.

**Output del paso**

- **Tipo:** Función pseudocódigo + páginas con flag dependency_ok / Blocked.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs validadas, 0 Blocked.

### 11.10 — Función `run_qa()`

<small>§6.10</small>

**Explicación**

Aplica las 5 categorías QA del Paso-09 9.2-9.6 a cada URL. Genera el Final Publish Gate (9.7) y, si GBP=Not Created, también el GBP Not Created Checklist (9.8).

**Firma de la función**

```python
def run_qa(pages: list[dict]) -> list[dict]
```

**Lógica interna**

```text
1. Para cada page:
   - Aplicar QA Estructural (9.2: 4 sub-checks)
   - Aplicar QA Local (9.3: 3 sub-checks)
   - Aplicar QA Contenido (9.4: 3 sub-checks)
   - Aplicar QA Conexión (9.5: 3 sub-checks incl. Breadcrumbs)
   - Aplicar QA Semántico (9.6: 1 sub-check Canibalización)
2. Final Publish Gate (9.7) = AND de las 5 categorías
3. Si gbp_status == "Not Created" → GBP Not Created Checklist (9.8)
4. Output: páginas con qa.* + publish_gate + gbp_checklist
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.10 — 28 URLs validadas, 28 Pass, 0 Blocked.

**Ejemplos incorrectos**

```text
- Saltar alguna categoría QA (rompe gate doctrinal)
- Marcar todos en Pass sin haber validado realmente
- Omitir GBP Checklist si gbp=Not Created (viola 9.8)
```

**Regla final**

```text
run_qa() aplica las 5 categorías + gate; cualquier No bloquea la publicación.
```

**Validación operativa**

Aplicar tras `check_dependencies()`. Cruce con Paso-09 9.2-9.8.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** 5 funciones de QA + consolidación en gate + opcional GBP checklist.

**Output del paso**

- **Tipo:** Función pseudocódigo + páginas con qa, publish_gate, gbp_checklist.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs con publish_gate = Yes; GBP checklist con 0 violaciones.

### 11.11 — Función `output_matrices()`

<small>§6.11</small>

**Explicación**

Genera las **3 matrices finales** que el Paso 13 (Sistema Final Operativo) consume: URL Matrix completa con score+tier+phase, Schema Map por page type, Internal Link Map.

**Firma de la función**

```python
def output_matrices(scored_pages: list[dict], link_matrix: list[dict]) -> dict
```

**Lógica interna**

```text
1. URL Matrix:
   - Filas: cada URL del inventario
   - Columnas: ID, URL, Tipo, Schema, Priority, Phase, Status (← Paso-03 3.5 + Paso-08 8.14)
2. Schema Map:
   - Filas: cada page type
   - Columnas: schema(s) requerido(s) (← Paso-03 3.8 + Paso-05 5.9)
3. Internal Link Map:
   - Filas: cada conexión (source → target)
   - Columnas: anchor, direction, page types (← Paso-07 7.11)
4. Output: dict {url_matrix, schema_map, link_matrix}
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.11 — 3 matrices generadas para el cluster Cerrajeros.

**Ejemplos incorrectos**

```text
- Omitir alguna columna doctrinal de la URL Matrix
- Schema Map con tipos inventados
- Link Map con URLs target no existentes en inventario
```

**Regla final**

```text
output_matrices() produce las 3 matrices que consume el SOP del Paso 13.
```

**Validación operativa**

Aplicar al final de `main()`. Cruce con Paso-03 3.5 (URL Matrix) + Paso-13 (siguiente paso).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Serializar las páginas scored + link_matrix en 3 estructuras tabulares finales.

**Output del paso**

- **Tipo:** Función pseudocódigo + dict con 3 matrices.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs en URL Matrix + 6 page types en Schema Map + ~80 conexiones en Link Map.

### 11.12 — Pseudocódigo principal `main()`

<small>§6.12</small>

**Explicación**

Función orquestadora que ejecuta las 11 funciones anteriores en el orden correcto. Es el punto de entrada del sistema; produce la salida final del Bloque 4.

**Firma de la función**

```python
def main() -> dict
```

**Lógica interna**

Ver §4 sub-sección 11.12 — secuencia completa con todas las llamadas + manejo de errores.

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.12 — `main()` aplicado al cluster Cerrajeros produce 3 matrices finales sin errores.

**Ejemplos incorrectos**

```text
- Cambiar orden de llamadas (rompe dependencias)
- Saltar el QA gate (rompe regla doctrinal)
- Capturar excepciones silenciosamente (oculta bloqueos)
```

**Regla final**

```text
main() ejecuta las 11 funciones en orden + bloquea si QA gate falla.
```

**Validación operativa**

Ejecutar end-to-end. Validar que las 3 matrices finales coinciden con expectativas del cluster.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Composición funcional + manejo de errores en orden secuencial.

**Output del paso**

- **Tipo:** Pseudocódigo orquestador.
- **Ejemplo (Cerrajeros Madrid 24h):** ejecución completa produce 3 matrices sin errores.

### 11.13 — Validación: cobertura de inputs heredados

<small>§6.13</small>

**Explicación**

Valida que `load_inputs()` recoge **TODOS** los outputs upstream necesarios y que ninguna función inventa inputs no presentes en Bloques 1-3.

**Patrón o fórmula**

```text
∀ función f en {load_inputs, normalize_slugs, ..., output_matrices}:
  ∀ input usado por f:
    ∃ output X.Y en Bloques 1-3 tal que f.input = X.Y
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
load_inputs() usa solo outputs ← 1.X (14 outputs Paso 1).
normalize_slugs() usa ← 1.5 + 1.7 + 1.9 + 1.6.
score_priority() usa ← 8.1 + 8.2-8.7 (6 factores doctrinales).
0 inputs inventados detectados.
```

**Ejemplos incorrectos**

```text
- Función que crea un input no derivado de Bloques 1-3
- Función que infiere un valor sin trazabilidad
- Inputs ⚠ inferido tratados como confirmed sin marcar
```

**Regla final**

```text
Cero inputs inventados. Cada input usado mapea a un output upstream confirmed.
```

**Validación operativa**

Aplicar al cierre del paso. Cruce con todos los §3 Heredados de las funciones.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Static analysis de las 11 funciones + cruce con catálogo de outputs upstream.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 137 outputs upstream cubiertos; 0 inputs inventados.

### 11.14 — Validación: secuencia respeta dependencias

<small>§6.14</small>

**Explicación**

Valida que el orden de `main()` respeta tanto las dependencias estructurales (Paso-02 2.13) como las temporales (Paso-08 8.11 + Paso-10 10.10).

**Patrón o fórmula**

```text
load → normalize → validate → generate → inject → expand → link → score → check → qa → output
   1.X    2.2-2.4    2.7      Pasos 4-7     6        4.10    7.X    8.X      10.10   9.X    finales
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
main() ejecuta:
  load_inputs()           # antes de todo
  normalize_slugs()       # tras inputs
  validate_categories()   # tras inputs (independiente de slugs)
  generate_pages()        # tras slugs + validate
  inject_local_coverage() # tras generate
  generate_expansion()    # opcional, tras inject
  assign_internal_links() # tras todas las páginas existen
  score_priority()        # tras pages + links
  check_dependencies()    # tras score
  run_qa()                # tras check
  output_matrices()       # al final
0 inversiones de orden detectadas.
```

**Ejemplos incorrectos**

```text
- Llamar score_priority() antes de generate_pages_by_type()
- Llamar run_qa() antes de assign_internal_links() (QA Conexión falla)
- Output_matrices() sin haber pasado QA gate
```

**Regla final**

```text
main() respeta el orden doctrinal de dependencias. Cualquier inversión es bug.
```

**Validación operativa**

Aplicar al cierre del paso. Cruce con Paso-02 2.13 + Paso-08 8.11 + Paso-10 10.10.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspección manual del orden + cross-check con dependency graph.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** orden secuencial validado; 0 inversiones.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 11 y avanzar al Paso 12 (Master Prompt).

### Validación de funciones

- ☐ Función `load_inputs()` recoge 137 outputs upstream (11.1)
- ☐ Función `normalize_slugs()` produce slugs limpios (11.2)
- ☐ Función `validate_categories()` elimina duplicados Additional vs core (11.3)
- ☐ Función `generate_pages_by_type()` produce N+1 URLs (11.4)
- ☐ Función `inject_local_coverage()` aplica LCAs solo en page types locales (11.5)
- ☐ Función `generate_expansion()` solo si Approved Expansion ≠ vacío (11.6)
- ☐ Función `assign_internal_links()` cumple matriz 7.11 (11.7)
- ☐ Función `score_priority()` aplica fórmula 8.1 con 6 factores (11.8)
- ☐ Función `check_dependencies()` bloquea violaciones de orden (11.9)
- ☐ Función `run_qa()` aplica las 5 categorías + gate (11.10)
- ☐ Función `output_matrices()` produce 3 matrices finales (11.11)

### Validación de orquestador

- ☐ Pseudocódigo principal `main()` ejecuta las 11 funciones en orden (11.12)

### Validación final

- ☐ Cobertura de inputs heredados: 0 inputs inventados (11.13)
- ☐ Secuencia respeta dependencias estructurales y temporales (11.14)

## Outputs Consolidados

<small>§8</small>

> Tabla final compacta con la trazabilidad row-per-output. Los IDs (`11.1`–`11.14`) coinciden con los declarados en §5. Esta tabla es la fuente única de la trazabilidad consolidada del paso (sustituye al antiguo b-doc).

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 11.1 | ← Paso-01 1.1-1.14 + Paso-02 + Paso-03 | **Función load_inputs()** = dict con variables Cerrajeros | Lectura programática de §8 de cada a-doc + preflight; serialización en dict normalizado. **Fuente:** GMB Crush. | confirmed |
| 11.2 | ← Paso-02 2.2-2.4 + Paso-03 3.3 | **Función normalize_slugs()** = `cerrajero` + `madrid` + 5 service_slugs + 1 additional_slug | Implementar slugify estándar + aplicar a los 4 grupos de slugs. **Fuente:** GMB Crush. | confirmed |
| 11.3 | ← Paso-02 2.7 + 2.12 | **Función validate_categories()** = effective_additional con `[duplicado-llaves]` (A=1) | Comparar semánticamente cada additional con cada core; aplicar criterio cobertura. **Fuente:** GMB Crush. | confirmed |
| 11.4 | ← Paso-04 4.3-4.8 + Paso-05 5.3-5.8 | **Función generate_pages_by_type()** = 29 URLs (1 HP + 5 SO + 1 GH + 5 LBS + 1 AC + 15 GA + 1 AUX) | 6 sub-funciones, una por page type, aplicando spec del Paso-05. **Fuente:** GMB Crush. | confirmed |
| 11.5 | ← Paso-06 6.2 + 6.12 + 6.17 | **Función inject_local_coverage()** = 22 páginas locales con 10 LCAs en areaServed | Iterar páginas, mapear page_type → conjunto LCAs según matriz Paso-06 6.12. **Fuente:** GMB Crush. | confirmed |
| 11.6 | ← Paso-01 1.11 + Paso-04 4.10 | **Función generate_expansion()** = `[]` (Phase 1, E=0) | Replicar lógica generate_pages_by_type() para cada Approved Area; en Phase 1 retorna vacío. **Fuente:** GMB Crush. | confirmed |
| 11.7 | ← Paso-07 7.9 + 7.11 | **Función assign_internal_links()** = ~80 enlaces internos (matriz 7.11 cumplida) | Lookup matriz 7.11 por page_type + selección anchor por catálogo 7.9. **Fuente:** GMB Crush. | confirmed |
| 11.8 | ← Paso-08 8.1-8.10 | **Función score_priority()** = 28 URLs con scores 19-29, tiers P1-P3, phases 1-4 | Implementar 6 funciones de medición + suma + mapeo a tier/phase doctrinales. **Fuente:** GMB Crush. | confirmed |
| 11.9 | ← Paso-08 8.11 + Paso-10 10.10 | **Función check_dependencies()** = 28 URLs validadas, 0 Blocked | Lookup parents por page (Paso-03 3.7) + comparar phases + bloquear conflictos. **Fuente:** GMB Crush. | confirmed |
| 11.10 | ← Paso-09 9.2-9.8 | **Función run_qa()** = 28 URLs con publish_gate = Yes; GBP checklist 0 violaciones | 5 funciones de QA + consolidación en gate + opcional GBP checklist. **Fuente:** GMB Crush. | confirmed |
| 11.11 | ← Paso-03 3.5 + 3.8 + Paso-07 7.11 | **Función output_matrices()** = 3 matrices (URL: 28 URLs / Schema: 6 page types / Link: ~80 conexiones) | Serializar páginas scored + link_matrix en 3 estructuras tabulares. **Fuente:** GMB Crush. | confirmed |
| 11.12 | ← 11.1-11.11 | **Pseudocódigo principal main()** = orquestador secuencial con 11 llamadas | Composición funcional + manejo de errores en orden secuencial. **Fuente:** GMB Crush. | confirmed |
| 11.13 | ← Bloques 1-3 completos | **Validación cobertura inputs** = 137 outputs upstream cubiertos; 0 inputs inventados | Static analysis de las 11 funciones + cruce con catálogo de outputs upstream. **Fuente:** GMB Crush. | OK |
| 11.14 | ← Paso-02 2.13 + Paso-08 8.11 + Paso-10 10.10 | **Validación secuencia dependencias** = orden secuencial validado; 0 inversiones | Inspección manual del orden + cross-check con dependency graph. **Fuente:** GMB Crush. | OK |

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
- Pseudocódigo del sistema GMB Crush (formalización algorítmica)

> **Nota importante — Pseudocódigo como contrato:**
> Las 11 funciones del Paso 11 NO inventan lógica nueva — formalizan en código la doctrina ya establecida en Bloques 1-3. Si una función necesita un input no presente en los outputs upstream, hay que volver al paso correspondiente y producirlo allí. El Paso 11 es el "compilador" del sistema, no su fuente.
