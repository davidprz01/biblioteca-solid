# Clase Libro
class Libro:
    def __init__(self, id_libro: str, titulo: str, autor: str):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # Por defecto siempre disponible


# Clase Revista
class Revista:
    def __init__(self, id_revista: str, titulo: str, numero: int):
        self.id = id_revista
        self.titulo = titulo
        self.numero = numero
        self.disponible = True  # Por defecto siempre disponible


# Clase Gestor de Inventario
class GestorDeInventario:
    def __init__(self):
        self.items = {}  # Guardará los libros y revistas por su ID

    def agregar_item(self, item) -> bool:
        if item.id in self.items:
            print(f"Ya existe un item con el id {item.id}")
            return False
        self.items[item.id] = item
        print(f"Item '{item.titulo}' agregado correctamente.")
        return True

    def eliminar_item(self, id_item: str) -> bool:
        if id_item not in self.items:
            print("El item no existe.")
            return False

        item = self.items[id_item]
        if not item.disponible:
            print("No se puede eliminar porque está prestado.")
            return False

        del self.items[id_item]
        print(f"Item con id {id_item} eliminado.")
        return True

    def prestar_item(self, id_item: str) -> bool:
        if id_item not in self.items:
            print("El item no existe.")
            return False

        item = self.items[id_item]
        if not item.disponible:
            print("El item ya está prestado.")
            return False

        item.disponible = False
        print(f"El item '{item.titulo}' ha sido prestado.")
        return True

    def devolver_item(self, id_item: str) -> bool:
        if id_item not in self.items:
            print("El item no existe.")
            return False

        item = self.items[id_item]
        item.disponible = True
        print(f"El item '{item.titulo}' ha sido devuelto y ahora está disponible.")
        return True

    def mostrar_inventario(self):
        if not self.items:
            print("El inventario está vacío.")
            return

        print("Inventario:")
        for id_item, item in self.items.items():
            estado = "Disponible" if item.disponible else "Prestado"
            print(f"{id_item} - {item.titulo} - {estado}")



inventario = GestorDeInventario()

# Crear libro y revista
libro1 = Libro("L001", "Cien Años de Soledad", "Gabriel García Márquez")
revista1 = Revista("R001", "National Geographic", 105)

# Agregar al inventario
inventario.agregar_item(libro1)
inventario.agregar_item(revista1)

# Mostrar inventario
inventario.mostrar_inventario()

# Prestar libro
inventario.prestar_item("L001")
inventario.mostrar_inventario()

# Devolver libro
inventario.devolver_item("L001")
inventario.mostrar_inventario()

# Eliminar revista
inventario.eliminar_item("R001")
inventario.mostrar_inventario()

