import tkinter as tk
from tkinter import messagebox
from src.logica.gestor_tareas import GestorTareas

class GestorTareasUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.gestor = GestorTareas()

        # Frame para entrada de tarea
        frame_tarea = tk.Frame(self.root)
        frame_tarea.pack(pady=10)

        tk.Label(frame_tarea, text="Título:").grid(row=0, column=0, padx=5)
        self.titulo_entry = tk.Entry(frame_tarea, width=30)
        self.titulo_entry.grid(row=0, column=1)

        tk.Label(frame_tarea, text="Descripción:").grid(row=1, column=0, padx=5)
        self.descripcion_entry = tk.Entry(frame_tarea, width=30)
        self.descripcion_entry.grid(row=1, column=1)

        tk.Button(frame_tarea, text="Agregar Tarea", command=self.agregar_tarea).grid(row=2, columnspan=2, pady=10)

        # Lista de tareas
        self.lista_tareas = tk.Listbox(self.root, width=50, height=10)
        self.lista_tareas.pack(pady=10)

        # Botones de control
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Marcar como Completada", command=self.marcar_completada).grid(row=0, column=0,
                                                                                                     padx=5)
        tk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea).grid(row=0, column=1, padx=5)

        self.actualizar_lista_tareas()

    def agregar_tarea(self):
        titulo = self.titulo_entry.get()
        descripcion = self.descripcion_entry.get()

        try:
            self.gestor.agregar_tarea(titulo, descripcion)
            messagebox.showinfo("Éxito", "Tarea agregada correctamente")
            self.actualizar_lista_tareas()
            self.titulo_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_lista_tareas(self):
        self.lista_tareas.delete(0, tk.END)
        for i, tarea in enumerate(self.gestor.obtener_tareas()):
            estado = "✔️" if tarea.completada else "❌"
            self.lista_tareas.insert(tk.END, f"{i + 1}. {estado} {tarea.titulo} - {tarea.descripcion}")

    def marcar_completada(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            self.gestor.marcar_completada(indice)
            messagebox.showinfo("Éxito", "Tarea marcada como completada")
            self.actualizar_lista_tareas()
        except IndexError:
            messagebox.showerror("Error", "Seleccione una tarea para marcar como completada")

    def eliminar_tarea(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            self.gestor.eliminar_tarea(indice)
            messagebox.showinfo("Éxito", "Tarea eliminada correctamente")
            self.actualizar_lista_tareas()
        except IndexError:
            messagebox.showerror("Error", "Seleccione una tarea para eliminar")


# Configuración inicial de la aplicación
root = tk.Tk()
app = GestorTareasUI(root)
root.mainloop()