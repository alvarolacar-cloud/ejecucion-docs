Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 5 — Salida a Mercado/paso-19-acciones-futuro-escalado/`, alineado con los frameworks oficiales GMB Crush.

# Paso 19 — Acciones Futuro y Escalado

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 5 outputs del Paso 19 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush.

# Bloque I — Introducción

## Objetivo del Paso 19

<small>§2</small>

En este paso la IA establece el **protocolo de escalado post-launch** — cuándo y cómo crear páginas de barrio (Approved Expansion Areas) tras lanzar la web base. Define vigilancia con **3 métricas** clave, validación con **3 triggers** (necesarios al menos 2 para escalar), y análisis SERP real para evitar páginas débiles sin tracción. Establece protocolo con criterio operativo, no decisiones impulsivas.

**Outputs del paso:**

- **19.1** Tablero de vigilancia post-launch — 3 métricas baseline (CTR / Posición / Volumen)
- **19.2** Estado de los 3 triggers por candidato a página de barrio
- **19.3** Análisis SERP ejecutado + decisión (crear / no crear)
- **19.4** Log de decisiones de escalado con fechas + justificación + confianza
- **19.5** URL Matrix actualizada con Approved Expansion Areas (si aplica)

**Errores que previene:**

- Crear páginas de barrio impulsivamente sin datos
- Escalar a zonas sin tracción (páginas débiles que diluyen autoridad)
- Sin protocolo escrito (decisiones inconsistentes entre operadores)
- Sin trazabilidad de por qué se aprobó/rechazó una zona
- Modificar URL Matrix sin documentar cambio (rompe Paso-13 13.7)

**Cuándo se ejecuta:** después de Paso 18 (QA + Deploy) cerrado y con datos GSC mínimos (≥ 30 días post-launch). Marca el inicio de la fase post-launch del cluster. Aplica indefinidamente hasta que el cluster se descontinúe.

## Info heredada de pasos anteriores

<small>§3</small>

| Campo | Origen |
|---|---|
| Approved Expansion Areas (default vacío Phase 1) | Paso-01 1.11 |
| URL Matrix completa | Paso-03 3.5 |
| Approved Expansion URLs (E=0 default) | Paso-04 4.10 |
| Expansion linking separado | Paso-07 7.15 |
| Función generate_expansion() | Paso-11 11.11 |
| Documentación de Cambios template | Paso-13 13.7 |
| Tracking Plan (GSC + GA4 + Rank Tracker) | Paso-13 13.8 |
| Sitio publicado | Paso-18 18.6 |
| Sitemap en GSC con datos | Paso-18 18.7 |

# Bloque II — Ejemplo rellenado para el Paso 19 — Escalado

<small>§4</small>

> Los 5 outputs del Paso 19 con sus valores reales para Cerrajeros Madrid 24h tras 6 meses post-launch.

### 19.1 — Tablero de vigilancia post-launch

```text
3 métricas baseline (revisión semanal/mensual):

Métrica 1 — CTR por LCA en GSC:
  Para cada LCA declarada (10 LCAs en Cerrajeros), filtrar queries en GSC
  que mencionen el barrio (ej. "cerrajero almagro", "cerrajero chamberí").
  Baseline: ¿hay queries con impresiones?

  Cerrajeros 6 meses post-launch:
    Almagro:    243 impresiones / 18 clicks (CTR 7.4%) / pos. media 8
    Chamberí:   189 / 14 / 7.4% / pos. 9
    Salamanca:  412 / 15 / 3.6% / pos. 14   ← señal: pos. baja, hay volumen
    Retiro:     156 / 8 / 5.1% / pos. 11
    Tetuán:     78 / 3 / 3.8% / pos. 18
    Centro:     67 / 4 / 5.9% / pos. 12
    Chamartín:  124 / 6 / 4.8% / pos. 13
    Arganzuela: 45 / 2 / 4.4% / pos. 17
    Moncloa:    52 / 3 / 5.7% / pos. 14
    Prosperidad: 23 / 1 / 4.3% / pos. 21

Métrica 2 — Posición media por servicio + Main City (Rank Tracker):
  Cerrajero urgente Madrid:           pos. 4 (P1)
  Apertura puertas Madrid:            pos. 6 (P2)
  Cambio cerraduras Madrid:           pos. 8 (P2)
  Cambio bombines Madrid:             pos. 11 (P3)
  Instalación seguridad Madrid:       pos. 9 (P2)
  GeoArticles principales:            pos. 5-12 (P1-P3)

