from ponto import Ponto

class Retangulo:
    # Método construtor
    def __init__(self, largura: int , altura: int, canto_superior_esquerdo: Ponto):
        self.largura = largura
        self.altura = altura
        self.canto_superior_esquerdo = canto_superior_esquerdo
    
    # Método para calcular e retornar a área do retângulo
    def calcular_area(self) -> float:
        return self.largura * self.altura
    
    # Método para calcular e retornar o perímetro do retângulo
    def calcular_perimetro(self):
        return (self.largura * 2) + (self.altura * 2)
    
    # Método para aumentar o tamanho do retângulo
    def aumentar_tamanho(self, aumento_largura: int = 0, aumento_altura: int = 0):
        self.largura += aumento_largura
        self.altura += aumento_altura
        return f"Largura: {self.largura}, Altura: {self.altura}"
    
    # Método para calcular e retornar a coordenada do centro de um retângulo
    def calcular_centro(self):
        centro_x = (self.canto_superior_esquerdo.x + self.largura) / 2
        centro_y = (self.canto_superior_esquerdo.y - self.altura / 2) 
        return (centro_x,centro_y)
    
    def __str__(self):
        return f"Largura: {self.largura}, Altura: {self.altura}"