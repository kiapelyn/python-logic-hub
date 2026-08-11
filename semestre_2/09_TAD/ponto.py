import math

class Ponto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def calcular_distancia(self, p: 'Ponto') -> float:
        #return (((self.x - p.x)**2) + ((self.x - p.x)**2))**(1/2)
        return math.hypot(self.x - p.x, self.y - p.y)
    
    def distancia_origem(self) -> float:
        #return (self.x**2 + self.y**2)**(1/2)
        return math.hypot(self.x - self.y)
    
    def __str__(self):
        return f'({self.x}, {self.y})'
