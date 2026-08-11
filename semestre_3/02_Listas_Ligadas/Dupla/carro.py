class Carro:
    def __init__(self, marca: str, modelo: str, valor: float):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        
    def __str__(self):
        return f"marca: {self.marca} | mdoelo: {self.modelo} | valor: {self.valor}\n"