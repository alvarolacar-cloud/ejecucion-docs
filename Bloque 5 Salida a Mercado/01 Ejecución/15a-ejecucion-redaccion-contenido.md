Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 5 — Salida a Mercado/paso-15-redaccion-contenido/`, alineado con los frameworks oficiales GMB Crush.

# Paso 15 — Redacción de Contenido

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 13 outputs del Paso 15 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush.

# Bloque I — Introducción

## Objetivo del Paso 15

<small>§2</small>

En este paso la IA redacta **TODO el copy del cluster web** aplicando 4 capas de redacción (Estructura / Zonas / Argumentos / Entidades) a los 6 page types doctrinales. Aplica las 4 reglas de calidad universales (Hero+CTA / Problema+Realidad / Datos+Precio / Contexto Local) + 13 reglas operativas que previenen canibalización, clusters rotos, reseñas inventadas y copy genérico. Es el paso que transforma la arquitectura de Bloques 1-4 en contenido publicable.

**Outputs del paso:**

- **15.1** Capas de redacción — 4 capas verticales (Estructura / Zonas / Argumentos / Entidades)
- **15.2** Reglas de calidad universal — 4 reglas (Hero+CTA / Problema+Realidad / Datos+Precio / Contexto Local)
- **15.3** Homepage redactada (1 página, 4 capas aplicadas)
- **15.4** Service Overview Pages redactadas (S=5 páginas, 4 capas × cada una)
- **15.5** Location-Based Service Pages redactadas (S=5 páginas, 4 capas × cada una)
- **15.6** Additional Category Page redactada (A=1 página, 4 capas)
- **15.7** GeoHub redactada (1 página, 4 capas)
- **15.8** GeoArticles redactados (G×S=15 artículos, 4 capas × cada uno)
- **15.9** Página de contacto redactada (1 página auxiliar)
- **15.10** Validación clusters completos por servicio (5 clusters core)
- **15.11** Validación Service Overview no compite con LBS (separación de roles)
- **15.12** Validación GeoArticle enlaza a LBS padre (3 puntos, anchors variados)
- **15.13** Validación datos verificables + sin reseñas inventadas (regla web-first)

**Errores que previene:**

- Publicar páginas con copy genérico sin contexto local
- Mezclar Service Overview con Location-Based Service (canibalización)
- Inventar reseñas o claims antes del Paso 14
- Hero pages largos con texto que hace scroll en móvil
- Anchors todos branded (sin variedad)
- Publicar cluster roto (servicio sin SO + LBS + 3 GAs)
- Saltar capas de redacción (texto sin Estructura → Zonas → Argumentos → Entidades)

**Cuándo se ejecuta:** después de Pasos 1-13 cerrados (Bloques 1-4 completos). El Paso 14 (GBP Creation) puede ser paralelo o posterior. Antes de Paso 16 (Diseño/Layout).

## Info heredada de pasos anteriores

<small>§3</small>

> Estos campos NO se deciden en Paso 15 — la IA los lee del paso indicado y los usa como input para redactar el contenido del Bloque III.

| Campo | Origen |
|---|---|
| Business Name | Paso-01 1.1 |
| Full NAP | Paso-01 1.4 |
| Main City | Paso-01 1.7 |
| Servicios principales (S=5) | Paso-01 1.9 |
| Local Coverage Areas | Paso-01 1.10 |
| Trust Signals | Paso-01 1.14 |
| Total páginas SEO base | Paso-02 2.9 |
| Inventario por tipo de página | Paso-02 2.10 |
| URL Matrix completa | Paso-03 3.5 |
| Validación No falsa ubicación | Paso-04 4.14 |
| Spec por page type (9 sub-outputs) | Paso-05 5.3 a 5.8 |
| Validación Word count | Paso-05 5.10 |
| Content Architecture por page type | Paso-06 6.6 a 6.11 |
| Schema `areaServed` coherente | Paso-06 6.17 |
| Anchor text variado | Paso-07 7.9 |
| Matriz de enlaces obligatorios | Paso-07 7.11 |
| Inventario priorizado completo | Paso-08 8.14 |
| Final Publish Gate | Paso-09 9.7 |
| Master Prompt + auxiliares | Paso-12 12.1-12.5 |
| Reglas No Negociables | Paso-13 13.6 |

# Bloque II — Ejemplo rellenado para el Paso 15 — Redacción de Contenido

<small>§4</small>

> Los 13 outputs del Paso 15 con sus valores reales para Cerrajeros Madrid 24h.

### 15.1 — Capas de redacción

```text
4 capas aplicadas en orden a cada página:

Capa 1 — ESTRUCTURA:
  H1 + H2s + secciones obligatorias por page type (spec Paso-05 5.3-5.8)
  Word count en rango doctrinal (Paso-05 5.10)

Capa 2 — ZONAS:
  Inyección de Local Coverage Areas en secciones permitidas
  (LBS, GH, AC, GA: en H2 dedicado + areaServed; HP: solo Main City;
   SO: ninguna LCA — page type no-local)

