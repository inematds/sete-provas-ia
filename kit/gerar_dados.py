#!/usr/bin/env python3
"""Gera os dados das provas 2 e 3, sempre iguais (semente fixa).

Saída em dados/:
  vendas.csv        90 dias de pedidos de uma rede de 4 cafeterias, SUJO de propósito
  vendas-mini.csv   14 dias do mesmo arquivo (para colar numa janela de chat)
  notas.txt         anotações bagunçadas de uma reunião de vendas (prova 3)
  gabarito.json     a verdade: o que está sujo e os totais depois de limpar

Uso: python3 kit/gerar_dados.py            (grava em ./dados)
     python3 kit/gerar_dados.py --conferir (regera em memória e compara com o que está no disco)
"""
import csv, io, json, random, sys
from datetime import date, timedelta
from pathlib import Path

SEMENTE = 2611
INICIO = date(2026, 8, 3)
DIAS = 90
LOJAS = {"Centro": 1.25, "Beira-Rio": 1.0, "Rodoviária": 0.9, "Alto da Serra": 0.75}
PRODUTOS = {  # preço em R$
    "Espresso": 6.50, "Cappuccino": 11.00, "Latte": 12.00, "Coado": 8.00,
    "Pão de queijo": 7.00, "Bolo de fubá": 9.50, "Café em grão 250g": 39.90, "Gelado": 13.50,
}
PAGAMENTOS = ["pix", "cartao", "dinheiro"]
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]


def variantes_loja(nome, rnd):
    opcoes = [nome.upper(), " " + nome, nome.lower() + " ", nome.replace("-", " ")]
    return rnd.choice([o for o in opcoes if o != nome])


def gerar():
    rnd = random.Random(SEMENTE)
    limpas = []
    pid = 50001
    for d in range(DIAS):
        dia = INICIO + timedelta(days=d)
        fim_de_semana = dia.weekday() >= 5
        for loja, peso in LOJAS.items():
            n = int(rnd.gauss(4.2 * peso * (1.3 if fim_de_semana else 1.0), 1.0))
            for _ in range(max(1, n)):
                prod = rnd.choice(list(PRODUTOS))
                limpas.append({"pedido": pid, "data": dia, "loja": loja, "produto": prod,
                               "qtd": rnd.randint(1, 4), "preco": PRODUTOS[prod],
                               "pagamento": rnd.choices(PAGAMENTOS, [5, 4, 1])[0]})
                pid += 1

    # sujeira, sempre recuperável
    linhas, problemas = [], {"loja_escrita_diferente": 0, "preco_com_RS_ou_virgula": 0,
                             "data_fora_do_padrao": 0, "linha_duplicada": 0, "linha_de_teste": 0}
    for r in limpas:
        loja, preco, data = r["loja"], f'{r["preco"]:.2f}', r["data"].isoformat()
        x = rnd.random()
        if x < 0.05:
            loja = variantes_loja(loja, rnd); problemas["loja_escrita_diferente"] += 1
        x = rnd.random()
        if x < 0.06:
            preco = rnd.choice([f'R$ {r["preco"]:.2f}', f'{r["preco"]:.2f}'.replace(".", ",")])
            problemas["preco_com_RS_ou_virgula"] += 1
        x = rnd.random()
        if x < 0.08:
            dt = r["data"]
            data = rnd.choice([dt.strftime("%d/%m/%Y"), f"{dt.day} {MESES[dt.month-1]} {dt.year}"])
            problemas["data_fora_do_padrao"] += 1
        linha = [r["pedido"], data, loja, r["produto"], r["qtd"], preco, r["pagamento"]]
        linhas.append(linha)
        if rnd.random() < 0.02:
            linhas.append(list(linha)); problemas["linha_duplicada"] += 1
    for i in range(6):
        dt = INICIO + timedelta(days=rnd.randrange(DIAS))
        linhas.append([90000 + i, dt.isoformat(), "Centro", "TESTE - NAO CONTAR", 99, "1.00", "pix"])
        problemas["linha_de_teste"] += 1
    rnd.shuffle(linhas)

    def totais(rows):
        fat, por_loja, por_prod, pedidos = 0.0, {}, {}, 0
        for r in rows:
            v = r["qtd"] * r["preco"]
            fat += v; pedidos += 1
            por_loja[r["loja"]] = por_loja.get(r["loja"], 0) + v
            por_prod[r["produto"]] = por_prod.get(r["produto"], 0) + v
        arr = lambda d: {k: round(v, 2) for k, v in sorted(d.items(), key=lambda kv: -kv[1])}
        return {"pedidos": pedidos, "faturamento": round(fat, 2), "ticket_medio": round(fat / pedidos, 2),
                "por_loja": arr(por_loja), "por_produto": arr(por_prod)}

    fim_mini = INICIO + timedelta(days=13)
    mini_ids = {r["pedido"] for r in limpas if r["data"] <= fim_mini}
    gabarito = {
        "periodo": [INICIO.isoformat(), (INICIO + timedelta(days=DIAS - 1)).isoformat()],
        "linhas_no_arquivo": len(linhas),
        "problemas_plantados": problemas,
        "vendas.csv": totais(limpas),
        "vendas-mini.csv": {"periodo": [INICIO.isoformat(), fim_mini.isoformat()],
                            **totais([r for r in limpas if r["data"] <= fim_mini])},
        "notas.txt": NOTAS_GABARITO,
    }
    mini = [l for l in linhas if l[0] in mini_ids]
    # a versão mini leva 2 linhas de teste também, para a armadilha existir no chat
    mini += [l for l in linhas if l[0] >= 90000][:2]
    gabarito["vendas-mini.csv"]["linhas_no_arquivo"] = len(mini)
    return linhas, mini, gabarito


