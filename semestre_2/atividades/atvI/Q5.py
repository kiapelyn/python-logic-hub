from typing import Dict, List

def calcularPresencaPessoal(nome: str, pres: Dict[str, List[str]]):
    listaPresencas = pres[nome]

    totalPresencas = listaPresencas.count("P")
    totalFaltas = listaPresencas.count("F")
    percentual = totalPresencas / len(listaPresencas) * 100
    
    return totalPresencas, totalFaltas, percentual


def dictPorAluno(nome: str, pres: Dict[str, List[str]]):
    porAluno = {}

    totalPresencas, totalFaltas, percentual = calcularPresencaPessoal(nome, pres)
    
    situacao = "APROVADO" if percentual >= 75 else "REPROVADO"
    
    porAluno[nome] = {
        "P": totalPresencas,
        "F": totalFaltas,
        "perc": percentual,
        "situacao": situacao
    }

    return porAluno

def estatisticasTurma(aulas: List[str], presencas: Dict[str, List[str]]):
    faltasPorAula = [0] * len(aulas)
    somaPercentuais = 0
    maiorPresenca = ("", -1)
    maisFaltas = ("", -1)

    for aluno in presencas:
        lista = presencas[aluno]
        indice = 0 
        for marca in lista:
            if marca == "F":
                faltasPorAula[indice] += 1
            indice += 1

        totalPresencas = lista.count("P")
        totalFaltas = lista.count("F")
        percentual = totalPresencas / len(lista) * 100
        somaPercentuais += percentual

        if percentual > maiorPresenca[1]:
            maiorPresenca = (aluno, percentual)
        if totalFaltas > maisFaltas[1]:
            maisFaltas = (aluno, totalFaltas)

    aulaMaisFaltas = aulas[faltasPorAula.index(max(faltasPorAula))]

    mediaTurma = somaPercentuais / len(presencas)

    print(f"Aula com mais faltas: {aulaMaisFaltas}")
    print(f"Aluno com maior presença: {maiorPresenca[0]} ({maiorPresenca[1]:.1f}%)")
    print(f"Aluno com mais faltas: {maisFaltas[0]} ({maisFaltas[1]} faltas)")
    print(f"Média de presença da turma: {mediaTurma:.1f}%")

def main():
    aulas = ["A1", "A2", "A3", "A4", "A5"]

    presencas = {
        "Ana": ["P", "P", "F", "P", "P"],
        "Bruno": ["P", "F", "F", "P", "F"],
        "Carla": ["P", "P", "P", "P", "P"],
        "Diego": ["F", "F", "P", "F", "P"]
    }

    print("Dicionário por aluno:")
    for aluno in presencas:
        print(dictPorAluno(aluno, presencas))

    print("\nEstatísticas da turma:")
    estatisticasTurma(aulas, presencas)


if __name__ == "__main__":
    main()
