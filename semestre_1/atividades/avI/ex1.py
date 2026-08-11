peso = float(input("Insira o peso em quilos: "))
altura = float(input("Insira a altura em metros: "))

if peso <= 0 or altura <= 0:
    print("Os valores devem ser diferentes de 0")
else:
    IMC = peso/(altura**2)
    if IMC <= 24.9:
        print(f"IMC = {IMC:.2f}; peso normal")
    else:
        print(f"IMC = {IMC:.2f}; sobrepeso")

