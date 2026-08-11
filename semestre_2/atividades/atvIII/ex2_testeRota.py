from rota import Rota

def insercao(lista: list[Rota]) -> list[Rota]:
    n = len(lista)
    for j in range(1, n):
        valor = lista[j]
        tempo = valor.tempo_total_min()
        i = j - 1
        while i >= 0 and tempo < lista[i].tempo_total_min():
            lista[i + 1] = lista[i]
            i -= 1
        lista[i + 1] = valor
    return lista

def main():
    total = int(input("Qual o total de rotas? "))
    lista = []
    
    for i in range(total):
        nome = input(f"\nIdentificador da rota {i+1}: ")
        trecho = []
        
        nm_trechos = int(input(f"Quantos trechos compõem a rota {nome}? "))
        
        for j in range(nm_trechos):
            dist_km = float(input("Dist Km: "))
            vel_kmh = float(input("Vel Kmh: "))
            semaforos = int(input("Qtde semaforos: "))
            trecho.append({'dist_km': dist_km, 'vel_kmh': vel_kmh, 'semaforos': semaforos})
        
        delay_sinal = float(input("Atraso médio do semáforo (s): "))

        lista.append(Rota(nome, trecho, delay_sinal))
    
    lista_ordenada = insercao(lista)
    
    print("[Ranking por Tempo Total]")
    for i in range(len(lista_ordenada)):
        print(f'{i+1}) {lista_ordenada[i]}')
    
    print()    
    inicio_min = int(input('Tempo mínimo: '))
    fim_min = int(input('Tempo máximo: '))
    print()
    
    print("\n" + "=" * 50)
    print(f"[Rotas que atendem a janela {inicio_min}-{fim_min} min]")
    print("=" * 50)

    contagem = 0
    for rotinha in lista_ordenada:
        
        if rotinha.atende_janela(inicio_min, fim_min):
            print(f"- Rota {rotinha.nome:<15} (Tempo: {rotinha.tempo_total_min():.2f} min)")
            contagem += 1 
            
    if contagem == 0:
        print('Nenhuma rota atende a janela')
            
    print("\n" + "=" * 50)
    print("[Comparativo de Emissões]")
    print("=" * 50)
    kg_co2_km = 0.192
    
    for rotinha in lista_ordenada:
        dist_total = 0.0
        for t in rotinha.trecho:
            dist_total += t.get("dist_km")
            
        emissao = rotinha.custo_emissao(kg_co2_km)
        
        print(f"Rota {rotinha.nome:<15}| Dist: {dist_total:.1f} km | Emissão: {emissao:.2f} kg CO2") 
    

if __name__ == '__main__':
    main()
    