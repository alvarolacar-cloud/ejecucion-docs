Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 4 — Automatizacion/paso-11-pseudocodigo-sistema/`, alineado con los frameworks oficiales GMB Crush.

# Paso 11 — Pseudocódigo del Sistema

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 19 outputs del Paso 11 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos: outputs a conseguir, obtención de outputs, checklist final y outputs consolidados.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush en los que se basa el paso.

# Bloque I — Introducción

## Objetivo del Paso 11

<small>§2</small>

En este paso la IA produce todos los outputs que **expresan el sistema GMB Crush como pseudocódigo ejecutable** — las 16 funciones que cargan inputs, normalizan slugs, validan categorías, generan páginas POR PAGE TYPE (6 funciones individuales: HP / SO / GH / LBS / AC / GA), inyectan cobertura local, asignan enlaces internos, calculan priority, validan dependencias, ejecutan QA y generan las matrices finales. Este paso NO produce datos nuevos: produce el **algoritmo** que orquesta los outputs heredados de Bloques 1-3 en una secuencia repetible.

**Outputs del paso:**

- **11.1** Función `load_inputs()` — recoge variables del preflight + outputs de Bloques 1-3
- **11.2** Función `normalize_slugs()` — slugify de todos los componentes
- **11.3** Función `validate_categories()` — eliminación de duplicados Additional vs core
- **11.4** Función `generate_homepage()` — algoritmo Homepage (HP)
- **11.5** Función `generate_service_overview()` — algoritmo Service Overview Pages × S
- **11.6** Función `generate_geohub()` — algoritmo Main City GeoHub
- **11.7** Función `generate_lbs()` — algoritmo Location-Based Service Pages × S
- **11.8** Función `generate_additional_category()` — algoritmo Additional Category Pages × A
- **11.9** Función `generate_geoarticles()` — algoritmo GeoArticles × G×S
- **11.10** Función `inject_local_coverage()` — inyección de LCAs en contenido + areaServed
- **11.11** Función `generate_expansion()` — opcional, solo si Approved Expansion ≠ vacío
- **11.12** Función `assign_internal_links()` — matriz de enlaces obligatorios por URL
- **11.13** Función `score_priority()` — aplicación de la fórmula maestra del Paso 8
- **11.14** Función `check_dependencies()` — validación de orden de publicación
- **11.15** Función `run_qa()` — validación de las 5 categorías QA del Paso 9
- **11.16** Función `output_matrices()` — generación URL Matrix + Schema Map + Link Map
- **11.17** Pseudocódigo principal `main()` — orquestador secuencial
- **11.18** Validación: cobertura de inputs heredados (no se inventa nada que no esté en Bloques 1-3)
- **11.19** Validación: secuencia respeta dependencias estructurales

**Errores que previene:**

- Ejecutar el sistema en orden caótico (rompe dependencias)
- Inventar inputs no heredados (que rompen trazabilidad)
- Olvidar validaciones intermedias (categorías duplicadas, slugs sucios)
- Saltar el QA gate antes de generar matrices finales
- Hacer expansion sin Approved Expansion declarado
- Re-implementar lógica que ya existe en Bloques 1-3
- Confundir generate_homepage con generate_lbs (rompe specs por page type)

**Cuándo se ejecuta:** después de Pasos 1-10 cerrados (Bloques 1-3 completos). Antes de Paso 12 (Master Prompt) y Paso 13 (Sistema Final Operativo).

## Info heredada de pasos anteriores

<small>§3</small>

> Este paso es **meta**: no consume outputs de un solo paso, sino que orquesta todos los de Bloques 1-3. Lista resumida:

| Bloque | Outputs heredados | Cómo se usan en el pseudocódigo |
|---|---|---|
| Bloque 1 (Pasos 1-3) | 1.1 a 3.14 (43 outputs) | `load_inputs()` recoge intake + fórmula + matriz base |
| Bloque 2 (Pasos 4-7) | 4.1 a 7.15 (59 outputs) | Las 6 funciones `generate_*()` aplican URL rules + page type specs + content arch + linking |
| Bloque 3 (Pasos 8-10) | 8.1 a 10.13 (35 outputs) | `score_priority()` aplica Paso 8; `run_qa()` aplica Paso 9; `check_dependencies()` aplica Paso 10 |

**Total upstream:** 137 outputs de Bloques 1-3 que el pseudocódigo orquesta en secuencia.

# Bloque II — Ejemplo rellenado para el Paso 11 — Pseudocódigo del Sistema

<small>§4</small>

> Los 19 outputs del Paso 11 con sus valores reales para Cerrajeros Madrid 24h. Cada sub-sección §4.X corresponde 1:1 al output 11.X declarado en §5.

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
            if not is_covered_by_core(cat["name"], inputs["core_services"]):
                effective_additional.append(cat)
    return effective_additional
    # Para Cerrajeros: [{"name": "Servicio de duplicado de llaves", "needs_page": True}]
```

### 11.4 — Función `generate_homepage()`

```python
def generate_homepage(inputs):
    """Genera 1 Homepage según spec Paso-05 5.3. Root Entity Anchor."""
    return {
        "id": "HP",
        "url": "/",
        "page_type": "Homepage",
        "h1": f"{inputs['business_name']} – {primary_service(inputs)} de confianza en {inputs['main_city']}",
        "meta_title": f"{primary_service(inputs)} en {inputs['main_city']} | {inputs['business_name']}",
        "meta_description": f"¿Necesitas {primary_service(inputs)} en {inputs['main_city']}? "
                            f"{inputs['business_name']} ofrece servicio local, soporte experto y respuesta rápida. Llama hoy.",
        "word_count_target": (900, 1300),
        "schema": ["Organization", "WebSite", "LocalBusiness", "FAQPage", "Speakable"],
        "structure": [
            "H1", "Intro con marca + servicio + Main City", "Quick Answer",
            "Servicios principales", "Vista previa cobertura local",
            "Bloques de confianza", "Sección FAQ", "Bloque NAP", "CTA", "Enlaces internos"
        ],
        "internal_links": ["SO-1..S", "GH", "AC-1..A", "AUX (/contacto/)"],
    }
    # Para Cerrajeros: 1 Homepage con HP-001
```

### 11.5 — Función `generate_service_overview()`

```python
def generate_service_overview(inputs, slugs):
    """Genera S Service Overview Pages según spec Paso-05 5.4. Topical Authority Pillars (no local)."""
    pages = []
    for i, service in enumerate(inputs["core_services"], 1):
        pages.append({
            "id": f"SO-{i}",
            "url": f"/{slugs['primary_category_slug']}/{slugs['service_slugs'][i-1]}/",
            "page_type": "Service Overview",
            "h1": f"Servicios profesionales de {service} por {inputs['business_name']}",
            "meta_title": f"{service} por {inputs['business_name']} | Expertos en {inputs['primary_gbp_category']}",
            "word_count_target": (850, 1000),
            "schema": ["Service", "WebPage", "BreadcrumbList", "Speakable"],
            "structure": ["H1", "Intro NO local", "H2 Authority", "H2 Uniqueness",
                          "H2 Depth", "H2 Intent", "H2 Optimization", "Bullets",
                          "FAQs", "CTA", "Enlaces internos"],
            "internal_links": ["HP", "Otros SO", f"LBS-{i} matching", "GA relevante"],
            "is_local": False,  # Crítico: SO NO se geolocaliza
        })
    return pages
    # Para Cerrajeros: 5 SO (cerrajero-urgente, apertura-puertas, cambio-cerraduras, cambio-bombines, instalacion-cerraduras-seguridad)
```

