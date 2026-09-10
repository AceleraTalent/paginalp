> *Antes, si querías que Claude revisara algo todos los días, tenías que prenderlo tú, pedirle la tarea y esperar. Con Routines eso cambió: configuras una vez y Claude corre solo en la nube de Anthropic — con tu laptop apagada, mientras duermes.*

:::callout
  **Ideal para**

  - Usuarios de Claude Code con plan pago
  - Founders que quieren reportes automáticos sin hacer nada
  - Equipos que tienen tareas repetitivas diarias o semanales
  - Cualquiera cansado de tener que prender Claude para que trabaje
:::

:::callout
  **Incluye**

  - Qué es Routines y qué lo hace diferente
  - Cómo configurar una Routine paso a paso
  - 5 Routines listas para activar hoy
  - Cómo conectarla con tus herramientas
  - Limitación principal a tener en cuenta
:::

---

### 1) Qué es Routines y qué lo hace diferente

Routines es una función dentro de Claude Code que permite programar tareas para que se ejecuten automáticamente en la nube de Anthropic, sin depender de que tu computador esté encendido.

La diferencia con usar Claude manualmente:

```plain text
Antes:
Tú prendes la laptop
        ↓
Abres Claude
        ↓
Escribes la tarea
        ↓
Esperas el resultado
        ↓
Tu laptop tiene que estar prendida todo el tiempo

Con Routines:
Configuras la tarea una sola vez
        ↓
Claude la corre solo en la nube
        ↓
Tu laptop puede estar apagada
        ↓
El resultado llega solo, en el horario que definiste
```

:::callout
  **Traducción a negocio:** en lugar de ser tú quien activa a Claude todos los días, Claude trabaja en horario fijo sin que hagas nada después de la configuración inicial.

:::

:::callout
  **Estado actual:** Routines está en fase de vista previa (preview). Ya funciona y la puedes activar hoy, pero está disponible solo dentro de los planes pagos de Claude Code.

:::

---

### 2) Cómo configurar una Routine

Son tres pasos. Una vez configurada, no tienes que volver a tocarla.

---

**Paso 1: Describe la tarea en lenguaje normal**

No necesitas escribir código ni instrucciones técnicas. Explícale a Claude qué quieres que haga exactamente como se lo explicarías a alguien de tu equipo.

```plain text
Ejemplo:
"Todos los días revisa mis correos nuevos de las últimas 24 horas,
identifica los que requieren respuesta urgente, extrae las tareas
que me dejaron pendientes y envíame un resumen por correo antes
de las 7am."
```

---

**Paso 2: Define el horario**

Le dices cuándo correr. Las opciones disponibles:

- **Diario** — a una hora específica todos los días
- **Semanal** — un día y hora fija cada semana
- **Una sola vez** — en una fecha y hora específica
```plain text
Ejemplos de horario:
"Todos los días a las 7:00am"
"Cada lunes a las 8:00am"
"El viernes 25 de julio a las 6:00pm una sola vez"
```

---

**Paso 3: Conéctala con lo que necesita**

La Routine necesita acceso a las herramientas donde vive la información que va a procesar. Conecta lo que corresponda:

- **Documentos** — Google Drive, Notion, archivos locales
- **Herramientas** — Gmail, Calendar, Slack, CRM
- **Repositorios** — GitHub u otros si trabajas con código
Desde ahí, corre sola sin que hagas nada más.

---

### 3) 5 Routines listas para activar hoy

Copia cualquiera de estas, adáptala a tu contexto y ábrela en Claude Code.

---

**Routine 1: Resumen matutino diario**

```plain text
Tarea: Todos los días a las 6:45am revisa:
- Mis correos de las últimas 24 horas
- Mi calendario del día de hoy
- Las tareas pendientes en Notion

Crea un resumen con:
1. Las 3 cosas más importantes que tengo hoy
2. Los correos que necesitan respuesta urgente
3. Cualquier conflicto de agenda

Envíame el resumen por correo a [tu email].

Horario: Diario a las 6:45am
Conexiones: Gmail, Google Calendar, Notion
```

---

**Routine 2: Reporte semanal de proyectos**

```plain text
Tarea: Cada lunes a las 8:00am revisa el estado de todos
mis proyectos activos en Notion.

Para cada proyecto, díme:
- Qué avanzó la semana pasada
- Qué está bloqueado o atrasado
- Cuáles son las tareas críticas de esta semana

Envíame el reporte por correo con el asunto:
"Reporte semanal [fecha]"

Horario: Cada lunes a las 8:00am
Conexiones: Notion, Gmail
```

---

**Routine 3: Monitor de correos importantes**

```plain text
Tarea: Todos los días a las 12pm revisa mis correos
de las últimas 6 horas.

Identifica correos de: clientes actuales, prospectos,
o cualquiera que mencione palabras como "urgente",
"propuesta", "contrato" o "pago".

En vía de notificación directa: envíame un resumen
de esos correos con el remitente, el asunto y una
línea de contexto por cada uno.

Horario: Diario a las 12:00pm
Conexiones: Gmail
```

---

**Routine 4: Cierre semanal de ventas**

```plain text
Tarea: Cada viernes a las 5:00pm revisa el CRM
y el calendario de la semana.

Dame un resumen de:
- Cuántas reuniones tuve con prospectos o clientes
- Qué oportunidades avanzaron
- Qué seguimientos quedaron pendientes
- Cuál es el estado del pipeline hoy vs el lunes

Envíalo al equipo comercial: [emails]

Horario: Cada viernes a las 5:00pm
Conexiones: CRM, Google Calendar, Gmail
```

---

**Routine 5: Revisión de repositorio de código**

```plain text
Tarea: Todos los días a las 9:00am revisa los commits
del día anterior en el repositorio [nombre].

Dame un resumen de:
- Qué cambios se hicieron y por quién
- Si hay algún conflicto o problema detectado
- Los pull requests pendientes de revisión

Envíame el reporte por correo.

Horario: Diario a las 9:00am
Conexiones: GitHub, Gmail
```

---

### 4) Cómo activar Routines en Claude Code

```plain text
1. Abre Claude Code (versión de escritorio)
2. Asegúrate de tener un plan pago activo
3. Busca la sección "Routines" en el menú principal
4. Haz clic en "Nueva Routine"
5. Pega la descripción de la tarea en lenguaje normal
6. Define el horario
7. Conecta las herramientas necesarias
8. Activa la Routine
```

:::callout
  **Tip:** empieza con la Routine más simple — el resumen matutino diario. Es la que más impacto inmediato tiene y la más fácil de verificar que funciona correctamente antes de configurar flujos más complejos.

:::

---

### 5) Limitación principal (para no frustrarte)

:::callout
  Routines está en fase de vista previa — puede tener comportamientos inesperados o cambios en la interfaz mientras Anthropic la sigue desarrollando. Además, requiere plan pago de Claude Code: no está disponible en el plan gratuito. Si una Routine falla silenciosamente (no llega el reporte), verifica los logs de ejecución dentro de Claude Code para entender qué pasó.

:::

**Tip práctico:** las primeras semanas, revisa que cada Routine esté ejecutándose correctamente — especialmente si depende de herramientas con integraciones OAuth como Gmail o Notion, donde los permisos pueden expirar y necesitar re-autorización.

---

:::callout
  **Una pregunta antes de cerrar:**

  ¿Qué tarea haces tú manualmente todos los días — o deberías hacer y no haces — que podría correr sola a las 7am mientras todavía estás durmiendo?

  Esa es tu primera Routine.

:::
