# Plan de ejecución del Bloque 4 (Pasos 11-13)

> Plantilla del sistema. Vista unificada de los **45 outputs** que producen los pasos 11, 12 y 13 cuando se ejecutan para cualquier cliente. Antes de arrancar, esta tabla muestra qué se va a producir, cómo se decide cada output y qué fuentes hacen falta.

> **Cómo usar esta plantilla:**
> 1. Confirma que los Bloques 1, 2 y 3 están cerrados (137 outputs upstream en `confirmed`).
> 2. Rellena la sección "Cliente" si arrancas un cliente nuevo.
> 3. Lee las 3 tablas (Paso 11, 12, 13) para entender qué outputs hay que producir.
> 4. Resuelve los bloqueos críticos antes de arrancar la ejecución (sección final).
> 5. Una vez ejecutado, vuelca los valores reales en `02 Consolidación Outputs/`.

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

> **Nota:** Bloque 4 es **meta** — apenas tiene inputs nuevos. Casi todo viene vía `← X.Y` de Bloques 1-3. Solo el Tracking Plan (13.8) y la Documentación de Cambios template (13.7) requieren decisión del operador.

### Catálogo formal de Fuentes del sistema

| Fuente formal | Significado |
|---|---|
| `GMB Crush` | La doctrina del sistema lo dicta |
| `Decisión de diseño` | Lo decide el operador con criterio |

### Mapeo entre ambas

| Etiqueta operativa | Equivale a (Fuente formal) |
|---|---|
| `← X.Y` | (depende — hereda la Fuente del output X.Y) |
| `Doctrina` | `GMB Crush` |
| `Decisión operador` | `Decisión de diseño` |

---

## Paso 11 — Pseudocódigo del Sistema (19 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **11.1** Función `load_inputs()` | `← Paso-01 + Paso-02 + Paso-03` | Lectura programática de §8 de cada a-doc + preflight; serialización en dict |
| **11.2** Función `normalize_slugs()` | `← 2.2 + 2.3 + 2.4 + 3.3` | Implementar slugify estándar + aplicar a 4 grupos de slugs |
| **11.3** Función `validate_categories()` | `← 2.7 + 2.12` | Comparar Additional vs core; aplicar criterio cobertura |
| **11.4** Función `generate_homepage()` | `← 4.3 + 5.3` | Aplicar spec Homepage del Paso-05 5.3 con inputs heredados |
| **11.5** Función `generate_service_overview()` | `← 4.4 + 5.4` | Aplicar spec SO del Paso-05 5.4 replicada × S core services (no-locales) |
| **11.6** Función `generate_geohub()` | `← 4.5 + 5.7 + 3.2` | Aplicar spec GeoHub Paso-05 5.7 al Main City con URL Option A o B |
| **11.7** Función `generate_lbs()` | `← 4.6 + 5.5` | Aplicar spec LBS Paso-05 5.5 replicada × S × Main City |
| **11.8** Función `generate_additional_category()` | `← 4.7 + 5.6 + 3.3` | Aplicar spec AC Paso-05 5.6 a las A categorías efectivas |
| **11.9** Función `generate_geoarticles()` | `← 4.8 + 5.8 + 3.4` | Aplicar spec GA Paso-05 5.8 a G×S combinaciones service × topic |
| **11.10** Función `inject_local_coverage()` | `← 6.2 + 6.12 + 6.17` | Iterar páginas, mapear page_type → conjunto LCAs según matriz |
| **11.11** Función `generate_expansion()` (opcional) | `← 1.11 + 4.10` | Replicar lógica generate_*() por Approved Area; vacío si E=0 |
| **11.12** Función `assign_internal_links()` | `← 7.9 + 7.11` | Lookup matriz 7.11 + selección anchor por catálogo 7.9 |
| **11.13** Función `score_priority()` | `← 8.1-8.10` | 6 funciones de medición + suma + mapeo tier/phase doctrinales |
| **11.14** Función `check_dependencies()` | `← 8.11 + 10.10` | Lookup parents + comparar phases + bloquear conflictos |
| **11.15** Función `run_qa()` | `← 9.2-9.8` | 5 funciones QA + consolidación gate + opcional GBP checklist |
| **11.16** Función `output_matrices()` | `← 3.5 + 3.8 + 7.11` | Serializar páginas scored + link_matrix en 3 estructuras tabulares |
| **11.17** Pseudocódigo principal `main()` | `← 11.1-11.16` | Composición funcional + manejo de errores en orden secuencial |
| **11.18** Validación cobertura inputs | `Doctrina` | Static analysis de las 16 funciones + cruce con catálogo upstream |
| **11.19** Validación secuencia dependencias | `Doctrina` | Inspección manual del orden + cross-check con dependency graph |

