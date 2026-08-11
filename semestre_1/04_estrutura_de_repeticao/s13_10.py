'''Escreva um programa em Python para calcular e exibir no vídeo o valor da expressão
abaixo.'''

n = int(input("insira o valor de n: "))
inicio = 1
y = 0

for calc in range(n):
    if inicio % 2 == 0:
        conta = 1/inicio
        y = y - conta
    elif inicio % 2 != 0:
        conta = 1/inicio
        y = y + conta
    inicio = inicio + 1

print(f"o valor da expressão é {y}")