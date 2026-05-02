Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 5 — Salida a Mercado/paso-18-qa-deploy/`, alineado con los frameworks oficiales GMB Crush. Los 35 criterios (16+8+5+6) y el protocolo de deploy están portados LITERALMENTE del documento fuente original.

# Paso 18 — QA y Deploy

<small>§1</small>

> **Cómo leer este documento:**
> - **Bloque I — Introducción** describe qué produce el paso y qué hereda.
> - **Bloque II — Ejemplo rellenado** muestra los 7 outputs del Paso 18 con sus valores reales para Cerrajeros Madrid 24h.
> - **Bloque III — Ejecución por la IA** contiene los 4 sub-bloques operativos.
> - **Bloque IV — Fuentes Internas GMB Crush usadas** lista los frameworks GMB Crush.

# Bloque I — Introducción

## Objetivo del Paso 18

<small>§2</small>

En este paso la IA **valida el sitio construido en el Paso 17 contra 35 criterios objetivos** antes de publicarlo en Cloudflare Pages. 4 auditorías secuenciales: Técnica (16 criterios) + Contenido (8) + Visual (5) + Rastros IA (6) = 35 totales. Sin 35/35 en verde, no hay deploy. Cada criterio se valida contra su output de origen (no contra criterio del operador). Tras el deploy, se registra el sitemap en Google Search Console.

**Outputs del paso:**

- **18.1** Auditoría Técnica — 16 criterios contrastados contra outputs de Pasos 3, 4, 5, 7, 1, 16
- **18.2** Auditoría de Contenido — 8 criterios contrastados contra Paso 15 + Paso 1.08-1.15 (NAP)
- **18.3** Auditoría Visual — 5 criterios contrastados contra Design Tokens y Layout-Map del Paso 16
- **18.4** Auditoría de Rastros IA — 6 criterios validan Fase 6 del Paso 17
- **18.5** Setup Cloudflare Pages + Dominio + DNS — repositorio conectado, build command, dominio canónico, SSL
- **18.6** Sitio en Producción — verificación post-deploy (sitemap, robots, schemas, responsive, 200 OK)
- **18.7** Sitemap registrado en Google Search Console post-deploy

**Errores que previene:**

- Deploy con criterios en rojo (errores en producción)
- Cloudflare falla la build por stack incompatible (Astro 6, Tailwind v4, npm)
- QA subjetivo (criterios "que se ven bien")
- Saltar registro en GSC (sin discovery automático)
- Sin verificación post-deploy (errores invisibles hasta que un usuario reporta)

**Cuándo se ejecuta:** después de Paso 17 (Constructor) cerrado con build local pasando. Antes de Paso 19 (Escalado post-launch). El Paso 14 (GBP Creation) se ejecuta DESPUÉS del Paso 18.

## Info heredada de pasos anteriores

<small>§3</small>

| Campo | Origen |
|---|---|
| NAP completo (8 campos) | Paso-01 1.4 (1.08-1.15 NAP) + 1.14 teléfono |
| Dominio canónico | Paso-01 1.2 + 1.3 |
| URL Matrix completa | Paso-03 3.5 |
| Canonical tags + URL patterns | Paso-04 4.1 + 4.3-4.8 |
| Page Type Rules + Schemas | Paso-05 5.3-5.9 (5.18 schemas) |
| Internal Linking Map | Paso-07 7.11 |
| Copy redactado por page type (4 capas) | Paso-15 15.3-15.9 |
| Puentes narrativos GA → LBS | Paso-15 15.12 |
| Design Tokens + Layout-Map | Paso-16 16.4 + 16.6 |
| Sitio Astro construido + Fase 6 limpieza IA | Paso-17 17.5 + 17.7 |
| Build local pasando | Paso-17 17.8 |

# Bloque II — Ejemplo rellenado para el Paso 18 — QA y Deploy

<small>§4</small>

> Los 7 outputs del Paso 18 con sus valores reales para Cerrajeros Madrid 24h. Las 4 auditorías están portadas LITERALMENTE del documento fuente original.

### 18.1 — Auditoría Técnica (16 criterios literales)

```text
| # | Elemento                       | Criterio                                                          | Fuente origen          |
|---|--------------------------------|-------------------------------------------------------------------|------------------------|
| 1 | URLs                           | Slugs coinciden con la URL Matrix. Sin 404.                      | Paso 3                 |
| 2 | Canonical                      | Cada página tiene canonical apuntando a su propia URL             | Paso-04 4.1            |
| 3 | Navegación Header              | Menú sigue Paso 7. Teléfono del Paso 1.14.                       | Paso-07 + Paso-01 1.14 |
| 4 | Footer                         | Enlaces a silos del Paso 7. NAP del Paso 1.                       | Paso-07 + Paso-01 1.4  |
| 5 | Páginas huérfanas              | Ninguna página sin enlace entrante en el Internal Linking Map     | Paso-03 + Paso-07      |
| 6 | Meta Tags                      | Title y description únicos por página                             | Paso-05 5.9            |
| 7 | H1                             | Un H1 por página con keyword principal                            | Paso-05 + Paso-15      |
| 8 | Schema Organization + WebSite  | Presente en Homepage                                              | Paso-05 5.9            |
| 9 | Schema LocalBusiness           | Presente en Homepage + LBS + GeoHub con NAP del Paso 1            | Paso-05 + Paso-01 1.4  |
| 10| Schema Service                 | Presente en Service Overview Pages + Additional Category          | Paso-05 5.9            |
| 11| Schema CollectionPage          | Presente en GeoHub                                                | Paso-05 5.9            |
| 12| Schema Article + FAQPage       | Presente en GeoArticles                                           | Paso-05 5.9            |
| 13| Schema BreadcrumbList          | Presente en todas las páginas                                     | Paso-05 5.9            |
| 14| Sitemap                        | Contiene todas las URLs del Paso 3                                | Paso-03 3.5            |
| 15| robots.txt                     | Existe, no bloquea URLs SEO, apunta al sitemap                    | —                      |
| 16| Responsive                     | Sin desbordamientos en 375px / 768px / 1280px                     | Paso-16 (mobile-first) |

