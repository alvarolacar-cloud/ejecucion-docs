Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 5 — Salida a Mercado/paso-19-acciones-futuro-escalado/`, alineado con los frameworks oficiales GMB Crush. Triggers, métricas y protocolo SERP portados LITERALMENTE del documento fuente original.

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

En este paso la IA establece el **protocolo de escalado post-launch** — cuándo y cómo crear páginas de barrio (Approved Expansion Areas) tras lanzar la web base. Establece **vigilancia de los 3 elementos críticos** (Flujo GeoArticle→Location / Autoridad GeoHub / Conversión LBS core), validación con **3 triggers** (Location ya responde / GeoArticles traen tráfico / Señal en SERP) bajo regla 2-de-3, y **protocolo de análisis SERP** con doble búsqueda (servicio+ciudad vs servicio+barrio) para decidir CREAR / NO CREAR basado en el comportamiento real de Google.

**Outputs del paso:**

- **19.1** Tablero de vigilancia post-launch — 3 elementos críticos con métricas + acciones correctivas
- **19.2** Estado de los 3 triggers por candidato a página de barrio (regla 2-de-3)
- **19.3** Análisis SERP ejecutado + decisión CREAR/NO CREAR (protocolo doble búsqueda)
- **19.4** Log de decisiones de escalado con fechas, justificación, confianza
- **19.5** URL Matrix actualizada con Approved Expansion Areas (si aplica)

**Errores que previene:**

- Crear páginas de barrio sin baseline de los 3 elementos
- Escalar basado en volumen estimado de keyword research (volumen ≠ prioridad)
- Escalar basado en número de competidores (cantidad ≠ oportunidad)
- Saltar el protocolo SERP (decisión por intuición)
- Modificar URL Matrix sin documentar cambio (rompe Paso-13 13.7)
- Tratar fallos de métricas como señal de "más páginas" (deben corregirse, no escalarse)

**Cuándo se ejecuta:** después de Paso 18 (QA + Deploy) cerrado y con baseline de las 3 métricas establecido a las 4 semanas post-launch. Aplica indefinidamente hasta que el cluster se descontinúe.

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
| Puentes narrativos GA → LBS | Paso-15 15.8 + 15.12 |
| Sitio publicado | Paso-18 18.6 |
| Sitemap en GSC con datos | Paso-18 18.7 |

# Bloque II — Ejemplo rellenado para el Paso 19 — Escalado

<small>§4</small>

> Los 5 outputs del Paso 19 con sus valores reales para Cerrajeros Madrid 24h.

### 19.1 — Tablero de vigilancia post-launch

```text
3 elementos críticos a vigilar (cadencia: baseline 4 semanas, revisión mensual durante 6 meses):

═══════════════════════════════════════════════════════════════════
ELEMENTO 1 — Flujo GeoArticle → Location
═══════════════════════════════════════════════════════════════════
Mide si los puentes narrativos (Paso-15 15.8 + 15.12) llevan al usuario
del GeoArticle (captación informacional) a la LBS (conversión local).

Métrica 1.1: % usuarios que hacen click en los puentes narrativos
  Cómo medir: GA4 eventos de click en enlaces internos desde GAs a LBS
  Acción correctiva si falla: ajustar copy de puentes o posición de botones

Métrica 1.2: Páginas/sesión cuando entrada es GeoArticle
  Cómo medir: GA4 páginas por sesión filtrando entrada por GA
  Acción correctiva si falla: si <2 páginas/sesión, los puentes no convierten
                              → revisar redacción

═══════════════════════════════════════════════════════════════════
ELEMENTO 2 — Autoridad del GeoHub
═══════════════════════════════════════════════════════════════════
Mide si `/madrid/` rankea para búsquedas informativas amplias y cumple
su rol de Main City Silo Container.

Métrica 2.1: Impresiones de /madrid/ en GSC
  Cómo medir: GSC filtrando por URL exacta /madrid/
  Acción correctiva si falla: ampliar contenido contextual (Paso-15 15.7)
                              o añadir datos estadísticos verificables

