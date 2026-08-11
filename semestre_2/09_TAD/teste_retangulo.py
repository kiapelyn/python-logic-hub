from retangulo import Retangulo
from ponto import Ponto

lista = []
n = int(input("Quantos retângulos tu quer? "))
for _ in range(n):
    largura = int(input("Largura --> "))
    altura = int(input("Altura --> "))
    coordenada_x_canto_superior_esquerdo = int(input("Coordenada X --> "))
    coordenada_y_canto_superior_esquerdo = int(input("Coordenada Y --> "))
    lista.append(Retangulo(largura, altura, Ponto(coordenada_x_canto_superior_esquerdo, coordenada_y_canto_superior_esquerdo)))

# Impressão da área
print("Área do retângulo:")
for r in lista:
    print(f"{r} --> {r.calcular_area()}")
print()  

# Impressão do perímetro
print("Perímetro do retângulo:")
for r in lista:
    print(f"{r} --> {r.calcular_perimetro()}")
print()

# Impressão do centro
print("Centro do retângulo:")
for r in lista:
    print(f"{r} --> {r.calcular_centro()}")
print()

# Aumentar tamanho do retângulo
print("Aumento do retângulo:")
for r in lista:
    aumento_largura = int(input("Em quanto vc quer aumentar a largura? "))
    aumento_altura = int(input("Em quanto vc quer aumentar a altura? "))
    print(f"{r} --> {r.aumentar_tamanho(aumento_largura, aumento_altura)}")
print()