'''Construa um programa em Python que leia três valores inteiros. Caso os três valores
informados sejam diferentes entre si, imprima no vídeo o menor valor. Se os valores não
forem diferentes apresente uma mensagem informando o usuário.'''

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a == b or b == c or a == c:
    print("Os valores devem ser diferentes.")
else:
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
        print(b)
    else:
        print(c)

        