class Node:
    """
    Representa um nó de uma Árvore Rubro-Negra.

    Attributes:
        key: Chave armazenada no nó.
        color: Cor do nó ('RED' ou 'BLACK').
        parent: Referência para o pai.
        left: Referência para o filho esquerdo.
        right: Referência para o filho direito.
    """

    RED = "RED"
    BLACK = "BLACK"

    def __init__(self, key=None, color=RED, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(key={self.key}, color={self.color})"


class RedBlackTree:
    """
    Implementação de uma Árvore Rubro-Negra.

    A árvore usa um nó sentinela compartilhado `nil`, sempre negro,
    para representar filhos nulos.
    """

    def __init__(self):
        self.nil = Node(color=Node.BLACK)
        self.nil.parent = self.nil
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.root = self.nil

    # =========================================================
    # Métodos públicos
    # =========================================================

    def insert(self, key):
        """
        Insere uma chave na árvore.

        A inserção começa como em uma ABB comum, criando o novo nó rubro.
        Em seguida, aplica correções para restaurar as propriedades
        da árvore rubro-negra.
        """
        new_node = Node(key=key, color=Node.RED, left=self.nil, right=self.nil, parent=self.nil)

        parent = self.nil
        current = self.root

        while current != self.nil:
            parent = current
            if new_node.key < current.key:
                current = current.left
            elif new_node.key > current.key:
                current = current.right
            else:
                # Ignora duplicatas; alternativamente poderia lançar exceção.
                return

        new_node.parent = parent

        if parent == self.nil:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self._insert_fixup(new_node)

    def search(self, key):
        """
        Busca uma chave na árvore.

        Returns:
            O nó correspondente, se encontrado; caso contrário, None.
        """
        current = self.root

        while current != self.nil:
            if key == current.key:
                return current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    def contains(self, key):
        """
        Verifica se a chave existe na árvore.

        Returns:
            True se a chave existir, False caso contrário.
        """
        return self.search(key) is not None

    def delete(self, key):
        """
        Remove a chave da árvore, se existir.

        A remoção segue os casos clássicos:
        - nó folha,
        - nó com um filho,
        - nó com dois filhos (substituição pelo sucessor).
        Após a remoção física, corrige a árvore se necessário.
        """
        node_to_delete = self._search_node(key)
        if node_to_delete == self.nil:
            return

        y = node_to_delete
        y_original_color = y.color

        if node_to_delete.left == self.nil:
            x = node_to_delete.right
            self._transplant(node_to_delete, node_to_delete.right)

        elif node_to_delete.right == self.nil:
            x = node_to_delete.left
            self._transplant(node_to_delete, node_to_delete.left)

        else:
            y = self._minimum(node_to_delete.right)
            y_original_color = y.color
            x = y.right

            if y.parent == node_to_delete:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node_to_delete.right
                y.right.parent = y

            self._transplant(node_to_delete, y)
            y.left = node_to_delete.left
            y.left.parent = y
            y.color = node_to_delete.color

        if y_original_color == Node.BLACK:
            self._delete_fixup(x)

    def inorder(self):
        """
        Retorna as chaves em ordem crescente.
        """
        result = []
        self._inorder_walk(self.root, result)
        return result

    def print_tree(self):
        """
        Imprime a árvore de forma legível para depuração.
        """
        if self.root == self.nil:
            print("(árvore vazia)")
            return
        self._print_subtree(self.root, "", True)

    def validate_properties(self):
        """
        Verifica programaticamente se todas as propriedades da
        árvore rubro-negra estão sendo respeitadas.

        Returns:
            True se a árvore for válida.

        Raises:
            AssertionError em caso de violação.
        """
        # Propriedade: NIL é preto.
        assert self.nil.color == Node.BLACK, "O nó sentinela NIL deve ser preto."

        # Propriedade: raiz é preta.
        if self.root != self.nil:
            assert self.root.color == Node.BLACK, "A raiz deve ser preta."

        self._validate_bst_property(self.root, None, None)
        self._validate_red_property(self.root)
        self._validate_black_height(self.root)

        return True

    # =========================================================
    # Operações internas: rotações
    # =========================================================

    def left_rotate(self, x):
        """
        Realiza rotação à esquerda em torno de x.

        Estrutura:
              x                 y
               \\               / \\
                y     ->      x   ...
               / \\             \\
             ... ...          ...
        """
        y = x.right
        x.right = y.left

        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        """
        Realiza rotação à direita em torno de x.

        Estrutura:
                x              y
               /              / \\
              y      ->     ...  x
             / \\                /
           ... ...            ...
        """
        y = x.left
        x.left = y.right

        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # =========================================================
    # Inserção: correção
    # =========================================================

    def _insert_fixup(self, z):
        """
        Restaura as propriedades da árvore rubro-negra após inserção.

        Casos clássicos:
        - Caso 1: pai vermelho e tio vermelho -> recoloração.
        - Caso 2/3: pai vermelho e tio preto -> rotações + recoloração.
        """
        while z.parent.color == Node.RED:
            if z.parent == z.parent.parent.left:
                uncle = z.parent.parent.right

                # Caso 1: pai vermelho e tio vermelho
                if uncle.color == Node.RED:
                    z.parent.color = Node.BLACK
                    uncle.color = Node.BLACK
                    z.parent.parent.color = Node.RED
                    z = z.parent.parent

                else:
                    # Caso 2: pai é filho esquerdo e z é filho direito
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)

                    # Caso 3: pai é filho esquerdo e z é filho esquerdo
                    z.parent.color = Node.BLACK
                    z.parent.parent.color = Node.RED
                    self.right_rotate(z.parent.parent)

            else:
                # Casos simétricos à direita
                uncle = z.parent.parent.left

                # Caso 1: pai vermelho e tio vermelho
                if uncle.color == Node.RED:
                    z.parent.color = Node.BLACK
                    uncle.color = Node.BLACK
                    z.parent.parent.color = Node.RED
                    z = z.parent.parent

                else:
                    # Caso 2 simétrico: pai é filho direito e z é filho esquerdo
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    # Caso 3 simétrico: pai é filho direito e z é filho direito
                    z.parent.color = Node.BLACK
                    z.parent.parent.color = Node.RED
                    self.left_rotate(z.parent.parent)

        self.root.color = Node.BLACK

    # =========================================================
    # Remoção: correção
    # =========================================================

    def _delete_fixup(self, x):
        """
        Restaura as propriedades da árvore rubro-negra após remoção.

        Trata os casos clássicos de 'duplo negro' usando recoloração e rotações.
        """
        while x != self.root and x.color == Node.BLACK:
            if x == x.parent.left:
                w = x.parent.right

                # Caso 1: irmão vermelho
                if w.color == Node.RED:
                    w.color = Node.BLACK
                    x.parent.color = Node.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right

                # Caso 2: irmão preto com dois filhos pretos
                if w.left.color == Node.BLACK and w.right.color == Node.BLACK:
                    w.color = Node.RED
                    x = x.parent

                else:
                    # Caso 3: irmão preto, filho direito preto, filho esquerdo vermelho
                    if w.right.color == Node.BLACK:
                        w.left.color = Node.BLACK
                        w.color = Node.RED
                        self.right_rotate(w)
                        w = x.parent.right

                    # Caso 4: irmão preto, filho direito vermelho
                    w.color = x.parent.color
                    x.parent.color = Node.BLACK
                    w.right.color = Node.BLACK
                    self.left_rotate(x.parent)
                    x = self.root

            else:
                # Casos simétricos
                w = x.parent.left

                # Caso 1 simétrico: irmão vermelho
                if w.color == Node.RED:
                    w.color = Node.BLACK
                    x.parent.color = Node.RED
                    self.right_rotate(x.parent)
                    w = x.parent.left

                # Caso 2 simétrico: irmão preto com dois filhos pretos
                if w.right.color == Node.BLACK and w.left.color == Node.BLACK:
                    w.color = Node.RED
                    x = x.parent

                else:
                    # Caso 3 simétrico: irmão preto, filho esquerdo preto, filho direito vermelho
                    if w.left.color == Node.BLACK:
                        w.right.color = Node.BLACK
                        w.color = Node.RED
                        self.left_rotate(w)
                        w = x.parent.left

                    # Caso 4 simétrico: irmão preto, filho esquerdo vermelho
                    w.color = x.parent.color
                    x.parent.color = Node.BLACK
                    w.left.color = Node.BLACK
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = Node.BLACK

    # =========================================================
    # Auxiliares internas
    # =========================================================

    def _search_node(self, key):
        current = self.root
        while current != self.nil:
            if key == current.key:
                return current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return self.nil

    def _minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def _transplant(self, u, v):
        """
        Substitui a subárvore enraizada em u pela subárvore enraizada em v.
        """
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def _inorder_walk(self, node, result):
        if node == self.nil:
            return
        self._inorder_walk(node.left, result)
        result.append(node.key)
        self._inorder_walk(node.right, result)

    def _print_subtree(self, node, prefix, is_tail):
        if node == self.nil:
            return

        label = f"{node.key} ({'R' if node.color == Node.RED else 'B'})"
        connector = "└── " if is_tail else "├── "
        print(prefix + connector + label)

        children = []
        if node.left != self.nil:
            children.append(node.left)
        if node.right != self.nil:
            children.append(node.right)

        for i, child in enumerate(children):
            next_prefix = prefix + ("    " if is_tail else "│   ")
            self._print_subtree(child, next_prefix, i == len(children) - 1)

    def _validate_bst_property(self, node, min_key, max_key):
        if node == self.nil:
            return

        if min_key is not None:
            assert node.key > min_key, f"Violação da propriedade BST: {node.key} <= {min_key}"
        if max_key is not None:
            assert node.key < max_key, f"Violação da propriedade BST: {node.key} >= {max_key}"

        self._validate_bst_property(node.left, min_key, node.key)
        self._validate_bst_property(node.right, node.key, max_key)

    def _validate_red_property(self, node):
        if node == self.nil:
            return

        if node.color == Node.RED:
            assert node.left.color == Node.BLACK, f"Nó vermelho {node.key} tem filho esquerdo vermelho."
            assert node.right.color == Node.BLACK, f"Nó vermelho {node.key} tem filho direito vermelho."

        self._validate_red_property(node.left)
        self._validate_red_property(node.right)

    def _validate_black_height(self, node):
        """
        Retorna a altura negra da subárvore e valida consistência.
        """
        if node == self.nil:
            return 1

        left_black_height = self._validate_black_height(node.left)
        right_black_height = self._validate_black_height(node.right)

        assert (
            left_black_height == right_black_height
        ), f"Altura negra inconsistente no nó {node.key}: {left_black_height} != {right_black_height}"

        return left_black_height + (1 if node.color == Node.BLACK else 0)


