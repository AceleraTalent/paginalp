> *Con Claude Code, una interfaz visual, la voz de ElevenLabs y tus API keys, puedes construir tu propio asistente de IA personalizado — con tu nombre, tu voz preferida, y entrenado en tu forma de pensar. En menos de una hora.*

:::callout
  **Ideal para**

  - Usuarios de Claude Code que quieren un proyecto concreto
  - Founders que quieren un asistente entrenado en su negocio
  - Cualquiera que haya soñado con tener un Jarvis propio
  - Personas que ya usan Claude o ChatGPT y quieren algo más personalizado
:::

:::callout
  **Incluye**

  - Lo que necesitas antes de empezar
  - Los 3 pasos para construirlo
  - El prompt exacto para darle a Claude Code
  - Cómo subirle tu forma de pensar
  - Cómo habilitarle control del computador
  - Limitación principal a tener en cuenta
:::

---

### 1) Lo que necesitas antes de empezar

Son cuatro cosas. Todas accesibles, dos de ellas gratuitas.

---

**Claude Code** — la app de escritorio de Anthropic. Descarga gratuita en [claude.ai/code](https://claude.ai/code). Necesitas un plan pago para usarlo.

---

**Una interfaz visual** — la cara de tu Jarvis. Busca en Google, Pinterest o Dribbble una interfaz de asistente que te guste — algo oscuro, futurista, minimalista. Guarda la imagen. Esa va a ser la referencia visual que le pases a Claude Code.

---

**Cuenta en ElevenLabs** — para la voz. Entra a [elevenlabs.io](https://elevenlabs.io), crea una cuenta gratuita, elige la voz que quieres que tenga tu asistente y copia el **Voice ID**. Después ve a tu perfil y copia tu **API key**.

---

**API key de Claude** — para que Jarvis pueda pensar. Entra a [console.anthropic.com](https://console.anthropic.com), crea una API key y cópiala. Esta es la que conecta tu Jarvis directamente con el modelo de Claude.

:::callout
  **Nota de costos:** ElevenLabs tiene plan gratuito con límite mensual de caracteres. La API de Claude tiene costo por token — para uso personal moderado, es mínimo. Estima menos de $5 USD al mes para empezar.

:::

---

### 2) Los 3 pasos para construirlo

---

**Paso 1: Consigue la interfaz**

Busca una imagen de interfaz de asistente que represente el estilo visual que quieres. Referencias útiles: busca en Google “Jarvis UI interface”, “AI assistant dashboard dark” o “HUD interface concept”. Guarda la imagen en tu computador.

---

**Paso 2: Configura ElevenLabs**

```plain text
1. Entra a elevenlabs.io
2. Crea cuenta gratuita
3. Ve a "Voice Library" y escucha las voces disponibles
4. Elige la que quieres para tu asistente
5. Haz clic en la voz → copia el Voice ID
6. Ve a tu perfil → API Keys → copia tu API key
```

---

**Paso 3: Dáselo todo a Claude Code**

Abre Claude Code, adjunta la imagen de la interfaz y pega este prompt adaptándolo con tus datos reales:

```plain text
Quiero que construyas mi asistente personal de IA.

Nombre del asistente: [nombre que quieras: Alfred, Jarvis, Nova, etc.]

Referencia visual: [adjunta la imagen de la interfaz que elegiste]
Constrúye la interfaz inspirada en esta imagen — modo oscuro,
estética futurista, limpia.

Voz:
ElevenLabs Voice ID: [pega el ID]
ElevenLabs API Key: [pega tu API key]

Inteligencia:
Claude API Key: [pega tu API key de Anthropic]
Modelo: claude-sonnet-4-6

Personalidad del asistente:
[describe cómo quieres que hable: formal como Alfred,
eficiente como Jarvis, cercano como un colega, etc.]

Capacidades iniciales que debe tener:
- Responder preguntas y ayudar con tareas de texto
- Leer mi calendario y agenda
- Recordar contexto entre conversaciones

Constrúyelo completo: frontend con la interfaz visual,
conexiones a las APIs, y que la voz funcione al hablarle.
Muéstrame el progreso mientras construyes.
```

:::callout
  **Qué esperar:** Claude Code va a escribir el código, instalar las dependencias y armar el proyecto completo. El proceso toma entre 30 minutos y una hora dependiendo de la complejidad de la interfaz. Tú solo revisas el resultado y pides ajustes.

:::

---

### 3) Cómo subirle tu forma de pensar

Esta es la parte que convierte un asistente genérico en uno que realmente te conoce.

Si ya usas Claude o ChatGPT frecuentemente, tienes meses o años de conversaciones que reflejan cómo piensas, qué decides, cómo priorizas. Ese contexto se puede subir a Jarvis para que sus respuestas sean específicas para ti — no genéricas.

---

**Prompt para crear tu perfil de pensamiento:**

```plain text
Voy a describirte cómo pienso y trabajo para que lo uses
como contexto permanente:

Mi negocio: [qué haces, a quién le vendes]
Mis prioridades actuales: [qué estás tratando de lograr]
Cómo tomo decisiones: [criterios que usas]
Qué me importa más en el trabajo: [valores y principios]
Mis fortalezas: [lo que haces mejor]
Mis puntos ciegos: [dónde necesitas más ayuda]
Tono que prefiero: [directo, reflexivo, retador, etc.]

Usa esto para personalizar todas tus respuestas.
No me des consejos genéricos — dáme análisis basados
en este contexto específico.
```

---

**Cómo cargarlo en Jarvis:**

Una vez que tengas el texto de tu perfil, agrégalo al archivo de instrucciones del sistema de Jarvis — Claude Code puede hacer esto directamente:

```plain text
Agrega este contexto al system prompt de Jarvis
para que lo tenga disponible en todas las conversaciones:
[pega tu perfil]
```

---

### 4) Cómo habilitarle control del computador

Este es el nivel más avanzado. Con las herramientas correctas, Jarvis puede controlar tu computador — abrir aplicaciones, navegar el navegador, mover archivos — exactamente como lo harías tú.

---

**Opción 1: Playwright MCP**

Le da control del navegador. Jarvis puede navegar páginas, hacer clics, llenar formularios.

```plain text
Agrega el MCP de Playwright a Jarvis para que pueda
controlar el navegador. Cuando le pida navegar a [URL]
o hacer una acción en el navegador, debe ejecutarla directamente.
```

---

**Opción 2: Computer Use de Anthropic**

Le da control total del escritorio — no solo el navegador. Puede ver la pantalla, mover el cursor y ejecutar cualquier acción.

```plain text
Activa Computer Use en Jarvis. Cuando le dé una tarea
que requiera interactuar con el escritorio, debe tomar
el control y ejecutarla, mostrándome lo que hace.
```

:::callout
  **Regla de seguridad:** nunca le des control del computador sin revisar primero qué va a hacer. Siempre pídele que te muestre el plan antes de ejecutar — especialmente para acciones que no se pueden deshacer como borrar archivos, enviar correos o hacer pagos.

:::

---

### 5) Limitación principal (para no frustrarte)

:::callout
  Jarvis es tan bueno como el contexto que tiene. Sin el perfil de pensamiento cargado, va a responder como cualquier instancia genérica de Claude — inteligente pero no personalizado. El tiempo de construcción varía: interfaces simples toman 30 minutos, interfaces complejas con animaciones y múltiples pantallas pueden tomar 2-3 horas de iteración con Claude Code.

:::

**Tip práctico:** empieza con una interfaz simple — fondo oscuro, texto blanco, botón de micrófono. Primero verifica que la voz funciona y que Claude responde correctamente. Después itera en el diseño visual. El orden importa: funcionalidad primero, estética después.

---

:::callout
  **Una pregunta antes de cerrar:**

  Si tuvieras un asistente que te conoce, sabe cómo piensas, puede hablar contigo con tu voz favorita y controlar tu computador — ¿cuál sería la primera tarea que le darías?

  Esa es exactamente la primera instrucción para darle a Jarvis cuando lo tengas listo.

:::
