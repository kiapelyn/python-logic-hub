'''Escreva um programa em Python para calcular e imprimir no vídeo o valor da expressão
abaixo: (expressão nos slides)
Observação: para o cálculo da expressão a variável x pode receber qualquer valor?
Lembre-se: não existe divisão por zero e nem raiz quadrada de números negativos no
campo dos números reais'''

x = float(input("Digite o valor de x: "))

# dois jeitos de fazer

if x < -5 or x > 5:
    y = (x-8)/((x**2)-25)**(1/2)
    print(f"y = {y:.3f}")
else:
    print("Valor inválido para x")
    
if x <= 5 and x >= -5:
    print("Valor inválido para x")
else:
    y = (x-8)/((x**2)-25)**(1/2)
    print(f"y = {y:.3f}")