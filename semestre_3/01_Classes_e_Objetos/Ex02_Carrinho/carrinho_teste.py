from itens import Itens
from carrinho import Carrinho

carrinho = Carrinho()
carrinho.adicionar_item('Lápis', 5.99, 2)
print(carrinho.total())
    