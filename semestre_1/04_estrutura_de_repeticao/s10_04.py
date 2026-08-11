'''Escreva um programa em Python que calcule o fatorial de um número inteiro e
positivo'''

from math import factorial

valor = int(input("Digite um valor inteiro e positivo: "))
contador = 1

if valor < 0:
    print("O valor deve ser positivo e inteiro")
else:
    while contador <= valor:
        if contador == 1:
            fatorial = 1
            contador = contador + 1
        else:
            fatorial = fatorial * contador 
            contador = contador + 1
            
print(f"{valor}! = {fatorial}")

'''resultado = factorial(valor)
    print(resultado)'''