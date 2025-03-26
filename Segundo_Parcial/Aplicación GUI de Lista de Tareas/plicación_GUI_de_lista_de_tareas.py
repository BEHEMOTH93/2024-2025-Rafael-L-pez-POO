import tkinter as tk
from tkinter import messagebox

# Función para añadir una tarea a la lista
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)  # Se añade la tarea al final de la lista
        entry_task.delete(0, tk.END)  # Se limpia el campo de entrada después de añadir
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")  # Mensaje si el campo está vacío

# Función para marcar una tarea como completada
def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)  # Se elimina la tarea de la lista
        listbox_tasks.insert(tk.END, f"✔ {task}")  # Se añade nuevamente con una marca de completado
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")  # Mensaje si no se selecciona tarea

# Función para eliminar una tarea de la lista
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        listbox_tasks.delete(selected_task_index)  # Se elimina la tarea de la lista
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")  # Mensaje si no se selecciona tarea

# Función para añadir una tarea presionando Enter
def add_task_enter(event):
    add_task()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")  # Título de la ventana
root.geometry("400x400")  # Tamaño de la ventana

# Campo de entrada para nuevas tareas
tk.Label(root, text="Nueva Tarea:").pack(pady=5)
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)
entry_task.bind("<Return>", add_task_enter)  # Se asocia la tecla Enter para añadir tareas

# Frame para agrupar los botones
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

# Botones para manejar las tareas
tk.Button(frame_buttons, text="Añadir Tarea", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Marcar como Completada", command=mark_completed).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Eliminar Tarea", command=delete_task).grid(row=0, column=2, padx=5)

# Lista de tareas en un Listbox
listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
