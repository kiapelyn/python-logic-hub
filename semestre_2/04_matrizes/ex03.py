'''Os dados são fornecidos em um formato de matriz (array bidimensional), onde cada linha
representa um ano e cada coluna representa um mês (de janeiro a dezembro).
Instruções:

c) Escreva outra função que determine o ano com a maior média e o ano com a menor média.
d) Implemente um programa principal que utilize essas funções para processar os dados e
imprimir os resultados.
'''
from random import randint
from math import inf
    
#criar matriz
def criar_matriz():
    matriz = [[randint(0,50) for j in range(12)] for i in range(10)]
    return matriz

def imprimir(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='\t')
    print()

def media(matriz):
    media = []
    for i in range(len(matriz)):
        p = 0
        for j in range(len(matriz[i])):
            p += matriz[i][j]
        media.append(p/12)
    return media

def maior(medias):
    maior = 0
    for i in range(len(medias)):
        if medias[i] > maior:
            maior = medias[i]
            ano = i+1
    print(f'O ano com maior temperatura foi {ano}')
    
def menor(medias):
    menor = inf #também é possível inicializar com o maior valor ou com o primeiro valor
    for i in range(len(medias)):
        if medias[i] < menor:
            menor = medias[i]
            ano = i+1
    print(f'O ano com menor temperatura foi {ano}')

def main():
    matriz = criar_matriz()
    imprimir(matriz)
    medias = media(matriz)
    print(f'{medias}')
    maior(medias)
    menor(medias)
    
if __name__ == "__main__":
    main()

