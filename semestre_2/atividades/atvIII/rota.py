class Rota:
    def __init__(self, nome: str, trecho: list[dict], delay_sinal: float):
        self.nome = nome
        self.trecho = trecho
        self.delay_sinal = delay_sinal
        
    def tempo_total_min(self) -> float:
        tempo_h = 0.0
        soma_semaforos = 0
        
        for i in self.trecho:
            if i.get("vel_kmh") > 0:
                tempo_h += i.get("dist_km") / i.get("vel_kmh")
            soma_semaforos += i.get("semaforos")
            
        d_m = self.delay_sinal / 60
        paradas_min = soma_semaforos * d_m
        tempo_total_min = 60 * tempo_h + paradas_min
        
        return tempo_total_min
    
    def velocidade_media_kmh(self) -> float:
        distancia_total = 0.0
        for i in self.trecho:
            distancia_total += i.get("dist_km")
            
        horas = self.tempo_total_min() / 60
        
        if horas == 0:
            return 0.0
            
        velocidade_media = distancia_total / horas
        
        return velocidade_media
    
    def atende_janela(self, inicio_min: float, fim_min: float) -> bool:
        tempo = self.tempo_total_min()
        if tempo >= inicio_min and tempo <= fim_min:
            return True
        return False
    
    def custo_emissao(self, kg_co2_km: float) -> float:
        distancia_total = 0.0
        for i in self.trecho:
            distancia_total += i.get("dist_km")
            
        emissao = distancia_total * kg_co2_km
        return emissao

    def __str__(self) -> str:
        return (f'Rota {self.nome:<10} | Tempo: {self.tempo_total_min():.2f} min | '
                f'Vel. média: {self.velocidade_media_kmh():.1f} km/h')