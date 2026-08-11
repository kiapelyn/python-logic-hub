def ordenar(l) -> list:
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            aux = l[i + 1]
            l[i + 1] = l[i]
            l[i] = aux

    return l

def verificar(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            existe = 1
            break
        else:
            existe = None
    
    return existe

def main():
    l = []
    n = int(input("Informe: "))

    for i in range(n):
        l.append(int(input("informe: ")))
    
    r = ordenar(l)
    existe = verificar(l)

    if existe is not None:
        ordenar(l)
        verificar(l)

    if existe is None:
        print('lista depois do trem')
        print(r)

if __name__ == '__main__':
    main()