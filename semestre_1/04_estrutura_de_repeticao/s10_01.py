'''programa exemplo para imprimir no terminal os números de 1 a 20

contador = 1

while contador <= 20:
    print(f'{contador}')
    contador = contador + 1'''

# <- breakpoint clicando do lado da linha pra mostrar onde o código para de executar
# python debug pra ver o código linha por linha

'''programa para ler os dois valores informados pelo usuário O programa
deve imprimir todos os números entre o primeiro e o segundo valor. A impressão deve
incluir os extremos.

contador1 = int(input("Digite o primeiro valor:"))
contador2 = int(input("Digite o seguundo valor:"))

while contador1 <= contador2:
    print(contador1)
    contador1 = contador1 + 1'''
    
'''programa para ler os dois valores informados pelo usuário O programa
deve imprimir somente os pares'''
    
contador1 = int(input("Digite o primeiro valor:"))
contador2 = int(input("Digite o seguundo valor:"))

while contador1 <= contador2:
    if contador1 % 2 == 0:
        print(contador1)
    contador1 = contador1 + 1