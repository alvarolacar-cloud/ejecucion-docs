Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 5 — Salida a Mercado/paso-16-extraccion-diseno-layout/`, alineado con los frameworks oficiales GMB Crush.

# Paso 16 — Extracción y Diseño de Layout

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 6 outputs del Paso 16 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush.

# Bloque I — Introducción

## Objetivo del Paso 16

<small>§2</small>

En este paso la IA convierte una **referencia visual aprobada** (web propia, competidora o moodboard) en un **sistema de design tokens y layout maps** que el constructor (Paso 17) ejecuta literalmente sin decisiones de diseño. Cierra TODAS las decisiones estéticas antes de la construcción para garantizar consistencia visual y evitar inconsistencias en producción.

**Outputs del paso:**

- **16.1** Identidad Visual y CSS Base — colores HEX, tipografías, tamaños, radius, shadows extraídos
- **16.2** Layout y Estructura por Sección — mapeo de cada sección por page type
- **16.3** Propuesta de Diseño aprobada — resumen visual + Layout-Map para validación cliente
- **16.4** Design Tokens Tailwind — tipografía, colores, componentes en nomenclatura Tailwind
- **16.5** Reglas Críticas CSS — reglas de aplicación por componente (Hero, botones, cards, etc.)
- **16.6** Layout-Map Definitivo — estructura completa por page type cruzada con Paso 15

**Errores que previene:**

- Iniciar construcción sin tokens definidos (cada página usa colores distintos)
- Decisiones estéticas en build-time (rompe consistencia)
- Layout-Map ambiguo (constructor improvisa estructura)
- Sin validación de cliente sobre la propuesta visual
- Tokens sin nomenclatura Tailwind (constructor reescribe naming)

**Cuándo se ejecuta:** después de Paso 15 (Redacción) cerrado. Antes de Paso 17 (Constructor del Sitio).

## Info heredada de pasos anteriores

<small>§3</small>

| Campo | Origen |
|---|---|
| Spec por page type (9 sub-outputs) | Paso-05 5.3 a 5.8 |
| Content Architecture por page type | Paso-06 6.6 a 6.11 |
| Páginas redactadas (28+1) | Paso-15 15.3 a 15.9 |
| Web de referencia aprobada (input cliente) | Cliente confirma |

# Bloque II — Ejemplo rellenado para el Paso 16 — Diseño de Layout

<small>§4</small>

> Los 6 outputs del Paso 16 con sus valores reales para Cerrajeros Madrid 24h.

### 16.1 — Identidad Visual y CSS Base

```text
Extracción de la web de referencia aprobada (cliente):

Colores HEX:
  Primary:     #C8102E (rojo emergencia 24h)
  Secondary:   #1A1A1A (negro confianza)
  Accent:      #FFB800 (amarillo CTA)
  Background:  #FFFFFF
  Text:        #2C2C2C
  Border:      #E5E5E5

Tipografías:
  Heading: Inter (700, 600)
  Body:    Inter (400, 500)
  Mono:    JetBrains Mono (para números de tel)

Tamaños:
  H1: 48px (mobile 32px)
  H2: 36px (mobile 28px)
  H3: 24px
  Body: 16px
  Small: 14px

Radius:
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px

Shadows:
  card: 0 2px 8px rgba(0,0,0,0.08)
  hover: 0 4px 16px rgba(0,0,0,0.12)
  focus: 0 0 0 3px rgba(200,16,46,0.3)
```

### 16.2 — Layout y Estructura por Sección

```text
Mapeo por page type (cruzado con Paso 15):

HOMEPAGE:
  Hero (60vh) → Quick Answer (auto) → Services Grid (5 cards) →
  Coverage Preview (banner con LCAs) → Trust Blocks (3 cols) →
  FAQ Accordion → NAP Block → CTA Final → Footer

SERVICE OVERVIEW (5 instancias):
  Hero compacto (40vh) → AUDIO H2s (5 sections con bullets) →
  FAQ → CTA presupuesto → Sidebar related services + matching LBS

LOCATION-BASED SERVICE (5 instancias):
  Hero local (50vh) → Quick Local Answer (banner) →
  Authority + Uniqueness + Depth (3 cards) → Local Pain Points (lista) →
  LCAs Section (grid 5×2 con barrios) → Related Services (3 cards) →
  FAQ → CTA Llamar fixed-bottom-mobile

