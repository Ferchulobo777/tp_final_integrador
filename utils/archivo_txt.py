# Importamos datetime para agregar fecha y hora al reporte
from datetime import datetime

# Importamos os para manejar rutas y crear directorios si no existen
import os

# ---------------------------------------------------------------------------- #
#               Función para generar el reporte en un archivo TXT              #
# ---------------------------------------------------------------------------- #

def generar_reporte_txt(nombre_archivo, titulo, datos, campos, umbral=None):
    try:
        # Crear el directorio del archivo si no existe
        os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)
        
        # Abrimos el archivo en modo escritura con codificación UTF-8
        with open(nombre_archivo, 'w', encoding="UTF-8") as archivo:

            # Escribimos el encabezado decorativo
            archivo.write(f"{'='*60}\n")
            archivo.write(f"{titulo.center(60)}\n")  # Centra el título en 60 caracteres
            archivo.write(f"{'='*60}\n\n")
            
            # Si se especificó un umbral de stock, lo mostramos
            if umbral is not None:
                archivo.write(f"Umbral de stock: ≤ {umbral} unidades\n\n")
            
            # Escribimos la cabecera de la tabla (los nombres de los campos en mayúsculas)
            archivo.write("\t".join(campo.upper() for campo in campos) + "\n")
            archivo.write("-"*60 + "\n")
            
            # Escribimos los datos de cada producto en el reporte
            for producto in datos:
                # Para cada producto, extraemos los valores de los campos indicados
                linea = "\t".join(str(producto.get(campo, '')) for campo in campos)
                archivo.write(f"{linea}\n")
            
            # Escribimos un resumen al final del reporte
            archivo.write(f"\nTotal de productos: {len(datos)}\n")
            archivo.write(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Si todo salió bien, devolvemos True
        return True

    # Si ocurre un error de permisos, lo informamos
    except PermissionError:
        print("Error: No tiene permisos para escribir en el directorio.")
        return False

    # Si ocurre cualquier otro error, también lo mostramos
    except Exception as e:
        print(f"Error inesperado al generar reporte: {str(e)}")
        return False
