'''Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas a partir do
terminal e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser
enforcado.
Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!
Digite uma letra: O
A palavra é: _ _ _ _ O
Digite uma letra: E
A palavra é: _ E _ _ O
Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''
import random
    
def jogar(palavras):
    segredo = random.choice(palavras).lower()
    linhas = ['_'] * len(segredo)
    erro = 0
    while erro <= 6 and '_' in linhas:
        letra = input("Digite uma letra: ").lower()

        if letra in segredo:
            for i in range(len(segredo)):
                if segredo[i] == letra:
                    linhas[i] = letra
        else:
            erro += 1
            print(f"Você errou pela {erro}ª vez. Tente de novo!")
        print(linhas)
        
    if '_' not in linhas:
        print("Você acertou!")
    else: print("Você foi inforcado")
                
    
def ler_palavras():
    palavras = []
    for i in range(5):
        palavras.append(input("Informe uma palavra --> "))
    return palavras

def main():
    palavras = ler_palavras()
    jogar(palavras)
    
if __name__=='__main__':
    main()