import random
from typing import List

def criarLabirinto(x: int, y: int) -> List[List]:
    a = []
    contPorta = 0
    for _ in range(y):
        aux = []
        for _ in range(x):
            num = random.randint(0,1)
            if num == 0: aux.append('#')
            elif num == 1: aux.append('.')
        a.append(aux)
    
    posX = random.randint(0, x-1)
    posY = random.randint(0, y-1)
    a[posY][posX] = 'E'

    posX = random.randint(0, x-1)
    posY = random.randint(0, y-1)
    a[posY][posX] = 'S'

    return a

def procurarRedor(lab: List[List], xAtual: int, yAtual: int, visitado: List[List]):
    visitado[yAtual][xAtual] = True
    
    # esquerda
    if(xAtual - 1 >= 0):
        novoX, novoY = xAtual - 1, yAtual
        if lab[novoY][novoX] == 'S':
            return True
        elif lab[novoY][novoX] == '.' and not visitado[novoY][novoX]:
            if procurarRedor(lab, novoX, novoY, visitado):
                return True

    # direita
    if(xAtual +1 < len(lab[0])):
        novoX, novoY = xAtual + 1, yAtual
        if lab[novoY][novoX] == 'S':
            return True
        elif lab[novoY][novoX] == '.' and not visitado[novoY][novoX]:
            if procurarRedor(lab, novoX, novoY, visitado):
                return True

    # cima
    if(yAtual - 1 >= 0):
        novoX, novoY = xAtual, yAtual - 1
        if lab[novoY][novoX] == 'S':
            return True
        elif lab[novoY][novoX] == '.' and not visitado[novoY][novoX]:
            if procurarRedor(lab, novoX, novoY, visitado):
                return True

    # baixo
    if(yAtual + 1 < len(lab)):
        novoX, novoY = xAtual, yAtual + 1
        if lab[novoY][novoX] == 'S':
            return True
        elif lab[novoY][novoX] == '.' and not visitado[novoY][novoX]:
            if procurarRedor(lab, novoX, novoY, visitado):
                return True

    # se nenhum caminho funcionou:
    return False

def procurarCaminho(matriz: List[List]) -> bool:
    visitado = [[False for _ in range(len(matriz[0]))] for _ in range(len(matriz))]

    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            if matriz[y][x] == 'E':        
                print(f"X = {x} | Y = {y}")
                return procurarRedor(matriz, x, y, visitado)

# ao criar funcao procurarRedor, colocar como argumento o novo endereço e o endereço de onde veio,
# para que a recursividade não seja chamada para o endereço de onde veio

    
def main():
    #length = int(input(f"Informe o comprimento da matriz"))
    #height = int(input(f"Informe a altura da matriz"))
    length = 4
    height = 5
    mat = criarLabirinto(length, height)

    for linha in mat:
        print(" ".join(f"{valor:3}" for valor in linha))

    existeCaminho = False
    existeCaminho = procurarCaminho(mat)
    print(existeCaminho)


if __name__ == "__main__":
    main()