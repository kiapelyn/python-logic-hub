'''
    Implemente uma função em Python que recebe uma lista de tuplas, onde cada
    tupla representa as coordenadas (x, y) de um ponto no plano cartesiano. A
    função deve gerar e imprimir no terminal as seguintes informações:
    a) O ponto mais distante da origem (0, 0).
    b) O ponto mais próximo da origem (0, 0).
    c) A média das distâncias dos pontos à origem.

'''

from math import sqrt

#tupla via terminal
'''qnt = int(input())
t = []

for i in range(qnt):
    a = int(input())
    b = int(input())
    t.append((a, b))'''

t = [(12,15),(32,32),(15,31),(65,43)]

def calcular_dist(list):
    dist = []
    for i in range(len(t)):
        dist.append(sqrt(t[i][0]**2 + t[i][1]**2))
    return dist 
    
def dist_maior(distancia, pontos):
    aux = dist[0]
    maior = t[0]
    for i in range(1, len(dist)):
        if dist[i] > aux:
            aux = dist[i]
            maior = t[i]
    return maior

def dist_menor(distancia, pontos):
    aux = dist[0]
    menor = t[0]
    for i in range(1, len(dist)):
        if dist[i] < aux:
            aux = dist[i]
            menor = t[i]
    return menor
        
def dist_media(distancia):
    soma = 0
    for i in dist:
        soma += i
    return soma/len(dist)

if __name__ == '__main__':
    dist = calcular_dist(t)
    print(dist_maior(dist, t))
    print(dist_menor(dist, t))
    print(f"{dist_media(dist):.2f}")