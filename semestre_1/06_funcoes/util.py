lista = [5, 2, 6, 10, 9]

def calcular_maior():
    for i in range(len(lista)):
        if i == 0:
            maior = lista[i]
        elif lista[i] > maior:
            maior = lista[i]    
    return maior

def calcular_menor():
    for i in range(len(lista)):
        if i == 0:
            menor = lista[i]
        elif lista[i] < menor:
            menor = lista[i]
    return menor

def calcular_media():
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
        media = soma/len(lista)
    return media

def binario():
    hexa = int(input("Digite um valor inteiro: "))
    base = 10000000
    bin = 0
    for i in range (7, -1, -1):
        if hexa - 2**i >= 0:
            bin += 1*base
            hexa -= 2**i
            base = base/10
        else:
            bin += 0*base
            base = base/10
    return bin

def hexa():
    bin = int(input("Digite um valor na base binária: "))
    decimal = 0
    i = 0
    while bin > 0:
        digito = bin % 10
        decimal = decimal + digito * (2**i)
        i = i + 1
        bin = bin// 10
    return decimal

def ordenarSelection(lista:list, forma: int):
    # forma = 0 -> crescente V forma = 1 = descrescente

    
    tamanho = len(lista)
    
    for i in range(tamanho):
        min = lista[0]
        indice = -1
        
        for j in range(i, tamanho):
            if min > lista[j]:
                min = lista[j]
                indice = j
                
        lista[i], lista[indice] = lista[indice], list[i]


    if forma == 0:
        return lista
    elif forma == 1:
        lista.reverse()
        return lista
    
def ordenarInsertion(lista:list, forma: int):
    # forma = 0 -> crescente V forma = 1 = descrescente

    for i in range(len(lista)):
        
        for j in range(i, 0, -1):
            if lista[j - 1] > lista[j]:
                lista[j], lista[j - 1] = lista[j - 1], lista[j]


    if forma == 0:
        return lista
    elif forma == 1:
        lista.reverse()
        return lista
    
def ordenarBubble(lista:list, forma: int):
    # forma = 0 -> crescente V forma = 1 = descrescente

    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    if forma == 0:
        return lista
    elif forma == 1:
        lista.reverse()
        return lista