import sys

# Constantes para definição de cores
RED = 0
BLACK = 1

class Node:
    """
    Representa um nó em uma Árvore Rubro-Negra.
    """
    def __init__(self, key, color=RED):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        color_str = "R" if self.color == RED else "B"
        return f"{self.key}({color_str})"


class RedBlackTree:
    """
    Implementação de uma Árvore Rubro-Negra (Red-Black Tree).
    Garante altura O(log n) através de balanceamento por cores e rotações.
    """

    def __init__(self):
        # Nó sentinela que representa as folhas nulas (sempre preto)
        self.nil = Node(None, color=BLACK)
        self.root = self.nil

    # --- Operações de Rotação ---

    def _left_rotate(self, x):
        """Realiza uma rotação à esquerda em torno do nó x."""
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

    def _right_rotate(self, y):
        """Realiza uma rotação à direita em torno do nó y."""
        x = y.left
        y.left = x.right
        
        if x.right != self.nil:
            x.right.parent = y
            
        x.parent = y.parent
        
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
            
        x.right = y
        y.parent = x

    # --- Inserção ---

    def insert(self, key):
        """
        Insere uma nova chave na árvore e restaura as propriedades rubro-negras.
        """
        new_node = Node(key)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = RED  # Novos nós são sempre rubros

        y = self.nil
        x = self.root

        # Busca a posição de inserção (ABB padrão)
        while x != self.nil:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y

        if y == self.nil:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        # Se for a raiz, basta pintar de preto. Caso contrário, corrigir.
        if new_node.parent == self.nil:
            new_node.color = BLACK
            return

        if new_node.parent.parent == self.nil:
            return

        self._insert_fixup(new_node)

    def _insert_fixup(self, k):
        """Corrige violações das propriedades após a inserção."""
        while k.parent.color == RED:
            if k.parent == k.parent.parent.left:
                uncle = k.parent.parent.right
                
                # Caso 1: Tio é rubro -> Recoloração
                if uncle.color == RED:
                    uncle.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    # Caso 2: Tio é negro, k é filho direito -> Rotação esquerda
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    
                    # Caso 3: Tio é negro, k é filho esquerdo -> Rotação direita
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self._right_rotate(k.parent.parent)
            else:
                # Lógica simétrica quando o pai é filho direito
                uncle = k.parent.parent.left
                
                if uncle.color == RED:
                    uncle.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self._left_rotate(k.parent.parent)
            
            if k == self.root:
                break
        
        self.root.color = BLACK

    # --- Busca ---

    def search(self, key):
        """Retorna o nó com a chave buscada ou None se não encontrar."""
        node = self._search_recursive(self.root, key)
        return node if node != self.nil else None

    def _search_recursive(self, node, key):
        if node == self.nil or key == node.key:
            return node
        
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def contains(self, key):
        """Verifica a existência de uma chave (booleano)."""
        return self.search(key) is not None

    # --- Remoção ---

    def delete(self, key):
        """Remove o nó com a chave especificada, se existir."""
        z = self._search_recursive(self.root, key)
        if z == self.nil:
            return # Chave não encontrada

        y = z
        y_original_color = y.color
        
        if z.left == self.nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == BLACK:
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        """Corrige violações das propriedades após a remoção (trata o 'duplo negro')."""
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == RED:
                    s.color = BLACK
                    x.parent.color = RED
                    self._left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == BLACK and s.right.color == BLACK:
                    s.color = RED
                    x = x.parent
                else:
                    if s.right.color == BLACK:
                        s.left.color = BLACK
                        s.color = RED
                        self._right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.right.color = BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == RED:
                    s.color = BLACK
                    x.parent.color = RED
                    self._right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == BLACK and s.left.color == BLACK:
                    s.color = RED
                    x = x.parent
                else:
                    if s.left.color == BLACK:
                        s.right.color = BLACK
                        s.color = RED
                        self._left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.left.color = BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

    def _transplant(self, u, v):
        """Auxiliar para substituir o subárvore de u pela de v."""
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    # --- Auxiliares de Depuração e Visualização ---

    def inorder(self):
        """Retorna uma lista com as chaves em ordem crescente."""
        keys = []
        self._inorder_recursive(self.root, keys)
        return keys

    def _inorder_recursive(self, node, keys):
        if node != self.nil:
            self._inorder_recursive(node.left, keys)
            keys.append(node.key)
            self._inorder_recursive(node.right, keys)

    def print_tree(self):
        """Imprime a estrutura da árvore de forma hierárquica."""
        self._print_helper(self.root, "", True)

    def _print_helper(self, node, indent, last):
        if node != self.nil:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            color = "RED" if node.color == RED else "BLACK"
            print(f"{node.key} ({color})")
            self._print_helper(node.left, indent, False)
            self._print_helper(node.right, indent, True)

    def validate_properties(self):
        """Verifica se a árvore respeita todas as regras rubro-negras."""
        if self.root == self.nil:
            return True
        
        # Propriedade: Raiz deve ser negra
        if self.root.color != BLACK:
            return False, "Raiz não é negra."

        # Propriedade: Sem nós rubros consecutivos e Altura Negra consistente
        try:
            self._check_node_properties(self.root)
            return True, "Todas as propriedades validadas."
        except Exception as e:
            return False, str(e)

    def _check_node_properties(self, node):
        """Retorna a altura negra do caminho se for válido."""
        if node == self.nil:
            return 1

        # Sem dois rubros consecutivos
        if node.color == RED:
            if node.left.color == RED or node.right.color == RED:
                raise Exception(f"Violação rubro-rubro no nó {node.key}")

        left_bh = self._check_node_properties(node.left)
        right_bh = self._check_node_properties(node.right)

        # Altura negra deve ser igual para ambos os lados
        if left_bh != right_bh:
            raise Exception(f"Alturas negras divergentes no nó {node.key}")

        return left_bh + (1 if node.color == BLACK else 0)


