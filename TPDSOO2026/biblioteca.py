from material import Material, Libro
from socio import Socio
from prestamos import Prestamo

# esta va a ser la clase que administra todo 
class Biblioteca:


    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = {}   # { codigo: Material }
        self.socios = {}     # { numero_socio: Socio }
        self.prestamos = []  # Lista de todos los préstamos (activos e históricos)

    # ---------- Altas ----------

    def agregar_material(self, material: Material) -> bool:
        if material.id in self.catalogo:
            print(f"Ya existe un material con el código '{material.id}'.")
            return False
        self.catalogo[material.id] = material
        print(f"Material agregado: {material}")
        return True

    def registrar_socio(self, socio: Socio) -> bool:
        if socio.numero_socio in self.socios:
            print(f"Ya existe un socio con el número '{socio.numero_socio}'.")
            return False
        self.socios[socio.numero_socio] = socio
        print(f"Socio registrado: {socio}")
        return True

    # ---------- Préstamos y devoluciones ----------

    def prestar_material(self, numero_socio, id_material) -> bool:
        socio = self.socios.get(numero_socio)
        material = self.catalogo.get(id_material)

        if not socio:
            print("Socio no encontrado.")
            return False
        if not socio.habilitado:
            print(f"{socio.nombre} no está habilitado para realizar préstamos.")
            return False
        if not material:
            print("Material no encontrado en el catálogo.")
            return False
        if not material.disponible:
            print(f"'{material.titulo}' ya está prestado en este momento.")
            return False

        nuevo_prestamo = Prestamo(socio, material)
        self.prestamos.append(nuevo_prestamo)
        print(f"Préstamo registrado. Fecha de devolución: {nuevo_prestamo.fecha_vencimiento}")
        return True

    def devolver_material(self, id_material) -> bool:
        material = self.catalogo.get(id_material)

        if not material:
            print("Código de material no encontrado.")
            return False
        if material.disponible:
            print("Ese material ya figura como disponible, no tiene préstamo activo.")
            return False

        # Buscar el préstamo activo de ese material
        prestamo_activo = next(
            (p for p in self.prestamos if p.material.id == id_material and p.fecha_devolucion_real is None),
            None
        )

        if prestamo_activo:
            prestamo_activo.registrar_devolucion()
            print(f"Devolución registrada. '{material.titulo}' vuelve al catálogo.")
            return True

        return False

    # ---------- Consultas ----------

    #Busca en el catálogo por título, autor o tipo.
    #La búsqueda no distingue mayúsculas/minúsculas (Para evitar ese Error unificamos el con LOWER).
        
    def buscar_materiales(self, criterio) -> list:

        criterio = criterio.lower().strip()
        resultados = []
        for m in self.catalogo.values():
            coincide_titulo = criterio in m.titulo.lower()
            coincide_tipo   = criterio == m.tipo.lower()
            coincide_autor  = isinstance(m, Libro) and criterio in m.autor.lower()

            if coincide_titulo or coincide_tipo or coincide_autor:
                resultados.append(m)
        return resultados

    def prestamos_activos(self) -> list:
        return [p for p in self.prestamos if p.fecha_devolucion_real is None]

    def prestamos_vencidos(self) -> list:
        return [p for p in self.prestamos if p.esta_vencido()]

    # ---------- Visualización ----------

    def mostrar_catalogo(self):
        print(f"\n  Catálogo — {self.nombre} ({len(self.catalogo)} items)")
        if not self.catalogo:
            print("  El catálogo está vacío.")
            return
        for m in self.catalogo.values():
            print(f"  • {m}")

    def mostrar_socios(self):
        print(f"\n  Socios registrados ({len(self.socios)})")
        if not self.socios:
            print("  No hay socios registrados.")
            return
        for s in self.socios.values():
            print(f"  • {s}")
