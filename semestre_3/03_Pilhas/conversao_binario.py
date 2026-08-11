from collections import deque

numero = int(input("Insira o número: "))
pilha = deque()
resultado = ''

while numero > 0:
    resto = numero % 2
    numero //= 2
    pilha.append(resto)
    
while pilha:
    resultado += str(pilha.pop())
    
print(resultado)