'''Escreva um programa em Python que calcule as raízes de uma equação do segundo grau.
Lembre-se que uma equação do segundo grau tem a seguinte forma: ax**2 + bx + c = 0.'''

from math import sqrt

a = float(input("Digite o valor de a: "))

if a == 0:
    print("A variável a não pode ser 0")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = b**2 - 4*a*c
    if delta <= 0:
        print("O delta não tem raiz real")
    else:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        print(f"x1 = {x1:.3f}, x2 = {x2:.3f}")