'''Desenvolva um programa em Python que calcule o valor da expressão:'''
from math import sqrt

n = int(input("Digite o valor da última variável: "))
cont = 1
total = 0

if n <= 0:
    print("O número deve ser MAIOR que 0")
else:
    while cont <= n:
        total = total + cont/sqrt(cont)
        cont = cont + 1
    print(total)