from collections import deque
from random import randint

def registrar():
    treinador = input("Nome do Treinador: ")
    pokemon = input("Nome do Pokémon: ")
    vida_total = int(input("Vida Total: "))
    vida_atual = int(input("Vida Atual: "))

    dano = calcular_dano(vida_atual, vida_total)

    if dano == 0:
        print("Pokémon saudável. Não será admitido.")
        return

    if dano >= 100:
        print("Caso de emergência! Encaminhar para TECH.")
        return

    tempo = calcular_tempo(dano)

    atendimento = {
        'treinador': treinador,
        'pokemon': pokemon,
        'vida_total': vida_total,
        'vida_atual': vida_atual,
        'dano': dano,
        'tempo': tempo
    }

    fila.append(atendimento)
    print("Paciente registrado com sucesso!")
    
def atender():
    if not fila:
        print("Fila vazia!")
        return

    em_atendimento = fila.popleft()
    print(f"Treinador {em_atendimento['treinador']} dirigir-se a sala {randint(1,10)}\n"
    "O enfermeiro Selmini aguarda\n"
    " \n"
    f"Pokémon: {em_atendimento['pokemon']}\n"
    f"Dano: {em_atendimento['dano']:.2f}%\n"
    f"Tempo estimado: {em_atendimento['tempo']} unidades")


def calcular_dano(vida_atual, vida_total):
    if vida_total < 10:
        print("Vida total inválida!")
        return

    return ((vida_total - vida_atual) / vida_total) * 100


def calcular_tempo(dano):
    
    if dano <= 0 or dano >= 100:
        return 0
    
    tabela = [10, 25, 50, 75, 99]
    
    for limite in tabela:
        if dano <= limite:
            return limite

def exibir(): 
    if not fila:
        print("Fila vazia!")
        return

    print("=== FILA DE ESPERA ===")
    i = 1
    for pokemon in fila:
        print(f"paciente {i} -> {pokemon['treinador']} - {pokemon['pokemon']} ({pokemon['dano']:.2f}%)")
        i += 1
        
def calcular_tempo_total(fila):
    total = 0
    for pokemon in fila:
        total += pokemon['tempo']
    return total

def calcular_media_dano(fila):
    soma = 0
    for pokemon in fila:
        soma += pokemon['dano']
    return soma / len(fila)

def encontrar_mais_critico(fila):
    critico = fila[0]
    menor_relacao = critico['vida_atual'] / critico['vida_total']

    for pokemon in fila:
        relacao = pokemon['vida_atual'] / pokemon['vida_total']
        if relacao < menor_relacao:
            menor_relacao = relacao
            critico = pokemon

    return critico


fila = deque()

def main():
    while True:
        print(" ========== MENU ==========\n"
        "1. Registrar treinador na fila\n"
        "2. Atender próximo treinador\n"
        "3. Exibir fila\n"
        "4. Exibir Relatório Atual\n"
        "5. Encerrar")
        op = int(input("Escolha uma opção: "))
        print()
        match op:
            case 1:
                registrar()
                
            case 2:
                atender()
                
            case 3:
                exibir()
    
            case 4:
                if not fila:
                    print("Fila vazia!")
                    continue

                total = len(fila)
                tempo_total = calcular_tempo_total(fila)
                media_dano = calcular_media_dano(fila)
                critico = encontrar_mais_critico(fila)

                print("=== RELATÓRIO ===")
                print(f"Quantidade na fila: {total}")
                print(f"Tempo total estimado: {tempo_total}")
                print(f"Média de dano: {media_dano:.2f}%")
                print(f"Mais crítico: {critico['pokemon']} ({critico['treinador']})")
            case 5:
                print("Encerrado")
                break
            
            case _:
                print("Opção invalida!")

        print()

if __name__ == "__main__":
    main()