Capa 3 — ARGUMENTOS:
  Razones específicas de por qué elegir el negocio
  (no claims genéricos; datos verificables; trust signals reales)

Capa 4 — ENTIDADES:
  Inyección de entidades semánticas relevantes
  (servicios, ciudades, categorías GBP, marcas, normativas)
```

### 15.2 — Reglas de calidad universal

```text
Regla 1 — Hero + CTA:
  Hero compacto (cabe en móvil sin scroll); CTA visible above-the-fold

Regla 2 — Problema + Realidad:
  Empezar describiendo el problema concreto del usuario;
  no abrir con descripción del negocio

Regla 3 — Datos + Precio:
  Incluir datos verificables (precios desde, tiempos típicos, garantías reales);
  no claims genéricos ("los mejores", "los más rápidos")

Regla 4 — Contexto Local:
  Mencionar barrios, calles, casos de uso reales del Main City;
  no listados vacíos de zonas
```

### 15.3 — Homepage redactada

```text
URL: /
Word count: 1,050 palabras (rango HP 900-1,300 ✓)

Capa 1 — Estructura aplicada:
  H1: Cerrajeros Madrid 24h — Cerrajero urgente de confianza en Madrid
  Intro con marca + servicio + Main City
  Quick Answer block
  Servicios principales (5 cards con CTA a SO)
  Vista previa cobertura local (10 LCAs en lista)
  Bloques de confianza (5 trust signals)
  FAQ (4 preguntas)
  Bloque NAP completo
  CTA final
  Enlaces internos (8): 5 SO + 1 GeoHub + 1 AC + 1 contacto

Capa 2 — Zonas: Madrid + 10 LCAs en sección dedicada
Capa 3 — Argumentos: 10+ años, técnicos cualificados, garantía, servicio móvil
Capa 4 — Entidades: Cerrajero, Madrid, GBP categories, normativa cerraduras
```

### 15.4 — Service Overview Pages redactadas (5 páginas)

```text
URLs: /cerrajero/{cerrajero-urgente, apertura-puertas, cambio-cerraduras,
                  cambio-bombines, instalacion-cerraduras-seguridad}/
Word count: 850-1,000 cada una (rango SO ✓)

Capa 1 — Estructura aplicada:
  H1: Servicios profesionales de [Service] por Cerrajeros Madrid 24h
  Intro NO local (pilar temático sin geo)
  H2 Authority — experiencia técnica del servicio
  H2 Uniqueness — diferenciación
  H2 Depth — profundidad técnica del servicio
  H2 Intent — para quién es el servicio
  H2 Optimization — cómo optimizar
  Bullet sections con beneficios
  FAQs (3-5 preguntas)
  CTA: Solicitar presupuesto
  Enlaces internos: HP + LBS matching + otras SO + GA relevante

Capa 2 — Zonas: NINGUNA (SO no se geolocaliza, regla 15.11)
Capa 3 — Argumentos: especialización técnica + casos de uso
Capa 4 — Entidades: tipos de cerraduras, marcas, normativa
```

### 15.5 — Location-Based Service Pages redactadas (5 páginas)

```text
URLs: /cerrajero/madrid/{service-slug}/
Word count: 800-1,000 cada una (rango LBS ✓)

Capa 1 — Estructura aplicada:
  H1: Cerrajeros Madrid 24h — [Service] en Madrid
  Intro local con dolor del usuario
  Quick Local Answer
  H2 Authority + Uniqueness + Depth
  H2 Local Pain Points (problemas específicos en Madrid)
  H2 Local Coverage Areas Served (10 LCAs en sección dedicada, naturales)
  H2 Related Services in Madrid (cross-link a otras LBS)
  FAQs (4-6) con cobertura natural
  CTA: Llamar ahora · 24h
  Enlaces internos: parent SO + GeoHub + 3 LBS lateral + 2 GAs + contacto

Capa 2 — Zonas: 10 LCAs naturales (Almagro, Chamberí, Salamanca, Retiro,
              Centro, Tetuán, Chamartín, Arganzuela, Moncloa, Prosperidad)
Capa 3 — Argumentos: tiempo de llegada, precio orientativo, garantía
Capa 4 — Entidades: Cerrajero, Madrid, distritos, GBP Cerrajero
```

### 15.6 — Additional Category Page redactada (A=1)

```text
URL: /cerrajero/madrid/duplicado-llaves/
Word count: 880 palabras (rango AC 800-1,000 ✓)

Capa 1 — Estructura aplicada:
  H1: Cerrajeros Madrid 24h — Duplicado de llaves experto en Madrid
  Intro con problema local específico
  H2 Authority + Uniqueness + Depth + Intent + Optimization
  Local Coverage Use Case (caso real con LCA)
  FAQs (4)
  CTA: Solicitar presupuesto
  Enlaces internos: GeoHub + 2 LBS relacionadas + 1 GA + contacto

