'''Escreva um programa em python que calcule e imprima no terminal o valor da série S a partir de
x e n informados pelo usuário da aplicação.'''

x = int(input("Valor de x: "))
n = int(input("Valor de n: "))
s = 0

for i in range (1, n+1):
    s += (x**i)/i
    
print(s)