# el socio representa al usuario de una biblioteca

class Socio:
    contador = 0 

    def __init__(self, nombre, dni):
        Socio.contador += 1
        self.numero_socio = Socio.contador
        self.nombre = nombre
        self.dni = dni 
        self.habilitado = True
        self.historial_prestamos = []  # Guarda todos los préstamos que realizó

    def __str__(self):
        estado = "Habilitado" if self.habilitado else "Suspendido"
        return f"Socio N° {self.numero_socio}: |DNI: {self.dni} |Nombre:{self.nombre} |Estado:[{estado}]"
