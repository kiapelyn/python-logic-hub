'''Escreva um programa em python que leia um valor inteiro a partir do teclado. Imprima uma
mensagem informando para o usuário a quantidade de dígitos que compõe o valor informado.'''

valor = int(input("Insira um valor inteiro: "))
digitos = 1

if valor >= 0:
    while valor > 9:
        valor = valor // 10
        digitos += 1
        
elif valor < 0:
    while valor < -10:
        valor = valor // 10
        digitos += 1

print(digitos)
    