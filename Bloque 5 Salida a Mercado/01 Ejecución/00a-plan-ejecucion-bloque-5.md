# Plan de ejecución del Bloque 5 (Pasos 15-19)

> Plantilla del sistema. Vista unificada de los **39 outputs** que producen los pasos 15, 16, 17, 18 y 19 cuando se ejecutan para cualquier cliente. Antes de arrancar, esta tabla muestra qué se va a producir, cómo se decide cada output y qué fuentes hacen falta.

> **Cómo usar esta plantilla:**
> 1. Confirma que los Bloques 1-4 están cerrados (182 outputs upstream en `confirmed`).
> 2. Rellena la sección "Cliente" si arrancas un cliente nuevo.
> 3. Lee las 5 tablas (Paso 15-19) para entender qué outputs hay que producir.
> 4. Resuelve los bloqueos críticos antes de arrancar la ejecución (sección final).
> 5. Una vez ejecutado, vuelca los valores reales en `02 Consolidación Outputs/`.

> **Nota sobre Paso 14:** Este Bloque 5 NO incluye el Paso 14 (Creación del GBP). El Paso 14 vive en Bloque 6 — GBP, y se ejecuta DESPUÉS del Paso 18 (Deploy) según la regla web-first. El cluster web sale a mercado con web pública pero GBP aún no creado; el GBP se crea en Bloque 6 usando la web ya publicada como source of truth.

---

## Cliente

| Campo | Valor |
|---|---|
| 1. Nombre del negocio | `[pendiente]` |
| 2. Qué hace | `[pendiente]` |
| 3. Dirección con CP | `[pendiente]` |
| 4. Estado del GBP | `[pendiente]` |
| 5. Ciudades para análisis Local Pack | `[pendiente]` |

---

## Leyenda de la columna "Fuentes para Decidir"

### Etiquetas operativas

| Etiqueta | Significado |
|---|---|
| `← X.Y` | Hereda del output X.Y de un paso anterior |
| `Doctrina` | Default fijo de los manuales GMB Crush |
| `Decisión operador` | Elección del que ejecuta el sistema |
| `Cliente confirma` | Input pendiente del cliente (referencia visual / aprobación diseño) |
| `Datos de búsqueda` | GSC + GA4 + Rank Tracker post-launch |
| `Local Pack` | Análisis SERP / Maps post-launch |

### Catálogo formal de Fuentes del sistema

| Fuente formal | Significado |
|---|---|
| `GMB Crush` | La doctrina del sistema lo dicta |
| `Input humano` | Lo declara el cliente |
| `Decisión de diseño` | Lo decide el operador |
| `Competidores` | Análisis SERP / Local Pack |
| `Datos de búsqueda` | Tracking post-launch |

### Mapeo entre ambas

| Etiqueta operativa | Equivale a (Fuente formal) |
|---|---|
| `← X.Y` | (depende — hereda Fuente del output X.Y) |
| `Doctrina` | `GMB Crush` |
| `Decisión operador` | `Decisión de diseño` |
| `Cliente confirma` | `Input humano` |
| `Datos de búsqueda` | `GMB Crush + Datos de búsqueda` |
| `Local Pack` | `GMB Crush + Competidores` |

---

## Paso 15 — Redacción de Contenido (13 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **15.1** Capas de redacción (4 capas) | `Doctrina` | Framework declarativo: Estructura / Zonas / Argumentos / Entidades |
| **15.2** Reglas de calidad universal (4 reglas) | `Doctrina` | 4 reglas fijas: Hero+CTA / Problema / Datos / Local |
| **15.3** Homepage redactada | `← 5.3 + 6.6 + 12.3` | Aplicar Auxiliary Content Architecture prompt a Homepage spec |
| **15.4** Service Overview Pages redactadas | `← 5.4 + 6.7` | Aplicar Auxiliary Content Architecture × S core services |
| **15.5** Location-Based Service Pages redactadas | `← 5.5 + 6.8 + 1.10` | Aplicar Auxiliary Content Architecture × S × Main City |
| **15.6** Additional Category Page redactada | `← 5.6 + 6.9` | Aplicar Auxiliary Content Architecture × A categorías efectivas |
| **15.7** GeoHub redactada | `← 5.7 + 6.10` | Aplicar Auxiliary Content Architecture con spec GeoHub |
| **15.8** GeoArticles redactados | `← 5.8 + 6.11 + 3.4` | Aplicar Auxiliary GeoArticles prompt × G×S combinaciones |
| **15.9** Página de contacto redactada | `← 1.4` | Plantilla básica de contacto + NAP + form + schema |
| **15.10** Validación clusters completos | `Doctrina` | Validar count por cluster (SO + LBS + 3 GAs por servicio core) |
| **15.11** Validación SO no compite con LBS | `Doctrina` | Comparar H1 SO vs H1 LBS por servicio core |
| **15.12** Validación GA enlaza a LBS padre | `Doctrina` | Inspeccionar 3 puntos de enlace por GA |
| **15.13** Validación datos verificables | `← 1.3 + 9.8` | Inspeccionar copy + schema vs reglas web-first |

