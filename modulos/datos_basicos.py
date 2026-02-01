def cargar_producto():
    nombre = input("Ingrese nombre del producto: ")
    precio = float(input("Ingrese precio: "))
    stock = int(input("Ingrese Stock: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    return producto