# 7 Tests for Any AI

[![7 Tests for Any AI](guia/assets/banner-en.jpg)](https://inematds.github.io/sete-provas-ia/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

Seven ready-to-copy work assignments: a sales page, a sales dashboard, a presentation, an animated explainer, a photo editor, a 3D game, and an agent hub. Each assignment comes in three forms: for an agent that works in a folder (Claude Code, Codex, Cursor), for a chat window (Agnes, ChatGPT, Gemini), and as a brief for a person, without any AI. Use them to compare models, choose a tool, or train a team. The data, answer key, and script-based evaluator are included; to use them, just copy the text. The evaluator requires Python 3.

## 📖 User guide

Complete guide (landing page + step-by-step instructions, with a copy button for each prompt): **https://inematds.github.io/sete-provas-ia/guia/en/**

## The 7 tests

| # | Test | File delivered | The hard part |
|---|---|---|---|
| 1 | Sales page | `index.html` | a single path (free trial) and a scene that makes you stop scrolling |
| 2 | Sales dashboard | `painel.html` | data intentionally made dirty: clean it, show what you fixed, click the number |
| 3 | Sales presentation | `apresentacao.html` | a price that changed, a wrong calculation, and a number forbidden in the notes |
| 4 | Animated explainer | `explicativo.html` | 20 seconds without voice, 1920 x 1080, looping, for a 10-year-old |
| 5 | Photo editor | `editor.html` | 8 tools that really work |
| 6 | 3D driving game | `jogo.html` | fun in 10 seconds, victory and defeat |
| 7 | Agent hub | `central.html` | pause, stop, failure, and old runs, with the agent behind a function |

## The three forms

| Folder | For | What changes |
|---|---|---|
| `prompts/<idioma>/agente/` | Claude Code, Codex, Cursor, Antigravity, Gemini CLI, OpenCode | reads the folder's data, writes files and an `ENTREGA.md` |
| `prompts/<idioma>/chat/` | Agnes, ChatGPT, Gemini, Claude.ai, DeepSeek, Grok, Copilot | responds with a single HTML file; the data is pasted at the end of the request |
| `prompts/<idioma>/pessoa/` | a person or team, without AI | suggested time and how it will be evaluated |

Languages: `pt`, `en`, `es`. Images and video are optional in all forms: those with a generator (for example, Higgsfield, Agnes, Codex) can use it; those without one can draw in code.

**You need:** Python 3 (no extra libraries) and, ideally, Chrome or Chromium, which the checker uses to open the page hidden and read the numbers the JavaScript calculates; without it, those numbers become AVISO (warning). On Windows, use `py` instead of `python3`. No git: "Code › Download ZIP". The **seed** is a fixed number that makes the data come out the same every time, so the answer key never changes. File names and CSV columns stay in Portuguese on purpose, and the checker messages are in Portuguese.

## The process, start to finish

| # | Step | Command | Who does it |
|---|---|---|---|
| 1 | Generate the data and answer key (already included; only if you change the seed) | `python3 kit/gerar_dados.py` | ⚙️ script |
| 2 | Build the 21 prompts for each language from `kit/provas/<idioma>.json` and update the guide | `python3 kit/montar.py` | ⚙️ script |
| 3 | Choose a test, form, and competitors | — | 🧠 you |
| 4 | Prepare a folder for each competitor (prompt + data) | `python3 kit/preparar.py 2 corrida/claude/02 agente en` | ⚙️ script |
| 5 | Run it: paste `PROMPT.md` into the agent or chat, or give it to the person | — | 🤖 AI or 🧑 person |
| 6 | Check what can be measured without AI | `python3 kit/avaliar.py 2 corrida/claude/02` (`--chat` for a chat submission) | ⚙️ script |
| 7 | Open the submission, use it for 5 minutes, and fill out the 10-point scorecard | `avaliar/ficha.en.md` | 🧠 you |
| 8 | Compare the scorecards and record each competitor's time and cost | — | 🧠 you |

The kit's own checks: `python3 kit/gerar_dados.py --conferir` (data matches the seed) and `python3 kit/montar.py --conferir` (prompts and guides are up to date).

## Answer key (no AI)

- **Test 2:** `vendas.csv` has 1,470 rows and five planted problems. Cleaned: 1,430 orders, R$ 50,162.10. Chat version (`vendas-mini.csv`): 224 orders, R$ 7.831,00. Reference cleanup: `python3 kit/limpar.py dados/vendas.csv`.
- **Test 3:** correct price R$ 89/kg (not 95), correct total 157 people (not 140), competitor's R$ 130 is forbidden. Everything is in `dados/gabarito.json`.

## Real test

Tests 2 and 3 in chat form were run with Claude Sonnet (subscription, conversation without tools). Submissions and screenshots are in `exemplos/chat-sonnet/`. The format has not yet been measured with Agnes or the other chat tools.

## Structure

```
prompts/{pt,en,es}/{agente,chat,pessoa}/   21 prompts per language (generated)
kit/provas/{pt,en,es}.json                  single source for prompts
kit/gerar_dados.py  kit/limpar.py  kit/avaliar.py  kit/montar.py  kit/preparar.py
dados/  vendas.csv  vendas-mini.csv  notas.txt (+ en/ es/)  gabarito.json
avaliar/ficha.en.md  ficha.es.md  ficha.md   10-point scorecard (EN, ES, PT)
exemplos/chat-sonnet/                       real test in chat mode
guia/                                       landing page + guide in PT/EN/ES
```

MIT License. Part of the [INEMA.CLUB](https://inema.club) ecosystem.