#!/usr/bin/env python3
"""Limpa o vendas.csv SEM IA e mostra os totais. É a resposta de referência da prova 2.

Uso: python3 kit/limpar.py dados/vendas.csv            -> resumo na tela
     python3 kit/limpar.py dados/vendas.csv --json     -> totais em JSON
     python3 kit/limpar.py dados/vendas.csv --saida limpo.csv

Regras de limpeza (as mesmas que a IA ou a pessoa precisa descobrir):
  1. loja com espaço, caixa diferente ou sem hífen  -> nome oficial
  2. preço com "R$" ou vírgula                       -> número com ponto
  3. data em dd/mm/aaaa ou "5 out 2026"              -> aaaa-mm-dd
  4. linha repetida igualzinha                       -> conta uma vez só
  5. produto "TESTE - NAO CONTAR"                     -> fora
"""
import csv, json, re, sys
from datetime import date

LOJAS = ["Centro", "Beira-Rio", "Rodoviária", "Alto da Serra"]
MESES = {m: i + 1 for i, m in enumerate(["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"])}


def chave(s):
    return re.sub(r"[\s\-]+", "", s).lower()


OFICIAL = {chave(l): l for l in LOJAS}


def data_iso(s):
    s = s.strip()
    if re.fullmatch(r"\d{4}-\d\d-\d\d", s):
        return s
    m = re.fullmatch(r"(\d\d)/(\d\d)/(\d{4})", s)
    if m:
        return date(int(m[3]), int(m[2]), int(m[1])).isoformat()
    m = re.fullmatch(r"(\d{1,2}) ([a-z]{3}) (\d{4})", s.lower())
    if m:
        return date(int(m[3]), MESES[m[2]], int(m[1])).isoformat()
    raise ValueError(f"data desconhecida: {s!r}")


def preco(s):
    return float(s.replace("R$", "").strip().replace(",", "."))


def limpar(caminho):
    vistos, limpas, log = set(), [], {"loja": 0, "preco": 0, "data": 0, "duplicada": 0, "teste": 0}
    with open(caminho, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            bruto = tuple(r.values())
            if bruto in vistos:
                log["duplicada"] += 1; continue
            vistos.add(bruto)
            if r["produto"].upper().startswith("TESTE"):
                log["teste"] += 1; continue
            loja = OFICIAL[chave(r["loja"])]
            if loja != r["loja"]:
                log["loja"] += 1
            if not re.fullmatch(r"\d+\.\d\d", r["preco"]):
                log["preco"] += 1
            d = data_iso(r["data"])
            if d != r["data"]:
                log["data"] += 1
            limpas.append({"pedido": int(r["pedido"]), "data": d, "loja": loja, "produto": r["produto"],
                           "qtd": int(r["qtd"]), "preco": preco(r["preco"]), "pagamento": r["pagamento"]})
    return limpas, log


def totais(rows):
    fat = sum(r["qtd"] * r["preco"] for r in rows)
    por = lambda k: {a: round(b, 2) for a, b in sorted(
        ((x, sum(r["qtd"] * r["preco"] for r in rows if r[k] == x)) for x in {r[k] for r in rows}),
        key=lambda kv: -kv[1])}
    return {"pedidos": len(rows), "faturamento": round(fat, 2), "ticket_medio": round(fat / len(rows), 2),
            "por_loja": por("loja"), "por_produto": por("produto")}


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    rows, log = limpar(sys.argv[1])
    t = totais(rows)
    if "--saida" in sys.argv:
        out = sys.argv[sys.argv.index("--saida") + 1]
        with open(out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
            w.writeheader(); w.writerows(rows)
    if "--json" in sys.argv:
        print(json.dumps({"consertos": log, **t}, ensure_ascii=False, indent=2)); return
    print("Consertos:", ", ".join(f"{k}={v}" for k, v in log.items()))
    print(f"Pedidos válidos: {t['pedidos']} | Faturamento: R$ {t['faturamento']:.2f} | Ticket médio: R$ {t['ticket_medio']:.2f}")
    for loja, v in t["por_loja"].items():
        print(f"  {loja:<14} R$ {v:>10.2f}")


if __name__ == "__main__":
    main()
