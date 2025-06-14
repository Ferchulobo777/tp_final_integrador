from style.estilos import mostrar_error,mostrar_exito,mostrar_info,mostrar_opcion,mostrar_titulo, generar_tabla_productos
from utils.archivo_json import cargar_datos, guardar_datos
from utils.archivo_txt import generar_reporte_txt
from datetime import datetime

ruta_json = "json/productos.json"
cargar_datos(ruta_json)

# ---------------------------------------------------------------------------- #
#                 Funcion para el servicio de agregar producto                 #
# ---------------------------------------------------------------------------- #

def agregar_producto():
     mostrar_titulo("\t\t\t\t\t 📝 ------------ Agregar Producto -------------- 📝\n")
     
     mostrar_opcion("🆕 Ingrese el nombre del producto 🆕:")
     nombre = input().strip().capitalize()
     
     mostrar_opcion("💲 Ingrese el precio 💲:")
     try:
        precio = float(input())
        precio = round(precio, 2)
     except ValueError:
         mostrar_error("❌ Precio invalido, debe ingresar un valor númerico")
         return
     
     mostrar_opcion("Ingresa la categoria:")
     categoria = input().strip().capitalize()
         
     mostrar_opcion("📦 Ingresa la cantidad de stock 📦:")
     try:
         stock = int(input())
     except ValueError:
         mostrar_error("❌ Stock invalido, debe ser un valor entero positivo")
         return
     mostrar_opcion("📝 Ingresa una descripción 📝:")
     descripcion = input()             
     
     
# ------------------------ cargar productos existentes ----------------------- #

     productos = cargar_datos(ruta_json)

# ------------------------ generar ID automaticamente ------------------------ #

     nuevo_id = productos[-1]["id"] + 1 if productos else 1
    
    
     nuevo_producto = {
      "id": nuevo_id,
      "nombre": nombre,
      "precio": precio,
      "categoria": categoria,
      "stock": stock,
      "descripcion": descripcion
}
     productos.append(nuevo_producto)
     guardar_datos(ruta_json, productos)
     
     
     mostrar_exito(f"✅ Producto: {nombre} agregado correctamente ✅")
     
     
   # ---------------------------------------------------------------------------- #
   #                 Función para el servicio de listar productos                 #
   # ---------------------------------------------------------------------------- #
     
def listar_productos():
    mostrar_titulo("\t\t\t\t\t 📝 ---------- Listar Productos ---------- 📝\n")
    productos = cargar_datos(ruta_json)
    generar_tabla_productos(productos)             
    
    
   # ---------------------------------------------------------------------------- #
   #               Función para el servicio de actualizar producto               #
   # ---------------------------------------------------------------------------- #
    
    
def actualizar_productos():
    mostrar_titulo("\t\t\t\t\t ✏️ ---------- Actualizar Producto ---------- ✏️\n")
    
    
    productos = cargar_datos(ruta_json)
    
    
    if not productos:
        mostrar_info("⚠️ No hay productos para actualizar ⚠️")
        return
    
    
    generar_tabla_productos(productos)
    
    mostrar_opcion("\t\t\t\t🔢 Ingresa el ID del producto a modificar: 🔢")
    try:
        id_actualizar = int(input())
    except ValueError:
        mostrar_error("❌ ID invalido. Debes ingresar un número entero ❌")
        return
    
    
    producto = next((p for p in productos if p["id"] == id_actualizar), None)
    
    if not producto:
        mostrar_error("❌ No se encontro producto con ese ID. ❌")
        return
    
    mostrar_info("💡 Presioná ENTER para dejar el valor actual sin cambios.")
    mostrar_opcion(f"📦 Nombre actual: {producto['nombre']}")
    nuevo_nombre = input("Nuevo nombre: ").strip().capitalize()
    if nuevo_nombre:
        producto["nombre"] = nuevo_nombre
    mostrar_opcion(f"💲 Precio actual: {producto['precio']:.2f}")
    nuevo_precio = input("Nuevo precio: ").strip()
    if nuevo_precio:
        try:
            producto["precio"] = round(float(nuevo_precio), 2)
        except ValueError:
            mostrar_error("❌ Precio inválido. Se mantiene el valor anterior.")                
    mostrar_opcion(f"🏷️ Categoría actual: {producto.get('categoria', 'Ninguna')}")
    nueva_categoria = input("Nueva categoría: ").strip().capitalize()
    if nueva_categoria:
        producto["categoria"] = nueva_categoria

    mostrar_opcion(f"📦 Stock actual: {producto['stock']}")
    nuevo_stock = input("Nuevo stock: ").strip()
    if nuevo_stock:
        try:
            producto["stock"] = int(nuevo_stock)
        except ValueError:
            mostrar_error("❌ Stock inválido. Se mantiene el valor anterior.")

    mostrar_opcion(f"📝 Descripción actual: {producto['descripcion']}")
    nueva_desc = input("Nueva descripción: ").strip()
    if nueva_desc:
        producto["descripcion"] = nueva_desc

    guardar_datos(ruta_json, productos)
    mostrar_exito(f"✅ Producto con ID {id_actualizar} actualizado correctamente ✅")
    
    
