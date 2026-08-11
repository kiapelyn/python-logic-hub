'''Uma mercearia de bairro mantém um cadastro enxuto dos produtos com três informações:
saldo: quantidade atual em estoque;
min: estoque mínimo desejado para não faltar produto;
preco: preço unitário de reposição.
Durante o dia, o sistema registra movimentações: entradas positivas (reposição, devolução) e
saídas negativas (vendas, perdas). No fechamento, o gerente precisa:
a) aplicar as movimentações ao estoque;
b) listar quais produtos ficaram abaixo do mínimo, para facilitar o pedido de compra.
'''

estoque = {
"café": {"saldo": 10, "min": 12, "preco": 12.50},
"pão": {"saldo": 30, "min": 25, "preco": 2.00},
"queijo": {"saldo": 5, "min": 12, "preco": 34.00},
}
movimentacao = [
["café", -3],
["pão", -10],
["café", 5],
["leite", 8] # produto novo não cadastrado
]

for i in range(len(movimentacao)):
    mudanca = movimentacao[i][1]
    saldos = estoque.get('saldo')
    mov = saldos + mudanca
    print(estoque)

    '''if movimentacao[i][1] not in estoque:
        estoque[0] = movimentacao[i][0]
        estoque[1] = mudanca
    print(mudanca, saldos)'''
    
