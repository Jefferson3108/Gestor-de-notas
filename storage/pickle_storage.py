import os
import pickle
from storage.base_storage import BaseStorage
class PickleStorage(BaseStorage):
    """Persistencia de notas utilizando pickle."""

    def __init__(self, archivo="data/notas.pkl"):
        self.archivo = archivo
        os.makedirs(os.path.dirname(self.archivo), exist_ok=True)
        if not os.path.exists(self.archivo):
            with open(self.archivo, "wb") as archivo:
                pickle.dump({}, archivo, protocol=pickle.HIGHEST_PROTOCOL)

    def _cargar_notas(self):
        """Carga todas las notas desde el archivo pickle."""
        with open(self.archivo, "rb") as archivo:
            return pickle.load(archivo)

    def guardar_nota(self, nota):
        """Guarda una nota en un archivo pickle."""
        notas = self._cargar_notas()
        if nota.nombre in notas:
            raise ValueError("Ya existe una nota con ese nombre.")
        notas[nota.nombre] = {
            "fecha_creacion": nota.fecha_creacion,
            "contenido": nota.contenido
        }
        with open(self.archivo, "wb") as archivo:
            pickle.dump(notas, archivo)
    
    def guardar_notas_adicionales(self, nota):
        """Guarda una nota en un archivo pickle."""
        notas = self._cargar_notas()
        if nota.nombre in notas:
            raise ValueError("Ya existe una nota con ese nombre.")
        notas[nota.nombre] = {
            "fecha_creacion": nota.fecha_creacion,
            "contenido": nota.contenido
        }
        with open(self.archivo, "ab") as archivo:
            pickle.dump(notas, archivo, protocol=pickle.HIGHEST_PROTOCOL)


    def leer_nota(self, nombre):
        """Lee una nota desde un archivo pickle."""
        notas = self._cargar_notas()
        return notas.get(nombre)

    def listar_notas(self):
        """Lista los nombres de las notas almacenadas."""
        notas = self._cargar_notas()
        return sorted(notas.keys())

    def eliminar_nota(self, nombre):
        """Elimina una nota existente."""
        notas = self._cargar_notas()
        if nombre not in notas:
            raise FileNotFoundError("La nota no existe.")
        del notas[nombre]
        with open(self.archivo, "wb") as archivo:
            pickle.dump(notas, archivo)

    def buscar_notas(self, clave):
        """Busca una palabra dentro de las notas."""
        encontrados = []
        notas = self._cargar_notas()
        for nombre, datos in notas.items():
            if clave.lower() in datos["contenido"].lower():
                encontrados.append(nombre)
        return encontrados

    def editar_nota(self, nombre, nuevo_contenido):
        """Edita el contenido de una nota existente."""
        notas = self._cargar_notas()
        if nombre not in notas:
            raise FileNotFoundError("La nota no existe.")
        notas[nombre]["contenido"] = nuevo_contenido
        with open(self.archivo, "wb") as archivo:
            pickle.dump(notas, archivo)
        


    
    
   