Capa 2 — Zonas: 10 LCAs (Madrid + Almagro, Chamberí, Salamanca, etc.)
Capa 3 — Argumentos: tipos de llaves duplicables, precios, tiempo
Capa 4 — Entidades: tipos de llaves, marcas (TESA, FAC, IFAM), normativa
```

### 15.7 — GeoHub redactada

```text
URL: /madrid/
Word count: 980 palabras (rango GH 700-1,100 ✓)

Capa 1 — Estructura aplicada:
  H1: Cerrajeros Madrid 24h — Servicios de cerrajería en Madrid
  City Intro con marca + servicios principales
  Menú de servicios (5 LBS con CTA a cada)
  Additional Category Menu (1 AC: Duplicado de llaves)
  Local Coverage Areas Section (10 LCAs en lista visible)
  GeoArticle Resources (15 GAs agrupados por servicio)
  Trust Signals
  CTA: Llamar ahora
  Enlaces internos: HP + 5 LBS + 1 AC + 15 GAs + contacto (22 enlaces)

Capa 2 — Zonas: 10 LCAs en sección dedicada (visible a un click)
Capa 3 — Argumentos: cobertura completa Madrid + 24h + servicio móvil
Capa 4 — Entidades: Madrid + distritos + barrios + GBP Cerrajero
```

### 15.8 — GeoArticles redactados (15 artículos)

```text
URLs: /madrid/{topic}/  (15 GAs validados con keyword research)
Word count: 1,000-1,500 cada uno (rango GA ✓)

Distribución:
  3 por Cerrajero urgente: cuanto-cuesta-... / que-hacer-si-no-puedes-... / cuanto-tarda-...
  3 por Apertura de puertas: cuanto-cuesta-abrir-... / que-hacer-si-te-dejas-llaves / sin-romper-cerradura
  3 por Cambio cerraduras: cuando-cambiar-... / cambio-tras-perder-llaves / cerradura-nueva-o-reparacion
  3 por Cambio bombines: cuando-cambiar-bombin / antibumping / cambio-bombin-sin-cambiar-cerradura
  3 por Instalación seguridad: mejores-cerraduras-viviendas / comunidades / puerta-blindada

Capa 1 — Estructura aplicada (cada GA):
  H1: [Article Topic] in Madrid
  Intro contextual (problema long-tail)
  H2 Problem
  H2 Local Context
  H2 Options / Mistakes
  H2 When to Call
  H2 Local Examples (caso real con LCA)
  FAQs (3-5)
  CTA: "Lee la página de [Service] en Madrid" → matching LBS
  Enlaces internos: matching LBS (parent) + GeoHub + GAs related + contacto

Capa 2 — Zonas: LCAs como ejemplos contextuales (no listados vacíos)
Capa 3 — Argumentos: datos verificables (precios desde, tiempos)
Capa 4 — Entidades: servicios, marcas, normativa, escenarios
```

### 15.9 — Página de contacto redactada

```text
URL: /contacto/
Word count: 320 palabras (página auxiliar, no SEO base)

Capa 1 — Estructura aplicada:
  H1: Contacta con Cerrajeros Madrid 24h
  NAP completo
  Formulario de contacto (3 campos)
  Mapa de cobertura
  Horario de atención (24h)
  CTA: Llamar ahora · WhatsApp · Email
  Schema: ContactPoint
```

### 15.10 — Validación clusters completos por servicio

```text
Cluster por servicio = SO + LBS + 3 GeoArticles (mínimo 5 páginas).
Si falta cualquiera, cluster ROTO → no se publica el servicio.

Cerrajeros Madrid 24h — 5 clusters validados:
  1. Cerrajero urgente:    SO-1 + LBS-1 + 3 GAs (GA-1, GA-2, GA-3) ✓
  2. Apertura de puertas:   SO-2 + LBS-2 + 3 GAs (GA-4, GA-5, GA-6) ✓
  3. Cambio cerraduras:     SO-3 + LBS-3 + 3 GAs (GA-7, GA-8, GA-9) ✓
  4. Cambio bombines:       SO-4 + LBS-4 + 3 GAs (GA-10, GA-11, GA-12) ✓
  5. Instalación seguridad: SO-5 + LBS-5 + 3 GAs (GA-13, GA-14, GA-15) ✓

5/5 clusters completos. 0 clusters rotos.
```

### 15.11 — Validación Service Overview no compite con LBS

```text
Verificar:
- SO H1: "Servicios profesionales de [Service] por [Brand]" (no menciona Madrid)
- LBS H1: "[Brand] – [Service] en Madrid" (sí menciona Madrid)
- 0 H1 duplicados o casi-duplicados entre SO y LBS

Cerrajeros Madrid 24h: 5 SO vs 5 LBS validados; 0 conflictos.
```

### 15.12 — Validación GeoArticle enlaza a LBS padre

```text
Cada GA debe tener 3 puntos de enlace a su LBS parent:
  1. Enlace inline en intro contextual (anchor variado)
  2. Enlace en H2 "When to Call"
  3. CTA final "Lee la página de [Service] en Madrid"

