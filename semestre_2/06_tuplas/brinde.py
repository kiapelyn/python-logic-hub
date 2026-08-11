'''Implemente uma função em Python que recebe uma lista de tuplas, onde cada
tupla representa um intervalo numérico [a, b], com a ≤ b. A função deve
realizar as seguintes operações:
c) Retornar a soma total do comprimento de todos os intervalos resultantes'''

from random import randint

lista = []
lista2 = []

def atribuir_valores():
    for i in range(randint(2,8)):
        valor1 = randint(0,10)
        valor2 = randint(0,10)
        if valor1 > valor2:
            valor1, valor2 = valor2, valor1
        tupla = (valor1, valor2)
        lista.append(tupla)
    return lista
    

def sobreposto(lista):
    for i in range(len(lista)):
        for j in range(1, len(lista)):
            if i == j:
                break
            else:
                a, b = lista[i]
                c, d = lista[j]
                if b >= c:
                    mini = min(a, c)
                    maxi = max(b, d)
                    novo = (mini, maxi)
            if novo not in lista and novo not in lista2:
                lista2.append(novo)
                
    return lista2
    
def sobreposto2(lista):
    a, b = lista[0]
    for i in range(1, len(lista)):
        c, d = lista[i]
        if c < a:
            a = min(a, c)
            b = max(b, d)
            novo = (a, b)
        if novo not in lista2:
            lista2.append(novo)
            
    return lista2


def comprimento(lista):
    soma = 0
    for i in range(len(lista)):
        a, b = lista[i]
        c = b-a
        soma += c
    return soma
    
lista = atribuir_valores()
lista2 = sobreposto(lista)
listanova = sobreposto2(lista)
soma = comprimento(lista2)
print(lista)
print(lista2)
print(listanova)
print(len(lista2))
print(soma)