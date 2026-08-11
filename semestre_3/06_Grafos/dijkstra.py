
import heapq


# função para calcular o caminho mínimo
def dijkstra(grafo, origem):
    
    # grafo: dict {u: [(v, peso), ...]}
    distancia = {v: float('inf') for v in grafo}
    anterior  = {v: None for v in grafo}
    distancia[origem] = 0
    fila = [(0, origem)]  # (distância, vértice)

    while fila:
        d_atual, u = heapq.heappop(fila)
        if d_atual > distancia[u]:
            continue  # já há caminho melhor

        for v, peso in grafo[u]:
            nova = d_atual + peso
            if nova < distancia[v]:    # relaxamento
                distancia[v] = nova
                anterior[v]  = u
                heapq.heappush(fila, (nova, v))

    return distancia, anterior


# função para reconstruir o caminho
def reconstruir_caminho(anterior, destino):    
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = anterior[atual]
    caminho.reverse()
    return caminho


# grafo do material (slide passo a passo)
# 6 vértices (0..5), não direcionado, pesos positivos.
# esperado: distâncias [0, 2, 3, 5, 4, 6]; caminho 0→5 = 0→1→4→5 (custo 6).
def main():
    # grafo não direcionado: cada aresta aparece nas duas listas.
    grafo = {
        0: [(1, 2), (2, 6)],
        1: [(0, 2), (2, 1), (3, 3), (4, 2)],
        2: [(0, 6), (1, 1), (4, 4)],
        3: [(1, 3), (4, 2), (5, 4)],
        4: [(1, 2), (2, 4), (3, 2), (5, 2)],
        5: [(3, 4), (4, 2)],
    }

    dist, ant = dijkstra(grafo, origem=0)
    caminho = reconstruir_caminho(ant, 5)
    print(caminho)
    
if __name__ == '__main__':
    main()
    