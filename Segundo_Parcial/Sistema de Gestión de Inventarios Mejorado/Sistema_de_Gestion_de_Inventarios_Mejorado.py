import os

# Definimos la clase Producto para representar cada producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_line(self):
        """Convierte el objeto Producto en una línea de texto para guardarlo en un archivo."""
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_line(line):
        """Convierte una línea de texto en un objeto Producto."""
        id_producto, nombre, cantidad, precio = line.strip().split(',')
        return Producto(id_producto, nombre, int(cantidad), float(precio))

# Definimos la clase Inventario para gestionar la lista de productos y su almacenamiento en archivos
class Inventario:
    FILE_NAME = "inventario.txt"  # Nombre del archivo donde se guarda el inventario

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()  # Carga los productos al iniciar

    def guardar_en_archivo(self):
        """Guarda todos los productos en un archivo de texto manejando excepciones."""
        try:
            with open(self.FILE_NAME, 'w') as file:
                for producto in self.productos:
                    file.write(producto.to_line())
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el archivo: {e}")

    def cargar_desde_archivo(self):
        """Carga los productos desde un archivo de texto si existe."""
        if not os.path.exists(self.FILE_NAME):
            return  # Si el archivo no existe, simplemente no hace nada
        try:
            with open(self.FILE_NAME, 'r') as file:
                self.productos = [Producto.from_line(line) for line in file]
        except FileNotFoundError:
            print("Archivo de inventario no encontrado, se creará uno nuevo.")
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {e}")

    def agregar_producto(self, producto):
        """Agrega un producto al inventario y lo guarda en el archivo."""
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario y actualiza el archivo."""
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado si existía.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza un producto y guarda los cambios en el archivo."""
        for p in self.productos:
            if p.id_producto == id_producto:
                if nueva_cantidad is not None:
                    p.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    p.precio = nuevo_precio
                self.guardar_en_archivo()
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos en el inventario y los muestra en la consola."""
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)

# Función principal con el menú interactivo
def main():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID único: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese nueva cantidad (deje en blanco si no cambia): ")
            nuevo_precio = input("Ingrese nuevo precio (deje en blanco si no cambia): ")

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
