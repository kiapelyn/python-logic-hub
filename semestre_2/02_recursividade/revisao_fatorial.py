def funcao(x):
    if x == 0: return 1
    return x * funcao(x-1)

print(funcao(6))

'''vai correr x-1 até x == 0, vai voltar multiplicando o valor que está armazenando na função por 
x-1 até que x volte a ser 6, ou seja, fatorial!'''