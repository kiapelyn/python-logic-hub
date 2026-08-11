from random import randint
n = 12

with open('financiamento.txt', 'r') as arquivo:
    for linha in arquivo:
        i = randint(1,10) / 100
        linha = linha.strip()
        nome, valor = linha.split(';')
        PMT = float(valor)*((i*((i+1)**n))/(((i+1)**n)-1))
        print(f'{nome} pretende financiar R${float(valor):.2f} ')
        print(f'em {n} parcelas de R${PMT:.2f} com {i*100:.0f}% de juros')
        print()