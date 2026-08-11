'''Implementar um algoritmo em python para calcular o cos(x). O valor de x deverá ser digitado
pelo usuário da aplicação em graus. O valor do cosseno de x será calculado pela soma dos 15
primeiros termos da série a seguir.'''

x = int(input("Valor de x (em graus): "))
cos = 0
n = 1


for i in range(15):
    if n == 1:
        n +=1
        cos += 1
    if n % 2 == 0:
        cont = 1
        total = 1
        while cont <= n:
            total = total * cont
            cont = cont + 1
        s = (x**n)/total
        if i % 2 != 0:
            cos = cos - s
        elif i % 2 == 0:
            cos = cos + s
        
print(cos)
