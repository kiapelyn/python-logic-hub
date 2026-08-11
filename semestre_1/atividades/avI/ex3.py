bicidisp = int(input("Insira a quantidade de bicicletas disponíveis: "))
alug = float(input("Insira o valor do aluguel diário: "))

if bicidisp <= 0 or alug <= 0:
    print("Os valores devem ser maiores que 0")
else:
    multa = alug * 0.1
    bicialug = bicidisp // 3
    biciatmen = bicialug * 30 // 10

    faturamento = bicialug * 365

    ganhomulta = multa * biciatmen

    print(f"O faturamento anual é de R${faturamento:.2f}")
    print(f"O ganho mensal com multas é de R${ganhomulta:.2f}")