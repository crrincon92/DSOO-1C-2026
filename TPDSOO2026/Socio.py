# el socio representa al usuario de una biblioteca

class Socio:

    def __init__(self, numero_socio, nombre):
        self.numero_socio = numero_socio
        self.nombre = nombre
        self.habilitado = True
        self.historial_prestamos = []  # Guarda todos los préstamos que realizó

    def __str__(self):
        estado = "Habilitado" if self.habilitado else "Suspendido"
        return f"Socio N°{self.numero_socio}: {self.nombre} [{estado}]"
