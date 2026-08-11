'''Escreva um programa em Python que calcule a quantidade de litros de combustível
gasta em uma viagem, utilizando um automóvel que faz 10,5 km/l (quilômetros por
litro). Para realizar o cálculo, o usuário deve fornecer o tempo gasto e a velocidade
média. Seu programa deverá imprimir a quantidade de litros com quatro casas
decimais'''

# Entrada da dados
tempo = float(input("Digite o tempo gasto na viagem em minutos: "))
velocidade = float(input("Digite a velocidade média do veículo: "))

# Processamento
gasto = 10.5
tempo1 = tempo/60
trajeto = tempo1 * velocidade
combustivel = trajeto * gasto

# Saida de dados
print(f"A quantidade de litros de combustível gasta para a viagem é de {combustivel:.4f}")