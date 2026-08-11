from collections import deque

modificadores = [
    {"nome": "Choice Band", "prioridade": 1, "descricao": "+5 no dano"},
    {"nome": "Potion", "prioridade": 1, "descricao": "x1.2 no dano + finaliza o turno"},
    {"nome": "Weakness Policy", "prioridade": 2, "descricao": "x2 no dano"},
    {"nome": "STAB Boots", "prioridade": 2, "descricao": "x1.5 se dano ≥ 10"},
    {"nome": "Critical Hit", "prioridade": 3, "descricao": "dano ao quadrado"},
]

def prioridade(mod):
    for i in modificadores:
        if i["nome"] == mod:
            return i["prioridade"]
    return 0

def descricao(mod):
    for i in modificadores:
        if i["nome"] == mod:
            return i["descricao"]

def aplicar(mod, dano):
    match mod:
        case "Choice Band": return dano + 5
        case "Potion": return dano * 1.2
        case "Weakness Policy": return dano * 2
        case "STAB Boots":
            if dano >= 20:
                return dano *1.5
            else:
                return dano
        case "Critical Hit": return dano ** 2


def processar(pilha, mod, dano):
    print(f"Inserindo {mod}")

    while pilha and prioridade(pilha[-1]) >= prioridade(mod):
        topo = pilha.pop()
        print(f"Removendo {topo}")
        print(f"Aplicando {topo}")
        antes = dano
        dano = aplicar(topo, dano)
        print(f"{topo}: {antes:.2f} → {dano:.2f}")

    pilha.append(mod)
    print(f"{mod} empilhado")

    return dano

def finalizar(pilha, dano):
    print("Finalizando processamento...")

    while pilha:
        topo = pilha.pop()
        antes = dano
        dano = aplicar(topo, dano)

        print(f"Aplicando {topo}: {antes:.2f} → {dano:.2f}")

    print("Pilha vazia!")
    return dano

def main():
    pilha = deque()
    usados = []

    dano = float(input("Valor base do ataque: "))

    while True:
        print(" ========== MENU ==========\n"
        "1 - Inserir modificador\n"
        "2 - Ver detalher de um modificador\n"
        "3 - Finalizar turno\n"
        "4 - Sair")

        op = int(input("Escolha: "))

        match op:
            case 1:
                print("\nModificadores:")
                for i in range(len(modificadores)):
                    print(f"{i+1} - {modificadores[i]['nome']}")

                op_mod = int(input("Escolha: "))
                mod = modificadores[op_mod - 1]["nome"]

                print(f"{mod} selecionado")
                print(descricao(mod))

                if mod in usados:
                    print("Modificador já utilizado!")
                    continue

                usados.append(mod)

                if mod == "Potion":
                    print("Finalizando turno...")
                    dano = finalizar(pilha, dano)
                    dano = aplicar("Potion", dano)
                    print(f"Dano final: {dano}")
                    break

                dano = processar(pilha, mod, dano)
                
            case 2:
                print("\n=== MODIFICADORES ===")
                for i in range(len(modificadores)):
                    print(f"{i+1} - {modificadores[i]['nome']}")

                op_mod = int(input("Escolha: "))
                mod = modificadores[op_mod - 1]["nome"]

                print(f"{mod}\n"
                f"Prioridade: {prioridade(mod)}\n"
                f"Efeito: {descricao(mod)}")

            case 3:
                dano = finalizar(pilha, dano)
                print(f"Dano final: {dano}")
                break

            case 4:
                print("Encerrado")
                break

            case _:
                print("Opção inválida")

        print()

if __name__ == "__main__":
    main()