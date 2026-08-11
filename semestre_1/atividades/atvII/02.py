'''Os fatores primos de 13195 são 5, 7, 13 e 29, sendo 29 o maior fator primo de 13195. Escreva
um programa em Python que leia um valor inteiro e imprima o seu maior fator primo.'''

valor = int(input("Digite o valor: "))
maior = 0
total = 0
r = 0

for i in range(1, valor + 1):
        for j in range(1, i +1):
            if i % j == 0:
                total += 1
            if total == 2:
                if r < i:
                    r = r * i
            
print(r)