Cerrajeros Madrid 24h: 16/16 ✓

Reglas operativas:
- Cada criterio se valida contra su output de origen, no contra el criterio del operador.
- Si un criterio falla, se vuelve al paso correspondiente y se corrige antes de seguir.
- Validar schemas con Schema.org Validator + Google Rich Results Test.
```

### 18.2 — Auditoría de Contenido (8 criterios literales)

```text
| # | Elemento                          | Criterio                                                                       | Fuente origen          |
|---|-----------------------------------|--------------------------------------------------------------------------------|------------------------|
| 1 | Copy Homepage                     | Coincide con las 4 capas del Paso 15 (sub-sección 15.3 Homepage redactada)    | Paso-15 15.3           |
| 2 | Copy Service Overview Pages       | Coincide con las 4 capas del Paso 15 (×S SO redactadas)                       | Paso-15 15.4           |
| 3 | Copy Location-Based Service Pages | Coincide con las 4 capas del Paso 15 (×S LBS redactadas)                      | Paso-15 15.5           |
| 4 | Copy Additional Category          | Coincide con las 4 capas del Paso 15 (A AC redactadas)                        | Paso-15 15.6           |
| 5 | Copy GeoHub                       | Coincide con las 4 capas del Paso 15 (GeoHub redactada)                       | Paso-15 15.7           |
| 6 | Copy GeoArticles                  | Coincide con las 4 capas del Paso 15 (G×S GAs redactados)                     | Paso-15 15.8           |
| 7 | Puentes narrativos GeoArticles    | 3 puntos de transición a la LBS padre con anchors variados                    | Paso-15 15.12          |
| 8 | NAP consistente                   | Mismo NAP en Header, Footer, Contact, schema                                  | Paso-01 1.4            |

Cerrajeros Madrid 24h: 8/8 ✓

