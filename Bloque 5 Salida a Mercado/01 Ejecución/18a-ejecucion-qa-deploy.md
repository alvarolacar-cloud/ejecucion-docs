Versión literal del chat · Sistema GMB Crush para webs locales
Documento generado siguiendo el esqueleto canónico (`00 convenciones/00-esqueleto-paso-a.md`).
Proveniencia: portado de `repos-1-y-2/Bloque 5 — Salida a Mercado/paso-18-qa-deploy/`, alineado con los frameworks oficiales GMB Crush.

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

En este paso la IA **valida el sitio contra 35 criterios objetivos** antes de desplegarlo a producción en Cloudflare Pages. 4 auditorías secuenciales (Técnica 16 / Contenido 8 / Visual 5 / Rastros IA 6 = 35 criterios totales). Si cualquiera falla, BLOCK + corregir en el paso de origen + reintentar QA. Tras el deploy, registra sitemap en Google Search Console.

**Outputs del paso:**

- **18.1** Auditoría Técnica — 16 criterios verificados (URLs, canonical, schemas, sitemap, responsive)
- **18.2** Auditoría de Contenido — 8 criterios verificados (copy por page type, NAP consistente)
- **18.3** Auditoría Visual — 5 criterios verificados (Design Tokens, Layout-Map, jerarquía)
- **18.4** Auditoría de Rastros IA — 6 criterios verificados (README limpio, sin meta generator, grep sin IA)
- **18.5** Configuración Cloudflare — `deploy-config.md` con build command, dominio, SSL, redirects
- **18.6** Sitio en Producción — web publicada en dominio activo con HTTPS
- **18.7** Sitemap en GSC — sitemap registrado en Google Search Console post-deploy

**Errores que previene:**

- Deploy con auditorías incompletas (errores en producción)
- Configuración Cloudflare ad-hoc sin documento (no replicable)
- Saltar registro en GSC (sin discovery de URLs)
- HTTPS roto o certificado SSL inválido
- Sitemap sin URLs canonicales
- 404s en URLs declaradas en URL Matrix

**Cuándo se ejecuta:** después de Paso 17 (Constructor) cerrado con build local pasando. Antes de Paso 19 (Escalado post-launch). El Paso 14 (GBP Creation) se ejecuta DESPUÉS del Paso 18.

## Info heredada de pasos anteriores

<small>§3</small>

| Campo | Origen |
|---|---|
| NAP + dominio + GBP Status web-first | Paso-01 1.2 + 1.3 + 1.4 |
| URL Matrix completa | Paso-03 3.5 |
| Canonical tags + URL patterns | Paso-04 4.1 + 4.3-4.8 |
| Meta tags + H1 + schemas | Paso-05 5.3-5.9 |
| Internal Linking Map | Paso-07 7.11 |
| Copy por page type (4 capas) | Paso-15 15.3-15.9 |
| Design Tokens + Layout-Map | Paso-16 16.4 + 16.6 |
| Sitio Astro construido + Fase 6 limpieza IA | Paso-17 17.5 + 17.7 |
| Build local pasando | Paso-17 17.8 |

# Bloque II — Ejemplo rellenado para el Paso 18 — QA y Deploy

<small>§4</small>

> Los 7 outputs del Paso 18 con sus valores reales para Cerrajeros Madrid 24h.

### 18.1 — Auditoría Técnica (16 criterios)

```text
1. ✓ URLs canónicas en todas las páginas (matching URL Matrix)
2. ✓ Canonical tag presente en <head> de cada página
3. ✓ HTTPS activo (Cloudflare SSL)
4. ✓ Sitemap.xml presente en /sitemap.xml con 29 URLs
5. ✓ Robots.txt presente en /robots.txt (Allow: /)
6. ✓ Schemas válidos (Google Rich Results Test 29/29 Pass)
7. ✓ Internal links sin 404s (88 enlaces validados)
8. ✓ External links con rel="noopener" donde aplique
9. ✓ Imágenes con alt text descriptivo
10. ✓ Lazy loading en imágenes below-the-fold
11. ✓ Responsive: 320px (mobile S) / 768px (tablet) / 1024px+ (desktop)
12. ✓ Lighthouse Performance ≥ 90 (mobile + desktop)
13. ✓ Lighthouse SEO ≥ 95 (mobile + desktop)
14. ✓ Lighthouse Accessibility ≥ 90
15. ✓ Core Web Vitals: LCP < 2.5s, CLS < 0.1, FID < 100ms
16. ✓ Hreflang AUSENTE (cluster mono-idioma)

Total: 16/16 ✓
```