ADDITIONAL CATEGORY (1 instancia):
  Similar a LBS pero más compacta (40vh hero) → Use Case local →
  AUDIO H2s → FAQ → CTA presupuesto

GEOHUB:
  Hero ciudad (35vh con mapa) → Services Menu (5 LBS cards) →
  AC Menu (1 AC card) → LCAs Section (lista distritos) →
  GeoArticle Resources (15 cards 3×5 grid) → Trust → CTA

GEOARTICLE (15 instancias):
  Hero artículo (30vh con breadcrumb) → Intro → H2 sections →
  FAQ → CTA "Lee la página de [Service]" + sidebar related GAs
```

### 16.3 — Propuesta de Diseño aprobada

```text
Documento entregado al cliente para aprobación:

  - Mockups Figma (5 páginas representativas: HP, SO, LBS, GH, GA)
  - Color palette + Typography sample
  - Layout-Map preliminar
  - 3 variaciones de Hero para HP

Validación cliente:
  ✓ Aprobado: Color #C8102E + Inter + Hero variante 2
  ⚠ Cambio: Añadir banner de teléfono fixed-bottom en mobile (urgencia 24h)

Iteración aplicada → Propuesta v2 aprobada el 2026-04-30.
```

### 16.4 — Design Tokens Tailwind

```yaml
# tailwind.config.js
theme:
  extend:
    colors:
      primary:
        DEFAULT: '#C8102E'
        50: '#FDE7EC'
        500: '#C8102E'
        700: '#8C0B20'
      secondary:
        DEFAULT: '#1A1A1A'
      accent:
        DEFAULT: '#FFB800'
      bg:
        DEFAULT: '#FFFFFF'
        muted: '#F8F8F8'
      text:
        DEFAULT: '#2C2C2C'
        muted: '#6B6B6B'
      border: '#E5E5E5'
    fontFamily:
      sans: ['Inter', 'system-ui', 'sans-serif']
      mono: ['JetBrains Mono', 'monospace']
    fontSize:
      h1: ['48px', { lineHeight: '56px', fontWeight: '700' }]
      h2: ['36px', { lineHeight: '44px', fontWeight: '700' }]
      h3: ['24px', { lineHeight: '32px', fontWeight: '600' }]
    borderRadius:
      sm: '4px'
      md: '8px'
      lg: '16px'
      full: '9999px'
    boxShadow:
      card: '0 2px 8px rgba(0,0,0,0.08)'
      hover: '0 4px 16px rgba(0,0,0,0.12)'
      focus: '0 0 0 3px rgba(200,16,46,0.3)'
```

### 16.5 — Reglas Críticas CSS

```text
HERO:
  - Altura: 60vh desktop / 50vh tablet / 40vh mobile
  - H1 con line-height 1.15
  - CTA primary visible above-the-fold
  - Background: gradient con foto de servicio (no decorativo puro)

BUTTONS:
  - Primary: bg-primary text-white rounded-md px-6 py-3 font-semibold
  - Secondary: bg-secondary text-white
  - Accent (Llamar urgente): bg-accent text-secondary animate-pulse-soft
  - Hover: shadow-hover transform translateY(-1px)

CARDS:
  - bg-white rounded-lg shadow-card p-6
  - Hover: shadow-hover
  - Service cards: title H3 + descripción 2 líneas + CTA inline

GRIDS:
  - Mobile: 1 col
  - Tablet: 2 cols
  - Desktop: 3-5 cols según contexto (services 3, LCAs 5, GAs 3)
  - Gap: gap-6 desktop / gap-4 mobile

FORMS:
  - Input border-border focus:border-primary
  - Label arriba (no placeholder único)
  - Submit button bg-primary

MOBILE-FIRST:
  - Diseño base mobile, escala con breakpoints (sm/md/lg)
  - Phone banner fixed-bottom en mobile (cliente aprobó este cambio)
```

### 16.6 — Layout-Map Definitivo

```text
Cruzado con Paso 15 (redacción) — el constructor consume este map literalmente:

