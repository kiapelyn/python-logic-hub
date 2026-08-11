'''Escreva um programa em Python que preencha um matriz quadrada de ordem 5
com valores aleatórios. Em seguida, troque os elementos da diagonal principal com
os elementos da diagonal secundária.'''

from random import randint

def gerar_matriz():
    matriz = [[randint(1, 100) for j in range(5)] for i in range(5)]
    return matriz
    
def imprimir(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(matriz[i][j], end='\t')
        print()

    


def mudar_matriz(matriz):
    j = len(matriz) - 1
    for i in range(len(matriz)):
            aux = matriz[i][i]
            matriz[i][i] = matriz[i][j]
            matriz[i][j] =  aux   
            j -= 1         

matriz = gerar_matriz()
imprimir(matriz)
print('matriz alterada')
mudar_matriz(matriz)
imprimir(matriz)