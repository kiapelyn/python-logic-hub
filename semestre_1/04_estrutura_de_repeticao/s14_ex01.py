lista = []

for contador in range(5):
    lista.append(int(input("Insira um valor: ")))

for i in range(len(lista)):
    print(lista[i], end=' ')
    
print()
for elemento in lista:
    print(elemento, end=' ')
    