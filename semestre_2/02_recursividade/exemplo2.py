# programa com função recursiva para ler um valor inteiro e positivo e retorne o
# valor de fibonacci na posição indicada

def fib(x: int) -> int:
    if x == 1 or x == 2: return 1
    else:
        return fib(x-1) + fib(x-2)

def main():
    x = int(input("Digite um valor inteiro e positivo: "))
    if x <= 0:
        print("O valor deve ser inteiro e positivo")
    else:
        print(f"a posição {x} corresponde ao valor {fib(x)}")

y = 1
if __name__ == '__main__':
    main()