import os
import shutil

from models.nota import Nota
from storage.base_storage import BaseStorage


class TXTStorage(BaseStorage):
    """Persistencia de notas en archivos de texto."""

    def __init__(self, carpeta="data/notas_txt"):
        self.carpeta = carpeta
        os.makedirs(self.carpeta, exist_ok=True)

    def _ruta_nota(self, nombre):
        """Construye la ruta completa de la nota."""
        return os.path.join(self.carpeta, f"{nombre}.txt")

    def guardar_nota(self, nota):
        """Guarda una nota en un archivo de texto."""
        ruta = self._ruta_nota(nota.nombre)

        if os.path.exists(ruta):
            raise ValueError("Ya existe una nota con ese nombre.")

        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(f"Fecha de creación: {nota.fecha_creacion}\n")
            archivo.write("-" * 40 + "\n")
            archivo.write(nota.contenido)

    def leer_nota(self, nombre):
        """Lee una nota desde un archivo de texto."""
        ruta = self._ruta_nota(nombre)

        if not os.path.exists(ruta):
            return None

        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        return contenido

    def listar_notas(self):
        """Lista los nombres de las notas almacenadas."""
        archivos = os.listdir(self.carpeta)
        notas = [archivo[:-4] for archivo in archivos if archivo.endswith(".txt")]
        return sorted(notas)

    def eliminar_nota(self, nombre):
        """Elimina una nota existente."""
        ruta = self._ruta_nota(nombre)

        if not os.path.exists(ruta):
            raise FileNotFoundError("La nota no existe.")

        os.remove(ruta)

    def buscar_notas(self, clave):
        """Busca una palabra dentro de las notas."""
        encontrados = []

        for nombre in self.listar_notas():
            contenido = self.leer_nota(nombre)
            if contenido and clave.lower() in contenido.lower():
                encontrados.append(nombre)

        return encontrados

    def editar_nota(self, nombre, nuevo_contenido):
        """Edita una nota existente y crea un respaldo."""
        ruta = self._ruta_nota(nombre)

        if not os.path.exists(ruta):
            raise FileNotFoundError("La nota no existe.")

        respaldo = os.path.join(self.carpeta, f"{nombre}_bak.txt")
        shutil.copy(ruta, respaldo)

        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(nuevo_contenido)
