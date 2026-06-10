# 📚 Sistema de Gestión de Biblioteca

Proyecto orientado a objetos desarrollado en Python para la gestión de materiales, socios y préstamos de una biblioteca.

---

## 🗂 Estructura del proyecto

```
├── main.py          # Punto de entrada. Menú interactivo por consola
├── biblioteca.py    # Clase principal que administra el sistema
├── material.py      # Clase abstracta Material y subclases Libro, Revista
├── socio.py         # Clase Socio
├── prestamos.py     # Clase Prestamo
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.10 o superior
- No requiere librerías externas

---

## ▶️ Ejecución

```bash
python main.py
```

---

## 🧱 Clases principales

### `Material` *(abstracta)*
Clase base para todos los materiales del catálogo. Implementa ID autoincremental compartido entre todas las subclases.

| Atributo | Descripción |
|---|---|
| `id` | Identificador único autoincremental |
| `titulo` | Título del material |
| `disponible` | Estado de disponibilidad (`True` / `False`) |

**Subclases:**
- `Libro`: agrega `autor` y `paginas`
- `Revista`: agrega `edicion`

---

### `Socio`
Representa a un usuario registrado en la biblioteca. También implementa número de socio autoincremental.

| Atributo | Descripción |
|---|---|
| `numero_socio` | Identificador único autoincremental |
| `nombre` | Nombre completo |
| `dni` | Documento de identidad |
| `habilitado` | Si puede realizar préstamos |
| `historial_prestamos` | Lista de todos sus préstamos |

---

### `Prestamo`
Registra el vínculo entre un socio y un material. Al crearse, marca el material como no disponible y se agrega al historial del socio.

| Atributo | Descripción |
|---|---|
| `fecha_salida` | Fecha en que se realizó el préstamo |
| `fecha_vencimiento` | 14 días después de la fecha de salida |
| `fecha_devolucion_real` | `None` si aún no fue devuelto |

---

### `Biblioteca`
Administra el catálogo, los socios y los préstamos.

| Método | Descripción |
|---|---|
| `agregar_material(material)` | Agrega un libro o revista al catálogo |
| `registrar_socio(socio)` | Registra un nuevo socio |
| `prestar_material(numero_socio, id_material)` | Registra un préstamo |
| `devolver_material(id_material)` | Registra la devolución de un material |
| `buscar_materiales(criterio)` | Busca por título, autor o tipo |
| `prestamos_activos()` | Lista préstamos sin devolver |
| `prestamos_vencidos()` | Lista préstamos fuera de plazo |
| `mostrar_catalogo()` | Imprime todos los materiales |
| `mostrar_socios()` | Imprime todos los socios registrados |

---

## 📋 Menú del sistema

```
 1. Agregar Libro
 2. Agregar Revista
 3. Registrar Socio
 4. Ver catálogo completo
 5. Buscar material
 6. Registrar préstamo
 7. Registrar devolución
 8. Ver préstamos activos
 9. Ver préstamos vencidos
10. Ver historial de un socio
11. Ver socios registrados
 0. Salir
```

---

## 🧩 Conceptos de POO aplicados

- **Abstracción**: `Material` es una clase abstracta con el método `__str__` obligatorio para todas las subclases
- **Herencia**: `Libro` y `Revista` heredan de `Material`
- **Encapsulamiento**: cada clase gestiona su propio estado interno
- **Polimorfismo**: cada subclase implementa su propia versión de `__str__`

---

## 👥 Autores

Proyecto desarrollado para la materia **Desarrollo de Software Orientado a Objetos (DSOO) — 1C 2026**
