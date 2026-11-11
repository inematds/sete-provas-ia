# 7 Provas para Qualquer IA

[![7 Provas para Qualquer IA](guia/assets/banner.jpg)](https://inematds.github.io/sete-provas-ia/guia/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## O que é

São sete pedidos de trabalho prontos para copiar: uma página de venda, um painel de vendas, uma apresentação, um explicativo animado, um editor de fotos, um jogo 3D e uma central de agentes. Cada pedido vem em três formas: para um agente que trabalha numa pasta (Claude Code, Codex, Cursor), para uma janela de chat (Agnes, ChatGPT, Gemini) e como briefing para uma pessoa, sem IA nenhuma. Serve para comparar modelos, escolher ferramenta ou treinar uma equipe. Os dados, o gabarito e o avaliador por script vêm junto; para usar basta copiar o texto, e para o avaliador, ter Python 3.

## 📖 Guia de uso

Guia completo (landing + passo a passo, com botão de copiar em cada prompt): **https://inematds.github.io/sete-provas-ia/guia/**

## As 7 provas

| # | Prova | Arquivo entregue | A parte difícil |
|---|---|---|---|
| 1 | Página de venda | `index.html` | um único caminho (teste grátis) e uma cena que faz parar de rolar |
| 2 | Painel de vendas | `painel.html` | dados sujos de propósito: limpar, mostrar o que consertou, clicar no número |
| 3 | Apresentação de vendas | `apresentacao.html` | preço que mudou, conta errada e número proibido nas anotações |
| 4 | Explicativo animado | `explicativo.html` | 20 s sem voz, 1920 x 1080, em loop, para uma criança de 10 anos |
| 5 | Editor de fotos | `editor.html` | 8 ferramentas funcionando de verdade |
| 6 | Jogo de direção 3D | `jogo.html` | divertido em 10 s, vitória e derrota |
| 7 | Central de agentes | `central.html` | pausar, parar, falha e execuções antigas, com o agente atrás de uma função |

## As três formas

| Pasta | Para | O que muda |
|---|---|---|
| `prompts/<idioma>/agente/` | Claude Code, Codex, Cursor, Antigravity, Gemini CLI, OpenCode | lê os dados da pasta, grava arquivos e um `ENTREGA.md` |
| `prompts/<idioma>/chat/` | Agnes, ChatGPT, Gemini, Claude.ai, DeepSeek, Grok, Copilot | responde com um único HTML; os dados vão colados no fim do pedido |
| `prompts/<idioma>/pessoa/` | uma pessoa ou equipe, sem IA | tempo sugerido e como será avaliado |

Idiomas: `pt`, `en`, `es`. Imagem e vídeo são opcionais em todas as formas: quem tem gerador (exemplo: Higgsfield, Agnes, Codex) usa; quem não tem desenha em código.

**Precisa de:** Python 3 (sem bibliotecas extras) e, de preferência, Chrome ou Chromium, que o avaliador usa para abrir a página escondido e ler os números calculados pelo JavaScript; sem ele, esses números viram AVISO. No Windows, troque `python3` por `py`. Sem git: botão "Code › Download ZIP". A **semente** é um número fixo que faz os dados saírem sempre iguais, por isso o gabarito nunca muda.

## O processo, do início ao fim

| # | Passo | Comando | Quem faz |
|---|---|---|---|
| 1 | Gerar os dados e o gabarito (já vêm prontos; só se mudar a semente) | `python3 kit/gerar_dados.py` | ⚙️ script |
| 2 | Montar os 21 prompts de cada idioma a partir de `kit/provas/<idioma>.json` e atualizar o guia | `python3 kit/montar.py` | ⚙️ script |
| 3 | Escolher prova, forma e concorrentes | — | 🧠 você |
| 4 | Preparar uma pasta por concorrente (prompt + dados) | `python3 kit/preparar.py 2 corrida/claude/02` | ⚙️ script |
| 5 | Rodar: colar o `PROMPT.md` no agente, no chat ou entregar à pessoa | — | 🤖 IA ou 🧑 pessoa |
| 6 | Conferir o que dá para medir sem IA | `python3 kit/avaliar.py 2 corrida/claude/02` (`--chat` para entrega de chat) | ⚙️ script |
| 7 | Abrir a entrega, usar 5 min e preencher a ficha de 10 pontos | `avaliar/ficha.md` | 🧠 você |
| 8 | Comparar as fichas e anotar tempo e custo de cada concorrente | — | 🧠 você |

Conferências do próprio kit: `python3 kit/gerar_dados.py --conferir` (dados batem com a semente) e `python3 kit/montar.py --conferir` (prompts e guias atualizados).

## Gabarito (sem IA)

- **Prova 2:** `vendas.csv` tem 1.470 linhas e cinco problemas plantados. Limpo: 1.430 pedidos, R$ 50.162,10. Versão de chat (`vendas-mini.csv`): 224 pedidos, R$ 7.831,00. Limpeza de referência: `python3 kit/limpar.py dados/vendas.csv`.
- **Prova 3:** preço certo R$ 89/kg (não 95), soma certa 157 pessoas (não 140), R$ 130 do concorrente proibido. Tudo em `dados/gabarito.json`.

## Teste real

As provas 2 e 3 na forma chat foram rodadas no Claude Sonnet (assinatura, conversa sem ferramentas). Entregas e capturas em `exemplos/chat-sonnet/`. No Agnes e nos outros chats o formato ainda não foi medido.

## Estrutura

```
prompts/{pt,en,es}/{agente,chat,pessoa}/   21 prompts por idioma (gerados)
kit/provas/{pt,en,es}.json                  fonte única dos prompts
kit/gerar_dados.py  kit/limpar.py  kit/avaliar.py  kit/montar.py  kit/preparar.py
dados/  vendas.csv  vendas-mini.csv  notas.txt (+ en/ es/)  gabarito.json
avaliar/ficha.md  ficha.en.md  ficha.es.md   ficha de 10 pontos (PT, EN, ES)
exemplos/chat-sonnet/                       teste real no modo chat
guia/                                       landing + guia PT/EN/ES
```

Licença MIT. Parte do ecossistema [INEMA.CLUB](https://inema.club).
