# Función para obtener las temperaturas diarias
def obtener_temperaturas():
    # Se crea una lista vacía para almacenar las temperaturas
    temperaturas = []

    # Usamos un ciclo `for` para pedir las temperaturas de cada día (7 días en total)
    for i in range(7):  # El rango va de 0 a 6, es decir, 7 iteraciones
        # Solicitamos al usuario la temperatura del día i+1
        temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        # Almacenamos la temperatura ingresada en la lista
        temperaturas.append(temperatura)

    # Devolvemos la lista con todas las temperaturas de la semana
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    # Usamos la función `sum()` para sumar todos los valores de la lista temperaturas
    total = sum(temperaturas)

    # Calculamos el promedio dividiendo la suma total entre la cantidad de días (7 días)
    promedio = total / len(temperaturas)

    # Devolvemos el promedio calculado
    return promedio


# Función principal que organiza el flujo del programa
def main():
    print("Programa para calcular el promedio de temperaturas semanales.")

    # Llamamos a la función `obtener_temperaturas` para obtener las temperaturas de la semana
    temperaturas = obtener_temperaturas()

    # Llamamos a la función `calcular_promedio` para calcular el promedio de las temperaturas
    promedio = calcular_promedio(temperaturas)

    # Mostramos el resultado en pantalla con dos decimales
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")


# Llamada a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()

