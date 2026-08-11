'''No último final de semana foi realizado um campeonato de arco e flecha na faculdade. Durante
a competição, cada competidor poderia lançar duas vezes a flecha ao alvo e a distância de cada
lançamento para cada jogador era registrada pelos juízes da competição. O competidor vencedor
foi aquele que lançou a flecha mais próxima do alvo nas duas tentativas, ou seja, o vencedor
atingiu a menor distância nas duas tentativas.
Escreva um programa em python que leia o nome e a distância atingida por cada competidor nas
duas tentativas. O seu programa deverá imprimir no terminal o nome do vencedor.'''

from math import inf

qnt = int(input("Quantos jogadores participaram? "))
soma = 0
dist = 0

for i in range(qnt):
    nome = input("Qual o nome do jogador? ")
    fl1 = float(input("Qual a distância do primeiro alvo? "))
    fl2 = float(input("Qual a distância do segundo alvo? "))
    if (fl1 + fl2) < dist or i == 0:
        dist = fl1+fl2
        nm = nome

print(nm)

    