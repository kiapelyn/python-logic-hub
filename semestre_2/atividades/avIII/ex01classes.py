class Tutor:
    nome: str
    
    def __init__(self, nome=''):
        self.nome = nome
        
class Pet:
    nome: str
    raca: str
    
    def __init__(self, nome='', raca=''):
        self.nome = nome
        self.raca = raca
        
class Consulta:
    tutor: Tutor
    pet: Pet
    valor: float
    
    def __init__(self, tutor, pet, valor=0.0):
        self.tutor = tutor
        self.pet = pet
        self.valor = valor
    
        