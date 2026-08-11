#Inverter o valor de A e B

A = int(input("Insira o valor de A: "))
B = int(input("Insira o valor de B: "))

A, B = B, A

print(f" Após a troca, A = {A} e B = {B}")