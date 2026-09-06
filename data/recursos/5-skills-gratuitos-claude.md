> *Si Claude alguna vez olvidó quién eras, diseñó algo feo, o se perdió en tu proyecto — el problema no era Claude. Era que le faltaban estas 5 cosas. Todas gratis. Todas instalables hoy.*

:::callout
  **Ideal para**

  - Usuarios de Claude que quieren más que un chatbot
  - Founders y equipos que trabajan proyectos largos con Claude
  - Developers que usan Claude Code
  - Cualquiera que haya recibido resultados genéricos o que Claude "olvidara" el contexto
:::

:::callout
  **Incluye**

  - Los 5 skills/MCPs con qué problema resuelve cada uno
  - Cómo instalar cada uno en Claude
  - Prompts para sacarle provecho desde el día uno
  - Limitación principal a tener en cuenta
:::

---

### Por qué Claude se queda corto sin estas 5 cosas

Claude por defecto es poderoso pero tiene cuatro puntos ciegos reales:

- **Olvida quién eres** — cada conversación empieza desde cero
- **Diseña funcional, no bonito** — sin criterio visual propio
- **No se conecta a tus herramientas** — no puede automatizar nada por sí solo
- **Se pierde en proyectos grandes** — empieza a inventar o contradecirse
- **Claude Code sin configurar** — capacidades dispersas que hay que activar una por una
Cada uno de los 5 skills de esta guía resuelve exactamente uno de esos problemas.

---

### Skill 1 — Claude Mem

**Problema que resuelve:** Claude olvida quién eres entre conversaciones.

Antes de este skill, cada sesión empezaba desde cero. Claude no sabía en qué proyecto estabas, qué decisiones ya habían tomado juntos, ni cómo trabajas. Con Claude Mem, el contexto de tu proyecto vive con él — lo que construyes hoy lo recuerda mañana.

**Lo que hace exactamente:**

- Guarda el contexto de tus proyectos de forma persistente
- Recuerda decisiones previas, preferencias y acuerdos
- Elimina la necesidad de re-explicar todo al inicio de cada sesión
---

**Cómo instalarlo:**

```plain text
1. Abre Claude Code
2. Ve a Settings → Skills
3. Busca "Claude Mem"
4. Instala y configura el archivo de memoria de tu proyecto
```

**Prompt para activarlo en tu proyecto:**

```plain text
Guarda este contexto para que lo recuerdes en futuras sesiones:

Proyecto: [nombre]
Objetivo: [qué estás construyendo]
Decisiones tomadas: [las más importantes]
Preferencias de trabajo: [cómo quieres que responda]
Siguientes pasos: [qué viene después]
```

---

### Skill 2 — UI UX Pro Max

**Problema que resuelve:** Claude diseña funcional pero no diseña bien.

Sin este skill, los resultados de diseño de Claude parecen plantilla — tipografía genérica, colores sin jerarquía, layouts que funcionan pero no impresionan. UI UX Pro Max le da criterio visual real: tipografía, paleta de colores, jerarquía, espaciado, y principios de diseño que hacen que el resultado se vea profesional.

**Lo que hace exactamente:**

- Le da a Claude principios de diseño UI/UX aplicados
- Mejora la selección de tipografías, colores y espaciado
- Produce interfaces y componentes con estética profesional, no de template
---

**Cómo instalarlo:**

```plain text
1. Abre Claude Code
2. Ve a Settings → Skills → Explorar
3. Busca "UI UX Pro Max"
4. Instala el skill en tu proyecto
```

**Prompt para activarlo:**

```plain text
Usando el skill de UI UX Pro Max, diseña [componente/página/interfaz].

Estilo de referencia: [Linear / Stripe / Apple / Notion / otro]
Audiencia: [a quién va dirigido]
Acción principal que debe provocar: [qué debe hacer el usuario]
Modo: [claro / oscuro / ambos]
```

---

### Skill 3 — N8N MCP

**Problema que resuelve:** Claude no puede conectarse a tus herramientas ni automatizar flujos.

N8N es una plataforma de automatización con más de 400 integraciones. Con el MCP de N8N conectado a Claude, puedes describir en lenguaje natural lo que quieres que pase — "cuando llegue un correo de un cliente nuevo, créalo en el CRM y notifica al equipo en Slack" — y Claude arma el flujo. Sin saber programar. Sin tocar N8N manualmente.

**Lo que hace exactamente:**

- Conecta Claude con más de 400 herramientas vía N8N
- Permite crear flujos de automatización con instrucciones en lenguaje natural
- Elimina la necesidad de configurar nodos en N8N manualmente
---