Reglas operativas:
- Si el copy en producción difiere del Paso 15, decidir: ¿el copy del Paso 15 estaba mal o el constructor lo modificó?
- Cualquier modificación del copy en el constructor se vuelve al Paso 15 para regenerar la decisión.
- Validar trust signals: ningún claim sin prueba (Paso-15 15.13).
```

### 18.3 — Auditoría Visual (5 criterios literales)

```text
| # | Elemento                  | Criterio                                                                          | Fuente origen      |
|---|---------------------------|-----------------------------------------------------------------------------------|--------------------|
| 1 | Colores                   | Coinciden con Design Tokens del Paso 16                                          | Paso-16 16.4       |
| 2 | Tipografías               | Coinciden con Design Tokens del Paso 16                                          | Paso-16 16.4       |
| 3 | Layout                    | Estructura de secciones sigue Layout-Map del Paso 16 por page type               | Paso-16 16.6       |
| 4 | Jerarquía Homepage        | Servicios Core destacados sobre Additional Category                              | Paso-15 + Paso-16  |
| 5 | GeoHub contenido propio   | No es solo índice de enlaces — tiene contenido propio                            | Paso-15 15.7       |

Cerrajeros Madrid 24h: 5/5 ✓

Reglas operativas:
- Validar contraste WCAG AA en todos los pares texto/fondo.
- Validar comportamiento responsive en 3 breakpoints (375 / 768 / 1280).
- Si un color o tipografía en producción no está en los Design Tokens, volver al Paso 16.
```

### 18.4 — Auditoría de Rastros IA (6 criterios literales)

```text
| # | Elemento              | Criterio                                            |
|---|-----------------------|-----------------------------------------------------|
| 1 | README.md             | No contiene texto del starter kit                   |
| 2 | Comentarios internos  | Sin instrucciones de IA en el código                |
| 3 | meta generator        | No aparece en HTML de producción                    |
| 4 | Referencias a IA      | grep limpio en todo el repositorio                  |
| 5 | package.json          | Nombre del proyecto real                            |
| 6 | Commits               | Sin referencias a IA en mensajes                    |

Cerrajeros Madrid 24h: 6/6 ✓

Reglas operativas:
- Si en QA aparece un rastro nuevo, volver a la Fase 6 del Paso 17.
- El cliente debe poder revisar el repositorio sin ver pruebas de generación automática.
```

### 18.5 — Setup Cloudflare Pages + Dominio + DNS

```text
═══════════════════════════════════════════════════════════════
sección 12.1 — Setup repositorio + Cloudflare
═══════════════════════════════════════════════════════════════
| Acción                                                | Estado | Notas                                          |
|--------------------------------------------------------|--------|------------------------------------------------|
| Crear repositorio remoto (GitHub)                     | ✓      | Repo privado o público según cliente          |
| Conectar repositorio a Cloudflare Pages               | ✓      | Cloudflare Dashboard → Pages → Connect Git    |
| Configurar build command                              | ✓      | `pnpm run build` (NO `npm run build`)         |
| Configurar build output directory                     | ✓      | `dist`                                         |
| Configurar Node version                               | ✓      | Compatible con Astro 5 + pnpm                 |

═══════════════════════════════════════════════════════════════
sección 12.2 — Dominio y DNS
═══════════════════════════════════════════════════════════════
| Acción                                                | Estado | Notas                                          |
|--------------------------------------------------------|--------|------------------------------------------------|
| Conectar dominio del Paso 1.02                        | ✓      | cerrajerosmadrid24h.com (DNS A o CNAME)       |
| Configurar redirección www ↔ apex                     | ✓      | Versión canónica del Paso 1.03                |
| Activar SSL/HTTPS                                     | ✓      | Cloudflare auto-SSL                            |
| Configurar redirects 301 si hay URLs viejas           | N/A    | Si el dominio ya estaba en uso                 |
```

### 18.6 — Sitio en Producción (verificación post-deploy)

```text
═══════════════════════════════════════════════════════════════
sección 12.3 — Verificación post-deploy
═══════════════════════════════════════════════════════════════
| Acción                                                | Estado | Notas                                                          |
|--------------------------------------------------------|--------|----------------------------------------------------------------|
| Sitemap accesible                                     | ✓      | https://[dominio]/sitemap-index.xml carga sin error            |
| robots.txt accesible                                  | ✓      | https://[dominio]/robots.txt carga sin error                   |
| Schemas válidos en producción                         | ✓      | Pasar 3 URLs por Schema.org Validator + Rich Results Test      |
| Responsive en 375 / 768 / 1280                        | ✓      | Verificar en producción, no solo local                         |
| 200 OK en todas las URLs del sitemap                  | ✓      | Crawler que recorre el sitemap entero                          |