### 11.6 — Función `generate_geohub()`

```python
def generate_geohub(inputs, slugs, all_pages):
    """Genera 1 Main City GeoHub según spec Paso-05 5.7. Main City Silo Container."""
    return {
        "id": "GH",
        "url": f"/{slugs['main_city_slug']}/",  # Option A (Paso-03 3.2)
        "page_type": "GeoHub",
        "h1": f"{inputs['business_name']} – Servicios de {inputs['primary_gbp_category']} en {inputs['main_city']}",
        "meta_title": f"Servicios de {inputs['primary_gbp_category']} en {inputs['main_city']} | {inputs['business_name']}",
        "word_count_target": (700, 1100),
        "schema": ["CollectionPage", "BreadcrumbList"],  # + LocalBusiness opcional si physical
        "structure": [
            "H1", "City Intro", "Menú de servicios (S LBS)",
            "Additional Category Menu (A AC)", "Local Coverage Areas Section",
            "GeoArticle Resources (G×S GAs)", "Trust Signals", "CTA", "Enlaces internos"
        ],
        "internal_links": ["HP", "Las S LBS", "Las A AC Pages", "Los G×S GAs", "AUX"],
        "lcas_section": True,  # GH es el contenedor principal de LCAs visibles
    }
    # Para Cerrajeros: 1 GeoHub /madrid/
```

### 11.7 — Función `generate_lbs()`

```python
def generate_lbs(inputs, slugs):
    """Genera S Location-Based Service Pages según spec Paso-05 5.5. Main City Converters."""
    pages = []
    for i, service in enumerate(inputs["core_services"], 1):
        pages.append({
            "id": f"LBS-{i}",
            "url": f"/{slugs['primary_category_slug']}/{slugs['main_city_slug']}/{slugs['service_slugs'][i-1]}/",
            "page_type": "Location-Based Service",
            "h1": f"{inputs['business_name']} – {service} en {inputs['main_city']}",
            "meta_title": f"Top {service} en {inputs['main_city']} | {inputs['business_name']}",
            "meta_description": f"¿Necesitas {service} en {inputs['main_city']}? "
                                f"{inputs['business_name']} ayuda con [problema 1], [problema 2] y [problema 3]. Llama para soporte local.",
            "word_count_target": (800, 1000),
            "schema": ["LocalBusiness", "BreadcrumbList", "FAQPage", "Speakable"],
            "structure": [
                "H1", "Intro local", "Quick Local Answer", "H2 Authority",
                "H2 Uniqueness", "H2 Depth", "H2 Local Pain Points",
                "H2 Local Coverage Areas Served", "H2 Related Services in Main City",
                "FAQs", "CTA", "Enlaces internos"
            ],
            "internal_links": [
                f"SO-{i} parent", "GH", "Otras LBS lateral",
                "GAs relacionados", "AUX"
            ],
            "lcas_in_content": True,  # LCAs aparecen en H2 dedicado + areaServed
        })
    return pages
    # Para Cerrajeros: 5 LBS en Madrid
```

### 11.8 — Función `generate_additional_category()`

```python
def generate_additional_category(inputs, slugs, effective_additional):
    """Genera A Additional Category Pages según spec Paso-05 5.6. GBP Additional Category Support."""
    pages = []
    for i, cat in enumerate(effective_additional, 1):
        cat_slug = slugify(cat["name"])
        pages.append({
            "id": f"AC-{i}",
            "url": f"/{slugs['primary_category_slug']}/{slugs['main_city_slug']}/{cat_slug}/",
            "page_type": "Additional Category",
            "h1": f"{inputs['business_name']} – {cat['name']} experto en {inputs['main_city']}",
            "meta_title": f"{cat['name']} en {inputs['main_city']} | {inputs['business_name']}",
            "word_count_target": (800, 1000),
            "schema": ["Service", "BreadcrumbList"],  # Service con areaServed
            "structure": [
                "H1", "Intro con problema local", "H2 Authority", "H2 Uniqueness",
                "H2 Depth", "H2 Intent", "H2 Optimization",
                "Local Coverage Use Case", "FAQs", "CTA", "Enlaces internos"
            ],
            "internal_links": ["GH", "LBS Madrid relacionadas", "GAs relevantes", "AUX"],
        })
    return pages
    # Para Cerrajeros: 1 AC (duplicado-llaves, A=1)
```

### 11.9 — Función `generate_geoarticles()`

```python
def generate_geoarticles(inputs, slugs, geo_topics_by_service):
    """Genera G×S GeoArticles según spec Paso-05 5.8. Semantic Boosters."""
    pages = []
    counter = 1
    for service_idx, service in enumerate(inputs["core_services"]):
        topics = geo_topics_by_service[service]  # ← Paso-03 3.4 (G topics por service)
        for topic in topics:
            pages.append({
                "id": f"GA-{counter}",
                "url": f"/{slugs['main_city_slug']}/{slugify(topic)}/",
                "page_type": "GeoArticle",
                "h1": f"{topic.capitalize()} en {inputs['main_city']}",
                "meta_title": f"{topic.capitalize()} en {inputs['main_city']} | {inputs['business_name']}",
                "word_count_target": (1000, 1500),
                "schema": ["Article", "FAQPage", "BreadcrumbList", "Speakable"],
                "structure": [
                    "H1", "Intro contextual", "H2 Problem", "H2 Local Context",
                    "H2 Options / Mistakes", "H2 When to Call",
                    "H2 Local Examples", "FAQs", "CTA", "Enlaces internos"
                ],
                "internal_links": [
                    f"LBS-{service_idx+1} matching",  # ← Paso-08 8.11 (parent obligatorio)
                    "GH", "GAs relacionados", "AUX"
                ],
                "parent_lbs": f"LBS-{service_idx+1}",
            })
            counter += 1
    return pages
    # Para Cerrajeros: 15 GAs (3 por servicio × 5 servicios)
```

### 11.10 — Función `inject_local_coverage()`

```python
def inject_local_coverage(pages, lcas, page_type_uses_lcas):
    """Inyecta LCAs en contenido + areaServed. Cumple Paso-06 6.2 + 6.17."""
    for page in pages:
        if page["page_type"] in page_type_uses_lcas:
            page["content_lcas"] = lcas["direct"] + lcas["candidate"]
            page["schema_areaServed"] = ["Madrid"] + lcas["direct"] + lcas["candidate"]
        elif page["page_type"] == "Homepage":
            page["content_lcas"] = []  # HP solo Main City
            page["schema_areaServed"] = ["Madrid"]
        else:  # Service Overview NO usa LCAs
            page["content_lcas"] = []
            page["schema_areaServed"] = []
    return pages
    # page_type_uses_lcas = ["Location-Based Service", "GeoHub", "Additional Category", "GeoArticle"]
```

### 11.11 — Función `generate_expansion()` (opcional)

```python
def generate_expansion(inputs):
    """Solo se ejecuta si Approved Expansion Areas ≠ []. Cumple Paso-04 4.10 + Paso-10 10.8."""
    if not inputs["approved_expansion_areas"]:
        return []  # Phase 1 default: E=0
    expansion_pages = []
    for area in inputs["approved_expansion_areas"]:
        # Generar GeoHub + LBS + GAs por Approved Expansion Area
        # Replicar lógica de generate_geohub/lbs/geoarticles para esa area
        ...
    return expansion_pages
    # Para Cerrajeros (Phase 1): []
```

