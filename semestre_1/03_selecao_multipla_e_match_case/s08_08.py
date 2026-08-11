'''Reescreva o programa do exercício 7 para aplicar a estrutura match.'''

renda = float(input("Digite o valor da renda anual:"))

match renda:
    case renda if renda <= 10000.00:
        print("Isento")
    case renda if renda <= 25000.00:
        aliquota = renda * 0.1035
        print(f"Imposto de R${aliquota:.2f}")
    case renda if renda <= 50000.00:
        aliquota = renda * 0.2542
        print(f"Importa de R${aliquota:.2f}")
    case _:
        aliquota = renda * 0.2975
        print(f"Imposto de R${aliquota:.2f}")