Métrica 2.2: Posiciones para búsquedas amplias
  Cómo medir: GSC queries informativas tipo "cerrajeros madrid"
  Acción correctiva si falla: si posición >20 tras 3 meses,
                              revisar contenido y enlaces internos

═══════════════════════════════════════════════════════════════════
ELEMENTO 3 — Conversión del Servicio Core
═══════════════════════════════════════════════════════════════════
Mide si la LBS del servicio core (la página principal de conversión)
está convirtiendo.

Métrica 3.1: Tasa de conversión de la LBS core
  Cómo medir: GA4 eventos de envío de formulario o click en tel:
              desde la LBS Cerrajero urgente Madrid
  Acción correctiva si falla: mejorar copy (Paso-15 15.5),
                              añadir calculadora o prueba social

Métrica 3.2: CTR del CTA "Llamar ahora"
  Cómo medir: GA4 eventos de click en CTA principal
  Acción correctiva si falla: si <5%, revisar Hero (Paso-15 15.5 +
                              Paso-16 16.5 reglas Hero)

═══════════════════════════════════════════════════════════════════
Regla operativa: cada métrica que falle desencadena una acción correctiva,
                  NO la creación de páginas nuevas.
═══════════════════════════════════════════════════════════════════
```

### 19.2 — Estado de los 3 triggers por candidato a página de barrio

```text
Los 3 triggers se evalúan por candidato (LCA con potencial de Approved Expansion).
Regla 2-de-3: se pueden crear páginas de barrio cuando se cumplen al menos 2 de los 3.

═══════════════════════════════════════════════════════════════════
TRIGGER 1 — Location ya responde
═══════════════════════════════════════════════════════════════════
La LBS principal (`/cerrajero/madrid/cerrajero-urgente/`) ya tiene tracción.

Indicadores concretos (todos para considerar Trigger ✓):
- Impresiones >100/mes en GSC
- Clicks reales >10/mes
- Al menos 1 keyword en posición <30

═══════════════════════════════════════════════════════════════════
TRIGGER 2 — GeoArticles traen tráfico
═══════════════════════════════════════════════════════════════════
Al menos 1-2 GAs tienen impresiones, tráfico y posicionamiento inicial.

Indicadores concretos (todos para considerar Trigger ✓):
- Al menos 1 GeoArticle con impresiones >50/mes en GSC
- Al menos 1 GeoArticle con clicks >5/mes
- Posición media <40 para alguna keyword del artículo

═══════════════════════════════════════════════════════════════════
TRIGGER 3 — Señal en SERP
═══════════════════════════════════════════════════════════════════
La SERP cambia claramente al añadir el barrio y aparecen 3+ páginas
específicas del barrio (patrón confirmado).

Indicadores concretos (todos para considerar Trigger ✓):
- Al ejecutar el protocolo de §6.3 (doble búsqueda), la SERP del barrio
  difiere claramente de la SERP de ciudad
- Aparecen 3+ resultados optimizados específicamente para el barrio
  (no solo Local Pack)
- Google mantiene la intención al añadir el barrio (no agrupa a nivel ciudad)

═══════════════════════════════════════════════════════════════════
Regla 2-de-3:
  3/3 triggers cumplidos = se puede crear (alta confianza)
  2/3 triggers cumplidos = se puede crear
  1/3 trigger cumplido   = NO escalar; esperar y reevaluar en 4-8 semanas
  0/3 triggers cumplidos = descartar
═══════════════════════════════════════════════════════════════════

Cerrajeros Madrid 24h — Estado a [fecha post-launch]:
Candidato: Almagro
- Trigger 1 (Location ya responde):  pendiente — la LBS necesita 4-8 semanas
- Trigger 2 (GeoArticles traen tráfico): pendiente — los GAs necesitan tiempo
- Trigger 3 (SERP cambia con barrio): pendiente — ejecutar §6.3 cuando 1+2 activos

Resultado: NO CREAR páginas de barrio en Almagro hasta que se cumplan ≥2 triggers.

