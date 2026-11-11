#!/usr/bin/env python3
"""Prepara a pasta de uma prova para um concorrente (IA ou pessoa). Funciona no Linux, Mac e Windows.

Uso:  python3 kit/preparar.py <prova 1-7> <pasta> [agente|pessoa] [pt|en|es]
      (no Windows: py kit\\preparar.py ...  ou  python kit\\preparar.py ...)

  prova   número de 1 a 7
  pasta   pasta nova (ou vazia) para este concorrente, ex.: corrida/claude/02
  forma   agente (padrão) = Claude Code, Codex, Cursor...  ·  pessoa = briefing sem IA
          (as palavras são essas, em português, em qualquer idioma)
  idioma  pt (padrão), en ou es

Exemplos:
  python3 kit/preparar.py 2 corrida/claude/02
  python3 kit/preparar.py 2 corrida/claude/02 agente en
  python3 kit/preparar.py 3 corrida/maria/03 pessoa es

Copia o prompt (PROMPT.md) e os dados que a prova pede. A forma chat não usa pasta:
copie o prompt de prompts/<idioma>/chat/ ou do guia (os dados já vão dentro dele).
"""
import shutil, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def sair(msg, cod=2):
    print(msg, file=sys.stderr); sys.exit(cod)


def main():
    a = sys.argv[1:]
    if len(a) < 2 or not a[0].isdigit() or not 1 <= int(a[0]) <= 7:
        sair(__doc__)
    n, pasta = int(a[0]), Path(a[1])
    forma = a[2] if len(a) > 2 else "agente"
    lang = a[3] if len(a) > 3 else "pt"
    if forma == "chat":
        sair(f"a forma chat não usa pasta: copie o texto de prompts/{lang}/chat/ (ou do guia) e cole numa conversa nova; os dados já vão dentro dele")
    if forma not in ("agente", "pessoa"):
        sair(f"forma desconhecida: {forma} (use agente ou pessoa, em português, em qualquer idioma)")
    if lang not in ("pt", "en", "es"):
        sair(f"idioma desconhecido: {lang} (use pt, en ou es)")
    achados = sorted((RAIZ / "prompts" / lang / forma).glob(f"0{n}-*.md"))
    if not achados:
        sair(f"não achei prompts/{lang}/{forma}/0{n}-*.md", 1)
    if pasta.exists() and any(pasta.iterdir()):
        sair(f"a pasta {pasta} já existe e não está vazia; escolha outra", 1)
    pasta.mkdir(parents=True, exist_ok=True)
    shutil.copy(achados[0], pasta / "PROMPT.md")
    if n == 2:
        shutil.copy(RAIZ / "dados" / "vendas.csv", pasta)
    elif n == 3:
        shutil.copy(RAIZ / "dados" / ("notas.txt" if lang == "pt" else f"{lang}/notas.txt"), pasta / "notas.txt")
    print(f"pronto: {pasta}")
    for f in sorted(pasta.iterdir()):
        print(f"  {f.name}")
    print()
    if forma == "pessoa":
        print(f"Agora entregue a pasta {pasta} para a pessoa: o briefing está em PROMPT.md.")
    else:
        print(f"Agora abra o agente DENTRO de {pasta} e cole o conteúdo de PROMPT.md.")
    print(f"No fim, a partir de qualquer pasta: python3 {RAIZ / 'kit' / 'avaliar.py'} {n} {pasta.resolve()}")


if __name__ == "__main__":
    main()
