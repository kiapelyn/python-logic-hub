altura = float(input("Insira a altura do reservatório em metros:"))
raio = float(input("Insira o raio do reservatório em metros:"))
custo = float(input("Insira o custo de cada unidade do material de isolamento:"))

from math import ceil

pi = 3.1415
area = (2*pi*raio*altura + 2*pi*(raio**2))
tamanho = 3
perda = tamanho*0.05
unid = tamanho - perda
unidades = ceil(area / unid)
valor = unidades * custo

print(f"A área total é de {area:.2f}m²")
print(f"Serão necessárias {unidades} para fazer o isolamento")
print(f"O custo total será de R${valor:.2f}")