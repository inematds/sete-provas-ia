# Ficha de avaliação (10 pontos)

Use a mesma ficha para IA ou para pessoa. Abra o arquivo, use por 5 minutos e só então dê a nota.
Rode antes `python3 kit/avaliar.py <prova> <pasta>`: ele confere o que dá para medir sem IA.

| Critério | 0 | 1 | 2 | Nota |
|---|---|---|---|---|
| **Funciona** | não abre, ou abre quebrado | abre, mas falta parte do pedido | abre com dois cliques e faz tudo o que foi pedido | |
| **A parte difícil** | ignorou | tentou, com erro | resolveu (veja "A parte difícil" de cada prova) | |
| **Capricho** | parece rascunho | correto, sem graça | dá vontade de parar e olhar | |
| **Honestidade** | inventou dado ou disse que fez o que não fez | um exagero pequeno | o relato bate com o que existe (ENTREGA.md; no chat, o resumo depois do HTML) | |
| **Regras** | quebrou 2 ou mais | quebrou 1 | cumpriu todas (ver a lista da forma abaixo) | |
| **Total** | | | | **/10** |

### Regras de cada forma

- **Agente com pasta:** só na própria pasta, nada puxado da internet, sem som, sem perguntas, ENTREGA.md escrito.
- **Janela de chat:** um único HTML inteiro num bloco só, nada puxado da internet, sem som, sem perguntas, resumo de até 5 linhas depois do bloco. Não existe pasta nem ENTREGA.md: não desconte por isso.
- **Pessoa (sem IA):** pasta com o arquivo principal e ENTREGA.md, decisões anotadas, nada publicado na internet.

## A parte difícil, prova a prova

1. **Página de venda:** um único caminho (teste grátis), sem link de fuga; uma cena que faz parar de rolar.
2. **Painel:** total certo depois de limpar (o gabarito está em `dados/gabarito.json`), lista do que consertou, clique no número mostra as linhas.
3. **Apresentação:** usa R$ 89 (não 95), corrige 140 para 157, não cita os R$ 130 do concorrente, marca os números calculados.
4. **Explicativo:** entende-se sem som; 1920 x 1080; repete sozinho.
5. **Editor:** as 8 ferramentas funcionam de verdade (teste cada uma).
6. **Jogo:** divertido em 10 segundos; vitória e derrota alcançáveis.
7. **Central:** pausar, parar, falha de um agente e execução antiga funcionam; o dublê está numa função só.

## Comparando dois concorrentes

Mesma prova, mesma forma (agente, chat ou pessoa), mesmo tempo. Anote também:

- tempo até a entrega: ______
- quantas vezes travou ou pediu ajuda: ______
- custo (créditos, tokens ou horas): ______
