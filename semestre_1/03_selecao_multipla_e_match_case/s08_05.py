'''Desenvolva um programa em Python que calcule o que deve ser pago por um produto,
considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize
os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o
cálculo adequado.'''

codigo = int(input("Digite o código do produto: "))
preco = float(input("Digite o preço do produto: "))

match codigo:
    case 1:
        desconto = preco * 0.1
        valor = preco - desconto
        print(f"Pagando em cheque ou dinheiro o preço será R${valor:.2f}")
    case 2:
        desconto = preco * 0.05
        valor = preco - desconto
        print(f"Pagando à vista no cartão de crédito o preço será R${valor:.2f}")
    case 3:
        parcela = preco / 2
        print(f"Pagando em duas vezes, cada parcela será de R${parcela:.2f}.")
    case 4:
        juros = preco * 0.1
        valor = preco + juros
        parcela = valor / 3
        print(f"Pagando em três vezes, cada parcela será de R${parcela:.2f}")