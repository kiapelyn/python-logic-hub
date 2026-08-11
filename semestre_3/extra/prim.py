import heapq

# função para transformar a lista de tuplas usada no kruskal para uma lista de adjacência
def construir(arestas, n):      
    adj = [[] for _ in range(n)]
    for peso, u, v in arestas:
        adj[u].append((peso, v))   # aresta u-v...
        adj[v].append((peso, u))   # ...nos dois sentidos
    return adj

def prim(n, adj, raiz=0):
    # adj[u] = lista de (peso, v)
    visitado = [False] * n
    agm, custo = [], 0
    # heap de (peso, origem, destino)
    # 0 -> custo para entrar na raiz; -1 -> para indicar que não tem origem
    heap = [(0, -1, raiz)]
    while heap:
        peso, u, v = heapq.heappop(heap)
        if visitado[v]:
            continue            # ja esta na arvore
        visitado[v] = True
        
        if u != -1:
            agm.append((u, v, peso)); custo += peso
        
        for w, viz in adj[v]:
            if not visitado[viz]:
                heapq.heappush(heap, (w, v, viz))
    return agm, custo

# programa principal
# (peso, u, v)
arestas = [
            (7,0,1),(3,0,2),(4,1,2),
            (2,1,3),(5,2,3),(6,2,4),
            (4,3,4),(5,3,5),(8,4,5)
          ]

adj = construir(arestas, 6)
print(prim(6, adj, 0))