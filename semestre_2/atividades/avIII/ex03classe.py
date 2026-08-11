class Livro:
    titulo : str
    paginas: int
    
    def __init__(self, titulo = '', paginas = 0):
        self.titulo = titulo
        self.paginas = paginas