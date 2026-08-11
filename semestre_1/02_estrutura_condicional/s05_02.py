'''O professor da disciplina de programação aplicou durante o semestre duas provas e
dois trabalhos. A média final será composta por 70% da média das provas e 30% da
média dos trabalhos. Escreva um programa em Python que calcule e imprima no vídeo
a média final de um aluno e também a sua situação (aprovado ou reprovado) levando
em consideração que para aprovação a média deverá ser maior ou igual a 7.'''

p1 = float(input("Insira a nota da primeira prova: "))
p2 = float(input("Insira a nota da segunda prova: "))
t1 = float(input("Insira a nota do primeiro trabalho: "))
t2 = float(input("Insira a nota do segundo trabalho: "))

pf = (p1 + p2)/2
tf = (t1 + t2)/2
media = (pf * 0.7) + (tf * 0.3)

print(f"A média final é {media:.2f}")

if media >= 7:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")
