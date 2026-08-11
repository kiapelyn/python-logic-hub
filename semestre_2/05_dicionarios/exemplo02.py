'''
    A partir de uma lista de palavras (que pode haver repetição), imprimir a 
    quantidade de vezes que cada palavra aparece. Por último imprimir a
    ocorrência de cada letra.
'''

qnt = int(input())
lista = []
dic = {}
dic2 = {}

print()

for i in range(qnt):
    lista.append(input())
    
print()

for palavra in lista:
    if palavra in dic:
        dic[palavra] += 1
    else:
        dic[palavra] = 1
        
for palavra, qtd in dic.items():
    print(f"{palavra}: {qtd}")

print()

for palavra in lista:
    for letra in palavra:
        if letra in dic2:
            dic2[letra] += 1
        else:
            dic2[letra] = 1
            
for letra, valor in dic2.items():
    print(f"{letra}: {valor}")
            