Cumple Paso-08 8.11 (landing antes que GA) + Paso-07 7.7.

Cerrajeros: 15 GAs × 3 puntos = 45 enlaces a LBS parent. 0 GAs sin enlace.
```

### 15.13 — Validación datos verificables + sin reseñas inventadas

```text
Verificar:
- 0 menciones a "X reseñas en Google" antes del Paso 14
- 0 review.aggregateRating en schema sin reseñas reales
- Trust signals con datos verificables (10+ años → confirmable)
- Precios "desde X€" reales (no inventados)
- Tiempos típicos basados en operativa real

Cerrajeros (web-first, GBP=Not Created):
- 0 reseñas Google afirmadas en copy
- Schema sin review.aggregateRating
- Trust signals: 5 verificables (años, técnicos, móvil, garantía, reseñas-pendientes)
```

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

> Tabla declarativa de los 13 outputs que el Paso 15 debe producir.

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 15.1 | Capas de redacción (4 capas) | Framework declarativo | GMB Crush | — |
| 15.2 | Reglas de calidad universal (4 reglas) | Reglas declarativas | GMB Crush | — |
| 15.3 | Homepage redactada | 1 página redactada (4 capas) | GMB Crush | Paso-05 5.3 + Paso-06 6.6 + Paso-12 12.3 |
| 15.4 | Service Overview Pages redactadas | S páginas redactadas (4 capas × cada) | GMB Crush | Paso-05 5.4 + Paso-06 6.7 |
| 15.5 | Location-Based Service Pages redactadas | S páginas redactadas (4 capas × cada) | GMB Crush | Paso-05 5.5 + Paso-06 6.8 + Paso-01 1.10 |
| 15.6 | Additional Category Page redactada | A páginas redactadas (4 capas × cada) | GMB Crush | Paso-05 5.6 + Paso-06 6.9 |
| 15.7 | GeoHub redactada | 1 página redactada (4 capas) | GMB Crush | Paso-05 5.7 + Paso-06 6.10 |
| 15.8 | GeoArticles redactados | G×S artículos redactados (4 capas × cada) | GMB Crush | Paso-05 5.8 + Paso-06 6.11 + Paso-03 3.4 |
| 15.9 | Página de contacto redactada | 1 página auxiliar | GMB Crush | Paso-01 1.4 |
| 15.10 | Validación clusters completos | Validation flag | GMB Crush | Paso-01 1.9 + Paso-02 2.10 |
| 15.11 | Validación SO no compite con LBS | Validation flag | GMB Crush | Paso-05 5.4 + 5.5 |
| 15.12 | Validación GA enlaza a LBS padre | Validation flag | GMB Crush | Paso-07 7.7 + Paso-08 8.11 |
| 15.13 | Validación datos verificables + sin reseñas inventadas | Validation flag | GMB Crush | Paso-01 1.3 + Paso-09 9.8 |

## Obtención de Outputs

<small>§6</small>

### 15.1 — Capas de redacción

<small>§6.1</small>

**Explicación**

Las 4 capas verticales aplicadas a cada página garantizan que el copy tenga estructura, contexto local, argumentos y entidades semánticas. Sin las 4 capas, el contenido es genérico y no posiciona.

**Patrón o fórmula**

```text
Capa 1 Estructura → Capa 2 Zonas → Capa 3 Argumentos → Capa 4 Entidades
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 15.1.

**Ejemplos incorrectos**

```text
- Saltar Capa 2 Zonas en LBS (rompe regla local context)
- Aplicar Capa 2 Zonas en SO (rompe rol no-local)
- Saltar Capa 4 Entidades (copy sin profundidad semántica)
```

**Regla final**

```text
Las 4 capas son aplicación obligatoria por página, en orden.
```

**Validación operativa**

Aplicar a las 28 páginas SEO base + 1 auxiliar.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar las 4 capas en orden a cada página según su page type.

**Output del paso**

- **Tipo:** Framework declarativo.
- **Ejemplo (Cerrajeros Madrid 24h):** las 4 capas aplicadas a 29 páginas.

### 15.2 — Reglas de calidad universal

<small>§6.2</small>

**Explicación**

4 reglas que aplican a TODAS las páginas, independientemente del page type. Definen calidad de copy mínima.

**Patrón o fórmula**

