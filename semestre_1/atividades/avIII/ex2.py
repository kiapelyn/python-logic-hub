def coletar_dados():
    for i in range(1, 8):
        sensor1.append(float(input(f"Volume de chuva (em mm) do sensor 1 para o dia {i}: ")))
        sensor2.append(float(input(f"Volume de chuva (em mm) do sensor 2 para o dia {i}: ")))
    return sensor1, sensor2

def calcular_media_diaria():
    for i in range(len(sensor1)):
        mediadiaria.append((sensor1[i]+sensor2[i])/2)
    return mediadiaria

def calcular_acumulo_semanal():
    acumulo = 0
    for i in range(len(mediadiaria)):
        acumulo += mediadiaria[i]
    return acumulo

def emitir_alerta():
    if acumulo <= 100:
            alerta = "Sem alerta"
    elif acumulo > 100 and acumulo < 201:
            alerta = "Alerta Amarelo"
    elif acumulo > 200 and acumulo < 301:
            alerta = "Alerta Laranja"
    else:
            alerta = "Alerta Vermelho"
    return alerta

sensor1 = []
sensor2 = []
mediadiaria = []

sensor1, sensor2 = coletar_dados()

mediadiaria = calcular_media_diaria()
print(f"média diária da semana: {mediadiaria}")

acumulo = calcular_acumulo_semanal()
print(f"total acumulado da semana: {acumulo}")

alerta = emitir_alerta()
print(alerta)
            