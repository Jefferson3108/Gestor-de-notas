import json
import os

from models.nota import Nota
from storage.base_storage import BaseStorage


class JSONStorage(BaseStorage):
    """Persistencia de notas en un archivo JSON."""

    def __init__(self, archivo="data/notas.json"):
        self.archivo = archivo
        os.makedirs(os.path.dirname(self.archivo), exist_ok=True)

        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as file:
                json.dump({}, file, indent=4, ensure_ascii=False)

    def _leer_todo(self):
        """Lee todas las notas del archivo JSON."""
        with open(self.archivo, "r", encoding="utf-8") as file:
            return json.load(file)

    def _guardar_todo(self, data):
        """Guarda el diccionario completo en el archivo JSON."""
        with open(self.archivo, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def guardar_nota(self, nota):
        """Guarda una nueva nota en JSON."""
        data = self._leer_todo()

        if nota.nombre in data:
            raise ValueError("Ya existe una nota con ese nombre.")

        data[nota.nombre] = nota.to_dict()
        self._guardar_todo(data)

    def leer_nota(self, nombre):
        """Lee una nota desde JSON."""
        data = self._leer_todo()

        if nombre not in data:
            return None

        nota = Nota.from_dict(data[nombre])
        return (
            f"Fecha de creación: {nota.fecha_creacion}\n"
            + "-" * 40
            + "\n"
            + nota.contenido
        )

    def listar_notas(self):
        """Lista las notas disponibles en JSON."""
        data = self._leer_todo()
        return sorted(data.keys())

    def eliminar_nota(self, nombre):
        """Elimina una nota del archivo JSON."""
        data = self._leer_todo()

        if nombre not in data:
            raise FileNotFoundError("La nota no existe.")

        del data[nombre]
        self._guardar_todo(data)

    def buscar_notas(self, clave):
        """Busca una palabra dentro de las notas."""
        data = self._leer_todo()
        encontrados = []

        for nombre, nota_data in data.items():
            contenido = nota_data["contenido"]
            if clave.lower() in contenido.lower():
                encontrados.append(nombre)

        return sorted(encontrados)

    def editar_nota(self, nombre, nuevo_contenido):
        """Edita el contenido de una nota en JSON."""
        data = self._leer_todo()

        if nombre not in data:
            raise FileNotFoundError("La nota no existe.")

        data[nombre]["contenido"] = nuevo_contenido.strip()
        self._guardar_todo(data)
