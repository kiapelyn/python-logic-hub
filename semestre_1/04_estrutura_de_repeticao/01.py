'''Faça um programa em Python que determine o mostre os cinco primeiros múltiplos de 3, a partir
de um número inteiro informado via teclado pelo usuário da aplicação.'''

from math import inf

valor = int(input("Digite o número: "))

multiplo = -inf
i = 0
parar = 0

while parar < 5:
    if valor % 3 == 0:
        print(valor)
        parar = parar + 1
        valor = valor + 1
    else:
        valor = valor + 1
            