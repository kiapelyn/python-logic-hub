pedidos = {
 "P001": {"cliente": "Ana", "produtos": {"Mouse": 80.0, "Teclado": 120.0}},
 "P002": {"cliente": "Bruno", "produtos": {"Monitor": 700.0}},
 "P003": {"cliente": "Ana", "produtos": {"Cabo HDMI": 40.0, "Mouse": 80.0}},
 "P004": {"cliente": "Carla", "produtos": {"Cadeira Gamer": 950.0}}
}


def RelatorioID(dicionario):
    valores = {}
    for id , prod in dicionario.items():
        tot = 0
        for i in prod["produtos"].values():
            tot+= i
        valores[id] = tot
    return valores

def RelatiorioPessoa(dicionario):
    valores = {}
    for id, prod in dicionario.items():
        tot = 0
        for i in prod["produtos"].values():
            tot+=i
        if prod["cliente"] in valores:
            valores[prod["cliente"]] += tot
        else:
            valores[prod["cliente"]] = tot
    return valores

def Faturamento(ValoresPedidos):
    tot=0
    for val in ValoresPedidos.values():
        tot+= val
    return tot
    
def main():

    valoresID = RelatorioID(pedidos)

    valoresClie = RelatiorioPessoa(pedidos)

    print(valoresID)
    print(valoresClie)
    print(max(valoresClie))
    print(Faturamento(valoresID))


if __name__ == "__main__":
    main()