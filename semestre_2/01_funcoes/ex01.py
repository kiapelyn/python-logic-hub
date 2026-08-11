def contar_graos() -> int:
    total = 0
    for i in range(64):
        total += 2**i
    return total


def calcular():
    a = 0
    resultado = []
    for i in range(64):
        resultado.append(2**i)
    return resultado

'''def somar():
    global resultado
    final = 0
    for i in range(len(resultado)):
        final += resultado[i]
    return final'''


total = contar_graos()
print(f"O total de grãos será de {total}")

resultado = sum(calcular())
print(f"O total de grãos será de {resultado}")

'''final = somar()
print(f"O total de grãos será de {somar}")'''


    