Métrica 3 — Conversiones por page type (GA4):
  HP:               34 conversiones (call/form)
  LBS-1 (urgente):  189 conversiones
  LBS-2 (apertura): 87 conversiones
  LBS-3 (cerradur): 56
  LBS-4 (bombines): 42
  LBS-5 (segurid):  31
  AC (duplicado):   12
  GH (madrid):      28
  GAs (15):         123 total (8.2 promedio por GA)
```

### 19.2 — Estado de los 3 triggers por candidato a página de barrio

```text
3 Triggers para crear página de barrio (necesarios al menos 2/3):

Trigger 1 — Volumen de búsqueda mensual:
  El barrio tiene ≥ 100 impresiones/mes en GSC para queries relacionadas.

Trigger 2 — Posición media:
  La LBS Madrid posiciona en la franja 8-15 para queries del barrio
  (ni dominante, ni inexistente — hay margen para mejorar con página dedicada).

Trigger 3 — Concurrencia local:
  En SERP "cerrajero [barrio]" hay ≤ 3 LBS dedicadas + el resto directorios
  (Competition Gap ≥ 4 en Paso-08 8.6).

Cerrajeros 6 meses post-launch — Estado por candidato:

Salamanca:
  Trigger 1: ✓ (412 impresiones/mes)
  Trigger 2: ✗ (pos. 14, fuera de franja 8-15) — línea
  Trigger 3: por validar (pendiente análisis SERP en 19.3)
  → 1/3 confirmado, 2/3 pendiente; análisis SERP necesario

Almagro:
  Trigger 1: ✗ (243 imp/mes pero ya CTR 7.4% sin URL — alta relevancia residual)
  Trigger 2: ✓ (pos. 8)
  Trigger 3: por validar
  → 1/3 confirmado, 2/3 pendiente; análisis SERP necesario

Chamberí:
  Trigger 1: ✗ (189 imp/mes; bajo umbral 100 pero ojo)
  Trigger 2: ✓ (pos. 9)
  Trigger 3: por validar
  → 1-2/3 confirmados; análisis SERP marginal

Otros 7 LCAs: ninguno cumple Trigger 1 (volúmenes < 100/mes); descartados por ahora.
```

### 19.3 — Análisis SERP ejecutado + decisión

```text
Análisis SERP manual + Ahrefs para los 3 candidatos shortlisted:

Salamanca:
  Query: "cerrajero salamanca madrid"
  Top 10:
    1. Directorio cerrajeros (DR 45)
    2. Lockerit (DR 32)
    3. Cerrajeros Salamanca Madrid (DR 28, LBS dedicada — competidor)
    4-5. Mapas + Local Pack
    6. Yelp / TrustPilot (genéricos)
    7-9. Páginas LBS Madrid genéricas (no dedicadas a Salamanca)
    10. Cerrajeros Madrid 24h (nosotros, posición 14 sin URL Salamanca)

  Análisis:
    - 1 LBS dedicada (Cerrajeros Salamanca Madrid)
    - 4 directorios débiles
    - Competition Gap: 4 (favorable)
    - Volumen: 412 impresiones/mes
    - Si creamos /cerrajero/madrid/salamanca/cerrajero-urgente/ → margen
      para entrar en top 5 con contenido específico

  Decisión: ✓ APROBAR escalado a Salamanca
    Confianza: alta (Trigger 1 ✓, Trigger 3 ✓; Trigger 2 marginal)

Almagro:
  Análisis: directorio dominante; LBS dedicada de competidor en pos 2.
  Competition Gap: 3 (saturado).
  Decisión: ✗ NO escalar (pos. 8 actual sin URL es buena; mejor dejar)
    Confianza: alta (Trigger 3 ✗)

Chamberí:
  Análisis: SERP dominado por nuestra propia LBS Madrid + directorios;
  poco margen sin URL dedicada; volumen marginal.
  Decisión: ⏳ POSPONER 3 meses (re-evaluar volumen)
    Confianza: media
```

### 19.4 — Log de decisiones de escalado

```text
═══════════════════════════════════════════════
LOG DE ESCALADO — Cerrajeros Madrid 24h
═══════════════════════════════════════════════

#001 — 2026-10-30 (6 meses post-launch)
Candidato:    Salamanca
Triggers:     1 ✓ / 2 ⚠ / 3 ✓ (2/3 confirmados)
SERP analysis: ✓ Competition Gap = 4
Decisión:     APROBAR escalado
Justificación: Volumen mensual > 400 imp; SERP no saturado;
              margen para top 5 con URL dedicada.
