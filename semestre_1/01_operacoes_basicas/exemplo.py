'''Programa para ler as duas notas de um aluno
Em seguida, calcule e imprime o valor da média'''

# Entrada de dados
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

# Processamento dos dados
media = (nota1 + nota2)/2

# Saida de dados
print(f"Sua média é: {media:.1f}")
