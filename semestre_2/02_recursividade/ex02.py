# método recursivo que calcule a soma dos dígitos de um número inteiro informado via teclado.

def somar(n: int) -> int:
    if n == 0: return 0
    else:
        return n % 10 + somar(n//10)

def main():
    if n < 10:
        print("O valor deve ser maior que 10")
    else:
        print(somar(n))
    
n = int(input("Digite um valor inteiro positivo com maior que 10:"))
if __name__=='__main__':
    main()