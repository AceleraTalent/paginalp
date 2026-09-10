> *Normalmente después de una llamada comercial tenemos la grabación por un lado, las notas por otro, la información del cliente en el CRM y el logo en Drive. Y terminamos esperando días para mandar algo que debería salir mientras la conversación todavía está fresca. Con Houston, el primer borrador está listo apenas termina la llamada.*

:::callout
  **Ideal para**

  - Consultores y agencias que mandan propuestas después de cada reunión
  - Equipos comerciales que tardan días en armar una propuesta
  - Negocios que quieren personalizar sin hacerlo manualmente
  - Cualquiera que haya perdido un cliente por tardar demasiado en responder
:::

:::callout
  **Incluye**

  - El problema real del proceso actual
  - Cómo configurar el agente paso a paso
  - El prompt exacto listo para copiar
  - Qué produce el agente y cómo se ve el resultado
  - Limitación principal a tener en cuenta
:::

---

### 1) El problema real del proceso actual

El flujo típico después de una reunión comercial:

```plain text
Reunión termina
        ↓
Grabación en una app
Notas en otra
Info del cliente en el CRM
Logo en Drive
Propuesta vieja en otro documento
        ↓
Pasar horas buscando todo
Armar el documento desde cero
Cambiar logos y colores manualmente
Escribir la propuesta
        ↓
1, 2 o varios días después…
La propuesta sale cuando la conversación ya se enfrió
```

:::callout
  **La propuesta perfecta llega tarde y pierde fuerza. Una propuesta buena que llega hoy cierra más que una propuesta perfecta que llega en tres días.**

:::

---

### 2) Cómo configurar el agente

---

**Paso 1: Instala Houston**

Entra a [gethouston.ai](http://gethouston.ai), descarga la app y crea tu cuenta con tu código de acceso.

---

**Paso 2: Conecta las herramientas donde vive tu información**

- **Herramienta de grabación de llamadas** — Fathom, Otter, Fireflies o la que uses. El agente necesita acceso a la transcripción de cada reunión.
- **CRM o Notion** — donde está el historial del cliente, sus datos, su contexto y las interacciones anteriores.
- **Google Drive** — donde tienes logos, colores de marca, documentos del cliente y propuestas anteriores.
- **Herramienta de propuestas o presentaciones** — Google Slides, Notion, Canva, o donde crees tus propuestas.
:::callout
  **Nota:** entre más información del cliente tenga disponible el agente (logo, colores, propuestas anteriores, historial en CRM), más personalizada va a ser la propuesta. No es magia — es el agente cruzando todo lo que ya existe.

:::

---

**Paso 3: Crea un agente nuevo**

Dentro de Houston, crea un agente nuevo con un nombre claro:

```plain text
Generador de propuestas comerciales - [nombre de tu empresa]
```

---

**Paso 4: Pega el prompt exacto**

Este es el prompt completo — adáptalo según tus herramientas y tu estructura de propuesta:

```plain text
Cada vez que termine una reunión comercial, revisa la transcripción
de la llamada e identifica:
- Quién es el cliente y a qué se dedica su empresa
- Qué problemas mencionó específicamente
- Qué objetivos quiere lograr
- Qué dijo que necesita
- Qué objeciones aparecieron
- Cuáles son los siguientes pasos acordados

Desppués revisa el CRM, Notion y Drive para encontrar:
- Logo y colores de la empresa
- Servicios o soluciones relevantes para este cliente
- Propuestas anteriores y documentos relacionados
- Historial de interacciones previas

Con toda esa información, crea una propuesta comercial personalizada
que incluya:
1. Contexto del cliente y su situación actual
2. Los problemas específicos que mencionó (sus palabras, no genérico)
3. La solución propuesta con alcance y entregables claros
4. Siguientes pasos concretos
5. Un correo listo para enviar presentando la propuesta

Usa el branding del cliente (logo, colores) y nuestra estructura
de propuesta. No incluyas servicios que no mencionó ni necesitó.
```

---

### 3) Qué produce el agente y cómo se ve

Una vez configurado, el flujo automático después de cada reunión:

---

**El agente lee la transcripción** → extrae los problemas reales del cliente en sus propias palabras, no en lenguaje genérico de propuesta.

---

**Cruza con la información del cliente** → busca en CRM, Notion y Drive el logo, los colores, el historial y las propuestas anteriores.

---

**Construye la propuesta personalizada** con:

- **Contexto real** — lo que la empresa hace y cuál es su situación actual según lo que se habló
- **Sus problemas específicos** — escritos con las palabras del cliente, no con jerga genérica
- **La solución enfocada** — solo lo relevante para este cliente, sin relleno
- **Alcance y entregables claros** — qué incluye, qué no incluye, cuánto tarda
- **Siguientes pasos** — qué pasa después de que aprueben
- **Branding del cliente** — logo y colores integrados, no pegados encima
---

**Genera el correo de envío** — listo para pegar en Gmail, con el tono correcto y el contexto de la reunión incluido.

:::callout
  **La diferencia que percibe el cliente:** no es una presentación genérica con el logo pegado encima. Es una propuesta que demuestra que entendiste exactamente qué necesita su empresa. Eso solo ya justifica el sí.

:::

---

### 4) Limitación principal (para no frustrarte)

:::callout
  El agente produce un **primer borrador**, no una propuesta final lista para enviar sin revisar. Siempre revisa antes de mandar — especialmente los números, los plazos y los compromisos específicos. El valor real está en que el 80% del trabajo ya está hecho y tú solo ajustas el 20% restante.

  Además, Houston corre sobre tu propia API de GPT. Una propuesta que requiere leer una transcripción larga más documentos del cliente puede consumir una cantidad relevante de tokens. Mide el costo real en las primeras semanas antes de escalar.

:::

**Tip práctico:** crea una estructura de propuesta modelo en Notion o Drive que el agente use como base. Entre más clara sea esa estructura, menos ajustes necesitarás en cada borrador.

---

:::callout
  **Una pregunta antes de cerrar:**

  ¿Cuántas propuestas salieron tarde en los últimos tres meses — y cuántas de esas oportunidades se enfriaron antes de que llegara la respuesta?

  Ese es el costo real de no automatizar esto.

:::
