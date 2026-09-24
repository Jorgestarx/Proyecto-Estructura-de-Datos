import tkinter as tk
from tkinter import ttk

def mostrar_seleccion(event):
    print("Elegiste:", combo.get())

ventana = tk.Tk()

combo = ttk.Combobox(ventana, values=["rojo", "verde", "azul"], state="readonly")
combo.pack()
combo.bind("<<ComboboxSelected>>", mostrar_seleccion)

ventana.mainloop()