---

## Paso 12 — Master Prompt (12 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **12.1** Master Prompt principal | `← 11.17 + Bloques 1-3` | Componer 7 secciones del prompt + integrar reglas y validations (~580 líneas literales) |
| **12.2** Auxiliary Prompt URL Matrix | `← 3.5 + 4.3-4.8` | Aislar sección URL Matrix del Master + simplificar ROLE |
| **12.3** Auxiliary Prompt Content Architecture | `← 5.3-5.8 + 6.6-6.11` | Aislar sección Content Architecture del Master |
| **12.4** Auxiliary Prompt GeoArticles | `← 3.4 + 8.11` | Aislar sección GA del Master + integrar keyword research |
| **12.5** Auxiliary Prompt QA | `← 9.2-9.8` | Aislar sección QA del Master + estructurar output diagnóstico |
| **12.6** Estructura del prompt | `Doctrina` | Aplicar plantilla 10-secciones (ROLE/CONTEXT/INPUTS/PROCESS/...) |
| **12.7** Web-First GBP Rule | `← 1.3 + 9.8` | Embeberla en Master Prompt + activar condicionalmente |
| **12.8** 14 reglas no-negociables | `← Bloques 1-3 (todas las reglas)` | Compilar reglas desde pasos origen y consolidar en sección del prompt |
| **12.9** Inputs Validation embedded | `← Paso-01 1.X + Paso-02 2.X` | Compilar checks desde §3 Heredados + integrar en sección 8 del prompt |
| **12.10** Executive Summary template | `← Paso-01 + Paso-02 + Paso-08` | Plantilla con placeholders rellenados por el prompt |
| **12.11** Validación prompt produce 7 outputs | `← 12.1-12.5` | Inspección de salida + cross-check con outputs esperados |
| **12.12** Validación prompt cumple web-first | `← 1.3 + 9.8` | Inspección de salida + cross-check con 7 sub-checks Paso-09 9.8 |

---

## Paso 13 — Sistema Final Operativo (14 outputs)

| Output a decidir | Fuentes para Decidir | Cómo Decidimos |
|---|---|---|
| **13.1** SOP completo del sistema | `← Bloques 1-4 (todos los outputs)` | Componer 11 secciones referenciando outputs upstream + 13.2-13.14 |
| **13.2** Resumen ejecutivo del cluster | `← 1.X + 2.X + 8.X + 12.10` | Plantilla con placeholders rellenados desde outputs upstream |
| **13.3** Workflow detallado | `← Bloques 1-4 (estructura)` | Compilar desde §5 de los 13 a-docs anteriores |
| **13.4** Estructura de carpetas y archivos | `Doctrina` | Captura del filesystem + documentar convención |
| **13.5** Inventario URL final consolidado | `← 3.5 + 8.14 + 9.7` | Join de matrices de pasos upstream en tabla consolidada |
| **13.6** 15 Reglas No Negociables | `← Bloques 1-3 + 12.8` | Compilar desde Paso-12 12.8 (14) + añadir 15ª "fuente única" |
| **13.7** Documentación de Cambios template | `Decisión operador` | Plantilla 6 campos obligatorios |
| **13.8** Tracking Plan | `← 10.3 + 10.7` + `Decisión operador` | Plantilla del stack + cadencia operativa |
| **13.9** Roadmap final | `← 10.4-10.9` | Consolidar las 5 fases del Paso-10 en vista de roadmap |
| **13.10** Pre-requisitos para Paso 14 | `← 9.7 + 9.8 + 10.13` | Compilar checklist 7 items desde outputs upstream |
| **13.11** Sistema como fuente única de verdad | `Doctrina` | Declaración doctrinal embebida en el SOP |
| **13.12** Validación cluster ready for GBP | `← 9.7 + 13.10` | Cruzar 7 checks contra outputs upstream |
| **13.13** Validación tracking configurado | `← 13.8` | Auditar cada herramienta del stack |
| **13.14** Cierre de Bloque 4 | `← 11 + 12 + 13` | Validación de los 3 pasos del Bloque 4 |

---

## Resumen — qué necesita la IA antes de ejecutar

