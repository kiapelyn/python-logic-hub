class Musica:
    codi: int
    titulo: str
    artista: str
    duracao_seg: int
    
    def __init__(self, codi, titulo = '', artista = '', duracao_seg=0.0):
        self.codi = codi
        self.titulo = titulo
        self.artista = artista
        self.duracao_seg = duracao_seg