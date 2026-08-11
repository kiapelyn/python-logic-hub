from ex02classe import Musica

# não consegui acertar o jeito que compara os valores
# mas fiz a segunda parte do minimo e máximo :(
# enfim já sei oq tenho q estudar nas férias 

playlist = [Musica(4, 'Rain', 'Sleep Token', 5.03),
            Musica(2, 'To Be Alone', 'Hozier', 4.35), 
            Musica(5, 'Asa Branca', 'Trio Parada Dura', 3.56),
            Musica(3, 'Kool-Aid', 'BMTH', 3.15),
            Musica(1, 'Be', 'Hozier', 3.12)
            ]

def bolha(lista):      
    for i in lista:
        for i in range(len(lista)-1):
            if lista[i].codi > lista[i+1].codi:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

        
playlist_nova = bolha(playlist)

for i in playlist_nova:
    print(i.codi, i.titulo)

def busca_binaria(lista: list[int], valor):
    ini, fim = 0, len(lista) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio].codi == valor:
            return True
        elif lista[meio].codi < valor:
            ini = meio + 1
        else:
            fim = meio - 1
    return False

print(busca_binaria(playlist, 2))

def busca_sequencial(lista: list[Musica], min: float, max: float) -> int:
    valido = []
    for i in lista:
        if i.duracao_seg >= min and i.duracao_seg <= max:
            valido.append((i.titulo, i.duracao_seg))
    return valido

valido = busca_sequencial(playlist, 3.0, 4.0)

print(valido)
