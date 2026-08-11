from lista_dupla import No
from lista_dupla import ListaDupla

lista = ListaDupla()

lista.inserirInicio(10)
lista.inserirInicio(20)
lista.inserirInicio(30)

lista.inserirFim(40)
lista.inserirFim(50)

lista.imprimir()

lista.remover(40)
lista.imprimir()

lista.remover(30)
lista.imprimir()

lista.remover(50)
lista.imprimir()

lista.remover(20)
lista.imprimir()

lista.remover(10)
lista.imprimir()