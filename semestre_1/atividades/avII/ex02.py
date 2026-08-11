a = int(input("Insira um valor inteiro de quatro dígitos: "))
b = int(input("Insira um segundo valor inteiro de quatro dígitos: "))
raro = 0
par = 0
impar = 0

while a < 1000 or a > 9999 or b < 1000 or b > 9999:
    print("Ambos os valores devem conter quatro dígitos")
    a = int(input("Insira um valor inteiro de quatro dígitos: "))
    b = int(input("Insira um segundo valor inteiro de quatro dígitos: "))
    
    if b < a:
        aux = a
        a = b
        b = a

for i in range (a, b+1):
    uni = i % 10
    dez =  i // 10 % 10
    cent = i // 100 % 10
    mil = i // 1000 % 10
    som1 = uni + dez
    som2 = cent + mil
    if som1 == som2:
        raro += 1
        if i % 2 == 0:
            par += 1
        else:
            impar +=1

print(f"há {raro} números raros entre {a} e {b}")
print(f"{par} números são pares e {impar} números são ímpares")
