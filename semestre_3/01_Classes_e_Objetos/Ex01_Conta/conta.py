from random import randint

class Conta:
    def __init__(self, titular: str):
        self.titular = titular
        self.numero = randint(1000, 9999)
        self.saldo = 0.0
        
    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            return self.saldo
        else: return False
    
    def sacar(self, valor: float):
        if valor <= self.saldo:
            self.saldo -= valor
            return self.saldo
        else: return False
            
    
    def transferir(self, valor: float, conta_destino: "Conta"):
        if valor <= self.saldo:
            self.sacar(valor)
            conta_destino.depositar(valor)
            return self.saldo
        else: return False

    
    def __str__(self):
        return f"Titular = {self.titular}\nNúmero = {self.numero}\nSaldo = R${self.saldo:.2f}"