# ---------------------------------------------------------------------------- #
#                  Función para el servicio de buscar producto                 #
# ---------------------------------------------------------------------------- #

def buscar_producto():
    mostrar_titulo("\t\t\t\t\t\t 🔍 ----------- Buscar Producto ------------ 🔍\n")
    productos = cargar_datos(ruta_json)
    
    
    if not productos:
        mostrar_info("⚠️ No hay productos cargados ⚠️")
        return
    
    mostrar_opcion("📌 Buscar por:\n1. ID\n2. Nombre")
    opcion = input("Opcion: ").strip()
    
    if opcion == "1":
        mostrar_opcion("🔢 Ingresa el ID del producto: ")
        try:
            id_buscar = int(input())
        except ValueError:
            mostrar_error("❌ ID inválido. Debés ingresar un número entero.")
            return
        
        producto = next((p for p in productos if p["id"] == id_buscar), None)
    
        if producto:
          generar_tabla_productos([producto])
        else:
          mostrar_error(f"❌ No se encontró un producto con el ID {id_buscar} ❌")
    
    elif opcion == "2":
       mostrar_opcion("🔤 Ingresá el nombre del producto:")
       nombre_buscar = input().strip().capitalize()
       coincidencias = [p for p in productos if nombre_buscar in p["nombre"]]
       
       if coincidencias:
           generar_tabla_productos(coincidencias)
       else:
           mostrar_error(f"❌ No se encontraron productos con el nombre '{nombre_buscar}' ❌")
    else:
        mostrar_error("❌ Opción inválida. Seleccioná 1 o 2.")          
            
                
        
# ---------------------------------------------------------------------------- #
#               Función para el servicio de eliminar un producto               #
# ---------------------------------------------------------------------------- #


def eliminar_producto():
    mostrar_titulo("\t\t\t\t\t🗑️ -------- Eliminar Producto -------- 🗑️\n")
    productos = cargar_datos(ruta_json)
    
    if not productos:
        mostrar_info("⚠️ No hay productos para eliminar ⚠️")
        return
    
    generar_tabla_productos(productos)
    
    mostrar_opcion("🔢 Ingresa el ID del producto a eliminar: ")
    try:
        id_eliminar = int(input())
    except ValueError:
        mostrar_error("❌ ID inválido. Debes ingresar un número entero ❌")
        return
    producto = next((p for p in productos if p["id"] == id_eliminar), None)
    
    if not producto:
        mostrar_error(f"❌ No se encontró un producto con el ID {id_eliminar} ❌")
        return
    
    mostrar_opcion(f"⚠️ ¿Estás seguro que deseas eliminar el producto '{producto['nombre']}'? (si/no): ")
    confirmacion = input().strip().lower()
    mostrar_error("debes ingresar si o no")
    if confirmacion == "si":
        productos = [p for p in productos if p["id"] != id_eliminar]
        guardar_datos(ruta_json, productos)
        mostrar_exito(f"✅ Producto ID: {id_eliminar} eliminado correctamente ✅")
    else:
        mostrar_error("❗ Operación cancelada ❗")
        
        
# ---------------------------------------------------------------------------- #
#               Función para el servicio de reporte de bajo Stock              #
# ---------------------------------------------------------------------------- #


def reportar_bajo_stock():
    mostrar_titulo("\t\t\t\t\t⚠️ -------- Productos con Bajo Stock -------- ⚠️\n")
    productos = cargar_datos(ruta_json)
    
    if not productos:
        mostrar_info("ℹ️ No hay productos cargados en el sistema ℹ️")
        return
    
    UMBRAL_BASE = 10
    
    mostrar_opcion(f"📉 Ingrese el umbral mínimo de stock (actual: {UMBRAL_BASE}). Enter para usar valor por defecto:")
    try:
        umbral_input = input().strip()
        umbral = int(umbral_input) if umbral_input else UMBRAL_BASE
        if umbral < 0:
            raise ValueError
    except ValueError:
        mostrar_error("❌ Valor inválido. Usando umbral por defecto (10 unidades)")
        umbral = UMBRAL_BASE
    
    # Filtrar productos con stock igual o menor al umbral
    productos_bajo_stock = [p for p in productos if p['stock'] <= umbral]
    
    if not productos_bajo_stock:
        mostrar_info(f"ℹ️ No hay productos con stock menor o igual a {umbral} unidades ℹ️")
        return
    
    # Mostrar tabla en pantalla
    generar_tabla_productos(productos_bajo_stock)
    
    # Generar reporte en TXT
    mostrar_opcion("¿Desea generar un reporte en archivo TXT? (si/no): ")
    if input().strip().lower() == 'si':
        fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M")
        nombre_archivo = f"reportes/reporte_bajo_stock_{fecha_actual}.txt"
        
        # Definir campos para el reporte
        campos = ['id', 'nombre', 'precio', 'stock', 'categoria']
        titulo = "REPORTE DE PRODUCTOS CON BAJO STOCK"
        
        if generar_reporte_txt(nombre_archivo, titulo, productos_bajo_stock, campos, umbral):
            mostrar_exito(f"✅ Reporte generado correctamente: {nombre_archivo} ✅")
        else:
            mostrar_error("❌ Error al generar el reporte ❌")
        
            