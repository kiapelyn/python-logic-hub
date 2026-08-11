# programa para calcular o volume de uma lata de óleo

from math import pi 
raio = float(input("Insira o valor do raio: "))
altura = float(input("Insira o valor da altura: "))
v = pi * raio**2 * altura
print(f"o volume equivale à {v:.3f}")