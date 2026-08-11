#a ideia da fila é o FIFO -> first in, first out.

from collections import deque
from random import randint

fila = deque()

dias = int(input("Por quantos dias ações serão compradas? "))
numero = 0
soma = 0

for i in range(dias):
    qnt = int(input(f"Quantas ações serão compradas no dia {i+1}? "))
    numero += qnt
    preco = randint(10,80)
    print(f"você tem {qnt} ações valendo R${preco:.2f} cada")
    for _ in range(qnt):
        fila.append(preco)
        soma += preco
        
print(f"Você tem {numero} ações.")
print(f"Montante total gasto: R${soma:.2f}")
valor = randint(10,80)
venda = int(input(f"Preço de cotação: R${valor},00. Quantas deseja vender? "))

total = 0
for i in range(venda):
    conta = fila.popleft() - valor
    total += conta

resultado = soma - total

if total >= 0:
    print(f"Total ganho: R${total:.2f}")
    print(f"Relação ao total gasto: R${resultado:.2f}")
else:
    total = total*(-1)
    print(f"Total perdido: -R${total:.2f}")
    print(f"Relação ao total gasto: R${resultado:.2f}")
