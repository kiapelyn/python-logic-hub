class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        
class ABB:
    def __init__(self):
        self.raiz = None
        
    
    # método para inserir um dado na árvore binária de busca
    def inserir(self, dado):
        self.raiz = self._inserir(self.raiz, dado)
        
    # método recursivo para inserir um dado na árvore
    def _inserir(self, no, dado):
        if no is None:
            return No(dado)
        
        if dado < no.dado:
            no.esq = self._inserir(no.esq, dado)
        elif dado > no.dado:
            no.dir = self._inserir(no.dir, dado)
        
        return no
    
    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado
    
    def _em_ordem(self, no, resultado):
        if no is None:
            return
        
        self._em_ordem(no.esq, resultado)
        resultado.append(no.dado)
        self._em_ordem(no.dir, resultado)
        
    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)
        
    def _remover(self, no, valor):
        if no is None:
            return None
        
        if valor < no.dado:
            no.esq = self._remover(no.esq, valor)
        elif valor > no.dado:
            no.dir = self._remover(no.dir, valor)
        else:
            # caso 1 - sem filhos
            if no.esq is None and no.dir is None:
                return None
            
            # caso 2 - um filho
            if no.esq is None:
                return no.dir
            elif no.dir is None:
                return no.esq
            
            # caso 3 - dois filhos
            sucessor = self.buscar_menor(no.dir)
            no.dado = sucessor.dado
            no.dir = self._remover(no.dir, sucessor.dado)    
        return no
                    
    def buscar_menor(self, no):
        while no.esq is not None:
            no = no.esq
            
        return no
        
        
            
            
if __name__ == "__main__":
    print('*' * 85)
    
    arvore = ABB()
    arvore.inserir(15)
    arvore.inserir(7)
    arvore.inserir(10)
    arvore.inserir(25)
    arvore.inserir(20)
    arvore.inserir(35)
    
    print(arvore.em_ordem())
    
    arvore.remover(20)
    print(arvore.em_ordem())
    
    arvore.remover(7)
    print(arvore.em_ordem())
    
    arvore.remover(15)
    print(arvore.em_ordem())
    
    arvore.remover(25)
    print(arvore.em_ordem())
    
    arvore.remover(35)
    print(arvore.em_ordem())
    
    arvore.remover(10)
    print(arvore.em_ordem())
