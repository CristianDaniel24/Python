import tkinter as tk
from tkinter import messagebox


biblioteca = []


def agregar_libro():
    try:
        titulo = entry_titulo.get().strip()
        autor = entry_autor.get().strip()
        ejemplares = entry_ejemplares.get().strip()

        if not titulo:
            raise ValueError("El nombre del libro no puede estar vacío.")
        if not autor:
            raise ValueError("El nombre del autor no puede estar vacío.")
        if not ejemplares.isdigit() or int(ejemplares) <= 0:
            raise ValueError("La cantidad de ejemplares debe ser un número mayor a 0.")

        biblioteca.append([titulo, autor, int(ejemplares)])
        actualizar_lista()
        limpiar_campos()
        messagebox.showinfo("Éxito", "Libro agregado correctamente.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def eliminar_libro():
    titulo = entry_titulo.get().strip()
    if not titulo:
        messagebox.showerror("Error", "Por favor, ingrese el título del libro para eliminar.")
        return

    for libro in biblioteca:
        if libro[0].lower() == titulo.lower():
            biblioteca.remove(libro)
            actualizar_lista()
            limpiar_campos()
            messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
            return

    messagebox.showerror("Error", "El libro no existe en la biblioteca.")


def buscar_libro():
    titulo = entry_titulo.get().strip()
    if not titulo:
        messagebox.showerror("Error", "Por favor ingrese el título del libro para buscar.")
        return

    for libro in biblioteca:
        if libro[0].lower() == titulo.lower():
            messagebox.showinfo("Búsqueda", f"Título: {libro[0]}, Autor: {libro[1]}, Ejemplares: {libro[2]}")
            return

    messagebox.showerror("Error", "El libro no existe en la biblioteca.")


def actualizar_lista():
    text_biblioteca.config(state=tk.NORMAL)
    text_biblioteca.delete(1.0, tk.END)
    for libro in biblioteca:
        text_biblioteca.insert(tk.END, f"Título: {libro[0]}, Autor: {libro[1]}, Ejemplares: {libro[2]}\n")
    text_biblioteca.config(state=tk.DISABLED)


def limpiar_campos():
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_ejemplares.delete(0, tk.END)

#
ventana = tk.Tk()
ventana.title("Biblioteca")
ventana.geometry("500x400")


label_menu = tk.Label(ventana, text="Opciones de Biblioteca", font=("Arial", 14))
label_menu.pack(pady=10)


label_titulo = tk.Label(ventana, text="Título del Libro:")
label_titulo.pack()
entry_titulo = tk.Entry(ventana, width=40)
entry_titulo.pack(pady=5)

label_autor = tk.Label(ventana, text="Autor del Libro:")
label_autor.pack()
entry_autor = tk.Entry(ventana, width=40)
entry_autor.pack(pady=5)

label_ejemplares = tk.Label(ventana, text="Cantidad de Ejemplares:")
label_ejemplares.pack()
entry_ejemplares = tk.Entry(ventana, width=40)
entry_ejemplares.pack(pady=5)


boton_agregar = tk.Button(ventana, text="Agregar Libro", command=agregar_libro)
boton_agregar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Libro", command=eliminar_libro)
boton_eliminar.pack(pady=5)

boton_buscar = tk.Button(ventana, text="Buscar Libro", command=buscar_libro)
boton_buscar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)


text_biblioteca = tk.Text(ventana, height=10, width=60, state=tk.DISABLED)
text_biblioteca.pack(pady=10)

ventana.mainloop()