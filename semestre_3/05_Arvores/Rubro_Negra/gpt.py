"""
Implementação completa de uma Árvore Rubro-Negra (Red-Black Tree) em Python.

Características:
- Inserção com balanceamento
- Remoção com correção de propriedades
- Busca
- Percurso em ordem
- Impressão visual da árvore
- Validação das propriedades da árvore rubro-negra

Autor: ChatGPT
"""

from __future__ import annotations


class Node:
    """
    Representa um nó da árvore rubro-negra.
    """

    RED = "RED"
    BLACK = "BLACK"

    def __init__(self, key=None, color=RED):
        self.key = key
        self.color = color
        self.parent: Node | None = None
        self.left: Node | None = None
        self.right: Node | None = None

    def __repr__(self):
        return f"{self.key}({self.color[0]})"


class RedBlackTree:
    """
    Implementação de uma Árvore Rubro-Negra.
    """

    def __init__(self):
        # Nó sentinela NIL (sempre negro)
        self.nil = Node(color=Node.BLACK)

        # O NIL aponta para si mesmo
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.parent = self.nil

        self.root = self.nil

    # =========================================================
    # ROTAÇÕES
    # =========================================================

    def left_rotate(self, x: Node):
        """
        Realiza rotação à esquerda em torno de x.
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

    def right_rotate(self, x: Node):
        """
        Realiza rotação à direita em torno de x.
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
    # INSERÇÃO
    # =========================================================

    def insert(self, key):
        """
        Insere uma chave na árvore.
        """

        new_node = Node(key, Node.RED)

        new_node.left = self.nil
        new_node.right = self.nil

        parent = self.nil
        current = self.root

        # Inserção padrão de ABB
        while current != self.nil:
            parent = current

            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent == self.nil:
            self.root = new_node

        elif new_node.key < parent.key:
            parent.left = new_node

        else:
            parent.right = new_node

        # Corrige violações
        self.insert_fixup(new_node)

    def insert_fixup(self, z: Node):
        """
        Corrige violações após inserção.
        """

        while z.parent.color == Node.RED:

            # Pai é filho esquerdo
            if z.parent == z.parent.parent.left:

                uncle = z.parent.parent.right

                # CASO 1: tio vermelho
                if uncle.color == Node.RED:
                    z.parent.color = Node.BLACK
                    uncle.color = Node.BLACK
                    z.parent.parent.color = Node.RED

                    z = z.parent.parent

                else:
                    # CASO 2: triângulo
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)

                    # CASO 3: linha
                    z.parent.color = Node.BLACK
                    z.parent.parent.color = Node.RED
                    self.right_rotate(z.parent.parent)

            # Casos simétricos
            else:

                uncle = z.parent.parent.left

                # CASO 1
                if uncle.color == Node.RED:
                    z.parent.color = Node.BLACK
                    uncle.color = Node.BLACK
                    z.parent.parent.color = Node.RED

                    z = z.parent.parent

                else:
                    # CASO 2
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    # CASO 3
                    z.parent.color = Node.BLACK
                    z.parent.parent.color = Node.RED
                    self.left_rotate(z.parent.parent)

        # A raiz deve ser negra
        self.root.color = Node.BLACK

    # =========================================================
    # BUSCA
    # =========================================================

    def search(self, key):
        """
        Busca uma chave na árvore.

        Retorna:
            - Node, se encontrado
            - None, caso contrário
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
        Retorna True se a chave existir na árvore.
        """

        return self.search(key) is not None

    # =========================================================
    # REMOÇÃO
    # =========================================================

    def transplant(self, u: Node, v: Node):
        """
        Substitui a subárvore enraizada em u por v.
        """

        if u.parent == self.nil:
            self.root = v

        elif u == u.parent.left:
            u.parent.left = v

        else:
            u.parent.right = v

        v.parent = u.parent

    def minimum(self, node: Node):
        """
        Retorna o menor nó da subárvore.
        """

        while node.left != self.nil:
            node = node.left

        return node

    def delete(self, key):
        """
        Remove uma chave da árvore.
        """

        z = self.search(key)

        if z is None:
            print(f"Chave {key} não encontrada.")
            return

        y = z
        y_original_color = y.color

        # CASO 1 ou 2
        if z.left == self.nil:

            x = z.right
            self.transplant(z, z.right)

        elif z.right == self.nil:

            x = z.left
            self.transplant(z, z.left)

        # CASO 3
        else:

            y = self.minimum(z.right)
            y_original_color = y.color

            x = y.right

            if y.parent == z:
                x.parent = y

            else:
                self.transplant(y, y.right)

                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)

            y.left = z.left
            y.left.parent = y

            y.color = z.color

        # Se removemos um nó negro,
        # precisamos corrigir a árvore
        if y_original_color == Node.BLACK:
            self.delete_fixup(x)

    def delete_fixup(self, x: Node):
        """
        Corrige violações após remoção.
        """

        while x != self.root and x.color == Node.BLACK:

            # x é filho esquerdo
            if x == x.parent.left:

                w = x.parent.right

                # CASO 1: irmão vermelho
                if w.color == Node.RED:
                    w.color = Node.BLACK
                    x.parent.color = Node.RED
                    self.left_rotate(x.parent)

                    w = x.parent.right

                # CASO 2: ambos filhos negros
                if w.left.color == Node.BLACK and w.right.color == Node.BLACK:
                    w.color = Node.RED
                    x = x.parent

                else:

                    # CASO 3
                    if w.right.color == Node.BLACK:
                        w.left.color = Node.BLACK
                        w.color = Node.RED
                        self.right_rotate(w)

                        w = x.parent.right

                    # CASO 4
                    w.color = x.parent.color
                    x.parent.color = Node.BLACK
                    w.right.color = Node.BLACK

                    self.left_rotate(x.parent)

                    x = self.root

            # Casos simétricos
            else:

                w = x.parent.left

                # CASO 1
                if w.color == Node.RED:
                    w.color = Node.BLACK
                    x.parent.color = Node.RED

                    self.right_rotate(x.parent)

                    w = x.parent.left

                # CASO 2
                if w.right.color == Node.BLACK and w.left.color == Node.BLACK:
                    w.color = Node.RED
                    x = x.parent

                else:

                    # CASO 3
                    if w.left.color == Node.BLACK:
                        w.right.color = Node.BLACK
                        w.color = Node.RED

                        self.left_rotate(w)

                        w = x.parent.left

                    # CASO 4
                    w.color = x.parent.color
                    x.parent.color = Node.BLACK
                    w.left.color = Node.BLACK

                    self.right_rotate(x.parent)

                    x = self.root

        x.color = Node.BLACK

    # =========================================================
    # PERCURSO EM ORDEM
    # =========================================================

    def inorder(self):
        """
        Retorna lista das chaves em ordem crescente.
        """

        result = []

        def _inorder(node):

            if node == self.nil:
                return

            _inorder(node.left)
            result.append(node.key)
            _inorder(node.right)

        _inorder(self.root)

        return result

    # =========================================================
    # IMPRESSÃO DA ÁRVORE
    # =========================================================

    def print_tree(self):
        """
        Imprime a árvore de forma hierárquica.
        """

        def _print(node, indent="", last=True):

            if node == self.nil:
                return

            print(indent, end="")

            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "

            color = "RED" if node.color == Node.RED else "BLACK"

            print(f"{node.key} ({color})")

            _print(node.left, indent, False)
            _print(node.right, indent, True)

        if self.root == self.nil:
            print("(árvore vazia)")
        else:
            _print(self.root)

    # =========================================================
    # VALIDAÇÃO DAS PROPRIEDADES
    # =========================================================

    def validate(self):
        """
        Verifica se todas as propriedades da árvore
        rubro-negra estão corretas.
        """

        # Propriedade 1:
        # raiz deve ser negra
        if self.root.color != Node.BLACK:
            return False

        def check(node):

            # NIL possui altura negra 1
            if node == self.nil:
                return 1

            # Não pode haver dois vermelhos consecutivos
            if node.color == Node.RED:

                if node.left.color == Node.RED:
                    return -1

                if node.right.color == Node.RED:
                    return -1

            left_black_height = check(node.left)
            right_black_height = check(node.right)

            # Violação encontrada abaixo
            if left_black_height == -1 or right_black_height == -1:
                return -1

            # Alturas negras diferentes
            if left_black_height != right_black_height:
                return -1

            # Soma altura negra
            if node.color == Node.BLACK:
                return left_black_height + 1

            return left_black_height

        return check(self.root) != -1