### 18.2 — Auditoría de Contenido (8 criterios)

```text
1. ✓ Copy presente en las 29 páginas (sin lorem ipsum)
2. ✓ Copy alineado con Paso-15 15.3-15.9 (cluster completo redactado)
3. ✓ NAP consistente (igual en HP, footer, schema, /contacto/)
4. ✓ Word count en rango doctrinal por page type (Paso-05 5.10)
5. ✓ Las 4 capas aplicadas (Estructura/Zonas/Argumentos/Entidades)
6. ✓ Las 4 reglas universales aplicadas (Hero+CTA / Problema / Datos / Local)
7. ✓ Contexto local en LBS, AC, GH, GA (LCAs naturales)
8. ✓ Sin reseñas Google inventadas (web-first; cumple Paso-09 9.8)

Total: 8/8 ✓
```

### 18.3 — Auditoría Visual (5 criterios)

```text
1. ✓ Design Tokens aplicados sin desviación (tailwind.config = Paso-16 16.4)
2. ✓ Layout-Map cumplido en las 29 páginas (Paso-16 16.6)
3. ✓ Jerarquía visual coherente (H1 > H2 > H3 sin saltos arbitrarios)
4. ✓ Colores consistentes (primary #C8102E en todos los CTAs primary)
5. ✓ Phone banner mobile fixed-bottom presente (cliente aprobó en Paso-16 16.3)

Total: 5/5 ✓
```

### 18.4 — Auditoría de Rastros IA (6 criterios)

```text
1. ✓ README.md limpio (0 menciones a IA/Claude/GPT/Anthropic/OpenAI)
2. ✓ Comentarios en src/ sin referencias IA (grep -r → 0 matches)
3. ✓ <meta name="generator"> AUSENTE en HTML producción
4. ✓ package.json con name + author humanos (no "ai-generated-*")
5. ✓ pnpm-lock.yaml limpio sin packages añadidos por error
6. ✓ Commits git en main sin "Co-Authored-By: Claude"

Total: 6/6 ✓
```

### 18.5 — Configuración Cloudflare (deploy-config.md)

```yaml
# deploy-config.md

# Cloudflare Pages — Cerrajeros Madrid 24h
project_name: cerrajeros-madrid-24h
production_branch: main
build_command: pnpm build
output_directory: dist
build_environment_variables:
  NODE_VERSION: 20
  PNPM_VERSION: 9

# Custom domain
domain: www.cerrajerosmadrid24h.com
ssl: Universal SSL (auto)
ssl_mode: Full (strict)

# DNS records (en Cloudflare DNS):
# A     @     cloudflare-pages-IP   (proxied)
# CNAME www   cerrajeros-madrid-24h.pages.dev   (proxied)
# TXT   @     v=spf1 ...   (si email del dominio)

# Redirects:
redirects:
  - source: /home
    target: /
    status: 301
  - source: /index
    target: /
    status: 301
  - source: /cerrajero
    target: /cerrajero/cerrajero-urgente/
    status: 301

# Headers:
headers:
  /*: 
    X-Content-Type-Options: nosniff
    X-Frame-Options: SAMEORIGIN
    Referrer-Policy: strict-origin-when-cross-origin
```

### 18.6 — Sitio en Producción

```text
Deploy ejecutado:
  Repo: github.com/[user]/cerrajeros-madrid-24h
  Branch: main
  Build: ✓ 29 pages built en 18s
  Deploy: ✓ Cloudflare Pages production
  Dominio: https://www.cerrajerosmadrid24h.com
  SSL: ✓ Universal SSL (HSTS preload pendiente Phase 4)

Verificación post-deploy:
  ✓ HTTPS activo en todas las URLs
  ✓ www.cerrajerosmadrid24h.com → resuelve correctamente
  ✓ cerrajerosmadrid24h.com (sin www) → 301 a www.
  ✓ /sitemap.xml accesible (29 URLs)
  ✓ /robots.txt accesible (Allow: /)
  ✓ 0 404s en links internos del cluster
  ✓ Lighthouse desktop: P 92 / SEO 100 / A 95 / BP 100
  ✓ Lighthouse mobile:  P 89 / SEO 100 / A 92 / BP 100

Deploy timestamp: 2026-04-30T14:30:00Z
```

