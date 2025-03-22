import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        """
        Se crea la ventana principal y se organizan los widgets en diferentes frames.
        """
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("650x400")

        # Frame superior para los campos de entrada
        frame_entry = tk.Frame(self.root, padx=10, pady=10)
        frame_entry.pack(fill=tk.X)

        # Etiqueta y campo para seleccionar la fecha con DateEntry
        tk.Label(frame_entry, text="Fecha:").grid(row=0, column=0)
        self.date_entry = DateEntry(frame_entry, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo para ingresar la hora del evento
        tk.Label(frame_entry, text="Hora:").grid(row=0, column=2)
        self.time_entry = tk.Entry(frame_entry, width=10)
        self.time_entry.grid(row=0, column=3, padx=5, pady=5)

        # Etiqueta y campo para ingresar la descripción del evento
        tk.Label(frame_entry, text="Descripción:").grid(row=1, column=0)
        self.desc_entry = tk.Entry(frame_entry, width=40)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Frame para los botones de acción
        frame_buttons = tk.Frame(self.root, padx=10, pady=5)
        frame_buttons.pack()

        # Botón para agregar un evento
        tk.Button(frame_buttons, text="Agregar Evento", command=self.add_event).pack(side=tk.LEFT, padx=5)
        # Botón para eliminar un evento seleccionado
        tk.Button(frame_buttons, text="Eliminar Evento", command=self.delete_event).pack(side=tk.LEFT, padx=5)
        # Botón para cerrar la aplicación
        tk.Button(frame_buttons, text="Salir", command=self.root.quit).pack(side=tk.LEFT, padx=5)

        # Frame inferior para mostrar la lista de eventos
        frame_list = tk.Frame(self.root, padx=10, pady=10)
        frame_list.pack(fill=tk.BOTH, expand=True)

        # Creación del TreeView para mostrar eventos con tres columnas: Fecha, Hora y Descripción
        self.tree = ttk.Treeview(frame_list, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def add_event(self):
        """
        Agrega un evento a la lista.
        Valida que los campos de hora y descripción no estén vacíos antes de añadirlo.
        """
        date = self.date_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()

        if not time or not desc:
            messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")
            return

        # Insertar el evento en el TreeView
        self.tree.insert("", tk.END, values=(date, time, desc))

        # Limpiar los campos de entrada después de agregar el evento
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def delete_event(self):
        """
        Elimina el evento seleccionado de la lista.
        Antes de eliminar, muestra una advertencia si no hay ningún evento seleccionado.
        Luego, solicita confirmación al usuario antes de proceder con la eliminación.
        """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")
            return

        # Confirmar eliminación con un cuadro de diálogo
        if messagebox.askyesno("Confirmación", "¿Seguro que desea eliminar este evento?"):
            self.tree.delete(selected_item)


if __name__ == "__main__":
    """
    Punto de entrada de la aplicación.
    Se crea la ventana principal y se instancia la clase AgendaApp.
    """
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
