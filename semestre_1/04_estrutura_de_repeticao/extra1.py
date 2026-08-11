'''O seu programa deverá ler pelo terminal um valor na base binária.
O seu programa deverá converter o valor lido para a base decimal.'''

bin = int(input("Digite um valor na base binária: "))
decimal = 0
i = 0

while bin > 0:
  digito = bin % 10
  decimal = decimal + digito * (2**i)
  i = i + 1
  bin = bin// 10

print(f"O valor {bin} na base decimal é {decimal}")
    
