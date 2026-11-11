#!/usr/bin/env python3
"""Confere uma entrega SEM IA: o que dá para medir por script. O resto vai na ficha (avaliar/ficha.md).

Uso: python3 kit/avaliar.py <prova 1-7> <pasta-ou-arquivo-da-entrega> [--chat]
     --sem-navegador  não abre a página (por padrão, se houver Chrome ou Chromium, abre a página escondida
                      para ler os números que o JavaScript calcula)
     --chat  a entrega veio de janela de chat (não exige ENTREGA.md; prova 2 usa o gabarito do vendas-mini.csv)

Exemplos:
  python3 kit/avaliar.py 3 corrida/claude/03
  python3 kit/avaliar.py 2 corrida/agnes/painel.html --chat

Saída: uma linha por conferência (OK / AVISO / FALHA) e o placar das que são automáticas.
Funciona com entregas em português, inglês ou espanhol.
"""
import json, re, shutil, subprocess, sys
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ARQ = {1: "index.html", 2: "painel.html", 3: "apresentacao.html", 4: "explicativo.html",
       5: "editor.html", 6: "jogo.html", 7: "central.html"}


class Texto(HTMLParser):
    """Texto visível (sem <script>/<style>) e scripts separados."""
    def __init__(self):
        super().__init__(); self.vis, self.js, self._em = [], [], None
    def handle_starttag(self, tag, a):
        if tag in ("script", "style"): self._em = tag
    def handle_endtag(self, tag):
        if tag == self._em: self._em = None
    def handle_data(self, d):
        (self.js if self._em == "script" else self.vis if self._em is None else []).append(d)


def achar_html(alvo, n):
    p = Path(alvo)
    if p.is_file():
        return p
    for nome in (ARQ[n], "index.html"):
        if (p / nome).exists():
            return p / nome
    htmls = sorted(p.glob("*.html"))
    return htmls[0] if htmls else None


def renderizado(f):
    """Texto da página DEPOIS do JavaScript rodar (Chrome/Chromium sem janela). '' se não houver navegador.
    Muitos números (total, contagens) só existem depois que o script calcula.
    O Chromium do Ubuntu (snap) não lê /tmp: se falhar, copia a pasta para ~/.cache e tenta de novo."""
    exes = [e for e in (shutil.which(n) for n in ("chromium", "chromium-browser", "google-chrome",
                                                 "google-chrome-stable", "chrome", "msedge")) if e]
    # Windows e Mac: o navegador não fica no PATH; procurar nos lugares de instalação padrão
    import os
    for base in filter(None, (os.environ.get("ProgramFiles"), os.environ.get("ProgramFiles(x86)"), os.environ.get("LocalAppData"))):
        for rel in (r"Google\Chrome\Application\chrome.exe", r"Microsoft\Edge\Application\msedge.exe", r"Chromium\Application\chrome.exe"):
            if Path(base, rel).exists():
                exes.append(str(Path(base, rel)))
    for mac in ("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
                "/Applications/Chromium.app/Contents/MacOS/Chromium"):
        if Path(mac).exists():
            exes.append(mac)
    if not exes:
        return "", "sem-navegador"
    def tenta(alvo):
        for exe in exes:
            try:
                r = subprocess.run([exe, "--headless", "--no-sandbox", "--disable-gpu", "--mute-audio",
                                    "--virtual-time-budget=6000", "--dump-dom", alvo.resolve().as_uri()],
                                   capture_output=True, text=True, timeout=90)
                if "<body" in r.stdout.lower():
                    return r.stdout
            except Exception:
                pass
        return ""
    dom = tenta(f)
    if not dom:
        import tempfile
        base = RAIZ / "corrida" / "_avaliar"  # pasta visível: o snap não lê /tmp nem pastas com ponto
        base.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=base) as tmp:
            copia = Path(tmp) / "entrega"
            shutil.copytree(f.parent, copia, ignore=shutil.ignore_patterns("*.csv", "node_modules"))
            dom = tenta(copia / f.name)
    return (dom, "ok") if dom else ("", "navegador-falhou")


def tem(texto, *palavras):
    t = texto.lower()
    return any(w.lower() in t for w in palavras)


