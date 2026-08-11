# variáveis fixas
quantalug = 0.4
quantcompra = 0.2
quantinutil = 0.05

anddisp = int(input("Quantos andaimes estão disponíveis para locação? "))

if anddisp <= 0:
    print("A quantidade de andaimes deve ser maior que 0")

else:
    alugd = float(input("Qual o valor do aluguém diário de cada andaime? "))
    
    if alugd <= 0:
        print("O valor do alguém deve ser maior que 0" )
    
    else:
        # faturamento anual
        alugados = (anddisp * quantalug)
        faturamento = alugd * alugados * 30
        anual = faturamento * 12

        # estoque final
        inutil = anddisp * quantinutil
        compra = anddisp * quantcompra
        estoque = compra + anddisp - inutil

        print(f"O faturamento anual com aluguéis é de R${anual:.2f}")
        print(f"Ao final do ano há {estoque:.0f} andaimes disponíveis")