---

## Paso 16 — Diseño y Layout (6 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **16.1** Identidad Visual y CSS Base | `Cliente confirma` (web de referencia) | Inspección visual + DevTools de la web de referencia |
| **16.2** Layout y Estructura por Sección | `← 5.3-5.8 + 6.6-6.11` | Mapear secciones por page type a partir de specs heredados |
| **16.3** Propuesta de Diseño aprobada | `← 16.1 + 16.2` + `Cliente confirma` | Mockups Figma + paleta + typography → cliente revisa → iteración → aprobación |
| **16.4** Design Tokens Tailwind | `← 16.1` | Convertir Identidad Visual a tailwind.config.js |
| **16.5** Reglas Críticas CSS | `← 16.4` | Definir reglas por componente (Hero/Buttons/Cards/Grids/Forms) |
| **16.6** Layout-Map Definitivo | `← 16.2 + 15.3-15.9` | Mapear secciones a Components + props alineados con copy |

---

## Paso 17 — Constructor del Sitio (8 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **17.1** Acta de Lectura y Autocontraste | `← Pasos 1-16 (todos)` | Lectura sistemática §8 + cross-check URL Matrix vs copy vs schemas vs links |
| **17.2** Proyecto Astro 5 + Tailwind v3 + pnpm | `Decisión operador` (stack canónico) | Comandos pnpm + copia tailwind.config Paso-16 |
| **17.3** 7 componentes UI parametrizados | `← 16.5` | Construir Astro components con props alineados a reglas CSS |
| **17.4** Header + Footer + Layout wrapper | `← 7.11 + 16.6` | Construir layouts globales aplicando Layout-Map |
| **17.5** 28+1 páginas construidas | `← 3.5 + 15.3-15.9 + 16.6` | Iterar URL Matrix + componer páginas con BaseLayout + Components + copy |
| **17.6** Schemas implementados y validados | `← 5.9 + 6.17 + 9.10` | Embed JSON-LD según mapping + cruce con LCAs + validar tools |
| **17.7** Limpieza de rastros IA | `Doctrina` | Iterar 5 áreas (README/src/meta/package/commits) + validar grep |
| **17.8** Build local pasando | `← 17.2-17.7` | Ejecutar pnpm install && pnpm build + revisar output |

---

## Paso 18 — QA y Deploy (7 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **18.1** Auditoría Técnica (16 criterios) | `← 4.1 + 5.9 + 17.5-17.6` | 16 checks individuales con tools (Lighthouse, GRT, manual responsive) |
| **18.2** Auditoría de Contenido (8 criterios) | `← 15.3-15.13 + 9.4 + 9.8` | Inspección manual + grep + cruce con Paso-15 + Paso-01 1.4 |
| **18.3** Auditoría Visual (5 criterios) | `← 16.4 + 16.6` | Inspección visual de 29 páginas + cruce con Layout-Map y tokens |
| **18.4** Auditoría de Rastros IA (6 criterios) | `← 17.7` | grep + inspección README + package.json + git log |
| **18.5** Configuración Cloudflare | `Decisión operador` (host canónico) | Crear deploy-config.md + aplicar config en Cloudflare dashboard |
| **18.6** Sitio en Producción | `← 18.1-18.5` | Push a main + Cloudflare auto-deploy + verificación post-deploy |
| **18.7** Sitemap en GSC | `← 18.6` | GSC dashboard + DNS TXT verification + submit sitemap |

---

## Paso 19 — Acciones Futuro y Escalado (5 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **19.1** Tablero de vigilancia post-launch | `← 13.8 + 18.7` + `Datos de búsqueda` | Configurar dashboards GSC + GA4 + Rank Tracker; revisar regularmente |
| **19.2** Estado de los 3 triggers por candidato | `← 19.1` | Cruzar Tablero con criterios de 3 triggers (volumen / posición / concurrencia) |
| **19.3** Análisis SERP + decisión | `← 19.2 + 8.6` + `Local Pack` | SERP analysis manual + Ahrefs para fortaleza top 10 |
| **19.4** Log de decisiones de escalado | `← 19.3 + 13.7` | Plantilla con 8 campos por decisión |
| **19.5** URL Matrix actualizada con Approved Expansion | `← 19.4 + 1.11 + 11.11` | Aplicar generate_expansion() + actualizar URL Matrix + documentar cambio |