Confianza:    Alta
Aprobado por: Operador
Próxima rev.: 2027-04-30 (medir impacto post-creación)

#002 — 2026-10-30
Candidato:    Almagro
Decisión:     NO escalar
Justificación: Pos. 8 sin URL ya es buena; SERP saturado;
              riesgo de canibalizar nuestra propia LBS Madrid.
Confianza:    Alta

#003 — 2026-10-30
Candidato:    Chamberí
Decisión:     POSPONER 3 meses
Justificación: Volumen marginal (189 imp/mes); SERP dominado por
              nuestra propia LBS Madrid; re-evaluar 2027-01-30.
Confianza:    Media
Próxima rev.: 2027-01-30
```

### 19.5 — URL Matrix actualizada con Approved Expansion Areas

```text
Tras decisión #001 — escalar a Salamanca:

Approved Expansion Areas (Paso-01 1.11) actualizada:
  Antes: []
  Ahora: ["Salamanca"]

Nuevas URLs generadas (aplicando Paso-11 11.11 generate_expansion()):
  EXP-GH-Salamanca:    /salamanca/                                    (1 GeoHub)
  EXP-LBS-1:           /cerrajero/salamanca/cerrajero-urgente/       (1 LBS)
  EXP-LBS-2:           /cerrajero/salamanca/apertura-puertas/         (1 LBS)
  EXP-LBS-3:           /cerrajero/salamanca/cambio-cerraduras/        (1 LBS)
  EXP-LBS-4:           /cerrajero/salamanca/cambio-bombines/          (1 LBS)
  EXP-LBS-5:           /cerrajero/salamanca/instalacion-cerraduras-seguridad/ (1 LBS)
  EXP-GA-1..15:        /salamanca/{topic}/                           (15 GAs)

Total expansión: 1 GH + 5 LBS + 15 GAs = 21 URLs nuevas (sub-cluster Salamanca)

URL Matrix global:
  Antes: 28 base + 1 aux = 29 URLs
  Ahora: 28 base + 21 expansion + 1 aux = 50 URLs

Documentación de Cambios (Paso-13 13.7) — entrada #001:
  Tipo: Expansion
  Descripción: Añadir Approved Expansion Area Salamanca → 21 URLs nuevas
  Outputs afectados: 1.11, 4.10, 7.15, 11.11, 19.4
  Validado QA: 2026-11-15 (tras construcción del sub-cluster)
```

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 19.1 | Tablero de vigilancia post-launch | 3 métricas baseline | GMB Crush + Datos de búsqueda | Paso-13 13.8 + Paso-18 18.7 |
| 19.2 | Estado de los 3 triggers por candidato | Diagnóstico por LCA | GMB Crush + Datos de búsqueda | Paso-19 19.1 (intra-paso) |
| 19.3 | Análisis SERP + decisión | SERP analysis + decisión documentada | GMB Crush + Competidores | Paso-19 19.2 + Paso-08 8.6 |
| 19.4 | Log de decisiones de escalado | Documento histórico de decisiones | GMB Crush | Paso-19 19.3 + Paso-13 13.7 |
| 19.5 | URL Matrix actualizada con Approved Expansion | URL Matrix v2 con expansion | GMB Crush | Paso-19 19.4 + Paso-01 1.11 + Paso-11 11.11 |

## Obtención de Outputs

<small>§6</small>

### 19.1 — Tablero de vigilancia post-launch

<small>§6.1</small>

**Explicación**

Tablero de 3 métricas que se monitoriza post-launch para detectar oportunidades de escalado a páginas de barrio.

**Patrón o fórmula**

```text
Métrica 1: CTR por LCA en GSC (queries con barrio mencionado)
Métrica 2: Posición media por servicio + Main City (Rank Tracker)
Métrica 3: Conversiones por page type (GA4)

Cadencia: semanal Phase 1-3, mensual Phase 4+ (post-launch).
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 19.1 — datos a 6 meses post-launch.

**Ejemplos incorrectos**

```text
- Vigilancia ad-hoc sin métricas declaradas
- Solo medir conversiones (sin CTR ni posiciones)
- Saltar GSC (sin discovery de queries por barrio)
```

**Regla final**

```text
3 métricas baseline establecidas en cadencia regular post-launch.
```

**Validación operativa**

Cruce con Paso-13 13.8 (Tracking Plan).

**Cómo se obtiene**

- **Fuente:** GMB Crush + Datos de búsqueda.
- **Método:** Configurar dashboards en GSC + GA4 + Rank Tracker; revisar regularmente.