Cerrajeros Madrid 24h:
  Dominio: https://www.cerrajerosmadrid24h.com
  Deploy: 2026-04-30T14:30:00Z
  Build: ✓ 29 pages en 18s
  SSL: ✓ Cloudflare auto-SSL
```

### 18.7 — Sitemap registrado en Google Search Console

```text
Reglas operativas para sección 12 (Deploy) — Cloudflare:
  - Antes del primer push, ejecutar `pnpm install && pnpm build` localmente.
  - El stack en Cloudflare debe coincidir con el local: `pnpm run build`, no `npm run build`.
  - Si Cloudflare falla la build, revisar versiones de Astro, Tailwind y pnpm.
  - El sitemap debe registrarse en Google Search Console tras el deploy.

Cerrajeros Madrid 24h:
  GSC Property: https://www.cerrajerosmadrid24h.com (Domain property + URL prefix)
  Verificación: ✓ DNS TXT record (Cloudflare DNS)
  Sitemap: https://www.cerrajerosmadrid24h.com/sitemap-index.xml
    Submitted: 2026-04-30T14:35:00Z
    Status: Success
    Discovered URLs: 29 (esperado 29 ✓)
```

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 18.1 | Auditoría Técnica (16 criterios literales) | 16 criterios contrastados | GMB Crush | Paso-03 + Paso-04 4.1 + Paso-05 5.9 + Paso-07 7.11 + Paso-01 1.4 + Paso-16 |
| 18.2 | Auditoría de Contenido (8 criterios literales) | 8 criterios contrastados | GMB Crush | Paso-15 15.3-15.8 + 15.12 + Paso-01 1.4 |
| 18.3 | Auditoría Visual (5 criterios literales) | 5 criterios contrastados | GMB Crush | Paso-16 16.4 + 16.6 + Paso-15 15.7 |
| 18.4 | Auditoría de Rastros IA (6 criterios literales) | 6 criterios contrastados | GMB Crush | Paso-17 17.7 |
| 18.5 | Setup Cloudflare Pages + Dominio + DNS | Configuración tracked | Decisión de diseño | Paso-01 1.2 + Paso-04 4.1 |
| 18.6 | Sitio en Producción (verificación post-deploy) | Verificación tracked | GMB Crush | Paso-18 18.1-18.5 (intra-paso) |
| 18.7 | Sitemap registrado en GSC | Registro completado | GMB Crush | Paso-18 18.6 (intra-paso) |

## Obtención de Outputs

<small>§6</small>

### 18.1 — Auditoría Técnica

<small>§6.1</small>

**Explicación**

16 criterios técnicos del original, cada uno contrastado contra su output de origen (no contra criterio del operador). Si un criterio falla, BLOCK + corregir en el paso correspondiente + reintentar QA.

**Patrón o fórmula**

```text
16 criterios literales del original (§7):
  URLs / Canonical / Header / Footer / Páginas huérfanas /
  Meta Tags / H1 / Schemas Org+WebSite / LocalBusiness / Service /
  CollectionPage / Article+FAQPage / BreadcrumbList /
  Sitemap / robots.txt / Responsive
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.1 — 16/16 ✓.

**Ejemplos incorrectos**

```text
- Inventar criterios fuera del catálogo doctrinal (Lighthouse, Core Web Vitals, hreflang, etc.)
- Validar contra criterio del operador en lugar del output de origen
- Saltar criterios "que no aplican" (rompe gate doctrinal)
- Schemas sin validar contra Schema.org Validator + Rich Results Test
```

**Regla final**

