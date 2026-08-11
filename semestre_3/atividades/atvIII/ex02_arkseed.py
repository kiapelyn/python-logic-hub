class Especie:
    def __init__(self, codigo_raridade, nome_comum, nome_cientifico, continente_origem, qtd_amostras):
        self.codigo_raridade = codigo_raridade
        self.nome_comum = nome_comum
        self.nome_cientifico = nome_cientifico
        self.continente_origem = continente_origem
        self.qtd_amostras = qtd_amostras

    def __str__(self):
        return f"[Raridade: {self.codigo_raridade}] {self.nome_comum} ({self.nome_cientifico}) - {self.continente_origem} | Amostras: {self.qtd_amostras}"

class NoEspecie:
    def __init__(self, especie):
        self.especie = especie
        self.esq = None
        self.dir = None
        self.altura = 1

class AVLArkSeed:
    def __init__(self):
        self.raiz = None

    def _altura(self, no):
        if no is None:
            return 0
        return no.altura

    def _atualizar_altura(self, no):
        no.altura = 1 + max(self._altura(no.esq), self._altura(no.dir))

    def _fator(self, no):
        if no is None:
            return 0
        return self._altura(no.esq) - self._altura(no.dir)

    def _rotacao_direita(self, z):
        y = z.esq
        T3 = y.dir
        y.dir = z
        z.esq = T3
        self._atualizar_altura(z)
        self._atualizar_altura(y)
        return y

    def _rotacao_esquerda(self, z):
        y = z.dir
        T2 = y.esq
        y.esq = z
        z.dir = T2
        self._atualizar_altura(z)
        self._atualizar_altura(y)
        return y

    def _rebalancear(self, no):
        self._atualizar_altura(no)
        fb = self._fator(no)

        if fb > 1 and self._fator(no.esq) >= 0:
            return self._rotacao_direita(no)

        if fb > 1 and self._fator(no.esq) < 0:
            no.esq = self._rotacao_esquerda(no.esq)
            return self._rotacao_direita(no)

        if fb < -1 and self._fator(no.dir) <= 0:
            return self._rotacao_esquerda(no)

        if fb < -1 and self._fator(no.dir) > 0:
            no.dir = self._rotacao_direita(no.dir)
            return self._rotacao_esquerda(no)

        return no

    def inserir_especie(self, especie):
        self.raiz = self._inserir(self.raiz, especie)

    def _inserir(self, no, especie):
        if no is None:
            return NoEspecie(especie)

        if especie.codigo_raridade < no.especie.codigo_raridade:
            no.esq = self._inserir(no.esq, especie)
        elif especie.codigo_raridade > no.especie.codigo_raridade:
            no.dir = self._inserir(no.dir, especie)
        else:
            return no # duplicado ignora

        return self._rebalancear(no)

    def remover_especie(self, codigo):
        removido = [None]
        self.raiz = self._remover(self.raiz, codigo, removido)
        return removido[0]

    def _remover(self, no, codigo, removido):
        if no is None:
            return None

        if codigo < no.especie.codigo_raridade:
            no.esq = self._remover(no.esq, codigo, removido)
        elif codigo > no.especie.codigo_raridade:
            no.dir = self._remover(no.dir, codigo, removido)
        else:
            removido[0] = no.especie
            if no.esq is None:
                return no.dir
            if no.dir is None:
                return no.esq

            sucessor = self._minimo(no.dir)
            no.especie = sucessor.especie
            no.dir = self._remover(no.dir, sucessor.especie.codigo_raridade, [None])

        return self._rebalancear(no)

    def _minimo(self, no):
        while no.esq is not None:
            no = no.esq
        return no

    def buscar_por_codigo(self, codigo):
        return self._buscar(self.raiz, codigo)

    def _buscar(self, no, codigo):
        if no is None:
            return None
        if codigo == no.especie.codigo_raridade:
            return no.especie
        if codigo < no.especie.codigo_raridade:
            return self._buscar(no.esq, codigo)
        return self._buscar(no.dir, codigo)

    def alerta_extincao(self, codigo_atual, novo_codigo):
        especie = self.remover_especie(codigo_atual)
        if especie:
            especie.codigo_raridade = novo_codigo
            self.inserir_especie(especie)
            print("Alerta processado: Código atualizado com sucesso e árvore rebalanceada.")
        else:
            print("Erro: Espécie não encontrada.")

    def resgatar_especie_rara(self):
        if self.raiz is None:
            print("Nenhuma espécie catalogada.")
            return

        no_mais_raro = self.raiz
        while no_mais_raro.dir is not None:
            no_mais_raro = no_mais_raro.dir
        
        especie = self.remover_especie(no_mais_raro.especie.codigo_raridade)
        print("Espécie mais rara resgatada com sucesso:")
        print(especie)

    def relatorio_emergencia(self):
        print("\n--- Relatório de Emergência (Da Mais Rara Para A Mais Comum) ---")
        if self.raiz is None:
            print("Nenhuma espécie catalogada.")
            return
        self._percurso_dre(self.raiz)

    def _percurso_dre(self, no):
        if no is not None:
            self._percurso_dre(no.dir)
            print(no.especie)
            self._percurso_dre(no.esq)


def menu():
    sistema = AVLArkSeed()
    
    while True:
        print("\n" + "="*45)
        print("ARKSEED - BANCO DE SEMENTES ORBITAL (2203)")
        print("="*45)
        print("a) Catalogar espécie")
        print("b) Alerta de extinção (Atualizar código)")
        print("c) Resgatar espécie mais rara")
        print("d) Buscar por código de raridade")
        print("e) Relatório de emergência")
        print("s) Sair do sistema")
        
        opcao = input("Escolha uma opção: ").lower()
        
        if opcao == 'a':
            codigo = int(input("Código de Raridade: "))
            nome_comum = input("Nome comum: ")
            nome_cientifico = input("Nome científico: ")
            continente = input("Continente de origem: ")
            qtd = int(input("Quantidade de amostras: "))
            especie = Especie(codigo, nome_comum, nome_cientifico, continente, qtd)
            sistema.inserir_especie(especie)
            print("Espécie catalogada com sucesso!")
            
        elif opcao == 'b':
            codigo_atual = int(input("Informe o código de raridade atual: "))
            novo_codigo = int(input("Informe o novo código de raridade: "))
            sistema.alerta_extincao(codigo_atual, novo_codigo)
            
        elif opcao == 'c':
            sistema.resgatar_especie_rara()
            
        elif opcao == 'd':
            codigo = int(input("Informe o código de raridade para busca: "))
            especie = sistema.buscar_por_codigo(codigo)
            if especie:
                print("\nEspécie encontrada:")
                print(especie)
            else:
                print("\nEspécie não encontrada.")
                
        elif opcao == 'e':
            sistema.relatorio_emergencia()
            
        elif opcao == 's':
            print("Encerrando o sistema ArkSeed. Salvem a Terra!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
