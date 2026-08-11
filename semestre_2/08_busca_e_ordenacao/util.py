# Función para realizar la búsqueda lineal en una lista numérica.
# La función debe recibir como parámetro la lista y el valor que se desea localizar.
def localizar_posicao(lista: list[int], valor: int) -> int:
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
        else:
            return -1
        
# Función para ordenar una lista de números enteros en orden ascendente utilizando el método de burbuja.
def bolha(lista):      
    for _ in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista
            

# Funcion para ordenar una lista de números enteros en orden ascendente utilizando el método de selección
def selecao(x):
    n = len(x)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if x[j] < x[menor]:
                menor = j
            
        # Troca os elementos (essa linha precisa estar dentro do laço externo)
        x[i], x[menor] = x[menor], x[i]

def busca_sequencial(lista: list[int], valor: int) -> int:
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  
    return -1  

def busca_binaria(lista: list[int], valor):
    ini, fim = 0, len(lista) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            ini = meio + 1
        else:
            fim = meio - 1
    return -1

        
        
# Función para ordenar una lista de números enteros en orden ascendente utilizando el método de inserción
def insercao(x):
    n = len(x)
    for j in range(1, n):
        valor = x[j]
        i = j - 1
        while i >= 0 and valor < x[i]:
            x[i + 1] = x[i]
            i -= 1
        x[i + 1] = valor
        
# Función para ordenar una lista de números enteros en orden ascendente utilizando el método de quicksort (pivote como el ultimo elemento)
def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    
    if inicio < fim:
        pivote = particionar(lista, inicio, fim)
        quicksort(lista, inicio, pivote - 1)
        quicksort(lista, pivote + 1, fim)
    
        
def particionar(lista, inicio, fim) -> int: # Devuelve el índice pivote
    
    #pivo como primeiro elemento
    #lista[inicio], lista[fim] = lista[fim], lista[inicio]
    
    #pivo no meio
    #lista[fim], lista[fim//2+1] = lista[fim//2+1], lista[fim]'''
    
    #pivo como ultimo elemento
    pivote = lista[fim]
    i = inicio - 1
    
    for j in range(inicio, fim):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    # Coloca el pivote en la ubicación correcta
    lista[i+1], lista[fim] = lista[fim], lista[i+1]
    return i+1


def mergesort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    esquerda_ordenada = mergesort(esquerda)
    direita_ordenada = mergesort(direita)
    
    return juntar_listas(esquerda_ordenada, direita_ordenada)

def juntar_listas(esq, dir):
    i = 0  # índice da lista da esquerda (para ninguém fazer confusão entre os índices)
    j = 0  # índice da lista da direita
    resultado = []
    
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    # cuidado: é importante verificar se sobre algum elemento na 
    # lista da esquerda ou na da direita. Se sobrar algum elemento,
    # acrescenta no final da lista
    while i < len(esq):
        resultado.append(esq[i])
        i += 1

    while j < len(dir):
        resultado.append(dir[j])
        j += 1

    return resultado