**Cómo instalarlo:**

```plain text
1. Necesitas una cuenta en n8n.io (tiene plan gratuito)
2. En N8N, activa la API y copia tu API key
3. En Claude, ve a Settings → Integrations → Add MCP Server
4. Agrega la URL del MCP de N8N con tu API key
```

**Prompt para crear una automatización:**

```plain text
Conecta con N8N y crea un flujo que haga lo siguiente:

Disparo: [qué evento activa el flujo]
Acción 1: [primera cosa que debe pasar]
Acción 2: [segunda cosa]
Condición: [si aplica alguna lógica]
Notificación final: [dónde y a quién]

Verifica que el flujo esté activo antes de confirmar.
```

---

### Skill 4 — LightRag

**Problema que resuelve:** Claude se pierde en proyectos grandes y empieza a inventar.

Cuando un proyecto tiene mucha información — documentos, decisiones, contexto acumulado — Claude puede contradecirse, olvidar partes importantes o simplemente adivinar. LightRag organiza toda esa información en una estructura que Claude puede navegar eficientemente, sin perderse ni fabricar respuestas.

**Lo que hace exactamente:**

- Organiza grandes volúmenes de información en grafos de conocimiento
- Permite a Claude recuperar contexto específico sin alucinaciones
- Es la diferencia entre un asistente que entiende tu proyecto y uno que adivina
---

**Cómo instalarlo:**

```plain text
1. Abre Claude Code
2. Ve a Settings → Skills → Explorar
3. Busca "LightRag"
4. Instala y carga los documentos de tu proyecto
```

**Prompt para usarlo en un proyecto real:**

```plain text
Usando LightRag, indexa estos documentos de mi proyecto:
[lista los archivos o pega el contenido]

Después responde:
¿Qué decisiones ya tomamos sobre [tema]?
¿Hay alguna contradicción entre los documentos?
¿Qué información falta para avanzar con [siguiente paso]?
```

---

### Skill 5 — Everything Claude Code

**Problema que resuelve:** Claude Code sin configurar tiene capacidades dispersas que hay que activar una por una.

Este es el más grande de los cinco. No es una habilidad puntual — es un departamento completo. Everything Claude Code agrupa en un solo paquete las capacidades de seguridad, herramientas de desarrollo, configuraciones avanzadas y flujos de trabajo que normalmente tendrías que configurar individualmente. Todo junto, todo gratis.

**Lo que hace exactamente:**

- Activa un conjunto completo de capacidades de Claude Code en un solo paso
- Incluye configuraciones de seguridad, herramientas de desarrollo y flujos preconfigurados
- Elimina la curva de configuración inicial de Claude Code
---

**Cómo instalarlo:**

```plain text
1. Abre Claude Code
2. Ve a Settings → Skills → Explorar → Plugins
3. Busca "Everything Claude Code"
4. Instala el paquete completo
5. Reinicia Claude Code para que todos los cambios apliquen
```

**Prompt para verificar la instalación:**

```plain text
¿Qué capacidades nuevas tengo disponibles ahora
con Everything Claude Code instalado?
Dame la lista organizada por categoría.
```

---

### Resumen rápido: los 5 skills y qué resuelve cada uno

:::callout
  **1. Claude Mem** → Claude recuerda quién eres entre sesiones

  **2. UI UX Pro Max** → Diseño profesional, no de plantilla

  **3. N8N MCP** → Automatizaciones con 400+ herramientas sin código

  **4. LightRag** → Claude no se pierde ni inventa en proyectos grandes

  **5. Everything Claude Code** → Departamento completo de capacidades en un clic

:::

---

### Limitación principal (para no frustrarte)

:::callout
  Algunos de estos skills requieren configuración inicial que va más allá de solo instalarlos — especialmente LightRag (necesitas cargar los documentos del proyecto) y N8N MCP (necesitas cuenta en N8N y configurar la API key). No son instalación de un clic para todos los casos. Dedica 20-30 minutos a configurar cada uno correctamente la primera vez y después funcionan solos.

:::

**Tip práctico:** empieza por **Claude Mem** — es el que más impacto inmediato tiene en el día a día y el más sencillo de configurar. Después agrega los demás según el problema que más te esté afectando hoy.

---

:::callout
  **Una pregunta antes de cerrar:**

  ¿Cuál de los cinco problemas — olvido de contexto, diseño genérico, falta de automatización, pérdida en proyectos grandes, o Claude Code sin configurar — te está costando más tiempo esta semana?

  Ese es el skill por donde empezar.

:::
