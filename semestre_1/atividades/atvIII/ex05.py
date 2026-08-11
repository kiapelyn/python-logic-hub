ladoa = float(input("Insira o primero lado: "))

if ladoa <= 0:
    print("O lado deve ser maior que 0")
else:
    ladob = float(input("Insira o segundo lado: "))
    if ladob <= 0:
        print("O lado deve ser maior que 0")
    else:
        ladoc = float(input("Insira o terceiro lado: "))
        if ladoc <= 0:
            print("O lado deve ser maior que 0")
        else:
            if (ladoa > ladob) and (ladoa >= ladoc):
                a = ladoa
                b = ladob
                c = ladoc
            elif (ladob > ladoa) and (ladob >= ladoc):
                a = ladob
                b = ladoa
                c = ladoc
            elif (ladoc > ladoa) and (ladoc >= ladob):
                a = ladoc
                b = ladob
                c = ladoa
                if a >= (c+b):
                    print("Não é um triângulo")
                else:
                    if a**2 == (b**2 + c**2):
                        print("Triângulo retângulo")
                    elif a**2 < (b**2 + c**2):
                        print("Triângulo acutângulo")
                    elif a**2 > (b**2 + c**2):
                        print("Triângulo obtusângulo")

'''fabs(x)  retorna o valor de x sem
sinal.

floor(x)  retorna o menor número
inteiro menor ou igual x

ceil(x)  retorna o menor número
inteiro maior ou igual a x

round(x, qtd)  retorna o valor de um
número arredondado de acordo com a
quantidade qtd.

trunc(y)  retorna a parte inteira de um
número, descartando suas casas decimais.'''