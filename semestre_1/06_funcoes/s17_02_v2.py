def classificar():
    if ladoa == ladob and ladoa == ladoc and ladob == ladoc:
        print("Triângulo Equilátero")
    elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
        print("Triângulo Isósceles")
    elif ladoa != ladob and ladoa != ladoc and ladob != ladoc:
        print("Triângulo Escaleno")

def validar():
    return ladoa < (ladoc+ladob) and ladob < (ladoa+ladoc) and ladoc < (ladoa+ladob)
    #vai voltar um valor booleano (true ou false)
    
ladoa = float(input("Insira o primero lado: "))
ladob = float(input("Insira o segundo lado: "))
ladoc = float(input("Insira o terceiro lado: "))

if(validar()):
    classificar()
else:
    print("Não é um triângulo")