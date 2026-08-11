from aluno import Aluno

qnt = int(input())
lista = []

def entrar_dados(qnt):
    for _ in range(qnt):
        nome = input('Nome: ')
        ra = int(input('RA: '))
        nota1 = float(input('Nota1: '))
        nota2 = float(input('Nota2: '))
        lista.append(Aluno(nome, ra, nota1, nota2))
    return lista

def imprimir_dados(lista):
    print(f'{'Nome':<20}{'Média':<10}{'Situação'}')
    print('-'*40)
    for estudante in lista:
        print(f'{estudante.nome:<20}{estudante.calcular_media():<10.2f}{estudante.avaliar_situacao()}')
    
def main():
    lista = entrar_dados(qnt)
    print('-'*40)
    imprimir_dados(lista)
    
if __name__ == '__main__':
    main()