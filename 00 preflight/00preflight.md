# 00 Preflight — Input humano mínimo

> Este documento contiene los **5 únicos inputs** que el operador entrega antes de que la IA ejecute el sistema. Todo lo demás lo infiere la IA aplicando la doctrina, el análisis competitivo (Local Pack) y las reglas de cada paso.

---

## 1. Nombre del negocio

<!-- ej. Cerrajeros Madrid 24h -->


## 2. Qué hace (descripción corta del servicio)

<!-- ej. cerrajería urgente y apertura de puertas en domicilios y oficinas -->


## 3. Dirección con código postal

<!-- ej. Calle Rafael Calvo 12, Barrio Almagro, Distrito Chamberí, 28010 Madrid -->

> Si el negocio es móvil sin dirección física, declarar `Servicio móvil — Main City: [ciudad]`. La IA infiere Main City desde aquí.


## 4. Estado del GBP

- [ ] Not Created (default web-first)
- [ ] Created (sin verificar)
- [ ] Verified
- [ ] Pending Verification


## 5. Ciudades donde analizar competidores

<!-- ej. Madrid -->

> Una o varias. La IA usa estas ciudades como base del Local Pack analysis para extraer Primary Category, servicios core, categorías adicionales, Candidate LCAs y trust signals.

---

## Lo que la IA infiere a partir de aquí

| Concepto | Cómo lo infiere |
|---|---|
| Servicios core (S=5) | Top 5 frecuencia en Local Pack de las ciudades del campo 5 |
| Planned Primary GBP Category | Categoría más repetida en Local Pack top |
| Planned Additional Categories | Secundarias frecuentes en competidores |
| Main City | Extraída del campo 3 (ciudad de la dirección) |
| Direct Local Coverage Areas | Barrio + distrito del campo 3 |
| Candidate Local Coverage Areas | Áreas declaradas por 2+ competidores top |
| GBP Creation Timing / Verification / URL | Defaults web-first según campo 4 |
| Slugs (Primary, Main City, Services, Additional) | Slugify aplicado a cada nombre |
| GeoHub URL Style | Default `/city/` salvo razón explícita |
| GeoArticles per Service (G) | Default 3 (doctrina) |
| Domain canónico | Slugify(nombre).com — propuesto, pendiente confirmar |
| Teléfono / Email | Placeholder pendiente que cliente confirme |
| Trust signals | Estándar del sector + diferenciadores extraídos de competidores |
| CTA preferido | Default según urgencia del servicio |
| Approved Expansion Areas | None en Phase 1 (default) |
| Default Page Status | Planned (default) |
| Default Priority | Por tipo de página según doctrina |

---

> **Cuando los 5 campos estén rellenos, la IA puede arrancar Paso 1 → 2 → 3 sin pedir nada más al humano.**
