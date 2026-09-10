> *Cada vez que termina una reunión importante, alguien tiene que entrar a Fathom, buscar la llamada, copiar el transcript, pedir un resumen y redactar el correo. Con Houston ese proceso queda automatizado desde la primera vez — después solo escribes un mensaje y el reporte llega solo.*

:::callout
  **Ideal para**

  - Equipos que graban llamadas con Fathom y reportan manualmente
  - Founders que necesitan mantener a su equipo informado sin hacerlo ellos
  - Comerciales que tienen muchas llamadas y pierden tiempo en el seguimiento
  - Cualquiera que haya enviado tarde un resumen de reunión por falta de tiempo
:::

:::callout
  **Incluye**

  - El problema real del proceso manual
  - Cómo configurar el agente paso a paso
  - El prompt exacto listo para copiar
  - Cómo conectar Fathom y Gmail vía Composio
  - Cómo usarlo después de cada llamada
  - Limitación principal a tener en cuenta
:::

---

### 1) El problema real del proceso manual

```plain text
Termina la reunión
        ↓
Entrar a Fathom
Buscar la llamada correcta
Abrir el transcript
Copiarlo completo
        ↓
Abrir ChatGPT o Claude
Pedir el resumen
Copiar el resultado
        ↓
Abrir Gmail
Redactar el correo
Buscar los correos de cada destinatario
Enviar
        ↓
15-30 minutos después de cada reunión
en trabajo que no aporta nada nuevo
```

:::callout
  **El problema no es que sea difícil. Es que es repetitivo, siempre igual, y consume tiempo después de cada llamada. Ese tipo de tarea es exactamente para lo que existen los agentes.**

:::

---

### 2) Cómo configurar el agente

---

**Paso 1: Instala Houston**

Entra a [gethouston.ai](http://gethouston.ai), descarga la app y crea tu cuenta con tu código de acceso.

---

**Paso 2: Conecta Fathom y Gmail vía Composio**

Houston se conecta a tus herramientas a través de **Composio**, una plataforma de integraciones que tiene cientos de apps listas para conectar. Dentro de Houston, busca las integraciones de:

- **Fathom** — donde están grabadas tus llamadas y los transcripts completos
- **Gmail** — desde donde el agente va a enviar los reportes automáticamente
:::callout
  **Nota sobre Composio:** es el puente entre Houston y tus herramientas externas. No necesitas configurar nada técnico — Houston te guía para conectar cada app. Si usas otra herramienta de grabación de llamadas (Otter, Fireflies, Zoom), verifica si Composio tiene esa integración disponible.

:::

---

**Paso 3: Crea el agente**

Dentro de Houston, crea un agente nuevo con un nombre claro:

```plain text
Reportes de reunión - [nombre de tu empresa]
```

---

**Paso 4: Pega el prompt exacto**

```plain text
Eres un agente encargado de enviar reportes de reuniones.

Cuando te indique una llamada, debes:
1. Buscar esa llamada en Fathom
2. Leer el transcript completo
3. Identificar y organizar:
   - Los temas principales que se trataron
   - Las decisiones que se tomaron
   - Las tareas asignadas con su responsable
   - Los próximos pasos acordados y sus fechas si existen
4. Redactar un correo claro y profesional con el resumen
5. Enviarlo por Gmail a la persona o personas que te indique

El correo debe ser directo y escaneable — con secciones cortas
y los puntos más importantes en negritas. No debe tomar más
de 2 minutos leerlo completo.
```

---

### 3) Cómo usarlo después de cada llamada

Una vez configurado, el flujo completo se activa con un solo mensaje en lenguaje natural:

```plain text
Envíales a Carolina y a Sebastián el resumen
de la última llamada con [nombre del cliente].
```

Houston hace todo lo demás:

---

**Busca la llamada en Fathom** — por nombre del cliente, fecha o cualquier referencia que le des.

---

**Lee el transcript completo** — no el resumen automático de Fathom, el transcript real, para no perderse ninguna decisión importante.

---

**Organiza el reporte** con:

- Temas tratados
- Decisiones tomadas
- Tareas con responsable y fecha
- Próximos pasos
---

**Redacta y envía el correo** — directo desde Gmail, a los destinatarios que indicaste, con el tono profesional y el formato escaneable.

:::callout
  **El resultado tangible:** tu equipo queda enterado de cada reunión importante sin que tú tengas que hacer el proceso manual cada vez. La información llega rápido, organizada y sin que se pierda nada relevante.

:::

---

### 4) Variaciones útiles del mismo agente

El mismo agente sirve para diferentes escenarios con pequeños ajustes en el mensaje:

---

**Reporte para el cliente directamente:**

```plain text
Envíales a [email del cliente] el resumen de nuestra
última llamada. Tono formal, sin mencionar nuestra
discusión interna de pricing.
```

---

**Reporte de todas las llamadas de la semana:**

```plain text
Crea un resumen consolidado de todas las llamadas
de esta semana y envíiaselo al equipo comercial.
Agrupa por cliente y destaca las oportunidades abiertas.
```

---

**Reporte con tareas extraidas al CRM:**

```plain text
Después de enviar el correo, extrae las tareas
del resumen y créalas en el CRM asignadas a cada responsable.
```

---

### 5) Limitación principal (para no frustrarte)

:::callout
  El agente trabaja con lo que está en el transcript. Si en la llamada se dijo algo importante de forma ambigua, el agente lo va a incluir tal como quedó — sin interpretar intenciones. Siempre revisa el primer reporte que genera para verificar que el tono y el nivel de detalle son los correctos para tus destinatarios. Después de ajustar el prompt una vez, los siguientes reportes salen bien sin necesidad de edición.

:::

**Tip práctico:** la primera vez que uses el agente con un cliente importante, revisa el correo antes de que lo envíe. Agrega al prompt: *"antes de enviar, muéstrame el borrador para aprobación"* hasta que confíes en el output.

---

:::callout
  **Una pregunta antes de cerrar:**

  ¿Cuántas reuniones de esta semana terminaron sin que el equipo recibiera un resumen de lo que se habló?

  Cada reunión sin reporte es una decisión que no llega a quien la necesita.

:::
