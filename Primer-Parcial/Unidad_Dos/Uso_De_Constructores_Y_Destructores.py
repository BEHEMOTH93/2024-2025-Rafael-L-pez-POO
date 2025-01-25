# Uso De Constructores y Destructores
class Persona:
    def __init__(self, nombre, edad):
        """Constructor de la clase Persona.
        Se ejecuta automáticamente al crear un objeto.
        Inicializa los atributos nombre y edad con los valores proporcionados."""
        # Guarda el nombre de la persona
        self.nombre = nombre
        # Guarda la edad de la persona
        self.edad = edad
        print(f"Persona {self.nombre} creada.")

    def mostrar_info(self):
        """ Metodo para mostrar la información de la persona.
        Imprime el nombre y la edad en la consola."""
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def __del__(self):
        """ Destructor de la clase Persona.
        Se ejecuta automáticamente cuando el objeto es eliminado.
        Muestra un mensaje indicando que la persona ha sido eliminada."""
        print(f"Persona {self.nombre} eliminada.")

# Creación de objetos
persona1 = Persona("Rafael López", 31)
# Se crea un objeto de la clase Persona
persona1.mostrar_info()
# Llamamos al metodo para mostrar la información

# Eliminación del objeto (opcional, Python lo hace automáticamente al finalizar el programa)
del persona1
# Se elimina manualmente el objeto para activar el destructor
