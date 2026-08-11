inicio = int(input("Digite o valor de inicio: "))
fim = int(input("Digite o valor de fim: "))
perfeitos = 0

for i in range (inicio, fim+1):
    soma = 0
    for j in range(1, i):
        if i % j == 0:
            soma += j
    if soma == i:
        perfeitos += 1
        print(i, soma)
print(perfeitos)