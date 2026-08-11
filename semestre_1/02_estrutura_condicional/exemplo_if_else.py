#programa para ler as duas notas de um aluno

#calcular e imprimir a média
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2
print(f"Sua média é {media:.2f}")

#Adicionar a situação
if media >= 7:
    print('Situação: Aprovado')
else: 
    print('Situação: Reprovado')