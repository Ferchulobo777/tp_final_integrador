# Importación de funciones de estilo para mejorar la visualización en consola
from style.estilos import generar_tabla
from style.estilos import mostrar_opcion, mostrar_error, mostrar_info, mostrar_exito, mostrar_titulo

# Importación de funciones de servicios que realizan las acciones sobre los productos
from services.servicios import (
    agregar_producto,           # Permite dar de alta un nuevo producto
    listar_productos,           # Muestra todos los productos existentes
    actualizar_productos,       # Permite modificar los datos de un producto
    buscar_producto,            # Permite buscar un producto por nombre o ID
    eliminar_producto,          # Elimina un producto del sistema
    reportar_bajo_stock         # Genera un reporte con productos que tienen poco stock
)

# ---------------------------------------------------------------------------- #
#                                Menu Principal                                #
# ---------------------------------------------------------------------------- #

# Esta función representa el menú principal del sistema. Se ejecuta en bucle hasta que el usuario decide salir.
def menu_principal():
    while True:
        # Muestra el título del sistema con estilo
        mostrar_titulo("\n📦 Sistema de Control de Stock\n")

        # Genera la tabla con las opciones disponibles del menú
        generar_tabla()

        # Pide al usuario que seleccione una opción
        mostrar_opcion("\nSeleccioná una opción:")
        opcion = input()

        # Opción 1 - Alta de producto
        if opcion == "1":
            while True:
                agregar_producto()
                mostrar_opcion("\n¿Desea agregar otro producto? SI-NO")
                opcion_continuar = input().strip().lower()
                if opcion_continuar != "si":
                    break  # Sale del sub-bucle si no desea continuar agregando

        # Opción 2 - Listado de productos
        elif opcion == "2":
            listar_productos()

        # Opción 3 - Modificación de productos
        elif opcion == "3":
            actualizar_productos()

        # Opción 4 - Búsqueda de productos
        elif opcion == "4":
            buscar_producto()

        # Opción 5 - Eliminación de productos
        elif opcion == "5":
            eliminar_producto()

        # Opción 6 - Reporte de bajo stock
        elif opcion == "6":
            reportar_bajo_stock()

        # Opción 7 - Salir del sistema
        elif opcion == "7":
            mostrar_info("Saliendo del programa...")
            break  # Rompe el bucle principal y finaliza el programa

        # En caso de ingresar una opción inválida
        else:
            mostrar_error("⚠️ Opción no válida. Por favor, intentá de nuevo.")
