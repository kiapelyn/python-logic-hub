PA = int(input("Habitantes de A:"))
TA = float(input("Taxa de crescimento de A: "))
PB = int(input("Habitantes de B:"))
TB = float(input("Taxa de crescimento de B: "))
ano = 0

if PA <= 0 or PB <= 0:
    print("a população deve ser maior que 0")
else:
    while PA < PB:
        PA += (PA * TA)
        PB += (PB * TB)
        ano += 1

print(f"Levará {ano} anos para que a população de A seja maior que a de B")