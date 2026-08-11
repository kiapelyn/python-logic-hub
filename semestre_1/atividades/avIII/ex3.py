def coletar_dados():
    qnt = (int(input("Quantas ações serão analisadas? ")))
    for i in range(qnt):
        nome.append(input("Nome da ação: "))
        abertura.append(float(input("Valor da ação na abertura: ")))
        fechamento.append(float(input("Valor da ação no fechamento: ")))
    return nome, abertura, fechamento

def calcular_variação():
    for i in range(len(nome)):
        vari = ((fechamento[i] - abertura[i])/abertura[i])*100
        print(f"A ação {nome[i]} teve variação de {vari:.2f}%")
        v.append(vari)
    print("--------------------------------------")
    return v

def simular_retorno():
    for i in range(len(v)):
        retorno = 1000 * v[i]
        print(f"Um investimento de R$1000,00 na ação {nome[i]} terá retorno de R${retorno:.2f}")
        r.append(retorno)
    print("--------------------------------------")
    return r

def calcular_maior():
    for i in range(len(r)):
        if i == 0:
            ma = r[i]
            maior = nome[i]
        elif r[i] > ma:
            ma = r[i]
            maior = nome[i]    
    return maior

def calcular_menor():
    for i in range(len(r)):
        if i == 0:
            me = r[i]
            menor = nome[i]
        elif r[i] < me:
            me = r[i]
            menor = nome[i]
    return menor
    


nome = []
abertura = []
fechamento = []
v = []
r = []

nome, abertura, fechamento = coletar_dados()
v = calcular_variação()
r = simular_retorno()
maior = calcular_maior()
menor = calcular_menor()

print(f"A ação mais lucrativa é a {maior}")
print(f"A ação menos lucrativa é a {menor}")


