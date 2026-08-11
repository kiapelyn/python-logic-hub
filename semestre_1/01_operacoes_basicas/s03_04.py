'''Antes do racionamento de energia ser decretado, quase ninguém falava em
quilowatts, mas agora, todos incorporaram essa palavra em seu vocabulário.
Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo, fazer
um programa em Python que leia o valor do salário mínimo e a quantidade de
quilowatts gasta por uma residência. O programa deverá calcular e imprimir no
vídeo:
 o valor em reais de cada quilowatt;
 o valor em reais a ser pago pela residência;
 o novo valor a ser pago pela residência considerando um desconto de 10%.
'''

# Entrada de dados
salario = float(input("Digite o valor do salário mínimo: "))
gasto = float(input("Digite a quantidade de quilowatts gasta: "))

# Processamento
cadaqw = (salario/7)/100
pagar = cadaqw * gasto
pago = pagar - (pagar*0.10)

# Saida
print(f"O valor de cada quilowatt é de R${cadaqw:.2f}")
print(f"O valor bruto a ser pago é R${pagar:.2f}")
print(f"O valor líquido a ser pago é R${pago:.2f}")