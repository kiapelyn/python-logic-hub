class Professor:
    def __init__(self, nome, nm_aulas_semanais, vlr_hr_aula, titulo, hora_extra: str):
        self.nome = nome
        self.nm_aulas_semanais = nm_aulas_semanais
        self.vlr_hr_aula = vlr_hr_aula
        self.titulo = titulo
        self.hora_extra = hora_extra
        
    def calcular_sal_bruto(self):
        sal_base = self.nm_aulas_semanais * 4.5 * self.vlr_hr_aula
        if self.titulo == 'mestre':
            sal_base += sal_base * 0.085
        elif self.titulo == 'doutor':
            sal_base += sal_base * 0.12
        
        if self.hora_extra == "sim":
            sal_base += sal_base * 0.05
            
        sal_base += sal_base * 1/6
        
        return sal_base
        
        