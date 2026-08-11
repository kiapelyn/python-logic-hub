import random
from math import inf 

'''programa para preencher uma lista com 10 números e colocá-los em ordem crescente.'''

# comando "pass" para dizer para uma função que você não vai fazê-la agora

def ler_dados():
    for i in range(10):
        lista1.append(random.randint(2, 57))

def imprimir():
    for i in range(len(lista1)):
        print(lista1[i], end=' ')

def ordenar():
    for _ in range(len(lista1)):
        for i in range(len(lista1)-1):
            if lista1[i] > lista1[i]:
                aux = lista1[i]
                lista1[i] = lista1[i+1]
                lista1[i+1] = aux
    print(lista1[i])

#principal
lista1 = []
ler_dados()
print("\nDados antes da ordenação")
imprimir()
ordenar()
    