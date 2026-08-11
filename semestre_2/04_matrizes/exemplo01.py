row = int(input("total de linhas --> "))
col =  int(input("total de colunas --> "))

m = []
#controle de linha
for i in range(row):
    aux = []
    #controle de coluna
    for j in range(col):
        aux.append(int(input(f"valor {i}.{j} --> ")))
    m.append(aux)


print(m)