Ver §4 sub-sección 15.2.

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
LBS-1 cumple las 4 reglas:
- Hero compacto (300 palabras above-the-fold) + CTA Llamar visible
- Intro empieza con "¿Necesitas cerrajero urgente en Madrid?"
- Datos: Precio desde 50€ + Llegada en 30 min + Garantía 12 meses
- Contexto local: menciona Almagro, Chamberí en H2 Coverage
```

**Ejemplos incorrectos**

```text
- Hero con 800 palabras (no cabe en móvil)
- Intro con "Somos los mejores cerrajeros..." (no empieza con problema)
- Trust signals sin datos verificables ("los más rápidos")
- "Cubrimos toda Madrid" sin mencionar barrios concretos
```

**Regla final**

```text
Las 4 reglas son universales — aplican a las 28 páginas SEO base.
```

**Validación operativa**

Aplicar a cada página redactada.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** QA por página contra las 4 reglas.

**Output del paso**

- **Tipo:** Reglas declarativas.
- **Ejemplo (Cerrajeros Madrid 24h):** 4 reglas aplicadas a 29 páginas; 0 violaciones.

### 15.3 — Homepage redactada

<small>§6.3</small>

**Explicación**

La Homepage aplica las 4 capas con spec Paso-05 5.3 + content architecture Paso-06 6.6. Es la página de entidad — concentra señales de marca + categoría + Main City + servicios + cobertura.

**Patrón o fórmula**

```text
Capa 1 Estructura: H1 + 11 bloques (Paso-06 6.6)
Capa 2 Zonas: solo Main City (no LCAs en HP)
Capa 3 Argumentos: 5 trust signals
Capa 4 Entidades: marca + categoría + Main City + servicios
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 15.3.

**Ejemplos incorrectos**

```text
- Homepage con 5 ciudades como targets equivalentes
- Homepage sin NAP completo
- Homepage sin enlaces a SO
- Homepage con 800 palabras (debajo del rango 900-1,300)
```

**Regla final**

```text
Homepage redactada = 1 página, 11 bloques, 4 capas, 1,050 palabras (en rango).
```

**Validación operativa**

Cruce con Paso-05 5.3 + Paso-06 6.6 + Paso-12 12.3 (Auxiliary Content Architecture).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar Auxiliary Content Architecture prompt (Paso-12 12.3) a Homepage spec.

**Output del paso**

- **Tipo:** 1 página redactada.
- **Ejemplo (Cerrajeros Madrid 24h):** Homepage de 1,050 palabras.

### 15.4 — Service Overview Pages redactadas

<small>§6.4</small>

**Explicación**

Las S=5 SO se redactan con spec Paso-05 5.4 (Topical Authority Pillar). Son **NO geolocalizadas** — no mencionan Madrid como target principal.

**Patrón o fórmula**

```text
Por cada core service (i = 1..5):
  Capa 1 Estructura: H1 + AUDIO H2s (Authority/Uniqueness/Depth/Intent/Optimization)
  Capa 2 Zonas: NINGUNA (SO es no-local)
  Capa 3 Argumentos: especialización técnica
  Capa 4 Entidades: tipos de servicio, marcas, normativa
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 15.4.

**Ejemplos incorrectos**

```text
- SO con H1 "Cerrajero urgente en Madrid" (rompe rol no-local; ese es LBS)
- SO con sección Local Coverage Areas (rompe rol no-local)
- SO escrita como artículo informacional (rompe rol pilar comercial)
```

**Regla final**

```text
S Service Overview Pages redactadas como pilares temáticos NO geolocalizados.
```

**Validación operativa**

Cruce con Paso-05 5.4 + Paso-06 6.7 + Paso-15 15.11.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar Auxiliary Content Architecture × S core services con spec SO.

**Output del paso**

- **Tipo:** S páginas redactadas.
- **Ejemplo (Cerrajeros Madrid 24h):** 5 SO de 850-1,000 palabras cada una.

### 15.5 — Location-Based Service Pages redactadas

<small>§6.5</small>

**Explicación**

Las S=5 LBS se redactan con spec Paso-05 5.5 (Main City Converter). Son las páginas comerciales más importantes — convierten búsquedas locales servicio + Main City.

**Patrón o fórmula**

```text
Por cada core service × Main City (i = 1..5):
  Capa 1 Estructura: H1 + 12 bloques (Paso-06 6.8)
  Capa 2 Zonas: 10 LCAs en H2 dedicado + areaServed
  Capa 3 Argumentos: tiempo de llegada, precio, garantía
  Capa 4 Entidades: servicio, Main City, distritos, GBP categoría
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 15.5.

**Ejemplos incorrectos**

```text
- LBS sin sección Local Coverage Areas (rompe regla local context)
- LBS con keyword stuffing de LCAs en cada párrafo
- LBS afirmando "Nuestra oficina en Almagro" (sin sede)
- LBS combinando 2 servicios en un H1 (rompe One Service)
```

**Regla final**

```text
S LBS redactadas como converters locales con LCAs naturales + areaServed.
```

**Validación operativa**

Cruce con Paso-05 5.5 + Paso-06 6.8 + Paso-09 9.6 (Local Coverage QA).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar Auxiliary Content Architecture × S × Main City con spec LBS.

**Output del paso**

- **Tipo:** S páginas redactadas.
- **Ejemplo (Cerrajeros Madrid 24h):** 5 LBS de 800-1,000 palabras cada una.

### 15.6 — Additional Category Page redactada

<small>§6.6</small>

**Explicación**

Las A=1 AC se redactan con spec Paso-05 5.6. Soportan categoría adicional GBP no cubierta por core service.

**Patrón o fórmula**