### 11.12 — Función `assign_internal_links()`

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
    # Para Cerrajeros: ~80 enlaces internos
```

### 11.13 — Función `score_priority()`

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
        if page["page_type"] == "Homepage":
            page["tier"] = "P1"; page["phase"] = 1         # ← 8.12
        scored.append(page)
    return scored
```

### 11.14 — Función `check_dependencies()`

```python
def check_dependencies(scored_pages):
    """Aplica matriz Paso-10 10.10. Bloquea si parent no está publicado."""
    for page in scored_pages:
        for parent in get_parents(page):
            if parent["status"] != "Published" and parent["phase"] >= page["phase"]:
                page["status"] = "Blocked"
                page["block_reason"] = f"Parent {parent['url']} no publicado a tiempo"
        # Cumple Paso-08 8.11: phase(parent) < phase(GA)
    return scored_pages
```

### 11.15 — Función `run_qa()`

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

### 11.16 — Función `output_matrices()`

```python
def output_matrices(scored_pages, link_matrix):
    """Genera las 3 matrices finales que consume Paso 13."""
    return {
        "url_matrix":    build_url_matrix(scored_pages),     # ← 3.5 expandida con score+tier+phase
        "schema_map":    build_schema_map(scored_pages),     # ← 3.8 + 5.9 + 6.17
        "link_matrix":   link_matrix,                         # ← 7.11
    }
```

### 11.17 — Pseudocódigo principal `main()`

```python
def main():
    # 1. Cargar inputs
    inputs = load_inputs()                                   # 11.1

    # 2. Normalizar
    slugs = normalize_slugs(inputs)                          # 11.2
    effective_additional = validate_categories(inputs)       # 11.3

    # 3. Generar páginas POR PAGE TYPE (6 funciones individuales)
    homepage = generate_homepage(inputs)                     # 11.4
    so_pages = generate_service_overview(inputs, slugs)      # 11.5
    geohub = generate_geohub(inputs, slugs, [])              # 11.6
    lbs_pages = generate_lbs(inputs, slugs)                  # 11.7
    ac_pages = generate_additional_category(inputs, slugs,
                                              effective_additional)  # 11.8
    ga_pages = generate_geoarticles(inputs, slugs,
                                      geo_topics_by_service)  # 11.9
    pages = [homepage] + so_pages + [geohub] + lbs_pages + ac_pages + ga_pages

    # 4. Inyección + expansión
    pages = inject_local_coverage(pages, inputs["lcas"],
                                   page_type_uses_lcas)       # 11.10
    pages += generate_expansion(inputs)                      # 11.11 (opcional)

    # 5. Conexión
    link_matrix = assign_internal_links(pages)               # 11.12

    # 6. Priorización
    scored_pages = score_priority(pages)                     # 11.13
    scored_pages = check_dependencies(scored_pages)          # 11.14

    # 7. QA gate
    qa_pages = run_qa(scored_pages)                          # 11.15
    if any(p["publish_gate"] != "Ready" for p in qa_pages):
        raise BlockedDeployError("Algunas URLs no pasan QA gate")

    # 8. Outputs finales
    matrices = output_matrices(qa_pages, link_matrix)        # 11.16
    return matrices
```

### 11.18 — Validación: cobertura de inputs heredados

Cumplido — `load_inputs()` recoge los **14 outputs de Paso 1** + las variables derivadas (slugs, A, S, G) de Paso 2. Las 6 funciones `generate_*()` consumen específicamente los specs por page type del Paso 5. Cero inputs inventados; cero placeholders sin trazabilidad.

### 11.19 — Validación: secuencia respeta dependencias

Cumplido — el orden `main()` reproduce el orden doctrinal:

```
load → normalize → validate → generate_HP → generate_SO → generate_GH → generate_LBS → generate_AC → generate_GA → inject → expand → link → score → check → qa → output
   1.X    2.2-2.4    2.7      5.3        5.4          5.7         5.5        5.6         5.8        6      4.10    7.X    8.X      10.10   9.X    finales
```

Cada paso espera que sus dependencias estén resueltas antes de ejecutarse. Cumple Paso-02 2.13 (orden HP → SO → GH → LBS → AC → GAs).

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 19 outputs que el Paso 11 debe producir. Cada output tiene un ID global (`Paso.Output`, ej. `11.7`) citable desde cualquier doc del sistema.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 11.1 | Función `load_inputs()` | Función pseudocódigo | GMB Crush | Paso-01 1.1-1.14 + Paso-02 + Paso-03 |
| 11.2 | Función `normalize_slugs()` | Función pseudocódigo | GMB Crush | Paso-02 2.2 + 2.3 + 2.4 + Paso-03 3.3 |
| 11.3 | Función `validate_categories()` | Función pseudocódigo | GMB Crush | Paso-02 2.7 + 2.12 |
| 11.4 | Función `generate_homepage()` | Función pseudocódigo | GMB Crush | Paso-04 4.3 + Paso-05 5.3 |
| 11.5 | Función `generate_service_overview()` | Función pseudocódigo | GMB Crush | Paso-04 4.4 + Paso-05 5.4 |
| 11.6 | Función `generate_geohub()` | Función pseudocódigo | GMB Crush | Paso-04 4.5 + Paso-05 5.7 + Paso-03 3.2 |
| 11.7 | Función `generate_lbs()` | Función pseudocódigo | GMB Crush | Paso-04 4.6 + Paso-05 5.5 |
| 11.8 | Función `generate_additional_category()` | Función pseudocódigo | GMB Crush | Paso-04 4.7 + Paso-05 5.6 + Paso-03 3.3 |
| 11.9 | Función `generate_geoarticles()` | Función pseudocódigo | GMB Crush | Paso-04 4.8 + Paso-05 5.8 + Paso-03 3.4 |
| 11.10 | Función `inject_local_coverage()` | Función pseudocódigo | GMB Crush | Paso-06 6.2 + 6.12 + 6.17 |
| 11.11 | Función `generate_expansion()` | Función pseudocódigo opcional | GMB Crush | Paso-01 1.11 + Paso-04 4.10 |
| 11.12 | Función `assign_internal_links()` | Función pseudocódigo | GMB Crush | Paso-07 7.9 + 7.11 |
| 11.13 | Función `score_priority()` | Función pseudocódigo | GMB Crush | Paso-08 8.1-8.10 |
| 11.14 | Función `check_dependencies()` | Función pseudocódigo | GMB Crush | Paso-08 8.11 + Paso-10 10.10 |
| 11.15 | Función `run_qa()` | Función pseudocódigo | GMB Crush | Paso-09 9.2-9.8 |
| 11.16 | Función `output_matrices()` | Función pseudocódigo | GMB Crush | Paso-03 3.5 + 3.8 + Paso-07 7.11 |
| 11.17 | Pseudocódigo principal `main()` | Orquestador | GMB Crush | Paso-11 11.1-11.16 (intra-paso) |
| 11.18 | Validación cobertura de inputs | Validation flag | GMB Crush | Bloques 1-3 completos |
| 11.19 | Validación secuencia respeta dependencias | Validation flag | GMB Crush | Paso-02 2.13 + Paso-08 8.11 + Paso-10 10.10 |

## Obtención de Outputs

<small>§6</small>

