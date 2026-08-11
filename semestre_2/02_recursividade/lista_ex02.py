# método recursivo que receba dois parâmetros: uma lista contendo números inteiros e um valor inteiro. 
# A função recursiva deverá retornar true caso o valor esteja presente na lista ou false caso contrário

lista = [2, 3, 6, 10, 1, 8]
a = int(input())

def existe(lista, a):
    if not lista: return False
    if lista[-1] == a: return True
    return existe(lista[:-1], a)
        
        
'''Sem recursividade

for i in range(len(lista)):
    if a not in lista:
        x = False
    else: x = True'''
    
print(existe(lista, a))