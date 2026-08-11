
# função para executar o percurso em profundidade no grafo
def dfs(grafo, origem):    
    visitados = set()
    ordem = []
    anterior = {v: None for v in grafo}

    def visitar(u):
        visitados.add(u)
        ordem.append(u)
        for v in sorted(grafo[u], key=str):   # ordem alfabética/numérica
            if v not in visitados:
                anterior[v] = u
                visitar(v)

    visitar(origem)
    return ordem, anterior


# função para executar o percurso em profundidade no grafo NÃO direcionado
def dfs_com_ciclo(grafo, origem):    
    visitados = set()
    ordem = []
    ciclos = []

    def visitar(u, pai):
        visitados.add(u)
        ordem.append(u)
        for v in sorted(grafo[u], key=str):
            if v not in visitados:
                visitar(v, u)
            elif v != pai:
                # aresta de retorno → ciclo
                aresta = tuple(sorted((u, v), key=str))
                if aresta not in ciclos:
                    ciclos.append(aresta)

    visitar(origem, None)
    return ordem, ciclos


# função para imprimir a ordem da visita
def imprimir_ordem(ordem, titulo="Ordem de visita"):
    print(f"\n  {titulo}: {' → '.join(str(v) for v in ordem)}")


# teste 01 - grafo do material (slide "DFS execução passo a passo")
# direcionado: 0→1, 0→3, 1→2, 1→3, 2→0, 3→2
# esperado: ordem [0, 1, 2, 3] (vizinhos em ordem crescente).
def teste_1_dfs_direcionado():
    print("=" * 70)
    print("TESTE 01 — DFS em grafo DIRECIONADO (exemplo do material)")
    print("=" * 70)

    grafo = {
        0: [1, 3],
        1: [2, 3],
        2: [0],
        3: [2],
    }

    ordem, anterior = dfs(grafo, origem=0)
    imprimir_ordem(ordem)
    print(f"  Anterior: {anterior}")  


# teste 02 — DFS em grafo NÃO direcionado, com detecção de ciclo
# slide "DFS em grafo NÃO direcionado": A-B, A-C, B-C, C-D
# esperado: ordem [A, B, C, D]; ciclo detectado via aresta A-C.
def teste_2_dfs_nao_direcionado_com_ciclo():
    print("\n" + "=" * 70)
    print("TESTE 02 — DFS em grafo NÃO direcionado com detecção de ciclo")
    print("=" * 70)

    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D'],
        'D': ['C'],
    }

    ordem, ciclos = dfs_com_ciclo(grafo, origem='A')
    imprimir_ordem(ordem)
    print(f"  Arestas de retorno (ciclos): {ciclos}")

# programa principal
if __name__ == "__main__":
    teste_1_dfs_direcionado()
    teste_2_dfs_nao_direcionado_com_ciclo()
    
    