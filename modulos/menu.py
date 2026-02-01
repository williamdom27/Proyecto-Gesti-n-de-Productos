from modulos.datos_basicos import cargar_producto
from modulos.gestion_datos import (
    agregar_producto,
    listar_productos,
    eliminar_producto
)

def ejecutar_menu():
    while True:
        print("""
1. Agregar producto
2. Listar productos
3. Eliminar producto
4. Salir
""")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = cargar_producto()
            agregar_producto(producto)

        elif opcion == "2":
            listar_productos()

        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(nombre)

        elif opcion == "4":
            print("Saliendo del sistema")
            break

        else:
            print("Opción inválida")
            continue