```text
Por cada additional category con needs_page=True (i = 1..A):
  Capa 1 Estructura: H1 + 11 bloques (Paso-06 6.9)
  Capa 2 Zonas: 10 LCAs (similar a LBS)
  Capa 3 Argumentos: tipos disponibles + precios + tiempos
  Capa 4 Entidades: tipos de servicio, marcas, normativa
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 15.6.

**Ejemplos incorrectos**

```text
- AC duplicando un core service (rompe Paso-02 2.12 anti-duplicación)
- AC sin contexto local (rompe regla 4)
- AC escrita como GA informacional (rompe rol comercial)
```

**Regla final**

```text
A Additional Category Pages redactadas como soporte de categoría GBP.
```

**Validación operativa**

Cruce con Paso-05 5.6 + Paso-06 6.9 + Paso-02 2.12.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar Auxiliary Content Architecture × A categorías efectivas.

**Output del paso**

- **Tipo:** A páginas redactadas.
- **Ejemplo (Cerrajeros Madrid 24h):** 1 AC duplicado-llaves de 880 palabras.

### 15.7 — GeoHub redactada

<small>§6.7</small>

**Explicación**

La GeoHub se redacta con spec Paso-05 5.7 (Main City Silo Container). Agrupa TODAS las señales de la Main City.

**Patrón o fórmula**

```text
Capa 1 Estructura: H1 + 10 bloques (Paso-06 6.10)
Capa 2 Zonas: 10 LCAs en sección dedicada visible
Capa 3 Argumentos: cobertura total Main City
Capa 4 Entidades: Main City + distritos + barrios + GBP categoría
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 15.7.

**Ejemplos incorrectos**

```text
- GeoHub con only generic city text (sin menús de servicios)
- GeoHub sin Local Coverage Areas Section
- GeoHub sin enlaces a las S LBS + A AC + G×S GAs
```

**Regla final**

```text
GeoHub redactada como Silo Container con menús completos de servicios + LCAs + GAs.
```

**Validación operativa**

Cruce con Paso-05 5.7 + Paso-06 6.10 + Paso-07 7.4 (GeoHub organiza Main City).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar Auxiliary Content Architecture con spec GeoHub.

**Output del paso**

- **Tipo:** 1 página redactada.
- **Ejemplo (Cerrajeros Madrid 24h):** 1 GeoHub de 980 palabras.

### 15.8 — GeoArticles redactados

<small>§6.8</small>

**Explicación**

Los G×S=15 GAs se redactan con spec Paso-05 5.8 (Semantic Booster). NO son landings comerciales — son boosters semánticos que apoyan a las LBS y al GeoHub.

**Patrón o fórmula**

```text
Por cada GA (i = 1..G×S):
  Capa 1 Estructura: H1 + 10 bloques (Paso-06 6.11)
  Capa 2 Zonas: LCAs como ejemplos contextuales (no listados)
  Capa 3 Argumentos: datos verificables (precios, tiempos, factores locales)
  Capa 4 Entidades: servicio + Main City + topic long-tail + escenarios
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 15.8 — 15 GAs distribuidos 3 por servicio core.

**Ejemplos incorrectos**

```text
- GA escrito como landing comercial (rompe rol semantic booster)
- GA con H1 idéntico a su LBS hijo (canibalización)
- GA sin parent LBS link (rompe Paso-08 8.11)
- GA con LCAs como listado vacío (rompe regla 4 contexto local)
```

**Regla final**

```text
G×S GeoArticles redactados como semantic boosters; cada uno con 3 enlaces a LBS parent.
```

**Validación operativa**

Cruce con Paso-05 5.8 + Paso-06 6.11 + Paso-08 8.11 + Paso-15 15.12.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar Auxiliary GeoArticles prompt (Paso-12 12.4) × G×S combinaciones.

**Output del paso**

- **Tipo:** G×S artículos redactados.
- **Ejemplo (Cerrajeros Madrid 24h):** 15 GAs de 1,000-1,500 palabras cada uno.

### 15.9 — Página de contacto redactada

<small>§6.9</small>

**Explicación**

Página auxiliar (NO SEO base). Sirve para conversiones directas y schema ContactPoint.

**Patrón o fórmula**

```text
Capa 1 Estructura: H1 + NAP + Form + Map + Hours + CTA
Capa 2-4: opcionales (página utilitaria)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 15.9.

**Ejemplos incorrectos**

```text
- Página de contacto sin formulario
- Página de contacto sin NAP completo
- Página de contacto sin schema ContactPoint
```

**Regla final**

```text
Página de contacto auxiliar siempre incluida; no cuenta como SEO base.
```

**Validación operativa**

Cruce con Paso-01 1.4 (NAP) + Paso-03 3.5 (URL Matrix incluye AUX).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Plantilla básica de contacto + NAP + form + schema.

**Output del paso**

- **Tipo:** 1 página auxiliar.
- **Ejemplo (Cerrajeros Madrid 24h):** /contacto/ de 320 palabras.

### 15.10 — Validación clusters completos por servicio

<small>§6.10</small>

**Explicación**

