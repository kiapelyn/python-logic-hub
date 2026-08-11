'''Escreva um programa em Python que leia um valor na base binária e faça a conversão para
a base decimal. O seu programa deverá validar se o número está na base binária antes de fazer a
conversão. Caso não esteja, o usuário da aplicação deverá ser informado. O número informado
pelo usuário poderá ter qualquer quantidade de bits.'''

bin = int(input("Digite um valor na base binária: "))
decimal = 0
i = 0

if bin > 11111111:
    print("Número inválido")
    
    while bin > 0:
        digito = bin % 10
        decimal = decimal + digito * (2**i)
        i = i + 1
        bin = bin// 10

print(f"O valor {bin} na base decimal é {decimal}")

#revisar