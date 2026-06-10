from abc import ABC, abstractmethod
# Clase madre abstracta

class Material(ABC):
    contador = 0

    def __init__(self, titulo):
        Material.contador += 1 
        self.id = Material.contador
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
    
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo)
        self.autor = autor
        self.paginas = paginas


    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[Libro] [Codigo: {self.id}] 'Titúlo: {self.titulo}' -Autor: {self.autor} ({self.paginas} pág.) —Estado: {estado}"


class Revista(Material):

    def __init__(self,titulo, edicion):
        super().__init__(titulo)
        self.edicion = edicion

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[Revista] [Codigo: {self.id}] 'Titúlo: {self.titulo}' (Ed. {self.edicion}) — Estado: {estado}"