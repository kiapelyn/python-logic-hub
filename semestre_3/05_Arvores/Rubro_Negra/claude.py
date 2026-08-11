"""
Árvore Rubro-Negra (Red-Black Tree) — Implementação completa em Python puro.

Propriedades mantidas:
  1. Todo nó é vermelho (RED) ou preto (BLACK).
  2. A raiz é sempre preta.
  3. Nós NIL (sentinela) são tratados como pretos.
  4. Nenhum caminho raiz→NIL possui dois nós vermelhos consecutivos.
  5. Todo caminho raiz→NIL passa pelo mesmo número de nós pretos
     (altura negra uniforme).
"""

# ---------------------------------------------------------------------------
# Constantes de cor
# ---------------------------------------------------------------------------
RED = 0
BLACK = 1


# ---------------------------------------------------------------------------
# Classe Node
# ---------------------------------------------------------------------------
class Node:
    """
    Representa um nó da Árvore Rubro-Negra.

    Atributos
    ---------
    key    : valor armazenado no nó.
    color  : RED (0) ou BLACK (1).
    parent : referência ao nó pai.
    left   : filho esquerdo.
    right  : filho direito.
    """

    def __init__(self, key, color: int = RED):
        """
        Parâmetros
        ----------
        key   : chave do nó.
        color : cor inicial; padrão RED para nós comuns, BLACK para o NIL.
        """
        self.key = key
        self.color = color
        self.parent: "Node | None" = None
        self.left: "Node | None" = None
        self.right: "Node | None" = None

    def __repr__(self) -> str:
        color_str = "RED" if self.color == RED else "BLACK"
        return f"Node(key={self.key}, color={color_str})"