```text
16/16 criterios literales del original deben estar en ✓ antes de proceder a 18.5.
```

**Validación operativa**

Aplicar los 16 criterios fila a fila contra su output de origen.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** 16 checks individuales con tools (Schema.org Validator, Rich Results Test, manual responsive en 3 breakpoints, crawler para 404s).

**Output del paso**

- **Tipo:** Auditoría documentada.
- **Ejemplo (Cerrajeros Madrid 24h):** 16/16 criterios pasados.

### 18.2 — Auditoría de Contenido

<small>§6.2</small>

**Explicación**

8 criterios del original que validan que el copy en producción coincide LITERAL con el redactado en Paso 15 (4 capas), más NAP consistente.

**Patrón o fórmula**

```text
8 criterios literales del original (§8):
  Copy de los 6 page types coincide con Paso-15 (cada page type)
  + Puentes narrativos GA → LBS con 3 puntos + anchors variados
  + NAP consistente entre Header, Footer, Contact, schema
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.2 — 8/8 ✓.

**Ejemplos incorrectos**

```text
- Copy en producción modificado por constructor sin volver a Paso 15
- NAP distinto entre Header y schema
- Puentes narrativos GA con < 3 puntos a LBS padre
- Trust signals con claims sin prueba (rompe Paso-15 15.13)
```

**Regla final**

```text
8/8 criterios literales deben estar en ✓.
```

**Validación operativa**

Inspección manual + cruce con Paso-15 15.3-15.8 y 15.12 + Paso-01 1.4.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspección manual de las 29 páginas + grep para detectar inconsistencias NAP + verificación 3 puntos GA→LBS.

**Output del paso**

- **Tipo:** Auditoría documentada.
- **Ejemplo (Cerrajeros Madrid 24h):** 8/8 criterios pasados.

### 18.3 — Auditoría Visual

<small>§6.3</small>

**Explicación**

5 criterios del original que validan que la implementación visual coincide con Design Tokens y Layout-Map del Paso 16.

**Patrón o fórmula**

```text
5 criterios literales del original (§9):
  Colores Design Tokens / Tipografías Design Tokens / Layout Layout-Map /
  Jerarquía Homepage (Servicios Core sobre Additional Category) /
  GeoHub contenido propio (no solo índice)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.3 — 5/5 ✓.

**Ejemplos incorrectos**

```text
- Página con colores fuera de paleta del Paso-16 16.4
- Layout divergente del Paso-16 16.6
- Servicios Core no destacados sobre Additional Category en HP
- GeoHub que es solo lista de enlaces sin contenido propio
- WCAG AA contraste no validado
```

**Regla final**

```text
5/5 criterios literales deben estar en ✓.
```

**Validación operativa**

Inspección visual de 29 páginas + cruce con Paso-16 16.4 + 16.6 + Paso-15 15.7.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspección visual + WCAG AA contrast check + responsive en 3 breakpoints.

**Output del paso**

- **Tipo:** Auditoría documentada.
- **Ejemplo (Cerrajeros Madrid 24h):** 5/5 criterios pasados.

### 18.4 — Auditoría de Rastros IA

<small>§6.4</small>

**Explicación**

6 criterios del original que verifican que la Fase 6 del Paso 17 se aplicó correctamente. Sin rastros IA visibles en producción.

**Patrón o fórmula**

```text
6 criterios literales del original (sección 10):
  README.md sin texto starter kit /
  Comentarios sin instrucciones IA /
  meta generator no aparece /
  grep limpio en repositorio /
  package.json con nombre real /
  Commits sin referencias a IA
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.4 — 6/6 ✓.

**Ejemplos incorrectos**

```text
- README "Generated by AI" en producción
- Comentarios "// AI-generated" en src/
- meta generator visible en HTML
- grep -ri "AI\|Claude\|ChatGPT" → matches
```

**Regla final**

```text
6/6 criterios literales deben estar en ✓. Si rastro nuevo aparece, volver a Fase 6 del Paso 17.
```

**Validación operativa**

`grep -ri` con keywords IA → 0 matches + inspección README + package.json + git log.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** grep + inspección manual.

**Output del paso**

- **Tipo:** Auditoría documentada.
- **Ejemplo (Cerrajeros Madrid 24h):** 6/6 criterios pasados.

### 18.5 — Setup Cloudflare Pages + Dominio + DNS

<small>§6.5</small>

**Explicación**

Setup completo del deploy en Cloudflare Pages: repositorio + build command + output dir + Node version + dominio + SSL + redirects. Sigue protocolo del original sección 12.1 + sección 12.2.

**Patrón o fórmula**

```text
sección 12.1 Setup:
  Crear repo GitHub + Connect Cloudflare Pages + build command (pnpm run build) +
  output dir (dist) + Node version compatible con Astro 5 + pnpm

