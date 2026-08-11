'''Escreva um programa em Python que leia dois valores inteiros e positivos representando o
início e o fim de um intervalo de números. Imprima todos os números primos no intervalo
formado pelos números informados pelo usuário.'''

inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
        
for i in range(inicio, fim+1):
    total = 0
    for j in range(1, i+1):
        if i % j == 0:
            total += 1
    if total == 2 or i == 1:
        print(i, end=' ')