> Esta sección es donde la IA produce cada uno de los 19 outputs (11.1–11.19). Cada output usa el patrón estándar adaptado a pseudocódigo: Explicación / Firma de la función / Lógica interna / Ejemplo Cerrajeros / Ejemplos incorrectos / Regla / Validación / Cómo se obtiene / Output del paso.

### 11.1 — Función `load_inputs()`

<small>§6.1</small>

**Explicación**

Función de entrada del sistema. Recoge **todas las variables** del preflight + outputs de Bloques 1-3 en un único objeto.

**Firma de la función**

```python
def load_inputs() -> dict
```

**Lógica interna**

```text
1. Leer 00preflight.md (5 campos del cliente)
2. Leer §8 Outputs Consolidados de los a-docs 01a, 02a, 03a (Bloque 1)
3. Leer §8 de los a-docs 04a, 05a, 06a, 07a (Bloque 2)
4. Leer §8 de los a-docs 08a, 09a, 10a (Bloque 3)
5. Devolver dict con todas las variables
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.1.

**Ejemplos incorrectos**

```text
- Inventar un campo no presente en preflight ni en outputs heredados
- Saltar la validación de status (cargar outputs ⚠ inferido como confirmed)
- Omitir Bloques completos
```

**Regla final**

```text
load_inputs() es source-of-truth: todo input usado downstream viene de aquí.
```

**Validación operativa**

Aplicar al inicio de `main()`. Validar que los 137 outputs upstream están en `confirmed`.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Lectura programática de los §8 de cada a-doc + preflight.

**Output del paso**

- **Tipo:** Función pseudocódigo + dict resultado.
- **Ejemplo (Cerrajeros Madrid 24h):** dict con 14 campos de Paso 1 + slugs Paso 2 + matriz Paso 3.

### 11.2 — Función `normalize_slugs()`

<small>§6.2</small>

**Explicación**

Normaliza todos los componentes que aparecen en URLs: categoría primaria, Main City, servicios, categorías adicionales.

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
- Slugs con caracteres especiales
```

**Regla final**

```text
Todos los slugs cumplen slugify estándar (cruza con Paso-02 2.2-2.4 + Paso-03 3.3).
```

**Validación operativa**

Aplicar tras `load_inputs()`. Cruce con Paso-04 4.13.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Implementar slugify estándar.

**Output del paso**

- **Tipo:** Función pseudocódigo + dict de slugs.
- **Ejemplo (Cerrajeros Madrid 24h):** `cerrajero` + `madrid` + 5 service_slugs + 1 additional_slug.

### 11.3 — Función `validate_categories()`

<small>§6.3</small>

**Explicación**

Cruza Additional Categories declaradas vs core services y elimina duplicaciones.

**Firma de la función**

```python
def validate_categories(inputs: dict) -> list[dict]
```

**Lógica interna**

```text
1. Iterar additional_gbp_categories
2. Si needs_page=True, validar que NO esté cubierta por algún core_service
3. Si está cubierta → marcar como "Servicio cubierto"
4. Si no está cubierta → añadir a effective_additional[]
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.3 — `cerrajería de urgencia` se elimina (cubierta); `duplicado de llaves` queda como única efectiva.

**Ejemplos incorrectos**

```text
- Generar página AC para una categoría ya cubierta (canibalización)
- Olvidar el check de semantic match
```

**Regla final**

```text
Una categoría adicional solo genera página propia si NO está cubierta por core service.
```

**Validación operativa**

Aplicar tras `load_inputs()`. Cruce con Paso-02 2.7 y 2.12.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Comparar semánticamente cada categoría adicional con cada core service.

**Output del paso**

- **Tipo:** Función pseudocódigo + lista categorías efectivas.
- **Ejemplo (Cerrajeros Madrid 24h):** `[{"name": "Servicio de duplicado de llaves"}]` (A=1).

### 11.4 — Función `generate_homepage()`

<small>§6.4</small>

**Explicación**

Genera la **única Homepage** del cluster aplicando spec Paso-05 5.3 (Root Entity Anchor). La Homepage es la raíz de entidad — concentra señales de marca, categoría GBP, Main City, NAP, servicios y cobertura.

**Firma de la función**

```python
def generate_homepage(inputs: dict) -> dict
```

**Lógica interna**

```text
1. Asignar URL = '/'
2. H1 con template: '[Brand] – [Primary Service] de confianza en [Main City]'
3. Meta Title: '[Primary Service] en [Main City] | [Brand]'
4. Meta Description: pregunta + servicios + ciudad + Llama hoy
5. Schema: Organization + WebSite + LocalBusiness + FAQPage + Speakable
6. Estructura: 11 bloques (Paso-06 6.6) — H1 → Intro → Quick Answer → Services
   → Coverage Preview → Trust → FAQ → NAP → CTA → Internal Links
7. Word count target: 900-1,300 (Paso-05 5.10)
8. Internal links: SO-1..S, GH, AC-1..A, AUX (Paso-07 7.11)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.4 — HP-001 con todos los campos.

**Ejemplos incorrectos**

```text
- Homepage con multiple services como targets (rompe rol Root Entity)
- Homepage targeting 5 cities equally
- Homepage sin NAP
- Homepage sin enlaces a service pages
```

**Regla final**

```text
generate_homepage() produce 1 Homepage = Root Entity Anchor con 11 bloques + schema completo.
```

**Validación operativa**

Aplicar al inicio de la generación. Cruce con Paso-05 5.3 + Paso-06 6.6.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar spec Homepage del Paso-05 5.3 con inputs heredados.

**Output del paso**

- **Tipo:** Función pseudocódigo + dict Homepage.
- **Ejemplo (Cerrajeros Madrid 24h):** 1 Homepage HP-001 (`/`) con 11 bloques.

### 11.5 — Función `generate_service_overview()`

<small>§6.5</small>

**Explicación**

Genera **S Service Overview Pages** (una por core service) aplicando spec Paso-05 5.4 (Topical Authority Pillars). **Crucial**: las SO son **NO geolocalizadas** — su rol es pilar temático que sustenta las versiones locales (LBS).

**Firma de la función**

```python
def generate_service_overview(inputs: dict, slugs: dict) -> list[dict]
```

**Lógica interna**

