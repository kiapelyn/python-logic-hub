'''Escreva um programa em Python que leia 3 valores inteiros. O programa deverá
ter uma função para determinar e retornar o maior valor digitado'''

def maior(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

a = int(input("Digite o 1º valor: "))
b = int(input("Digite o 2º valor: "))
c = int(input("Digite o 3º valor: "))
m = maior(a, b, c)


print(f"O maior valor é {m}")