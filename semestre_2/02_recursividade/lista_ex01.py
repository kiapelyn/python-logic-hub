# método recursivo que receba como parâmetro uma lista contendo números inteiros e seu tamanho. 
# A função recursiva deverá retornar o maior valor armazenado na lista

lista = [2, 3, 6, 10, 1, 8]
a = len(lista)

def maior(lista, a):
    if a == 1: return lista[0]
    else:
        maior_restante = maior(lista, a - 1)
        if lista[a - 1] > maior_restante: return lista[a - 1]
        else: return maior_restante
       
    
    
print(maior(lista, a))


'''aux = 0
for i in range(a):
    if lista[i] > aux or i == 0:
        aux = lista[i]
print(aux)'''