# ---------------------------------------------------------------------------
# Classe RedBlackTree
# ---------------------------------------------------------------------------
class RedBlackTree:
    """
    Árvore Rubro-Negra com suporte a inserção, remoção e busca.

    A implementação segue o algoritmo clássico descrito por Cormen et al.
    (CLRS), utilizando um nó sentinela ``nil`` para representar todas as
    folhas nulas, o que simplifica o tratamento de casos de fronteira.
    """

    def __init__(self):
        # Sentinela: nó preto compartilhado que representa todos os NIL.
        self.nil = Node(key=None, color=BLACK)
        self.nil.parent = self.nil
        self.nil.left = self.nil
        self.nil.right = self.nil

        # Raiz aponta inicialmente para o sentinela (árvore vazia).
        self.root: Node = self.nil

    # -----------------------------------------------------------------------
    # Rotações
    # -----------------------------------------------------------------------

    def _left_rotate(self, x: Node) -> None:
        """
        Rotação à esquerda em torno do nó ``x``.

        Antes:          Depois:
            x               y
           / \\            / \\
          A   y          x   C
             / \\        / \\
            B   C      A   B
        """
        y = x.right                    # y torna-se o novo "topo"
        x.right = y.left               # a subárvore esquerda de y vai para x

        if y.left is not self.nil:
            y.left.parent = x

        y.parent = x.parent            # liga y ao pai de x

        if x.parent is self.nil:       # x era raiz
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x                     # x fica à esquerda de y
        x.parent = y

    def _right_rotate(self, x: Node) -> None:
        """
        Rotação à direita em torno do nó ``x`` (simétrica a _left_rotate).

        Antes:          Depois:
            x               y
           / \\            / \\
          y   C          A   x
         / \\                / \\
        A   B              B   C
        """
        y = x.left
        x.left = y.right

        if y.right is not self.nil:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # -----------------------------------------------------------------------
    # Inserção
    # -----------------------------------------------------------------------

    def insert(self, key) -> None:
        """
        Insere uma chave na árvore, mantendo todas as propriedades
        rubro-negras após a operação.

        Parâmetros
        ----------
        key : chave a inserir (deve ser comparável via < e >).
        """
        new_node = Node(key=key, color=RED)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.parent = self.nil

        # --- Passo 1: inserção padrão de ABB ---
        parent = self.nil
        current = self.root

        while current is not self.nil:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is self.nil:           # árvore estava vazia
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # --- Passo 2: restaurar propriedades rubro-negras ---
        self._insert_fixup(new_node)

    def _insert_fixup(self, z: Node) -> None:
        """
        Corrige violações das propriedades rubro-negras após inserção.

        Casos tratados (e seus simétricos à direita):
          Caso 1 – tio vermelho  : recolorir pai, tio e avô; subir z.
          Caso 2 – tio preto, z filho interno  : rotação simples em pai.
          Caso 3 – tio preto, z filho externo  : recolorir + rotação em avô.
        """
        while z.parent.color == RED:
            # ---- pai é filho ESQUERDO do avô ----
            if z.parent is z.parent.parent.left:
                uncle = z.parent.parent.right    # tio

                # Caso 1: tio vermelho → recolorir e subir
                if uncle.color == RED:
                    z.parent.color = BLACK
                    uncle.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent          # sobe para o avô

                else:
                    # Caso 2: z é filho direito (triângulo) → rotação em pai
                    if z is z.parent.right:
                        z = z.parent
                        self._left_rotate(z)

                    # Caso 3: z é filho esquerdo (linha reta) → rotação em avô
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._right_rotate(z.parent.parent)

            # ---- pai é filho DIREITO do avô (casos simétricos) ----
            else:
                uncle = z.parent.parent.left

                # Caso 1 simétrico
                if uncle.color == RED:
                    z.parent.color = BLACK
                    uncle.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent

                else:
                    # Caso 2 simétrico
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)

                    # Caso 3 simétrico
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._left_rotate(z.parent.parent)

        # Garante que a raiz seja sempre preta (propriedade 2)
        self.root.color = BLACK

    # -----------------------------------------------------------------------
    # Busca
    # -----------------------------------------------------------------------

    def search(self, key) -> "Node | None":
        """
        Busca a chave na árvore e retorna o nó correspondente,
        ou ``None`` se a chave não existir.

        Parâmetros
        ----------
        key : chave a procurar.
        """
        current = self.root
        while current is not self.nil:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def contains(self, key) -> bool:
        """Retorna ``True`` se a chave existir na árvore, ``False`` caso contrário."""
        return self.search(key) is not None

    # -----------------------------------------------------------------------
    # Remoção
    # -----------------------------------------------------------------------

    def delete(self, key) -> None:
        """
        Remove a chave da árvore, restaurando as propriedades rubro-negras.

        Se a chave não existir, o método não faz nada.

        Parâmetros
        ----------
        key : chave a remover.
        """
        target = self.search(key)
        if target is None:
            return  # chave inexistente: operação silenciosa
        self._delete_node(target)

    def _delete_node(self, z: Node) -> None:
        """Remove o nó ``z`` da árvore e chama o fixup necessário."""
        y = z                            # y é o nó que será fisicamente removido
        y_original_color = y.color       # guarda a cor original de y

        if z.left is self.nil:
            # Caso 1/2a: sem filho esquerdo → substitui por filho direito
            x = z.right
            self._transplant(z, z.right)

        elif z.right is self.nil:
            # Caso 2b: sem filho direito → substitui por filho esquerdo
            x = z.left
            self._transplant(z, z.left)

        else:
            # Caso 3: dois filhos → usa o sucessor (mínimo da subárvore direita)
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right                  # filho do sucessor (pode ser NIL)

            if y.parent is z:
                # Sucessor é filho direto de z
                x.parent = y
            else:
                # Desloca o sucessor para fora da sua posição atual
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            # Coloca o sucessor no lugar de z
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color            # herda a cor do nó removido

        # Se o nó removido era preto, podem surgir violações ("duplo-negro")
        if y_original_color == BLACK:
            self._delete_fixup(x)

    def _transplant(self, u: Node, v: Node) -> None:
        """
        Substitui a subárvore enraizada em ``u`` pela subárvore enraizada em ``v``,
        ajustando o ponteiro do pai de ``u``.
        """
        if u.parent is self.nil:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node: Node) -> Node:
        """Retorna o nó com a menor chave na subárvore enraizada em ``node``."""
        while node.left is not self.nil:
            node = node.left
        return node

    def _delete_fixup(self, x: Node) -> None:
        """
        Corrige violações das propriedades rubro-negras após remoção.

        Trata a condição de "duplo-negro" em ``x`` por meio de rotações
        e recolorações, subindo pelo caminho até a raiz quando necessário.

        Casos (e simétricos à direita):
          Caso 1 – irmão vermelho            : rotação + recolorir, reduzir ao 2/3/4.
          Caso 2 – irmão preto, sobrinhos pretos : recolorir irmão; subir.
          Caso 3 – irmão preto, sobrinho próximo vermelho : rotação + recolorir.
          Caso 4 – irmão preto, sobrinho distante vermelho: rotação + recolorir; termina.
        """
        while x is not self.root and x.color == BLACK:
            # ---- x é filho ESQUERDO ----
            if x is x.parent.left:
                sibling = x.parent.right

                # Caso 1: irmão vermelho
                if sibling.color == RED:
                    sibling.color = BLACK
                    x.parent.color = RED
                    self._left_rotate(x.parent)
                    sibling = x.parent.right    # atualiza irmão após rotação

                # Caso 2: irmão preto, ambos sobrinhos pretos
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    x = x.parent               # sobe o "duplo-negro"

                else:
                    # Caso 3: sobrinho próximo (esquerdo) vermelho, distante preto
                    if sibling.right.color == BLACK:
                        sibling.left.color = BLACK
                        sibling.color = RED
                        self._right_rotate(sibling)
                        sibling = x.parent.right

                    # Caso 4: sobrinho distante (direito) vermelho
                    sibling.color = x.parent.color
                    x.parent.color = BLACK
                    sibling.right.color = BLACK
                    self._left_rotate(x.parent)
                    x = self.root               # termina o loop

            # ---- x é filho DIREITO (casos simétricos) ----
            else:
                sibling = x.parent.left

                # Caso 1 simétrico
                if sibling.color == RED:
                    sibling.color = BLACK
                    x.parent.color = RED
                    self._right_rotate(x.parent)
                    sibling = x.parent.left

                # Caso 2 simétrico
                if sibling.right.color == BLACK and sibling.left.color == BLACK:
                    sibling.color = RED
                    x = x.parent

                else:
                    # Caso 3 simétrico
                    if sibling.left.color == BLACK:
                        sibling.right.color = BLACK
                        sibling.color = RED
                        self._left_rotate(sibling)
                        sibling = x.parent.left

                    # Caso 4 simétrico
                    sibling.color = x.parent.color
                    x.parent.color = BLACK
                    sibling.left.color = BLACK
                    self._right_rotate(x.parent)
                    x = self.root

        # Nó que absorveu o "duplo-negro" ou a raiz tornam-se pretos
        x.color = BLACK

    # -----------------------------------------------------------------------
    # Funções auxiliares / depuração
    # -----------------------------------------------------------------------

    def inorder(self) -> list:
        """
        Retorna uma lista com as chaves em ordem crescente (in-order traversal).
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Node, result: list) -> None:
        if node is not self.nil:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def print_tree(self) -> None:
        """
        Imprime a estrutura da árvore de forma hierárquica (raiz no topo),
        indicando a cor de cada nó. Útil para depuração visual.
        """
        print("─" * 50)
        self._print_recursive(self.root, prefix="", is_left=True)
        print("─" * 50)

    def _print_recursive(self, node: Node, prefix: str, is_left: bool) -> None:
        if node is self.nil:
            return
        color_label = "R" if node.color == RED else "B"
        connector = "├── " if is_left else "└── "
        print(f"{prefix}{connector}[{node.key}:{color_label}]")
        extension = "│   " if is_left else "    "
        self._print_recursive(node.left,  prefix + extension, is_left=True)
        self._print_recursive(node.right, prefix + extension, is_left=False)

    # -----------------------------------------------------------------------
    # Validação das propriedades rubro-negras
    # -----------------------------------------------------------------------

    def validate(self) -> bool:
        """
        Verifica programaticamente se todas as propriedades da árvore
        rubro-negra estão sendo respeitadas.

        Retorna
        -------
        bool : ``True`` se a árvore for válida, ``False`` caso contrário
               (com mensagem descritiva impressa no console).
        """
        # Propriedade 2: raiz deve ser preta
        if self.root is not self.nil and self.root.color != BLACK:
            print("VIOLAÇÃO: a raiz não é preta.")
            return False

        ok, _ = self._validate_recursive(self.root)
        if ok:
            print("✓ Árvore válida — todas as propriedades rubro-negras respeitadas.")
        return ok

    def _validate_recursive(self, node: Node) -> tuple:
        """
        Retorna (is_valid: bool, black_height: int) para o nó fornecido.
        Checa ausência de dois vermelhos consecutivos e altura negra uniforme.
        """
        if node is self.nil:
            return True, 1   # nó NIL conta como 1 nó preto

        left_ok,  left_bh  = self._validate_recursive(node.left)
        right_ok, right_bh = self._validate_recursive(node.right)

        if not left_ok or not right_ok:
            return False, 0

        # Propriedade 4: nenhum nó vermelho tem filho vermelho
        if node.color == RED:
            if node.left.color == RED or node.right.color == RED:
                print(f"VIOLAÇÃO: dois vermelhos consecutivos em [{node.key}].")
                return False, 0

        # Propriedade 5: alturas negras iguais nos dois lados
        if left_bh != right_bh:
            print(
                f"VIOLAÇÃO: alturas negras diferentes em [{node.key}] "
                f"(esq={left_bh}, dir={right_bh})."
            )
            return False, 0

        black_height = left_bh + (1 if node.color == BLACK else 0)
        return True, black_height


# ===========================================================================
# Bloco de testes
# ===========================================================================

if __name__ == "__main__":

    def section(title: str) -> None:
        print(f"\n{'=' * 60}")
        print(f"  {title}")
        print(f"{'=' * 60}")

    # -----------------------------------------------------------------------
    # Teste 1 — Inserções sequenciais: 9, 8, 7, 6, 1, 2, 3, 4, 5
    # -----------------------------------------------------------------------
    section("TESTE 1 — Inserções: 9, 8, 7, 6, 1, 2, 3, 4, 5")
    rbt1 = RedBlackTree()
    keys1 = [9, 8, 7, 6, 1, 2, 3, 4, 5]

    for k in keys1:
        rbt1.insert(k)
        print(f"\nApós inserir {k}:")
        rbt1.print_tree()

    print(f"\nOrdem crescente: {rbt1.inorder()}")
    rbt1.validate()

    # -----------------------------------------------------------------------
    # Teste 2 — Inserções: 4, 7, 12, 15, 3, 5, 14, 18
    # -----------------------------------------------------------------------
    section("TESTE 2 — Inserções: 4, 7, 12, 15, 3, 5, 14, 18")
    rbt2 = RedBlackTree()
    keys2 = [4, 7, 12, 15, 3, 5, 14, 18]

    for k in keys2:
        rbt2.insert(k)

    print("Árvore após todas as inserções:")
    rbt2.print_tree()
    print(f"Ordem crescente: {rbt2.inorder()}")
    rbt2.validate()

    # -----------------------------------------------------------------------
    # Teste 3 — Buscas (existentes e inexistentes)
    # -----------------------------------------------------------------------
    section("TESTE 3 — Buscas")

    # Usamos a árvore do teste 1 (chaves 1–9)
    for key in [1, 5, 9, 0, 10, 6]:
        found = rbt1.search(key)
        if found:
            print(f"  search({key}) → {found}")
        else:
            print(f"  search({key}) → Não encontrado")

    print()
    for key in [3, 7, 99]:
        print(f"  contains({key}) → {rbt1.contains(key)}")

    # -----------------------------------------------------------------------
    # Teste 4 — Remoções (folha, um filho, dois filhos)
    # -----------------------------------------------------------------------
    section("TESTE 4 — Remoções")

    # Árvore de trabalho: insere 10..50 de 10 em 10
    rbt3 = RedBlackTree()
    for k in [20, 10, 30, 5, 15, 25, 40, 35, 50]:
        rbt3.insert(k)

    print("Árvore inicial (para remoções):")
    rbt3.print_tree()
    print(f"Ordem: {rbt3.inorder()}")
    rbt3.validate()

    # Remoção de folha: 35 (sem filhos)
    print("\n→ Removendo 35 (folha):")
    rbt3.delete(35)
    rbt3.print_tree()
    print(f"Ordem: {rbt3.inorder()}")
    rbt3.validate()

    # Remoção de nó com um filho: 40 (só tem 50 como filho direito)
    print("\n→ Removendo 40 (um filho):")
    rbt3.delete(40)
    rbt3.print_tree()
    print(f"Ordem: {rbt3.inorder()}")
    rbt3.validate()

    # Remoção de nó com dois filhos: 20 (raiz com duas subárvores)
    print("\n→ Removendo 20 (dois filhos — raiz):")
    rbt3.delete(20)
    rbt3.print_tree()
    print(f"Ordem: {rbt3.inorder()}")
    rbt3.validate()

    # Remoção de chave inexistente — não deve lançar exceção
    print("\n→ Tentando remover 99 (inexistente):")
    rbt3.delete(99)
    print("  Nenhuma exceção levantada — comportamento correto.")
    rbt3.validate()

    # -----------------------------------------------------------------------
    # Teste 5 — Inserção e remoção de muitos elementos (stress test)
    # -----------------------------------------------------------------------
    section("TESTE 5 — Stress test (inserção + remoção de 50 elementos)")
    import random
    random.seed(42)

    rbt4 = RedBlackTree()
    nums = random.sample(range(1, 201), 50)
    for n in nums:
        rbt4.insert(n)

    assert rbt4.inorder() == sorted(nums), "Ordem incorreta após inserções!"
    rbt4.validate()

    # Remove metade dos elementos
    to_remove = nums[:25]
    for n in to_remove:
        rbt4.delete(n)

    remaining = sorted(nums[25:])
    assert rbt4.inorder() == remaining, "Ordem incorreta após remoções!"
    rbt4.validate()
    print(f"  50 inserções + 25 remoções — árvore íntegra. Restam {len(remaining)} nós.")
    print(f"  Ordem final: {rbt4.inorder()}")