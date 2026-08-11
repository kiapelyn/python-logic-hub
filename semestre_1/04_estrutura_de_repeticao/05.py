'''Escreva um programa em Python que leia um valor inteiro n que representa o número de linhas
que serão impressas no vídeo. O seu programa deverá imprimir um triângulo formado por
asteriscos (%) conforme figura a seguir. O número de linhas de impressão será exatamente o valor
de n informado pelo usuário da aplicação. Por exemplo, suponha que o usuário tenha informado
o valor 6 para n, o triângulo deverá ter o seguinte formato
%
%%
%%%
%%%%
%%%%%
%%%%%%'''

valor = int(input("Digite um valor inteiro: "))

if valor > 0:
    for i in range(1, valor+1):
        print(i*"%")
else:
    for i in range(valor, 0):
        i = i*-1
        print(i*"%")