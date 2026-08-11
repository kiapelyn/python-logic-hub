class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        
class ListaSimples:
    def __init__(self):
        self.head = None
    
    def inserirFim(self, dado):
        pass
    
    def inserirHead(self, dado):
        novo = No(dado)
        if self.head is None:
            self.head = novo
        else:
            novo.proximo = self.head
            self.head = novo
            
    def imprimir(self):
        aux = self.head
        while aux:
            if aux.proximo:
                print(aux.dado, end='-> ')
            else: print(aux.dado)
            aux = aux.proximo
            
