'''Escreva um programa em Python que leia três valores inteiros. Imprima-os em ordem
crescente.'''

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a > b:
    aux = a
    a = b
    b = aux

if a > c:
    aux = a
    a = c
    c = aux

if b > c:
    aux = b
    b = c
    c = aux
    
print(a, b, c)