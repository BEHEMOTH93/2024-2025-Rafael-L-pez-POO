# Aplicación de Gestión de Tareas con GUI y Atajos de Teclado usando Tkinter
# Autor: Estudiante de primer semestre
# Descripción: Esta app permite gestionar tareas (agregar, marcar como completadas, eliminar) usando botones y atajos de teclado.

import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Función para agregar tareas
# -----------------------------
def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "No se puede agregar una tarea vacía.")

# ---------------------------------------------
# Función para marcar una tarea como completada
# Se añade un ✔ y se cambia el color a gris
# ---------------------------------------------
def marcar_completada(event=None):
    if ventana.focus_get() == entrada_tarea:
        return  # Ignorar si el foco está en el campo de entrada
    try:
        seleccion = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(seleccion)
        if not tarea.startswith("✔ "):
            lista_tareas.delete(seleccion)
            nueva_tarea = "✔ " + tarea
            lista_tareas.insert(seleccion, nueva_tarea)
            lista_tareas.itemconfig(seleccion, {'fg': 'gray'})
    except IndexError:
        messagebox.showwarning("Selecciona una tarea", "Por favor, selecciona una tarea para marcar como completada.")

# -----------------------------------
# Función para eliminar una tarea
# -----------------------------------
def eliminar_tarea(event=None):
    if ventana.focus_get() == entrada_tarea:
        return  # Ignorar si el foco está en el campo de entrada
    try:
        seleccion = lista_tareas.curselection()[0]
        lista_tareas.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Selecciona una tarea", "Por favor, selecciona una tarea para eliminar.")

# -----------------------------------
# Función para cerrar la aplicación
# -----------------------------------
def cerrar_app(event=None):
    ventana.quit()

# ----------------------------------------
# Creación de la ventana principal
# ----------------------------------------
# Decisión: ventana de tamaño fijo para mantener el diseño ordenado
ventana = tk.Tk()
ventana.title("Gestión de Tareas")
ventana.geometry("400x400")
ventana.resizable(False, False)

# ------------------------------
# Campo de entrada y botón para agregar tareas
# ------------------------------
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)

btn_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
btn_agregar.pack()

# ----------------------------------
# Lista de tareas mostrada en Listbox
# Decisión: Listbox permite seleccionar y manejar tareas fácilmente
# ----------------------------------
lista_tareas = tk.Listbox(ventana, width=50, height=15)
lista_tareas.pack(pady=10)

# ------------------------------
# Botones de acción
# ------------------------------
btn_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack()

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack()

# ------------------------------
# Asignación de atajos de teclado
# ------------------------------
# Enter: agrega tarea
# C: marca como completada
# D/Delete: elimina tarea
# Escape: cierra la aplicación
ventana.bind("<Return>", agregar_tarea)
ventana.bind("<c>", marcar_completada)
ventana.bind("<d>", eliminar_tarea)
ventana.bind("<Delete>", eliminar_tarea)
ventana.bind("<Escape>", cerrar_app)

# ------------------------------
# Iniciar el bucle principal
# ------------------------------
ventana.mainloop()
