from random import randint
import util
import time

def gerar_lista(n):
    lista = []
    for _ in range(n):
        lista.append(randint(0, n**2))
    return lista

def medir_tempo(algoritmo, lista):
    lista_aux = lista.copy()
    inicio = time.perf_counter()
    # relógio de alta precisão para simulação
    algoritmo(lista_aux)
    # algoritmo aqui é o nome da função, ex: bolha
    fim = time.perf_counter()
    return (fim - inicio) * 1000

def main():
    tamanho = [100, 1000, 10000, 100000]
    print('Comparação entre os métodos de ordenação')
    print()
    for n in tamanho:
        print(f'Lista de tamanho {n}')
        lista = gerar_lista(n)
        tempo_bolha = medir_tempo(util.bolha, lista)
        tempo_selecao = medir_tempo(util.selecao, lista)
        tempo_insercao = medir_tempo(util.insercao, lista)
        tempo_quicksort = medir_tempo(util.quicksort, lista)
        print(f'Tempo bolha: {tempo_bolha:.3f}')
        print(f'Tempo seleção: {tempo_selecao:.3f}')
        print(f'Tempo inserção: {tempo_insercao:.3f}')
        print(f'Tempo quicksort: {tempo_quicksort:.3f}')
        print('-' * 40)


if __name__ == '__main__':
    main()