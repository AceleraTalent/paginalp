> *Si solo abres Claude en el navegador y le escribes ahí, estás usando una pequeña parte de lo que puede hacer. Estos 5 niveles te muestran el camino completo — desde el uso básico hasta tener un agente trabajando solo con tu laptop cerrada.*

:::callout
  **Ideal para**

  - Usuarios de Claude que quieren ir más allá del chat básico
  - Founders y equipos que usan Claude todos los días
  - Profesionales que quieren automatizar sin aprender a programar
  - Cualquiera que sienta que Claude podría darle más
:::

:::callout
  **Incluye**

  - Los 5 niveles de uso de Claude en orden de profundidad
  - Qué desbloquea cada nivel
  - Cómo empezar con cada uno
  - Prompts y ejemplos listos para copiar
  - Por dónde empezar según tu nivel actual
:::

---

### La escalera completa

```plain text
Nivel 1 — Claude Code
Más poder, misma conversación
        ↓
Nivel 2 — Comandos guardados
Menos tiempo escribiendo, más tiempo haciendo
        ↓
Nivel 3 — Skills
Claude aprende cómo trabajas tú
        ↓
Nivel 4 — MCP
Claude accede a tus herramientas directamente
        ↓
Nivel 5 — Managed Agents
Claude trabaja solo, incluso con la laptop cerrada
```

:::callout
  **Cómo leer esta guía:** no tienes que llegar al nivel 5 para obtener valor. Cada nivel ya es una mejora significativa sobre el anterior. Empieza donde estás y sube cuando el nivel actual ya te quede pequeño.

:::

---

### Nivel 1 — Claude Code

**Lo que desbloquea:** el mismo Claude del navegador, pero con más capacidades.

Claude Code es la versión de escritorio de Claude que corre en una terminal. No necesitas saber programar — Claude escribe el código, ejecuta los comandos y te muestra los resultados. Tú solo indicas qué quieres lograr e iteras sobre el resultado.

La diferencia con el navegador: Claude Code puede acceder a archivos de tu computador, ejecutar código real, instalar skills y conectarse a MCPs. El Claude del navegador no puede hacer nada de eso.

---

**Cómo empezar:**

```plain text
1. Descarga Claude Code desde claude.ai/code
2. Instálalo en tu Mac o Windows
3. Inicia sesión con tu cuenta de Claude
4. Abre una conversación y dale la misma instrucción
   que le darías en el navegador
```

**Prompt para probar que funciona:**

```plain text
Lee todos los archivos de esta carpeta: [ruta]
Dime qué hay ahí y si falta algo importante.
```

---

### Nivel 2 — Comandos guardados

**Lo que desbloquea:** dejas de escribir el mismo mensaje muchas veces.

Si hay una instrucción que usas frecuentemente — resumir una reunión, escribir un correo, analizar un documento — puedes guardarla como un comando corto. En lugar de escribir el prompt completo cada vez, escribes `/correo` o `/resumen` y Claude ejecuta la instrucción guardada.

---

**Cómo crear un comando:**

```plain text
En Claude Code, ve a Settings → Commands → New Command

Nombre del comando: correo
Instrucción guardada:
"Escribe un correo profesional basado en este contexto.
Tono: directo y cordial. Máximo 150 palabras.
Estructura: saludo breve, punto principal, llamado a la acción claro."
```

**Cómo usarlo después:**

```plain text
/correo
Necesito escribirle a [cliente] para hacer seguimiento
de la propuesta que enviamos el lunes.
```

---

### Nivel 3 — Skills

**Lo que desbloquea:** Claude aprende cómo trabajas tú, no cómo trabaja cualquiera.

Una skill es un archivo simple que le enseña a Claude tu forma de hacer las cosas: cómo escribes, qué estructura usas, qué tono manejas, cómo organizas tu trabajo. Claude guarda esa información y la aplica automáticamente sin que tú se lo pidas cada vez.

La diferencia con un prompt largo: un prompt tienes que repetirlo. Una skill vive en Claude y se activa sola cuando es relevante.

---

**Cómo instalar una skill:**

```plain text
En Claude Code, ve a Settings → Skills → Explorar
Busca la skill que necesitas e instálala
O crea la tuya: Settings → Skills → New Skill
```

