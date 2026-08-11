#sintaxe de dicionário

aluno1 = {
    'nome': 'Vulpes', 'RA': 16, 'curso': 'CDN'
}

aluno2 = {
    'nome': 'Chaos', 'RA': 17, 'curso': 'Direito'
}

aluno3 = {
    'nome': 'Fox', 'RA': 19, 'curso': 'Design'
}

aluno4 = {
    'nome': 'Moony', 'RA': 13, 'curso': 'Medicina'
}

print(aluno1['nome'])




#não é comum, mas existe a função

aluno5 = dict(nome='Lil', RA=23, curso='Letras')




#uma lista de dicionários

alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]

print(alunos[0]['curso'])