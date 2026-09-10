## Obsidian + Nexus + Claude: Construye un Second Brain que realmente recuerda tu trabajo

Claude puede ser muy bueno, pero cada conversación empieza sin contexto. Este sistema convierte nuestras notas, decisiones y proyectos en una fuente organizada de información que podemos reutilizar.

:::callout
  **Ideal para**

  - Consultores, founders, managers y profesionales que trabajan con muchos proyectos.
  - Equipos que quieren dejar de perder decisiones entre WhatsApp, Drive, reuniones y chats.
  - Personas que ya usan Claude o Claude Code.
  - Personas que quieren que su conocimiento siga siendo suyo y viva en archivos propios.
:::

:::callout
  **Al terminar tendremos**

  - Un vault de Obsidian organizado.
  - Una estructura clara para notas, proyectos y reuniones.
  - Una nota central de contexto para Claude.
  - Un sistema para convertir reuniones y aprendizajes en conocimiento reutilizable.
  - Una ruta técnica opcional para conectar Claude Code con Nexus.
:::

---

### 1. Antes de empezar: entender qué estamos construyendo

Obsidian no es una app de notas tradicional: trabaja con una carpeta local de archivos Markdown. Eso significa que nuestro sistema es **portable**: las notas siguen siendo archivos simples que podemos abrir y mover incluso fuera de Obsidian.

Markdown también nos ayuda a mantener el contenido “limpio”: texto, títulos, listas y tablas que sobreviven al tiempo. En un Second Brain, esto importa porque nuestro conocimiento no debería depender de una plataforma específica.

Claude no debe ser el lugar donde guardamos todo. Claude nos ayuda a **pensar, organizar, resumir y encontrar patrones** sobre información que ya tenemos ordenada. Obsidian es el “cerebro de conocimiento”. Nexus es la “memoria técnica” que usamos con Claude Code para dar continuidad entre proyectos y sesiones.

| Capa | Para qué sirve | Ejemplos |
|---|---|---|
| Obsidian | Guardar y organizar conocimiento | Reuniones, clientes, ideas, decisiones, aprendizajes |
| Claude | Analizar, resumir y conectar conocimiento | Encontrar patrones, crear planes, detectar contradicciones |
| Nexus | Dar continuidad técnica a Claude Code | Decisiones de arquitectura, patrones de código, contexto entre proyectos |

:::callout
  Claude y Nexus no “leen todo automáticamente”. Nuestro sistema funciona mejor cuando **decidimos** qué carpetas, proyectos y datos se conectan, y con qué permisos.

:::

---

### 2. Ruta A: configurar Obsidian en menos de 20 minutos

Esta ruta construye la base del sistema. Si solo hacemos una cosa hoy, que sea esto.

#### Paso 1 — Crear el vault

1. Descargar e instalar Obsidian desde su sitio oficial.
1. Abrir Obsidian.
1. Seleccionar **Create new vault**.
1. Nombrarlo exactamente:
```plain text
Second Brain
```

1. Guardarlo en una carpeta fácil de encontrar, por ejemplo:
```plain text
Documentos/Second Brain
```

No conviene guardar el vault dentro de Descargas ni en una carpeta temporal: si se mueve o se borra, se rompe el hábito y se pierde continuidad.

#### Paso 2 — Activar las tres configuraciones obligatorias

Ir a:

```plain text
Settings → Files and links
```

Configurar:

1) Activar:

```plain text
Automatically update internal links
```

Esto evita enlaces rotos cuando renombramos notas.

2) En “Default location for new attachments”, elegir:

```plain text
In the folder specified below
```

Esto evita adjuntos dispersos en cualquier carpeta.

3) En “Attachment folder path”, escribir:

```plain text
_attachments
```

Esto mantiene imágenes y PDFs ordenados y fáciles de respaldar.

#### Paso 3 — Crear la estructura exacta de carpetas

Crear estas carpetas exactamente así:

```plain text
00 Inbox
10 Atlas
20 Calendar
30 Efforts
90 Templates
_attachments
```

