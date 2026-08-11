'''Escreva um programa em Python que leia as coordenadas (x, y) de dois pontos no
plano cartesiano. O programa deverá imprimir uma mensagem no vídeo informando
qual dos dois pontos está mais próximo da origem dos eixos (0, 0). A expressão para o
cálculo da distância entre dois pontos a e b é dada por: (expressão nos slides)'''

xa = float(input("Insira o valor de x de a: "))
ya = float(input("Insira o valor de y de a: "))
xb = float(input("Insira o valor de x de b: "))
yb = float(input("Insira o valor de y de b: "))

dist_a = (xa**2 + ya**2)**(1/2)
dist_b = (xb**2 + yb**2)**(1/2)

print(f"Distância de a = {dist_a:.3f}; distância de b = {dist_b:.3f}")

if dist_a < dist_b:
    print("O ponto a está mais perto da origem")
else:
    print("O ponto b está mais perto da origem")
    
