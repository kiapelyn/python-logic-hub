from ex03classe import Livro

# mesma coisa do 2

livros = [Livro('Macunaíma', 340),
          Livro('Divina Comédia', 1280),
          Livro('Os Miseráveis', 853),
          Livro('Ensaio sobre a Segueira', 420),
          Livro('Amor e Gelato', 314)]


def insercao(x):
    n = len(x)
    for j in range(1, n):
        valor = x[j].paginas
        i = j - 1
        while i >= 0 and valor < x[i].paginas:
            x[i + 1].paginas = x[i].paginas
            i -= 1
        x[i + 1].paginas = valor
            
insercao(livros)

for i in livros:
        print(f'{i.paginas}')
    