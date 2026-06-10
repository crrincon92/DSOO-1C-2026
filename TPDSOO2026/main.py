# main.py
# Punto de entrada del sistema. Contiene el menú interactivo por consola.

from material import Libro, Revista
from socio import Socio
from biblioteca import Biblioteca


def menu():
    biblioteca = Biblioteca("----Biblioteca DSOO----")
    #Datos de ejemplo para probar el sistema
    biblioteca.agregar_material(Libro( "El Aleph", "Jorge Luis Borges", 150))
    biblioteca.agregar_material(Libro( "Rayuela", "Julio Cortázar", 600))
    biblioteca.agregar_material(Libro( "El principito", "Saint-Exuperí", 110))
    biblioteca.agregar_material(Libro( "Cien años de soledad", "Gabriel García Marquez", 470))
    biblioteca.agregar_material(Libro( "Don Quijote de la Mancha", "Jorge Luis Borges", 1000))
    biblioteca.agregar_material(Revista( "National Geographic", "Marzo 2025"))
    biblioteca.agregar_material(Revista( "Revista Gente", "Abril 2025"))
    biblioteca.agregar_material(Revista( "Revista Caras", "Julio 2025"))
    biblioteca.registrar_socio(Socio( "Ana Gómez", 12345678))
    biblioteca.registrar_socio(Socio( "Carlos Pérez",23456789))
    biblioteca.registrar_socio(Socio( "Juan Pérez",34567891))

    opciones = {
        "1":  "Agregar Libro",
        "2":  "Agregar Revista",
        "3":  "Registrar Socio",
        "4":  "Ver catálogo completo",
        "5":  "Buscar material",
        "6":  "Registrar préstamo",
        "7":  "Registrar devolución",
        "8":  "Ver préstamos activos",
        "9":  "Ver préstamos vencidos",
        "10": "Ver historial de un socio",
        "11": "Ver socios registrados",
        "0":  "Salir",
    }

    while True:
        print(f"\n{'='*46}")
        print(f"  BIBLIOTECA {biblioteca.nombre.upper()}")
        print(f"{'='*46}")
        for k, v in opciones.items():
            print(f"  {k:>2}. {v}")
        print(f"{'='*46}")

        opcion = input("  Opción: ").strip()

        if opcion == "1":
            print("\n  -- Nuevo Libro --")
            titulo = input("  Título: ").strip()
            autor  = input("  Autor: ").strip()
            try:
                paginas = int(input("  Páginas: ").strip())
            except ValueError:
                print("Cantidad de páginas inválida. Se usará 0.")
                paginas = 0
            biblioteca.agregar_material(Libro( titulo, autor, paginas))

        elif opcion == "2":
            print("\n  -- Nueva Revista --")
            titulo  = input("  Título: ").strip()
            edicion = input("  Edición: ").strip()
            biblioteca.agregar_material(Revista(titulo, edicion))

        elif opcion == "3":
            print("\n  -- Nuevo Socio --")
            nombre = input("  Nombre: ").strip()
            dni = input( " ingrese DNI: ").strip()
            biblioteca.registrar_socio(Socio(nombre, dni))

        elif opcion == "4":
            biblioteca.mostrar_catalogo()

        elif opcion == "5":
            criterio = input("\n  Buscar (título, autor o tipo): ").strip()
            resultados = biblioteca.buscar_materiales(criterio)
            if resultados:
                print(f"\n  {len(resultados)} resultado(s):")
                for m in resultados:
                    print(f"  • {m}")
            else:
                print("  No se encontraron coincidencias.")

        elif opcion == "6":
            print("\n  -- Registrar Préstamo --")
            numero_socio    = int(input("  N° de socio: ").strip())
            id_material = int(input("  Código del material: ").strip())
            biblioteca.prestar_material(numero_socio, id_material)

        elif opcion == "7":
            print("\n  -- Registrar Devolución --")
            id_material = int(input("  Código del material: ").strip())
            biblioteca.devolver_material(id_material)

        elif opcion == "8":
            activos = biblioteca.prestamos_activos()
            print(f"\n  Préstamos activos: {len(activos)}")
            if activos:
                for p in activos:
                    print(f"  • {p}")
            else:
                print("  No hay préstamos activos.")

        elif opcion == "9":
            vencidos = biblioteca.prestamos_vencidos()
            print(f"\n  Préstamos vencidos: {len(vencidos)}")
            if vencidos:
                for p in vencidos:
                    print(f"  • {p}")
            else:
                print("  No hay préstamos vencidos.")

        elif opcion == "10":
            numero = int(input("\n  N° de socio: ").strip())
            socio = biblioteca.socios.get(numero)
            if not socio:
                print(" Socio no encontrado.")
            elif not socio.historial_prestamos:
                print(f"  {socio.nombre} no tiene préstamos registrados.")
            else:
                print(f"\n  Historial de {socio.nombre} ({len(socio.historial_prestamos)} préstamo(s)):")
                for p in socio.historial_prestamos:
                    print(f"  • {p}")

        elif opcion == "11":
            biblioteca.mostrar_socios()

        elif opcion == "0":
            print("\n  Hasta luego.\n")
            break

        else:
            print("  Opción no válida.")

# inicio de menú
if __name__ == "__main__":
    menu()