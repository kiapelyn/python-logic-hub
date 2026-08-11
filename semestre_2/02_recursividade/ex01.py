# método recursivo que calcule o valor de x n. O valor de n deve ser maior ou igual a 0

def elevado(x: int, n: int) -> int:
    if n == 0: return 1
    return x * elevado(x, n-1)
    
def main():
    if n < 0:
        print("O valor deve ser maior ou igual a 0")
    else:
        x = int(input('Digite o valor da base:'))
        print(elevado(x,n))

n = int(input('Digite o valor do expoente:'))
if __name__=='__main__':
    main()


