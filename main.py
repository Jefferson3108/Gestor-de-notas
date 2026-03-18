from controllers.nota_controller import NotaController
from storage.json_storage import JSONStorage
from storage.txt_storage import TXTStorage
from views.nota_view import NotaView


def seleccionar_storage():
    """Permite seleccionar el tipo de almacenamiento."""
    print("Seleccione el tipo de almacenamiento:")
    print("1. Archivos de texto")
    print("2. JSON")

    opcion = input("Opción: ").strip()

    if opcion == "2":
        return JSONStorage()

    return TXTStorage()


def main():
    """Punto de entrada del programa."""
    storage = seleccionar_storage()
    view = NotaView()
    controller = NotaController(storage, view)
    controller.ejecutar()


if __name__ == "__main__":
    main()
