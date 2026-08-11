'''Escreva um programa em Python que leia um único valor formado por quatro bits
(0s e/ou 1s). O seu programa deverá converter o valor para a base decimal e
imprimir no vídeo.'''

#entrada
original = int(input("Digite um valor de quatro bits: "))

#processamento
unidade = original % 10; unidadef = unidade*1
dezena = original//10 % 10; dezenaf = dezena*2
centena = original//100 % 10; centenaf = centena*4
milhar = original//1000 % 10; milharf = milhar*8

'''milhar = original // 1000; milharf = milhar*8
centena = original % 1000 // 100; centenaf = centena*4
dezena = original % 100 // 10; dezenaf = dezena*2
unidade = original % 10; unidadef = unidade*1'''

resultado = unidadef + dezenaf + centenaf + milharf

#saida
print(f"{original} em decimal é {resultado}")