# =========================================================
# TESTES
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("TESTE 1")
    print("=" * 60)

    tree = RedBlackTree()

    sequence1 = [9, 8, 7, 6, 1, 2, 3, 4, 5]

    for value in sequence1:
        print(f"\nInserindo {value}")
        tree.insert(value)

        tree.print_tree()

        print("Inorder:", tree.inorder())

        assert tree.validate()

    print("\nÁrvore final:")
    tree.print_tree()

    print("\nValidação:", tree.validate())

    # =====================================================

    print("\n" + "=" * 60)
    print("TESTE 2")
    print("=" * 60)

    tree2 = RedBlackTree()

    sequence2 = [4, 7, 12, 15, 3, 5, 14, 18]

    for value in sequence2:
        tree2.insert(value)

    print("\nÁrvore final:")
    tree2.print_tree()

    print("\nInorder:", tree2.inorder())

    print("\nValidação:", tree2.validate())

    # =====================================================
    # BUSCAS
    # =====================================================

    print("\n" + "=" * 60)
    print("BUSCAS")
    print("=" * 60)

    searches = [7, 15, 99, 1]

    for value in searches:

        result = tree2.search(value)

        if result:
            print(f"Chave {value} encontrada -> {result}")
        else:
            print(f"Chave {value} NÃO encontrada")

    # =====================================================
    # REMOÇÕES
    # =====================================================

    print("\n" + "=" * 60)
    print("REMOÇÕES")
    print("=" * 60)

    removals = [
        18,  # folha
        15,  # um filho
        7    # dois filhos
    ]

    for value in removals:

        print(f"\nRemovendo {value}")

        tree2.delete(value)

        tree2.print_tree()

        print("Inorder:", tree2.inorder())

        print("Validação:", tree2.validate())

        assert tree2.validate()

    print("\nTodos os testes foram executados com sucesso.")