# =========================================================
# Testes
# =========================================================

def run_sequence_test(sequence, title):
    print("=" * 70)
    print(title)
    print("=" * 70)

    tree = RedBlackTree()

    for key in sequence:
        print(f"\nInserindo {key}...")
        tree.insert(key)
        tree.print_tree()
        print("Inorder:", tree.inorder())
        assert tree.validate_properties()

    print("\nÁrvore final:")
    tree.print_tree()
    print("Inorder final:", tree.inorder())
    assert tree.validate_properties()

    return tree


if __name__ == "__main__":
    # -----------------------------------------------------
    # Teste 1: sequência solicitada
    # -----------------------------------------------------
    sequence1 = [9, 8, 7, 6, 1, 2, 3, 4, 5]
    tree1 = run_sequence_test(sequence1, "Teste 1: Inserção da sequência 9, 8, 7, 6, 1, 2, 3, 4, 5")

    # Buscas
    print("\n" + "=" * 70)
    print("Buscas na árvore 1")
    print("=" * 70)
    for key in [1, 5, 9, 10, 42]:
        result = tree1.search(key)
        print(f"search({key}) -> {result}")
        print(f"contains({key}) -> {tree1.contains(key)}")

    assert tree1.contains(1) is True
    assert tree1.contains(10) is False

    # Remoções cobrindo casos
    print("\n" + "=" * 70)
    print("Remoções na árvore 1")
    print("=" * 70)

    removals1 = [5, 6, 8]  # exemplos que tendem a cobrir folha, um filho, dois filhos
    for key in removals1:
        print(f"\nRemovendo {key}...")
        tree1.delete(key)
        tree1.print_tree()
        print("Inorder:", tree1.inorder())
        assert tree1.validate_properties()

    # -----------------------------------------------------
    # Teste 2: segunda sequência solicitada
    # -----------------------------------------------------
    sequence2 = [4, 7, 12, 15, 3, 5, 14, 18]
    tree2 = run_sequence_test(sequence2, "Teste 2: Inserção da sequência 4, 7, 12, 15, 3, 5, 14, 18")

    print("\n" + "=" * 70)
    print("Buscas na árvore 2")
    print("=" * 70)
    for key in [3, 14, 20]:
        result = tree2.search(key)
        print(f"search({key}) -> {result}")
        print(f"contains({key}) -> {tree2.contains(key)}")

    print("\n" + "=" * 70)
    print("Remoções na árvore 2")
    print("=" * 70)

    removals2 = [3, 15, 7]
    for key in removals2:
        print(f"\nRemovendo {key}...")
        tree2.delete(key)
        tree2.print_tree()
        print("Inorder:", tree2.inorder())
        assert tree2.validate_properties()

    print("\nTodos os testes terminaram com sucesso.")