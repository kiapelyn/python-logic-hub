'''Escreva um programa em python que leia um número na base binária e, em seguida, faça a sua
conversão para a base decimal. Antes de fazer a conversão, seu programa deverá validar se o
número informado realmente está na base de numeração binária. Se não estiver, não poderá ser
convertido.'''

binario = int(input("Digite o binário: "))
base = 10
pow = 0
conta = 0
conv = 0

if binario > 11111111:
    print("Número inválido")
else:
    for i in range(8):
        conta = (binario % base)
        conv = conv + (conta*(2**pow))
        binario = binario - conta
        base = base * 10
        pow += 1
            
print(conv)

#TA ERRADOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

'''     um = (binario // 10)*(2**1)
        dois = (binario // 100)*(2**2) + um
        tres = (binario // 1000)*(2**3) + dois
        quatro = (binario // 10000)*(2**4) + tres
        cinco = (binario // 100000)*(2**5) + quatro
        seis = (binario // 1000000)*(2**6) + cinco
        sete = (binario // 10000000)*(2**7) + seis
        oito = (binario // 100000000)*(2**8)+ sete'''