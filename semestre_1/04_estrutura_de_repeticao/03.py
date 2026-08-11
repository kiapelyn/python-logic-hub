'''Escreva um programa em Python que imprima no terminal a soma dos números ímpares de um
intervalo. O início e o fim do intervalo deverão ser fornecidos pelo usuário da aplicação. A soma
deve englobar os extremos do intervalo.'''

soma = 0
inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

for i in range (inicio, fim + 1):
    if i % 2 != 0:
        soma += i
        
print(soma)