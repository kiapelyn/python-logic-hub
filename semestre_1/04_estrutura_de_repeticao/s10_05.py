'''Escreva um programa em Python que calcule o valor da expressão abaixo:'''

n = int(input("Digite o valor da variável n: "))
contador = 1

while contador <= n:
    if contador == 1:
        y = 1
        contador = contador + 1
    else:
        valor = 1/(contador**(1/2))
        y = y + valor
        contador = contador + 1

print(y)
