# método recursivo para calcular o fatorial duplo

def fatorial(x: int) -> int:
    #caso base
    if x == 0: return 1
    return x * fatorial(x-1)

def main():
    x = int(input("Digite um valor inteiro e positivo: "))
    if x < 0:
        print("O valor deve ser inteiro e positivo")
    else:
        print(f"{x}! = {fatorial(x)}")

if __name__ == '__main__':
    main()
    