(Para cualquier otro candidato — Chamberí, Salamanca, etc. — repetir evaluación.)
```

### 19.3 — Análisis SERP + decisión

```text
Protocolo objetivo para decidir CREAR / NO CREAR basado en comportamiento real
de Google. Solo se ejecuta si Triggers 1 y 2 (§6.2) ya están cumplidos.

═══════════════════════════════════════════════════════════════════
INPUT
═══════════════════════════════════════════════════════════════════
Servicio: [SERVICIO]
Ciudad:   [CIUDAD]
Barrio:   [BARRIO]

═══════════════════════════════════════════════════════════════════
INSTRUCCIONES DE EJECUCIÓN
═══════════════════════════════════════════════════════════════════
1. Ejecutar dos búsquedas en Google:
   a) "{servicio} {ciudad}"
   b) "{servicio} {barrio}"

2. Analizar SOLO resultados orgánicos (ignorar Local Pack y Ads).

3. Comparar las dos SERPs respondiendo:
   a) ¿Los resultados orgánicos son los mismos o muy similares?
   b) ¿Aparecen 3+ páginas optimizadas específicamente para el barrio?
   c) ¿Existen múltiples URLs diferentes orientadas al barrio?
   d) ¿Google mantiene la intención a nivel ciudad aunque se añada el barrio?

4. Clasificar en uno de 2 escenarios:

   ESCENARIO A — SIN segmentación:
     La SERP del barrio es igual o muy similar a la SERP de ciudad.
     Google agrupa la intención a nivel ciudad.
     → NO CREAR página de barrio.

   ESCENARIO B — CON segmentación:
     La SERP cambia claramente. Aparecen 3+ páginas específicas del barrio.
     → CREAR página de barrio (si además se cumplen Triggers 1 y 2 del §6.2).

═══════════════════════════════════════════════════════════════════
OUTPUT OBLIGATORIO
═══════════════════════════════════════════════════════════════════
Resultado: [CREAR / NO CREAR]

Justificación (3-5 líneas):
- Si la SERP cambia o no.
- Si hay patrón de páginas específicas del barrio.
- Qué indica Google sobre la intención (ciudad vs barrio).

Nivel de confianza: [Alto / Medio / Bajo]

═══════════════════════════════════════════════════════════════════
REGLAS DEL PROTOCOLO
═══════════════════════════════════════════════════════════════════
- NO decidir en base al número de competidores
  → la cantidad no es señal de oportunidad.
- NO decidir en base al volumen estimado de búsqueda
  → el volumen indica oportunidad, no prioridad.
- SOLO decidir en base al comportamiento real de la SERP
  → Google es el árbitro final.
- Repetir el análisis al menos en 2 ubicaciones físicas distintas
  (con VPN o desde dispositivos en zonas distintas) para evitar
  sesgos de personalización.

═══════════════════════════════════════════════════════════════════
Cerrajeros Madrid 24h — Análisis SERP a [fecha]:

Candidato: Almagro
Búsqueda a) "cerrajero madrid": [resultados orgánicos top 10]
Búsqueda b) "cerrajero almagro": [resultados orgánicos top 10]

Comparación:
  ¿SERPs similares? [pendiente: ejecutar cuando Trigger 1 + 2 activos]
  ¿3+ resultados específicos barrio? [pendiente]
  ¿Múltiples URLs orientadas? [pendiente]
  ¿Google mantiene intención ciudad? [pendiente]

Resultado: [pendiente — esperar tracción de la LBS Madrid]
Confianza: [pendiente]
```

### 19.4 — Log de decisiones de escalado

```text
═══════════════════════════════════════════════
LOG DE ESCALADO — Cerrajeros Madrid 24h
═══════════════════════════════════════════════

#001 — [fecha post-launch ≥ 4 semanas]
Candidato:    Almagro
Triggers:     1 [estado] / 2 [estado] / 3 [estado]
SERP analysis: [pendiente / Escenario A / Escenario B]
Decisión:     [CREAR / NO CREAR / POSPONER]
Justificación (3-5 líneas):
  - Si la SERP cambia o no.
  - Si hay patrón de páginas específicas del barrio.
  - Qué indica Google sobre la intención (ciudad vs barrio).