NOTAS = """anotações - Grão do Morro - ideia de assinatura p/ escritórios (digitado durante a call, bagunçado)

quem: Marta (dona), Kenji (operação). eu anotando.

- querem vender café em grão p/ ESCRITÓRIOS, não só no balcão. 1º alvo = Vieira & Sato Advogados (2 andares, perto da loja Rodoviária)
- gerente do escritório é a Lúcia. ela disse que o pessoal "odeia a máquina de cápsula"
- Vieira & Sato tem 120 pessoas. Lúcia acha que 60% toma café todo dia
- preço que a Marta pensou: R$ 95 o kg entregue...
  >> ATUALIZAÇÃO depois da call: Marta mandou msg, usar R$ 89 o kg e não 95. esquece o 95
- entrega a cada 2 semanas. moedor emprestado de graça se fechar 6 meses
- quem toma café gasta uns 0,5 kg por mês (número do Kenji, das lojas)
- a Grão do Morro torra 2x por semana, então o café chega com no máx. 4 dias de torra
- concorrente: ACHO que a CaféJá cobra uns R$ 130 o kg?? não tenho certeza nenhuma - NÃO citar isso
- já tem 3 escritórios na fila: Vieira & Sato, um estúdio de design (15 pessoas), um escritório de arquitetura (22 pessoas)
- Marta: "3 escritórios, uns 40 cada, então 140 pessoas" (conta dela, conferir)
- oferta de teste: 2 primeiras semanas grátis, cancela quando quiser
- o que a Lúcia quer: sem sujeira, sem armadilha de contrato, que a equipe goste
- próximo passo que a Marta quer: degustação de 20 min na Vieira & Sato numa quinta de manhã
- marca: acolhedora, simples, um pouco engraçada. cores: creme + verde-escuro + laranja queimado
"""

NOTAS_GABARITO = {
    "preco_certo_kg": 89, "preco_abandonado_kg": 95,
    "numero_proibido": 130, "motivo_proibido": "palpite sobre concorrente marcado como NÃO citar",
    "soma_errada": {"dita": 140, "certa": 120 + 15 + 22, "conta": "120 + 15 + 22 = 157"},
    "contas_derivadas": {
        "bebem_cafe_vieira_sato": "120 x 60% = 72 pessoas",
        "kg_por_mes_vieira_sato": "72 x 0,5 kg = 36 kg/mês",
        "receita_mes_vieira_sato": "36 kg x R$ 89 = R$ 3.204 por mês",
    },
    "numeros_permitidos": [120, 60, 89, 2, 6, 0.5, 4, 3, 15, 22, 157, 20, 72, 36, 3204],
    "numeros_proibidos": [95, 130, 140],
}


def para_csv(linhas):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["pedido", "data", "loja", "produto", "qtd", "preco", "pagamento"])
    w.writerows(linhas)
    return buf.getvalue()


def main():
    raiz = Path(__file__).resolve().parent.parent / "dados"
    linhas, mini, gab = gerar()
    saidas = {"vendas.csv": para_csv(linhas), "vendas-mini.csv": para_csv(mini), "notas.txt": NOTAS,
              "gabarito.json": json.dumps(gab, ensure_ascii=False, indent=2) + "\n"}
    if "--conferir" in sys.argv:
        ruins = [n for n, t in saidas.items() if not (raiz / n).exists() or (raiz / n).read_text() != t]
        print("ok: dados batem com a semente" if not ruins else f"DIFERENTE: {ruins}")
        sys.exit(1 if ruins else 0)
    raiz.mkdir(exist_ok=True)
    for n, t in saidas.items():
        (raiz / n).write_text(t)
    g = gab["vendas.csv"]
    print(f"vendas.csv: {gab['linhas_no_arquivo']} linhas | limpo: {g['pedidos']} pedidos, R$ {g['faturamento']:.2f}")
    print(f"vendas-mini.csv: {gab['vendas-mini.csv']['linhas_no_arquivo']} linhas")
    print("problemas plantados:", gab["problemas_plantados"])


if __name__ == "__main__":
    main()
