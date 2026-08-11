'''Escreva um programa em Python que calcule o fatorial de um número inteiro e
positivo'''

valor = int(input("Digite um número inteiro e positivo: "))
cont = 1
total = 1

while cont <= valor:
    total = total * cont
    cont = cont + 1
    
print(total)