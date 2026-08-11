''' A delegacia de polícia da pequena cidade de Springfield conta com somente 3 policiais: o chefe
de polícia Clancy, e os policiais Eddie e Lou. Como é de se esperar, esse pequeno contingente de
policiais não consegue atender imediatamente a todos os chamados policiais. Portanto, você foi
contratado para criar um sistema de atendimento (um programa escrito em linguagem de
programação python), de maneira que cada um dos policiais fique com um conjunto equilibrado
de chamados.

A cada registro de ocorrência o sistema deve imprimir um resumo da quantidade de ocorrências
de cada policial, o número de ocorrências do tipo Homer e o percentual de ocorrências do tipo
“Direção Perigosa” em relação do total de ocorrências cadastradas.'''

nova = input('Deseja inserir uma nova ocorrências? (Sim/Não):')
Clancy = 0
Eddie = 0
Lou = 0
homer = 0
total = 0
dir = 0

while nova == 'sim':
    oco = input("Qual o tipo de ocorrência? (Direção Perigosa, Barulho, Bebedeira, Homer) ")
    if oco == 'Homer' or oco == 'homer':
        grav = 'Alto'
        resp = 'Clancy'
        Clancy += 1
        homer += 1
    else:
        if oco == 'Direção Perigosa' or oco == 'direção perigosa':
            dir += 1
        grav = input("Qual a gravidade da ocorrência? (Baixo, Médio, Alto) " )
        
        if Clancy < Eddie and Clancy < Lou:
            Clancy += 1
            resp = 'Clancy'
        elif Eddie < Clancy and Eddie < Lou:
            Eddie += 1
            resp = 'Eddie'
        elif Lou < Clancy and Lou < Eddie:
            Lou +=1
            resp = 'Lou'
        elif Clancy == Lou and Lou == Eddie and Clancy == Eddie:
            Eddie += 1
            resp = 'Eddie'
    total += 1
    por = (dir*100)/total
    
    #resumo
    print(f"Ocorrências respondidas por Clancy: {Clancy}")
    print(f"Ocorrências respondidas por Eddie: {Eddie}")
    print(f"Ocorrências respondidas por Lou: {Lou}")
    print(f"Houveram {homer} ocorrências do tipo homer")
    print(f"{por}% das ocorrências são sobre direção perigosa")
    nova = input('Deseja inserir uma nova ocorrências? (Sim/Não):')

if nova == 'não':
    print("Obrigado por usar o sistema de registro de ocorrências de Springfield")