Cada servicio core debe tener su cluster mínimo: 1 SO + 1 LBS + 3 GeoArticles. Si falta cualquiera, cluster ROTO → no se publica el servicio.

**Patrón o fórmula**

```text
Para cada core service (i = 1..S):
  Cluster_i = SO_i + LBS_i + GA_i_1 + GA_i_2 + GA_i_3
  Si len(Cluster_i) < 5 → BLOCK cluster
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 15.10.

**Ejemplos incorrectos**

```text
- Publicar SO+LBS sin GAs (cluster roto)
- Publicar 2 GAs por servicio (rompe G=3)
- Publicar GAs sin LBS hijo (rompe Paso-08 8.11)
```

**Regla final**

```text
Cero clusters rotos. Si un servicio tiene cluster incompleto, no se publica el servicio entero.
```

**Validación operativa**

Aplicar a los S clusters core.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Validar count por cluster.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 5/5 clusters completos.

### 15.11 — Validación SO no compite con LBS

<small>§6.11</small>

**Explicación**

Los Service Overview son **pilares temáticos no-locales**. Las LBS son **converters locales**. Sus roles son distintos y sus H1 NO deben canibalizarse.

**Patrón o fórmula**

```text
SO H1: "Servicios profesionales de [Service] por [Brand]" (no menciona Main City)
LBS H1: "[Brand] – [Service] en [Main City]" (sí menciona Main City)
0 H1 duplicados o casi-duplicados
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

```text
SO-1: "Servicios profesionales de Cerrajero urgente por Cerrajeros Madrid 24h"
LBS-1: "Cerrajeros Madrid 24h – Cerrajero urgente en Madrid"
→ Distintos H1, distintos roles, 0 canibalización.
```

**Ejemplos incorrectos**

```text
- SO con H1 "Cerrajero urgente en Madrid" (canibaliza con LBS)
- LBS con H1 "Servicios profesionales de Cerrajero urgente" (canibaliza con SO)
```

**Regla final**

```text
SO ≠ LBS en H1, contenido y target. Cero canibalización entre roles.
```

**Validación operativa**

Cruce con Paso-09 9.12 (Canibalización QA).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Comparar H1 SO vs H1 LBS por servicio core.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 5 SO vs 5 LBS; 0 conflictos.

### 15.12 — Validación GeoArticle enlaza a LBS padre

<small>§6.12</small>

**Explicación**

Cada GA debe tener **3 puntos de enlace** a su LBS parent: inline en intro + H2 When to Call + CTA final. Sin enlaces a LBS, el GA queda huérfano comercialmente.

**Patrón o fórmula**

```text
Por cada GA:
  Punto 1: enlace inline en intro contextual (anchor variado)
  Punto 2: enlace en H2 "When to Call"
  Punto 3: CTA final "Lee la página de [Service] en [Main City]"
Total: 3 enlaces × G×S GAs
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

15 GAs × 3 puntos = 45 enlaces a LBS parent. 0 GAs sin enlace.

**Ejemplos incorrectos**

```text
- GA con 1 solo enlace a LBS (insuficiente)
- GA con 0 enlaces a LBS (huérfano)
- GA con 3 enlaces idénticos branded (rompe variedad anchors)
```

**Regla final**

```text
Cada GA enlaza 3 veces a su LBS parent con anchors variados.
```

**Validación operativa**

Cruce con Paso-07 7.7 + Paso-08 8.11.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar 3 puntos de enlace por GA.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 15 GAs × 3 = 45 enlaces validados.

### 15.13 — Validación datos verificables + sin reseñas inventadas

<small>§6.13</small>

**Explicación**

Regla web-first: **0 reseñas Google afirmadas** antes del Paso 14. Trust signals con datos verificables (no claims genéricos).

**Patrón o fórmula**

```text
Si GBP_STATUS = Not Created:
  - 0 menciones a "X reseñas en Google"
  - 0 review.aggregateRating en schema
  - Trust signals: solo datos verificables
  - Precios: "desde X€" (reales, no inventados)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 15.13.

**Ejemplos incorrectos**

```text
- "100+ reseñas en Google" cuando GBP no existe
- review.aggregateRating { ratingValue: 5 } sin reseñas reales
- "Los más rápidos de Madrid" (claim sin dato)
- "Precio desde 30€" (cuando precio real es 50€)
```

**Regla final**

```text
Datos verificables + 0 reseñas inventadas. Cumple web-first si GBP=Not Created.
```

**Validación operativa**

Cruce con Paso-09 9.8 (GBP Not Created QA Checklist) + Paso-01 1.3.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspeccionar copy + schema de las 28 URLs contra reglas web-first.

**Output del paso**

- **Tipo:** Validation flag.
- **Ejemplo (Cerrajeros Madrid 24h):** 28 URLs validadas; 0 reseñas inventadas; trust signals verificables.

## Checklist Final

<small>§7</small>

### Validación de framework

- ☐ Capas de redacción aplicadas en orden (15.1)
- ☐ Reglas de calidad universal cumplidas (15.2)