PAGE: HOMEPAGE (URL: /)
  Sections:
    1. <Header>
    2. <HeroHomepage> → H1 + Subtitle + 2 CTAs (Llamar / Servicios)
    3. <QuickAnswer> → 1 párrafo + bullets
    4. <ServicesGrid cols=3 mobile=1> → 5 ServiceCard
    5. <CoveragePreview> → Banner con 10 LCAs
    6. <TrustBlocks cols=3> → 5 trust cards
    7. <FAQAccordion> → 4 preguntas
    8. <NAPBlock> → NAP completo + map
    9. <FinalCTA> → 1 botón + contact
    10. <Footer>
  Schemas embebidos: Organization + WebSite + LocalBusiness + FAQPage + Speakable

PAGE: SERVICE OVERVIEW (URLs: /cerrajero/{service-slug}/)
  Variantes: 5 (1 por core service)
  Sections:
    1. <Header>
    2. <HeroSO compact=true> → H1 + intro NO local + 1 CTA presupuesto
    3. <AudioSection name="Authority">
    4. <AudioSection name="Uniqueness">
    5. <AudioSection name="Depth">
    6. <AudioSection name="Intent">
    7. <AudioSection name="Optimization">
    8. <Bullets> + 3-5 ventajas
    9. <FAQAccordion> → 3-5 preguntas
    10. <CTAPresupuesto>
    11. <SidebarRelated> → matching LBS + otras SO + 1 GA
    12. <Footer>
  Schemas: Service + WebPage + BreadcrumbList + Speakable

PAGE: LOCATION-BASED SERVICE (URLs: /cerrajero/madrid/{service-slug}/)
  Variantes: 5
  Sections:
    1. <Header>
    2. <HeroLBS local=true> → H1 + intro local + CTA Llamar
    3. <QuickLocalAnswer banner=true>
    4. <Cards3Cols name="Authority+Uniqueness+Depth">
    5. <LocalPainPoints list=true>
    6. <LCAsSection grid="5x2"> → 10 LCAs (Almagro, Chamberí, ...)
    7. <RelatedServices cards=3>
    8. <FAQAccordion> → 4-6 preguntas
    9. <CTAFixedBottomMobile> → Llamar urgente 24h
    10. <Footer>
  Schemas: LocalBusiness + BreadcrumbList + FAQPage + Speakable

PAGE: ADDITIONAL CATEGORY (URL: /cerrajero/madrid/duplicado-llaves/)
  Variantes: 1 (A=1)
  Sections: Hero compact + UseCase + Audio + FAQ + CTA
  Schemas: Service + BreadcrumbList + FAQPage

PAGE: GEOHUB (URL: /madrid/)
  Variantes: 1
  Sections:
    1. <Header>
    2. <HeroCity hasMap=true>
    3. <ServicesMenu cards=5>
    4. <ACMenu cards=1>
    5. <LCAsList visible=true>
    6. <GAResourcesGrid 3x5>
    7. <TrustBlocks>
    8. <CTAFinal>
    9. <Footer>
  Schemas: CollectionPage + BreadcrumbList

PAGE: GEOARTICLE (URLs: /madrid/{topic}/)
  Variantes: 15
  Sections: Hero artículo + Intro + 5 H2s + FAQ + CTAtoLBS + Sidebar
  Schemas: Article + FAQPage + BreadcrumbList + Speakable
```

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 16.1 | Identidad Visual y CSS Base | Sistema visual extraído | GMB Crush + Input humano | — (input cliente: web de referencia) |
| 16.2 | Layout y Estructura por Sección | Mapeo layout × page type | GMB Crush | Paso-05 5.3-5.8 + Paso-06 6.6-6.11 |
| 16.3 | Propuesta de Diseño aprobada | Documento de validación cliente | GMB Crush + Input humano | Paso-16 16.1 + 16.2 (intra-paso) |
| 16.4 | Design Tokens Tailwind | tailwind.config.js | GMB Crush | Paso-16 16.1 (intra-paso) |
| 16.5 | Reglas Críticas CSS | Reglas por componente | GMB Crush | Paso-16 16.4 (intra-paso) |
| 16.6 | Layout-Map Definitivo | Map por page type cruzado con copy | GMB Crush | Paso-16 16.2 + Paso-15 15.3-15.9 |

## Obtención de Outputs

<small>§6</small>

### 16.1 — Identidad Visual y CSS Base

<small>§6.1</small>

**Explicación**

Extracción de los elementos visuales clave de la web de referencia aprobada por el cliente. Es el ancla doctrinal de TODAS las decisiones de diseño downstream.

**Patrón o fórmula**

```text
Web de referencia → extracción colores + tipografías + tamaños + radius + shadows
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 16.1.

