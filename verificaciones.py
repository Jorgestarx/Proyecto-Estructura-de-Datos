#verificación nombre
def verificar_nombre(nombre):
       copia_nombre = nombre.replace(" ", "")
       return copia_nombre.isalpha()

#verificación identificación
def verificar_identificación(identificación):
     return  identificación.isdigit() and len(identificación) == 11

#verificación genero
def verificar_genero(genero, generos):
     return genero in generos

#verificación menu
def verificar_menu(menu, menus):
     return menu in menus

#verificación nsesiones             
def verificar_nsesiones(nsesiones):
     return nsesiones >0



#Tkinter

def verificar_contraseña():
    if entrycontraseña.get() == "1793":
        mensaje2.config(text="Contraseña correcta")
        VentanaRegistro()
        boton.config(state = "disabled")
    else:
        mensaje2.config(text="Contraseña incorrecta")