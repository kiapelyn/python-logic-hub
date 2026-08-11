'''Escreva um programa em python para preencher um vetor de 1000 posições
com valores fornecidos pelo usuário. Imprima no vídeo apenas os números
primos armazenados no vetor. Um número é primo quando ele tem apenas 2
divisores (1 e ele mesmo)'''
from math import sqrt

lista = []

for _ in range(5):  # Mantendo o range(6) para os testes
    lista.append(int(input('Digite o valor: ')))
for num in lista:
    divisor = 0
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
                divisor += 1
                break
    if divisor == 0:
        print(num, end=" ")
