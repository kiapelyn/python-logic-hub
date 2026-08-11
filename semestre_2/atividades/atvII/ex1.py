from random import randint

def criar_matriz(ordem):
    matriz_original = [[randint(0, 50) for j in range(ordem)] for i in range(ordem)]
    return matriz_original

def imprimir(matriz, ordem):
    for i in range(ordem):
        for j in range(ordem):
            print(matriz[i][j], end='\t')
        print()

def analisar_matriz(matriz):
    n = len(matriz)
    resultado = [['N' for j in range(n)] for i in range(n)]

    testes = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    for i in range(n):
        for j in range(n):
            centro = matriz[i][j]
            redor = []

            for a, b in testes:
                x = i + a
                y = j + b
                if 0 <= x < n and 0 <= y < n:
                    redor.append(matriz[x][y])

            if centro > max(redor):
                resultado[i][j] = 'P'
            elif centro < min(redor):
                resultado[i][j] = 'V'

    return resultado

def main():
    ordem = int(input())
    matriz = criar_matriz(ordem)
    imprimir(matriz, ordem)
    print()
    resultado = analisar_matriz(matriz)
    imprimir(resultado, ordem)
    

if __name__ == "__main__":
    main()

    


            
                
