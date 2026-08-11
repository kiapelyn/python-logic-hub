'''Um número é chamado de palíndromo se tem a mesma leitura nos dois sentidos, por exemplo, o
número 212 (da direita para esquerda ou da esquerda para a direita é o mesmo número). O maior
número palíndromo gerado pelo produto de dois números naturais com dois dígitos é 9009 (91 x
99). Escreva um programa em python que encontre o maior número palíndromo formado pela
multiplicação de dois números naturais com três dígitos.'''

maior_palindromo = 0

for val1 in range(100, 1000):
    for val2 in range(100, 1000):
        val3 = val1 * val2
        original = val3
        invertido = 0

        while val3 > 0:
            digito = val3 % 10
            invertido = invertido * 10 + digito
            val3 = val3 // 10

        if original == invertido and original > maior_palindromo:
            maior_palindromo = original

print("Maior palíndromo:", maior_palindromo)