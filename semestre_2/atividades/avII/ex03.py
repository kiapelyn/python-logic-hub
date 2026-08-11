qnt = int(input())

def ler_dados(qnt):
    dados = []
    for i in range(qnt):
        t = ((input('data: ')), float(input('tmin: ')), float(input('tmax: ')))
        dados.append(t)
    return dados

def calcular_amplitude(dados):
    temps = []
    for data, tmin, tmax in dados:
        amplitude = tmax - tmin
        temps.append((data, amplitude))
    return temps
        
def calcular_media(temps, dados):
    medias = []
    for (data, amplitude), (data, tmin, tmax) in zip(temps, dados):
        media_dia = (tmin + tmax)/2
        data_dia = data
        medias.append((data_dia, media_dia, amplitude))
    return medias
    
def maior(medias):
    maiortemp = 0
    for data, media_dia, amplitude in medias:
        if amplitude > maiortemp:
            maiortemp = amplitude
            datamax = data
    return datamax, maiortemp    
    

def main():
    dados = ler_dados(qnt)
    temps = calcular_amplitude(dados)
    medias = calcular_media(temps, dados)
    datamax, maiortemp = maior(medias)
    print(f'a data de maior amplitude foi {datamax} com {maiortemp:.1f}°C')
    
if __name__ == "__main__":
    main()