**Output del paso**

- **Tipo:** Tablero con datos.
- **Ejemplo (Cerrajeros Madrid 24h):** 3 métricas con datos de 6 meses post-launch.

### 19.2 — Estado de los 3 triggers por candidato

<small>§6.2</small>

**Explicación**

Para cada LCA candidata a Approved Expansion, evaluar 3 triggers. Necesarios al menos 2/3 para considerar escalado.

**Patrón o fórmula**

```text
Trigger 1 — Volumen: ≥ 100 impresiones/mes en GSC
Trigger 2 — Posición: pos. media en franja 8-15 (margen para mejorar)
Trigger 3 — Concurrencia: SERP no saturado (Competition Gap ≥ 4)

Decisión:
  3/3 → escalar con alta confianza
  2/3 → escalar con confianza media-alta
  1/3 → NO escalar (datos insuficientes)
  0/3 → descartar
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 19.2 — Salamanca 1/3+análisis pendiente; Almagro 1/3; Chamberí 1-2/3 marginal.

**Ejemplos incorrectos**

```text
- Escalar con 0-1/3 triggers (decisión impulsiva)
- Saltar evaluación de triggers (todo se aprueba)
- Cambiar criterios de triggers ad-hoc (rompe disciplina)
```

**Regla final**

```text
3 triggers fijos. Mínimo 2/3 confirmados para considerar escalado (+ análisis SERP final).
```

**Validación operativa**

Aplicar a cada LCA con datos suficientes en 19.1.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Datos de búsqueda.
- **Método:** Cruzar Tablero (19.1) con criterios de 3 triggers.

**Output del paso**

- **Tipo:** Diagnóstico por LCA.
- **Ejemplo (Cerrajeros Madrid 24h):** 3 candidatos shortlisted (Salamanca, Almagro, Chamberí); resto descartados.

### 19.3 — Análisis SERP + decisión

<small>§6.3</small>

**Explicación**

Para cada candidato con ≥ 2/3 triggers confirmados, ejecutar análisis SERP manual + Ahrefs para validar concurrencia real. Decisión final: APROBAR / NO ESCALAR / POSPONER.

**Patrón o fórmula**

```text
1. Buscar "cerrajero [barrio]" en Google (sin login)
2. Analizar top 10 orgánico:
   - Cuántas LBS dedicadas vs directorios
   - DR/UR de competidores (Ahrefs)
   - Mapas + Local Pack visibles
3. Calcular Competition Gap (Paso-08 8.6)
4. Decidir: APROBAR / NO ESCALAR / POSPONER
5. Documentar confianza: alta / media / baja
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 19.3 — Salamanca APROBAR; Almagro NO; Chamberí POSPONER.

**Ejemplos incorrectos**

```text
- Decisión sin análisis SERP real (intuición)
- Aprobar zona con SERP saturado (página débil)
- Sin documentación de confianza (post-mortem imposible)
```

**Regla final**

```text
Decisión final exige análisis SERP real + Competition Gap calculado.
```

**Validación operativa**

Cruce con Paso-08 8.6 (Competition Gap).

**Cómo se obtiene**

- **Fuente:** GMB Crush + Competidores.
- **Método:** SERP analysis manual + Ahrefs para fortaleza top 10.

**Output del paso**

- **Tipo:** SERP analysis + decisión.
- **Ejemplo (Cerrajeros Madrid 24h):** 3 candidatos analizados; 1 aprobado, 1 rechazado, 1 pospuesto.

### 19.4 — Log de decisiones de escalado

<small>§6.4</small>

**Explicación**

Documento histórico de TODAS las decisiones de escalado (aprobadas, rechazadas, pospuestas). Garantiza trazabilidad de por qué cada zona se escaló o no, y cuándo re-evaluar.

**Patrón o fórmula**

```text
Por cada decisión:
  Fecha + Candidato + Triggers + SERP + Decisión + Justificación +
  Confianza + Aprobado por + Próxima revisión (si aplica)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 19.4 — 3 entradas de log con todos los campos.

**Ejemplos incorrectos**

```text
- Log sin Justificación (decisiones opacas)
- Log sin Confianza (post-mortem sin contexto)
- Log sin Próxima revisión para POSPONER (zonas pospuestas indefinidamente)
```

**Regla final**

```text
Cada decisión = 1 entrada con 8 campos obligatorios.
```

**Validación operativa**

Cruce con Paso-13 13.7 (Documentación de Cambios template).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Plantilla con 8 campos por decisión + actualización post-evaluación.

**Output del paso**

- **Tipo:** Documento histórico.
- **Ejemplo (Cerrajeros Madrid 24h):** 3 entradas en log a 6 meses post-launch.

### 19.5 — URL Matrix actualizada con Approved Expansion Areas

<small>§6.5</small>

**Explicación**

Tras una decisión APROBAR (19.4), actualizar URL Matrix con sub-cluster de la Approved Expansion Area. Aplica `generate_expansion()` del Paso-11 11.11.

**Patrón o fórmula**

```text
1. Approved Expansion Areas (Paso-01 1.11) ← añadir nueva area
2. generate_expansion() (Paso-11 11.11) genera:
   - 1 GeoHub por area
   - S LBS por area
   - G×S GAs por area
