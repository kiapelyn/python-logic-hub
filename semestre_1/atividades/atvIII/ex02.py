aplicacao = float(input("Insira o valor da aplicação mensal: "))
taxa = float(input("Insira o valor da taxa mensal de juros (apenas o número): "))
meses = float(input("Insira o número de meses de aplicação: "))

juros = (taxa / 100) * aplicacao
valor_acumulado = aplicacao * (((1 + juros) ** meses - 1)/juros)

print(f"O valor do rendimento é de R${valor_acumulado:.2f}")