### Inputs heredados de Bloques 1-3 (deben estar `confirmed`)

- ☐ **Outputs 1.X** — Intake completo (los 14 outputs de Paso 1)
- ☐ **Outputs 2.X** — Fórmula Maestra (los 15 outputs de Paso 2)
- ☐ **Outputs 3.X** — Matriz Base (los 14 outputs de Paso 3)
- ☐ **Outputs 4.X-7.X** — Bloque 2 Arquitectura (los 59 outputs)
- ☐ **Outputs 8.X-10.X** — Bloque 3 Priorización (los 35 outputs)

**Total upstream:** 137 outputs de Bloques 1-3 que el Bloque 4 consolida.

### Decisiones del operador (2 nuevas en Bloque 4)

- ☐ Tracking stack y cadencia (output 13.8) — operador decide qué tools y frecuencia
- ☐ Documentación de Cambios convention (output 13.7) — operador decide formato

### Defaults doctrinales (no requieren input)

- Las 16 funciones del pseudocódigo (outputs 11.1-11.16)
  · 3 funciones de carga/normalización: 11.1-11.3
  · **6 funciones individuales por page type: 11.4-11.9** (HP/SO/GH/LBS/AC/GA)
  · 7 funciones de orquestación: 11.10-11.16
- Pseudocódigo principal `main()` (output 11.17)
- Estructura del prompt (output 12.6)
- Web-First GBP Rule (output 12.7)
- Las 14 reglas no-negociables del prompt (output 12.8)
- Las 11 secciones del SOP (output 13.1)
- Las 15 Reglas No Negociables del sistema (output 13.6)
- Estructura de carpetas (output 13.4)

### Inputs externos NO requeridos

> Bloque 4 NO necesita Local Pack, Keyword research, ni Cliente confirma. Es **enteramente meta** — orquesta y consolida lo ya producido en Bloques 1-3.

---

## Cascada de dependencias (qué bloquea qué)

```
Bloques 1-3 cerrados (137 outputs confirmed)
    │
    ├─► Paso 11 (Pseudocódigo)
    │       │
    │       ├── 11.1-11.3 carga + normalización
    │       ├── 11.4-11.9 las 6 funciones por page type (HP/SO/GH/LBS/AC/GA)
    │       ├── 11.10-11.16 orquestación (inject + expansion + links + score + qa + matrices)
    │       ├── 11.17 main() (orquestador)
    │       └── 11.18-11.19 validaciones
    │
    ├─► Paso 12 (Master Prompt)
    │       │
    │       ├── 12.1 Master Prompt (← 11.17 + Bloques 1-3)
    │       ├── 12.2-12.5 4 auxiliares
    │       ├── 12.6-12.10 estructura + reglas + validations
    │       └── 12.11-12.12 validaciones
    │
    └─► Paso 13 (Sistema Final Operativo)
            │
            ├── 13.1 SOP completo (← Bloques 1-4)
            ├── 13.2-13.11 11 secciones del SOP
            ├── 13.12-13.13 validaciones operacionales
            └── 13.14 cierre de Bloque 4 → Bloque 5 UNLOCKED
```

---

## Bloqueos antes de ejecutar

> Si alguno de estos bloqueos no se resuelve, los outputs de Bloque 4 quedarán como `⚠ inferido`. El Paso 14 (GBP Creation) NO se arranca hasta que Bloque 4 esté 100% cerrado.

| Bloqueo | Outputs que quedan ⚠ | Cómo se desbloquea |
|---|---|---|
| Bloques 1-3 sin cerrar | TODOS los 45 outputs de Bloque 4 | Cerrar Pasos 1-10 antes de arrancar Bloque 4 |
| Outputs upstream con ⚠ inferido | Los outputs derivados quedan ⚠ heredado | Volver al paso correspondiente, completar, re-correr |
| Operador no decide Tracking stack | 13.8 + 13.13 | Operador define stack y cadencia |
| Operador no decide convention de Documentación de Cambios | 13.7 | Operador define template |

---

> **Cuándo arrancar la ejecución:** una vez Bloques 1-3 estén cerrados con los 137 outputs upstream en `confirmed`. Bloque 4 es **enteramente derivativo** — produce 45 outputs nuevos pero todos son consolidaciones/orquestaciones de los upstream. Cero research externo, cero tools nuevos. Tras cerrar Bloque 4, el Paso 14 (GBP Creation) queda DESBLOQUEADO con 7 pre-requisitos del output 13.10.
