from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.box import ROUNDED, SIMPLE_HEAVY

# ---------------------------------------------------------------------------- #
#                               Definimos un tema                              #
# ---------------------------------------------------------------------------- #
custom_theme = Theme({
    "titulo": "bold cyan",
    "opcion": "bold green",
    "error": "bold red",
    "info": "yellow",
    "exito": "bold blue",
})

# ---------------------------------------------------------------------------- #
#                        Consola con tema personalizado                        #
# ---------------------------------------------------------------------------- #
consola = Console(theme=custom_theme)

# ---------------------------------------------------------------------------- #
#                Funciones auxiliares para imprimir por consola                #
# ---------------------------------------------------------------------------- #
def mostrar_titulo(texto):
    consola.print(texto, style = "titulo")
    
def mostrar_opcion(texto):
    consola.print(texto, style="opcion")
    
def mostrar_error(texto):
    consola.print(texto, style="error")

def mostrar_info(texto):
    consola.print(texto, style="info")
    
def mostrar_exito(texto):
    consola.print(texto, style="exito")
    
# ---------------------------------------------------------------------------- #
#                   función para generar tabla menu principal                  #
# ---------------------------------------------------------------------------- #
    
def generar_tabla():
    tabla = Table(title="📋 Menú Principal", box=ROUNDED, style="opcion", expand=False)
    tabla.add_column("N°", justify="center", style="bold cyan", no_wrap=True)
    tabla.add_column("Acción", justify="left", style="bold green")

    opciones = [
        ("1", "Agregar Producto"),
        ("2", "Listar Productos"),
        ("3", "Modificar Producto"),
        ("4", "Buscar Producto"),
        ("5", "Eliminar Producto"),
        ("6", "Reporte Bajo de Stock"),
        ("7", "Salir")
    ]

    for numero, descripcion in opciones:
        tabla.add_row(numero, descripcion)

    consola.print(tabla)
    
    
    # ---------------------------------------------------------------------------- #
    #                    función para generar tabla de productos                   #
    # ---------------------------------------------------------------------------- #
    
    
def generar_tabla_productos(productos):
        if not productos:
            mostrar_info("⚠️ No hay productos cargados ⚠️")
            return
        tabla = Table(title="📦 Productos en Stock 📦", title_style="bold green")
        
        tabla.add_column("ID", justify="center", style="cyan", no_wrap=True)
        tabla.add_column("    Nombre", justify="left", style="green")
        tabla.add_column("Precio", justify="right", style="#FFA500")
        tabla.add_column("Categoria", justify="center", style="yellow")
        tabla.add_column("Stock", justify="center", style="magenta")
        tabla.add_column("            Descripción", style="blue")
        
        for producto in productos:
            tabla.add_row(
                str(producto["id"]),
                str(producto["nombre"]),
                f"${producto['precio']:.2f}",
                str(producto['categoria']),
                str(producto["stock"]),
                str(producto["descripcion"])
            )
        consola.print(tabla)        
        