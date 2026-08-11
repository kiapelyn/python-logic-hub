def eh_primo(n: int) -> bool:
    i = 1
    qnt = 0
    for i in range(n(1**2)+1):
        if n % i == 0:
            qnt = qnt+1
    if qnt == 2:
        return qnt

def gerar_primos(n: int) -> list:
    lista = []
    valor = 2
    while len(lista) < n:
        if eh_primo(valor):
            lista.append(valor)
        valor = valor + 1
    return lista

def imprimir():
    lista = gerar_primos()
    print(lista)
            

def main() -> None:
    n = int(input("Informe a quantidade de números primos: "))
    lista = gerar_primos(n)
    imprimir(lista)

if __name__ == "__main__":
    main()
