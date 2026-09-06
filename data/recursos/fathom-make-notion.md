> **Objetivo:** Cada vez que termines una llamada grabada en Fathom, el transcript aparece automáticamente como una nueva página en Notion.

---

### ¿Qué necesitas antes de empezar?

- ✅ Cuenta activa en **Fathom** (plan que permita API o Zapier/Make)
- ✅ Cuenta en [**Make.com**](http://Make.com) (plan gratuito funciona para empezar)
- ✅ Workspace de **Notion** con integración activa
- ✅ Una base de datos en Notion donde guardar los transcripts
---

### PASO 1 — Preparar Notion

#### 1.1 Crear la base de datos de llamadas

En tu Notion, crea una nueva base de datos (tipo Table) con estas columnas:

| Columna | Tipo |
|---|---|
| Nombre de la llamada | Title |
| Fecha | Date |
| Participantes | Rich Text |
| Duración | Rich Text |
| Transcript | Rich Text |
| Resumen | Rich Text |
| Action Items | Rich Text |
| Link a Fathom | URL |

#### 1.2 Conectar Notion con Make

1. Ve a **Notion → Settings → Connections → Develop or manage integrations**
1. Crea una integración nueva → llámala `Make Automation`
1. Copia el **Internal Integration Token** (lo vas a necesitar en Make)
1. Ve a tu base de datos en Notion → `...` → **Add connections** → selecciona tu integración `Make Automation`
---

### PASO 2 — Preparar Fathom

#### Opción A: Fathom vía Webhook (recomendado si tienes plan de pago)

1. Ve a **Fathom → Settings → Integrations → Webhooks**
1. Crea un nuevo webhook
1. Selecciona el evento: `call.completed` o `transcript.ready`
1. La URL del webhook la obtienes en Make (la configuras en el Paso 3)
#### Opción B: Fathom vía Zapier/Make nativo

1. Fathom tiene integración directa con Make en algunos planes
1. En Make, busca el módulo **Fathom** en el catálogo
1. Si no aparece, usa la Opción A (webhook)
---

### PASO 3 — Construir el escenario en Make

#### 3.1 Crear escenario nuevo

1. Entra a [**make.com**](http://make.com) → `Create a new scenario`
1. Haz clic en el `+` para agregar el primer módulo
#### 3.2 Configurar el trigger (disparador)

**Si usas Webhook de Fathom:**

- Busca y agrega: `Webhooks → Custom Webhook`
- Make te genera una URL → **copia esa URL**
- Pégala en Fathom (Paso 2, Opción A)
- Haz una llamada de prueba en Fathom para que Make detecte la estructura del JSON
**Si Fathom tiene módulo nativo:**

- Busca `Fathom` → selecciona `Watch Calls` o similar
- Autoriza tu cuenta de Fathom
#### 3.3 Agregar módulo de Notion

1. Haz clic en `+` para agregar otro módulo después del trigger
1. Busca **Notion**
1. Selecciona: `Create a Database Item`
1. Conecta tu cuenta de Notion con el token del Paso 1.2
1. Selecciona tu base de datos de llamadas
1. Mapea los campos:
```
Nombre de la llamada  → {{title}} o {{call_name}} del webhook
Fecha                 → {{created_at}} o {{date}}
Participantes         → {{attendees}} o {{participants}}
Transcript            → {{transcript}} o {{transcript_text}}
Resumen               → {{summary}}
Action Items          → {{action_items}}
Link a Fathom         → {{recording_url}}
```

> ⚠️ Los nombres exactos de las variables dependen del JSON que envía Fathom. Verifica los campos reales después de hacer una llamada de prueba.

#### 3.4 Guardar y activar el escenario

1. Haz clic en **Save** (💾)
1. Activa el escenario con el toggle ON/OFF
1. Cambia el intervalo de revisión si usas polling (cada 15 min es suficiente)
---

### PASO 4 — Probar la automatización

1. Haz una llamada de prueba en Fathom (puede ser contigo mismo, 1-2 minutos)
1. Espera a que Fathom genere el transcript (puede tardar unos minutos)
1. Verifica en Make → **Run history** que el escenario se ejecutó
1. Revisa tu base de datos en Notion → debe aparecer la nueva página con el transcript
---

### PASO 5 — Mejoras opcionales

#### Agregar procesamiento con IA (Claude o GPT)

Entre el trigger de Fathom y el módulo de Notion, puedes agregar:

- `HTTP → Make a request` a la API de Anthropic o OpenAI
- Envía el transcript como prompt
- Pide que extraiga: resumen ejecutivo, action items, decisiones clave
- Mapea la respuesta a los campos de Notion
#### Agregar notificación

- Agrega un módulo de **Gmail** o **Slack** al final del escenario
- Envía un mensaje cuando se guarde un nuevo transcript
---

### Troubleshooting común

| Problema | Solución |
|---|---|
| Make no recibe datos de Fathom | Verifica que el webhook URL esté bien pegado en Fathom |
| Error de permisos en Notion | Asegúrate de haber conectado la integración a esa base de datos específica |
| Los campos aparecen vacíos | Revisa el JSON del webhook en Make → Run history → ver datos reales |
| El transcript es muy largo | Notion tiene límite de 2000 chars por campo → divide en bloques |

---

### Recursos útiles

- [Documentación ](https://www.make.com/en/help)[Make.com](http://Make.com)
- [Fathom Integrations](https://fathom.video/integrations)
- [Notion API](https://developers.notion.com)
---

*Guía creada con Claude · Actualiza esta página con tus notas del proceso*

