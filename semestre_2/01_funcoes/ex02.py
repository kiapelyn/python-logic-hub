def imprimir(n: int) -> None:
    while True:
        print(f"{n:.0f}", end=' ')
        if n == 1:
            break
        if n % 2 == 0:
            n = n//2
        else:
            n = (3*n)+1
            
def main() -> None:
    n = int(input("Digite um valor: "))
    imprimir(n)

if __name__ == "__main__":
    main()