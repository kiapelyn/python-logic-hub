'''Escreva um programa em Python que leia os lados de n triângulos. Para cada triângulo
imprima a sua classificação quanto aos lados (equilátero, isósceles ou escaleno). O
programa deverá parar a execução quando o usuário digitar o valor zero para um dos
lados. Observação: para que os valores formem um triângulo é necessário que cada um
dos lados seja menor que a soma dos outros dois'''

n = int(input("Insira a quantidade de triangulos:"))

while True:
    ladoa = float(input("Insira o primero lado: "))
    ladob = float(input("Insira o segundo lado: "))
    ladoc = float(input("Insira o terceiro lado: "))

    if ladoa == 0 or ladob == 0 or ladoc == 0:
        break
    
    if ladoa < ladob+ladoc or ladob < ladoa+ladoc or ladoc < ladoa+ladob:
        if ladoa == ladob and ladoa == ladoc and ladob == ladoc:
            print("Triângulo Equilátero")
        elif (ladoa == ladob or ladoa == ladoc or ladob) and ladoa != ladob != ladoc:
            print("Triângulo Isósceles")