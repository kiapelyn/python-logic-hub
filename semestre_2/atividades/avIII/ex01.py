from ex01classes import Tutor
from ex01classes import Pet
from ex01classes import Consulta

tutores = []
pets = []
consultas = []

def receber_dados(qnt):
    for i in range(qnt):
        nometutor = input('Nome do tutor: ')
        nomepet = input('Nome do pet: ')
        raca = input('Raça do pet: ')
        valor = float(input('Valor da consulta: '))
        tutores.append(Tutor(nometutor))
        pets.append(Pet(nomepet, raca))
        consultas.append(Consulta(nometutor, nomepet, valor))
    return tutores, pets, consultas
        
def imprimir_registros(consultas):
    print(f'{'Nome do Tutor':<20}{'Nome do Pet':<20}{'Valor'}')
    print('-'*50)
    for agendamento in consultas:
        print(f'{agendamento.tutor:<20}{agendamento.pet:<20}{agendamento.valor}')
    
def imprimir_receita(consultas):
    print(f'{'Receita total:'}')
    print('-'*20)
    receita = 0.0
    for i in consultas:
        receita += i.valor
    print(f'R${receita:.2f}')
    
def calcular_devido(consultas, tutor):
    print(f'{'Nome do Tutor':<20}{'Valor Devido'}')
    print('-'*35)
    valor = 0.0
    for i in consultas:
        if i.tutor == tutor:
            valor += i.valor
    print(f'{tutor:<20}{valor:.2f}')
        
def main():
    qnt = int(input('Quantidade de registros: '))
    tutores, pets, consultas = receber_dados(qnt)
    imprimir_registros(consultas)
    print()
    imprimir_receita(consultas)
    print()
    tutor = input('Tutor a ser analizado: ')
    calcular_devido(consultas, tutor)
        
if __name__ == '__main__':
    main()
