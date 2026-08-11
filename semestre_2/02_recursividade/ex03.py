
# método recursivo que calcule o máximo divisor comum (MDC) entre dois valores inteiros usando fórmula dada

def mdc(m: int, n: int) -> int:
    if n > m:
        return mdc(n, m)
    elif n == 0:
        return m
    return mdc(n, m % n)

def main():
    m = int(input("Valor m ---> "))
    n = int(input("Valor n ---> "))
    print(mdc(m,n))

if __name__=="__main__":
    main()