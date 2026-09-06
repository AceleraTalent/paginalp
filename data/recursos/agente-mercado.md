:::callout
   En una tarde puedes armar un agente que te pregunte qué vas a cocinar, calcule ingredientes, pida confirmación y después te deje el carrito listo en el Éxito.

:::

### Introducción

Hacer mercado online es aburrido

La solución que te voy a enseñar) es un agente conversacional: tú le dices qué tienes antojo de cocinar, el agente te hace un par de preguntas, calcula ingredientes con cantidades exactas, te pide confirmación… y *solo cuando tú dices “sí”*, abre [exito.com](http://exito.com) con Playwright y te arma el carrito completo, solito.

Esta guía es para gente **no técnica**. Si sabes copiar/pegar, abrir VS Code y seguir pasos, estás listo.

---

### Lo que necesitas antes de empezar

Antes de arrancar, revisa que tengas esto:

- VS Code instalado
- Cuenta en Claude con plan **Pro** (mínimo)
- Node.js instalado
- Extensión de Claude para VS Code: **Claude Code**
---

:::callout
  **Tip:** si algo te suena chino (Node, terminal, etc.), tranquilo: acá vas por pasos y copiando comandos.

:::

### Paso 1 — Instalar VS Code y Node.js

- **VS Code:** descárgalo e instálalo desde: [https://code.visualstudio.com](https://code.visualstudio.com)  
- **Node.js:** descárgalo e instálalo desde: [https://nodejs.org](https://nodejs.org) (recomendado: versión LTS)
:::figure Screenshot 2026-04-29 at 7.24.49 AM.png

---

### Paso 2 — Abrir Claude Pro y crear el proyecto

¿Por qué Pro? Porque para construir cosas así de rápido (y pedirle a Claude que te arme el proyecto completo, con archivos y comandos) lo ideal es usar **Claude Code** y un flujo donde el modelo tenga “herramientas” para trabajar como dev.

Qué vas a hacer:

1. Entra a Claude y asegúrate de tener **Pro** activo.
1. En VS Code, instala/activa **Claude Code**.
1. Crea una carpeta nueva para tu proyecto, por ejemplo: `agente-exito`.
1. Abre esa carpeta en VS Code (File → Open Folder).
  :::figure Screenshot 2026-04-29 at 7.25.26 AM.png

  :::figure Screenshot 2026-04-29 at 7.26.02 AM.png

1. Ahí mismo vas a construir y correr el agente.
:::figure Screenshot 2026-04-29 at 7.26.35 AM.png

---

### Paso 3 — El prompt exacto para construirlo (copia y pega tal cual)

Este es el corazón de la guía. Copia esto y pégalo en Claude (idealmente usando Claude Code dentro de VS Code) para que te genere el proyecto completo.

```plain text
Actúa como un dev senior paciente y un profe bacano. Vamos a construir un agente conversacional por terminal en Node.js que use Playwright para armar un carrito de mercado en exito.com.

OBJETIVO
Crear una app de consola que:
1) El usuario escribe qué quiere cocinar (ej: "quiero hacer pasta", "tengo antojo de bandeja paisa", "quiero sancocho").
2) El agente propone 2–3 opciones de recetas concretas relacionadas para que el usuario elija (numeradas 1, 2, 3).
3) Cuando el usuario elige, el agente pregunta: "¿Para cuántas personas?"
4) El agente calcula una lista de ingredientes con cantidades exactas (en unidades claras: g, ml, unidades, tarros, etc.) ajustada al número de personas.
5) El agente muestra la lista completa y pregunta si confirma o si quiere ajustar:
   - Si quiere ajustar, permitir: cambiar cantidades, quitar ingrediente, agregar ingrediente.
   - Repetir confirmación hasta que el usuario diga "confirmo".
6) SOLO cuando el usuario confirma, el agente abre Playwright (Chromium), entra a https://www.exito.com, y por cada ingrediente:
   - Busca el ingrediente.
   - Selecciona el producto más relevante.
   - Lo agrega al carrito.
   - Maneja popups/modales comunes (bienvenida, cookies, registro/login).
   - Si toca hacer scroll o cargar más, hacerlo.
7) Al terminar, el agente dice: "Listo, tu carrito quedó armado. Ya puedes revisar y pagar."

REQUISITOS DE IMPLEMENTACIÓN
- Node.js (ESM o CommonJS, pero consistente).
- Playwright.
- Conversacional por terminal usando readline/promises.
- Código organizado en archivos:
  - src/index.js (o .ts si decides TypeScript)
  - src/recipes.js (o recipes.ts) con 6–10 recetas base y sus ingredientes por 2 personas (para escalar).
  - src/exito.js (o exito.ts) con las funciones de Playwright para abrir el sitio, buscar y agregar al carrito.
  - src/utils.js con helpers (normalización de texto, delays, logging).
- Manejo básico de errores:
  - Si un ingrediente NO se encuentra en el sitio:
    - Buscar con una variante (sin marcas, sin tildes, sin palabras extra).
    - Si aún no aparece, escoger el producto más similar (por nombre) y MOSTRÁRSELO al usuario en consola (nombre + precio si se puede).
    - Preguntar: "¿Lo agrego? (s/n)".
    - Solo agregar si el usuario aprueba.
- No avanzar a Playwright hasta tener confirmación explícita del usuario.
- El flujo debe ser claro, con mensajes en español latino y tono cercano.

MANEJO DE POPUPS (IMPORTANTÍSIMO)
En el código de Playwright incluye una función `dismissPopups(page)` que intente:
- Aceptar o cerrar el modal de cookies (buscar botones tipo "Aceptar", "Entendido", "Aceptar todas", "Cerrar").
- Cerrar popups de bienvenida (botón X).
- Cerrar o minimizar banners flotantes.
- Si aparece un modal de login/registro, cerrarlo (no vamos a loguearnos en este MVP).
Debe ser tolerante a fallos (try/catch, timeouts cortos) y llamarse:
- después de cargar el home
- después de cada búsqueda
- antes de intentar clickear "Agregar" (para no fallar por overlays)

ENTREGABLES
1) Estructura de carpetas final.
2) package.json con scripts:
   - "start": "node src/index.js" (o equivalente)
3) Instrucciones exactas para correrlo.
4) Código completo de todos los archivos.

IMPORTANTE
- Usa selectores robustos (role, text, locators) y espera por navegación.
- Comenta el código en lo mínimo necesario (no biblias), pero sí deja claro qué hace cada parte.
- Si hay decisiones (por ejemplo, cómo identificar el botón de agregar), propon 2 opciones y elige una.

Ahora genera el proyecto completo con los archivos y el código.
```

---

### Paso 4 — Instalar Playwright

En la terminal de VS Code (Terminal → New Terminal), corre esto:

```bash
npm install playwright
npx playwright install
```

Cómo correr el agente cuando ya esté listo:

```bash
npm start
```

Si tu proyecto quedó con otro comando (por ejemplo `node src/index.js`), usa el que Claude te deje en el `package.json` (pero la idea es que sea `npm start`).

---

### Paso 5 — Cómo hablarle al agente (ejemplos reales)

Arranca el programa, y habla como si le estuvieras escribiendo a un amigo que cocina y es ordenado.

Ejemplos para iniciar:

- “Quiero hacer pasta para hoy”
- “Tengo antojo de bandeja paisa”
- “Ayúdame a hacer un sancocho para 6 personas”
#### Así se ve un flujo completo (ejemplo)

**Tú:** Quiero hacer pasta para hoy  

**Agente:** Listo. ¿Cuál de estas te provoca?
1) Pasta boloñesa clásica
2) Pasta cremosa con pollo
3) Pasta con atún y tomate  

