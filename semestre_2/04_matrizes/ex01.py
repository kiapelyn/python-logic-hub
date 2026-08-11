'''Escreva um programa em Python que leia um vetor de números inteiros (a quantidade
de elementos fica a seu critério). O seu programa deverá gerar um novo vetor
contendo os elementos do vetor original, mas sem duplicação. Imprima os elementos
do vetor para verificar se o seu código está correto. Observação: na resolução desse
exercício deverão ser utilizadas apenas as estrutura de programação estudadas até o
momento'''

from random import randint
original = []
nova = []

#lendo os valores da lista original
for i in range(randint(2, 8)):
    original.append(randint(-2, 10))
    if original[i] not in nova:
        nova.append(original[i])


print(original)
print(nova)
        

        
    