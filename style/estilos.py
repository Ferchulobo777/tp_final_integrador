# Importamos las clases necesarias desde la librería rich
from rich.console import Console         # Para imprimir texto en consola con estilos
from rich.theme import Theme            # Para crear un tema personalizado de colores
from rich.table import Table            # Para crear tablas
from rich.box import ROUNDED, SIMPLE_HEAVY  # Para definir el estilo de los bordes de la tabla

# ---------------------------------------------------------------------------- #
#                               Definimos un tema                              #
# ---------------------------------------------------------------------------- #

# Creamos un tema personalizado con distintos estilos de texto (colores y negrita)
custom_theme = Theme({
    "titulo": "bold cyan",    # Estilo para títulos
    "opcion": "bold green",   # Estilo para opciones del menú
    "error": "bold red",      # Estilo para errores
    "info": "yellow",         # Estilo para mensajes informativos
    "exito": "bold blue",     # Estilo para mensajes de éxito
})

# ---------------------------------------------------------------------------- #
#                        Consola con tema personalizado                        #
# ---------------------------------------------------------------------------- #

# Creamos una consola con el tema que definimos anteriormente
consola = Console(theme=custom_theme)

# ---------------------------------------------------------------------------- #
#                Funciones auxiliares para imprimir por consola                #
# ---------------------------------------------------------------------------- #

# Estas funciones permiten imprimir distintos tipos de mensajes con su estilo correspondiente

def mostrar_titulo(texto):
    consola.print(texto, style="titulo")  # Muestra un título

def mostrar_opcion(texto):
    consola.print(texto, style="opcion")  # Muestra una opción de menú

def mostrar_error(texto):
    consola.print(texto, style="error")   # Muestra un mensaje de error

def mostrar_info(texto):
    consola.print(texto, style="info")    # Muestra información al usuario

def mostrar_exito(texto):
    consola.print(texto, style="exito")   # Muestra un mensaje de éxito

# ---------------------------------------------------------------------------- #
#                   Función para generar tabla menú principal                  #
# ---------------------------------------------------------------------------- #

def generar_tabla():
    # Crea una tabla con título "Menú Principal" y un estilo de borde redondeado
    tabla = Table(title="📋 Menú Principal", box=ROUNDED, style="opcion", expand=False)
    
    # Definimos las columnas: N° (número de opción) y Acción (lo que hace cada opción)
    tabla.add_column("N°", justify="center", style="bold cyan", no_wrap=True)
    tabla.add_column("Acción", justify="left", style="bold green")

    # Lista de opciones del menú
    opciones = [
        ("1", "Agregar Producto"),
        ("2", "Listar Productos"),
        ("3", "Modificar Producto"),
        ("4", "Buscar Producto"),
        ("5", "Eliminar Producto"),
        ("6", "Reporte Bajo de Stock"),
        ("7", "Salir")
    ]

    # Agregamos cada opción como una fila en la tabla
    for numero, descripcion in opciones:
        tabla.add_row(numero, descripcion)

    # Mostramos la tabla en consola
    consola.print(tabla)

# ---------------------------------------------------------------------------- #
#                   Función para generar tabla de productos                    #
# ---------------------------------------------------------------------------- #

def generar_tabla_productos(productos):
    # Si no hay productos, mostramos un mensaje informativo
    if not productos:
        mostrar_info("⚠️ No hay productos cargados ⚠️")
        return

    # Creamos una tabla para mostrar los productos en stock
    tabla = Table(title="📦 Productos en Stock 📦", title_style="bold green")
    
    # Definimos las columnas de la tabla con sus estilos
    tabla.add_column("ID", justify="center", style="cyan", no_wrap=True)
    tabla.add_column("    Nombre", justify="left", style="green")
    tabla.add_column("Precio", justify="right", style="#FFA500")  # Naranja
    tabla.add_column("Categoria", justify="center", style="yellow")
    tabla.add_column("Stock", justify="center", style="magenta")
    tabla.add_column("            Descripción", style="blue")
    
    # Recorremos la lista de productos y agregamos cada uno como una fila
    for producto in productos:
        tabla.add_row(
            str(producto["id"]),
            str(producto["nombre"]),
            f"${producto['precio']:.2f}",
            str(producto['categoria']),
            str(producto["stock"]),
            str(producto["descripcion"])
        )
    
    # Mostramos la tabla en consola
    consola.print(tabla)
