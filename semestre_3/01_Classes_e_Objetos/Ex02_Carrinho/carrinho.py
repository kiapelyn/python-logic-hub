from itens import Itens

class Carrinho:
    def __init__(self):
        self.itens = []
        
    def adicionar_item(self, nome:str, preco: float, qnt: int):
        self.itens.append({nome: Itens(nome, preco, qnt)})

    
    def remover_item(nome):
        pass
    
    def atualizar_quantidade(self, nome, quantidade, carrinho):
        #if self.nome in carrinho:
            #carrinho.value(self.qnt) += self.qnt
        pass
    
    def total(self):
        soma = 0
        for i in self.itens.values():
            soma += i.preco * i.qnt
        return soma
    
    def __str__(self):
        return f"Nome = {self.nome}\nPreco = R${self.preco:.2f}\nQuantidade = {self.qnt}"
    