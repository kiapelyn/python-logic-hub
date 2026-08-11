def func(n):
    if n == 1: return 1
    return (n-1) * func(n-1)

print(func(5))