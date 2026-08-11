a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))
c = int(input("Insira o terceiro valor: "))

if a > b:
    aux = a
    a = b
    b = aux
if a > c:
    aux = a
    a = c
    c = aux
if b > c:
    aux = b
    b = c
    c = aux
    
diferença = c - a
print(f"A diferença é {diferença}")