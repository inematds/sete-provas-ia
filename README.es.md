# 7 Pruebas para Cualquier IA

[![7 Pruebas para Cualquier IA](guia/assets/banner-es.jpg)](https://inematds.github.io/sete-provas-ia/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

Son siete encargos de trabajo listos para copiar: una página de ventas, un panel de ventas, una presentación, un explicativo animado, un editor de fotos, un juego 3D y una central de agentes. Cada encargo viene en tres formatos: para un agente que trabaja en una carpeta (Claude Code, Codex, Cursor), para una ventana de chat (Agnes, ChatGPT, Gemini) y como briefing para una persona, sin IA. Sirve para comparar modelos, elegir herramientas o capacitar a un equipo. Incluye los datos, las respuestas correctas y el evaluador por script; para usarlo basta con copiar el texto, y para el evaluador, tener Python 3.

## 📖 Guía de uso

Guía completa (landing + paso a paso, con un botón para copiar cada prompt): **https://inematds.github.io/sete-provas-ia/guia/es/**

## Las 7 pruebas

| # | Prueba | Archivo entregado | La parte difícil |
|---|---|---|---|
| 1 | Página de ventas | `index.html` | un solo camino (prueba gratis) y una escena que hace que dejes de desplazarte |
| 2 | Panel de ventas | `painel.html` | datos ensuciados a propósito: limpiarlos, mostrar qué se corrigió, hacer clic en el número |
| 3 | Presentación de ventas | `apresentacao.html` | precio que cambió, cuenta incorrecta y número prohibido en las notas |
| 4 | Explicativo animado | `explicativo.html` | 20 s sin voz, 1920 x 1080, en bucle, para un niño de 10 años |
| 5 | Editor de fotos | `editor.html` | 8 herramientas que funcionan de verdad |
| 6 | Juego de conducción 3D | `jogo.html` | divertido en 10 s, victoria y derrota |
| 7 | Central de agentes | `central.html` | pausar, detener, fallos y ejecuciones antiguas, con el agente detrás de una función |

## Los tres formatos

| Carpeta | Para | Qué cambia |
|---|---|---|
| `prompts/<idioma>/agente/` | Claude Code, Codex, Cursor, Antigravity, Gemini CLI, OpenCode | lee los datos de la carpeta, guarda archivos y un `ENTREGA.md` |
| `prompts/<idioma>/chat/` | Agnes, ChatGPT, Gemini, Claude.ai, DeepSeek, Grok, Copilot | responde con un único HTML; los datos se pegan al final del encargo |
| `prompts/<idioma>/pessoa/` | una persona o equipo, sin IA | tiempo sugerido y cómo se evaluará |

Idiomas: `pt`, `en`, `es`. Las imágenes y el video son opcionales en todos los formatos: quien tenga un generador (por ejemplo: Higgsfield, Agnes, Codex) lo usa; quien no, dibuja con código.

**Necesitas:** Python 3 (sin bibliotecas extra) y, de preferencia, Chrome o Chromium, que el evaluador usa para abrir la página oculta y leer los números que calcula el JavaScript; sin él, esos números pasan a AVISO. En Windows, usa `py` en lugar de `python3`. Sin git: "Code › Download ZIP". La **semilla** es un número fijo que hace que los datos salgan siempre iguales, por eso las respuestas nunca cambian. Los nombres de archivo y las columnas del CSV quedan en portugués a propósito, y los mensajes del evaluador están en portugués.

## El proceso, de principio a fin

| # | Paso | Comando | Quién lo hace |
|---|---|---|---|
| 1 | Generar los datos y las respuestas correctas (ya vienen listos; solo si se cambia la semilla) | `python3 kit/gerar_dados.py` | ⚙️ script |
| 2 | Armar los 21 prompts de cada idioma a partir de `kit/provas/<idioma>.json` y actualizar la guía | `python3 kit/montar.py` | ⚙️ script |
| 3 | Elegir prueba, formato y competidores | — | 🧠 tú |
| 4 | Preparar una carpeta por competidor (prompt + datos) | `python3 kit/preparar.py 2 corrida/claude/02 agente es` | ⚙️ script |
| 5 | Ejecutar: pegar el `PROMPT.md` en el agente o el chat, o entregárselo a la persona | — | 🤖 IA o 🧑 persona |
| 6 | Revisar lo que se puede medir sin IA | `python3 kit/avaliar.py 2 corrida/claude/02` (`--chat` para entrega de chat) | ⚙️ script |
| 7 | Abrir la entrega, usarla durante 5 min y completar la ficha de 10 puntos | `avaliar/ficha.es.md` | 🧠 tú |
| 8 | Comparar las fichas y anotar el tiempo y el costo de cada competidor | — | 🧠 tú |

Comprobaciones del kit: `python3 kit/gerar_dados.py --conferir` (los datos coinciden con la semilla) y `python3 kit/montar.py --conferir` (prompts y guías actualizados).

## Respuestas correctas (sin IA)

- **Prueba 2:** `vendas.csv` tiene 1.470 filas y cinco problemas introducidos. Limpio: 1.430 pedidos, R$ 50.162,10. Versión de chat (`vendas-mini.csv`): 224 pedidos, R$ 7.831,00. Limpieza de referencia: `python3 kit/limpar.py dados/vendas.csv`.
- **Prueba 3:** precio correcto R$ 89/kg (no 95), suma correcta: 157 personas (no 140), R$ 130 del competidor prohibidos. Todo está en `dados/gabarito.json`.

## Prueba real

Las pruebas 2 y 3 en formato chat se ejecutaron con Claude Sonnet (suscripción, conversación sin herramientas). Entregas y capturas en `exemplos/chat-sonnet/`. El formato todavía no se ha medido en Agnes ni en otros chats.

## Estructura

```
prompts/{pt,en,es}/{agente,chat,pessoa}/   21 prompts por idioma (generados)
kit/provas/{pt,en,es}.json                  fuente única de los prompts
kit/gerar_dados.py  kit/limpar.py  kit/avaliar.py  kit/montar.py  kit/preparar.py
dados/  vendas.csv  vendas-mini.csv  notas.txt (+ en/ es/)  gabarito.json
avaliar/ficha.es.md  ficha.en.md  ficha.md   ficha de 10 puntos (ES, EN, PT)
exemplos/chat-sonnet/                       prueba real en modo chat
guia/                                       landing + guía PT/EN/ES
```

Licencia MIT. Parte del ecosistema [INEMA.CLUB](https://inema.club).