class No:
    def __init__(self, dado):
        self.dado = dado
        self.dir = None
        self.esq = None
        
class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    def inserirInicio(self, dado):
        novo = No(dado)
        
        if self.tamanho == 0:
            self.fim = novo
            
        else:
            novo.dir = self.inicio
            self.inicio.esq = novo
            
        self.inicio = novo
        self.tamanho += 1
            
    def inserirFim(self, dado):
        novo = No(dado)
        
        if self.tamanho == 0:
            self.inicio = novo
            
        else:
            self.fim.dir = novo
            novo.esq = self.fim
            
        self.fim = novo
        self.tamanho += 1
        
    def imprimir(self):
        aux = self.inicio
        while aux:
            print(aux.dado, end=' ')
            aux = aux.dir
        print()
            
    def pesquisar(self, dado):
        aux = self.inicio

        for _ in range(self.tamanho):
            if aux.dado == dado:
                return aux
            aux = aux.dir
            
    def remover(self, dado):
        aux = self.pesquisar(dado)
        
        if aux is not None:
            if self.tamanho == 1:
                self.inicio = None
                self.fim = None
            
            elif aux == self.inicio:
                aux.dir.esq = None
                self.inicio = aux.dir
                aux.dir = None
            
            elif aux == self.fim:
                aux.esq.dir = None
                self.fim = aux.esq
                aux.esq = None
            
            else:
                aux.esq.dir = aux.dir
                aux.dir.esq = aux.esq
                aux.esq = None
                aux.dir = None
            
        aux = None
        self.tamanho -= 1