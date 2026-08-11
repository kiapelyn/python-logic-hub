from random import randint

def gerar_labirinto():
    n = int(input())
    labirinto = []

    for i in range(n):
        linha = []
        for j in range(n):
            valor = randint(0, 1)

            if valor  == 0:
                linha.append('#')
            else:
                linha.append('.')
        labirinto.append(linha)


    x_de_entrada = randint(0, n-1)
    y_de_entrada = randint(0, n-1)
    x_de_saida = randint(0, n-1)
    y_de_saida = randint(0, n-1)


    while x_de_entrada == x_de_saida and y_de_entrada == y_de_saida:
        x_de_saida = randint(0, n-1)
        y_de_saida = randint(0, n-1)

    labirinto[x_de_entrada][y_de_entrada] = 'E'
    labirinto[x_de_saida][y_de_saida] = 'S'

    return labirinto


def mostrar_labirinto(labirinto):
    for linha in labirinto:
        print(' '.join(linha))
    print()


def encontrar_entrada(labirinto):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == 'E':
                return i, j


def existe_caminho(labirinto, x, y, visitado):

    if x < 0 or x >= len(labirinto) or y < 0 or y >= len(labirinto):
        return False

    if labirinto[x][y] == '#' or visitado[x][y]:
        return False

    if labirinto[x][y] == 'S':
        return True

    visitado[x][y] = True

    if (existe_caminho(labirinto, x-1, y, visitado) or
        existe_caminho(labirinto, x+1, y, visitado) or
        existe_caminho(labirinto, x, y-1, visitado) or
        existe_caminho(labirinto, x, y+1, visitado)):
        return True

    return False


def main():
    labirinto = gerar_labirinto()
    mostrar_labirinto(labirinto)

    entrada_x, entrada_y = encontrar_entrada(labirinto)


    n = len(labirinto)
    visitado = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(False)
        visitado.append(linha)


    if existe_caminho(labirinto, entrada_x, entrada_y, visitado):
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()