sección 12.2 Dominio y DNS:
  Conectar dominio Paso-01 1.2 + redirección www ↔ apex (canónica Paso-01 1.3) +
  Cloudflare auto-SSL + redirects 301 si aplica
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.5.

**Ejemplos incorrectos**

```text
- Build command "npm run build" en lugar de "pnpm run build" (rompe stack)
- Sin redirección www ↔ apex (rompe canónica)
- SSL Flexible (rompe seguridad; debe ser auto-SSL completo)
- Sin Node version compatible con Astro 5
```

**Regla final**

```text
Setup completo Cloudflare + Dominio + DNS antes de proceder a 18.6.
```

**Validación operativa**

Verificar que `pnpm install && pnpm build` pasa en local antes del primer push (Paso-17 17.8).

**Cómo se obtiene**

- **Fuente:** Decisión de diseño.
- **Método:** Cloudflare Dashboard + DNS records + GitHub integration.

**Output del paso**

- **Tipo:** Configuración tracked.
- **Ejemplo (Cerrajeros Madrid 24h):** Cloudflare Pages activo en cerrajerosmadrid24h.com con SSL.

### 18.6 — Sitio en Producción (verificación post-deploy)

<small>§6.6</small>

**Explicación**

Verificación post-deploy con 5 checks: sitemap accesible + robots accesible + schemas válidos + responsive + 200 OK en todas las URLs. Sigue protocolo del original sección 12.3.

**Patrón o fórmula**

```text
5 checks post-deploy (sección 12.3):
  Sitemap-index.xml accesible
  robots.txt accesible
  Schemas válidos en producción (3 URLs por Schema.org Validator + Rich Results Test)
  Responsive en 375 / 768 / 1280 (en producción, no solo local)
  200 OK en todas las URLs del sitemap (crawler completo)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.6.

**Ejemplos incorrectos**

```text
- Deploy sin verificación post-deploy
- Sitemap inaccesible (URL no carga)
- 404s en producción (URLs declaradas no accesibles)
- Schemas válidos en local pero rotos en producción (problema de SSR)
```

**Regla final**

```text
5/5 checks post-deploy en ✓ antes de marcar 18.6 como confirmed.
```

**Validación operativa**

Crawler que recorre sitemap entero + verificar 200 OK en todas + schemas con tools.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Verificación post-deploy con 5 checks.

**Output del paso**

- **Tipo:** Verificación tracked.
- **Ejemplo (Cerrajeros Madrid 24h):** 5/5 checks pasados; sitio LIVE.

### 18.7 — Sitemap registrado en GSC

<small>§6.7</small>

**Explicación**

Registro del sitemap.xml en Google Search Console post-deploy. Activa el discovery de URLs por Google. Cumple regla operativa de la sección 12 del documento fuente: "El sitemap debe registrarse en Google Search Console tras el deploy."

**Patrón o fórmula**

```text
1. Verificar property en GSC (DNS TXT o URL prefix)
2. Submit sitemap.xml (sitemap-index.xml según Astro)
3. Verificar Discovered URLs = N+1 esperadas
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.7 — Sitemap submitted Success; 29 URLs discovered.

**Ejemplos incorrectos**

```text
- Saltar registro GSC (sin discovery automático)
- Sitemap con URLs no canonicales
- GSC sin verificar (no recibe data)
```

**Regla final**

```text
Sitemap registrado + Discovered URLs = N+1 esperadas. Si no, BLOCK.
```

