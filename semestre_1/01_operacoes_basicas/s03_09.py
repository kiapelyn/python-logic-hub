'''Escreva um programa em Python que leia um único valor contendo três dígitos, por
exemplo, 697. O seu programa deverá inverter a ordem dos dígitos e imprimir o
resultado no vídeo. Por exemplo, se o usuário digitar 697, o seu programa deverá
imprimir no vídeo o valor 796. Você deverá utilizar apenas o conteúdo apresentado
em aula na resolução do problema.'''

from math import trunc

original = int(input("Digite um valor real de três digitos: "))
unidade = (original % 10); removuni = (original - unidade)//10; uni = unidade*100
dezena = (removuni % 10); removdez = (removuni - dezena)//10; dez = dezena*10
centena = (removdez)

# centena = original // 100
# dezena = original % 100 // 10
# unidade = valor % 10

resultado = uni + dez + centena

print(f"Resultado: {resultado}")