
programa_do_ratinho = [
                       {'pai': 'ACGTACGTACGTACG', 'filho':'ACGTACGTACGAACG'},
                       {'pai': 'ACGTACGTACGTACG', 'filho':'ACGTACGTACACACG'},
                       {'pai': 'AGCTA', 'filho':'AGGTC'},
                       {'pai': 'ACGTACGT', 'filho':'ACGTACGA'},
                       {'pai': 'ACGTACGT', 'filho':'ACGTTCGA'},
                       {'pai': 'ACGTACGTACGTACG', 'filho':'ACGTACGTACGTA'},
                       ]

def validar_tamanho(programa_do_ratinho):
    novo_programa_do_ratinho = []
    for i in range(len(programa_do_ratinho)):
        pai, filho = programa_do_ratinho[i].values()
        if len(pai) < 2 or len(filho) < 2 or len(pai) != len(filho):
            novo_programa_do_ratinho.append('DESCARTE')
        else: 
            novo_programa_do_ratinho.append(programa_do_ratinho[i])
    return novo_programa_do_ratinho
            
    
            
def validar_paternidade(novo_programa_do_ratinho):
    valores = []
    for i in range(len(novo_programa_do_ratinho)):
        if novo_programa_do_ratinho[i] != 'DESCARTE':
            pai, filho = novo_programa_do_ratinho[i].values()
            comprimento = (len(pai)//2)
            
            if comprimento % 2 == 0:
                contador = 0
            else: contador = -1
            
            pai = pai[comprimento:]
            filho = filho[comprimento:]
            
            for letrap, letraf in zip(pai, filho):
                if letrap == letraf:
                    contador += 1
            conta = (contador / comprimento)*100
            valores.append(conta)   
        else: 
            valores.append('-')
    return valores
        
def imprimir(valores):
    for i in range(len(valores)):
        if valores[i] == '-':
            print(f'teste {i+1}: - SEQUÊNCIAS DE TAMANHO INVÁLIDO')
        elif valores[i] < 70:
            print(f'teste {i+1}: {valores[i]:.2f}% NÃO COMPATÍVEL')
        else: print(f'teste {i+1}: {valores[i]:.2f}% POTENCIAL PAI-FILHO')
        
    

def main():
    novo_programa_do_ratinho = validar_tamanho(programa_do_ratinho)
    valores = validar_paternidade(novo_programa_do_ratinho)
    imprimir(valores)

if __name__ == "__main__":
    main()