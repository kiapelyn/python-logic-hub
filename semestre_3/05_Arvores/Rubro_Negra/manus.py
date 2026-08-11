class Node:
    RED = True
    BLACK = False

    def __init__(self, key, color=RED, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color=Node.BLACK)  # Nó sentinela negro
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        z = Node(key)
        z.left = self.NIL
        z.right = self.NIL

        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.parent.color == Node.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # Tio
                if y.color == Node.RED:  # Caso 1
                    z.parent.color = Node.BLACK
                    y.color = Node.BLACK
                    z.parent.parent.color = Node.RED
                    z = z.parent.parent
                else:  # Caso 2 e 3
                    if z == z.parent.right:  # Caso 2
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = Node.BLACK  # Caso 3
                    z.parent.parent.color = Node.RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left  # Tio
                if y.color == Node.RED:  # Caso 1 (simétrico)
                    z.parent.color = Node.BLACK
                    y.color = Node.BLACK
                    z.parent.parent.color = Node.RED
                    z = z.parent.parent
                else:  # Caso 2 e 3 (simétrico)
                    if z == z.parent.left:  # Caso 2 (simétrico)
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = Node.BLACK  # Caso 3 (simétrico)
                    z.parent.parent.color = Node.RED
                    self.left_rotate(z.parent.parent)
        self.root.color = Node.BLACK

    def search(self, key):
        x = self.root
        while x != self.NIL and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def contains(self, key):
        return self.search(key) != self.NIL

    def __transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def delete(self, key):
        z = self.search(key)
        if z == self.NIL:
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.__transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.__transplant(z, z.left)
        else:
            y = self.__minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == Node.BLACK:
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == Node.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Node.RED:
                    w.color = Node.BLACK
                    x.parent.color = Node.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == Node.BLACK and w.right.color == Node.BLACK:
                    w.color = Node.RED
                    x = x.parent
                else:
                    if w.right.color == Node.BLACK:
                        w.left.color = Node.BLACK
                        w.color = Node.RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Node.BLACK
                    w.right.color = Node.BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == Node.RED:
                    w.color = Node.BLACK
                    x.parent.color = Node.RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == Node.BLACK and w.left.color == Node.BLACK:
                    w.color = Node.RED
                    x = x.parent
                else:
                    if w.left.color == Node.BLACK:
                        w.right.color = Node.BLACK
                        w.color = Node.RED
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Node.BLACK
                    w.left.color = Node.BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = Node.BLACK

    def inorder_walk(self, node):
        if node != self.NIL:
            self.inorder_walk(node.left)
            print(node.key, end=" ")
            self.inorder_walk(node.right)

    def inorder(self):
        keys = []
        self._inorder_collect(self.root, keys)
        return keys

    def _inorder_collect(self, node, keys):
        if node != self.NIL:
            self._inorder_collect(node.left, keys)
            keys.append(node.key)
            self._inorder_collect(node.right, keys)

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, indent):
        if node != self.NIL:
            self._print_tree_recursive(node.right, indent + 1)
            print("  " * indent + str(node.key) + " (" + ("RED" if node.color else "BLACK") + ")")
            self._print_tree_recursive(node.left, indent + 1)

    def validate_properties(self):
        if self.root == self.NIL:
            return True
        
        # Propriedade 4: A raiz é negra
        if self.root.color != Node.BLACK:
            print("Violação: Raiz não é negra")
            return False
            
        return self._validate_recursive(self.root)[0]

    def _validate_recursive(self, node):
        if node == self.NIL:
            return True, 1  # (is_valid, black_height)

        # Propriedade 6: Não podem existir dois nós rubros consecutivos
        if node.color == Node.RED:
            if node.left.color == Node.RED or node.right.color == Node.RED:
                print(f"Violação: Nó rubro {node.key} tem filho rubro")
                return False, 0

        left_valid, left_bh = self._validate_recursive(node.left)
        right_valid, right_bh = self._validate_recursive(node.right)

        if not left_valid or not right_valid:
            return False, 0

        # Propriedade 7: Mesmo número de nós negros em todos os caminhos
        if left_bh != right_bh:
            print(f"Violação: Altura negra inconsistente no nó {node.key}")
            return False, 0

        bh = left_bh + (1 if node.color == Node.BLACK else 0)
        return True, bh

if __name__ == "__main__":
    rbt = RedBlackTree()
    
    print("--- Inserindo sequência 1: 9, 8, 7, 6, 1, 2, 3, 4, 5 ---")
    for k in [9, 8, 7, 6, 1, 2, 3, 4, 5]:
        rbt.insert(k)
        print(f"Inserido {k}. Árvore válida: {rbt.validate_properties()}")
    
    print("\nEstrutura final da sequência 1:")
    rbt.print_tree()
    
    print("\n--- Inserindo sequência 2: 4, 7, 12, 15, 3, 5, 14, 18 ---")
    rbt2 = RedBlackTree()
    for k in [4, 7, 12, 15, 3, 5, 14, 18]:
        rbt2.insert(k)
    rbt2.print_tree()
    print(f"Árvore 2 válida: {rbt2.validate_properties()}")

    print("\n--- Testes de Busca ---")
    for k in [7, 20]:
        print(f"Busca {k}: {'Encontrado' if rbt2.contains(k) else 'Não encontrado'}")

    print("\n--- Testes de Remoção na Árvore 2 ---")
    # Caso 1: Folha (ex: 3 ou 5 ou 14 ou 18)
    print("\nRemovendo 3 (folha):")
    rbt2.delete(3)
    rbt2.print_tree()
    print(f"Válida: {rbt2.validate_properties()}")

    # Caso 2: Um filho (ex: 15 tem 14 e 18, mas vamos remover 18 primeiro)
    print("\nRemovendo 18 (folha):")
    rbt2.delete(18)
    rbt2.print_tree()
    print(f"Válida: {rbt2.validate_properties()}")
    
    print("\nRemovendo 15 (um filho):")
    rbt2.delete(15)
    rbt2.print_tree()
    print(f"Válida: {rbt2.validate_properties()}")

    # Caso 3: Dois filhos (ex: 7 ou 12)
    print("\nRemovendo 7 (dois filhos):")
    rbt2.delete(7)
    rbt2.print_tree()
    print(f"Válida: {rbt2.validate_properties()}")
