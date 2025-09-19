Código inicial (¡NO LO MODIFIQUES DIRECTAMENTE!)
                
# Este código viola S.O.L.I.D. a propósito
import datetime

class Biblioteca:
    def __init__(self):
        self.inventario = {} # Diccionario para almacenar libros
        self.prestamos_activos = {} # {id_libro: usuario}

    # Funcionalidades de INVENTARIO (Viola S - SRP)
    def agregar_libro(self, id_libro, titulo):
        if id_libro not in self.inventario:
            self.inventario[id_libro] = {"titulo": titulo, "disponible": True}
            print(f"Libro '{titulo}' agregado.")
        else:
            print(f"El libro con ID {id_libro} ya existe.")

    def eliminar_libro(self, id_libro):
        if id_libro in self.inventario:
            del self.inventario[id_libro]
            print(f"Libro con ID {id_libro} eliminado.")
        else:
            print(f"Libro con ID {id_libro} no encontrado.")

    # Funcionalidades de PRÉSTAMOS (Viola S - SRP y D - DIP)
    def prestar_libro(self, id_libro, usuario):
        if id_libro in self.inventario and self.inventario[id_libro]["disponible"]:
            self.inventario[id_libro]["disponible"] = False
            self.prestamos_activos[id_libro] = usuario
            self.registrar_evento_en_archivo(f"Préstamo: {usuario} ha prestado el libro {self.inventario[id_libro]['titulo']}")
            self.enviar_notificacion_por_email(usuario, "Has prestado un libro.")
            print(f"Libro prestado a {usuario}.")
        else:
            print("El libro no está disponible o no existe.")

    def devolver_libro(self, id_libro):
        if id_libro in self.prestamos_activos:
            usuario = self.prestamos_activos.pop(id_libro)
            self.inventario[id_libro]["disponible"] = True
            self.registrar_evento_en_archivo(f"Devolución: {usuario} ha devuelto el libro {self.inventario[id_libro]['titulo']}")
            print(f"Libro devuelto por {usuario}.")
        else:
            print("Este libro no estaba prestado.")
            
    # Funcionalidades de NOTIFICACIÓN (Viola I - ISP y O - OCP)
    def enviar_notificacion_por_email(self, destinatario, mensaje):
        # Lógica para enviar un email
        print(f"Notificación por email a {destinatario}: {mensaje}")

    def enviar_notificacion_por_sms(self, destinatario, mensaje):
        print("Enviando SMS...")
        raise NotImplementedError("La funcionalidad de SMS no está implementada aún.")
        
    # Funcionalidades de REGISTRO (Viola S - SRP y D - DIP)
    def registrar_evento_en_archivo(self, evento):
        # Lógica para escribir en un archivo de texto
        with open("log_biblioteca.txt", "a") as f:
            f.write(f"[{datetime.datetime.now()}] {evento}\n")
        print("Evento registrado en el archivo log_biblioteca.txt")