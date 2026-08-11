'''Escreva um programa em Python que leia uma quantidade de números inteiros informados pelo
usuário da aplicação. Ao final da digitação de todos os números, o seu programa deverá imprimir
no terminal a soma de todos os números também a média aritmética. Observação: quantos
números o usuário irá digitar? O seu programa deverá solicitar a quantidade de números e, em
seguir, cada número será digitado.'''

qnt = int(input("Quantos valores serão inseridos? "))
soma = 0

for i in range(qnt):
    valor = int(input("Digite um número inteiro: "))
    soma += valor
    media = soma/qnt

print(soma)
print(media)
