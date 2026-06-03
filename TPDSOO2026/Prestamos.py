from datetime import date, timedelta
from Socio import socio
from Material import material

class Prestamo:
    # cantidad de dias para prestar
    DIAS_PLAZO = 14
    
    def __init__(self, socio, material):
        self.socio = socio
        self.material = material
        self.fecha_salida = date.today()
        self.fecha_vencimiento = date.today() + timedelta(dias=self.DIAS_PLAZO)
        self.fecha_devolucion_real = None

        # El material deja de estar disponible en el momento del préstamo
        self.material.disponible = False
        # Se registra en el historial personal del socio
        self.socio.historial_prestamos.append(self)

    #True si el plazo esta vencido y no se devolvio el material
    def esta_vencido(self) -> bool:
        return self.fecha_devolucion_real is None and date.today() > self.fecha_vencimiento

    #Cierra el préstamo y libera el material
    def registrar_devolucion(self):
        self.fecha_devolucion_real = date.today()
        self.material.disponible = True

    def __str__(self):
        if self.fecha_devolucion_real:
            estado = f"Devuelto el {self.fecha_devolucion_real}"
        elif self.esta_vencido():
            dias = (date.today() - self.fecha_vencimiento).days
            estado = f"VENCIDO hace {dias} día(s)"
        else:
            estado = f"Activo — vence el {self.fecha_vencimiento}"

        return f"'{self.material.titulo}' prestado a {self.socio.nombre} | {estado}"
