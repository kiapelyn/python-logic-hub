'''Uma plataforma de streaming utiliza um sistema de recomendação que mantém uma
sequência de conteúdos sugeridos para cada usuário. Essa sequência é armazenada em
uma lista duplamente encadeada, onde cada elemento representa um conteúdo
recomendado.

Com o objetivo de variar as sugestões apresentadas ao usuário, o sistema
periodicamente realiza uma rotação na lista de recomendações. Essa rotação consiste
em deslocar os primeiros elementos da lista para o final da estrutura, preservando a
ordem relativa dos demais elementos.

Por exemplo, considere a seguinte lista de recomendações: 10 20 30 40 50. Se o sistema
aplicar uma rotação de k = 2 posições, os dois primeiros elementos devem ser movidos
para o final da lista, resultando em: 30 40 50 10 20.
'''

from lista_dupla import ListaDupla

lista = ListaDupla()
lista.inserirFim(10)
lista.inserirFim(20)
lista.inserirFim(30)
lista.inserirFim(40)
lista.inserirFim(50)
lista.inserirFim(60)



def rotacionar(rot):
    if lista.tamanho > 0 and lista.tamanho != rot and rot != 0:
        for i in range(rot):
            lista.inserirFim(lista.inicio.dado)
            lista.remover(lista.inicio.dado)
        lista.imprimir()
    else:
        print("0 deslocamentos")
        return
        
def main():
    lista.imprimir()
    rot = int(input("Quantas posições serão rotacionadas? ")) % lista.tamanho
    rotacionar(rot)
   
if __name__ == "__main__":
    main()