**Validación operativa**

GSC dashboard muestra "Success" en sitemap status + Discovered URLs igual a N+1.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** GSC dashboard + DNS TXT verification + submit sitemap.

**Output del paso**

- **Tipo:** Registro completado.
- **Ejemplo (Cerrajeros Madrid 24h):** Sitemap status Success; 29/29 URLs discovered.

## Checklist Final

<small>§7</small>

> Validación operativa antes de marcar Paso 18 como cerrado.

### Validación de las 4 auditorías (35 criterios totales)

- ☐ Auditoría Técnica 16/16 ✓ (18.1)
- ☐ Auditoría de Contenido 8/8 ✓ (18.2)
- ☐ Auditoría Visual 5/5 ✓ (18.3)
- ☐ Auditoría de Rastros IA 6/6 ✓ (18.4)
- ☐ TOTAL: 35/35 criterios en verde

### Validación de Deploy

- ☐ Setup Cloudflare + Dominio + DNS aplicado (18.5)
- ☐ Sitio en producción con verificación post-deploy 5/5 (18.6)
- ☐ Sitemap registrado en GSC con N+1 URLs discovered (18.7)

## Outputs Consolidados

<small>§8</small>

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 18.1 | ← Paso-03 + Paso-04 4.1 + Paso-05 5.9 + Paso-07 + Paso-01 1.4 + Paso-16 | **Auditoría Técnica** = 16/16 criterios literales del original | 16 checks individuales con tools (Schema.org, Rich Results Test, responsive 3 breakpoints, crawler 404s). **Fuente:** GMB Crush. | confirmed |
| 18.2 | ← Paso-15 15.3-15.8 + 15.12 + Paso-01 1.4 | **Auditoría de Contenido** = 8/8 criterios literales del original | Inspección manual + grep + cruce con Paso-15 + verificación 3 puntos GA→LBS. **Fuente:** GMB Crush. | confirmed |
| 18.3 | ← Paso-16 16.4 + 16.6 + Paso-15 15.7 | **Auditoría Visual** = 5/5 criterios literales del original | Inspección visual + WCAG AA contrast + responsive 3 breakpoints. **Fuente:** GMB Crush. | confirmed |
| 18.4 | ← Paso-17 17.7 | **Auditoría de Rastros IA** = 6/6 criterios literales del original | grep + inspección README + package.json + git log. **Fuente:** GMB Crush. | confirmed |
| 18.5 | ← Paso-01 1.2 + Paso-04 4.1 | **Setup Cloudflare + Dominio + DNS** = repo conectado + pnpm run build + dist + dominio canónico + SSL | Cloudflare Dashboard + DNS records + GitHub integration. **Fuente:** Decisión de diseño. | confirmed |
| 18.6 | ← 18.1-18.5 | **Sitio en Producción** = 5/5 checks post-deploy (sitemap + robots + schemas + responsive + 200 OK) | Crawler sitemap + verificar 200 OK + schemas con tools. **Fuente:** GMB Crush. | confirmed |
| 18.7 | ← 18.6 | **Sitemap registrado en GSC** = Submitted Success; N+1 URLs discovered | GSC dashboard + DNS TXT verification + submit sitemap. **Fuente:** GMB Crush. | confirmed |

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
- QA + Deploy Framework GMB Crush (35 criterios literales + Cloudflare protocol)

> **Nota — QA gate doctrinal y criterios literales:**
> Los 35 criterios (16 + 8 + 5 + 6) están portados **literalmente** del documento fuente original (secciones 7 Técnica, 8 Contenido, 9 Visual, 10 Rastros IA). No se inventan criterios fuera de este catálogo. El protocolo de Deploy (sección 12.1 Setup, sección 12.2 Dominio, sección 12.3 Verificación) también es literal.
>
> Cada criterio se valida contra su output de origen — no contra criterio del operador. Si un criterio falla, BLOCK + corregir en el paso de origen + reintentar QA. Solo tras 35/35 ✓ + sitio LIVE + sitemap en GSC se cierra el Paso 18.
