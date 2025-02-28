import json

class Producto:
    """
    Representa un producto en el inventario.
    Cada producto tiene un ID único, nombre, cantidad y precio.
    """
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único para identificar el producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad del producto."""
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio

    def obtener_info(self):
        """Devuelve una cadena con la información del producto."""
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    """
    Representa el sistema de gestión de inventario.
    Utiliza un diccionario para almacenar productos, donde la clave es el ID del producto.
    También maneja la persistencia de datos a través de archivos JSON.
    """
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos
        self.archivo = "inventario.json"
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        """Agrega un nuevo producto al inventario si el ID no está repetido."""
        if producto.id_producto in self.productos:
            print("El ID del producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto específico."""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca un producto por su nombre y muestra su información."""
        for producto in self.productos.values():
            if producto.nombre.lower() == nombre.lower():
                print(producto.obtener_info())
                return
        print("Producto no encontrado.")

    def mostrar_todos(self):
        """Muestra todos los productos almacenados en el inventario."""
        if self.productos:
            for producto in self.productos.values():
                print(producto.obtener_info())
        else:
            print("No hay productos en el inventario.")

    def guardar_en_archivo(self):
        """Guarda el inventario en un archivo JSON para persistencia de datos."""
        with open(self.archivo, "w") as f:
            json.dump({id_p: vars(p) for id_p, p in self.productos.items()}, f)

    def cargar_desde_archivo(self):
        """Carga los datos del inventario desde un archivo JSON si existe."""
        try:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                self.productos = {id_p: Producto(**p) for id_p, p in datos.items()}
        except FileNotFoundError:
            self.productos = {}

# Interfaz de usuario en consola
def menu():
    """Función que maneja el menú de opciones para la gestión del inventario."""
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Nuevo precio (deje vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
