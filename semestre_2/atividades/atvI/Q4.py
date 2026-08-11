precos = {
    "arroz": 22.5,
    "feijao": 9.8,
    "leite": 4.7,
    "pao": 1.5
}

vendas = [
    ["arroz", "feijao", "feijao", "leite"],
    ["pao", "pao", "pao", "leite"],
    ["arroz", "leite"],
    ["feijao", "feijao", "feijao"]
]


def TotVendas(vendas, precos):
    totais = []
    for venda in vendas:
        total = 0
        for item in venda:
            total += precos[item]
        totais.append(total)
    return totais


def FaturamentoTot(totais):
    fat = 0
    for valor in totais:
        fat += valor
    return fat


def QtdItem(vendas):
    qtd = {}
    for venda in vendas:
        for item in venda:
            if item in qtd:
                qtd[item] += 1
            else:
                qtd[item] = 1
    return qtd


def MaisVendido(qtd):
    maior = 0
    produto = ""
    for nome, valor in qtd.items():
        if valor > maior:
            maior = valor
            produto = nome
    return produto


def MaisFaturado(qtd, precos):
    maior = 0
    produto = ""
    for nome, valor in qtd.items():
        faturamento = valor * precos[nome]
        if faturamento > maior:
            maior = faturamento
            produto = nome
    return produto


def TicketMed(faturamento, vendas):
    return faturamento / len(vendas)


def Relatorio(vendas, precos):

    totais = TotVendas(vendas, precos)
    qtd = QtdItem(vendas)
    faturamento = FaturamentoTot(totais)
    mais_vendido = MaisVendido(qtd)
    mais_faturado = MaisFaturado(qtd, precos)
    ticket = TicketMed(faturamento, vendas)

    relatorio = {
        "TotVendas": totais,
        "FaturamentoTot": faturamento,
        "QtdItem": qtd,
        "mais_vendido": mais_vendido,
        "mais_faturado": mais_faturado,
        "TicketMed": ticket
    }

    return relatorio


def main():
    relat = Relatorio(vendas, precos)

    print("Totais de cada venda: ", relat["TotVendas"])
    print("Faturamento total: ", relat["FaturamentoTot"])
    print("Quantidade vendida por item: ", relat["QtdItem"])
    print("Produto mais vendido: ", relat["mais_vendido"])
    print("Produto mais faturado: ", relat["mais_faturado"])
    print("Ticket médio: ", relat["TicketMed"])


if __name__ == "__main__":
    main()
