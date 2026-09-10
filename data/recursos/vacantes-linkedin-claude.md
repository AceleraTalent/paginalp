> *La mayoría de personas busca trabajo revisando plataformas manualmente, aplicando a ciegas y esperando. Con Claude + Apify, subes tu hoja de vida, escribes un prompt y en menos de 10 segundos recibes más de 20 vacantes alineadas con tu perfil exacto, el salario de cada una y un porcentaje real de probabilidad de entrevista.*

:::callout
  **Ideal para**

  - Profesionales en búsqueda activa de empleo
  - Personas que quieren salarios más altos
  - Quienes están hartos de aplicar a ciegas
  - Cualquiera que quiera saber exactamente dónde tiene probabilidades reales
:::

:::callout
  **Incluye**

  - Cómo funciona el sistema
  - Configuración de Apify en Claude (una sola vez)
  - El actor de LinkedIn que necesitas instalar
  - El prompt exacto para buscar vacantes
  - Cómo interpretar los resultados
  - Limitación principal a tener en cuenta
:::

---

### 1) Cómo funciona el sistema

Apify es una plataforma de web scraping que tiene actores — scrapers especializados para sitios específicos. El actor de LinkedIn Job Search extrae vacantes en tiempo real directamente de LinkedIn con todos sus detalles: cargo, empresa, salario, ubicación y requisitos.

Cuando conectas Apify con Claude, Claude puede ejecutar ese scraper, recibir los resultados y cruzarlos con tu hoja de vida para darte un análisis personalizado: qué vacantes encajan, cuánto pagan, y qué tan probable es que te llamen.

:::callout
  **Traducción práctica:** en lugar de buscar tú en LinkedIn y filtrar manualmente, le delegas toda la búsqueda a Claude. Tú solo revisas los resultados y decides dónde aplicar.

:::

---

### 2) Configuración (una sola vez, dos minutos)

---

**Paso 1: Instala Apify en Claude**

Abre Claude → haz clic en **Connectors** → busca **Apify** → instálalo.

---

**Paso 2: Crea tu cuenta en Apify**

Entra a [apify.com](http://apify.com), crea una cuenta gratis. No necesitas plan pago para empezar.

---

**Paso 3: Copia tu API key**

Dentro de Apify, ve a **Settings → Integrations** y copia tu API key. Pégala en Claude cuando te la pida al activar el conector.

---

**Paso 4: Instala el actor de LinkedIn**

Entra a este link directo:

[apify.com/bebity/linkedin-premium-actor](http://apify.com/bebity/linkedin-premium-actor)

Busca **LinkedIn Job Companies** y guarda el actor en tu cuenta. Con esto Claude ya puede ejecutar búsquedas de vacantes en tiempo real.

:::callout
  **Nota:** esta configuración se hace una sola vez. Después de esto, cada búsqueda tarda menos de 10 segundos desde Claude.

:::

---

### 3) El prompt exacto para buscar vacantes

Una vez configurado, sube tu hoja de vida a Claude y usa este prompt:

```plain text
Aquí está mi hoja de vida: [adjunta el archivo]

Usa el conector de Apify con el actor de LinkedIn Job Search.

Busca vacantes en [ciudad o remoto] para perfiles como el mío.
Filtros: [industria o cargo objetivo], salario mínimo [monto si aplica].

Para cada vacante que encuentres dame:
1. Cargo y empresa
2. Salario o rango salarial
3. Requisitos principales
4. Porcentaje de match con mi perfil (0-100%)
5. La razón principal por la que encajo o no encajo

Ordénalas de mayor a menor probabilidad de entrevista.
```

:::callout
  **Tip:** entre más específico seas con la ciudad, el cargo y el salario mínimo, mejores son los resultados. No pongas filtros muy amplios o recibes vacantes irrelevantes.

:::

---

### 4) Cómo interpretar los resultados

Claude te devuelve una lista ordenada. Así la lees:

---

**El porcentaje de match**

No es un número inventado — Claude lo calcula cruzando los requisitos de la vacante con tu experiencia, habilidades y formación. Un 85%+ significa que cumples la mayoría de los criterios. Por debajo del 60%, la aplicación necesita una carta de presentación muy fuerte.

---

**La razón de encaje o no encaje**

Esta es la parte más valiosa. Si Claude te dice “te falta experiencia en [habilidad específica]”, ya sabes qué mencionar en tu carta o cómo enmarcar tu CV para esa vacante.

---

**El orden de la lista**

Aplica en orden. Las primeras vacantes son donde tienes más probabilidad de llegar a entrevista. No pierdas tiempo aplicando de abajo hacia arriba.

---

**Prompt de seguimiento para prepararte:**

```plain text
Toma la vacante #1 de la lista.
Dame:
1. Las 3 preguntas más probables que me van a hacer en la entrevista
2. Cómo debo responder cada una basándote en mi hoja de vida
3. Qué debo destacar en el primer párrafo de mi carta de presentación
```

---

### 5) Limitación principal (para no frustrarte)

:::callout
  Apify consume créditos por cada búsqueda. El plan gratuito incluye créditos mensuales suficientes para varias búsquedas, pero si haces muchas consultas al día puedes agotar el cupo. Además, LinkedIn bloquea scrapers periódicamente — si una búsqueda falla, espera unas horas e inténtalo de nuevo.

:::

**Tip práctico:** no hagas búsquedas genéricas. Cada búsqueda bien filtrada vale más que diez búsquedas amplias. Usa bien tus créditos.

---

:::callout
  **Una pregunta antes de cerrar:**

  ¿Cuántas vacantes rechazaste en el último mes porque no sabías si realmente encajabas o cuánto pagaban?

  Ese es el costo real de buscar trabajo sin esto.

:::
