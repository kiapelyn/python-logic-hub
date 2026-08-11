def preco_cada(vendas, precos):
    totais_venda = []
    for venda in vendas:
        soma = 0
        for produto in venda:
            for nome, preco in precos.items():
                if nome == produto:
                    soma += preco
        totais_venda.append(f"R$ {soma:.2f}")
    return totais_venda

def preco_total(vendas, precos):
    soma_geral = 0
    for venda in vendas:
        soma = 0
        for produto in venda:
            for nome, preco in precos.items():
                if nome == produto:
                    soma += preco
        soma_geral += soma
    return round(soma_geral, 2)

def qtde_total(vendas):
    qtde_por_item = {}
    for venda in vendas:
        for produto in venda:
            if produto in qtde_por_item:
                qtde_por_item[produto] += 1
            else:
                qtde_por_item[produto] = 1
    return qtde_por_item

def mais_vendido(qtde_por_item):
    maior = 0
    maior_nome = ''
    for nome,qtde in qtde_por_item.items():
        if qtde > maior:
            maior = qtde
            maior_nome = nome
    return maior_nome

def maior_faturamento(qtde_por_item, precos):
    faturamento = {}
    maior = 0
    maior_nome = ""
    for nome, preco in precos.items():
        for produto, qtde in qtde_por_item.items():
            if nome == produto:
                faturamento[nome] = qtde * preco
                
    for nome_i, faturamento_i in faturamento.items():
        if faturamento_i > maior:
            maior = faturamento_i
            maior_nome = nome_i
    return maior_nome
            

def ticket_medio(preco_geral, vendas):
    ticket = preco_geral / len(vendas)
    return round(ticket, 2)
                      
            

def main():
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
    
    totais_venda = preco_cada(vendas, precos)
    
    preco_geral = preco_total(vendas,  precos)
    
    qtde_por_item = qtde_total(vendas)
    
    maior_vendido = mais_vendido(qtde_por_item)
    
    maior_valor = maior_faturamento(qtde_por_item, precos)
    
    ticket = ticket_medio(preco_geral, vendas)

    relatorio = {
        "totais_venda": totais_venda,
        "faturamento_total": preco_geral,
        "qtd_por_item": qtde_por_item,
        "mais_vendido": maior_vendido,
        "mais_faturado": maior_valor,
        "ticket_medio": ticket
    }
    
    print(relatorio)
    
if __name__ == '__main__':
    main()