
# função para realizar a soma --> (a + bi) + (c + di) = (a + c, b + d)
def somar(c1, c2):
    a, b = c1
    c, d = c2
    real = a + c
    imag = b + d
    return (real, imag)

# função para realizar a multiplicação --> (a + bi)(c + di) = (ac - bd, ad + bc)
def multiplicar(c1, c2):
    a, b = c1
    c, d = c2
    real = (a * c) - (b * d)
    imag = (a * d) + (b * c)
    return (real, imag)

# função para imprimir o número complexo no formato pedido no enunciado do exercício
def exibir_complexo(c):
    a, b = c
    print(f"{a} + {b}i")

# função principal --> sempre chamada a partir do programa principal
def main():
    z1 = (3, 2)   # 3 + 2i
    z2 = (1, 4)   # 1 + 4i

    s = somar(z1, z2)
    m = multiplicar(z1, z2)

    print("Soma:")
    exibir_complexo(s)

    print("Multiplicação:")
    exibir_complexo(m)

# programa principal
if __name__ == "__main__":
    main()
