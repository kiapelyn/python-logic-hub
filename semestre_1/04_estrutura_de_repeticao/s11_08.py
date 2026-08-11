'''Escreva um programa em Python que leia um valor inteiro e positivo. Imprima uma
mensagem no vídeo informando se o número digitado é ou não um número primo. Um
número é primo quando é divisível apenas por 1 e por ele mesmo.'''

valor = int(input("Digite um valor inteiro e positivo: "))

'''
if valor <= 0:
    print("O valor deve ser inteiro e positivo")
else:
    if valor % 2 != 0 or valor == 2
        if valor % 3 != 0 or valor == 3):
            num = "valor primo"
        else:
            num = "valor não primo"
        print(num)'''

total = 0

if valor <= 0:
    print("O valor deve ser inteiro e positivo")
else:
    for cont in range(1, valor + 1):
        if valor % cont == 0:
            total += 1
    if total == 2:
        print(f"{valor} é primo")
    else:
        print(f"{valor} não é primo")
        
'''dic6 = {
    'Aaron': 10,
    'Andrew': 8,
    'Dan': 9,
    'Kevin': 6.9,
    'Matt': 4.9,
    'Neil': 7.1
}

for aluno in dic6:
  maior = max(({dic6[aluno]}))

print(maior)'''