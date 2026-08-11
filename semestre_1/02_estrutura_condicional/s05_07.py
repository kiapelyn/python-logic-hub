'''Escreva um programa em Python que leia três valores e verifique se os mesmos
representam os lados de um triângulo. Observação: Para que os valores representem os
lados de um triângulo é necessário que cada um dos lados seja menor que a soma dos
outros dois'''

a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))

if a < (c+b) and b < (a+c) and c < (a+b):
    print("É um triângulo")
else:
    print("Não é um triângulo")