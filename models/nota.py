from datetime import datetime


class Nota:
    """Representa una nota del sistema."""

    def __init__(self, nombre, contenido, fecha_creacion=None):
        self.nombre = nombre.strip()
        self.contenido = contenido.strip()
        self.fecha_creacion = fecha_creacion or datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def to_dict(self):
        """Convierte la nota en un diccionario."""
        return {
            "nombre": self.nombre,
            "contenido": self.contenido,
            "fecha_creacion": self.fecha_creacion,
        }

    @classmethod
    def from_dict(cls, data):
        """Crea una nota a partir de un diccionario."""
        return cls(
            data["nombre"],
            data["contenido"],
            data.get("fecha_creacion"),
        )

    def __str__(self):
        """Representación legible de la nota."""
        return f"{self.nombre} ({self.fecha_creacion})"
