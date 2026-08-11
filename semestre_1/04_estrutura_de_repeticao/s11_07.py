'''Faça um programa em Python que leia um número inteiro e positivo e imprima todos os
seus divisores (positivos e negativos).'''

valor = int(input("Digite um valor inteiro e positivo: "))

if valor <= 0:
    print("O valor deve ser inteiro e positivo")
else:
    for cont in range(-valor, valor + 1):
        if cont == 0:
            cont = cont + 1
        elif valor % cont == 0:
            print(cont)