### 18.7 — Sitemap en GSC

```text
Google Search Console — Cerrajeros Madrid 24h:
  Property: https://www.cerrajerosmadrid24h.com (Domain property + URL prefix)
  Verificación: ✓ DNS TXT record (Cloudflare DNS)
  Sitemap: https://www.cerrajerosmadrid24h.com/sitemap.xml
    Submitted: 2026-04-30T14:35:00Z
    Status: Success
    Discovered URLs: 29 (esperado: 29 ✓)

Configuración adicional:
  - GA4 vinculado a GSC ✓
  - Bing Webmaster Tools opcional (pendiente)
```

# Bloque III — Ejecución por la IA

## Outputs a Conseguir

<small>§5</small>

| ID | Output | Tipo | Fuente | Hereda de |
|---|---|---|---|---|
| 18.1 | Auditoría Técnica | 16 criterios verificados | GMB Crush | Paso-04 4.1 + Paso-05 5.9 + Paso-17 17.5-17.6 |
| 18.2 | Auditoría de Contenido | 8 criterios verificados | GMB Crush | Paso-15 15.3-15.13 + Paso-09 9.4 + 9.8 |
| 18.3 | Auditoría Visual | 5 criterios verificados | GMB Crush | Paso-16 16.4 + 16.6 |
| 18.4 | Auditoría de Rastros IA | 6 criterios verificados | GMB Crush | Paso-17 17.7 |
| 18.5 | Configuración Cloudflare | deploy-config.md | Decisión de diseño | Paso-01 1.2 + Paso-04 4.1 |
| 18.6 | Sitio en Producción | Web publicada activa | GMB Crush | Paso-18 18.1-18.5 (intra-paso) |
| 18.7 | Sitemap en GSC | Registro completado | GMB Crush | Paso-18 18.6 (intra-paso) |

## Obtención de Outputs

<small>§6</small>

### 18.1 — Auditoría Técnica

<small>§6.1</small>

**Explicación**

16 criterios técnicos que aseguran que el sitio cumple estándares SEO + Performance + Accessibility antes de ir a producción.

**Patrón o fórmula**

```text
16 criterios:
  URLs canónicas / Canonical tag / HTTPS / Sitemap / Robots /
  Schemas / Links sin 404 / External rel / Alt text / Lazy load /
  Responsive / Lighthouse P/SEO/A / Core Web Vitals / Hreflang
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.1 — 16/16 ✓.

**Ejemplos incorrectos**

```text
- Saltar criterios "que no aplican" (rompe gate doctrinal)
- Lighthouse < 90 ignorado ("ya optimizamos después")
- Schemas sin validar contra Google Rich Results Test
- 404s en internal links no resueltos
```

**Regla final**

```text
16/16 criterios deben estar en ✓ antes de proceder a 18.5 (deploy config).
```

**Validación operativa**

Ejecutar Lighthouse + Google Rich Results Test + grep links + responsive test manual.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** 16 checks individuales con tools (Lighthouse, GRT, manual responsive).

**Output del paso**

- **Tipo:** Auditoría documentada.
- **Ejemplo (Cerrajeros Madrid 24h):** 16/16 criterios pasados.

### 18.2 — Auditoría de Contenido

<small>§6.2</small>

**Explicación**

8 criterios que validan que el copy redactado en Paso-15 está intacto en producción y cumple las reglas web-first.

**Patrón o fórmula**

```text
8 criterios:
  Copy presente / Alineado Paso-15 / NAP consistente / Word count /
  4 capas aplicadas / 4 reglas universales / Contexto local / Sin reseñas inventadas
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.2 — 8/8 ✓.

**Ejemplos incorrectos**

```text
- Lorem ipsum en alguna página
- NAP distinto entre HP y footer
- Word count fuera de rango doctrinal
- Reseñas Google afirmadas (rompe web-first)
```

**Regla final**

```text
8/8 criterios deben estar en ✓.
```

**Validación operativa**

QA manual + cruce con Paso-15 + Paso-01 1.4.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspección manual + grep para detectar lorem ipsum / inconsistencias NAP.

**Output del paso**

- **Tipo:** Auditoría documentada.
- **Ejemplo (Cerrajeros Madrid 24h):** 8/8 criterios pasados.

### 18.3 — Auditoría Visual

