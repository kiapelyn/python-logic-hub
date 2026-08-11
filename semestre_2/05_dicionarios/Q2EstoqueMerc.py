
# função para atualizar o estoque
def atualizar(estoque, movimentacao):
    for mov in movimentacao:
        produto = mov[0]
        quantidade = mov[1]
        
        if produto not in estoque:
            estoque[produto] = {"saldo": quantidade, "min": 0, "preco": 0}
        
        estoque[produto]["saldo"] += quantidade

# retorna itens abaixo do mínimo com sugestão de compra e custo
def abaixo_do_minimo(estoque):
    relatorio = []
    for produto, info in estoque.items():
        if info["saldo"] < info["min"]:
            comprar = info["min"] - info["saldo"]
            custo = round(comprar * info["preco"], 2)
            relatorio.append({
                "produto": produto,
                "saldo": info["saldo"],
                "min": info["min"],
                "comprar": comprar,
                "preco": info["preco"],
                "custo_estimado": custo
            })
    return relatorio

# função main
def main():
    estoque = {
    "café":   {"saldo": 10, "min": 12, "preco": 12.50},
    "pão":    {"saldo": 30, "min": 25, "preco": 2.00},
    "queijo": {"saldo":  5, "min": 12, "preco": 34.00},
    }

    movimentacao = [
        ["café", -3],
        ["pão", -10],
        ["café", 5],
        ["leite", 8]   # produto novo não cadastrado
    ]
    
    # atualizar o estoque a partir das movimentações do dia
    atualizar(estoque, movimentacao)
    
    # fechamento: listar produtos abaixo do mínimo
    faltantes = abaixo_do_minimo(estoque)
    for item in faltantes:
        print(f"{item['produto']}: saldo={item['saldo']}, min={item['min']}, "
              f"comprar={item['comprar']} (preço {item['preco']:.2f}) "
              f"custo≈{item['custo_estimado']:.2f}")

# programa principal
if __name__ == '__main__':
    main()