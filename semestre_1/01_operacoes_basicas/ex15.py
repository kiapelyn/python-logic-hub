#valor da prestação em atraso de um produto

valor = float(input("Insira o valor da prestação em atraso: "))
taxa = float(input("Insira o valor da taxa do atraso: "))
tempo = int(input("Inpira o tempo, em dias, que o valor está atrasado: "))

p = valor + (valor * (taxa/100) * tempo)

print(f"A prestação é de R${p:.2f}")