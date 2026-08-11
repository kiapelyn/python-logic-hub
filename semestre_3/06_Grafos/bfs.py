
from collections import deque


# função para exercutar o percurso em largura no grafo
def bfs(grafo, origem):
    distancia = {v: float('inf') for v in grafo}
    anterior  = {v: None for v in grafo}
    distancia[origem] = 0
    ordem = []
    fila = deque([origem])

    while fila:
        u = fila.popleft()
        ordem.append(u)
        for v in grafo[u]:
            if distancia[v] == float('inf'):   # ainda não visitado
                distancia[v] = distancia[u] + 1
                anterior[v]  = u
                fila.append(v)

    return distancia, anterior, ordem


# função para reconstruir o caminho a partir do dicionário anterior
def reconstruir_caminho(anterior, destino):
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = anterior[atual]
    caminho.reverse()
    return caminho

# testando o grafo do material (slide "BFS caminho mínimo não ponderado")
def main():
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D', 'E'],
        'D': ['B', 'C', 'E'],
        'E': ['C', 'D'],
    }

    dist, ant, ordem = bfs(grafo, origem='A')
    print(f"\n  Ordem de visita: {' → '.join(ordem)}")
    

# programa principal
if __name__ == '__main__':
    main()