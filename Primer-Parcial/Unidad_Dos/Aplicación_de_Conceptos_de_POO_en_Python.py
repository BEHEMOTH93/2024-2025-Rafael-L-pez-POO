# Aplicación de conceptos de POO en Python
# Objetivo: Demostrar herencia, encapsulación y polimorfismo

# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.__edad = edad  # Atributo privado (encapsulación)

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.__edad}"

    # Metodo para acceder al atributo privado
    def obtener_edad(self):
        return self.__edad

    # Metodo para modificar el atributo privado
    def establecer_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser positiva.")

# Clase derivada
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.carrera = carrera  # Atributo propio de la clase derivada

    # Polimorfismo: Sobrescritura de un método
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.obtener_edad()}, Carrera: {self.carrera}"

# Clase derivada adicional para demostrar más polimorfismo
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    # Polimorfismo: Sobrescritura de un método
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.obtener_edad()}, Materia: {self.materia}"

# Crear instancias y demostrar funcionalidad
persona = Persona("Rafael", 31)
print(persona.mostrar_informacion())

estudiante = Estudiante("Martha", 35, "Ingeniería de Sistemas")
print(estudiante.mostrar_informacion())

profesor = Profesor("Alejandro", 31, "Redes")
print(profesor.mostrar_informacion())

# Demostrando encapsulación
print("Edad original:", persona.obtener_edad())
persona.establecer_edad(32)
print("Nueva edad:", persona.obtener_edad())
