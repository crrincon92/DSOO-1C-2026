from abc import ABC, abstractmethod
# Clase madre abstracta

class Material(ABC):
    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo
        self.disponible = True

    # va a devolver el nombre de la clase    
    def tipo(self) -> str:
        return self.__class__.__name__
    
    #decorador que define que cada subclase este obligada a usarlo
    @abstractmethod 
    def __str__(self) -> str:
        pass

class Libro(Material):
    
    def __init__(self, id, titulo, autor, paginas):
        super().__init__(id, titulo)
        self.autor = autor
        self.paginas = paginas


    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[Libro] [{self.id}] '{self.titulo}' - {self.autor} ({self.paginas} pág.) — {estado}"


class Revista(Material):

    def __init__(self, id, titulo, edicion):
        super().__init__(id, titulo)
        self.edicion = edicion

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[Revista] [{self.id}] '{self.titulo}' (Ed. {self.edicion}) — {estado}"