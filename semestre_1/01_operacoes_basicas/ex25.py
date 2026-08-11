'''Escreva um programa em Python que leia uma medida em pés, calcular, armazenar e imprimir no vídeo o
seu valor convertido em metros, lembrando que um pé mede 0,3048 metro, ou seja, um pé é igual a 30,48
centímetros. Imprima o valor no vídeo utilizando duas casas decimais.'''

pes = float(input("Digite um valor em pés: "))

metros = pes * 0.3048

print(f"{pes} pés é igual a {metros:.3f} metros")