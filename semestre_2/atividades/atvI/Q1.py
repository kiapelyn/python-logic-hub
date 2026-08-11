from random import randint

def gerarMatriz(larg,comp):
    matriz = [[randint(0,10) for i in range(comp)]for j in range(larg)]
    return matriz

def imprimirMatriz(matriz):
    txt = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            txt += "\t" +str(matriz[i][j])
        txt += "\n"
    return print(txt)

def AnaliseMatriz(matriz):
    linhas = len(matriz)
    coluna = len(matriz[0])
    
    nova_matriz = [[ -1 for i in range(coluna+2)] for i in range(linhas+2)]
    
    for i in range(linhas):
        for j in range(coluna):
            nova_matriz[i+1][j+1] = matriz[i][j]
    
    #analiseMatriz
    matrizLetra = [[ '' for i in range(coluna)] for i in range(linhas)]
    for i in range(linhas):
        for j in range(coluna):
            if(nova_matriz[i+1][j+1]>nova_matriz[i+1][j] and
               nova_matriz[i+1][j+1]>nova_matriz[i+1][j+2] and
               nova_matriz[i+1][j+1]>nova_matriz[i][j+1] and
               nova_matriz[i+1][j+1]>nova_matriz[i+2][j+1] and 
               nova_matriz[i+1][j+1]>nova_matriz[i][j] and
               nova_matriz[i+1][j+1]>nova_matriz[i][j+2] and
               nova_matriz[i+1][j+1]>nova_matriz[i+2][j] and
               nova_matriz[i+1][j+1]>nova_matriz[i+2][j+2]
               
               ):
                
                matrizLetra[i][j] = "P"
                
            elif(
                (nova_matriz[i+1][j+1]<nova_matriz[i+1][j] or nova_matriz[i+1][j] ==-1) and 
                (nova_matriz[i+1][j+1]<nova_matriz[i+1][j+2] or nova_matriz[i+1][j+2]==-1) and 
                (nova_matriz[i+1][j+1]<nova_matriz[i][j+1] or nova_matriz[i][j+1]==-1) and 
                (nova_matriz[i+1][j+1]<nova_matriz[i+2][j+1] or nova_matriz[i+2][j+1]==-1) and
                (nova_matriz[i+1][j+1]<nova_matriz[i][j] or nova_matriz[i][j] ==-1) and
               (nova_matriz[i+1][j+1]<nova_matriz[i][j+2] or nova_matriz[i][j+2] ==-1) and
               (nova_matriz[i+1][j+1]<nova_matriz[i+2][j] or nova_matriz[i+2][j] ==-1) and
               (nova_matriz[i+1][j+1]<nova_matriz[i+2][j+2] or nova_matriz[i+2][j+2] ==-1)
            ):
                
                matrizLetra[i][j] = "V"
            
            elif(matrizLetra[i][j] == ""):
                
                matrizLetra[i][j] = "N"                
    
    return matrizLetra
    

def main():
    x = int(input("Insira a altura da matriz: "))
    y = int(input("Insira o comprimento da matriz: "))

    
    matriz = gerarMatriz(x,y)

    imprimirMatriz(matriz)

    matrizLetra = AnaliseMatriz(matriz)

    imprimirMatriz(matrizLetra)

if __name__ == "__main__":
    main()