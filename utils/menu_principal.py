from style.estilos import generar_tabla
from style.estilos import mostrar_opcion, mostrar_error, mostrar_info, mostrar_exito,mostrar_titulo
from services.servicios import agregar_producto, listar_productos, actualizar_productos, buscar_producto, eliminar_producto, reportar_bajo_stock


# ---------------------------------------------------------------------------- #
#                                Menu Principal                                #
# ---------------------------------------------------------------------------- #

def menu_principal():
    while True:
        mostrar_titulo("\n📦 Sistema de Control de Stock\n")
        generar_tabla()
        mostrar_opcion("\nSeleccioná una opción:")
        opcion = input()

        if opcion == "1":
            while True:
                agregar_producto()
                mostrar_opcion("\n¿Desea agregar otro producto? SI-NO")
                opcion_continuar = input().strip().lower()
                if opcion_continuar != "si":
                 break   
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            actualizar_productos()
        elif opcion == "4":
            buscar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            reportar_bajo_stock()
        elif opcion == "7":
            mostrar_info("Saliendo del programa...")
            break
        else:
            mostrar_error("⚠️ Opción no válida. Por favor, intentá de nuevo.")