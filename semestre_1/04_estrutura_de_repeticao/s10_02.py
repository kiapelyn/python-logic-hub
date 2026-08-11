'''Escreva um programa em Python que leia 15 números fornecidos pelo usuário.
Imprima o maior valor informado.'''


contador = 1

while contador <= 5:
    valor = int(input("Digte um valor: "))
    if contador == 1 or valor > maior:
        maior = valor
    contador = contador + 1
print(maior)