**Ejemplos incorrectos**

```text
- Inventar colores sin web de referencia
- Mezclar 2-3 webs de referencia (rompe coherencia)
- Saltar la fase de extracción (decisiones improvisadas en build)
```

**Regla final**

```text
Identidad visual = extracción literal de UNA web de referencia aprobada.
```

**Validación operativa**

Aplicar al inicio del paso. Cliente confirma colores + tipografías exactos antes de proceder.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Input humano.
- **Método:** Inspección visual + DevTools de la web de referencia + extracción manual de tokens.

**Output del paso**

- **Tipo:** Sistema visual extraído.
- **Ejemplo (Cerrajeros Madrid 24h):** colores rojo/negro/amarillo + Inter + sizes/radius/shadows definidos.

### 16.2 — Layout y Estructura por Sección

<small>§6.2</small>

**Explicación**

Mapeo de las secciones de cada page type. Define el orden y composición de bloques visuales por tipo de página.

**Patrón o fórmula**

```text
Por cada page type:
  Lista de secciones en orden + variantes (mobile/desktop) + composición
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 16.2 — 6 page types con sus secciones definidas.

**Ejemplos incorrectos**

```text
- Layout sin distinguir por page type
- Layouts contradictorios con Content Architecture (Paso-06)
- Sections sin variantes mobile (rompe mobile-first)
```

**Regla final**

```text
Layout-Map definido por page type, alineado con Content Architecture del Paso-06.
```

**Validación operativa**

Cruce con Paso-05 5.3-5.8 + Paso-06 6.6-6.11.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Mapear secciones de cada page type a partir de los specs heredados.

**Output del paso**

- **Tipo:** Mapeo layout × page type.
- **Ejemplo (Cerrajeros Madrid 24h):** 6 page types × 8-12 secciones por tipo.

### 16.3 — Propuesta de Diseño aprobada

<small>§6.3</small>

**Explicación**

Documento entregado al cliente para validación visual antes de proceder con tokens y layout definitivos. Incluye mockups + paleta + tipografías + variaciones.

**Patrón o fórmula**

```text
Mockups Figma (5 páginas) + Palette + Typography + Variantes Hero
→ Cliente revisa → ✓ Aprobado o ⚠ Iteración
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 16.3 — propuesta v1 → iteración con phone banner mobile → v2 aprobada.

**Ejemplos incorrectos**

```text
- Saltar la fase de aprobación (cliente recibe sorpresa en producción)
- Aprobación verbal sin documento (sin trazabilidad)
- Mockups solo desktop (cliente no ve mobile)
```

**Regla final**

```text
Propuesta de Diseño aprobada por escrito antes de generar tokens definitivos.
```

**Validación operativa**

Cliente firma aprobación. Iteraciones se documentan.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Input humano.
- **Método:** Generar mockups en Figma + paleta + typography sample → cliente revisa → iteración → aprobación.

**Output del paso**

- **Tipo:** Documento de validación.
- **Ejemplo (Cerrajeros Madrid 24h):** Propuesta v2 aprobada el 2026-04-30.

### 16.4 — Design Tokens Tailwind

<small>§6.4</small>

**Explicación**

Tokens extraídos del 16.1 expresados en `tailwind.config.js`. El constructor (Paso 17) consume este archivo literalmente.

**Patrón o fórmula**

```text
Identidad Visual (16.1) → tailwind.config.js con extend.colors / fontFamily / fontSize / etc.
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 16.4 — tailwind.config con primary/secondary/accent + Inter + sizes/radius/shadows.

**Ejemplos incorrectos**

```text
- Tokens en CSS variables (rompe convención Tailwind)
- Tokens con naming arbitrario (constructor reescribe)
- Tokens sin variantes 50-700 para colores principales
```

**Regla final**

```text
Tokens en tailwind.config.js con nomenclatura consistente.
```

**Validación operativa**

Validar que tailwind.config genera CSS sin errores.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Convertir 16.1 a estructura Tailwind config.

**Output del paso**

- **Tipo:** tailwind.config.js.
- **Ejemplo (Cerrajeros Madrid 24h):** archivo de ~50 líneas con extend completo.

### 16.5 — Reglas Críticas CSS

<small>§6.5</small>

**Explicación**

Reglas de aplicación por componente (Hero, Buttons, Cards, Grids, Forms). Garantiza consistencia entre páginas.

**Patrón o fórmula**

```text
Por cada componente: declarar clases Tailwind base + variantes + breakpoints
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 16.5 — 6 componentes con sus reglas.

