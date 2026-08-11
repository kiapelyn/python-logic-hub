'''Reescreva o exercício 1 substituindo a estrutura if-elif-else pela estrutura match.'''

codigo = int(input("Insira o código do produto:"))

match codigo:
    case 1:
        print("Alimento não perecível")
    case 2 | 3 | 4:
        print("Alimento perecível")
    case 5 | 6:
        print("Vestuário")
    case 7:
        print("Higiene Pessoal")
    case codigo if codigo >= 8 and codigo <= 15:
        print("Limpeza e utensílios domésticos")
    case _:
        print("Código inválido")