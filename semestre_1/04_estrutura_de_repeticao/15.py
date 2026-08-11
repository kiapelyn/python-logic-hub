'''O fatorial de um número natural é representado por um ponto de exclamação (!), por exemplo,
10! = 10 x 9 x 8 x ... x 3 x 2 x 1 = 3628800. A soma dos dígitos do número 10! é 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. Escreva um programa em python que leia um valor natural informado pelo teclado e
calcule e imprima a soma de todos os dígitos do fatorial do número informado.'''

valor = int(input("Digite um número inteiro e positivo: "))
cont = 1
total = 1
soma = 0
base = 10

while cont <= valor:
    total = total * cont
    cont = cont + 1
    
while soma >= 0:
    a = (total % base)
    b = a / base * 10
    base = base * 10
    soma = soma + b // 1
    if base > (total*10):
        break
    
print(f"{valor}! = {total}")
print(f"{total} --> {soma}")

