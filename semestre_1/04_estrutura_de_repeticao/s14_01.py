'''Escreva um programa em Python que leia um valor inteiro e positivo. O seu programa deverá
exibir um padrão triangular de números conforme exemplo mostrado na figura a seguir.
Suponha que na entrada de dados o usuário da aplicação tenha informado o número inteiro
4.'''

num = int(input("Insira um número inteiro: "))


for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end=' ') # end=' ' não deixa quebrar as linhas
    print() # quebra linha :D