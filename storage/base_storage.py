from abc import ABC, abstractmethod


class BaseStorage(ABC):
    """Contrato base para los tipos de almacenamiento."""

    @abstractmethod
    def guardar_nota(self, nota):
        """Guarda una nota."""
        raise NotImplementedError

    @abstractmethod
    def leer_nota(self, nombre):
        """Recupera una nota por nombre."""
        raise NotImplementedError

    @abstractmethod
    def listar_notas(self):
        """Lista las notas disponibles."""
        raise NotImplementedError

    @abstractmethod
    def eliminar_nota(self, nombre):
        """Elimina una nota."""
        raise NotImplementedError

    @abstractmethod
    def buscar_notas(self, clave):
        """Busca notas por palabra clave."""
        raise NotImplementedError

    @abstractmethod
    def editar_nota(self, nombre, nuevo_contenido):
        """Edita una nota existente."""
        raise NotImplementedError
