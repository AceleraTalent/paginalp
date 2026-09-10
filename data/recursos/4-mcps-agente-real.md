> *La mayoría de personas usa Claude para preguntas y respuestas. Con estos 4 MCPs, Claude navega internet en vivo, controla un navegador como un humano, rastrea sitios web completos y genera campañas visuales — todo sin salir de tu conversación.*

:::callout
  **Ideal para**

  - Usuarios de Claude que quieren ir más allá del chat
  - Equipos que investigan competidores, mercados o clientes
  - Marketers que producen contenido visual con IA
  - Founders que quieren automatizar tareas en el navegador
:::

:::callout
  **Incluye**

  - Qué es un MCP y por qué cambia todo
  - Los 4 MCPs esenciales con casos de uso reales
  - Cómo instalar cada uno en Claude
  - Prompts listos para copiar
  - Limitación principal a tener en cuenta
:::

---

### Qué es un MCP (y por qué importa)

MCP (Model Context Protocol) es el estándar que le permite a Claude conectarse con herramientas externas y ejecutar acciones reales fuera de la conversación. No es un plugin — es una conexión directa que le da capacidades nuevas a Claude que no tiene por defecto.

Sin MCPs: Claude sabe mucho pero no puede hacer nada en el mundo real.

Con MCPs: Claude navega, investiga, controla aplicaciones y genera contenido sin que tú intervengas.

:::callout
  **Cómo instalar cualquier MCP en Claude:** ve a **Claude → Settings → Integrations** (o Connectors) → agrega el servidor MCP correspondiente con su URL. Cada MCP de esta guía incluye el link directo.

:::

---

### MCP 1 — Perplexity

**Lo que hace:** le da a Claude acceso a internet en vivo dentro de tu conversación.

Sin este MCP, Claude tiene un corte de conocimiento — no sabe qué pasó hoy, esta semana, o el mes pasado. Con Perplexity conectado, Claude puede responder preguntas con información real y actualizada al momento, sin que tú salgas de la conversación a buscar nada.

---

**Casos de uso reales:**

- Investigar noticias recientes de una industria o empresa
- Verificar datos actualizados antes de tomar una decisión
- Comparar precios, tasas o estadísticas que cambian frecuentemente
- Seguir tendencias de mercado en tiempo real
---

**Prompts para usar con Perplexity MCP:**

```plain text
Busca las últimas noticias sobre [empresa o industria]
de los últimos 7 días y dime qué está pasando.
```

```plain text
¿Cuál es la tasa de cambio actual de [moneda]?
¿Cómo ha cambiado en los últimos 30 días?
```

```plain text
Investiga los tres competidores principales de [empresa]
y dime qué han lanzado o anunciado en el último mes.
```

