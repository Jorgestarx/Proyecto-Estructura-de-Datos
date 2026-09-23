import datetime



#----------------------------------------verificaciones-------------------------------------------------
#verificación nombre
def verificar_nombre(nombre):
       copia_nombre = nombre.replace(" ", "")
       return copia_nombre.isalpha()

#verificación identificación
def verificar_identificación(identificación):
     return  identificación.isdigit() and len(identificación) == 11

#verificación genero
def verificar_genero(genero, generos):
     genero_verif = genero.lower().strip()
     return genero_verif in generos

#verificación menus
def verificar_menu(menu, menus):
     return menu in menus


#verificación nsesiones             
def verificar_nsesiones(nsesiones):
     return nsesiones >0



#----------------------------------------Diccionarios ------------------------------------------------------
#DICCIONARIO GÉNERO
generos = ["femenino", "masculino"]

#Diccionario menú  
menus = {"Menu ejecutivo" : 35000     , "Menu vegetariano" : 28000  , "Menu de degustación" : 75000  , "Menu infantil" : 20000 , "Menu gourmet" : 95000}


#-----------------------------------Clase Gestión de clientes----------------------------------- 
class GestionClientes():
     def __init__(self, nombre, identificacion, genero, menu, costo_sesion, nsesiones): 
                    self.nombre = nombre
                    self.identificacion = identificacion
                    self.genero = genero
                    self.menu = menu
                    self.costo_sesion = costo_sesion
                    self.nsesiones = nsesiones 
                    registro = datetime.datetime.now()
                    self.registro = registro.strftime("%d/%m/%Y %H:%M")

     def calculo_total(self, costo_sesion, nsesiones):
          costo_total = costo_sesion * nsesiones
          return costo_total

#------------------------------------------Inputs Datos--------------------------------------------

if __name__ == "__main__":
     #Nombre completo
     while True:
       nombre = input("Ingrese su nombre completo: ")
       if verificar_nombre(nombre):
         print("Nombre ingresado correctamente.")
         break
       else:
          print("Nombre inválido, intentelo de nuevo.")


#Identificación
     while True:
      identificación =input("Ingrese su número de identificación (11 dígitos): ")
      if verificar_identificación(identificación):
          print("Número de identificación ingresado correctamente. ")
          break
      else:
          print("Número de identificación inválido, intente de nuevo.")

     #Genero   
     while True:
      genero = input("Genero (Masculino/Femenino): ")
      if verificar_genero(genero, generos):
          print("Genero ingresado correctamente")
          break
      else:
          print("Genero inválido, intente de nuevo.")

     #Menu       
     while True:
      menu = input(f"¿Qué menu desea ordenar? {list(menus.keys())}: ")
      if verificar_menu(menu, menus):
          print("Menu recibido correctamente")
          break
      else:
          print("Menú inválido, intente de nuevo (Asegurese de escribirlo tal cual como se muestra en las opciones).")


     #costo por sesion
     costo_sesion = menus[menu] 


     #Número sesiones
     while True:
      try:
          nsesiones = int(input("¿Cuántas sesiones desea pagar?: "))
          if verificar_nsesiones(nsesiones): 
               print("Número de sesiones recibido correctamente.")
               break
          else:
               print("Número de sesiones incorrecto, intente de nuevo")
      except ValueError:
          print("Número de sesiones inválido, intente de nuevo.")

     cliente = GestionClientes(nombre, identificación, genero, menu, costo_sesion, nsesiones)

     print(cliente.calculo_total(cliente.costo_sesion, cliente.nsesiones))