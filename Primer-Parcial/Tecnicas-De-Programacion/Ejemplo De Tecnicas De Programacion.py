# Ejemplo de Técnicas de Programación en Python

# Este programa muestra un combate entre dos personajes:
# Ursa (Guerrero) e Invoker (Mago).
# Aplicamos Abstracción, Encapsulación, Herencia y Polimorfismo.

# Clase base que sirve como plantilla para cualquier personaje
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        # Muestra los atributos básicos del personaje
        print(f"{self.nombre}:")
        print(f"· Fuerza: {self.fuerza}")
        print(f"· Inteligencia: {self.inteligencia}")
        print(f"· Defensa: {self.defensa}")
        print(f"· Vida: {self.vida}")

    def esta_vivo(self):
        # Devuelve True si la vida del personaje es mayor a 0
        return self.vida > 0

    def morir(self):
        # Reduce la vida a 0 y muestra un mensaje
        self.vida = 0
        print(f"{self.nombre} ha muerto.")


# Clase Guerrero que hereda de Personaje
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        # Usa el constructor de la clase base e incluye un atributo nuevo: espada
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def atributos(self):
        # Muestra los atributos del Guerrero, incluyendo su espada
        super().atributos()
        print(f"· Espada: {self.espada}")

    def daño(self, enemigo):
        # Calcula el daño que el Guerrero inflige a un enemigo
        return self.fuerza * self.espada - enemigo.defensa


# Clase Mago que hereda de Personaje
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        # Usa el constructor de la clase base e incluye un atributo nuevo: libro
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        # Muestra los atributos del Mago, incluyendo su libro mágico
        super().atributos()
        print(f"· Libro: {self.libro}")

    def daño(self, enemigo):
        # Calcula el daño que el Mago inflige a un enemigo
        return self.inteligencia * self.libro - enemigo.defensa


# Función para realizar un combate entre dos personajes
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\nTurno {turno}")

        # Turno del jugador 1
        print(f">>> {jugador_1.nombre} ataca a {jugador_2.nombre}:")
        daño = max(0, jugador_1.daño(jugador_2))  # El daño no puede ser negativo
        jugador_2.vida -= daño
        print(f"{jugador_1.nombre} inflige {daño} puntos de daño.")
        if not jugador_2.esta_vivo():
            jugador_2.morir()
            break

        # Turno del jugador 2
        print(f">>> {jugador_2.nombre} ataca a {jugador_1.nombre}:")
        daño = max(0, jugador_2.daño(jugador_1))  # El daño no puede ser negativo
        jugador_1.vida -= daño
        print(f"{jugador_2.nombre} inflige {daño} puntos de daño.")
        if not jugador_1.esta_vivo():
            jugador_1.morir()
            break

        turno += 1

    # Resultado del combate
    if jugador_1.esta_vivo():
        print(f"\n{jugador_1.nombre} ha ganado el combate.")
    elif jugador_2.esta_vivo():
        print(f"\n{jugador_2.nombre} ha ganado el combate.")
    else:
        print("\nEl combate terminó en empate.")


# --------------------------------------------
# Creación de los personajes
print("\n--- Creación de Personajes ---")
ursa = Guerrero("Ursa", 25, 8, 5, 120, 3)  # Guerrero: fuerza alta, espada poderosa
invoker = Mago("Invoker", 10, 20, 4, 100, 4)  # Mago: inteligencia alta, libro mágico

# Mostramos sus atributos
ursa.atributos()
invoker.atributos()

# Inicio del combate
print("\n--- Iniciando el Combate ---")
combate(ursa, invoker)