```text
1. Iterar core_services (longitud S, default 5)
2. Por cada service:
   - URL: /[primary-cat-slug]/[service-slug]/
   - H1: 'Servicios profesionales de [Service] por [Brand]'
   - Meta Title: '[Service] por [Brand] | Expertos en [Primary Category]'
   - Schema: Service + WebPage + BreadcrumbList + Speakable
   - Estructura: H1 → Intro NO local → AUDIO H2s → Bullets → FAQs → CTA → Links
   - Word count: 850-1,000
   - Internal links: HP, otras SO, LBS matching, GA relevante
   - is_local: False  (CRÍTICO)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.5 — 5 SO pages: SO-1 Cerrajero urgente, SO-2 Apertura de puertas, SO-3 Cambio de cerraduras, SO-4 Cambio de bombines, SO-5 Instalación de cerraduras de seguridad.

**Ejemplos incorrectos**

```text
- SO con Madrid como target principal (rompe rol no-local)
- SO escrita como artículo informacional (rompe rol comercial)
- URL /cerrajero/madrid/cerrajero-urgente/ como SO (esa URL es LBS)
```

**Regla final**

```text
generate_service_overview() produce S SO no-locales. NO target Main City. NO target LCAs.
```

**Validación operativa**

Aplicar tras `validate_categories()`. Cruce con Paso-05 5.4 + Paso-06 6.7.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar spec SO del Paso-05 5.4 replicada × S core services.

**Output del paso**

- **Tipo:** Función pseudocódigo + lista de S SO.
- **Ejemplo (Cerrajeros Madrid 24h):** 5 SO en `/cerrajero/{service}/`.

### 11.6 — Función `generate_geohub()`

<small>§6.6</small>

**Explicación**

Genera el **único Main City GeoHub** aplicando spec Paso-05 5.7 (Main City Silo Container). El GeoHub agrupa TODAS las señales de la Main City: servicios + categorías + LCAs + GeoArticles.

**Firma de la función**

```python
def generate_geohub(inputs: dict, slugs: dict, all_pages: list) -> dict
```

**Lógica interna**

```text
1. URL: /[main-city-slug]/   (Option A, default; Paso-03 3.2)
2. H1: '[Brand] – Servicios de [Industry] en [Main City]'
3. Meta Title: 'Servicios de [Industry] en [Main City] | [Brand]'
4. Schema: CollectionPage + BreadcrumbList (+ LocalBusiness opcional)
5. Estructura: 10 bloques (Paso-06 6.10):
   H1 → City Intro → Menú servicios (S LBS) → AC Menu (A AC) →
   LCAs Section → GeoArticle Resources (G×S GAs) → Trust → CTA → Links
6. Word count: 700-1,100
7. Internal links: HP, las S LBS, las A AC, los G×S GAs, AUX
8. lcas_section = True (GH es donde las LCAs son visibles como menu)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.6 — 1 GeoHub `/madrid/` con 21 internal links (5 LBS + 1 AC + 15 GA).

**Ejemplos incorrectos**

```text
- GeoHub con only generic city text (sin menús de servicios)
- GeoHub sin links a service pages
- Tratar Almagro como child page (rompe LCAs sin URL)
- GeoHub sin CTA
```

**Regla final**

```text
generate_geohub() produce 1 GeoHub = Main City Silo Container con menús completos.
```

**Validación operativa**

Aplicar tras `generate_service_overview()`. Cruce con Paso-05 5.7 + Paso-06 6.10.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar spec GeoHub Paso-05 5.7 al GeoHub Main City con URL Option A o B (Paso-03 3.2).

**Output del paso**

- **Tipo:** Función pseudocódigo + dict GeoHub.
- **Ejemplo (Cerrajeros Madrid 24h):** 1 GeoHub `/madrid/` con 10 bloques.

### 11.7 — Función `generate_lbs()`

<small>§6.7</small>

**Explicación**

Genera **S Location-Based Service Pages** (una por core service en la Main City) aplicando spec Paso-05 5.5 (Main City Converters). Son las páginas comerciales más importantes — convierten búsquedas locales de alta intención.

**Firma de la función**

```python
def generate_lbs(inputs: dict, slugs: dict) -> list[dict]
```

**Lógica interna**

```text
1. Iterar core_services (longitud S)
2. Por cada service:
   - URL: /[primary-cat-slug]/[main-city-slug]/[service-slug]/
   - H1: '[Brand] – [Service] en [Main City]'
   - Meta Title: 'Top [Service] en [Main City] | [Brand]'
   - Meta Description: pregunta local + dolor + Llama
   - Schema: LocalBusiness + BreadcrumbList + FAQPage + Speakable
   - Estructura: 12 bloques (Paso-06 6.8):
     H1 → Intro local → Quick Local Answer → AUDIO H2s →
     H2 Local Pain Points → H2 LCAs Section → H2 Related Services →
     FAQs → CTA → Links
   - Word count: 800-1,000
   - Internal links: parent SO, GH, otras LBS lateral, GAs, AUX
   - lcas_in_content = True (LCAs en H2 dedicado)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.7 — 5 LBS en Madrid:
- LBS-1: `/cerrajero/madrid/cerrajero-urgente/`
- LBS-2: `/cerrajero/madrid/apertura-puertas/`
- LBS-3: `/cerrajero/madrid/cambio-cerraduras/`
- LBS-4: `/cerrajero/madrid/cambio-bombines/`
- LBS-5: `/cerrajero/madrid/instalacion-cerraduras-seguridad/`

**Ejemplos incorrectos**

```text
- Mezclar Madrid and Almagro as equal targets en H1
- Crear 1 página por cada zona de cobertura
- Afirmar oficina en Salamanca
- Combinar 2 servicios en una sola landing local (rompe One Service)
```

**Regla final**

```text
generate_lbs() produce S LBS = Main City Converters con LCAs Section + areaServed.
```

**Validación operativa**

Aplicar tras `generate_geohub()`. Cruce con Paso-05 5.5 + Paso-06 6.8.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar spec LBS Paso-05 5.5 replicada × S core services × Main City.

**Output del paso**

- **Tipo:** Función pseudocódigo + lista de S LBS.
- **Ejemplo (Cerrajeros Madrid 24h):** 5 LBS en `/cerrajero/madrid/{service}/`.

### 11.8 — Función `generate_additional_category()`

<small>§6.8</small>

**Explicación**

Genera **A Additional Category Pages** (una por categoría efectiva tras `validate_categories()`) aplicando spec Paso-05 5.6 (GBP Additional Category Support). Solo se generan para categorías que NO están cubiertas por un core service.

**Firma de la función**

```python
def generate_additional_category(inputs: dict, slugs: dict, effective_additional: list) -> list[dict]
```

**Lógica interna**

```text
1. Iterar effective_additional (longitud A)
2. Por cada cat:
   - URL: /[primary-cat-slug]/[main-city-slug]/[additional-slug]/
   - H1: '[Brand] – [Additional Service] experto en [Main City]'
   - Meta Title: '[Additional Service] en [Main City] | [Brand]'
   - Schema: Service (con areaServed) + BreadcrumbList + FAQPage opcional
   - Estructura: 11 bloques (Paso-06 6.9)
   - Word count: 800-1,000
   - Internal links: GH, LBS Madrid relacionadas, GAs relevantes, AUX
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.8 — 1 AC: `/cerrajero/madrid/duplicado-llaves/` (A=1, solo `Servicio de duplicado de llaves` queda efectivo).

**Ejemplos incorrectos**

```text
- Crear /cerrajero/madrid/cerrajero-urgente/ como AC (canibaliza con LBS-1)
- AC sin local context
- AC sin links a GeoHub
- AC para una categoría que ya está cubierta por core service
```

**Regla final**

```text
generate_additional_category() solo genera A páginas (categorías efectivas, no duplicadas con core).
```

**Validación operativa**

Aplicar tras `generate_lbs()`. Cruce con Paso-05 5.6 + Paso-06 6.9 + Paso-02 2.12.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar spec AC Paso-05 5.6 a las A categorías efectivas con slugs Paso-03 3.3.

**Output del paso**

- **Tipo:** Función pseudocódigo + lista de A AC.
- **Ejemplo (Cerrajeros Madrid 24h):** 1 AC `/cerrajero/madrid/duplicado-llaves/`.

### 11.9 — Función `generate_geoarticles()`

<small>§6.9</small>

**Explicación**

Genera **G×S GeoArticles** (G topics por cada core service) aplicando spec Paso-05 5.8 (Semantic Boosters). Los GAs **NO son landing comerciales** — son boosters semánticos que apoyan a las LBS y al GeoHub.