- `00 Inbox`: notas rápidas que todavía no hemos organizado.
- `10 Atlas`: conocimiento que no caduca.
- `20 Calendar`: reuniones, diario, revisiones semanales y notas con fecha.
- `30 Efforts`: proyectos activos con principio y final.
- `90 Templates`: plantillas para crear notas más rápido.
- `_attachments`: imágenes, PDFs y archivos adjuntos.
:::callout
  No creemos veinte carpetas por tema. La estructura debe ayudarnos a guardar rápido, no obligarnos a pensar demasiado antes de escribir.

:::

---

### 3. Las cuatro notas que debemos crear el primer día

Crear estas notas y ubicarlas así:

| Nota | Carpeta | Qué debe contener |
|---|---|---|
| Inicio | Raíz del vault | Links a proyectos, reuniones, decisiones y notas importantes |
| Contexto General | 10 Atlas | Quiénes somos, qué hacemos, objetivos, herramientas y prioridades |
| Decisiones | 10 Atlas | Decisiones importantes y por qué se tomaron |
| Revisión Semanal | 20 Calendar | Qué aprendimos, qué se bloqueó y qué sigue |

Contenido exacto para copiar dentro de `Contexto General`:

```markdown
# Contexto General

## Quiénes somos
[Escribir aquí quiénes somos y qué hacemos.]

## Qué vendemos o construimos
[Productos, servicios, proyectos o iniciativas.]

## Objetivos actuales
-
-
-

## Proyectos activos
-
-
-

## Herramientas que usamos
-
-
-

## Decisiones importantes
-
-
-
```

:::callout
  Esta nota es nuestra “pieza central”: cuando Claude no tiene contexto, esta es la primera referencia que podemos pegar o resumir.

:::

---

### 4. Cómo capturar información sin que el sistema se vuelva pesado

Regla simple:

**Todo entra primero por Inbox. Solo organizamos cuando la nota ya es útil.**

Esto reduce fricción. Nuestro objetivo no es “orden perfecto”, es **continuidad**.

#### Ejemplo 1 — Después de una reunión

Crear una nota en:

```plain text
20 Calendar
```

Título:

```plain text
2026-06-22 — Reunión con [Cliente]
```

Plantilla:

```markdown
# Reunión con [Cliente]

## Qué se habló
-

## Decisiones tomadas
-

## Próximos pasos
-

## Riesgos o bloqueos
-

## Información que debemos recordar
-
```

#### Ejemplo 2 — Idea importante

Guardar en:

```plain text
10 Atlas
```

Título:

```plain text
Idea — [Nombre corto de la idea]
```

#### Ejemplo 3 — Proyecto activo

Guardar en:

```plain text
30 Efforts
```

Título:

```plain text
Proyecto — [Nombre del proyecto]
```

Contenido:

```markdown
# Proyecto — [Nombre]

## Objetivo
## Entregables
## Estado actual
## Próximos pasos
## Decisiones
## Links relacionados
```

---

### 5. Cómo conectar nuestras notas con Claude

No necesitamos instalar diez plugins para empezar. Lo más práctico es usar Claude como “motor de síntesis” y Obsidian como “fuente de verdad”.

#### Uso 1 — Convertir una reunión en acciones

Prompt exacto:

```plain text
Voy a pegar las notas de una reunión.

Haz tres cosas:
1. Resume las decisiones tomadas.
2. Extrae tareas con responsable y fecha si aparecen.
3. Identifica riesgos, preguntas abiertas y datos que faltan.

No inventes información.
Devuelve el resultado en formato Markdown listo para pegar en Obsidian.

[PEGAR NOTAS]
```

#### Uso 2 — Encontrar patrones entre varias notas

```plain text
Analiza estas notas de reuniones y proyectos.

Identifica:
- Problemas que se repiten.
- Decisiones contradictorias.
- Oportunidades que no estamos aprovechando.
- Las tres prioridades más importantes para esta semana.

No inventes información. Cita de qué nota viene cada hallazgo.

[PEGAR NOTAS]
```

#### Uso 3 — Convertir conocimiento suelto en una nota útil

```plain text
Convierte esta información desordenada en una nota para Obsidian.

Usa esta estructura:
# Título
## Resumen
## Ideas principales
## Decisiones
## Próximas acciones
## Notas relacionadas

No agregues información externa. Solo organiza lo que ya existe.

[PEGAR INFORMACIÓN]
```

---

### 6. Ruta B: usar Nexus con Claude Code (opcional)

