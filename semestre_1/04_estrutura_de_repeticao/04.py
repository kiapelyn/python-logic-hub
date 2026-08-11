'''Calcule e imprima no vídeo o valor do imposto de renda mensal que um grupo de n contribuintes
deverá pagar a partir da renda mensal e do número de dependentes (os dados dos contribuintes
deverão ser fornecidos via teclado e armazenados). Para cada contribuinte será feito um
desconto de 5% do salário mínimo vigente por dependente. (valores de líquota dados em imagem)'''

qnt = int(input("Quantos contríbuentes serão catalogados? "))
sl_min = 1518

for i in range(qnt):
    salario = int(input("Qual a renda mensal? "))
    if salario < (sl_min * 2):
        print("Contibuínte isento de pagamento")
    else:
        dep = int(input("Quantos são os dependentes? "))
        vl_dep = dep * (0.05 * sl_min)
        if salario >= (sl_min * 2) and salario < (sl_min * 3):
            vl_imp = salario * 0.05
        elif salario >= (sl_min * 3) and salario < (sl_min * 5):
            vl_imp = salario * 0.1
        elif salario >= (sl_min * 5) and salario < (sl_min * 7):
            vl_imp = salario * 0.15
        else:
            vl_imp = salario * 0.2
        total = vl_imp - vl_dep
        if total <= 0:
            print(f"O valor estipulado é de R${total:.2f}, logo, não há importo a ser recolhido")
        else:
            print(f"O valor do imposto a ser recolhido é de {total:.2f}")