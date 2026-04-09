import time
import sys

print ("/============================/")
print ("/===Elcción de grupo k-pop===/")
print ("/============================/\n")

print ("Debes seleccionar a que grupo de K-POP deseas unirte.\n")
print ("Los equipos son los siguientes.\n")

print ("1.  - BTS.")
print ("2.  - BLACKPINK.")
print ("3.  - Stary Kids.\n")

print ("Ingrese a que equipo desea unirse en la sección de abajo.")

equipo_de_usuario = str(input("Ingrese su equipo : ")).lower()

while equipo_de_usuario == "blackpink" or equipo_de_usuario == "bts" or equipo_de_usuario == "straykids":
    print ()
    print ("Procesando.")
    time.sleep(3)
    print (f"bienvenido al fandom de {equipo_de_usuario}.")
    break

else:
    print ("Ingrese un grupo valido.")










