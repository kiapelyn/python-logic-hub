'''Escreva um programa em Python que leia um valor inteiro e positivo (o valor
deverá ser testado). O seu programa deverá imprimir no vídeo todos os divisores
inteiros do valor informado pelo usuário. A impressão dos valores deverá ser
feito em uma função'''

def dividir():
    m = a//2
    for i in range(1, m+1):
            if a % i == 0:
                print(i, end=' ')
    print(a)

a = int(input("Digite um valor inteiro positivo: "))
if a > 0:
    dividir()
else:
    print("O valor deve ser inteiro e maior que 0")