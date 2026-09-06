**Cada PDF que subes a Claude se procesa y se cobra dos veces, **y Microsoft lanzó la solución gratis. Se llama **MarkItDown**, tiene alrededor de **173.000 estrellas en GitHub** y convierte cualquier documento en Markdown limpio para que solo pagues por las palabras. En esta guía te explico por qué los PDFs están consumiendo silenciosamente tu presupuesto de tokens, cómo solucionarlo con una sola línea de código y cómo configurar el servidor MCP para que Claude Desktop convierta automáticamente cada archivo.

:::callout
  Repo: 

:::

---

### Lo que aprenderás

- Por qué Claude cobra el procesamiento de tus PDFs de una forma que puede aumentar significativamente el consumo de tokens
- Qué es MarkItDown y cómo soluciona este problema
- Cómo instalarlo y utilizarlo con una sola línea de código
- Cómo configurar el servidor MCP para que Claude Desktop convierta automáticamente tus archivos
- Mejores prácticas y respuestas a las preguntas más comunes
---

### Requisitos previos

- [ ] **Python + pip** instalados: puedes descargarlos desde [python.org](http://python.org/)
- [ ] Un terminal que sepas abrir y utilizar (Terminal en Mac, iTerm o el terminal integrado de VS Code)
- [ ] **Claude Desktop** si quieres utilizar la configuración automática con MCP (opcional, pero recomendado)
- [ ] 5 minutos para completar la configuración
No necesitas conocimientos avanzados de programación. Si puedes copiar y pegar un comando, puedes hacerlo.

---

### Estás pagando el doble por cada PDF

Cuando subes un PDF, Claude no se limita a leer el texto. Convierte cada página en una imagen y luego extrae el texto sobre ella, lo que significa que terminas pagando por ambas cosas.

> 💸 **Los números:** La propia documentación de Anthropic estima que solo el texto puede representar entre **1.500 y 3.000 tokens por página**, y la imagen de cada página se suma a ese consumo. Un contrato de 20 páginas puede consumir **más de 60.000 tokens** antes de que alguien le haga siquiera una pregunta.

Si tú (o tu equipo) procesan documentos de clientes en Claude durante todo el día, aquí es donde tu consumo de tokens puede desaparecer silenciosamente.

---

### ¿Qué es MarkItDown?

MarkItDown es una herramienta gratuita y de código abierto de Microsoft que convierte archivos en Markdown limpio y optimizado para trabajar con modelos de lenguaje (LLM).

Es compatible con PDFs, documentos de Word, hojas de Excel, presentaciones de PowerPoint y mucho más. Solo tienes que indicarle un archivo y te lo devuelve como Markdown en texto plano. Los títulos y las tablas se mantienen durante la conversión, en lugar de convertirse en texto desordenado o difícil de interpretar.

> 💡 Una vez que tu documento está en Markdown, las imágenes de las páginas desaparecen por completo. Claude puede leer únicamente el texto, así que pagas por las palabras (**no por una imagen de cada página añadida al contenido).**

| **1. Tienes un documento** | Un PDF, documento de Word u hoja de Excel que normalmente subirías directamente a Claude |
|---|---|
| **2. MarkItDown lo convierte** | Un solo comando lo transforma en Markdown limpio, manteniendo los títulos, tablas y estructura |
| **3. Claude recibe solo texto** | Sin imágenes de las páginas, sin consumo innecesario — solo las palabras |
| **4. Pagas una fracción** | Las mismas respuestas, el mismo documento, pero con muchos menos tokens |

---

### Cómo instalarlo (online)

**Paso 1 — Instala el paquete:**

```bash
pip install 'markitdown[all]'
```

**Paso 2 — Convierte un archivo:**

```bash
markitdown contract.pdf -o contract.md
```

Eso es todo. Sube el archivo `.md` resultante a Claude en lugar del PDF y eliminarás el consumo de tokens asociado a las imágenes de las páginas.

> ✅ Convierte un PDF de varias páginas y pega el Markdown en Claude. Compara el consumo de tokens con el que genera subir el PDF original. La diferencia en documentos largos puede ser enorme.

---

### Configurar el servidor MCP 

Existe un servidor MCP oficial para MarkItDown, lo que permite que Claude Desktop convierta automáticamente cada archivo que subas.

**Paso 1 — Instala el servidor MCP:**

```bash
pip install markitdown-mcp
```

**Paso 2 — Añádelo a Claude Desktop:**

Abre el archivo de configuración de Claude Desktop (`claude_desktop_config.json`) desde **Settings → Developer → Edit Config** y añade:

```json
{
  "mcpServers": {
    "markitdown": {
      "command": "markitdown-mcp"
    }
  }
}
```

**Paso 3 — Reinicia Claude Desktop.**

Ahora Claude puede convertir cualquier archivo a Markdown por sí solo. Configúralo una vez y no tendrás que volver a preocuparte por ello.

---

### Mejores prácticas

- **Convierte cualquier documento de más de unas pocas páginas.** Cuanto más largo sea el documento, mayor será el ahorro. Los contratos, informes y briefs son donde más se nota el consumo adicional.
- **Procesa los documentos de tus clientes en lote.** Si trabajas con documentos durante todo el día, conviértelos primero con MarkItDown como un paso estándar de tu proceso.
- **Guarda los archivos Markdown.** Son más pequeños, fáciles de buscar y puedes reutilizarlos en futuras sesiones de Claude sin volver a pagar por los costos de conversión.
- **Usa el servidor MCP si trabajas principalmente con Claude Desktop.** Después de configurarlo una sola vez, no tendrás que hacer ningún esfuerzo adicional.