**Tú:** 1  

**Agente:** ¿Para cuántas personas?  

**Tú:** 4  

**Agente:** De una. Para 4 personas, necesitas:
- 400 g pasta
- 500 g carne molida
- 1 tarro salsa de tomate
- 1 cebolla
- 2 dientes de ajo
- 1 cucharada aceite de oliva
- Sal y pimienta

¿Confirmas esta lista o quieres ajustar algo? (confirmo / ajustar)  

**Tú:** confirmo  

**Agente:** Perfecto. Abriendo [exito.com](http://exito.com) y armando tu carrito…  

**Agente:** (va agregando ingredientes…)  

**Agente:** Listo, tu carrito quedó armado. Ya puedes revisar y pagar.

---

### Paso 6 — Cómo el agente maneja los popups del Éxito

Esto es de las cosas que más rompe automatizaciones. La clave es que en el prompt (el de arriba) le dejaste una instrucción explícita a Claude:

- Cerrar popups de bienvenida (el típico “X”)
- Aceptar/cerrar el modal de cookies
- Manejar modales de login/registro (cerrarlos)
- Hacer scroll si no aparecen productos de una
- Volver a llamar `dismissPopups(page)` *después de cada acción grande* (entrar, buscar, antes de click)
Traducción al mundo real: el agente no se queda “pegado” porque había una ventana tapando el botón.

---

:::figure Imagen del recurso original

### Paso 7 — Qué hacer si un producto no aparece

Este es el “plan B” inteligente, y también lo dejas claro en el prompt.

Regla práctica:

- Si no existe el producto exacto, el agente busca algo **parecido**.
- Te muestra la alternativa en consola.
- Te pregunta: **“¿Lo agrego? (s/n)”**
- Solo lo mete al carrito si tú apruebas.
Eso evita que el agente te compre cualquier cosa rara sin permiso.

---

### Cierre

Esto suena a magia, pero en serio: hoy cualquier persona lo puede armar en una tarde con buenas instrucciones y las herramientas correctas.

Y el que aprende a hacer esto tiene una ventaja enorme:

- para recuperar tiempo,
- para montar automatizaciones en su negocio,
- o incluso para vender este tipo de soluciones.
**CTA:** si quieres que te mande esta guía en limpio (y con una checklist imprimible), escríbeme la palabra **ÉXITO**.
