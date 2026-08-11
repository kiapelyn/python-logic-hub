def misterio(v,n):
    if n == 1: return v[0]
    if n == 2:
        if v[0] < v[1]:
            return v[1]
        else:
            return v[0]
    x = misterio(v, n-1)
    if x < v[n-1]:
        return v[n-1]
    return x

v = [5, 3, 2, 11, 9, 10]
n = 6

print(misterio(v, n))