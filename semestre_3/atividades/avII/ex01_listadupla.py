class No:
    def __init__(self, nome):
        self.nome = nome
        self.pokemons = 0
        self.ginasio = False
        self.visitado = False

        self.esq = None
        self.dir = None
        
class Jornada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.atual = None
        self.tamanho = 0
        
    def inserirFim(self, nome):
        novo = No(nome)
        
        if self.tamanho == 0:
            self.inicio = novo
            self.atual = novo

            print(f"Você iniciou sua jornada em: {novo.nome}")

            novo.visitado = True
            novo.pokemons = int(input("Quantos Pokémon você avistou aqui? "))
            novo.ginasio = input("Visitou ginásio? (s/n): ") == "s"

        else:
            self.fim.dir = novo
            novo.esq = self.fim

        self.fim = novo
        self.tamanho += 1
        
    def posicaoAtual(self):
        aux = self.inicio
        pos = 0

        while aux:
            if aux == self.atual:
                return pos
            aux = aux.dir
            pos += 1

        return -1
        
    def inserirPosicao(self, posicao, nome):
        posicao -= 1

        pos_atual = self.posicaoAtual()

        if posicao < pos_atual:
            print("Não é possível inserir antes do ponto atual da jornada!")
            return
        
        novo = No(nome)

        if posicao < 0:
            return

        if posicao >= self.tamanho:
            self.inserirFim(nome)
            return

        aux = self.inicio

        for i in range(posicao):
            aux = aux.dir

        novo.esq = aux.esq
        novo.dir = aux

        if aux.esq:
            aux.esq.dir = novo
        else:
            self.inicio = novo

        aux.esq = novo

        self.tamanho += 1
        
    def avancar(self):
        if self.atual is None:
            print("Jornada vazia!")
            return

        if self.atual.dir is None:
            print("Você já está no último local!")
            return

        self.atual = self.atual.dir
        
        if not self.atual.visitado:
            self.atual.visitado = True

            print(f"Você chegou em: {self.atual.nome}")

            self.atual.pokemons = int(input("Quantos Pokémon você avistou aqui? "))
            self.atual.ginasio = input("Visitou ginásio? (s/n): ") == "s"
            
        else:
            print(f"Você retornou para: {self.atual.nome}")
        
    def voltar(self):
        if self.atual is None:
            print("Jornada vazia!")
            return

        if self.atual.esq is None:
            print("Você já está no primeiro local!")
            return

        self.atual = self.atual.esq

        print(f"Retornou para: {self.atual.nome}")
        
    def removerAtual(self):
        if self.atual is None:
            print("Jornada vazia!")
            return

        aux = self.atual

        if self.tamanho == 1:
            self.inicio = None
            self.fim = None
            self.atual = None

        elif aux == self.inicio:
            self.inicio = aux.dir
            self.inicio.esq = None
            self.atual = self.inicio

        elif aux == self.fim:
            self.fim = aux.esq
            self.fim.dir = None
            self.atual = self.fim

        else:
            aux.esq.dir = aux.dir
            aux.dir.esq = aux.esq
            self.atual = aux.dir

        self.tamanho -= 1
        print(f"Removido: {aux.nome}")
        aux.esq = None
        aux.dir = None
        
    def exibir(self):
        aux = self.inicio
        
        if self.inicio is None:
            print("Jornada vazia!")
            return

        while aux:
            if aux == self.atual:
                status = " (ATUAL)"
            elif aux.visitado:
                status = " (visitado)"
            else:
                status = " (planejado)"

            print(f"{aux.nome}: {status}")

            aux = aux.dir
    
    def estatisticas(self):
        if self.inicio is None:
            print("Jornada vazia!")
            return

        aux = self.inicio

        total_pokemons = 0
        ginasios = 0
        visitados = 0

        while aux:
            total_pokemons += aux.pokemons

            if aux.ginasio:
                ginasios += 1

            if aux.visitado:
                visitados += 1

            aux = aux.dir

        print("=== ESTATÍSTICAS ===\n"
        f"Pokémons avistados: {total_pokemons}\n"
        f"Ginásios visitados: {ginasios}\n"
        f"Locais visitados: {visitados}")
        
def main():
    jornada = Jornada()

    while True:
        print("========= MENU =========\n"
            "1 - Inserir local no fim\n"
            "2 - Inserir local em posição\n"
            "3 - Avançar na jornada\n"
            "4 - Voltar na jornada\n"
            "5 - Remover local atual\n"
            "6 - Exibir jornada\n"
            "7 - Exibir estatísticas\n"
            "8 - Encerrar")

        op = int(input("Escolha uma opção: "))
        print()

        match op:
            case 1:
                nome = input("Nome do local: ")

                jornada.inserirFim(nome)
                print(f"Você registrou que visitará {nome}")

            case 2:
                pos = int(input("Posição: "))
                nome = input("Nome do local: ")

                jornada.inserirPosicao(pos, nome)

            case 3:
                jornada.avancar()

            case 4:
                jornada.voltar()

            case 5:
                jornada.removerAtual()

            case 6:
                jornada.exibir()

            case 7:
                jornada.estatisticas()

            case 8:
                print("Encerrando sistema...")
                break

            case _:
                print("Opção inválida!")

        print()


if __name__ == "__main__":
    main()