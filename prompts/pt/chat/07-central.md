# Prova 7: Central de agentes

Crie uma central de comando para um time pequeno de agentes de IA: um planejador, um pesquisador, um redator e um revisor.

Eu digito um objetivo e vejo o time planejar, fazer e revisar, ao vivo. Posso pausar ou parar uma execução. No fim recebo um relatório limpo e posso abrir execuções antigas. Se um agente falhar, vejo o motivo e a execução continua.

Nesta versão cada agente é um dublê: espera alguns segundos e devolve um texto de exemplo. Coloque esse dublê atrás de uma única função, para trocar por um modelo de verdade depois. Não use chave de API.

Arquivo principal: `central.html`, que abre com dois cliques. Tudo roda no navegador; as execuções antigas ficam guardadas no próprio navegador.

## Capricho
- Faça ficar bonito de verdade: quem passar o olho tem que parar de rolar a tela.
- Use as ferramentas e habilidades que você tiver (design, animação, gerador de imagem). Você escolhe.

## Imagens (opcional)
- Se esta interface gera imagem, gere no máximo 4 e diga o nome de arquivo de cada uma (img1.jpg, img2.jpg...), para eu salvar ao lado do HTML. No HTML, use <img src="img1.jpg"> e mostre um desenho em SVG ou CSS no lugar se o arquivo não existir, para a página nunca abrir com imagem quebrada.
- Se não gera, desenhe tudo em SVG ou CSS dentro do HTML. A prova vale igual.
- Modo raio-X: a tecla X e um botão pequeno ligam contornos, numa cor para cada imagem e noutra cor para cada animação feita em código, com uma etiqueta pequena em cada um.

## Como entregar (você está numa janela de chat, sem pasta)
- Responda com UM arquivo HTML completo num único bloco de código, do <!doctype html> ao </html>, com o CSS e o JavaScript dentro.
- O arquivo tem que vir inteiro. Nada de "o resto continua igual".
- Não use arquivos da internet. Nunca toque som.
- Não faça perguntas. Termine de uma vez.
- Depois do bloco, em até 5 linhas: o que fez e como abrir.