# --- Bloco de Testes ---

if __name__ == "__main__":
    rbt = RedBlackTree()

    print("=== Teste de Inserção: Sequência 1 (9, 8, 7, 6, 1, 2, 3, 4, 5) ===")
    for k in [9, 8, 7, 6, 1, 2, 3, 4, 5]:
        rbt.insert(k)
    
    rbt.print_tree()
    valid, msg = rbt.validate_properties()
    print(f"Status: {msg} | Inorder: {rbt.inorder()}\n")

    print("=== Teste de Inserção: Sequência 2 (4, 7, 12, 15, 3, 5, 14, 18) ===")
    # Nota: Algumas chaves já existem, a estrutura de ABB lida com duplicatas à direita
    rbt2 = RedBlackTree()
    for k in [4, 7, 12, 15, 3, 5, 14, 18]:
        rbt2.insert(k)
    
    rbt2.print_tree()
    valid, msg = rbt2.validate_properties()
    print(f"Status: {msg}\n")

    print("=== Teste de Busca ===")
    for search_key in [15, 100]:
        found = rbt2.search(search_key)
        print(f"Chave {search_key} encontrada? {'Sim' if found else 'Não'}")

    print("\n=== Teste de Remoção ===")
    # Removendo uma folha
    print("Removendo 18 (Folha):")
    rbt2.delete(18)
    rbt2.print_tree()

    # Removendo nó com um filho
    print("\nRemovendo 15 (Um filho):")
    rbt2.delete(15)
    rbt2.print_tree()

    # Removendo nó com dois filhos (ex: a raiz ou nó interno)
    print("\nRemovendo 7 (Dois filhos):")
    rbt2.delete(7)
    rbt2.print_tree()

    valid, msg = rbt2.validate_properties()
    print(f"\nStatus Final: {msg}")
    print(f"Inorder Final: {rbt2.inorder()}")