:::callout
  Esta ruta es opcional. Está pensada para personas que usan Claude Code, trabajan con repositorios, automatizaciones, código o proyectos técnicos. No es necesaria para empezar a usar Obsidian.

:::

Antes de instalar Nexus necesitamos:

- [ ] Claude Code instalado.
- [ ] Git instalado.
- [ ] Node.js en la versión requerida por el repositorio oficial.
- [ ] pnpm instalado.
- [ ] Un proyecto o repositorio que queramos registrar.
- [ ] Acceso al README oficial de Nexus.
Regla:

**No copiar comandos de TikTok, Reels o YouTube sin comparar primero con el README oficial del repositorio. Los comandos pueden cambiar.**

#### Instalación desde el repositorio oficial

Si el repositorio o la estructura real difieren, usar:

`[REVISAR README OFICIAL]`

Comandos (plantilla; validar en el repo oficial):

```bash
git clone [URL_OFICIAL_DEL_REPO_DE_NEXUS]
```

Clona el repositorio en nuestra máquina.

```bash
cd Nexus
```

Entra a la carpeta del proyecto (puede llamarse distinto).

```bash
pnpm install
```

Instala dependencias del proyecto.

```bash
pnpm build
```

Compila el proyecto.

```bash
node packages/cli/dist/index.js init
```

Ejecuta el asistente de inicialización (la ruta puede cambiar). `[REVISAR README OFICIAL]`

Durante `init` normalmente vamos a:

1. Crear o guardar la clave de cifrado.
1. Elegir el proveedor de modelo.
1. Autorizar o configurar Claude Code.
1. Registrar el primer proyecto.
1. Completar el chequeo de salud.
1. Reiniciar Claude Code al terminar.
:::callout
  **Seguridad:** guardar la clave de cifrado en un gestor de contraseñas. Si se pierde, podemos perder acceso a la memoria local de Nexus.

:::

---

### 7. Cómo comprobar que Nexus está funcionando

Estos comandos son ejemplos comunes; si no existen en nuestra instalación, usar:

`[REVISAR README OFICIAL]`

```bash
nexus status
```

Deberíamos ver el estado del servicio/CLI y configuración básica.

```bash
nexus project list
```

Deberíamos ver proyectos registrados (aunque sea uno).

```bash
nexus query "decisiones importantes"
```

Deberíamos obtener resultados del contexto/memoria disponible (si ya registramos contenido).

Prompts para Claude Code:

```plain text
Explícame este proyecto como si acabara de entrar al equipo.
Primero revisa el contexto disponible y luego indícame:
1. Qué hace el proyecto.
2. Qué decisiones importantes ya existen.
3. Qué partes no debería modificar sin revisar dependencias.
4. Qué preguntas siguen abiertas.
```

```plain text
Antes de proponer cambios, revisa si existe una decisión,
patrón o nota previa relacionada con este tema.

Luego responde:
- Qué ya sabemos.
- Qué conflicto podría aparecer.
- Qué archivos o proyectos podrían verse afectados.
- Qué deberíamos validar antes de implementar.
```

---

### 8. Los tres errores que debemos evitar

#### Error 1 — Intentar organizar todo desde el primer día

Primero capturamos. Luego organizamos solo lo que volvemos a usar. El hábito gana al “sistema perfecto”.

#### Error 2 — Convertir Obsidian en una carpeta muerta

Cada semana revisamos Inbox, proyectos activos y decisiones. Si no hay revisión, el sistema deja de “recordar”.

#### Error 3 — Conectar información sensible sin pensar

Antes de conectar archivos, repositorios o notas con herramientas de IA, revisamos permisos, secretos, datos de clientes y documentos confidenciales. Nuestro sistema debe ser útil **y** seguro.

---

### 9. Rutina semanal de 15 minutos

- [ ] Vaciar `00 Inbox`.
- [ ] Mover notas útiles a Atlas, Calendar o Efforts.
- [ ] Actualizar proyectos activos.
- [ ] Registrar decisiones importantes.
- [ ] Revisar qué aprendimos esta semana.
- [ ] Pedirle a Claude que encuentre prioridades, riesgos y patrones.
:::callout
  No necesitamos construir un sistema perfecto hoy. Solo necesitamos crear un lugar donde el conocimiento importante deje de perderse. Empecemos con un vault, una nota de contexto y una reunión bien documentada.

:::