**Ejemplos incorrectos**

```text
- Reglas vagas ("hacer botones bonitos")
- Sin variantes mobile/desktop
- Sin reglas para hover/focus/active
```

**Regla final**

```text
Cada componente tiene reglas explícitas para base + variantes + breakpoints.
```

**Validación operativa**

Cruce con 16.4 (tokens) y 16.6 (layout map).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Definir reglas por componente alineadas con tokens.

**Output del paso**

- **Tipo:** Documento de reglas.
- **Ejemplo (Cerrajeros Madrid 24h):** 6 componentes con reglas detalladas.

### 16.6 — Layout-Map Definitivo

<small>§6.6</small>

**Explicación**

Layout-Map cruzado con copy del Paso 15. El constructor (Paso 17) consume este map para generar las páginas.

**Patrón o fórmula**

```text
Por cada page type: lista de <Components> + props + secciones de copy
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 16.6 — 6 page types con sus components.

**Ejemplos incorrectos**

```text
- Layout-Map sin cruzar con copy (constructor inventa estructura)
- Components sin props (constructor improvisa)
- Sin schemas embebidos por page type
```

**Regla final**

```text
Layout-Map = receta literal para constructor; cero ambigüedad.
```

**Validación operativa**

Cruce con Paso-15 15.3-15.9 (copy redactado) + Paso-05 5.9 (schemas).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Mapear cada sección del 16.2 a `<Component>` con props alineados con copy del Paso 15.

**Output del paso**

- **Tipo:** Map por page type.
- **Ejemplo (Cerrajeros Madrid 24h):** 6 page types con receta completa de components.

## Checklist Final

<small>§7</small>

- ☐ Identidad Visual extraída de web de referencia (16.1)
- ☐ Layout por page type definido (16.2)
- ☐ Propuesta de Diseño aprobada por cliente (16.3)
- ☐ Design Tokens Tailwind generados (16.4)
- ☐ Reglas Críticas CSS documentadas (16.5)
- ☐ Layout-Map Definitivo cruzado con copy (16.6)

## Outputs Consolidados

<small>§8</small>

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 16.1 | — (input cliente) | **Identidad Visual y CSS Base** = colores rojo/negro/amarillo + Inter + tokens completos | Inspección visual + DevTools de web referencia. **Fuente:** GMB Crush + Input humano. | confirmed |
| 16.2 | ← Paso-05 5.3-5.8 + Paso-06 6.6-6.11 | **Layout y Estructura por Sección** = 6 page types × 8-12 secciones cada uno | Mapear secciones por page type a partir de specs heredados. **Fuente:** GMB Crush. | confirmed |
| 16.3 | ← 16.1 + 16.2 | **Propuesta de Diseño aprobada** = Propuesta v2 aprobada 2026-04-30 (con phone banner mobile) | Mockups Figma + paleta + typography → cliente revisa → iteración → aprobación. **Fuente:** GMB Crush + Input humano. | confirmed |
| 16.4 | ← 16.1 | **Design Tokens Tailwind** = tailwind.config.js con extend completo | Convertir 16.1 a estructura Tailwind config. **Fuente:** GMB Crush. | confirmed |
| 16.5 | ← 16.4 | **Reglas Críticas CSS** = 6 componentes con reglas (Hero/Buttons/Cards/Grids/Forms/Mobile) | Definir reglas por componente alineadas con tokens. **Fuente:** GMB Crush. | confirmed |
| 16.6 | ← 16.2 + Paso-15 15.3-15.9 | **Layout-Map Definitivo** = 6 page types con receta de components + props + schemas | Mapear secciones a Components + props alineados con copy. **Fuente:** GMB Crush. | confirmed |

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
- Design Extraction Framework GMB Crush

> **Nota — Diseño cierra antes de construir:**
> El Paso 16 cierra TODAS las decisiones estéticas antes del Paso 17 (Constructor). El constructor NO toma decisiones de diseño; solo ejecuta lo que dice este paso. Si una decisión de diseño se filtra al Paso 17, la consistencia visual se rompe y hay que volver atrás.
