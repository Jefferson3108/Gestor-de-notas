from storage.json_storage import JSONStorage
from storage.pickle_storage import PickleStorage
from storage.txt_storage import TXTStorage


class NotaView:
    """Gestiona la interacción por consola con el usuario."""

    def mostrar_menu(self):
        """Muestra el menú principal."""
        print("\n--- Gestor de notas MVC ---")
        print("1. Crear nota")
        print("2. Leer nota")
        print("3. Listar notas")
        print("4. Buscar palabra")
        print("5. Editar nota")
        print("6. Eliminar nota")
        print("7. Volver a seleccionar almacenamiento ")
    
    def seleccionar_storage(self):
     """Permite seleccionar el tipo de almacenamiento."""
     print("Seleccione el tipo de almacenamiento:")
     print("1. Archivos de texto")
     print("2. JSON")
     print("3. Pickle")
     print("4. Salir")
     
    def solicitar_opcion_almacenamiento(self):
        """Solicita una opción de almacenamiento al usuario."""
        return input("Seleccione una opción: ").strip()
    
    def solicitar_opcion(self):
        """Solicita una opción al usuario."""
        return input("Seleccione una opción: ").strip()

    def solicitar_nombre(self):
        """Solicita el nombre de una nota."""
        return input("Nombre de la nota: ").strip()

    def solicitar_contenido(self):
        """Solicita el contenido de una nota."""
        return input("Contenido de la nota: ").strip()

    def solicitar_palabra_clave(self):
        """Solicita una palabra clave."""
        return input("Palabra a buscar: ").strip()

    def mostrar_mensaje(self, mensaje):
        """Muestra un mensaje general."""
        print(mensaje)

    def mostrar_notas(self, notas):
        """Muestra una lista de notas."""
        if not notas:
            print("No hay notas registradas.")
            return

        print("\nNotas disponibles:")
        for nota in notas:
            print(f" - {nota}")

    def mostrar_contenido_nota(self, contenido):
        """Muestra el contenido de una nota."""
        print("\nContenido de la nota:\n")
        print(contenido)

    def confirmar_eliminacion(self):
        """Solicita confirmación para eliminar."""
        respuesta = input("¿Confirma la eliminación? (s/n): ").strip().lower()
        return respuesta == "s"
