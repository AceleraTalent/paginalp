> *Hasta ahora, crear video con IA requería entrar a Higgsfield, subir archivos, configurar parámetros, descargar el resultado y volver a tu flujo de trabajo. Con el MCP de Higgsfield conectado a Claude, todo eso desaparece le das instrucciones en lenguaje natural y Claude opera Higgsfield directamente.*

:::callout
  **Ideal para**

  - Founders y marketers que producen contenido visual
  - Agencias que crean ads para Meta / TikTok
  - Equipos que necesitan escalar producción de video
  - Cualquiera que ya use Claude y quiera agregarle video
:::

:::callout
  **Incluye**

  - Qué es el MCP de Higgsfield y por qué importa
  - Cómo configurarlo en menos de 2 minutos
  - 5 usos reales con prompts listos para copiar
  - Los modelos clave y cuándo usar cada uno
  - Limitación principal (para no frustrarte)
:::

---

### 1) Qué es esto (y por qué importa)

Higgsfield es una plataforma de generación de video con IA campañas para Meta, UGC ads, animaciones de producto, contenido editorial. Tiene modelos como Seedance 2.0, Kling 3.0 y Marketing Studio.

El MCP (Model Context Protocol) es un conector que le permite a Claude comunicarse directamente con Higgsfield. En lugar de usar dos apps, le das instrucciones a Claude en lenguaje natural y él opera Higgsfield por ti.

:::callout
  **Traducción a negocio:** menos fricción operativa, más velocidad de producción, y la capacidad de integrar video generativo dentro de workflows más grandes orquestados desde Claude.

:::

---

### 2) Cómo configurarlo

Son tres pasos. Tarda menos de 2 minutos.

---

**Paso 1: Obtén el link del MCP de Higgsfield**

Entra a [higgsfield.ai](http://higgsfield.ai) → ve a la sección de integraciones o MCP → copia el link del servidor MCP.

---

**Paso 2: Conéctalo en Claude**

Entra a **Claude → Customize → Connectors → Add Connector**.

Pega el link del MCP de Higgsfield y guarda.

---

**Paso 3: Verifica la conexión**

En cualquier conversación en Claude, escribe:

```plain text
¿Qué herramientas de Higgsfield tengo disponibles ahora mismo?
```

Si la conexión funciona, Claude lista los modelos y capacidades disponibles en tu cuenta.

:::callout
  **Nota:** necesitas una cuenta activa en Higgsfield con créditos disponibles. Las generaciones de video consumen créditos de tu cuenta de Higgsfield — no de Claude.

:::

---

### 3) Los modelos y cuándo usar cada uno

Higgsfield tiene varios modelos. Estos son los tres que más vas a usar desde Claude:

---

**Seedance 2.0**

El modelo más sólido para preservar identidad visual. Cuando subas una foto de persona o producto y necesites que el resultado sea fiel al original, este es el indicado.

*Usar para: UGC ads con avatar, videos de producto con continuidad visual, contenido de marca con personaje específico.*

---

**Kling 3.0**

El modelo cinematográfico. Produce la estética más premium — iluminación dramática, movimiento fluido, sensación de producción alta. Requiere una imagen de inicio.

*Usar para: campañas editoriales, contenido de lujo, videos de marca que necesitan estética cine.*

---

**Marketing Studio Video**

El modelo más directo para ads comerciales. Le das la URL de un producto o lo subes como imagen y genera un video listo para Meta o TikTok con presets de UGC, Tutorial, Unboxing, Product Review.

*Usar para: campañas de performance, ads de ecommerce, contenido de lanzamiento de producto.*

---

### 4) 5 usos reales con prompts

Cada uso incluye el prompt exacto que puedes copiar y adaptar.

---

#### 1. Campaña de producto para Meta desde una sola imagen

Sube la foto de tu producto a Claude y pídele que genere un video ad listo para Meta. Marketing Studio hace el resto.

```plain text
Tengo esta imagen de producto: [sube la foto].
Usa el MCP de Higgsfield con Marketing Studio Video.
Genera un video ad en formato 9:16 para Meta Stories.
Preset: Product Review.
El video debe mostrar el producto en uso, con iluminación cálida y movimiento suave.
Duración: 6 segundos.
```

---

#### 2. UGC ad con avatar propio

Si tienes un avatar entrenado en Higgsfield (o usas uno de los presets), Claude puede generar un UGC ad completo en un solo prompt.

```plain text
Usa el MCP de Higgsfield.
Genera un video UGC con el avatar [nombre del avatar].
El video debe durar 8 segundos, formato 9:16.
El avatar habla a cámara presentando [producto/servicio].
Tono: conversacional, confiado, sin exagerar.
Fondo: interior moderno, luz natural desde la izquierda.
```

---

#### 3. Video cinematográfico desde foto de referencia

Para contenido de marca premium — editorial, lujo, moda — Kling 3.0 con una imagen de inicio da los mejores resultados.

```plain text
Usa el MCP de Higgsfield con el modelo Kling 3.0.
Imagen de inicio: [sube la foto de referencia].
Anima esta escena con movimiento de cámara lento hacia adelante,
iluminación cinematográfica cálida, y profundidad de campo pronunciada.
Duración: 5 segundos. Formato: 16:9.
No añadas texto ni efectos adicionales.
```

---

#### 4. Animación de producto para ecommerce

Convierte una foto de producto estática en un video de 5-8 segundos con movimiento sutil — ideal para feeds de Instagram o carruseles animados.

```plain text
Usa el MCP de Higgsfield con Seedance 2.0.
Tengo esta foto de producto: [sube imagen].
Genera un video de 6 segundos donde el producto rota suavemente
sobre fondo blanco con iluminación de estudio.
El movimiento debe ser limpio, sin sacudidas, con sombra suave debajo del producto.
Formato: 1:1 para feed de Instagram.
```

---

#### 5. Múltiples variaciones para testing de ads

Este es el uso más potente: pedirle a Claude que genere varias versiones del mismo video con parámetros distintos para testear cuál performa mejor.

```plain text
Usa el MCP de Higgsfield.
Necesito 3 variaciones de un video ad para el mismo producto.
Variación 1: fondo blanco, tono minimalista, 6 segundos.
Variación 2: fondo oscuro, iluminación dramática, 6 segundos.
Variación 3: fondo de ambiente urbano exterior, luz natural, 6 segundos.
Usa Marketing Studio Video para las tres. Formato 9:16.
Imagen de producto: [sube imagen].
Genera las tres en secuencia y dime los IDs de cada trabajo.
```

---

### 5) Limitación principal (para no frustrarte)

:::callout
  Las generaciones de video son **asíncronas** — Claude inicia el trabajo y Higgsfield lo procesa en segundo plano. No hay resultado inmediato. Dependiendo del modelo y la carga del servidor, puede tardar entre 30 segundos y varios minutos. Claude te devuelve un job ID para hacer seguimiento.

:::

**Tip práctico:** cuando lances varias generaciones en paralelo, pídele a Claude que lleve un registro de los job IDs y los revise en orden una vez que pasen 2-3 minutos. Así no pierdes ningún resultado.

---
