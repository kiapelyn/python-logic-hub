


def criptografar(texto: str, d: int) -> str:
    aux = ""
    for letra in texto:
        if letra.isalpha():
            cod = ord(letra)
            aux += chr(((cod - 97 + d) % 26) + 97)
        else:
            aux += letra
    return aux

def descriptografar(texto_cripto:str, d: int) -> str:
    return criptografar(texto_cripto, -d)    

def main():
    d = int(input("Insira a chave: "))
    texto = input("Insira a frase: ").lower()
    texto_cripto = criptografar(texto, d)
    texto_descripto = descriptografar(texto_cripto, d)
    print(texto_cripto) 
    print(texto_descripto)  


    
if __name__=='__main__':
    main()