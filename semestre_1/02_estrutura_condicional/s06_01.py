'''Um hotel cobra R$ 300,00 a diária e mais uma taxa de serviços. A taxa de serviços é de:
R$ 22,50 por diária, se o número de diárias for maior que 15.
R$ 56,00 por diária, se o número de diárias for igual a 15.
R$ 88,00 por diária, se o número de diárias for menor que 15.
Construa um programa em Python que calcule e imprima o valor da conta de um cliente.'''

D = int(input("Quantos dias durará a hospedagem? "))

'''if D > 15:
    print(f"O valor será R${(300*D) + (22.50*D):.2f}")
elif D == 15:
    print(f"O valor será R${(300*D) + (56.00*D):.2f}")
else:
    print(f"O valor será R${(300*D) + (88.00*D):.2f}")'''
    
if D > 15:
    T = 22.50
elif D == 15:
    T = 56.00
else:
    T = 88.00
    
R = 300*D + T*D

print(f"O valor será R${R:.2f}")