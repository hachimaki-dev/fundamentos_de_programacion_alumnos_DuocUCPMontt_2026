import time 
import sys

print ("/====================/")
print ("/===Menú Maincraft===/")
print ("/====================/\n")

print ("Aquí podras craftear una de las dos opciones.\n")

print ("1. -   Espada de diamante.")
print ("2. -   Pico de diamante.")
print ("3. -   Salir de la Mesa.\n")

print ("Confirme que desea hacer.\n")

while True :
    eleccion = int(input("Cofirmar : "))
    print()

    if eleccion == 1:
        print ("Crafetando 'Espada de diamante'.")
        time.sleep(2)
        print ("Su espada ha sido crafteado.")
        
    elif eleccion == 2:
        print ("Crafteando 'Pico de diamante'.")
        time.sleep(2)
        print ("Su pico de diamante ha sido crafteado.")

    elif eleccion == 3:
        print ("Saliedo de mesa de crafteo.")
        time.sleep(2)
        break

    else:
        print ("Número invalido, eliga solo del 1 al 3.")
        continue


