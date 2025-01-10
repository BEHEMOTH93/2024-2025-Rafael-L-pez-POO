# Programa para calcular el área de un rectángulo.
# En este programa solicitaremos al usuario el ancho y la altura de un rectángulo,
# calcula el área y muestra el resultado.

def calcular_area_rectangulo(ancho, altura):

    """ Calcula el área de un rectángulo.

    :param ancho: Ancho del rectángulo (float).
    :param altura: Altura del rectángulo (float).
    :return: Área del rectángulo (float)."""
    return ancho * altura


# Solicitamos los datos al usuario

print("¡Bienvenido al calculador de áreas!")
ancho = float(input("Por favor, ingresa el ancho del rectángulo (en metros): "))
altura = float(input("Por favor, ingresa la altura del rectángulo (en metros): "))

# Calcula el área
area = calcular_area_rectangulo(ancho, altura)

# En esta parte nos mostrara el resultado
print(f"El área del rectángulo es: {area} metros cuadrados")

# Variable booleana para verificar si el área es mayor a 10 m²
es_area_grande = area > 10
print(f"¿Es el área mayor a 10 m²? {es_area_grande}")