def numeros(texto):
    """Números como aparecem na tela: 3.204 / 3,204 / 0,5 / 89 / 157."""
    achados = set()
    for m in re.finditer(r"(?<![\w.,])(\d{1,3}(?:[.,]\d{3})+|\d+)(?:[.,](\d+))?(?![\w])", texto):
        inteiro = re.sub(r"[.,]", "", m[1]) if re.fullmatch(r"\d{1,3}(?:[.,]\d{3})+", m[1]) else m[1]
        v = float(f"{inteiro}.{m[2]}") if m[2] else float(inteiro)
        achados.add(v)
    return achados


def formatos_dinheiro(v):
    """7831.0 -> 7.831,00 / 7,831.00 / 7831.00 / 7831,00 (e sem centavos quando é redondo)."""
    i, c = f"{v:.2f}".split(".")
    en = f"{int(i):,}"            # 7,831
    br = en.replace(",", ".")     # 7.831
    fs = {f"{br},{c}", f"{en}.{c}", f"{i}.{c}", f"{i},{c}"}
    if c == "00":
        fs |= {br, en} if int(i) >= 1000 else set()
    return fs


def main():
    if len(sys.argv) < 3 or not sys.argv[1].isdigit() or int(sys.argv[1]) not in ARQ:
        print(__doc__); sys.exit(2)
    n, alvo, chat = int(sys.argv[1]), sys.argv[2], "--chat" in sys.argv
    gab = json.loads((RAIZ / "dados/gabarito.json").read_text(encoding="utf-8"))
    res = []
    ok = lambda c, msg: res.append(("OK" if c else "FALHA", msg))
    aviso = lambda c, msg: res.append(("OK" if c else "AVISO", msg))

    f = achar_html(alvo, n)
    if not f:
        print(f"FALHA  nenhum .html em {alvo}"); sys.exit(1)
    bruto = f.read_text(encoding="utf-8", errors="replace")
    t = Texto(); t.feed(bruto)
    vis, js = " ".join(t.vis), " ".join(t.js)
    if "--sem-navegador" in sys.argv:
        dom, modo = "", "pedido"
    else:
        dom, modo = renderizado(f)
    if dom:
        t2 = Texto(); t2.feed(dom)
        vis_r = " ".join(t2.vis)
    else:
        vis_r = ""

    ok(f.name == ARQ[n], f"arquivo principal se chama {ARQ[n]} (achei {f.name})")
    ok(re.search(r"<!doctype html", bruto, re.I) and re.search(r"</html>", bruto, re.I), "HTML completo (doctype até </html>)")
    externos = set(re.findall(r"""(?:src|href)\s*=\s*["'](https?://[^"']+)""", bruto, re.I))
    externos |= set(re.findall(r"""import\s[^;]*?from\s*["'](https?://[^"']+)""", bruto))
    liberados = [u for u in externos if n == 6 and re.search(r"three", u, re.I)]
    fora = sorted(externos - set(liberados))
    aviso(not fora, "nada puxado da internet" + (f" (achei: {', '.join(fora[:3])})" if fora else ""))
    if not chat:
        pasta = f.parent
        aviso((pasta / "ENTREGA.md").exists() or (pasta / "DONE.md").exists(), "ENTREGA.md na pasta")
    aviso(re.search(r"""(['"]x['"]|['"]X['"]|KeyX)""", js) is not None, "modo raio-X (tecla X) no código")
    aviso(not re.search(r"\.play\(\)", js) or re.search(r"muted", bruto), "nenhum som tocando sozinho")

    if n == 1:
        links = re.findall(r"""<a\s[^>]*href\s*=\s*["']([^"'#][^"']*)["']""", bruto, re.I)
        aviso(len(links) == 0, f"nenhum link que tira a pessoa da página ({len(links)} achados)")
        ok(tem(vis, "grátis", "gratis", "free", "gratuit"), "fala do teste grátis")
    elif n == 2:
        g = gab["vendas-mini.csv" if chat else "vendas.csv"]
        achou = any(fm in bruto or fm in vis_r for fm in formatos_dinheiro(g["faturamento"]))
        msg = f"faturamento total certo depois de limpar (R$ {g['faturamento']:.2f})"
        if achou or dom:
            ok(achou, msg)
        else:  # sem navegador o total calculado pelo JavaScript não aparece no código: não dá para afirmar FALHA
            aviso(False, msg + " — não achei no código; confira na tela")
        p = gab["problemas_plantados"] if not chat else None
        if p:
            conta = sum(1 for v in p.values() if re.search(rf"(?<!\d){v}(?!\d)", vis + js + vis_r))
            aviso(conta >= 3, f"mostra quantas linhas de cada problema ({conta} de {len(p)} contagens achadas)")
        aviso(tem(vis + js, "teste", "test", "duplic"), "fala das linhas de teste ou duplicadas")
        ok(re.search(r"addEventListener\(\s*['\"]click|onclick", bruto) is not None, "dá para clicar (ver as linhas por trás do número)")
    elif n == 3:
        G = gab["notas.txt"]
        nums = numeros(vis + " " + js + " " + vis_r)
        proib = [x for x in G["numeros_proibidos"] if x in nums]
        ok(not proib, "não usa número proibido (95 velho, 130 do concorrente, 140 da conta errada)" + (f": achei {proib}" if proib else ""))
        (ok if (89 in nums or dom) else aviso)(89 in nums, "usa o preço atualizado (R$ 89 o kg)")
        aviso(157 in nums, "corrigiu a soma (120 + 15 + 22 = 157)")
        ok(re.search(r"Arrow(Right|Left)", js) is not None, "setas do teclado passam os slides")
    elif n == 4:
        ok("1920" in bruto and "1080" in bruto, "tela de 1920 x 1080")
        aviso(re.search(r"infinite|loop|setInterval|% ?\d+", bruto) is not None, "repete sozinho (loop)")
        aviso(not re.search(r"speechSynthesis|<audio", bruto), "sem voz")
    elif n == 5:
        itens = {"abrir foto": ("type=\"file\"", "type='file'", "showOpenFilePicker", "drop"),
                 "camadas": ("camada", "layer", "capa"), "pincel": ("pincel", "brush", "pincel"),
                 "recorte": ("recort", "crop", "recortar"), "filtros": ("filtro", "filter"),
                 "texto": ("fillText",), "desfazer": ("desfaz", "undo", "deshacer"),
                 "exportar PNG": ("image/png", "toBlob", "toDataURL")}
        for nome, chaves in itens.items():
            ok(tem(bruto, *chaves), f"ferramenta: {nome}")
    elif n == 6:
        ok(tem(bruto, "three"), "usa Three.js (3D)")
        ok(tem(vis + js, "vitória", "vitoria", "venceu", "win", "victoria", "ganaste"), "tela de vitória")
        ok(tem(vis + js, "derrota", "perdeu", "game over", "lose", "perdiste", "fim de jogo"), "tela de derrota")
    elif n == 7:
        for nome, chaves in {"pausar": ("pausa", "pause", "pausar"), "parar": ("parar", "stop", "detener"),
                             "relatório": ("relatório", "relatorio", "report", "informe"),
                             "execuções antigas guardadas": ("localStorage", "indexedDB", "historico", "histórico", "history")}.items():
            ok(tem(bruto, *chaves), nome)
        papeis = sum(1 for grupo in (("planej", "planner", "planific"), ("pesquis", "research", "investig"),
                                     ("redat", "writer", "redact"), ("revis", "checker", "review"))
                     if tem(bruto, *grupo))
        ok(papeis == 4, f"os 4 agentes aparecem ({papeis} de 4)")
        aviso(not re.search(r"sk-[A-Za-z0-9]{10}|api[_-]?key\s*[:=]\s*['\"][^'\"]{8}", bruto, re.I), "nenhuma chave de API no arquivo")

    nota_modo = {"ok": "página aberta no navegador (números calculados conferidos)",
                 "pedido": "só o código (--sem-navegador); números calculados pela página viram AVISO",
                 "sem-navegador": "só o código: não achei Chrome/Chromium; números calculados pela página viram AVISO",
                 "navegador-falhou": "só o código: o navegador não abriu a página; números calculados viram AVISO"}[modo]
    print(f"Modo: {nota_modo}\n")
    for estado, msg in res:
        print(f"{estado:<6} {msg}")
    falhas = sum(1 for e, _ in res if e == "FALHA")
    certos = sum(1 for e, _ in res if e == "OK")
    print(f"\nPlacar automático: {certos}/{len(res)}  ({falhas} falha(s)). Compare placares só do mesmo modo.")
    print("Agora abra o arquivo, use por 5 minutos e preencha avaliar/ficha.md.")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