3. URL Matrix actualizada con sub-cluster
4. Documentación de Cambios (Paso-13 13.7) — entrada de cambio
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 19.5 — Salamanca añadida; +21 URLs (1 GH + 5 LBS + 15 GAs).

**Ejemplos incorrectos**

```text
- Modificar URL Matrix sin Documentación de Cambios
- Saltar generate_expansion() (URLs ad-hoc)
- Mezclar URLs base con expansion (rompe Paso-07 7.15)
```

**Regla final**

```text
URL Matrix v2 = URL Matrix v1 + sub-cluster Approved Expansion (separado).
```

**Validación operativa**

Cruce con Paso-01 1.11 + Paso-04 4.10 + Paso-07 7.15 + Paso-11 11.11.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar generate_expansion() + actualizar URL Matrix + documentar cambio.

**Output del paso**

- **Tipo:** URL Matrix v2.
- **Ejemplo (Cerrajeros Madrid 24h):** URL Matrix v2 con 50 URLs (28 base + 21 expansion + 1 aux).

## Checklist Final

<small>§7</small>

- ☐ Tablero de vigilancia con 3 métricas configurado (19.1)
- ☐ Estado de 3 triggers evaluado por candidato (19.2)
- ☐ Análisis SERP ejecutado para shortlist (19.3)
- ☐ Log de decisiones documentado con 8 campos por entrada (19.4)
- ☐ URL Matrix actualizada con sub-cluster Approved Expansion si aplica (19.5)
- ☐ Documentación de Cambios entrada registrada (cruce Paso-13 13.7)

## Outputs Consolidados

<small>§8</small>

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 19.1 | ← Paso-13 13.8 + Paso-18 18.7 | **Tablero de vigilancia** = 3 métricas (CTR LCAs / Posición servicios / Conversiones) con datos 6 meses post-launch | Configurar dashboards GSC + GA4 + Rank Tracker; revisar regularmente. **Fuente:** GMB Crush + Datos de búsqueda. | confirmed |
| 19.2 | ← 19.1 | **Estado de los 3 triggers** = 3 candidatos shortlisted (Salamanca / Almagro / Chamberí); 7 descartados | Cruzar Tablero con criterios de 3 triggers (volumen / posición / concurrencia). **Fuente:** GMB Crush + Datos de búsqueda. | confirmed |
| 19.3 | ← 19.2 + Paso-08 8.6 | **Análisis SERP + decisión** = 1 APROBAR (Salamanca) + 1 NO (Almagro) + 1 POSPONER (Chamberí) | SERP analysis manual + Ahrefs para fortaleza top 10. **Fuente:** GMB Crush + Competidores. | confirmed |
| 19.4 | ← 19.3 + Paso-13 13.7 | **Log de decisiones** = 3 entradas con 8 campos obligatorios cada una | Plantilla con 8 campos por decisión + actualización post-evaluación. **Fuente:** GMB Crush. | confirmed |
| 19.5 | ← 19.4 + Paso-01 1.11 + Paso-11 11.11 | **URL Matrix actualizada** = v2 con 50 URLs (28 base + 21 sub-cluster Salamanca + 1 aux) | Aplicar generate_expansion() + actualizar URL Matrix + documentar cambio. **Fuente:** GMB Crush. | confirmed |

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
- Post-Launch Scaling Framework GMB Crush (3 métricas + 3 triggers + SERP analysis)

> **Nota — Escalado con disciplina, no impulso:**
> El Paso 19 establece un protocolo objetivo para decidir cuándo escalar a páginas de barrio. Sin protocolo, las decisiones son impulsivas y producen páginas débiles que diluyen la autoridad del cluster. Con protocolo, cada zona aprobada tiene base de datos sólida + análisis SERP + log de justificación. El operador NO crea páginas de barrio sin ejecutar 19.1 → 19.4.