<small>§6.3</small>

**Explicación**

5 criterios que validan que la implementación visual coincide con los Design Tokens y Layout-Map del Paso-16.

**Patrón o fórmula**

```text
5 criterios:
  Design Tokens / Layout-Map cumplido / Jerarquía visual /
  Colores consistentes / Phone banner mobile (si aprobado por cliente)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.3 — 5/5 ✓.

**Ejemplos incorrectos**

```text
- Página con colores fuera de paleta (rompe tokens)
- Layout divergente del Paso-16 16.6
- H1 en H3 styling (rompe jerarquía)
- Phone banner ausente en mobile (cliente aprobó en 16.3)
```

**Regla final**

```text
5/5 criterios deben estar en ✓.
```

**Validación operativa**

Inspección visual + cruce con Paso-16 16.4 + 16.6.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Inspección visual de las 29 páginas + cruce con Layout-Map y tokens.

**Output del paso**

- **Tipo:** Auditoría documentada.
- **Ejemplo (Cerrajeros Madrid 24h):** 5/5 criterios pasados.

### 18.4 — Auditoría de Rastros IA

<small>§6.4</small>

**Explicación**

6 criterios que verifican que la Fase 6 del Paso-17 se aplicó correctamente. Sin rastros IA visibles en producción.

**Patrón o fórmula**

```text
6 criterios:
  README limpio / Comentarios sin IA / Meta generator ausente /
  package.json humano / pnpm-lock limpio / Commits git sin IA
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.4 — 6/6 ✓.

**Ejemplos incorrectos**

```text
- README "Generated by Claude" en GitHub público
- Comentario "// AI-generated" en src/
- meta generator visible en source HTML
- Commits "Co-Authored-By Claude" en branch main
```

**Regla final**

```text
6/6 criterios deben estar en ✓. grep verifica.
```

**Validación operativa**

`grep -ri "AI\|Claude\|ChatGPT\|GPT\|Anthropic\|OpenAI"` → 0 matches.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** grep + inspección README + package.json + git log.

**Output del paso**

- **Tipo:** Auditoría documentada.
- **Ejemplo (Cerrajeros Madrid 24h):** 6/6 criterios pasados; 0 matches en grep.

### 18.5 — Configuración Cloudflare

<small>§6.5</small>

**Explicación**

Documento `deploy-config.md` que contiene toda la configuración de Cloudflare Pages: build command, dominio, SSL, redirects, headers, DNS.

**Patrón o fórmula**

```yaml
project_name + production_branch + build_command + output_directory +
custom_domain + ssl + DNS records + redirects + headers
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.5.

**Ejemplos incorrectos**

```text
- Configuración ad-hoc sin documento (no replicable)
- SSL Flexible (no Strict; rompe seguridad)
- Sin redirects 301 para variantes URL (rompe SEO)
- DNS sin proxied (rompe Cloudflare protección)
```

**Regla final**

```text
deploy-config.md como source-of-truth de la configuración Cloudflare.
```

**Validación operativa**

Aplicar config a Cloudflare + verificar SSL + redirects.

**Cómo se obtiene**

- **Fuente:** Decisión de diseño.
- **Método:** Crear deploy-config.md + aplicar config en Cloudflare dashboard.

**Output del paso**

- **Tipo:** Documento de configuración.
- **Ejemplo (Cerrajeros Madrid 24h):** deploy-config.md con 6 secciones.

### 18.6 — Sitio en Producción

<small>§6.6</small>

**Explicación**

Deploy ejecutado en Cloudflare Pages. Sitio accesible en dominio canónico con HTTPS activo.

**Patrón o fórmula**

```text
git push origin main → Cloudflare Pages auto-deploy →
verificar dominio + HTTPS + URLs + sitemap + Lighthouse
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.6 — deploy 2026-04-30T14:30:00Z.

**Ejemplos incorrectos**

```text
- Deploy sin verificación post-deploy
- HTTPS roto (mixed content warnings)
- Lighthouse < 90 en producción (degraded performance)
- 404s en producción (URLs declaradas no accesibles)
```

**Regla final**

```text
Sitio publicado + HTTPS + 0 404s + Lighthouse ≥ 90 antes de marcar 18.6 como confirmed.
```

**Validación operativa**

Verificación post-deploy con Lighthouse + manual URL check.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** Push a main + auto-deploy + verificación.

**Output del paso**

