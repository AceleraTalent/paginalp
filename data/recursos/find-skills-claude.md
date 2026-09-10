> *El error más común con los Skills de Claude no es no usarlos — es intentar encontrar el correcto por tu cuenta. Existen casi 60,000 skills repartidos en cientos de repositorios. El skill número uno de todo el ecosistema, Find Skills, resuelve exactamente ese problema: tú le dices qué quieres lograr, y él encuentra el mejor skill para ese trabajo exacto.*

:::callout
  **Ideal para**

  - Cualquiera que use Claude Code regularmente
  - Equipos técnicos que quieren dejar de reinventar soluciones
  - Founders que automatizan procesos con Claude
  - Personas cansadas de buscar skills manualmente en GitHub
:::

:::callout
  **Incluye**

  - Qué es Cross AI Tools y por qué importa
  - Qué es Find Skills y cómo funciona exactamente
  - Cómo instalarlo (comando exacto)
  - Cómo verificar seguridad antes de instalar cualquier skill
  - El flujo completo: encontrar, verificar, instalar
  - 3 ejemplos de uso real
  - Limitación principal a tener en cuenta
:::

---

### 1) Qué es Cross AI Tools (y por qué importa)

[Cross AI Tools](https://crossaitools.com) es un directorio que indexa automáticamente skills, servidores MCP y marketplaces de Claude Code — organizado por categorías como frontend, backend, testing, seguridad, DevOps, documentación y más de 24 categorías adicionales.

El problema que resuelve es simple: hay skills para programar, para investigar, para escribir — pero están dispersos en cientos de repositorios distintos de GitHub. Sin un índice central, encontrar el skill correcto para tu tarea específica es adivinar a ciegas.

:::callout
  **Traducción práctica:** en lugar de buscar en GitHub repositorio por repositorio, tienes un solo lugar donde comparar popularidad, categoría y seguridad de cualquier skill antes de instalarlo.

:::

---

### 2) Qué es Find Skills y cómo funciona

Find Skills es el skill número uno de todo el directorio — con casi 2 millones de instalaciones. Su función es resolver exactamente el problema de “cuál skill debería usar para esto”.

**Cómo trabaja:**

1. Le dices a Claude qué estás intentando hacer (en lenguaje natural, sin nombrar ningún skill específico)
1. Busca en el ecosistema abierto de skills en lugar de hacer que reinventes la solución
1. Verifica la calidad de cada opción revisando el número de instalaciones y la reputación de la fuente
1. Prioriza opciones probadas de fuentes confiables (como vercel-labs o anthropics) sobre paquetes desconocidos con pocas instalaciones
1. Te recomienda el skill que realmente encaja con tu flujo de trabajo
:::callout
  **Por qué importa esto:** en lugar de adivinar qué skill instalar, Claude hace la búsqueda, la verificación de calidad y la comparación por ti. Tú solo describes el problema.

:::

---

### 3) Cómo instalarlo

La instalación es un solo comando desde tu terminal, dentro de Claude Code:

```bash
npx -y skills add vercel-labs/skills --skill find-skills --agent claude-code
```

Este comando instala Find Skills directamente en la carpeta `.claude/skills` de tu proyecto actual.

:::callout
  **Nota:** necesitas tener Claude Code instalado y Node.js disponible en tu máquina para ejecutar `npx`. Si no tienes Claude Code, instálalo primero desde la documentación oficial de Anthropic.

:::

---

### 4) Cómo verificar seguridad antes de instalar cualquier skill

Esta es la parte que la mayoría de personas se va a saltar — y después se va a arrepentir.

**No instales skills aleatorios directamente desde GitHub sin revisarlos primero.** Cross AI Tools tiene una sección de auditoría que clasifica cada skill según su nivel de riesgo antes de que lo pegues en Claude:

---

**Seguro** — el skill fue revisado y no presenta comportamientos sospechosos. Puedes instalarlo con confianza razonable.

---

**Con alertas** — el skill tiene comportamientos que requieren tu atención antes de instalar (por ejemplo, acceso a archivos sensibles o ejecución de comandos poco comunes). Revisa qué hace exactamente antes de continuar.

---

**Alto riesgo** — el skill presenta patrones que podrían comprometer tu sistema o tus datos. Evita instalarlo a menos que entiendas exactamente qué hace y confíes plenamente en la fuente.

:::callout
  **Regla de oro:** un skill no es solo texto — puede incluir instrucciones que Claude ejecuta con acceso a tu sistema. Revisar la auditoría de seguridad antes de instalar no es opcional, es el paso que más gente se salta y el que más problemas previene.

:::

---

### 5) El flujo completo

El proceso, de principio a fin, son tres pasos:

---

**Paso 1: Encuentra el skill**

Descríbele a Claude (con Find Skills instalado) qué estás intentando lograr. Él busca y compara opciones por ti.

```plain text
Necesito un skill que me ayude a [tarea específica].
Busca en el ecosistema de skills disponible y dime
cuáles son las 3 mejores opciones, con su número
de instalaciones y la reputación de la fuente.
```

---

**Paso 2: Revisa si es seguro**

Antes de instalar cualquier sugerencia, verifica su clasificación de seguridad en Cross AI Tools — búscalo directamente en el sitio o pídele a Claude que te confirme si tiene alertas conocidas.

---

**Paso 3: Instálalo**

Una vez confirmada la seguridad, usa el comando de instalación que te proporciona el sitio (similar al de Find Skills) para agregarlo a tu proyecto.

:::callout
  **El cambio real:** Claude deja de actuar como un chatbot en blanco que necesita que le expliques todo desde cero, y empieza a actuar como si ya supiera hacer el trabajo — porque ya tiene el skill específico cargado para esa tarea.

:::

---

### 6) 3 ejemplos de uso real

---

**Buscando un skill para revisión de código**

```plain text
Necesito que Claude revise mis pull requests automáticamente
antes de hacer merge. Busca el mejor skill para esto
en el ecosistema disponible.
```

---

**Buscando un skill para documentación**

```plain text
Quiero generar documentación técnica automática a partir
de mi código. Encuentra el skill más confiable para esto,
priorizando fuentes con buena reputación.
```

---

**Buscando un skill para investigación**

```plain text
Necesito un skill que me ayude a investigar competidores
y generar reportes estructurados. Busca opciones probadas
y dime cuál tiene mejor relación entre instalaciones y calidad.
```

---

### 7) Limitación principal (para no frustrarte)

:::callout
  Find Skills te recomienda opciones basadas en popularidad y reputación de la fuente — pero eso no garantiza que el skill sea perfecto para tu caso específico. Un skill con muchas instalaciones puede estar optimizado para un flujo de trabajo distinto al tuyo. Siempre lee la descripción completa del skill (el archivo [SKILL.md](http://SKILL.md)) antes de instalarlo a ciegas, incluso si viene recomendado.

:::

**Tip práctico:** instala primero a nivel de proyecto, no global. Así pruebas el skill en un contexto controlado antes de decidir si quieres tenerlo disponible en todos tus proyectos.

---

:::callout
  **Una pregunta antes de cerrar:**

  ¿Cuántas veces le pediste a Claude algo que ya existía como skill probado, sin saberlo, y terminaste reconstruyendo la solución desde cero?

  Ese es exactamente el tiempo que Find Skills te devuelve.

:::
