from abc import ABC

class Material(ABC):
    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo
        self.disponible = True
        
    def esta_disponible(self):
        return self.disponible 

    def marcar_disponible(self):
        self.disponible = True

class libro(Material):
    def __init__(self, id, titulo, autor,isbn):
        super().__init__(id, titulo)
        self.autor = autor
        self.isbn = isbn
        