---

## Resumen — qué necesita la IA antes de ejecutar

### Inputs heredados de Bloques 1-4 (deben estar `confirmed`)

- ☐ **Outputs 1.X-13.X** (Bloques 1-4): 182 outputs upstream

### Decisiones del operador (3 nuevas en Bloque 5)

- ☐ Stack técnico canónico (output 17.2) — Astro 5 + Tailwind v3 + pnpm
- ☐ Hosting canónico (output 18.5) — Cloudflare Pages
- ☐ Aprobaciones de cliente: web de referencia (16.1) + propuesta de diseño (16.3)

### Tools externos requeridos

- ☐ **Figma** — para mockups y propuesta de diseño (output 16.3)
- ☐ **Lighthouse** — para auditoría técnica (output 18.1)
- ☐ **Google Rich Results Test** — para validación de schemas (output 17.6, 18.1)
- ☐ **Google Search Console + Google Analytics 4 + Rank Tracker (Ahrefs)** — para vigilancia post-launch (output 19.1)

### Defaults doctrinales (no requieren input)

- 4 capas de redacción + 4 reglas universales (outputs 15.1, 15.2)
- 7 componentes UI (output 17.3) y 6 fases del constructor (17.1-17.7)
- 35 criterios de QA (outputs 18.1-18.4)
- 3 triggers + protocolo SERP (outputs 19.2, 19.3)

---

## Cascada de dependencias (qué bloquea qué)

```
Bloques 1-4 cerrados (182 outputs confirmed)
    │
    ├─► Paso 15 (Redacción)
    │       └── Aplica Master Prompt 12.1 + auxiliares 12.3, 12.4
    │
    ├─► Paso 16 (Diseño/Layout)
    │       │
    │       ├── 16.1 ← Cliente confirma web de referencia
    │       └── 16.3 ← Cliente aprueba propuesta de diseño
    │
    ├─► Paso 17 (Constructor)
    │       │
    │       ├── 17.1 acta lectura ← Pasos 1-16 (cross-check)
    │       └── 17.5 páginas ← URL Matrix + copy + Layout-Map
    │
    ├─► Paso 18 (QA + Deploy)
    │       │
    │       ├── 18.1-18.4 4 auditorías (35 criterios totales)
    │       ├── 18.5 configuración Cloudflare
    │       ├── 18.6 deploy ejecutado
    │       └── 18.7 sitemap en GSC
    │
    └─► Paso 19 (Escalado post-launch)
            │
            ├── 19.1 vigilancia ← post-launch ≥ 30 días
            └── 19.5 URL Matrix v2 si APROBAR expansion
```

---

## Bloqueos antes de ejecutar

| Bloqueo | Outputs que quedan ⚠ | Cómo se desbloquea |
|---|---|---|
| Bloques 1-4 sin cerrar | TODOS los 39 outputs de Bloque 5 | Cerrar Pasos 1-13 antes de arrancar Bloque 5 |
| Cliente no aprueba web de referencia | 16.1, 16.3, 16.4-16.6 (todo Paso 16) | Cliente confirma web de referencia |
| Cliente no aprueba propuesta de diseño | 16.3 → 16.4-16.6 + Paso 17 | Cliente revisa mockups + aprueba |
| Build local roto | 17.8 → bloquea Paso 18 | Resolver errores de build |
| Cualquier auditoría < 100% | 18.1-18.4 → bloquea 18.5-18.7 | Volver al paso de origen del fallo |
| Sin datos GSC mínimos 30 días | 19.1-19.4 (Paso 19 entero) | Esperar 30+ días post-launch + medir |

---

> **Cuándo arrancar la ejecución:** una vez Bloques 1-4 estén cerrados con los 182 outputs upstream en `confirmed`. Bloque 5 es la **fase de salida a mercado** — convierte la arquitectura abstracta en sitio web publicado en producción. Tras cerrar Paso 18, el cluster está LIVE; el Paso 19 es continuo (vigilancia + escalado bajo demanda). El Paso 14 (GBP Creation) se ejecuta en Bloque 6 DESPUÉS del Paso 18.
