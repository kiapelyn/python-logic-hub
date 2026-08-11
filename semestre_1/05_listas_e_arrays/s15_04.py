'''Escreva um programa em python que leia o nome de cada produto
comercializado por um vendedor, a respectiva quantidade em estoque e o valor
unitário (todos esses valores devem ser armazenados). O seu programa deverá:

a) Imprimir o nome do produto mais caro (considerar mais de um produto com o
mesmo valor).
b) Imprimir o valor total (em reais) de cada produto armazenado.
c) Imprimir o valor total (em reais) armazenado em estoque'''

prod = []
quant = []
preco = []
maxi = 0

total = int(input("Quantos produtos serão cadastrados: "))

for i in range(total):
    print(f"Produto {i+1}")
    prod.append(input("Nome do produto: "))
    preco.append(float(input("Valor do produto: ")))
    quant.append(int(input("Quantidade do produto: ")))
    if preco[i] > maxi or i == 0:
        maxi = preco.index
        maior = prod(preco.index)
print(maior)