**🔗 Link de instalación:** [Perplexity MCP](https://docs.perplexity.ai/guides/mcp-server)

---

### MCP 2 — Playwright

**Lo que hace:** le da a Claude control total de un navegador web.

Claude puede navegar páginas, hacer clics, llenar formularios, subir archivos y ejecutar cualquier acción que tú harías manualmente en el navegador. La diferencia con un chatbot normal es total: Claude deja de decirte cómo hacer algo y empieza a hacerlo por ti.

---

**Casos de uso reales:**

- Llenar formularios repetitivos en plataformas que no tienen API
- Navegar y extraer información de sitios que bloquean scrapers simples
- Automatizar flujos de trabajo en herramientas web sin integración nativa
- Tomar screenshots de páginas para documentación o análisis
---

**Prompts para usar con Playwright MCP:**

```plain text
Entra a [URL], busca [información específica] y tráemela
organizada en una tabla.
```

```plain text
Navega a [URL], completa el formulario de contacto con
esta información: [datos] y confírmame cuando esté enviado.
```

```plain text
Entra a mi cuenta de [plataforma], descarga el reporte
de [período] y guardalo en mi carpeta de descargas.
```

**🔗 Link de instalación:** [Playwright MCP](https://github.com/microsoft/playwright-mcp)

---

### MCP 3 — Firecrawl

**Lo que hace:** rastrea sitios web completos y carga todo el contenido directo en tu conversación con Claude.

La diferencia con Perplexity es el nivel de profundidad: Perplexity te da resultados de búsqueda actualizados. Firecrawl entra a un sitio específico, recorre todas sus páginas y trae el contenido completo para que Claude lo analice. Es el compañero de research que siempre quisiste — lee todo, organiza todo, y te da lo que necesitas.

---

**Casos de uso reales:**

- Investigar un competidor completo: página de precios, casos de éxito, blog, propuesta de valor
- Analizar el sitio web de un prospecto antes de una reunión comercial
- Extraer toda la documentación técnica de una herramienta para entenderla rápido
- Monitorear cambios en páginas clave de tu industria
---

**Prompts para usar con Firecrawl MCP:**

```plain text
Rastrea el sitio completo de [URL] y dame:
- Su propuesta de valor principal
- A quién le venden
- Sus precios si están publicados
- Sus diferenciadores vs el mercado
```

```plain text
Antes de mi reunión con [empresa], rastrea [URL de su sitio]
y prepárame un resumen ejecutivo de lo que hacen,
qué problemas resuelven y quiénes son sus clientes.
```

```plain text
Rastrea la documentación de [URL] y explícame
cómo funciona [funcionalidad específica] en lenguaje simple.
```

**🔗 Link de instalación:** [Firecrawl MCP](https://docs.firecrawl.dev/mcp)

---

### MCP 4 — Higgsfield

**Lo que hace:** genera campañas publicitarias completas, videos, UGC ads e influencers digitales directamente desde Claude.

Higgsfield es una plataforma de generación de video con IA — con modelos como Seedance 2.0, Kling 3.0 y Marketing Studio. Con el MCP conectado, Claude puede operar Higgsfield directamente: subes una imagen de producto, describes la campaña, y Claude genera el video sin que salgas del flujo de trabajo. Esto no existe en ninguna otra herramienta de IA conversacional.

---

**Casos de uso reales:**

- Generar un video ad para Meta desde una foto de producto
- Crear múltiples variaciones de un mismo ad para testear cuál performa mejor
- Producir contenido UGC con avatares sin contratar creadores
- Animar imágenes estáticas de producto para Instagram o TikTok
---

**Prompts para usar con Higgsfield MCP:**

```plain text
Usa el MCP de Higgsfield con Marketing Studio Video.
Tengo esta imagen de producto: [sube la foto].
Genera un video ad de 6 segundos en formato 9:16 para Meta Stories.
Preset: Product Review. Iluminación cálida, movimiento suave.
```

```plain text
Usa Higgsfield con Seedance 2.0.
Necesito 3 variaciones del mismo video con fondos distintos:
blanco, oscuro y urbano exterior. Formato 9:16, 6 segundos cada uno.
Imagen: [sube imagen]. Dame los IDs de cada generación.
```

**🔗 Link de instalación:** [Higgsfield MCP](https://mcp.higgsfield.ai/mcp)

---

### Cómo instalarlos todos en Claude

El proceso es el mismo para los 4:

```plain text
1. Abre Claude
2. Ve a Settings → Integrations (o Connectors)
3. Haz clic en "Add Connector" o "Add MCP Server"
4. Pega la URL del MCP correspondiente
5. Autoriza los permisos que pida
6. Listo — Claude ya tiene esa capacidad disponible
```

:::callout
  **Nota:** algunos MCPs como Playwright requieren instalación local en tu computador (Node.js). Los demás se conectan directamente desde Claude sin instalar nada adicional. Revisa la documentación de cada uno antes de empezar.

:::

---

### Limitación principal (para no frustrarte)

:::callout
  Cada MCP consume recursos distintos. Playwright requiere que tu computador esté encendido y el navegador disponible. Firecrawl y Perplexity tienen límites de uso según el plan que tengas. Higgsfield consume créditos de tu cuenta de Higgsfield — no de Claude. Antes de usar cada uno intensivamente, revisa los límites de uso de tu plan en cada plataforma.

:::

**Tip práctico:** instala primero Perplexity — es el más inmediato y el que más cambia la experiencia diaria con Claude desde el primer día. Después agrega los demás uno por uno según tu caso de uso.

---

:::callout
  **Una pregunta antes de cerrar:**

  ¿Cuántas veces esta semana saliste de Claude a buscar información, navegar una página o generar algo en otra herramienta — y después tuviste que copiar y pegar el resultado de vuelta?

  Esos pasos intermedios son exactamente lo que eliminan estos 4 MCPs.

:::
