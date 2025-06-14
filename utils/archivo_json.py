import json
from style.estilos import mostrar_error

def cargar_datos(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
        
def guardar_datos(ruta, datos):
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        mostrar_error(f"❌ error al guardar los datos {e}")      