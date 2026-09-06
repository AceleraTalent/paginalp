> *Normalmente reclutar significa horas filtrando CVs, respondiendo correos uno por uno y coordinando horarios entre candidatos y entrevistadores. Con Houston, tú solo llegas a la parte importante: conocer a los mejores candidatos y tomar la decisión final.*

:::callout
  **Ideal para**

  - Founders que reclutan sin equipo de RRHH
  - Equipos pequeños que abren vacantes cada cierto tiempo
  - Empresas que quieren profesionalizar su proceso sin contratar un reclutador
  - Cualquiera que haya perdido candidatos buenos por responder tarde
:::

:::callout
  **Incluye**

  - Qué hace el agente reclutador exactamente
  - Cómo configurarlo paso a paso
  - El prompt exacto listo para copiar
  - Cómo usarlo desde la vacante hasta la entrevista
  - El resumen pre-entrevista de cada candidato
  - Limitación principal a tener en cuenta
:::

---

### 1) Qué hace el agente reclutador

El proceso típico sin un agente:

```plain text
Publicas la vacante
        ↓
Llegan CVs por correo o LinkedIn
        ↓
Alguien lee cada CV manualmente
Filtra los que no cumplen
Clasifica los que sí cumplen
        ↓
Redacta correos individuales para cada candidato
        ↓
Coordina horarios de entrevista uno por uno
        ↓
Prepara qué preguntar en cada entrevista
        ↓
Horas invertidas antes de hablar con el primer candidato
```

Con el agente de Houston:

```plain text
Tú das la vacante y el perfil
        ↓
Houston revisa los CVs, clasifica y crea el ranking
        ↓
Redacta los correos de invitación a entrevista
        ↓
Revisa el calendario y propone horarios disponibles
        ↓
Prepara el resumen de cada candidato antes de la reunión
        ↓
Tú solo llegas a la entrevista
```

:::callout
  **Traducción a negocio:** el agente no toma la decisión de contratar — tú decides. Lo que hace es eliminar todo el trabajo operativo antes de llegar a esa decisión.

:::

---

### 2) Cómo configurarlo paso a paso

---

**Paso 1: Instala Houston**

Entra a [gethouston.ai](http://gethouston.ai), descarga la app y crea tu cuenta con tu código de acceso.

---

**Paso 2: Conecta las herramientas clave**

- **Gmail** — donde llegan los CVs y desde donde salen los correos a candidatos
- **Google Calendar** — para revisar disponibilidad y proponer horarios de entrevista
- **Google Drive o Notion** — donde el agente guarda los CVs clasificados, el ranking y los resúmenes de cada candidato
:::callout
  **Nota:** si recibes CVs por LinkedIn o por un ATS (Applicant Tracking System), verifica si Houston tiene integración directa o si necesitas reenviar los archivos por correo para que el agente los procese.

:::

---

**Paso 3: Crea el agente**

Dentro de Houston, crea un agente nuevo con un nombre claro:

```plain text
Reclutador - [nombre de tu empresa]
```

---

**Paso 4: Pega el prompt exacto**

Adáptalo según tu proceso y tus herramientas:

```plain text
Actuar como reclutador para mi empresa.

Cuando te comparta una vacante:
1. Identifica el perfil ideal con los requisitos mínimos y deseables
2. Revisa los CVs recibidos en Gmail
3. Clasifica a los candidatos según los requisitos de la vacante
4. Crea un ranking con los mejores perfiles, explicando por qué
   cada uno encaja o no encaja
5. Redacta correos personalizados para invitar a entrevista
   a los candidatos del top del ranking
6. Revisa mi calendario y propone tres opciones de horario
   disponible para cada entrevista
7. Guarda el ranking y los resúmenes en Notion

Antes de cada entrevista, prepárame un resumen del candidato que incluya:
- Su experiencia relevante para esta vacante
- Sus fortalezas principales
- Posibles dudas o puntos débiles a explorar
- Las 5 preguntas que debería hacerle en la entrevista
```

---

### 3) Cómo usarlo desde la vacante hasta la entrevista

Una vez configurado, el flujo completo empieza con un solo mensaje:

```plain text
Tengo una vacante nueva.

Cargo: [nombre del cargo]
Equipo: [área o equipo al que pertenece]
Experiencia requerida: [años y tipo]
Habilidades imprescindibles: [lista]
Habilidades deseables: [lista]
Modalidad: [presencial / remoto / híbrido]
Fecha de inicio esperada: [fecha]

Reporta a: [cargo del jefe directo]
Salario ofrecido: [rango si aplica]

Revisa los CVs que han llegado por correo y crea el ranking.
```

A partir de ahí, Houston trabaja automáticamente y te entrega:

---

**El ranking de candidatos** — ordenados de mayor a menor encaje con la vacante, con una justificación corta para cada posición del ranking.

---

**Los correos listos para enviar** — personalizados para cada candidato del top del ranking, con el nombre de la empresa, el cargo y las opciones de horario incluidas.

---

**Los horarios propuestos** — basados en la disponibilidad real de tu calendario, sin que tengas que revisar nada manualmente.

---

### 4) El resumen pre-entrevista

Antes de cada entrevista, le preguntas al agente:

```plain text
Prepárame para la entrevista con [nombre del candidato].
```

Houston revisa el CV y todo lo guardado en Notion y te entrega:

- **Experiencia relevante** — solo lo que aplica a esta vacante, no todo el historial
- **Fortalezas principales** — lo que destaca del perfil para este rol específico
- **Puntos débiles o dudas** — lo que vale la pena explorar en la conversación
- **5 preguntas sugeridas** — diseñadas para evaluar exactamente los requisitos de la vacante
:::callout
  **El resultado tangible:** llegas a cada entrevista con contexto completo del candidato y preguntas preparadas. No improvisas, no pierdes tiempo en preguntas genéricas — vas directo a lo que necesitas saber para tomar la decisión.

:::

---

### 5) Limitación principal (para no frustrarte)

:::callout
  El agente clasifica y rankea candidatos con base en el texto del CV — no puede evaluar el fit cultural, el lenguaje corporal ni nada que no esté escrito. Un candidato puede rankear alto en papel y no ser el indicado. El agente elimina el trabajo operativo de filtrado, pero la decisión final siempre es tuya.

  Además, si los CVs llegan en formatos poco estándar (escaneos de imagen, PDFs muy diseñados sin texto seleccionable), el agente puede tener dificultad para extraer la información correctamente.

:::

**Tip práctico:** en el correo de la vacante, pide a los candidatos que envíen el CV en formato Word o PDF de texto plano. Eso mejora significativamente la precisión del análisis del agente.

---

:::callout
  **Una pregunta antes de cerrar:**

  ¿Cuántas horas invirtió tu equipo en la última contratación en tareas que no tienen nada que ver con evaluar si el candidato es el indicado?

  Ese es exactamente el trabajo que este agente te quita de encima.

:::