Confianza:    [Alto / Medio / Bajo]
Aprobado por: Operador
Próxima rev.: [+4-8 semanas si POSPONER]

#002 — ...
```

### 19.5 — URL Matrix actualizada con Approved Expansion Areas

```text
Solo se ejecuta tras decisión CREAR (19.4).

Tras decisión CREAR para [Barrio]:

Approved Expansion Areas (Paso-01 1.11) actualizada:
  Antes: []
  Ahora: ["[Barrio]"]

Nuevas URLs generadas (aplicando Paso-11 11.11 generate_expansion()):
  EXP-GH-[Barrio]:    /[barrio-slug]/                                (1 GeoHub)
  EXP-LBS-1:           /cerrajero/[barrio-slug]/cerrajero-urgente/    (1 LBS)
  EXP-LBS-2..5:       /cerrajero/[barrio-slug]/{service-slug}/       (S-1 LBS)
  EXP-GA-1..15:       /[barrio-slug]/{topic}/                         (G×S GAs)

Total expansión: 1 GH + S LBS + G×S GAs URLs nuevas (sub-cluster Barrio)

URL Matrix global v2:
  Antes: 28 base + 1 aux = 29 URLs
  Después: 28 base + (1+S+G×S) expansion + 1 aux URLs

Documentación de Cambios (Paso-13 13.7) — entrada:
  Tipo: Expansion
  Descripción: Añadir Approved Expansion Area [Barrio] → 1+S+G×S URLs nuevas
  Outputs afectados: 1.11, 4.10, 7.15, 11.11, 19.4
  Validado QA: [fecha — tras construcción del sub-cluster]
```

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 19.1 | Tablero de vigilancia post-launch | 3 elementos × 2 métricas con acciones correctivas | GMB Crush + Datos de búsqueda | Paso-13 13.8 + Paso-15 15.5 + 15.7 + 15.8 + Paso-18 18.7 |
| 19.2 | Estado de los 3 triggers por candidato | Diagnóstico por LCA con regla 2-de-3 | GMB Crush + Datos de búsqueda | Paso-19 19.1 (intra-paso) |
| 19.3 | Análisis SERP + decisión | Protocolo doble búsqueda + 2 escenarios | GMB Crush + Competidores | Paso-19 19.2 (intra-paso) |
| 19.4 | Log de decisiones de escalado | Documento histórico de decisiones | GMB Crush | Paso-19 19.3 + Paso-13 13.7 |
| 19.5 | URL Matrix actualizada con Approved Expansion | URL Matrix v2 con sub-cluster | GMB Crush | Paso-19 19.4 + Paso-01 1.11 + Paso-11 11.11 |

## Obtención de Outputs

<small>§6</small>

### 19.1 — Tablero de vigilancia post-launch

<small>§6.1</small>

**Explicación**

Tablero que vigila los **3 elementos críticos** del sistema en producción. Cada elemento tiene 2 métricas y una acción correctiva si falla. Sin baseline de las 3, cualquier decisión de escalado es ciega.

**Patrón o fórmula**

```text
3 elementos × 2 métricas × acción correctiva si falla:

Elemento 1 — Flujo GeoArticle → Location
Elemento 2 — Autoridad del GeoHub
Elemento 3 — Conversión del Servicio Core

Cadencia:
  Baseline: 4 semanas tras lanzamiento
  Revisión: mensual durante los primeros 6 meses
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 19.1 — los 3 elementos con sus 2 métricas + acciones correctivas.

**Ejemplos incorrectos**

```text
- Vigilancia ad-hoc sin baseline (decisiones ciegas)
- Tratar fallos de métricas como señal de "crear más páginas"
  (deben corregirse, no escalarse)
- Saltar el establecimiento de baseline a las 4 semanas
- Revisar trimestralmente en lugar de mensualmente (datos stale)
```

**Regla final**

```text
Sin baseline + corrección de fallos en métricas, no se aplica el escalado.
```

**Validación operativa**

