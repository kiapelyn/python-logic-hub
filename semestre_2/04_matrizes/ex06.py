from random import randint

def ler_dados(matriz):
    matriz = [[randint(1, 5) for j in range(len(matriz[i]))] for i in range(len(matriz))]
    return matriz
    
def imprimir(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            #print(f"{matriz[i][j]:>6}", end='')
            print("%6d" % matriz[i][j], end='')
        print()
        
        
def multiplicar(a, b):
    c = []
    for i in range(len(a)):
        linha = []
        for j in range(len(b[0])):
            aux = 0
            for k in range(len(a[i])):
                aux += a[i][k] * b[k][j]
            linha.append(aux)
        c.append(linha)
            
    return c
                
                
    
#programa principal

a = [[1,2],[3,0],[2,1]]
b = [[1,0,1],[2,1,3]]  
imprimir(a)
print()
imprimir(b)
print()
c = multiplicar(a, b)
imprimir(c)



        