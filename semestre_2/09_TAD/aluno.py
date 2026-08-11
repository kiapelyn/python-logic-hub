class Aluno:
    #construtor
    def __init__(self, nome = 'xaolin matador de porco', ra = 0, nota1 = 0, nota2 = 0):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        
    def calcular_media(self):
        return (self.nota1+self.nota2)/2
    
    def avaliar_situacao(self):
        if self.calcular_media() >= 7.0:
            return 'Aprovado'
        return 'Reprovado'
    
        