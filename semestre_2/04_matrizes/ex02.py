'''Escreva um programa em Python que preencha uma matriz quadrada de ordem 4 com
valores inteiros aleatórios. Em seguida:
a) Mostre a soma dos elementos da diagonal principal.
b) Mostre a soma dos elementos da diagonal secundária.'''

from random import randint

#meu jeito

m = []
msp = []
sp = 0
mss = []
ss = 0

for i in range(4):
    aux = []
    for j in range(4):
        aux.append(randint(1,10))
        if i == j:
            sp += aux[i]
            msp.append(aux[i])
        if i + j == 3:
            ss += aux[j]
            mss.append(aux[j])
    m.append(aux)


print(f"matriz principal --> {m}")
print(f"soma principal --> {msp} --> {sp}")
print(f"soma secundária --> {mss} --> {ss}")

#jeito do professor

matriz = [[randint(1, 10) for j in range(4)] for i in range(4)]
dp = 0
ds = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j], end='\t')
    print()

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            dp += matriz[i][j]

        if i + j == 3:
            ds += matriz[i][j]


print(f"soma principal --> {dp}")
print(f"soma secundária --> {ds}")