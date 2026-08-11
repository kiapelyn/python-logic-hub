#Calculo de fatorial 


# para somar [1+1+1+1+1+...+1+1] 100 vezes
cont = 1
total = 0

while cont <= 100:
    total = total + 1
    cont = cont + 1
    
# para somar [1+2+3+4+5+6...+99+100]
cont = 1
total = 0

while cont <= 100:
    total = total + cont
    cont = cont + 1
    

# para multiplicar [1*2*3*4*5*...*99*100]

cont = 1
total = 1

while cont <= 100:
    total = total * cont
    cont = cont + 1
    
# para somar fração 

print(total)

# ------------------

for cont in range(0, 11, 1): #onde começca, até onde vai (um antes), de quanto em quanto conta
    print(cont)
    