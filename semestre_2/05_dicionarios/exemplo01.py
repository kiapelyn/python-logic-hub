'''
    Programa exemplo para ler o RA, o nome e a nota dos alunos matriculados na disciplina 
    Felicidade. Em seguida, imprimir a quantidade de alunos com média (maior ou igual a 7).
'''

lista = []

for i in range(5):
    RA = int(input('RA: '))
    nome = input('Nome: ')
    nota = float(input('Nota: '))
    lista.append({'RA':RA, 'nome':nome, 'nota':nota})
    print()

print(lista)

#tem dois jeitos de fazer

total = 0
for i in range(len(lista)):
    aluno = lista[i]
    if aluno['nota'] >= 7.0:
        total += 1
print(total)

total = 0
for aluno in lista:
    if aluno.get('nota') >= 7.0: 
        total += 1
print(total)

# e a média dos alunos

media = 0
for aluno in lista:
    media += aluno.get('nota')
media /= len(lista)
print(f'{media:.2f}')