import tkinter as tk
from tkinter import messagebox

def confirmar_salida():
    respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea salir?")
    if respuesta:
        ventana.destroy()

ventana = tk.Tk()
boton = tk.Button(ventana, text="Salir", command=confirmar_salida)
boton.pack()
ventana.mainloop()