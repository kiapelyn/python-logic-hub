'''Escreva um programa em Python para calcular e imprimir no vídeo o valor da
expressão abaixo. O valor da expressão deve ser exibido no vídeo com três casas
decimais.'''

import math

# Entrada
x = float(input("Digite o valor de x: "))

# Processamento
y = math.sqrt(math.cbrt(x-1/2))

'''a = x-(1/2)
b = a**(1/3)
y = pow(b,(1/2)) 
os dois são a mesma coisa'''

# Saida
print(f"O valor de y é {y:.3f}")