**Firma de la función**

```python
def generate_geoarticles(inputs: dict, slugs: dict, geo_topics_by_service: dict) -> list[dict]
```

**Lógica interna**

```text
1. Iterar core_services × geo_topics_by_service[service] (validados con keyword research, Paso-03 3.4)
2. Por cada (service, topic):
   - URL: /[main-city-slug]/[topic-slug]/
   - H1: '[Article Topic] in [Main City]'
   - Meta Title: '[Article Topic] in [Main City] | [Brand]'
   - Schema: Article + FAQPage + BreadcrumbList + Speakable
   - Estructura: 10 bloques (Paso-06 6.11):
     H1 → Intro contextual → H2 Problem → H2 Local Context →
     H2 Options/Mistakes → H2 When to Call → H2 Local Examples →
     FAQs → CTA → Links
   - Word count: 1,000-1,500
   - Internal links: matching LBS (parent obligatorio Paso-08 8.11), GH, GAs related, AUX
   - parent_lbs: f"LBS-{service_idx+1}"
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 11.9 — 15 GAs en `/madrid/{topic}/`:
- 3 por Cerrajero urgente: cuanto-cuesta-... / que-hacer-si-no-puedes-... / cuanto-tarda-...
- 3 por Apertura de puertas: cuanto-cuesta-abrir-... / que-hacer-si-te-dejas-llaves / sin-romper-cerradura
- 3 por Cambio cerraduras: cuando-cambiar-... / cambio-tras-perder-llaves / cerradura-nueva-o-reparacion
- 3 por Cambio bombines: cuando-cambiar-bombin / antibumping / cambio-bombin-sin-cambiar-cerradura
- 3 por Instalación seguridad: mejores-cerraduras-viviendas / comunidades / puerta-blindada

**Ejemplos incorrectos**

```text
- GA con H1 idéntico a su LBS hijo (canibalización)
- GA escrito como landing comercial (rompe rol semantic booster)
- GA sin parent LBS (rompe Paso-08 8.11)
- Más GAs que G×S (rompe fórmula 2.8)
```

**Regla final**

```text
generate_geoarticles() produce G×S GAs como semantic boosters; cada uno con parent LBS.
```

**Validación operativa**

Aplicar tras `generate_additional_category()`. Cruce con Paso-05 5.8 + Paso-06 6.11 + Paso-08 8.11.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar spec GA Paso-05 5.8 a G×S combinaciones service × topic (topics de Paso-03 3.4).

**Output del paso**

- **Tipo:** Función pseudocódigo + lista de G×S GAs.
- **Ejemplo (Cerrajeros Madrid 24h):** 15 GAs en `/madrid/{topic}/`.

### 11.10 — Función `inject_local_coverage()`

<small>§6.10</small>

**Explicación**

Inyecta las LCAs (Direct + Candidate) en el contenido y schema `areaServed` de las páginas locales. Las páginas no-locales (SO) reciben lista vacía. La Homepage solo recibe Main City.

**Firma de la función**

```python
def inject_local_coverage(pages: list, lcas: dict, page_type_uses_lcas: list) -> list
```

**Lógica interna**

```text
1. Para cada page:
   - Si page_type ∈ {LBS, GeoHub, AC, GeoArticle} → inyectar lcas (direct + candidate)
   - Si page_type = Homepage → inyectar solo Main City
   - Si page_type = SO → inyectar [] (no-local)
2. Schema areaServed:
   - LBS, GH, AC, GA: [Main City] + lcas direct + lcas candidate
   - HP: [Main City]
   - SO: [] o sin areaServed
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

22 páginas locales con 10 LCAs en areaServed; 5 SO sin LCAs.

**Ejemplos incorrectos**

```text
- Inyectar LCAs en SO (rompe rol pilar temático)
- Olvidar areaServed en LBS
- Mencionar LCA no aprobada
```

**Regla final**

```text
LCAs en contenido + areaServed solo en page types locales; SO siempre no-local.
```

**Validación operativa**

Aplicar tras `generate_geoarticles()`. Cruce con Paso-06 6.2 + 6.12 + 6.17.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Iterar páginas, mapear page_type → conjunto LCAs según matriz Paso-06 6.12.

**Output del paso**

- **Tipo:** Función pseudocódigo + páginas con `content_lcas` y `schema_areaServed`.
- **Ejemplo (Cerrajeros Madrid 24h):** 22 páginas locales con 10 LCAs; 5 SO sin LCAs.

### 11.11 — Función `generate_expansion()`

<small>§6.11</small>

**Explicación**

Función opcional. Solo se ejecuta si Approved Expansion Areas ≠ vacío. En Phase 1 web-first default, NO se ejecuta.

**Firma de la función**

```python
def generate_expansion(inputs: dict) -> list[dict]
```

**Lógica interna**

```text
1. Si approved_expansion_areas == [] → return []
2. Por cada area: generar GeoHub + S LBS + G×S GAs replicando lógica de generate_*()
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```python
generate_expansion(inputs) == []  # Phase 1, E=0
```

**Ejemplos incorrectos**

```text
- Generar expansion sin aprobación
- Mezclar LBS de Approved Area con LBS de Main City
```

**Regla final**

```text
generate_expansion() solo se ejecuta tras decisión explícita del operador.
```

**Validación operativa**

Cruce con Paso-01 1.11 + Paso-04 4.10.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Replicar lógica de generate_*() para cada Approved Area.

**Output del paso**

- **Tipo:** Función pseudocódigo + lista (puede estar vacía).
- **Ejemplo (Cerrajeros Madrid 24h):** `[]`.

### 11.12 — Función `assign_internal_links()`

<small>§6.12</small>

**Explicación**

Asigna los enlaces internos según la matriz del Paso-07 7.11.

**Firma de la función**

```python
def assign_internal_links(pages: list[dict]) -> list[dict]
```

**Lógica interna**

```text
1. Para cada page: determinar enlaces Required según page_type (matriz 7.11)
2. Por cada link target: validar que target existe + asignar anchor (Paso-07 7.9) + dirección
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

~80 enlaces internos en el cluster.

**Ejemplos incorrectos**

```text
- Enlazar a URL no existente (link roto)
- Anchors todos branded
- Saltar enlaces Required
```

**Regla final**

```text
assign_internal_links() cumple matriz Paso-07 7.11 + anchors variados Paso-07 7.9.
```

**Validación operativa**

Cruce con Paso-07 7.14.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Lookup matriz 7.11 + selección anchor por catálogo 7.9.

**Output del paso**

- **Tipo:** Función pseudocódigo + lista de tuplas.
- **Ejemplo (Cerrajeros Madrid 24h):** ~80 enlaces.

### 11.13 — Función `score_priority()`

<small>§6.13</small>

**Explicación**

Aplica la fórmula maestra del Paso-08 8.1 a cada URL.

**Firma de la función**

```python
def score_priority(pages: list[dict]) -> list[dict]
```

**Lógica interna**

Ver §4 sub-sección 11.13.

**Ejemplo correcto con Cerrajeros Madrid 24h**

28 URLs con scores 19-29, tiers P1-P3.

**Ejemplos incorrectos**

```text
- Sumar con pesos distintos (rompe fórmula)
- Olvidar HP=P1 (viola 8.12)
```

**Regla final**

```text
score_priority() aplica fórmula completa con peso 1; HP siempre P1.
```

**Validación operativa**

