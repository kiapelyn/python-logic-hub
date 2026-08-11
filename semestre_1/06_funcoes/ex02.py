'''Escreva um programa em Python que armazene uma quantidade de números inteiros em uma
lista. A quantidade de números da lista deverá ser informada pelo usuário da aplicação que, por sua
vez, também deverá informar os valores para serem armazenados. Em seguida o seu programa
deverá calcular e imprimir no terminal a diferença (subtração) entre o maior e o menor valor
armazenado. Para calcular o maior e o menor valor da lista você deverá utilizar as funções do módulo
util.py.'''

qnt = int(input("Quantos serão os números da lista? "))

def calcular_maior():
    for i in range(len(lista)):
        if i == 0:
            maior = lista[i]
        elif lista[i] > maior:
            maior = lista[i]    
    return maior

def calcular_menor():
    for i in range(len(lista)):
        if i == 0:
            menor = lista[i]
        elif lista[i] < menor:
            menor = lista[i]
    return menor

lista = []
for j in range(qnt):
    lista.append(int(input("valor: ")))

maior = calcular_maior()
menor = calcular_menor()

sub = maior - menor

if sub < 0:
    sub = sub *-1
    
print(f"A diferença é {sub}")