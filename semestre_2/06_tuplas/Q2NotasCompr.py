def comparar_notas(prova1, prova2):
    """
    prova1 e prova2: listas de tuplas (nome, nota)
    Ex.: [("Ana", 7.0), ("Bruno", 8.5)]
    Compara alunos presentes nas duas listas (mesmo nome).
    """
    # mapa da 1ª prova: nome -> nota
    notas1 = {}
    for nome, nota in prova1:
        notas1[nome] = float(nota)

    melhoraram = []  # (nome, n1, n2)
    pioraram = []    # (nome, n1, n2)
    mantiveram = []  # (nome, n1, n2)

    # percorre a 2ª prova e compara com a 1ª
    for nome, nota2 in prova2:
        n2 = float(nota2)
        if nome in notas1:
            n1 = notas1[nome]
            if n2 > n1:
                melhoraram.append((nome, n1, n2))
            elif n2 < n1:
                pioraram.append((nome, n1, n2))
            else:
                mantiveram.append((nome, n1, n2))
        

    # impressão dos resultados no terminal
    print("Alunos que melhoraram:")
    if not melhoraram:
        print("- (nenhum)")
    else:
        for nome, n1, n2 in melhoraram:
            print(f"- {nome}: {n1} -> {n2}")

    print("\nAlunos que pioraram:")
    if not pioraram:
        print("- (nenhum)")
    else:
        for nome, n1, n2 in pioraram:
            print(f"- {nome}: {n1} -> {n2}")

    print("\nAlunos que mantiveram a mesma nota:")
    if not mantiveram:
        print("- (nenhum)")
    else:
        for nome, n1, n2 in mantiveram:
            print(f"- {nome}: {n1} -> {n2}")


# função principal
def main():
    prova1 = [("Ana", 7.0), ("Bruno", 8.5), ("Carla", 6.0), ("Diego", 9.0)]
    prova2 = [("Ana", 7.5), ("Bruno", 8.5), ("Carla", 5.0), ("Diego", 8.0), ("Eva", 6.0)]

    comparar_notas(prova1, prova2)

# programa principal
if __name__ == "__main__":
    main()