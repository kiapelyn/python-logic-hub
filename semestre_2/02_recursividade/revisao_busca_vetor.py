def muitofeio(x, v, n):
    if n == 0: return 0
    feio = muitofeio(x, v, n-1)
    if feio == 1 or x == v[n-2]: return 1
    
x = 9
v = [5,3,2,11,9,10]
n = 6
    
print(muitofeio(x,v,n))
    