# Creación de una Aplicación GUI Básica

# Se importa la librería Tkinter para crear la interfaz gráfica,
# y messagebox para mostrar cuadros de diálogo con mensajes al usuario.
import tkinter as tk
from tkinter import messagebox

# Función para agregar un elemento a la lista.
# Verifica que el campo no esté vacío para evitar agregar elementos sin valor.
def agregar_item():

    item = entry.get()
    if item:
        lista.insert(tk.END, item)  # Inserta el elemento al final de la lista.
        entry.delete(0, tk.END)  # Limpia el campo de texto después de agregar el elemento.
    else:
# Muestra un cuadro de advertencia si el campo está vacío.
        messagebox.showwarning("Advertencia", "El campo no puede estar vacío")

def limpiar_lista():
    # Función para limpiar todos los elementos de la lista.
    # Útil para reiniciar la interfaz sin cerrar la aplicación.
    lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
# Define el título de la ventana.
ventana.title("Agregador Basico")
# Establece el tamaño de la ventana.
ventana.geometry("400x300")

# Etiqueta y campo de texto
label = tk.Label(ventana, text="Ingrese un elemento:")
# Muestra una etiqueta para guiar al usuario.
label.pack(pady=5)

entry = tk.Entry(ventana)
# Campo de texto para que el usuario ingrese datos.
entry.pack(pady=5)

# Botones
# Botón para agregar elementos a la lista.

btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_item)
btn_agregar.pack(pady=5)
# Botón para limpiar la lista.
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Lista para mostrar los elementos
lista = tk.Listbox(ventana)
# Lista para visualizar los elementos agregados.
lista.pack(pady=10, fill=tk.BOTH, expand=True)

# Iniciar el bucle de la aplicación
# Mantiene la ventana abierta y activa los eventos de la GUI.
ventana.mainloop()
