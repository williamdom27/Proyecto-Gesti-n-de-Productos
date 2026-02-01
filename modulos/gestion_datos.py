productos = []

def agregar_producto(producto):
    productos.append(producto)

def listar_productos():
    if not productos:
        print ("No hay productos registrados")
        return
    
    for i, producto in enumerate(productos, start=1):
        print(
            f"{i}. {producto['nombre']} - "
            f"${producto['precio']} - "
            f"stock: {producto['stock']}"
        )

def eliminar_producto(nombre):
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)
            print("Producto eliminado")
            return
    
    print("Producto no encontrado")