Cruce con Paso-08 8.1-8.10 + 8.12.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Implementar 6 funciones de medición + suma + mapeo a tier/phase.

**Output del paso**

- **Tipo:** Función pseudocódigo + páginas scored.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs con scores y tiers.

### 11.14 — Función `check_dependencies()`

<small>§6.14</small>

**Explicación**

Valida que cada página puede publicarse cuando le toca según su Phase.

**Firma de la función**

```python
def check_dependencies(scored_pages: list[dict]) -> list[dict]
```

**Lógica interna**

Ver §4 sub-sección 11.14.

**Ejemplo correcto con Cerrajeros Madrid 24h**

28 URLs, 0 Blocked.

**Ejemplos incorrectos**

```text
- Publicar GA en Phase 2 cuando su LBS está en Phase 3
- Olvidar validar parent SO en LBS
```

**Regla final**

```text
check_dependencies() bloquea cualquier publicación que viole orden parent → child.
```

**Validación operativa**

Cruce con Paso-10 10.10.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Lookup parents (Paso-03 3.7) + comparar phases + bloquear conflictos.

**Output del paso**

- **Tipo:** Función pseudocódigo + páginas con flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs validadas, 0 Blocked.

### 11.15 — Función `run_qa()`

<small>§6.15</small>

**Explicación**

Aplica las 5 categorías QA del Paso-09 9.2-9.6 + Final Publish Gate (9.7).

**Firma de la función**

```python
def run_qa(pages: list[dict]) -> list[dict]
```

**Lógica interna**

Ver §4 sub-sección 11.15.

**Ejemplo correcto con Cerrajeros Madrid 24h**

28 URLs con publish_gate = Yes; GBP checklist 0 violaciones.

**Ejemplos incorrectos**

```text
- Saltar alguna categoría QA (rompe gate doctrinal)
- Marcar Pass sin haber validado realmente
```

**Regla final**

```text
run_qa() aplica las 5 categorías + gate; cualquier No bloquea la publicación.
```

**Validación operativa**

Cruce con Paso-09 9.2-9.8.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** 5 funciones QA + gate consolidation + opcional GBP checklist.

**Output del paso**

- **Tipo:** Función pseudocódigo + páginas con qa, publish_gate, gbp_checklist.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs con publish_gate Pass.

### 11.16 — Función `output_matrices()`

<small>§6.16</small>

**Explicación**

Genera las **3 matrices finales** que el Paso 13 (SOP) consume.

**Firma de la función**

```python
def output_matrices(scored_pages: list[dict], link_matrix: list[dict]) -> dict
```

**Lógica interna**

Ver §4 sub-sección 11.16.

**Ejemplo correcto con Cerrajeros Madrid 24h**

3 matrices: URL (28 URLs) + Schema (6 page types) + Link (~80 conexiones).

**Ejemplos incorrectos**

```text
- Omitir alguna columna doctrinal
- Schema Map con tipos inventados
- Link Map con URLs no existentes
```

**Regla final**

```text
output_matrices() produce las 3 matrices que consume el SOP del Paso 13.
```

**Validación operativa**

Cruce con Paso-03 3.5 + 3.8 + Paso-07 7.11.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Serializar las páginas scored + link_matrix en 3 estructuras.

**Output del paso**

- **Tipo:** Función pseudocódigo + dict con 3 matrices.
- **Ejemplo (Cerrajeros Madrid 24h):** URL Matrix 28 + Schema Map 6 + Link Map 80.

### 11.17 — Pseudocódigo principal `main()`

<small>§6.17</small>

**Explicación**

Función orquestadora que ejecuta las 16 funciones anteriores en orden.

**Firma de la función**

```python
def main() -> dict
```

**Lógica interna**

Ver §4 sub-sección 11.17.

**Ejemplo correcto con Cerrajeros Madrid 24h**

`main()` produce 3 matrices finales sin errores.

**Ejemplos incorrectos**

```text
- Cambiar orden de llamadas (rompe dependencias)
- Saltar el QA gate
- Llamar generate_lbs() antes que generate_service_overview()
```

**Regla final**

```text
main() ejecuta las 16 funciones en orden + bloquea si QA gate falla.
```

**Validación operativa**

Ejecutar end-to-end.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Composición funcional + manejo de errores.

**Output del paso**

- **Tipo:** Pseudocódigo orquestador.
- **Ejemplo (Cerrajeros Madrid 24h):** ejecución completa produce 3 matrices.

### 11.18 — Validación: cobertura de inputs heredados

<small>§6.18</small>

**Explicación**

Valida que `load_inputs()` recoge **TODOS** los outputs upstream y que ninguna función inventa inputs.

**Patrón o fórmula**

```text
∀ función f en {load_inputs, normalize_slugs, generate_homepage, generate_so,
                generate_gh, generate_lbs, generate_ac, generate_ga, ...}:
  ∀ input usado por f:
    ∃ output X.Y en Bloques 1-3 tal que f.input = X.Y
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
load_inputs() usa solo outputs ← 1.X (14 outputs Paso 1).
generate_homepage() usa ← 5.3 + 1.1 + 1.7.
generate_lbs() usa ← 5.5 + 1.9 + 1.10 + 2.4.
0 inputs inventados detectados.
```

**Ejemplos incorrectos**

```text
- Función que crea un input no derivado de Bloques 1-3
- Inputs ⚠ inferido tratados como confirmed
```

**Regla final**

```text
Cero inputs inventados. Cada input usado mapea a un output upstream confirmed.
```

**Validación operativa**

Cruce con catálogo de outputs upstream.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Static analysis de las 16 funciones.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 137 outputs cubiertos; 0 inputs inventados.

### 11.19 — Validación: secuencia respeta dependencias

<small>§6.19</small>

**Explicación**

Valida que el orden de `main()` respeta tanto las dependencias estructurales (Paso-02 2.13) como las temporales (Paso-08 8.11 + Paso-10 10.10).

**Patrón o fórmula**

```text
load → normalize → validate → HP → SO → GH → LBS → AC → GA →
inject → expand → link → score → check → qa → output
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
main() ejecuta las 16 funciones en orden secuencial respetando:
- Paso-02 2.13 (HP → SO → GH → LBS → AC → GAs)
- Paso-08 8.11 (parent antes que GA)
- Paso-10 10.10 (matriz dependencias)
0 inversiones detectadas.
```

**Ejemplos incorrectos**

```text
- Llamar generate_lbs() antes que generate_service_overview()
- score_priority() antes de generate_pages
- output_matrices() sin haber pasado QA gate
```

**Regla final**

```text
main() respeta el orden doctrinal de dependencias. Cualquier inversión es bug.
```

**Validación operativa**

Cruce con Paso-02 2.13 + Paso-08 8.11 + Paso-10 10.10.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspección manual del orden + cross-check con dependency graph.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** orden secuencial validado; 0 inversiones.

## Checklist Final

<small>§7</small>

> Validación operativa antes de cerrar el Paso 11 y avanzar al Paso 12 (Master Prompt).

### Validación de funciones de carga y normalización

- ☐ Función `load_inputs()` recoge 137 outputs upstream (11.1)
- ☐ Función `normalize_slugs()` produce slugs limpios (11.2)
- ☐ Función `validate_categories()` elimina duplicados (11.3)

### Validación de las 6 funciones de generación de páginas

