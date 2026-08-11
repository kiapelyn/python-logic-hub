def gasto_pedido(dici):
    totais = {}
    for pedido, info in dici.items():
        produtos = info["produtos"]
        valor = sum(produtos.values())
        totais[pedido] = valor
    return totais

def gasto_cliente(dici):
    totais = {}
    for cliente, info in dici.items():
        cliente = info["cliente"]
        valor = sum(info["produtos"].values())
        
        if cliente in totais:
            totais[cliente] += valor
        else:
            totais[cliente] = valor
            
    return totais

def maior_gasto(dici):
    maior = 0
    cliente_maior = ""
    for cliente, valor in dici.items():
        if valor > maior:
            maior = valor
            cliente_maior = cliente
    return (f"o cliente com maior gasto foi {cliente_maior} com R${maior:.2f}")
    
        
def faturamento(dici):
    soma = sum(dici.values())
    return (f"o faturamento foi de R${soma:.2f}")
    
def main():
    pedidos = {
        "P001": {"cliente": "Ana", "produtos": {"Mouse": 80.0, "Teclado": 120.0}},
        "P002": {"cliente": "Bruno", "produtos": {"Monitor": 700.0}},
        "P003": {"cliente": "Ana", "produtos": {"Cabo HDMI": 40.0, "Mouse": 80.0}},
        "P004": {"cliente": "Carla", "produtos": {"Cadeira Gamer": 950.0}}
        }
    
    print(gasto_pedido(pedidos))
    por_cliente = gasto_cliente(pedidos)
    print(por_cliente)
    print(maior_gasto(por_cliente))
    print(faturamento(por_cliente))
    
if __name__ == "__main__":
    main()
