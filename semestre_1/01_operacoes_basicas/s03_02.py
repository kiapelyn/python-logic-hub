'''Escreva um programa que leia uma temperatura em graus Celsius e apresente no
vídeo a sua equivalente em graus Fahrenheit. A fórmula de conversão é:
F = C * (9/5) + 32
onde C é a temperatura em graus Celsius e F a temperatura em graus Fahrenheit.
Exiba a temperatura no vídeo com três casas decimais.
'''

# entrada de dados
celsius = float(input("Digite a temperatura em celsius:"))

# processamento
fahrenheit = celsius * (9/5) + 32

#saida de dados
print(f"A temperatura em Fahrenheit é {fahrenheit:.3f}")