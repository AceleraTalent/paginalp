> *La mayoría de personas le piden a Claude una respuesta. Los mejores usuarios le piden cinco — de cinco agentes distintos que se contradicen entre sí, encuentran los huecos del otro, y al final producen un veredicto que ningún agente solo hubiera dado.*

:::callout
  **Ideal para**

  - Founders antes de lanzar un producto o cambiar precio
  - Equipos que necesitan validación real, no cheap yes-men
  - Cualquiera que vaya a tomar una decisión cara e irreversible
  - Consultores que quieren una segunda (y tercera) opinión instantánea
:::

:::callout
  **Incluye**

  - Qué es Claude Council y cómo funciona
  - Los 5 agentes y qué busca cada uno
  - Cómo activarlo y el prompt base
  - 4 casos de uso reales con ejemplos
  - Cómo leer el veredicto del Chairman
  - Limitación principal a tener en cuenta
:::

---

### 1) Qué es Claude Council (y por qué importa)

Claude Council es un skill que convierte a Claude en un panel de cinco asesores que evalúan tu idea desde ángulos opuestos. No te dicen qué quieres escuchar — te dicen lo que necesitas saber antes de que sea caro.

El flujo es así: presentas tu idea o decisión. Los cinco agentes responden de forma independiente. Luego cada uno lee las respuestas de los otros y encuentra los puntos ciegos. Finalmente, un **Chairman** lee todo y produce el veredicto final.

:::callout
  **Traducción a negocio:** antes de lanzar un producto, cambiar un precio, contratar a alguien, o invertir tres semanas construyendo algo — puedes someter la decisión a un panel que se presiona a sí mismo. Sin validación barata. Sin "sí, excelente idea".

:::

---

### 2) Los 5 agentes y qué busca cada uno

Cada agente tiene un rol fijo. No se solapan. Cada uno mira tu idea desde un ángulo que los demás ignoran deliberadamente.

---

**Agente 1 — El Crítico**

Busca el error fatal. El hueco que te va a hundir. Su trabajo no es destruirte — es encontrar lo que tú no quieres ver porque estás muy dentro de la idea.

*Pregunta que siempre hace: ¿Qué tiene que ser verdad para que esto falle?*

---

**Agente 2 — El Estratega**

Pregunta si siquiera estás resolviendo el problema correcto. Puede que tu solución sea buena pero el problema no valga la pena resolver.

*Pregunta que siempre hace: ¿Es este el problema correcto?*

---

**Agente 3 — El Optimista**

Busca el upside que estás dejando de ver. Lo que podrías estar subestimando. El potencial que no estás explotando.

*Pregunta que siempre hace: ¿Qué oportunidad estás ignorando?*

---

**Agente 4 — El Cliente**

Reacciona como alguien sin contexto. Como tu cliente real que no sabe nada de tu industria, tu jerga, ni tu lógica interna. Si él no lo entiende, nadie lo entiende.

*Pregunta que siempre hace: ¿Por qué debería importarme esto?*

---

**Agente 5 — El Pragmático**

Solo quiere saber qué deberías hacer mañana. No en seis meses. Mañana. Corta toda la teoría y va directo a la acción concreta más próxima.

*Pregunta que siempre hace: ¿Cuál es el siguiente paso real?*

---

**El Chairman**

Lee las respuestas de los cinco, identifica los puntos de acuerdo, los conflictos, y los puntos ciegos que ningún agente vio. Produce el veredicto final: una síntesis que no es el promedio de las opiniones — es una posición nueva construida sobre el debate.

---

### 3) Cómo activarlo

Para usar Claude Council necesitas el skill instalado en Claude Cowork. Una vez instalado, el comando base es:

```plain text
/council [describe tu idea, decisión o situación]
```

**Prompt base para cualquier decisión:**

```plain text
/council Estoy considerando [decisión concreta].

Contexto:
- Situación actual: [dónde estás hoy]
- Lo que quieres lograr: [objetivo específico]
- Recursos disponibles: [tiempo, dinero, equipo]
- Lo que ya intentaste: [si aplica]
- Lo que más te preocupa: [tu mayor duda]

Necesito que el panel evalúe esto sin filtros.
```

:::callout
  **Tip clave:** entre más contexto real le des, más útil es el panel. No escribas la versión bonita de tu idea — escribe la versión honesta con los problemas incluidos.

:::

---

### 4) 4 casos de uso reales

---

#### Antes de lanzar un producto

```plain text
/council Voy a lanzar [producto/servicio] en [fecha].
Precio: [precio]. Cliente objetivo: [descripción].
Lo que lo diferencia: [diferenciador].
Mi mayor miedo: que nadie lo compre porque [razón].
Evalúen si debo lanzar, esperar o cambiar algo antes.
```

---

#### Antes de cambiar un precio

```plain text
/council Quiero subir el precio de [producto] de [precio actual] 
a [precio nuevo].
Razón: [por qué quieres subirlo].
Mi base de clientes actual: [descripción].
Mi miedo: perder [X]% de clientes.
Evalúen el timing, el riesgo y cómo comunicarlo.
```

---

#### Antes de contratar a alguien

```plain text
/council Estoy considerando contratar a [rol] con un salario de [monto].
El problema que quiero resolver: [descripción].
Mi situación financiera actual: [contexto].
Lo que me frena: [duda principal].
Evalúen si es el momento correcto y si este es el rol correcto.
```

---

#### Antes de pivotar o cambiar dirección

```plain text
/council Llevo [tiempo] haciendo [cosa actual] y los resultados son [resultado].
Estoy considerando cambiar a [nueva dirección].
Lo que me hace querer cambiar: [razón].
Lo que perdería si cambio: [costo del pivote].
Evalúen si es un pivote válido o si estoy huyendo del trabajo difícil.
```

---

### 5) Cómo leer el veredicto del Chairman

El veredicto final no es un resumen — es una posición. El Chairman toma los cinco análisis, identifica dónde están de acuerdo, dónde se contradicen, y qué dejó de ver el panel completo.

Lo que debes buscar en el veredicto:

- **El punto de convergencia:** en qué coincidieron los cinco agentes — eso es lo que más peso tiene
- **El conflicto principal:** dónde el Crítico y el Optimista discreparon más — ahí está la tensión real de tu decisión
- **La acción del Chairman:** el paso concreto que recomienda — no el que te gusta, el que tiene más soporte del panel
:::callout
  **Regla de uso:** si el veredicto te dice algo que no quieres escuchar, esa es exactamente la razón por la que lo pediste. La validación barata ya la tienes gratis en cualquier otro lado.

:::

---

### 6) Limitación principal (para no frustrarte)

:::callout
  Claude Council no reemplaza la decisión — la informa. El panel puede darte el análisis más sólido del mundo pero la ejecución, el contexto que no pusiste en el prompt, y las variables humanas siguen siendo tuyas. Un panel de IA que se presiona a sí mismo sigue siendo tan bueno como la información que le diste.

:::

**Tip práctico:** usa Council para decisiones donde ya tienes opinión formada. El valor no es que te diga qué hacer — es que te muestre los ángulos que tu opinión ya formada está ignorando.

---

:::callout
  **Una pregunta antes de cerrar:**

  ¿Cuál es la última decisión importante que tomaste basándote solo en tu propia opinión — y cómo salió?

  Ese es exactamente el caso de uso por donde empezar con Council.

:::
