# CLAUDE.md — sete-provas-ia

Kit público: 7 prompts de teste em 3 formas (agente, chat, pessoa) e 3 idiomas, com dados, gabarito e avaliador sem IA.

- Fonte única dos prompts: `kit/provas/<idioma>.json`. Nunca editar `prompts/` à mão: mudar o JSON e rodar `python3 kit/montar.py` (também reescreve o bloco `<!--PROVAS-->` dos 3 guias).
- Dados com semente fixa: `python3 kit/gerar_dados.py`. Mudou o gerador, conferir `python3 kit/limpar.py dados/vendas.csv` contra `dados/gabarito.json`.
- Antes do push: `python3 kit/gerar_dados.py --conferir && python3 kit/montar.py --conferir`.
- Kit sem fonte: nenhum link, autor ou aula de terceiro em README, guia, prompts ou posts. Ferramenta citada vira "exemplo: X".
- Conta GitHub: inematds (autor `inematds <inematds@gmail.com>`).

## Self-learning

Quando eu for corrigido, ou perceber um erro meu: antes de seguir, acrescentar a lição como regra de uma linha no TOPO da seção Lessons abaixo.

## Lessons
