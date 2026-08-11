#função para calcular o valor do delta
def delta(b, a, c):
    d = (b**2)-(4*a*c)
    return d

#funcção para calcular e retornar as raízes de uma equação do 2º grau
def raiz(b, d, a):
    rI = ((-b) - (d**(1/2)))/(2*a)
    rII = ((-b) + (d**(1/2)))/(2*a)
    return rI, rII