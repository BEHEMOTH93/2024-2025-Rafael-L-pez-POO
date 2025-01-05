# Sistema_De_reservas.py

class Habitacion:
    """Clase que representa una habitación de hotel."""
    def __init__(self, numero, tipo, precio, disponible=True):
        self.numero = numero
        self.tipo = tipo  # Simple, Doble, Suite
        self.precio = precio
        self.disponible = disponible

    def reservar(self):

        """ Metodo para reservar la habitación."""
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"Habitación {self.numero} ya está reservada.")

    def liberar(self):
        """ Metodo para liberar la habitación."""
        self.disponible = True
        print(f"Habitación {self.numero} está ahora disponible.")


class Cliente:
    """ Clase que representa un cliente del hotel. """
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}"


class Reserva:
    """ Clase que gestiona las reservas del hotel. """
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion

    def realizar_reserva(self):
        """ Metodo para realizar una reserva."""
        if self.habitacion.disponible:
            self.habitacion.reservar()
            print(f"Reserva realizada para {self.cliente.nombre} en la habitación {self.habitacion.numero}.")
        else:
            print(f"La habitación {self.habitacion.numero} no está disponible.")

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos habitaciones.
    habitacion1 = Habitacion(101, "Doble", 50.0)
    habitacion2 = Habitacion(102, "Suite", 100.0)

    # Creamos un cliente.
    cliente1 = Cliente("Rafael López", "1993666999")

    # Intentamos reservar una habitación.
    reserva1 = Reserva(cliente1, habitacion1)
    reserva1.realizar_reserva()

    # Liberamos la habitación y volvemos a reservar.
    habitacion1.liberar()
    reserva1.realizar_reserva()