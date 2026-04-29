# 00 Convenciones de ejecución

> Reglas operativas que aplican a la IA cuando ejecuta cualquier paso del sistema GMB Crush. No son doctrina del sistema (que vive en los Xa) — son reglas de **honestidad de output**: cómo declarar qué está confirmado vs qué está inferido cuando faltan herramientas externas.

---

## Regla 1 — Marcador `⚠` para outputs inferidos

Cuando la IA ejecuta un paso y un campo necesita acción externa real (abrir Google Maps para Local Pack, consultar keyword tool para Datos de búsqueda) pero la IA NO tiene acceso a esa herramienta en el momento, el output debe llevar el marcador `⚠` con un sufijo que indique qué se necesita para validar.

### Cuándo aplicar `⚠`

Aplicar cuando se cumplen las **dos** condiciones:

1. La `Fuente` del campo (según catálogo de fuentes del b-doc) contiene `Competidores`, `Datos de búsqueda`, `IA sin respaldo`, o cualquier combinación con `+`.
2. La IA **no ejecutó** la acción externa real y sustituyó por inferencia, conocimiento sectorial o placeholder.

### Cuándo NO aplicar

No aplicar `⚠` cuando:

- `Fuente: GMB Crush` (puro) — doctrina aplicada directamente.
- `Fuente: Input humano` — lo declara el cliente, no se infiere.
- `Fuente: Decisión de diseño` — el operador elige.
- La IA **sí ejecutó** la acción externa (browser, keyword tool, etc.) → marcar como `validated` opcional.

---

## Formato del marcador

### En texto libre

```text
§9 Planned Primary GBP Category: Heating contractor  ⚠ inferido — pendiente Local Pack real
```

### En listas

```text
Servicios principales (5 core services)  ⚠ inferidos — pendiente Local Pack real:
  1. Instalación de aerotermia
  2. Mantenimiento de aerotermia
  ...
```

### En tablas

Añadir columna `Status` con uno de tres valores:

| Valor | Significado |
|---|---|
| `confirmed` | Fuente Input humano / GMB Crush / Decisión de diseño |
| `⚠ inferido` | Fuente Competidores / Datos / IA pero **sin** tool externa |
| `validated` | Fuente Competidores / Datos **con** tool externa ejecutada |

Ejemplo URL Matrix:

```text
| ID | URL | Schema | Priority | Phase | Status |
|---|---|---|---|---|---|
| HP | / | Organization + LocalBusiness | P1 | 1 | confirmed |
| SO-1 | /calefaccion/instalacion-aerotermia/ | Service | P1 | 1 | ⚠ inferido |
| GA-1 | /madrid/cuanto-cuesta-instalar-aerotermia/ | Article | P3 | 2 | ⚠ inferido |
```

---

## Regla 2 — Resumen de status al cierre de cada paso

Al terminar cada paso (Paso 1, 2, 3, ...), la IA debe entregar un bloque de cierre con la cuenta de outputs por status. Este bloque va al final del paso, antes de avanzar al siguiente.

### Plantilla de cierre

```text
## Resumen de status — Paso N

| Status | Cantidad | Acción pendiente |
|---|---:|---|
| confirmed | X | — |
| ⚠ inferido | Y | [tool externa necesaria, ej. "Abrir Google Maps de Madrid + Barcelona, extraer Local Pack top 5"] |
| ⚠ placeholder | Z | [acción del cliente, ej. "Confirmar teléfono y email reales"] |
```

### Ejemplo (Paso 1 Aeroterm)

```text
## Resumen de status — Paso 1 Aeroterm

| Status | Cantidad | Acción pendiente |
|---|---:|---|
| confirmed | 16 | — |
| ⚠ inferido | 25 | Abrir Google Maps de Madrid + Barcelona + París; extraer Local Pack top 5 para Primary Category, 5 servicios core, Candidate LCAs y trust signals del sector |
| ⚠ placeholder | 3 | Cliente debe confirmar: teléfono, email, dominio |
```

---

## Regla 3 — Outputs marcados ⚠ no deben pasar a publicación

Cualquier campo con marcador `⚠` queda **bloqueado para producción** hasta que:

- Un operador humano ejecute la acción externa pendiente y reemplace el valor.
- O la IA ejecute la acción externa con tool y promueva el campo a `validated`.

El Paso 18 (QA y deploy) debe rechazar el deploy si quedan marcadores `⚠ inferido` o `⚠ placeholder` en outputs estructurales (URLs, schema, NAP, categorías GBP).

---

## Por qué esta regla existe

Sin esta convención, la IA puede entregar outputs aparentemente terminados (28 URLs, 5 servicios, NAP completo) cuando en realidad varios campos son inferencias plausibles sustituyendo análisis competitivo real. Un humano leyendo el output puede llevárselo como ground truth y publicar contenido sobre datos no validados.

El marcador `⚠` hace explícito el **boundary entre lo que la IA sabe** (doctrina, intake) **y lo que la IA infiere** (Local Pack, keyword research) cuando faltan tools.