- **Tipo:** Web publicada.
- **Ejemplo (Cerrajeros Madrid 24h):** https://www.cerrajerosmadrid24h.com activo.

### 18.7 — Sitemap en GSC

<small>§6.7</small>

**Explicación**

Registro del sitemap.xml en Google Search Console post-deploy. Activa el discovery de URLs por Google.

**Patrón o fórmula**

```text
1. Verificar property en GSC (DNS TXT o URL prefix)
2. Submit sitemap.xml
3. Verificar Discovered URLs = N+1 esperadas
4. Vincular GA4 (opcional pero recomendado)
```

**Ejemplo correcto con Cerrajeros Madrid 24h**

Ver §4 sub-sección 18.7 — Sitemap submitted 2026-04-30T14:35:00Z; 29 URLs discovered.

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

GSC dashboard muestra "Success" en sitemap status.

**Cómo se obtiene**

- **Fuente:** GMB Crush.
- **Método:** GSC dashboard + DNS TXT verification + submit sitemap.

**Output del paso**

- **Tipo:** Registro completado.
- **Ejemplo (Cerrajeros Madrid 24h):** Sitemap status Success; 29/29 URLs discovered.

## Checklist Final

<small>§7</small>

- ☐ Auditoría Técnica 16/16 ✓ (18.1)
- ☐ Auditoría de Contenido 8/8 ✓ (18.2)
- ☐ Auditoría Visual 5/5 ✓ (18.3)
- ☐ Auditoría de Rastros IA 6/6 ✓ (18.4)
- ☐ Configuración Cloudflare aplicada (18.5)
- ☐ Sitio en producción con HTTPS + Lighthouse ≥ 90 (18.6)
- ☐ Sitemap registrado en GSC con N+1 URLs discovered (18.7)
- ☐ TOTAL: 35/35 criterios + deploy + sitemap = paso 18 cerrado

## Outputs Consolidados

<small>§8</small>

| ID | Hereda de | Output y valor (Cerrajeros Madrid 24h) | Cómo se obtiene + Fuente | Status |
|---|---|---|---|---|
| 18.1 | ← Paso-04 4.1 + Paso-05 5.9 + Paso-17 17.5-17.6 | **Auditoría Técnica** = 16/16 criterios pasados | 16 checks individuales con tools (Lighthouse, GRT, manual responsive). **Fuente:** GMB Crush. | confirmed |
| 18.2 | ← Paso-15 15.3-15.13 + Paso-09 9.4 + 9.8 | **Auditoría de Contenido** = 8/8 criterios pasados | Inspección manual + grep + cruce con Paso-15 + Paso-01 1.4. **Fuente:** GMB Crush. | confirmed |
| 18.3 | ← Paso-16 16.4 + 16.6 | **Auditoría Visual** = 5/5 criterios pasados | Inspección visual de 29 páginas + cruce con Layout-Map y tokens. **Fuente:** GMB Crush. | confirmed |
| 18.4 | ← Paso-17 17.7 | **Auditoría de Rastros IA** = 6/6 criterios pasados; grep 0 matches | grep + inspección README + package.json + git log. **Fuente:** GMB Crush. | confirmed |
| 18.5 | ← Paso-01 1.2 + Paso-04 4.1 | **Configuración Cloudflare** = deploy-config.md con 6 secciones | Crear deploy-config.md + aplicar config en Cloudflare dashboard. **Fuente:** Decisión de diseño. | confirmed |
| 18.6 | ← 18.1-18.5 | **Sitio en Producción** = https://www.cerrajerosmadrid24h.com activo + Lighthouse ≥ 90 | Push a main + Cloudflare auto-deploy + verificación post-deploy. **Fuente:** GMB Crush. | confirmed |
| 18.7 | ← 18.6 | **Sitemap en GSC** = sitemap submitted Success; 29/29 URLs discovered | GSC dashboard + DNS TXT verification + submit sitemap. **Fuente:** GMB Crush. | confirmed |

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
- QA Deploy Framework GMB Crush (35 criterios + Cloudflare config)

> **Nota — QA gate doctrinal:**
> Los 35 criterios son no-negociables. Si un criterio falla, BLOCK + corregir en el paso de origen + reintentar QA. El operador NO puede saltar criterios por urgencia comercial. Solo tras 35/35 ✓ + sitio en producción + sitemap registrado se cierra el Paso 18.
