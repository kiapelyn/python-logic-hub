'''Reescreva o exercício 3 substituindo a estrutura if-elif-else pela estrutura match.'''

idade = int(input("Digite a idade do nadador:"))

match idade:
    case idade if idade < 5:
        print("Idade inválida")
    case 5 | 6 | 7:
        print("Categoria Infantil A")
    case 8 | 9 | 10:
        print("Categoria Infantil B")
    case 11 | 12 | 13:
        print("Categoria Juvenil A")
    case 14 | 15 | 16 | 17:
        print ("Categoria Juvenil B")
    case _:
        print("Categoria Adulto")