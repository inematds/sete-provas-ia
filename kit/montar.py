#!/usr/bin/env python3
"""Monta os 21 prompts (7 provas x 3 formas) de cada idioma a partir de kit/provas/<idioma>.json.

Formas:
  agente  -> Claude Code, Codex, Cursor, Antigravity... (trabalha numa pasta, grava arquivos)
  chat    -> Agnes, ChatGPT, Gemini, Claude.ai... (sem pasta: devolve um HTML só; dados vão colados no pedido)
  pessoa  -> sem IA: briefing para uma pessoa ou equipe, com tempo sugerido e ficha de avaliação

Uso: python3 kit/montar.py            grava prompts/<idioma>/<forma>/NN-slug.md e atualiza os guias
     python3 kit/montar.py --conferir  só confere se o que está no disco está atualizado
"""
import html, json, re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
IDIOMAS = ["pt", "en", "es"]
FORMAS = ["agente", "chat", "pessoa"]


def dados_de(idioma, nome):
    p = RAIZ / "dados" / (nome if idioma == "pt" or nome.endswith(".csv") else f"{idioma}/{nome}")
    return p.read_text(encoding="utf-8")


def montar(idioma):
    cfg = json.loads((RAIZ / f"kit/provas/{idioma}.json").read_text(encoding="utf-8"))
    R, B = cfg["rotulos"], cfg["blocos"]
    saida = {}
    for p in cfg["provas"]:
        lib = B["liberado_cdn"] if p.get("cdn") else ""
        for forma in FORMAS:
            arq_dados = p.get("dados_chat") if forma == "chat" else p.get("dados")
            pedido = p["pedido"].replace("{DADOS}", arq_dados or "")
            if forma == "chat" and arq_dados:
                pedido = re.sub(r"`[^`]+`", f"`{arq_dados}`", pedido, count=1)
            abrir = p.get("abrir_chat", p["abrir"]) if forma == "chat" else p["abrir"]
            partes = [f"# {R['prova']} {p['n']}: {p['titulo']}"]
            if forma == "pessoa":
                linha = f"**{R['tempo']}:** {p['tempo']}"
                if p.get("perfil"):
                    linha += f" · **{R['perfil']}:** {p['perfil']}"
                partes.append(linha)
            partes += [pedido, abrir, B["capricho_pessoa"] if forma == "pessoa" else B["capricho"]]
            if forma == "chat":
                partes += [B["imagens_chat"], B["regras_chat"].replace("{LIBERADO}", lib)]
                if arq_dados:
                    partes.append(f"{R['dados_abaixo']}\n\n=== {arq_dados} ===\n{dados_de(idioma, arq_dados).rstrip()}\n=== {R['fim']} ===")
            elif forma == "agente":
                partes += [B["imagens_agente"], B["regras_agente"].replace("{LIBERADO}", lib)]
            else:
                regras = B["regras_pessoa"]
                if arq_dados:  # só as provas com arquivo de dados dizem onde achar o arquivo
                    regras = regras.replace("\n\n## ", "\n" + R["dados_pessoa"] + "\n\n## ", 1)
                partes += [B["imagens_pessoa"], regras]
            saida[f"prompts/{idioma}/{forma}/{p['n']:02d}-{p['slug']}.md"] = "\n\n".join(partes) + "\n"
    return cfg, saida


def bloco_guia(cfg, saida, idioma):
    """HTML estático das 7 provas para o guia (entre <!--PROVAS--> e <!--/PROVAS-->)."""
    R = cfg["rotulos"]
    nomes = {"agente": R["modo_agente"], "chat": R["modo_chat"], "pessoa": R["modo_pessoa"]}
    out = []
    for p in cfg["provas"]:
        abas, paineis = [], []
        for i, forma in enumerate(FORMAS):
            txt = saida[f"prompts/{idioma}/{forma}/{p['n']:02d}-{p['slug']}.md"]
            pid = f"p{p['n']}-{forma}"
            abas.append(f'<button class="aba{" on" if i == 0 else ""}" data-alvo="{pid}">{html.escape(nomes[forma].split(" (")[0])}</button>')
            paineis.append(f'<div class="painel{" on" if i == 0 else ""}" id="{pid}"><p class="quem">{html.escape(nomes[forma])}</p>'
                           f'<button class="copiar" data-de="{pid}-txt">{html.escape(R["copiar"])}</button>'
                           f'<pre class="prompt" id="{pid}-txt">{html.escape(txt)}</pre></div>')
        out.append(
            f'<article class="prova" id="prova-{p["n"]}"><div class="prova-top"><span class="num">{p["n"]}</span>'
            f'<div><h3>{html.escape(p["titulo"])}</h3><p>{html.escape(p["resumo"])}</p>'
            f'<p class="meta"><b>{html.escape(R["arquivo_principal"])}:</b> <code>{p["arquivo"]}</code> · <b>{html.escape(R["tempo_guia"])}:</b> {p["tempo"]}</p></div></div>'
            f'<div class="dificil"><b>{html.escape(R["parte_dificil"])}:</b> {html.escape(p["dificil"])}</div>'
            f'<div class="abas">{"".join(abas)}</div>{"".join(paineis)}</article>')
    return "\n".join(out)


def main():
    conferir = "--conferir" in sys.argv
    ruins = []
    for idioma in IDIOMAS:
        if not (RAIZ / f"kit/provas/{idioma}.json").exists():
            print(f"(sem kit/provas/{idioma}.json, pulei)"); continue
        cfg, saida = montar(idioma)
        guia = RAIZ / ("guia/index.html" if idioma == "pt" else f"guia/{idioma}/index.html")
        if guia.exists():
            g = guia.read_text(encoding="utf-8")
            novo = re.sub(r"(<!--PROVAS-->).*?(<!--/PROVAS-->)", lambda m: m[1] + "\n" + bloco_guia(cfg, saida, idioma) + "\n" + m[2], g, flags=re.S)
            saida[str(guia.relative_to(RAIZ))] = novo
        for rel, txt in saida.items():
            f = RAIZ / rel
            if conferir:
                if not f.exists() or f.read_text(encoding="utf-8") != txt:
                    ruins.append(rel)
            else:
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_text(txt, encoding="utf-8")
        print(f"{idioma}: {len(saida)} arquivos {'conferidos' if conferir else 'gravados'}")
    if conferir:
        print("ok: tudo atualizado" if not ruins else f"DESATUALIZADO: {ruins}")
        sys.exit(1 if ruins else 0)


if __name__ == "__main__":
    main()
