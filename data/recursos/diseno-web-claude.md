> *El error más común al usar Claude para diseño: pedirle que construya una página sin darle referencia visual. El resultado siempre es genérico. Con tres recursos concretos — estilos, animaciones y video de fondo — el resultado cambia completamente.*

:::callout
  **Ideal para**

  - Founders que quieren páginas que se vean profesionales
  - Creadores que usan Claude para diseño web
  - Cualquiera que haya recibido resultados genéricos de Claude en diseño
  - Equipos sin diseñador que necesitan resultados visuales de calidad
:::

:::callout
  **Incluye**

  - Por qué Claude diseña genérico sin referencia
  - Los 3 recursos con links directos
  - Cómo usar cada uno con Claude paso a paso
  - Prompts exactos para cada recurso
  - Limitación principal a tener en cuenta
:::

---

### Por qué Claude diseña genérico sin referencia

Claude es un modelo de lenguaje entrenado en texto — no tiene criterio visual propio. Cuando le pides “haz una página bonita” sin darle referencia, adivina. Y lo que adivina siempre se parece a lo mismo: fondo blanco, tipografía de sistema, colores azul y gris, sin jerarquía visual.

El problema no es Claude. Es la instrucción.

:::callout
  **La solución:** darle tres tipos de referencia antes de pedir el diseño — un sistema de estilo, una animación concreta y un video de fondo. Con esos tres insumos, Claude construye algo que se ve intencional, no generado.

:::

---

### Recurso 1 — Estilos de diseño

**Lo que resuelve:** darle a Claude un sistema visual completo — tipografía, colores, espaciado, jerarquía — en lugar de que lo invente.

Existen librerías de estilos de diseño que ya tienen definidos sistemas visuales inspirados en marcas reconocidas como Linear, Stripe, Vercel, Apple o Notion. En lugar de describir cómo quieres que se vea, le das el link del estilo y Claude lo implementa directamente.

---

**Cómo usarlo:**

```plain text
1. Entra a la librería de estilos:
   https://opendesign.so (o la que prefieras)
2. Elige el estilo que quieres aplicar
3. Copia el link o el código del estilo
4. Pásalo a Claude con esta instrucción:
```

**Prompt exacto:**

```plain text
Instala este sistema de diseño y úsalo como base
para todo lo que construyas en esta sesión:
[pega el link o el código del estilo]

Después, construye [lo que necesitas: landing page,
dashboard, sección hero, pricing page, etc.].
Mantener consistencia visual en todos los elementos.
```

:::callout
  **Tip:** el estilo que eliges le dice a tu audiencia quién eres. Linear y Vercel para productos técnicos. Stripe para finanzas y pagos. Apple para productos premium. Notion para herramientas de productividad. Elige el que resuena con tu cliente ideal, no el que más te guste a ti.

:::

---

### Recurso 2 — Animaciones listas para copiar

**Lo que resuelve:** agregar movimiento a tu página sin saber CSS ni JavaScript.

Hay sitios con animaciones prehechas que incluyen el código listo. Eliges la animación que quieres, copias el prompt o el código, y se lo pasas a Claude para que la integre en tu página. Puedes repetir esto con tantas animaciones como necesites.

---

**Recursos de animaciones gratuitas:**

- **Animista** — [animista.net](https://animista.net) — animaciones CSS listas para copiar, con preview en vivo
- **Magic UI** — [magicui.design](https://magicui.design) — componentes animados para React
- **Aceternity UI** — [ui.aceternity.com](https://ui.aceternity.com) — efectos visuales premium listos para integrar
---

**Cómo usarlo:**

```plain text
1. Entra a cualquiera de los sitios de animaciones
2. Navega hasta encontrar una que te guste
3. Haz clic en "Copy" o "Copy prompt"
4. Pásale el código a Claude con esta instrucción:
```

**Prompt exacto:**

```plain text
Integra esta animación en [la sección específica
de la página: hero, cards, botón, navbar, etc.].
Asegúrate de que se vea natural con el resto del diseño
y que no afecte el rendimiento de la página.

Código de la animación:
[pega el código copiado]
```

:::callout
  **Tip de uso:** no pongas animaciones en todo. Una o dos animaciones bien colocadas (sección hero, transición de cards) elevan el diseño. Muchas animaciones juntas lo hacen ver caótico y lento.

:::

---

### Recurso 3 — Video de fondo con Higgsfield

**Lo que resuelve:** convertir una foto estática de tu producto en un video animado listo para usar como fondo de página.

Higgsfield es una plataforma de generación de video con IA. Subes la foto de tu producto, defines el movimiento y el ambiente visual, y Higgsfield genera un video de alta calidad. Después le das ese video a Claude y él lo integra como fondo en tu página.

---

**Cómo usarlo:**

```plain text
1. Entra a gethouston.ai (Higgsfield) y crea tu cuenta
2. Sube la foto de tu producto o imagen de referencia
3. Define el tipo de movimiento que quieres:
   - Cámara lenta cinematográfica
   - Movimiento sutil de fondo
   - Animación de producto rotando
4. Genera el video (tarda 1-3 minutos)
5. Descarga el archivo de video
6. Pásale el video a Claude con esta instrucción:
```

**Prompt en Higgsfield para generar el video:**

```plain text
Usa el MCP de Higgsfield con Seedance 2.0.
Tengo esta imagen: [sube la foto del producto].
Genera un video de 6-8 segundos con movimiento de cámara
lento y suave, iluminación cinematográfica cálida.
El producto debe verse estable, el movimiento es del ambiente.
Formato: 16:9 para uso como fondo de página web.
```

**Prompt para integrar el video en tu página:**

```plain text
Integra este video como fondo de la sección hero
de la página. El video debe:
- Reproducirse automáticamente en loop
- No tener sonido
- Tener una capa de overlay oscuro al 40% de opacidad
  para que el texto sea legible encima
- Ser responsive en móvil y desktop

Archivo de video: [adjunta o pega el link del video]
```

---

### El flujo completo

Así se usan los tres recursos juntos en una sola sesión:

```plain text
Paso 1: Instala el estilo de diseño
↓
Paso 2: Pide la estructura base de la página
↓
Paso 3: Agrega las animaciones sección por sección
↓
Paso 4: Integra el video de fondo en el hero
↓
Paso 5: Revisa y pide ajustes en lenguaje normal
```

:::callout
  **El resultado:** una página con sistema visual consistente, movimiento intencional y un hero con video de producto — sin tocar código tú mismo y sin contratar un diseñador.

:::

---

### Limitación principal (para no frustrarte)

:::callout
  Claude construye páginas que funcionan y se ven bien, pero para proyectos de producción real — donde la página va a recibir tráfico, tiene formularios, se conecta a un CRM o necesita SEO — siempre habrá detalles técnicos que requieren revisión de alguien con conocimiento de desarrollo web. El output de Claude es un excelente punto de partida y un prototipo funcional — no siempre es el producto final sin tocar.

:::

**Tip práctico:** usa Claude para construir el prototipo rápido y mostrarlo a un cliente o validar la idea. Si el cliente aprueba, ahí decides si contratas a alguien para refinarlo o si Claude puede llevarlo al 100% según la complejidad del proyecto.

---

:::callout
  **Una pregunta antes de cerrar:**

  ¿Cuántas veces le pediste a Claude que construyera algo visual y el resultado no representó bien tu trabajo — y lo dejaste así porque no sabías cómo mejorarlo?

  Esos tres recursos son exactamente lo que faltaba en esa instrucción.

:::
