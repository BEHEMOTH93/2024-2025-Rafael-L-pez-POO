# Clase que representa la información diaria del clima
class ClimaDiario:
    # Constructor que inicializa una lista de temperaturas vacía
    def __init__(self):
        self.temperaturas = []  # Encapsulando la lista de temperaturas

    # Método para agregar una temperatura diaria
    def agregar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    # Método para calcular el promedio de las temperaturas semanales
    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

    # Método para ingresar las temperaturas de los 7 días de la semana
    def ingresar_temperaturas(self):
        for i in range(7):
            while True:
                try:
                    temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                    self.agregar_temperatura(temperatura)
                    break  # Salir del ciclo si la entrada es válida
                except ValueError:
                    print("Por favor, ingrese un número válido para la temperatura.")

    # Método para mostrar el promedio de las temperaturas
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")


# Función principal que organiza el flujo del programa
def main():
    print("Programa para calcular el promedio de temperaturas semanales (POO).")

    # Crear una instancia de la clase ClimaDiario
    clima = ClimaDiario()

    # Ingresar las temperaturas de los 7 días
    clima.ingresar_temperaturas()

    # Mostrar el promedio semanal de las temperaturas
    clima.mostrar_promedio()


# Llamada a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