### Validación de páginas redactadas

- ☐ Homepage redactada (15.3)
- ☐ Service Overview Pages redactadas × S (15.4)
- ☐ Location-Based Service Pages redactadas × S (15.5)
- ☐ Additional Category Pages redactadas × A (15.6)
- ☐ GeoHub redactada (15.7)
- ☐ GeoArticles redactados × G×S (15.8)
- ☐ Página de contacto redactada (15.9)

### Validación de clusters y reglas

- ☐ Clusters completos por servicio (15.10)
- ☐ SO no compite con LBS (15.11)
- ☐ GeoArticle enlaza a LBS padre × 3 puntos (15.12)
- ☐ Datos verificables + sin reseñas inventadas (15.13)

## Outputs Consolidados

<small>§8</small>

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 15.1 | — | **Capas de redacción** = 4 capas (Estructura/Zonas/Argumentos/Entidades) aplicadas a 29 páginas | Aplicar las 4 capas en orden por página según page type. **Fuente:** GMB Crush. | confirmed |
| 15.2 | — | **Reglas de calidad universal** = 4 reglas (Hero+CTA / Problema / Datos / Local) aplicadas a 29 páginas | QA por página contra las 4 reglas. **Fuente:** GMB Crush. | confirmed |
| 15.3 | ← Paso-05 5.3 + Paso-06 6.6 + Paso-12 12.3 | **Homepage redactada** = 1 página de 1,050 palabras (rango 900-1,300 ✓) | Aplicar Auxiliary Content Architecture prompt a Homepage spec. **Fuente:** GMB Crush. | confirmed |
| 15.4 | ← Paso-05 5.4 + Paso-06 6.7 | **Service Overview Pages redactadas** = 5 SO de 850-1,000 palabras (no-localizadas) | Aplicar Auxiliary Content Architecture × S core services. **Fuente:** GMB Crush. | confirmed |
| 15.5 | ← Paso-05 5.5 + Paso-06 6.8 + Paso-01 1.10 | **Location-Based Service Pages redactadas** = 5 LBS de 800-1,000 palabras + 10 LCAs naturales | Aplicar Auxiliary Content Architecture × S × Main City. **Fuente:** GMB Crush. | confirmed |
| 15.6 | ← Paso-05 5.6 + Paso-06 6.9 | **Additional Category Page redactada** = 1 AC (duplicado-llaves) de 880 palabras | Aplicar Auxiliary Content Architecture × A categorías efectivas. **Fuente:** GMB Crush. | confirmed |
| 15.7 | ← Paso-05 5.7 + Paso-06 6.10 | **GeoHub redactada** = 1 página (/madrid/) de 980 palabras + 22 internal links | Aplicar Auxiliary Content Architecture con spec GeoHub. **Fuente:** GMB Crush. | confirmed |
| 15.8 | ← Paso-05 5.8 + Paso-06 6.11 + Paso-03 3.4 | **GeoArticles redactados** = 15 GAs de 1,000-1,500 palabras (3 por servicio × 5) | Aplicar Auxiliary GeoArticles prompt × G×S combinaciones. **Fuente:** GMB Crush. | confirmed |
| 15.9 | ← Paso-01 1.4 | **Página de contacto redactada** = /contacto/ de 320 palabras + form + ContactPoint schema | Plantilla básica de contacto + NAP + form + schema. **Fuente:** GMB Crush. | confirmed |
| 15.10 | ← Paso-01 1.9 + Paso-02 2.10 | **Validación clusters completos** = 5/5 clusters completos (SO + LBS + 3 GAs cada uno) | Validar count por cluster. **Fuente:** GMB Crush. | OK |
| 15.11 | ← Paso-05 5.4 + 5.5 | **Validación SO no compite con LBS** = 5 SO vs 5 LBS; 0 conflictos | Comparar H1 SO vs H1 LBS por servicio core. **Fuente:** GMB Crush. | OK |
| 15.12 | ← Paso-07 7.7 + Paso-08 8.11 | **Validación GA enlaza a LBS padre** = 15 GAs × 3 puntos = 45 enlaces validados | Inspeccionar 3 puntos de enlace por GA. **Fuente:** GMB Crush. | OK |
| 15.13 | ← Paso-01 1.3 + Paso-09 9.8 | **Validación datos verificables + sin reseñas inventadas** = 28 URLs Pass; 0 reseñas inventadas | Inspeccionar copy + schema vs reglas web-first. **Fuente:** GMB Crush. | OK |

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
- Content Writing Framework GMB Crush (4 capas + 4 reglas universales)

> **Nota — Redacción como capa que cierra el sistema:**
> El Paso 15 transforma la arquitectura abstracta de Bloques 1-4 en copy real publicable. Sin Paso 15, el sistema produce "qué debería ir" pero no "qué va a leer el usuario". El Paso 16 (Diseño/Layout) toma este copy y lo viste; el Paso 17 (Constructor) lo construye; el Paso 18 (QA+Deploy) lo publica.
