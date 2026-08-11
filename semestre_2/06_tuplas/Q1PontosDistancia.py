from random import randint
from math import sqrt

# função para gerar a lista de pontos
def gerar_pontos():
    lista = [] # --> lista = list()
    for _ in range(randint(1, 5)):
        lista.append((randint(-10, 10), randint(-10, 10)))
    return lista

# função para calcular a distância de cada um dos pontos até a origem
def calcular_distancia(lista):
    distancia = []
    for i in range(len(lista)):
        x, y = lista[i]
        distancia.append(sqrt(x * x + y * y))
    return distancia

# função para retornar o ponto mais distante da origem
def maisDistante(lista, distancia):
    ponto = lista[0]
    maior = distancia[0]
    for i in range(len(lista)):
        if distancia[i] > maior:
            maior = distancia[i]
            ponto = lista[i]
    return ponto

# função para retornar o ponto mais próximo da origem
def maisProximo(lista, distancia):
    ponto = lista[0]
    menor = distancia[0]
    for i in range(len(lista)):
        if distancia[i] < menor:
            menor = distancia[i]
            ponto = lista[i]
    return ponto

# função para calcular a média das distância
def calcularMedia(distancia):
    media = 0
    for d in distancia:
        media += d
    return media / len(distancia)
    
# função main()
def main():
    lista = gerar_pontos()
    distancia = calcular_distancia(lista)
    for i in range(len(lista)):
        print(f'{lista[i]} --> {distancia[i]:.2f}')

    print(f'ponto mais distante em relação a origem --> {maisDistante(lista, distancia)}')
    print(f'ponto mais próximo em relação a origem --> {maisProximo(lista, distancia)}')
    print(f'média das distâncias --> {calcularMedia(distancia):.2f}')
    
    
if __name__ == '__main__':
    main()