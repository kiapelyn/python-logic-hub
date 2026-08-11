# método recursivo que leia dois valores inteiros m e n e calcule a multiplicação 
# (sem utilizar o operador *) entre eles.

def somar(n: int, m: int) -> int:
    if n == 0: return 0
    elif n < 0:
        return -somar(m, -n)
    return m + somar(m, n - 1)

def main():
    m = int(input("Valor m ---> "))
    n = int(input("Valor n ---> "))
    print(somar(n, m))

if __name__=="__main__":
    main()