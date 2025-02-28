class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para autor y título porque no deberían cambiar después de crear el libro
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para gestionar los libros prestados


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario para buscar libros rápidamente por ISBN
        self.usuarios_registrados = {}  # Diccionario para almacenar usuarios por ID
        self.historial_prestamos = []  # Lista para registrar el historial de préstamos

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro '{libro.info[0]}' agregado a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"Usuario {usuario.nombre} registrado correctamente.")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, usuario, isbn):
        if usuario.id_usuario not in self.usuarios_registrados:
            print("Usuario no registrado.")
            return

        if isbn not in self.libros_disponibles:
            print("Libro no disponible para préstamo.")
            return

        libro = self.libros_disponibles.pop(isbn)
        usuario.libros_prestados.append(libro)
        self.historial_prestamos.append((usuario.nombre, libro.info[0], "prestado"))
        print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, usuario, isbn):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                self.historial_prestamos.append((usuario.nombre, libro.info[0], "devuelto"))
                print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
                return
        print("El usuario no tiene prestado ese libro.")

    def buscar_libro(self, filtro, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if (filtro == 'titulo' and valor in libro.info[0]) or \
                    (filtro == 'autor' and valor in libro.info[1]) or \
                    (filtro == 'categoria' and valor == libro.categoria):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, usuario):
        if not usuario.libros_prestados:
            print("El usuario no tiene libros prestados.")
        else:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"- {libro.info[0]} de {libro.info[1]} (ISBN: {libro.isbn})")

    def mostrar_historial(self):
        if not self.historial_prestamos:
            print("No hay movimientos registrados.")
        else:
            print("Historial de préstamos/devoluciones:")
            for registro in self.historial_prestamos:
                print(f"{registro[0]} {registro[2]} el libro '{registro[1]}'.")


# Probando el sistema
libro1 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", "1234")
libro2 = Libro("IT", "Stephen King", "Terror", "5678")
usuario1 = Usuario("Rafael", "001")

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)

biblioteca.prestar_libro(usuario1, "1234")
biblioteca.listar_libros_prestados(usuario1)
biblioteca.devolver_libro(usuario1, "1234")
biblioteca.mostrar_historial()
