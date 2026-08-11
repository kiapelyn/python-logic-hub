'''Uma empresa de logística mantém duas filas de processamento de pedidos
representadas por listas duplamente encadeadas. A lista A contém pedidos de clientes
premium. A lista B contém pedidos de clientes comuns.

Para garantir prioridade equilibrada, o sistema precisa gerar uma nova lista onde os
pedidos sejam intercalados.

Implemente um método que intercale duas listas e retorne a lista resultante. Por
exemplo: Lista A: 1 3 5 e Lista B: 2 4 6. Resultado esperado: 1 2 3 4 5 6.
'''

from lista_dupla import No
from lista_dupla import ListaDupla

listaA = ListaDupla()
listaB = ListaDupla()


def lerDados(n, n2):
    for i in range(n):
        listaA.inserirFim(int(input(f"Valor {i+1} da lista A: ")))

    for i in range(n2):
        listaB.inserirFim(int(input(f"Valor {i+1} da lista B: ")))
      
    return listaA, listaB

def intercalar(listaA, listaB):
    listaC = ListaDupla()
    pA = listaA.inicio
    pB = listaB.inicio
    while pA is not None and pB is not None:
        listaC.inserirFim(pA.dado)
        listaC.inserirFim(pB.dado)
        pA = pA.dir
        pB = pB.dir

    while pA is not None:
        listaC.inserirFim(pA.dado)
        pA = pA.dir
        
    while pB is not None:
        listaC.inserirFim(pB.dado)
        pB = pB.dir
        
    return listaC

def main():
    n = int(input("Quantos valores terá a lista A?"))
    n2 = int(input("Quantos valores terá a lista B?"))
    
    listaA, listaB = lerDados(n, n2)
    listaC = intercalar(listaA, listaB)
    listaC.imprimir()
    
if __name__ == "__main__":
    main()
    
    
'''
minha versão original:

def intercalar(listaA, listaB, n, n2):
    listaC = ListaDupla()
    minimo = min(n, n2)
    for i in range(minimo):
        if i == 0:
            aux1 = listaA.inicio
            aux2 = listaB.inicio
        else:
            aux1 = aux1.dir
            aux2 = aux2.dir
            
        listaC.inserirFim(aux1.dado)
        listaC.inserirFim(aux2.dado)'''
