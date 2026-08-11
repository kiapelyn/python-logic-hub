from emprestimo import Emprestimo


def bolha(lista: list[Emprestimo]) -> list[Emprestimo]:
    n = len(lista)
    for j in range(n): 
        for i in range(n - 1 - j): 
            if lista[i].calcular_vlr_total_juros() > lista[i + 1].calcular_vlr_total_juros():
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


def main():
    lista = []
    
    qnt = int(input('Quantidade de empréstimos: '))
    
    for i in range(qnt):
        vlr_financiado = float(input("Valor financiado: "))
        tx_juros_mensal = float(input("Taxa de juros mensal (em %): "))
        nm_parcelas = int(input("Número de parcelas: "))
        id_emprestimo = input("Identificador do empréstimo: ")
        nome_cliente = input("Nome do cliente: ")
        print()
        
        lista.append(Emprestimo(vlr_financiado, tx_juros_mensal, nm_parcelas, id_emprestimo, nome_cliente))
    
    lista_ordenada = bolha(lista)
    
    print("[Ranking por Juros Totais]")
    for i in range(len(lista_ordenada)):
        print(f'{i+1}) {lista_ordenada[i]}')
    print()
    print('-' * 30)
    print()
    
    
    print("[Saldos após 12 parcelas]")
    k = 12
    
    
    for emp in lista_ordenada:
        saldo = emp.saldo_devedor(k)
        print(f"{emp.id_emprestimo:<15}: R$ {saldo:10.2f}") 
        

if __name__ == '__main__':
    main()