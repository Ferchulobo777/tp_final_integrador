from datetime import datetime
import os

# ---------------------------------------------------------------------------- #
#               Función para generar el reporte en un archivo TXT              #
# ---------------------------------------------------------------------------- #

def generar_reporte_txt(nombre_archivo, titulo, datos, campos, umbral=None):
    try:
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)
        
        with open(nombre_archivo, 'w', encoding="UTF-8") as archivo:
            # Encabezado del reporte
            archivo.write(f"{'='*60}\n")
            archivo.write(f"{titulo.center(60)}\n")
            archivo.write(f"{'='*60}\n\n")
            
            if umbral is not None:
                archivo.write(f"Umbral de stock: ≤ {umbral} unidades\n\n")
            
            # Cabecera de la tabla
            archivo.write("\t".join(campo.upper() for campo in campos) + "\n")
            archivo.write("-"*60 + "\n")
            
            # Datos del reporte
            for producto in datos:
                linea = "\t".join(str(producto.get(campo, '')) for campo in campos)
                archivo.write(f"{linea}\n")
            
            # Pie del reporte
            archivo.write(f"\nTotal de productos: {len(datos)}\n")
            archivo.write(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        return True
    
    except PermissionError:
        print("Error: No tiene permisos para escribir en el directorio.")
        return False
    except Exception as e:
        print(f"Error inesperado al generar reporte: {str(e)}")
        return False
        