- ☐ Función `generate_homepage()` produce 1 HP con spec 5.3 (11.4)
- ☐ Función `generate_service_overview()` produce S SO no-locales con spec 5.4 (11.5)
- ☐ Función `generate_geohub()` produce 1 GH con spec 5.7 (11.6)
- ☐ Función `generate_lbs()` produce S LBS con spec 5.5 (11.7)
- ☐ Función `generate_additional_category()` produce A AC con spec 5.6 (11.8)
- ☐ Función `generate_geoarticles()` produce G×S GAs con spec 5.8 (11.9)

### Validación de funciones de orquestación

- ☐ Función `inject_local_coverage()` aplica LCAs correctamente (11.10)
- ☐ Función `generate_expansion()` opcional según E (11.11)
- ☐ Función `assign_internal_links()` cumple matriz 7.11 (11.12)
- ☐ Función `score_priority()` aplica fórmula 8.1 (11.13)
- ☐ Función `check_dependencies()` bloquea violaciones (11.14)
- ☐ Función `run_qa()` aplica las 5 categorías + gate (11.15)
- ☐ Función `output_matrices()` produce 3 matrices (11.16)

### Validación de orquestador y cierre

- ☐ Pseudocódigo principal `main()` ejecuta las 16 funciones en orden (11.17)
- ☐ Cobertura de inputs heredados: 0 inputs inventados (11.18)
- ☐ Secuencia respeta dependencias estructurales y temporales (11.19)

## Outputs Consolidados

<small>§8</small>

> Tabla final compacta con la trazabilidad row-per-output. Los IDs (`11.1`–`11.19`) coinciden con los declarados en §5. Esta tabla es la fuente única de la trazabilidad consolidada del paso (sustituye al antiguo b-doc).

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 11.1 | ← Paso-01 1.1-1.14 + Paso-02 + Paso-03 | **Función load_inputs()** = dict con variables Cerrajeros | Lectura programática de §8 de cada a-doc + preflight. **Fuente:** GMB Crush. | confirmed |
| 11.2 | ← Paso-02 2.2-2.4 + Paso-03 3.3 | **Función normalize_slugs()** = `cerrajero` + `madrid` + 5 service_slugs + 1 additional_slug | Implementar slugify estándar. **Fuente:** GMB Crush. | confirmed |
| 11.3 | ← Paso-02 2.7 + 2.12 | **Función validate_categories()** = effective_additional con `[duplicado-llaves]` (A=1) | Comparar Additional vs core; aplicar criterio cobertura. **Fuente:** GMB Crush. | confirmed |
| 11.4 | ← Paso-04 4.3 + Paso-05 5.3 | **Función generate_homepage()** = 1 Homepage HP-001 (`/`) con 11 bloques | Aplicar spec Homepage del Paso-05 5.3 con inputs heredados. **Fuente:** GMB Crush. | confirmed |
| 11.5 | ← Paso-04 4.4 + Paso-05 5.4 | **Función generate_service_overview()** = 5 SO `/cerrajero/{service}/` no-locales | Aplicar spec SO del Paso-05 5.4 replicada × S core services. **Fuente:** GMB Crush. | confirmed |
| 11.6 | ← Paso-04 4.5 + Paso-05 5.7 + Paso-03 3.2 | **Función generate_geohub()** = 1 GeoHub `/madrid/` con 10 bloques + 21 internal links | Aplicar spec GeoHub Paso-05 5.7 al GeoHub Main City. **Fuente:** GMB Crush. | confirmed |
| 11.7 | ← Paso-04 4.6 + Paso-05 5.5 | **Función generate_lbs()** = 5 LBS `/cerrajero/madrid/{service}/` con LCAs Section + areaServed | Aplicar spec LBS Paso-05 5.5 replicada × S × Main City. **Fuente:** GMB Crush. | confirmed |
| 11.8 | ← Paso-04 4.7 + Paso-05 5.6 + Paso-03 3.3 | **Función generate_additional_category()** = 1 AC `/cerrajero/madrid/duplicado-llaves/` (A=1) | Aplicar spec AC Paso-05 5.6 a las A categorías efectivas. **Fuente:** GMB Crush. | confirmed |
| 11.9 | ← Paso-04 4.8 + Paso-05 5.8 + Paso-03 3.4 | **Función generate_geoarticles()** = 15 GAs `/madrid/{topic}/` (3 por servicio × 5 servicios) | Aplicar spec GA Paso-05 5.8 a G×S combinaciones service × topic. **Fuente:** GMB Crush. | confirmed |
| 11.10 | ← Paso-06 6.2 + 6.12 + 6.17 | **Función inject_local_coverage()** = 22 páginas locales con 10 LCAs en areaServed | Iterar páginas, mapear page_type → LCAs según matriz 6.12. **Fuente:** GMB Crush. | confirmed |
| 11.11 | ← Paso-01 1.11 + Paso-04 4.10 | **Función generate_expansion()** = `[]` (Phase 1, E=0) | Replicar lógica generate_*() para cada Approved Area. **Fuente:** GMB Crush. | confirmed |
| 11.12 | ← Paso-07 7.9 + 7.11 | **Función assign_internal_links()** = ~80 enlaces internos | Lookup matriz 7.11 + selección anchor por catálogo 7.9. **Fuente:** GMB Crush. | confirmed |
| 11.13 | ← Paso-08 8.1-8.10 | **Función score_priority()** = 28 URLs con scores 19-29, tiers P1-P3 | 6 funciones de medición + suma + mapeo tier/phase. **Fuente:** GMB Crush. | confirmed |
| 11.14 | ← Paso-08 8.11 + Paso-10 10.10 | **Función check_dependencies()** = 28 URLs validadas, 0 Blocked | Lookup parents + comparar phases + bloquear conflictos. **Fuente:** GMB Crush. | confirmed |
| 11.15 | ← Paso-09 9.2-9.8 | **Función run_qa()** = 28 URLs con publish_gate = Yes | 5 funciones QA + gate consolidation + GBP checklist. **Fuente:** GMB Crush. | confirmed |
| 11.16 | ← Paso-03 3.5 + 3.8 + Paso-07 7.11 | **Función output_matrices()** = 3 matrices (URL: 28 / Schema: 6 / Link: ~80) | Serializar páginas scored + link_matrix. **Fuente:** GMB Crush. | confirmed |
| 11.17 | ← 11.1-11.16 | **Pseudocódigo principal main()** = orquestador secuencial con 16 llamadas | Composición funcional + manejo de errores. **Fuente:** GMB Crush. | confirmed |
| 11.18 | ← Bloques 1-3 completos | **Validación cobertura inputs** = 137 outputs upstream cubiertos; 0 inputs inventados | Static analysis de las 16 funciones + cruce con catálogo upstream. **Fuente:** GMB Crush. | OK |
| 11.19 | ← Paso-02 2.13 + Paso-08 8.11 + Paso-10 10.10 | **Validación secuencia dependencias** = orden secuencial validado; 0 inversiones | Inspección manual del orden + cross-check con dependency graph. **Fuente:** GMB Crush. | OK |

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
> Las 16 funciones del Paso 11 NO inventan lógica nueva — formalizan en código la doctrina ya establecida en Bloques 1-3. Si una función necesita un input no presente en los outputs upstream, hay que volver al paso correspondiente y producirlo allí. El Paso 11 es el "compilador" del sistema, no su fuente. Las 6 funciones individuales `generate_*()` (HP/SO/GH/LBS/AC/GA) cumplen la separación de page types del Paso 5 — cada función aplica el spec doctrinal de su page type.