Cruce con Paso-13 13.8 (Tracking Plan) + Paso-15 15.5 (LBS) + 15.7 (GeoHub) + 15.8 (GAs).

**Cómo se obtiene**

- **Fuente:** GMB Crush + Datos de búsqueda.
- **Método:** Configurar dashboards en GA4 (eventos de click en puentes, conversión LBS) + GSC (impresiones GeoHub, posiciones queries amplias).

**Output del paso**

- **Tipo:** Tablero con 3 elementos × 2 métricas.
- **Ejemplo (Cerrajeros Madrid 24h):** baseline establecido a las 4 semanas post-launch.

### 19.2 — Estado de los 3 triggers por candidato

<small>§6.2</small>

**Explicación**

Para cada LCA candidata a Approved Expansion, evaluar 3 triggers. Regla 2-de-3: se pueden crear páginas de barrio cuando se cumplen al menos 2 de los 3.

**Patrón o fórmula**

```text
Trigger 1 — Location ya responde:
  - Impresiones >100/mes en GSC (en LBS Madrid)
  - Clicks reales >10/mes
  - Al menos 1 keyword en posición <30

Trigger 2 — GeoArticles traen tráfico:
  - Al menos 1 GA con impresiones >50/mes
  - Al menos 1 GA con clicks >5/mes
  - Posición media <40 para alguna keyword del artículo

Trigger 3 — Señal en SERP:
  - SERP del barrio difiere de la SERP de ciudad
  - 3+ resultados específicos del barrio
  - Google mantiene la intención al añadir el barrio

Decisión:
  3/3 → se puede crear (alta confianza)
  2/3 → se puede crear
  1/3 → NO escalar, reevaluar en 4-8 semanas
  0/3 → descartar
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 19.2 — Almagro con 3 triggers pendientes; resultado NO CREAR.

**Ejemplos incorrectos**

```text
- Escalar con 0-1/3 triggers (decisión impulsiva)
- Saltar evaluación de triggers (todo se aprueba)
- Cambiar criterios de los triggers ad-hoc (rompe disciplina)
- Usar volumen estimado de keyword research como sustituto de Trigger 1 o 2
  (volumen indica oportunidad, no prioridad)
```

**Regla final**

```text
3 triggers fijos con indicadores concretos. Mínimo 2/3 para considerar escalado.
Si solo 1/3, esperar y reevaluar en 4-8 semanas.
```

**Validación operativa**

Aplicar a cada LCA con datos suficientes en 19.1.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Datos de búsqueda.
- **Método:** Cruzar Tablero (19.1) con criterios de los 3 triggers; documentar estado por candidato.

**Output del paso**

- **Tipo:** Diagnóstico por LCA.
- **Ejemplo (Cerrajeros Madrid 24h):** Almagro con 3 triggers pendientes; NO CREAR.

### 19.3 — Análisis SERP + decisión

<small>§6.3</small>

**Explicación**

Protocolo objetivo para decidir CREAR / NO CREAR basado en el comportamiento real de Google. Solo se ejecuta si Triggers 1 y 2 (§6.2) ya están cumplidos.

**Patrón o fórmula**

```text
INPUT: Servicio + Ciudad + Barrio

INSTRUCCIONES:
1. Ejecutar dos búsquedas en Google:
   a) "{servicio} {ciudad}"
   b) "{servicio} {barrio}"
2. Analizar SOLO resultados orgánicos (ignorar Local Pack y Ads).
3. Comparar las dos SERPs respondiendo 4 preguntas.
4. Clasificar en escenario:
   ESCENARIO A (sin segmentación) → NO CREAR
   ESCENARIO B (con segmentación) → CREAR si Triggers 1+2 también

OUTPUT: Resultado + Justificación 3-5 líneas + Nivel de confianza
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 19.3 — protocolo aplicado a Almagro; pendiente hasta tracción LBS Madrid.

**Ejemplos incorrectos**

