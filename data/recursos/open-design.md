> *La mayoría de herramientas de diseño con AI te dan una página en blanco y esperan que sepas cómo hacerla ver bien. Open Design llega con más de 70 estilos listos inspirados en las marcas de diseño más reconocidas del mundo y funciona con casi cualquier modelo de IA que ya uses.*

:::callout
  **Ideal para**

  - Founders y equipos que construyen con Claude Code o Codex
  - Diseñadores que quieren acelerar producción
  - Developers que necesitan resultados visuales consistentes
  - Cualquiera que use IA para crear interfaces o documentos
:::

:::callout
  **Incluye**

  - Qué es Open Design y por qué es diferente
  - Los 70+ estilos y cómo elegir el correcto
  - Con qué modelos funciona (y el truco del uso local)
  - Qué puede crear más allá de páginas web
  - Cómo instalarlo y conectarlo con Claude
  - Limitación principal a tener en cuenta
:::

---

### 1) Qué es Open Design (y por qué importa)

Open Design es una herramienta de diseño generativo que funciona desde tu computadora. Le describes lo que quieres crear y construye el diseño completo  con identidad visual coherente, sin que tengas que tomar decisiones de estilo desde cero.

Lo que lo diferencia de otras herramientas similares no es solo lo que genera, sino **cómo mantiene la consistencia visual**: en lugar de inventar un estilo por cada componente, aplica un sistema de diseño completo inspirado en marcas reales desde el primer elemento.

:::callout
  **Traducción a negocio:** menos tiempo en decisiones de diseño, más velocidad para llegar a un resultado que se ve profesional, y sin depender de un diseñador para cada iteración.

:::

---

### 2) Los 70+ estilos y cómo elegir

Open Design trae más de 70 estilos precargados inspirados en marcas de diseño reconocidas. No son temas genéricos, son sistemas visuales completos con tipografía, espaciado, colores y jerarquía definidos.

Algunos de los estilos disponibles:

---

**Linear** — oscuro, tipografía nítida, bordes precisos. Ideal para herramientas de productividad, SaaS técnico, dashboards internos.

---

**Stripe** — limpio, confianza implícita, alto contraste en llamados a la acción. Ideal para páginas de pago, landing pages de conversión, productos fintech.

---

**Vercel** — minimalismo extremo, negro sobre blanco, muy técnico. Ideal para documentación, herramientas para developers, páginas de deploy.

---

**Apple** — espacio en blanco generoso, fotografía prominente, texto grande. Ideal para productos físicos, launches de producto, páginas de marketing premium.

---

**Notion** — estructura clara, neutral, legible. Ideal para reportes, documentación interna, planes de equipo, wikis.

---

**Tesla** — cinematográfico, oscuro, imponente. Ideal para productos de hardware, marcas aspiracionales, landing pages de alto impacto.

:::callout
  **Cómo elegir:** piensa en qué marca admira tu cliente ideal. Si le vendes a developers, Linear o Vercel. Si le vendes a consumidores premium, Apple o Tesla. Si es interno o educativo, Notion. El estilo no es decoración — es señal de credibilidad para tu audiencia específica.

:::

---

### 3) Con qué modelos funciona

Esta es una de las ventajas más importantes de Open Design frente a alternativas como v0 o Lovable.

---

**Claude Code** — integración directa. Open Design puede recibir instrucciones desde Claude Code y generar el diseño dentro del mismo flujo de desarrollo.

---

**Codex (OpenAI)** — compatible. Puedes usarlo dentro de flujos agénticos de Codex para generar interfaces como parte de un pipeline más grande.

---

**Gemini** — también compatible. Para quienes ya trabajan dentro del ecosistema de Google.

---

**Uso local (sin tokens)** — si lo corres localmente con un modelo open source, no consumes tokens de ninguna API. El costo de generación baja a cero.

:::callout
  **Nota sobre uso local:** requiere configuración técnica inicial (instalar el modelo localmente, conectarlo con Open Design). Si prefieres empezar rápido, conectarlo con Claude Code o Codex es más inmediato aunque tiene costo por token.

:::

---

### 4) Qué puede crear

Open Design no es solo para páginas web. Estos son los tipos de output que genera:

---

**Páginas web y landing pages** — con secciones hero, features, pricing, testimonios, y CTA. Listas para conectar a tu stack.

---

**Dashboards** — interfaces de datos con tablas, gráficos, métricas y navegación lateral. Estilo consistente en cada componente.

---

**Apps móviles** — pantallas que se ven como aplicaciones reales, no como wireframes. Con navegación, estados y componentes nativos.

---

**Presentaciones** — slides con jerarquía visual clara, no el look genérico de PowerPoint con IA.

---

**Pricing pages y funnels** — estructuras de conversión completas con comparación de planes, FAQs y llamados a la acción.

---

**Reportes financieros y planes de equipo** — documentos estructurados con el mismo sistema visual, no un PDF improvisado.

---

### 5) Cómo instalarlo y conectarlo con Claude

#### Instalación base

```plain text
# Clona el repositorio
git clone https://github.com/[repo-open-design]
cd open-design

# Instala dependencias
npm install

# Inicia el servidor local
npm run dev
```

#### Conectarlo con Claude Code

Una vez corriendo localmente, desde Claude Code puedes llamarlo así:

```plain text
Usando Open Design con el estilo [nombre del estilo],
crea una [tipo de página: landing page / dashboard / pricing page].

Contenido:
- Título principal: [tu título]
- Propuesta de valor: [una línea]
- Secciones: [lista las secciones que necesitas]
- CTA principal: [texto del botón y a dónde lleva]

Exporta el resultado como HTML/CSS listo para producción.
```

#### Para generar un dashboard

```plain text
Usando Open Design con estilo Linear,
crea un dashboard de métricas para [tipo de negocio].

Métricas a mostrar:
- [Métrica 1: nombre + valor de ejemplo]
- [Métrica 2: nombre + valor de ejemplo]
- [Métrica 3: nombre + valor de ejemplo]

Incluye: barra lateral de navegación, header con nombre del usuario,
tabla de últimas transacciones y gráfico de tendencia mensual.
```

---

### 6) Limitación principal (para no frustrarte)

:::callout
  Open Design genera el **diseño visual** — no el backend, no la lógica de negocio, no las integraciones. Lo que produces es una interfaz funcional en HTML/CSS (o el framework que elijas), pero conectarlo a datos reales o a una base de datos requiere trabajo de desarrollo adicional. No es un producto terminado, es la capa de presentación lista para que un developer la conecte.

:::

**Tip práctico:** úsalo para validar visualmente una idea antes de construir el backend. Muéstrale la interfaz generada a un cliente o inversor para obtener feedback sobre el producto antes de invertir tiempo en desarrollo.

---

:::callout
  **Antes de cerrar esta guía, una pregunta concreta:**

  ¿Cuál es el último diseño que tuviste que pedirle a alguien más porque no tenías la herramienta o el tiempo?

  Ese es exactamente el caso de uso por donde empezar con Open Design.

:::

