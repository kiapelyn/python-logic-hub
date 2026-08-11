'''Escreva um programa em python que calcule e imprima no terminal o valor armazenado na série
de Fibonacci a partir da sua posição fornecida via teclado. Por exemplo, o número 8 está
armazenado na 7ª posição da série.'''

from math import inf

posicao = int(input("Digite a posição "))

if posicao <= 0:
    print("A posição deve ser um número maior que 0")
elif posicao == 1:
    print(f"O valor na posição {posicao} da série de Fibonacci é: 0")
else:
    a = 0
    b = 1
    for i in range(2, posicao):
        prox = a + b
        a = b
        b = prox
    print(f"O valor na posição {posicao} da série de Fibonacci é: {b}")