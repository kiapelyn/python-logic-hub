'''Escreva um programa em Python que leia n pontos no plano cartesiano (coordenada x e coordenada y) e
imprima no vídeo as coordenadas (x e y) do ponto mais distante e mais perto da origem (ponto de
coordenadas x = 0 e y = 0). A quantidade n de pontos deverá ser informada no início do programa. A
fórmula da distância entre dois pontos a e b é dada por:

Na fórmula apresenta, xa indica a coordenada x do ponto a e, xb indica a coordenada x do ponto b. A mesma
observação é feita para a coordenada y.
Observação: não serão levados em consideração empates, ou seja, dois ou mais pontos que tenham a
maior distância em relação a origem dos pontos. Seguem alguns valores de teste'''

from math import inf

qnt = int(input("Qual a quantidade de pontos que serão informados? --> "))
xb = 0
yb = 0
madist = 0
mendist = inf

for i in range(qnt):
    xa = float(input("Valor de x:"))
    ya = float(input("Valor de y:"))
    d = ((xa-xb)**2 + (ya-yb)**2)**(1/2)
    print(f"Distância até a origem --> {d}")
    if d > madist:
        madist = d
        maix = xa
        maiy = ya
    if d < mendist:
        mendist = d
        menx = xa
        meny = ya
        
print(f"O ponto mais distante tem coordenadas --> ({maix}, {maiy})")
print(f"O ponto mais perto tem coordenadas --> ({menx}, {meny})")

    