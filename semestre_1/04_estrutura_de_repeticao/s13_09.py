'''Escreva um programa em Python que calcule e imprima no vídeo o valor total das
compras de um cliente. O valor total deverá ser calculado a partir da soma do preço de
cada produto. Em seguida o usuário deverá escolher a forma de pagamento:
À vista com 10% de desconto;
Em duas vezes com um acréscimo de 15.5%'''

num = int(input("Quantos itens estão sendo comprados? "))
valor = 0
forma = int(input("Para pagamento a vista, digite 1. Para parcelar em duas vezes, digite 2: "))

for item in range(num):
    preco = float(input("Valor do produto: "))
    valor = valor + preco

if forma == 1:
    total = valor - (valor * 0.1)
    print(f"Valor bruto: R${valor:.2f}")
    print(f"Total final: R${total:.2f}")
elif forma == 2:
    total = valor + (valor * 0.155)
    parcela = total / 2
    print(f"Valor bruto: R${valor:.2f}")
    print(f"Total total: R${total:.2f}")
    print(f"Duas parcelas de: R${parcela:.2f}")
else:
    print("Insira um método de pagamento válido")