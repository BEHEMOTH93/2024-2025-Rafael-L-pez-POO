# Definimos la clase Producto para representar cada producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id_producto: ID único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible en el inventario.
        :param precio: Precio unitario del producto.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """
        Representación en texto del producto.
        Esto permite imprimir el objeto directamente con print().
        """
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Definimos la clase Inventario para gestionar la lista de productos
class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía para almacenar los productos.
        """
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario verificando que el ID sea único.
        :param producto: Objeto de tipo Producto a agregar.
        """
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID.
        Si el ID no existe, simplemente no hace nada.
        :param id_producto: ID del producto a eliminar.
        """
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado si existía.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad o el precio de un producto identificado por su ID.
        :param id_producto: ID del producto a actualizar.
        :param nueva_cantidad: Nueva cantidad del producto (opcional).
        :param nuevo_precio: Nuevo precio del producto (opcional).
        """
        for p in self.productos:
            if p.id_producto == id_producto:
                if nueva_cantidad is not None:
                    p.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    p.precio = nuevo_precio
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """
        Busca productos en el inventario cuyo nombre contenga la palabra ingresada.
        :param nombre: Nombre (o parte del nombre) del producto a buscar.
        """
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """
        Muestra todos los productos en el inventario.
        Si el inventario está vacío, indica que no hay productos.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)


# Función principal con el menú interactivo
def main():
    """
    Función principal que ejecuta un menú interactivo en la consola.
    Permite al usuario gestionar el inventario a través de opciones.
    """
    inventario = Inventario()  # Se crea una instancia del inventario

    while True:
# Mostrar menú de opciones
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        # Opción para agregar un nuevo producto
        if opcion == "1":
            id_producto = input("Ingrese ID único: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

# Opción para eliminar un producto por su ID
        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

# Opción para actualizar un producto existente
        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese nueva cantidad (deje en blanco si no cambia): ")
            nuevo_precio = input("Ingrese nuevo precio (deje en blanco si no cambia): ")

# Convertir valores ingresados si no están vacíos
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

# Opción para buscar productos por nombre
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

# Opción para mostrar todos los productos en el inventario
        elif opcion == "5":
            inventario.mostrar_productos()

# Opción para salir del programa
        elif opcion == "6":
            print("Saliendo del programa.")
            break

# Mensaje si la opción ingresada no es válida
        else:
            print("Opción no válida. Intente nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
