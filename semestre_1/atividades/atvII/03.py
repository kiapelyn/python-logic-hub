qnt = int(input("Quantos alunos participaram da pesquisa? "))
a = 0
c = 0
t = 0

for i in range(qnt):
    voto = int(input("Você é afavor (1) ou contra (2) a estação de bicicletas da ESPM? "))

    if voto != 1 and voto != 2:
        print("Por favor, escolha uma opção válida (1 ou 2)")
        
    elif voto == 1:
            a += 1
            t +=1
    else:
        c += 1
        t += 1

pora = a * 100 / t
porc = c * 100 / t
print(f"De um total de {t} alunos, {pora}% votaram afavor e {porc}% votaram contra")