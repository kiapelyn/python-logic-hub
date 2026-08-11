def minhafuncao(n):
    if n < 4: return 3*n
    return 2 * minhafuncao(n-4)+5

print(minhafuncao(3))
print(minhafuncao(7))