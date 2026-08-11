'''Um comerciante comprou um produto e quer vendê-lo com um determinado lucro. A
regra que o comerciante aplica é a seguinte: quando o valor de compra do produto é
inferior a R$ 20,00 o lucro é de 45%. Se o valor de compra do produto é maior que R$
20,00, mas menor do que R$ 100,00 o lucro é de 30%. Caso contrário o lucro é de 20%.
Escreva um programa em Python que leia o produto e o valor de compra de um produto, e
calcule e imprima no vídeo o seu valor de venda obedecendo a regra especificada acima.'''

valor = float(input("Digite o valor do produto"))

if valor < 0:
    print("Valor inválido")
elif valor 