```text
- Decidir por número de competidores (cantidad ≠ oportunidad)
- Decidir por volumen estimado de búsqueda (volumen ≠ prioridad)
- Saltar el protocolo (decisión por intuición)
- Una sola ubicación física (sesgo de personalización)
- No documentar nivel de confianza (post-mortem imposible)
```

**Regla final**

```text
Solo decidir basado en el comportamiento real de la SERP. Google es el árbitro final.
Repetir análisis en al menos 2 ubicaciones físicas distintas para evitar sesgo.
```

**Validación operativa**

Solo aplicar si Triggers 1+2 ya están cumplidos. Cruce con §6.2.

**Cómo se obtiene**

- **Fuente:** GMB Crush + Competidores.
- **Método:** Doble búsqueda en Google (servicio+ciudad / servicio+barrio) + comparación de orgánicos top 10 + clasificación en Escenario A o B.

**Output del paso**

- **Tipo:** SERP analysis + decisión documentada.
- **Ejemplo (Cerrajeros Madrid 24h):** análisis pendiente hasta tracción LBS Madrid.

### 19.4 — Log de decisiones de escalado

<small>§6.4</small>

**Explicación**

Documento histórico de TODAS las decisiones de escalado (CREAR, NO CREAR, POSPONER). Garantiza trazabilidad de por qué cada zona se escaló o no, y cuándo re-evaluar.

**Patrón o fórmula**

```text
Por cada decisión:
  Fecha + Candidato + Triggers (estado 1/2/3) + SERP analysis +
  Decisión + Justificación (3-5 líneas) + Confianza + Aprobado por +
  Próxima revisión (si POSPONER)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 19.4 — entrada #001 con todos los campos.

**Ejemplos incorrectos**

```text
- Log sin Justificación (decisiones opacas)
- Log sin Confianza (post-mortem sin contexto)
- Log sin Próxima revisión para POSPONER (zonas pospuestas indefinidamente)
- Decisiones no documentadas (rompe Paso-13 13.7)
```

**Regla final**

```text
Cada decisión = 1 entrada con campos obligatorios. Cruzar con Documentación de Cambios.
```

**Validación operativa**

Cruce con Paso-13 13.7 (Documentación de Cambios template).

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Plantilla con campos obligatorios por decisión + actualización post-evaluación.

**Output del paso**

- **Tipo:** Documento histórico.
- **Ejemplo (Cerrajeros Madrid 24h):** log con entradas según se vayan tomando decisiones.

### 19.5 — URL Matrix actualizada con Approved Expansion Areas

<small>§6.5</small>

**Explicación**

Tras una decisión CREAR (19.4), actualizar URL Matrix con sub-cluster de la Approved Expansion Area. Aplica `generate_expansion()` del Paso-11 11.11.

**Patrón o fórmula**

```text
1. Approved Expansion Areas (Paso-01 1.11) ← añadir nueva area
2. generate_expansion() (Paso-11 11.11) genera por area:
   - 1 GeoHub
   - S LBS
   - G×S GAs
3. URL Matrix actualizada con sub-cluster
4. Documentación de Cambios (Paso-13 13.7) — entrada de cambio
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 19.5 — plantilla de actualización URL Matrix v2 cuando aplique.

**Ejemplos incorrectos**

```text
- Modificar URL Matrix sin Documentación de Cambios
- Saltar generate_expansion() (URLs ad-hoc)
- Mezclar URLs base con expansion (rompe Paso-07 7.15)
- Crear URLs expansion sin decisión CREAR previa en log (19.4)
```

**Regla final**

```text
URL Matrix v2 = URL Matrix v1 + sub-cluster Approved Expansion (separado).
Solo tras decisión CREAR documentada.
```

**Validación operativa**

Cruce con Paso-01 1.11 + Paso-04 4.10 + Paso-07 7.15 + Paso-11 11.11.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Aplicar generate_expansion() + actualizar URL Matrix + documentar cambio.

**Output del paso**

- **Tipo:** URL Matrix v2.
- **Ejemplo (Cerrajeros Madrid 24h):** URL Matrix se actualizará si se aprueba algún Approved Expansion futuro.

## Checklist Final

<small>§7</small>

