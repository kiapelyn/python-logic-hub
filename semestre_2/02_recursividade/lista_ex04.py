# método recursivo que receba como parâmetro um valor inteiro não nulo. 
# A função recursiva deverá retornar true caso o valor seja primo ou false caso contrário.

a = int(input())
b = 0

def binario(a, b):
    if a == 0: return 0
    if a % 2 == 1:
        b += 1
        b = b*10
        return binario(a/2, b)
    if a % 2 == 0:
        b += 0
        b = b*10
        return binario(a/2, b)

print(binario(a,b))


