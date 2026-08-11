'''Escreva um programa em Python para calcular e imprimir no vídeo o valor da
expressão abaixo. O valor da expressão deve ser exibido no vídeo com três casas
decimais.'''

#para usar comandos matematicos é necessário importar a biblioteca
from math import sqrt
from math import pow 

#Entrada
x = float(input("Digite o valor de x: "))

#Processamento
a = pow(x,4) 
b = pow(x,2)
c = (a-1)/(2*b)
d = pow(c,2)
e = b/2
f = 1+d
y = sqrt(f) - e


#Saida
print(f"O valor de y é {y:.3f}")