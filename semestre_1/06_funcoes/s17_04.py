'''Escreva um programa em Python para calcular as raízes de uma equação do
segundo grau. O seu programa deverá ter uma função para calcular e retornar o
valor do delta e também uma função para calcular e retornar as duas raízes da
equação'''

def delta(b, a, c):
    d = (b**2)-(4*a*c)
    return d

def raizI(b, d, a):
    rI = ((-b) - d)/(2*a)
    return rI

def raizII(b, d, a):
    rII = ((-b) + d)/(2*a)
    return rII


a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
c = int(input("Qual o valor de c? "))

d = delta(b, a, c)
rI = raizI(d, b, a)
rII = raizII(d, b, a)

print(f"As raízes da função são {rI} e {rII}")
