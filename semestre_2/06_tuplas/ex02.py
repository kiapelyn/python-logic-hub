'''
    Implemente uma função em Python para comparar as notas de alguns alunos
    na primeira prova e na segunda prova aplicada por um professor. A função deve
    receber como parâmetro duas listas de tuplas, onde cada tupla contém o nome
    de um aluno e sua nota em uma prova. A função deve exibir os seguintes
    resultados:
    a) Alunos que melhoraram suas notas da primeira prova para a segunda.
    b) Alunos que pioraram suas notas.
    c) Alunos que mantiveram a mesma nota.

'''

from random import randint

qnt = int(input('quantidade de alunos: '))
P1 = []
P2 = []

def atribuir_notas(qnt):
    for i in range(qnt):
        nome = input('nome: ')
        nota1 = (nome, float(randint(0,10)))
        nota2 = (nome, float(randint(0,10)))
        P1.append(nota1)
        P2.append(nota2)
    return P1, P2

def comparar_notas(P1, P2):
    for (nome, nota1), (nome, nota2) in zip(P1, P2):
        if nota2 > nota1:
            situacao = "melhorou"
        elif nota2 < nota1:
            situacao = "piorou"
        else:
            situacao = "manteve a nota"
        print(f"{nome}: {nota1} --> {nota2} = {situacao}")
    
def main():
    P1, P2 = atribuir_notas(qnt)
    comparar_notas(P1, P2)
    
if __name__ == "__main__":
    main()