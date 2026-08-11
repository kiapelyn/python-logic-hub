'''Escreva um programa em Python que leia um número inteiro. Imprimir sua
tabuada no vídeo (considerar apenas o intervalo entre 0 e 10). O programa deve
permitir reprocessamento, ou seja, após a sua execução deverá ser perguntado
ao usuário se ele deseja executar novamente ou finalizar a aplicação.'''

executar = input("Gostaria de executar o programa? (sim ou não) ")

while executar == "sim":
    valor = int(input("Digite o número: "))
    multiplicador = 0
    while multiplicador <= 10:
        resultado = valor * multiplicador
        multiplicador = multiplicador + 1
        print(resultado)
    executar = input("Gostaria de executar o programa? ")

if executar == "não":
    print("Programa encerrado, obrigado!")
    