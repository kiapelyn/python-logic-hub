
a = 0
b = 1
soma = 0
while b <= 4000000:
    prox = a + b
    a = b
    b = prox
    if prox % 2 == 0:
        soma += prox

print(soma)