from models.nota import Nota
from storage.json_storage import JSONStorage
from storage.pickle_storage import PickleStorage
from storage.txt_storage import TXTStorage


class NotaController:
    """Coordina la lógica del sistema de notas."""

    def __init__(self, storage, view):
        self.storage = storage
        self.view = view

    def ejecutar(self):
        self.ejecutar_opciones_storage()

        while True:
            self.view.mostrar_menu()
            opcion = self.view.solicitar_opcion()

            if opcion == "1":
                self.crear_nota()

            elif opcion == "2":
                self.leer_nota()

            elif opcion == "3":
                self.listar_notas()

            elif opcion == "4":
                self.buscar_notas()

            elif opcion == "5":
                self.editar_nota()

            elif opcion == "6":
                self.eliminar_nota()

            elif opcion == "7":
                self.ejecutar_opciones_storage()
            else:
                self.view.mostrar_mensaje("Opción no válida.")

    def ejecutar_opciones_storage(self):
        while True:
            self.view.seleccionar_storage()
            opcion = self.view.solicitar_opcion_almacenamiento()

            if opcion == "1":
                self.storage = TXTStorage()
                self.view.mostrar_mensaje(
                    "Almacenamiento TXT seleccionado."
                )
                break

            elif opcion == "2":
                self.storage = JSONStorage()
                self.view.mostrar_mensaje(
                    "Almacenamiento JSON seleccionado."
                )
                break

            elif opcion == "3":
                self.storage = PickleStorage()
                self.view.mostrar_mensaje(
                    "Almacenamiento Pickle seleccionado."
                )
                break
            elif opcion == "4":
                self.view.mostrar_mensaje("Saliendo del programa.")
                exit()

            else:
                self.view.mostrar_mensaje("Opción no válida.")

    def crear_nota(self):
        """Crea una nueva nota."""
        nombre = self.view.solicitar_nombre()
        contenido = self.view.solicitar_contenido()

        if not nombre:
            self.view.mostrar_mensaje("El nombre no puede estar vacío.")
            return

        if not contenido:
            self.view.mostrar_mensaje("El contenido no puede estar vacío.")
            return

        try:
            nota = Nota(nombre, contenido)
            self.storage.guardar_nota(nota)
            self.view.mostrar_mensaje("Nota creada correctamente.")
        except ValueError as error:
            self.view.mostrar_mensaje(str(error))

    def leer_nota(self):
        """Lee una nota existente."""
        nombre = self.view.solicitar_nombre()
        contenido = self.storage.leer_nota(nombre)

        if contenido is None:
            self.view.mostrar_mensaje("La nota no existe.")
            return

        self.view.mostrar_contenido_nota(contenido)

    def listar_notas(self):
        """Lista las notas disponibles."""
        notas = self.storage.listar_notas()
        self.view.mostrar_notas(notas)

    def buscar_notas(self):
        """Busca una palabra dentro de las notas."""
        clave = self.view.solicitar_palabra_clave()

        if not clave:
            self.view.mostrar_mensaje(
                "Debe ingresar una palabra clave válida."
            )
            return

        encontrados = self.storage.buscar_notas(clave)

        if encontrados:
            self.view.mostrar_mensaje("\nLa palabra fue encontrada en:")
            self.view.mostrar_notas(encontrados)
        else:
            self.view.mostrar_mensaje("No se encontraron coincidencias.")

    def editar_nota(self):
        """Edita una nota existente."""
        nombre = self.view.solicitar_nombre()
        nuevo_contenido = self.view.solicitar_contenido()

        if not nuevo_contenido:
            self.view.mostrar_mensaje(
                "El nuevo contenido no puede estar vacío."
            )
            return

        try:
            self.storage.editar_nota(nombre, nuevo_contenido)
            self.view.mostrar_mensaje("Nota actualizada correctamente.")
        except FileNotFoundError as error:
            self.view.mostrar_mensaje(str(error))

    def eliminar_nota(self):
        """Elimina una nota existente."""
        nombre = self.view.solicitar_nombre()

        try:
            if self.view.confirmar_eliminacion():
                self.storage.eliminar_nota(nombre)
                self.view.mostrar_mensaje(
                    "Nota eliminada correctamente."
                )
            else:
                self.view.mostrar_mensaje("Operación cancelada.")
        except FileNotFoundError as error:
            self.view.mostrar_mensaje(str(error))