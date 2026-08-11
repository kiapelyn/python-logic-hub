'''def somar():
    c = a + b
    print(c)''' #jeito 1
    
def somar(x,y):
    c = x + y
    return c #jeito 2
    
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))

c = somar(a,b)
print(f"a soma de {a} e {b} é {c}")

