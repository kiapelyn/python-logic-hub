def funcao(n):
    if n < 2: return n
    return funcao(n-1) + funcao(n-2)

print(funcao(6))

#fibonacci
