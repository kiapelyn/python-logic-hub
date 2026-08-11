'''Escreva um programa em python que preencha um vetor de 1000 posições
com valores fornecidos pelo usuário. Imprima no vídeo a quantidade de
números pares e ímpares digitados e a porcentagem de pares e ímpares.'''

lista = []
total_pares = 0
total_impares = 0

for i in range(5):
    lista.append(int(input("Digite o valor: ")))
    if lista[i] % 2 == 0:
        total_pares += 1
    else:
        total_impares += 1
        
print(f"{total_pares} números são pares e {total_impares} são ímpares")
print(f"{total_pares/len(lista)*100}% são pares e {total_impares/len(lista)*100}% são ímpares")    