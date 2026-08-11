'''Escreva um programa em Python (utilize a estrutura if-elif-else) que calcule o valor do
imposto de renda de um contribuinte. Considere que o valor do imposto é calculado de
acordo com a tabela abaixo:'''

renda = float(input("Digite o valor da renda anual:"))

if renda <= 10000.00:
    print("Isento")
elif renda <= 25000.00:
    aliquota = renda * 0.1035
    print(f"Imposto de R${aliquota:.2f}")
elif renda <= 50000.00:
    aliquota = renda * 0.2542
    print(f"Importa de R${aliquota:.2f}")
else:
    aliquota = renda * 0.2975
    print(f"Imposto de R${aliquota:.2f}")