'''Escreva um programa em Python que leia o código de um determinado produto e mostre
a sua classificação. Utilize a seguinte tabela como referência. observação: na resolução 
desse exercício deve ser utilizada a estrutura if-elif-else'''

codigo = int(input("Insira o código do produto:"))

if codigo == 1:
    print("Alimento não perecível")
elif codigo >= 2 and codigo <= 4:
    print("Alimento perecível")
elif codigo >= 5 and codigo <= 6:
    print("Vestuário")
elif codigo == 7:
    print("Higiene Pessoal")
elif codigo >= 8 and codigo <= 15:
    print("Limpeza e utensílios domésticos")
else:
    print("Código inválido")
    