'''Elaborar um programa em Python para calcular o valor do salário líquido mensal de
um professor do ensino fundamental. Para o cálculo do salário mensal do professor
são necessários os seguintes dados: valor da hora-aula, número de horas
trabalhadas no mês e a porcentagem de desconto do INSS. O cálculo do salário leva
em consideração os seguintes passos:
a) calcula-se o valor do salário bruto (valor da hora-aula multiplicada pelo número
de horas trabalhadas).
b) A partir do salário bruto, calcula-se o valor que será descontado referente ao
INSS.
c) Calcula-se o salário líquido mensal (valor do salário bruto menos o valor do
desconto do INSS.
d) Exibir o valor do salário líquido com apenas duas casas decimais.
'''

#Entrada de dados
horaaula = float(input("Digite o valor da hora-aula:"))
horastrab = float(input("Digite o número de horas trabalhadas no mês:"))
INSS = float(input("Digite a porcentagem do desconto do INSS (digite penas o número): "))

#Processamento
bruto = horaaula * horastrab
desconto = (INSS/100) * bruto
liquido = bruto - desconto

#Saida
print(f"O salário líquido será de R${liquido:.2f}")