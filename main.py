from controllers.nota_controller import NotaController
from views.nota_view import NotaView





def main():
    """Punto de entrada del programa."""
    view = NotaView()
    controller = NotaController(None, view)
    controller.ejecutar()
    


if __name__ == "__main__":
    main()
