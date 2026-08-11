'''
Uma concessionária de veículos deseja desenvolver um pequeno sistema para organizar
seu estoque de automóveis. Cada veículo possui as seguintes informações: marca,
modelo e valor.

Para armazenar os veículos, a concessionária decidiu utilizar a estrutura de lista
duplamente encadeada implementada em aula. Cada nó da lista deverá armazenar um
objeto da classe Carro

Implemente as seguintes funções usando a lista duplamente encadeada:
1. Listar carros
2. Buscar carros pelo modelo
3. Encontrar o carro mais caro
4. Calcular o valor médio dos carros
'''
from lista_dupla import ListaDupla
from carro import Carro


def registrar():
    lista = ListaDupla()
    n = int(input('Informe a quantidade de carros para registrar: '))
    
    for _ in range(n):
        marca = input('Informe o nome da marca: ')
        modelo = input('Informe o nome do modelo: ')
        valor = float(input('Informe o preço do carro: '))
        
        lista.inserirFim(Carro(marca, modelo, valor))
    return lista

def buscar(lista):
    busca = input("Nome do modelo: ")
    return Carro
    
        
    
    
def main():
    lista = registrar()
    lista.imprimir()
    print(buscar(lista))

if __name__ == '__main__':
    main()

