
''' 
    a partir de uma lista de palavras (que pode haver repetição), imprimir a 
    quantidade de vezes que cada palavra aparece. Por último imprimir a ocorrência
    de cada letra . 
'''
# entrada das palavras
lista = []
total = int(input("Qual o total de palavras? "))
for i in range(total):
    lista.append(input("Palavra: "))
    
# contar o número de ocorrência de cada uma das palavras
ocorrencia_palavra = {}
for palavra in lista:
    if palavra in ocorrencia_palavra:
        ocorrencia_palavra[palavra] += 1 # ocorrencia[palavra] = ocorrencia[palavra] + 1
    else:
        ocorrencia_palavra[palavra] = 1
        
# impressão da ocorrência das palavras
for chave, valor in ocorrencia_palavra.items():
    print(f'{chave} --> {valor}')

# contar a ocorrência das letras
ocorrencia_letra = {}
for palavra in lista:
    for letra in palavra:
        if letra in ocorrencia_letra:
            ocorrencia_letra[letra] += 1
        else:
            ocorrencia_letra[letra] = 1

print("\nOcorrência das letras")
for chave, valor in ocorrencia_letra.items():
    print(f'{chave} --> {valor}')

