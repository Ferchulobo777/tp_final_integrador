# Importamos el módulo json para poder trabajar con archivos en formato JSON
import json

# Importamos una función para mostrar mensajes de error con estilo
from style.estilos import mostrar_error

# --------------------------------------------------------------------------- #
# Función: cargar_datos                                                       #
# Descripción: Carga los datos desde un archivo JSON y los devuelve como una #
# lista de diccionarios. Si el archivo no existe o está mal formado,         #
# devuelve una lista vacía.                                                  #
# --------------------------------------------------------------------------- #
def cargar_datos(ruta):
    try:
        # Abrimos el archivo en modo lectura con codificación UTF-8
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)  # Cargamos y devolvemos el contenido en formato lista/dict
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o tiene un formato inválido, devolvemos una lista vacía
        return []

# --------------------------------------------------------------------------- #
# Función: guardar_datos                                                      #
# Descripción: Guarda los datos en un archivo JSON, recibiendo la ruta y     #
# los datos (lista o diccionario). Si ocurre un error, lo muestra con estilo.#
# --------------------------------------------------------------------------- #
def guardar_datos(ruta, datos):
    try:
        # Abrimos el archivo en modo escritura con codificación UTF-8
        with open(ruta, "w", encoding="utf-8") as archivo:
            # Guardamos los datos con indentación para que sea legible
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        # Si ocurre un error inesperado, lo mostramos por consola
        mostrar_error(f"❌ Error al guardar los datos: {e}")
