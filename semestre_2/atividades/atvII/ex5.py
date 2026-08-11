def qtde_presenca(presencas):
    p = {}
    f = {}
    for nome in presencas:
        p[nome] = 0
        f[nome] = 0
    for nome, anotacoes in presencas.items():
        for anotacao in anotacoes:
            if anotacao == "P":
                p[nome] += 1
            else:
                f[nome] += 1
    return p, f
        
def percentual_presencas(p,aulas):
    percentual = {}
    for nome, presenca in p.items():
        calculo = (presenca / len(aulas)) * 100
        
        if nome not in percentual:
            percentual[nome] = calculo
    return percentual 
                   
def registro_aprovacao(p, f, percentual):
    por_aluno = {} 
    for nome in p:
        pres = p[nome]
        falt = f[nome]
        perc = percentual.get(nome)
        if perc >= 75:
            situ = "APROVADO"
        else:
            situ = "REPROVADO"
            
        por_aluno[nome]  = {"P": pres, "F": falt, "perc": perc, "situacao": situ}
    return por_aluno

def aula_falta(aulas, presencas):
    registro = {}
    for aula in aulas:
        registro[aula] = 0

    for i in range(len(aulas)):
        aula = aulas[i]
        for presenca in presencas.values():
            if presenca[i] == "F":
                registro[aula] += 1
    maior = 0
    maior_nome = ''
    for aula,qtde in registro.items():
        if qtde > maior:
            maior = qtde
            maior_nome = aula
            
    return maior_nome

def presenca_aluno(p, f):
    maior_presenca_qtde = -1  
    mais_p = ""              
    for aluno, qtde in p.items():
        if qtde > maior_presenca_qtde:
            maior_presenca_qtde = qtde
            mais_p = aluno
    
    maior_falta_qtde = -1 
    mais_f = ""           
    for aluno, qtde in f.items():
        if qtde > maior_falta_qtde:
            maior_falta_qtde = qtde
            mais_f = aluno
            
    return mais_p, mais_f

def media(aulas, p):
    soma = 0
    geral = 0
    for presenca in p.values():
        soma += presenca 
        geral += presenca * len(aulas)
    total = (soma/geral) * 100
    return total

def media(aulas, p):
    total_presencas_turma = sum(p.values())
    total_aulas = len(aulas)
    num_alunos = len(p)
    
    total_aulas_turma = total_aulas * num_alunos 
    
    if total_aulas_turma > 0:
        media_perc = (total_presencas_turma / total_aulas_turma) * 100
        return media_perc
    else:
        return 0.0

def main():
    aulas = ["A1", "A2", "A3", "A4", "A5"]
    presencas = {
        "Ana": ["P", "P", "F", "P", "P"],
        "Bruno": ["P", "F", "F", "P", "F"],
        "Carla": ["P", "P", "P", "P", "P"],
        "Diego": ["F", "F", "P", "F", "P"]
    }
    p, f = qtde_presenca(presencas)
    
    percentual = percentual_presencas(p, aulas)
    
    por_aluno = registro_aprovacao(p, f, percentual)
    
    aula_mais_faltas = aula_falta(aulas, presencas)

    mais_p,  mais_f = presenca_aluno(p,f)
    
    total_media = media(aulas, p)
    
    relatorio = {
        "por_aluno": por_aluno,
        "aula_mais_faltas": aula_mais_faltas,
        "melhor_presenca": mais_p,
        "mais_faltas": mais_f,
        "presenca_media_turma": total_media
        }
    
    print(relatorio)
    
if __name__ == '__main__':
    main()