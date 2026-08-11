# método recursivo que receba dois parâmetros: uma lista contendo números inteiros e um valor inteiro. 
# A função recursiva deverá retornar o número de ocorrências do valor na lista.

lista = [2, 3, 6, 10, 1, 8, 8, 2, 8]
a = int(input())
b = 0

def vezes(lista, a):
    if not lista: return 0
    if lista[-1] == a: return 1 + vezes(lista[:-1], a)
    else: return vezes(lista[:-1], a)

print(vezes(lista, a))

'''for i in range (len(lista)):
    if a == lista[i]:
        b += 1
        
print(b)'''

        
        