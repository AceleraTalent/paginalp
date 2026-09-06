:::callout
  **5 MCPs que vuelven a Claude un Agente de verdad**

  Convierte tu IA en un sistema que **busca**, **navega**, **lee**, **planifica** y **ejecuta** sin caos.

:::

### ¿Qué es un MCP?

Un **MCP (Model Context Protocol)** es un “conector” que le da a Claude herramientas externas (web, navegador, docs, archivos, flujos) para que deje de depender solo del texto del chat y pueda **hacer trabajo real**.

---

### Los 5 MCPs (y el problema que resuelven)

#### 1) Tavily — búsqueda para agentes de IA

**Qué hace:** Motor de búsqueda hecho para agentes. Devuelve resultados en **datos limpios y estructurados** listos para LLMs.

**El problema que resuelve:** “Claude no puede leer ese sitio / no tengo acceso a esa página”. Con Tavily, el agente **encuentra y resume** lo que necesita de forma más confiable.

**Ideal para:** research rápido, comparativas, validar información, encontrar fuentes.

**Links:** [Website](https://tavily.com/) · [Docs](https://docs.tavily.com/)

---

#### 2) Playwright — Claude controla tu navegador

**Qué hace:** Le permite a Claude **usar el navegador** como si fuera una persona: clics, formularios, navegación, pasos repetitivos.

**El problema que resuelve:** El “modo agente” deja de ser teoría y se vuelve ejecución: *“llena este formulario por mí”* → lo hace.

**Ideal para:** automatizar tareas repetitivas, flujos de soporte, scraping ligero, operaciones.

**Links:** [Website/Docs](https://playwright.dev/) · [Repo](https://github.com/microsoft/playwright)

---

#### 3) Context7 — documentación real y actualizada

**Qué hace:** Le da a Claude **documentación actualizada** de lo que estés usando (miles de librerías).

**El problema que resuelve:** Se acabó Claude:

- inventando APIs que no existen
- sugiriendo métodos deprecados
- usando ejemplos viejos
**Ideal para:** desarrollo, integraciones, coding con precisión, evitar bugs por docs desactualizadas.

**Links:** [Website](https://context7.com/) · [Repo](https://github.com/upstash/context7)

> Nota para el reel: *Usar solo el minuto 3. Quitar el sonido, dejar solo el video y acelerarlo.*

---

#### 4) Task Manager AI — de requerimientos a tareas con dependencias

**Qué hace:** Le das un PRD / requerimientos y genera un plan de tareas **estructurado**, con **dependencias**.

**El problema que resuelve:** Una sesión de código caótica se vuelve un **pipeline**: Claude ejecuta paso a paso, en orden, sin perderse.

**Ideal para:** builds grandes, features complejas, refactors, lanzamientos.

**Links:** [Website](https://tryhamster.com/product/taskmaster) · [Repo](https://github.com/eyaltoledano/claude-task-master)

---

#### 5) Markdownify — cualquier documento → markdown “legible” por Claude

**Qué hace:** Convierte **PDFs, imágenes y audio** en markdown limpio que Claude puede entender sin fricción.

**El problema que resuelve:** Se acabó:

- “Claude no entiende esta imagen”
- “no puedo leer este PDF”
- copiar/pegar manualmente
**Ideal para:** análisis de documentos, procesos internos, inputs de clientes, transcripción + estructuración.

**Links:** [Repo](https://github.com/zcaceres/markdownify-mcp) · [NPM](https://www.npmjs.com/package/mcp-markdownify-server)

---

### La combinación ganadora (stack recomendado)

- **Tavily** para encontrar información
- **Markdownify** para convertirla a formato legible
- **Context7** para precisión técnica
- **Task Manager AI** para convertir objetivos en plan ejecutable
- **Playwright** para ejecutar en el mundo real (web)
---
