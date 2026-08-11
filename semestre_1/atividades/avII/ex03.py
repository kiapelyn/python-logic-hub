melhor = (int(input("Qual o melhor Sistema Operacional para uso em servidores? ")))
win = 0
unix = 0
lin = 0
net = 0
mac = 0
outro = 0
total = 0

if melhor < 0 or melhor > 6:
    print("Código Inválido")
while melhor != 0:
    match melhor:
        case 1:
            win += 1
            total +=1
            melhor = (int(input("Qual o melhor Sistema Operacional para uso em servidores? ")))
        case 2:
            unix += 1
            total +=1
            melhor = (int(input("Qual o melhor Sistema Operacional para uso em servidores? ")))
        case 3:
            lin += 1
            total +=1
            melhor = (int(input("Qual o melhor Sistema Operacional para uso em servidores? ")))
        case 4:
            net += 1
            total +=1
            melhor = (int(input("Qual o melhor Sistema Operacional para uso em servidores? ")))
        case 5:
            mac += 1
            total +=1
            melhor = (int(input("Qual o melhor Sistema Operacional para uso em servidores? ")))
        case 6:
            outro += 1
            total +=1
            melhor = (int(input("Qual o melhor Sistema Operacional para uso em servidores? ")))


if melhor == 0:
    towin = win * 100 / total
    tunix = unix * 100 / total
    tlin = lin * 100 / total
    tnet = net * 100 / total
    tmac = mac * 100 / total
    toutro = outro * 100 / total
    
    print("Sistema Operaciona    Votos       %")
    print("------------------    -----     ------")
    print(f"Windows Server          {win}        {towin:.2f}%")
    print(f"Unix                    {unix}        {tunix:.2f}%")
    print(f"Linux                   {lin}        {tlin:.2f}%")
    print(f"Netware                 {net}        {tnet:.2f}%")
    print(f"Mac OS                  {mac}        {tmac:.2f}%")
    print(f"Outro                   {outro}        {toutro:.2f}%")
    print("-------------------   -----")
    print(f"Total:                  {total}")

if win == unix == lin == net == mac == outro:
    print(f"Os votos para todos os Sistemas Operacionais foram iguais entre si, resultando em:")
    print(f"{win} votos para cada de um total de {total}")
else:
    maior = 0
    if win >= maior:
        maior = win
        ven = 'Windows Server'
        por = towin
        if unix > maior:
            maior = unix
            ven = 'Unix'
            por = tunix
        elif lin > maior:
            maior = lin
            ven = 'Linux'
            por = tlin
        elif net > maior:
            maior = net
            ven = 'Netware'
            por = tnet
        elif mac > maior:
            maior = mac
            ven = 'Mac OS'
            por = tmac
        elif outro > maior:
            maior = outro
            ven = 'Outro'
            por = toutro

    if unix == maior and ven != 'Unix':
        maior2 = 'Unix'
    elif lin == maior and ven != 'Linux':
        maior2 = 'Linux'
    elif net == maior and ven != 'Netware':
        maior2 = 'Netware'
    elif mac == maior and ven != 'Mac':
        maior2 = 'Mac OS'
    elif outro == maior and ven != 'Outro':
        maior2 = 'Outro'
    else:
        maior2 = 'Indefinido'
        
    if maior2 == 'Indefinido':
        print(f"O Sistema Operacional mais votado foi o {ven}, com {total} votos")
        print(f"correspondendo a {por:.2f}% dos votos.")
    else:
        print(f"Os Sistemas Operacionais mais votados foram {ven} e {maior2}, com {total} votos cada")
        print(f"correspondendo a {por:.2f}% dos votos.")