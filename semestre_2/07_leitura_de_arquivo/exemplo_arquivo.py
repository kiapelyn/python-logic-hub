
#bloco de leitura de arquivo
countap = 0
countrep = 0
aprovado = []
reprovado = []
mediaap = []
mediarep = []

with open('alunos.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        nome, nota1, nota2 = linha.split(';')
        print(f'{nome} teve notas {nota1} e {nota2}')
        notafinal = (float(nota1)+float(nota2))/2
        if notafinal >= 6.75:
            countap += 1
            aprovado.append(nome)
            mediaap.append(notafinal)
        else:
            countrep +=1
            reprovado.append(nome)
            mediarep.append(notafinal)
            
    print()
            
    print(f'{countap} aluno(s) aprovado(s):')
    for nome, media in zip(aprovado, mediaap):
        print(f" - {nome} -> {media:.1f}")
    
    print()
        
    print(f'{countrep} aluno(s) reprovado(s):')
    for nome, media in zip(reprovado, mediarep):
        print(f" - {nome} -> {media:.1f}")