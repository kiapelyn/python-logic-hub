'''Escreva um programa em Python que leia um único valor contendo três dígitos, por
exemplo, 697. O seu programa deverá exibir o valor da dezena do número
informado. Se o usuário digitar o número 697, seu programa deverá imprimir no
vídeo apenas o número 9. Você deverá utilizar apenas o conteúdo apresentado em
aula na resolução do problema'''

#Entrada
original = int(input("Digite um valor real de três dígitos: "))

#Processamento
unidade = original % 10
remov = (original-unidade)//10
dezena = (remov % 10) 

#Saida
print(f"Resultado: {dezena}")