- ☐ Tablero de vigilancia con 3 elementos críticos × 2 métricas configurado (19.1)
- ☐ Baseline establecido a las 4 semanas post-launch
- ☐ Estado de 3 triggers evaluado por candidato (19.2)
- ☐ Regla 2-de-3 aplicada (necesarios al menos 2/3 para considerar escalado)
- ☐ Análisis SERP ejecutado para shortlist con Triggers 1+2 cumplidos (19.3)
- ☐ Protocolo doble búsqueda + análisis en 2 ubicaciones físicas
- ☐ Log de decisiones documentado con campos obligatorios (19.4)
- ☐ URL Matrix actualizada solo tras decisión CREAR documentada (19.5)
- ☐ Cruce con Documentación de Cambios (Paso-13 13.7)

## Outputs Consolidados

<small>§8</small>

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 19.1 | ← Paso-13 13.8 + Paso-15 15.5 + 15.7 + 15.8 + Paso-18 18.7 | **Tablero de vigilancia** = 3 elementos críticos (Flujo GA→Location / Autoridad GeoHub / Conversión LBS core) × 2 métricas + acciones correctivas; baseline 4 semanas post-launch | Configurar dashboards GA4 (eventos clicks puentes, conversión LBS) + GSC (impresiones GeoHub, posiciones queries amplias). **Fuente:** GMB Crush + Datos de búsqueda. | confirmed |
| 19.2 | ← 19.1 | **Estado de los 3 triggers** = Trigger 1 (Location ya responde) + Trigger 2 (GeoArticles traen tráfico) + Trigger 3 (Señal en SERP) con regla 2-de-3 | Cruzar Tablero con criterios de 3 triggers; documentar estado por candidato. **Fuente:** GMB Crush + Datos de búsqueda. | confirmed |
| 19.3 | ← 19.2 | **Análisis SERP + decisión** = protocolo doble búsqueda + 2 escenarios (A sin segmentación → NO CREAR / B con segmentación → CREAR si Triggers 1+2) | Doble búsqueda Google (servicio+ciudad / servicio+barrio) + comparación orgánicos + clasificación. **Fuente:** GMB Crush + Competidores. | confirmed |
| 19.4 | ← 19.3 + Paso-13 13.7 | **Log de decisiones** = entradas con campos obligatorios (Fecha + Candidato + Triggers + SERP + Decisión + Justificación + Confianza) | Plantilla con campos obligatorios + actualización post-evaluación. **Fuente:** GMB Crush. | confirmed |
| 19.5 | ← 19.4 + Paso-01 1.11 + Paso-11 11.11 | **URL Matrix actualizada** = v2 con sub-cluster Approved Expansion (1 GH + S LBS + G×S GAs por barrio aprobado) | Aplicar generate_expansion() + actualizar URL Matrix + documentar cambio en Paso-13 13.7. **Fuente:** GMB Crush. | confirmed |

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
- Post-Launch Scaling Framework GMB Crush (3 elementos vigilancia + 3 triggers + protocolo SERP doble búsqueda)

> **Nota — Escalado con datos, no con intuición:**
> El Paso 19 establece un protocolo objetivo para decidir cuándo escalar a páginas de barrio. Los **3 elementos** (§6.1) miden si el sistema funciona en producción. Los **3 triggers** (§6.2) con regla 2-de-3 validan si hay tracción suficiente. El **protocolo SERP** (§6.3) decide la creación basado en el comportamiento real de Google, NO en intuición, NO en número de competidores, NO en volumen estimado. El operador NO crea páginas de barrio sin ejecutar 19.1 → 19.4.
>
> **Sobre el contenido literal:**
> Los 3 elementos a vigilar (sub-sección 4.1), los 3 triggers (sub-sección 4.2) y el protocolo SERP (sub-sección 4.3) están portados **literalmente** del documento fuente original (secciones 7, 9, 10 del fuente). Los indicadores numéricos (>100/mes, >50/mes, pos <30, etc.) son los del original. Cualquier discrepancia entre este doc y el original debe resolverse en favor del original.
