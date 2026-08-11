'''Dois números inteiros positivos a e b são chamados números amigos se a soma dos divisores
próprios de a for igual a b e a soma dos divisores próprios de b for igual a a, sendo a ≠ b. A
soma dos divisores próprios de um número n corresponde à soma de todos os inteiros
positivos menores que n que o dividem de forma exata. Por exemplo: os divisores próprios
de 220 são: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 e 110. A soma desses divisores é 284. Os
divisores próprios de 284 são: 1, 2, 4, 71 e 142. A soma desses divisores é 220. Assim, 220 e
284 formam um par de números amigos. Escreva um programa em Python que leia um valor
inteiro representando o limite de um intervalo. O seu programa deverá imprimir todos os
pares de números amigos.'''

valor = int(input('valor limite: '))

for i in range(1, valor+1):
    #encontra e soma os divisores de i
    divisor = 0
    for j in range(1, i):
        if i % j == 0:
            divisor += j
    for j in range(1, divisor+1):
        soma = 0
        for k in range(1, j):
            if j % k == 0:
                soma += k

if i == divisor:
    print(f"{valor} e {divisor} são números amigos")
