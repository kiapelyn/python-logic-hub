''' Escreva um programa que calcule e imprima no vídeo: a área de um retângulo e o
seu perímetro. Lembrando que a área é calculada multiplicando-se o valor da base
pelo valor da altura. O perímetro é a soma de todos os lados. Exibir os valores no
vídeo com apenas duas casas decimais. '''

# entrada de dados
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

#processamento
area = base * altura
perimetro = (base * 2) + (altura * 2)

#saida de dados
print(f"a área é {area} e o perímetro é {perimetro}")