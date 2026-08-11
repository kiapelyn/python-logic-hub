'''Escreva um programa em python que preencha um vetor de 1000 posições
com valores fornecidos pelo usuário. Imprima no vídeo o maior e o menor
valor armazenado.'''

lista = []
mini = 0
maxi = 0

for i in range(1000):
    lista.append(int(input("Digite o valor: ")))
    if lista[i] > maxi or i == 0:
        maxi = lista[i]
    if lista[i] < mini or i == 0:
        mini = lista[i]

print("menor valor = ", mini, "maior valor = ", maxi)

# outra forma

menor = min(lista)
maior = max(lista)
print("menor valor = ", menor, "maior valor = ", maior)
print(lista)