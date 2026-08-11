from ponto import Ponto

qnt = int(input())
lista = []

def entrar_dados(qnt):
    for i in range(qnt):
        x = int(input(f'x{i+1} -> '))
        y = int(input(f'y{i+1} -> '))
        print()
        lista.append(Ponto(x, y))
    return lista

def imprimir_dados(lista):
    print(f'{'Ponto':<12}{'Distância'}')
    print('-'*30)
    for pontos in lista:
        print(f'{str(pontos):<12}{pontos.distancia_origem():.2f}')
        
def main():
    lista = entrar_dados(qnt)
    print('-'*30)
    imprimir_dados(lista)
    
if __name__ == '__main__':
    main()