> *Normalmente tenemos una reunión, hablamos de mil cosas, dejamos tareas — y esa información queda perdida entre el calendario, una grabación, notas, WhatsApp o la memoria. Con Houston, ese proceso se automatiza completamente: el agente guarda todo después de cada llamada y te prepara antes de la siguiente.*

:::callout
  **Ideal para**

  - Founders y comerciales con muchas reuniones a la semana
  - Equipos que pierden seguimientos entre llamadas
  - Quienes graban llamadas pero nunca revisan las grabaciones
  - Cualquiera que haya prometido algo en una reunión y se le olvidado
:::

:::callout
  **Incluye**

  - El problema real que resuelve este agente
  - Cómo configurarlo paso a paso
  - El prompt exacto para el agente (listo para copiar)
  - Qué hace automáticamente después de cada llamada
  - Cómo consultar el contexto antes de una reunión
  - Limitación principal a tener en cuenta
:::

---

### 1) El problema real

El flujo típico sin un agente:

```plain text
Reunión con cliente
        ↓
Información queda dispersa en:
calendario + grabación + notas sueltas + WhatsApp + memoria
        ↓
Próxima reunión
        ↓
Buscar qué pasó, qué prometimos, qué quedó pendiente
        ↓
Llegar sin contexto o con contexto incompleto
        ↓
Olvidar seguimientos. Perder tareas. Dañar la relación.
```

:::callout
  **Lo que cambia con Houston:** el agente captura automáticamente la información después de cada llamada, la organiza en Notion, y la tiene lista antes de la siguiente reunión. Tú no tienes que recordar nada — el agente lo recuerda por ti.

:::

---

### 2) Cómo configurarlo paso a paso

---

**Paso 1: Instala Houston**

Entra a [gethouston.ai](http://gethouston.ai), descarga la app para Mac o Windows y crea tu cuenta con tu código de acceso.

---

**Paso 2: Conecta las tres herramientas clave**

- **Google Calendar** — para que el agente detecte cuándo tienes reuniones y con quién
- **Tu herramienta de grabación de llamadas** — Fathom, Otter, Fireflies, o cualquier app donde queden las grabaciones y transcripciones
- **Notion** — donde el agente va a guardar los resúmenes, tareas y grabaciones de cada cuenta
:::callout
  **Nota clave:** la herramienta de grabación es el insumo más importante. Sin ella, el agente puede prepararte para la reunión pero no puede extraer automáticamente lo que se habló después. Si todavía no grabas tus llamadas, este es el momento de empezar.

:::

---

**Paso 3: Crea un agente nuevo en Houston**

Dentro de la app, crea un agente nuevo con un nombre claro:

```plain text
Memoria de clientes - [nombre de tu empresa]
```

---

**Paso 4: Pega el prompt exacto del agente**

Este es el prompt completo — adáptalo con el nombre de tu base de datos en Notion:

```plain text
Cada vez que tenga una reunión en mi calendario, identifica
el nombre de la persona y el cliente.

Cuando termine la llamada:
- Guarda el enlace de la grabación en mi base de datos de Notion
- Escribe el resumen de lo que se habló
- Extrae las tareas pendientes, quién es responsable de cada una
  y la fecha límite si existe
- Registra las decisiones importantes y los siguientes pasos acordados

Antes de la próxima reunión con esa persona:
- Revisa toda la información guardada anteriormente
- Prepárame un resumen con:
  1. Qué se habló la última vez
  2. Qué tareas quedaron pendientes y cuál es su estado
  3. Qué compromisos hice yo que debo haber cumplido
  4. Qué deberíamos revisar o avanzar en esta reunión
```

---

### 3) Qué hace automáticamente después de cada llamada

Una vez configurado, el flujo automático es:

---

**Termina la llamada** → Houston detecta que la reunión finalizó en el calendario.

---

**Accede a la grabación** → Toma el enlace o la transcripción de tu herramienta de grabación.

---

**Guarda en Notion automáticamente:**

- Resumen de lo que se habló
- Enlace a la grabación
- Decisiones importantes tomadas
- Tareas pendientes con responsable y fecha
- Siguientes pasos acordados
---

**Todo queda en la ficha de ese cliente en Notion** — acumulando historial con cada reunión. No hay nada que copiar, no hay nada que organizar manualmente.

---

### 4) Cómo consultar el contexto antes de una reunión

Cuando aparece una nueva reunión con ese cliente en tu calendario, simplemente le preguntas al agente:

```plain text
¿Qué pasó la última vez con [nombre del cliente]
y qué tenemos pendiente?
```

Houston revisa todo lo guardado en Notion sobre esa cuenta y te entrega en segundos:

- Lo que se habló en la última reunión
- Las tareas que quedaron abiertas
- Los compromisos que tú hiciste y debes haber cumplido
- Lo que vale la pena revisar o avanzar hoy
:::callout
  **El resultado tangible:** llegas a cada reunión con contexto completo, sin buscar nada, sin olvidar nada, sin improvisar. El cliente siente que lo conoces y que le das seguimiento real — y eso se traduce directamente en confianza y en cierres.

:::

---

### 5) Limitación principal (para no frustrarte)

:::callout
  Este flujo depende de que tus llamadas estén grabadas y la transcripción sea accesible para Houston. Si tienes reuniones presenciales o llamadas por WhatsApp sin grabación, el agente no puede extraer automáticamente lo que se habló — tendrías que dictarle un resumen manual después. Además, Houston corre sobre tu propia API de GPT, así que los costos de tokens se acumulan con el uso.

:::

**Tip práctico:** para reuniones sin grabación, crea el hábito de mandarle al agente una nota de voz de 60 segundos con lo más importante apenas termine la reunión. El agente lo procesa igual y lo guarda en Notion con el mismo formato.

---

:::callout
  **Una pregunta antes de cerrar:**

  ¿Cuántos seguimientos importantes se te han caído en los últimos tres meses porque la información de la reunión quedó perdida en alguna parte?

  Ese es exactamente el costo de no tener esto configurado.

:::
