# Gestor de Notas MVC

Proyecto de ejemplo basado en la Guía Académica 5.2 de Programación Avanzada.

El proyecto implementa un gestor de notas con:

- Programación Orientada a Objetos
- estructura MVC
- persistencia desacoplada
- dos tipos de almacenamiento: TXT y JSON

## Estructura del proyecto

```text
gestor_notas_mvc/
|-- main.py
|-- models/
|   `-- nota.py
|-- views/
|   `-- nota_view.py
|-- controllers/
|   `-- nota_controller.py
|-- storage/
|   |-- base_storage.py
|   |-- txt_storage.py
|   `-- json_storage.py
`-- data/
```

## Descripción de los componentes

### models/
Contiene la clase `Nota`, que representa la entidad principal del sistema.

### views/
Contiene la clase `NotaView`, encargada de la interacción por consola con el usuario.

### controllers/
Contiene la clase `NotaController`, que coordina el flujo entre la vista y el almacenamiento.

### storage/
Contiene la abstracción de persistencia y sus implementaciones:

- `BaseStorage`: contrato común
- `TXTStorage`: almacenamiento en archivos `.txt`
- `JSONStorage`: almacenamiento en archivo `.json`
- `PickleStorage`: almacenamiento en archivo `.json`

### data/
Carpeta donde se almacenan los archivos generados por el programa durante la ejecución.

## Requisitos

Este proyecto usa únicamente módulos de la biblioteca estándar de Python.  
No requiere instalar paquetes externos.

Versión recomendada de Python:

```text
Python 3.10 o superior
```

## Archivo requirements.txt

Se incluye un archivo `requirements.txt` por organización del proyecto.  
En este caso no contiene dependencias externas porque todo el código utiliza la biblioteca estándar.

## Ejecución

En la terminal, ubíquese en la carpeta del proyecto y ejecute:

```bash
python main.py
```

## Funcionamiento general

Al iniciar el programa, se solicita seleccionar el tipo de almacenamiento o salir del programa:

- `1`: Archivos de texto
- `2`: JSON
- `3`: Pickle
- `4`: Salir
Luego se muestra un menú con las operaciones disponibles:

- crear nota
- leer nota
- listar notas
- buscar palabra
- editar nota
- eliminar nota
- volver a seleccionar almacenamiento

## Control de cambios

El proyecto fue preparado con un repositorio Git para que el historial de cambios pueda revisarse con:

```bash
git log --oneline
``
