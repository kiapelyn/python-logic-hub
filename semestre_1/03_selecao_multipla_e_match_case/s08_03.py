'''Elabore um programa em Python (utilize a estrutura if-elif-else) que, dada a idade de um
nadador, classifique-o em uma das seguintes categorias:'''

idade = int(input("Digite a idade do nadador:"))

if idade < 5:
    print("Idade inválida")
elif idade <= 7:
    print("Categoria Infantil A")
elif idade <= 10:
    print("Categoria Infantil B")
elif idade <= 13:
    print("Categoria Juvenil A")
elif idade <= 17:
    print ("Categoria Juvenil B")
else:
    print("Categoria Adulto")