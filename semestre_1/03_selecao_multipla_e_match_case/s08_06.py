'''Desenvolva um programa em Python que leia o valor de dois números inteiros e a
operação aritmética desejada. O seu programa deverá calcular, então, a resposta
adequada. Utilize os símbolos da tabela a seguir para ler qual a operação aritmética
escolhida.'''

x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
operacao = input("Digite a operação: ")

match operacao:
    case "adição":
        total = x + y
        print(total)
    case "subtração":
        total = x - y
        print(total)
    case "multiplicação":
        total = x * y
        print(total)
    case operacao if operacao == "divisão" and y == 0:
        print("Não é possível dividir por 0")   
    case operacao if operacao == "divisão" and y != 0:
        total = x / y
        print(total)
    case _:
        print("Operação inválida")