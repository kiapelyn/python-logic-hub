risada = input()
lista  = ['a','e','i','o','u']


def codigos(lista):
    code = []
    for i in range(len(lista)):
        code.append(ord(lista[i]))
    return code
    

def pegar_vogais(risada, code):
    vogais = []
    for letra in range(len(risada)):
        if ord(risada[letra]) in code:
            vogais.append(risada[letra])
    return vogais

def inverter(vogais):
    vogais_invertidas = vogais[::-1]
    return vogais_invertidas

def verificar(vogais, vogais_invertidas):
    if vogais == vogais_invertidas: return 'sim'
    else: return 'não'
    
def main():
    code = codigos(lista)
    vogais = pegar_vogais(risada, code)
    vogais_invertidas = inverter(vogais)
    print(verificar(vogais, vogais_invertidas))
    
if __name__ == "__main__":
    main()
    