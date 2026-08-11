from professor import Professor

qnt = int(input('Quantidade de professores: '))
print()
lista = []
for _ in range(qnt):
    nome = input('Nome --> ')
    nm_aulas_semanais = int(input('Números de Aulas Semanais --> '))
    vlr_hr_aula = float(input('Valor Hora-Aula --> '))
    titulo = input('Título (mestre, doutor, nenhum) --> ')
    hora_extra = input("Fez hora extra? --> ")

    lista.append(Professor(nome, nm_aulas_semanais, vlr_hr_aula, titulo, hora_extra)) 
    
    print('-' * 30)
    
print(f'{'Nome':<20}{'Salário Bruto'}') 
print('-' * 40)

for professor in lista:
    salario_bruto = professor.calcular_sal_bruto()
    print(f'{professor.nome:<20}R${salario_bruto:.2f}')