**Ejemplo de skill personalizada:**

```plain text
# Mi estilo de escritura

Cuando escribas contenido para mí:
- Tono: directo, sin rodeos, sin clichés de marketing
- Estructura: idea principal primero, contexto después
- Longitud: lo mínimo necesario para ser claro
- Nunca uses: "sin duda", "es importante destacar", 
  "en conclusión"
- Siempre usa: ejemplos concretos, números cuando existen
```

---

### Nivel 4 — MCP

**Lo que desbloquea:** Claude accede a tus herramientas directamente, sin que tú copies y pegues nada.

MCP (Model Context Protocol) son conectores que le permiten a Claude leer y escribir en tus aplicaciones en tiempo real. Con Gmail conectado, Claude lee tus correos. Con Notion conectado, guarda notas ahí. Con Slack, puede enviar mensajes. Tú describes lo que quieres y Claude lo ejecuta en la herramienta correspondiente.

---

**Cómo conectar un MCP:**

```plain text
1. En Claude Code, ve a Settings → Integrations
2. Haz clic en "Add Connector" o "Add MCP Server"
3. Pega la URL del MCP de la herramienta que quieres conectar
4. Autoriza los permisos
```

**MCPs esenciales para empezar:**

- Gmail: `https://gmailmcp.googleapis.com/mcp/v1`
- Google Calendar: `https://calendarmcp.googleapis.com/mcp/v1`
- Notion: `https://mcp.notion.com/mcp`
**Prompt para probar la conexión:**

```plain text
Revisa mis correos de hoy en Gmail y dime cuáles
necesitan respuesta urgente de mi parte.
```

---

### Nivel 5 — Managed Agents

**Lo que desbloquea:** Claude trabaja solo, incluso con tu laptop cerrada.

Este es el nivel más avanzado. Un Managed Agent es un agente configurado para ejecutar tareas de forma autónoma en un schedule definido — sin que tú estés presente. Puede revisar tus correos cada hora, generar un reporte cada lunes, o dispararse cuando pasa algo específico en una de tus herramientas.

:::callout
  **Nota de honestidad:** este nivel requiere más configuración que los anteriores. Necesitas entender bien los niveles 1 al 4 antes de llegar aquí, y en la mayoría de casos necesitas el plan Pro de la herramienta que uses para que el agente corra 24/7 sin depender de que tu computador esté encendido.

:::

**Dónde implementar Managed Agents:**

- **Houston AI** ([gethouston.ai](http://gethouston.ai)) — plan Pro permite agentes que corren 24/7
- **Claude Code con servidor propio** — para equipos técnicos
- [**Make.com**](http://Make.com)** o N8N + Claude API** — para flujos programados sin servidor propio
**Ejemplo de lo que puede hacer un Managed Agent:**

```plain text
Cada lunes a las 8am:
- Revisa mis correos de la semana anterior
- Extrae las tareas pendientes que me comprometieron
- Las cruza con mi calendario
- Me envía un resumen por WhatsApp antes de que empiece el día
```

---

### Por dónde empezar según tu nivel actual

---

**Si solo usas Claude en el navegador:**

→ Empieza por el **Nivel 1**. Descarga Claude Code esta semana y dale la misma tarea que le das en el navegador. La diferencia en capacidades es inmediata.

---

**Si ya usas Claude Code pero cada sesión empieza de cero:**

→ Ve al **Nivel 2 y 3**. Guarda tus prompts frecuentes como comandos y crea tu primera skill con tu estilo de trabajo.

---

**Si ya tienes skills pero sigues copiando y pegando información de otras apps:**

→ Ve al **Nivel 4**. Conecta Gmail o Notion y prueba pedirle algo que requiera leer tu información real.

---

**Si ya tienes MCPs conectados y quieres que Claude trabaje sin ti:**

→ Explora el **Nivel 5** con Houston AI o [Make.com](http://Make.com) + Claude API.

---

:::callout
  **Una pregunta antes de cerrar:**

  ¿En qué nivel estás hoy?

  El siguiente nivel es exactamente el trabajo repetitivo que todavía haces tú y podría estar haciendo Claude.

:::
