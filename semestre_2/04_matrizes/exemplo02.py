row = int(input("total de linhas --> "))
col =  int(input("total de colunas --> "))

#colocando o exemplo01 em apenas uma linha

m = [[int(input("valor --> ")) for j in range(col)] for i in range(row)]

print(m)