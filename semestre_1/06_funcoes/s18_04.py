'''Escreva um programa em Python para calcular as raízes de uma equação do
segundo grau. O seu programa deverá ter uma função para calcular e retornar o
valor do delta e também uma função para calcular e retornar as duas raízes da
equação.'''

def delta(b, a, c):
    d = (b**2)-(4*a*c)
    return d

def raiz(b, d, a):
    rI = ((-b) - (d**(1/2)))/(2*a)
    rII = ((-b) + (d**(1/2)))/(2*a)
    return rI, rII

a = int(input("Qual o valor de a? "))

if a != 0:
    b = int(input("Qual o valor de b? "))
    c = int(input("Qual o valor de c? "))
    d = delta(b, a, c)
    if d < 0:
        print("A equação não tem raíz real")
    else:
        rI, rII = raiz(b, d, a)
        print(f"As raízes da função são {rI:.2f} e {rII:.2f}")
else:
    print("O valor de a deve ser diferente de 0")
