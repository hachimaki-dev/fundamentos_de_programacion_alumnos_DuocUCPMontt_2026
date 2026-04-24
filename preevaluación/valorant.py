import time
import sys

total_de_armas = 0


print ("/=============================/")
print ("/=====Armería de Valorant=====/")
print ("/=============================/\n")

print ("Bienvenido a la tienda de armas de valorant.")
print ("Aquí podras encontrar una variedad de armas para poder ganar.\n")


print ("Estamos cargando el menú de armas.")
time.sleep(3)

print ("/=======================/")
print ("/=====Menú de armas=====/")
print ("/=======================/\n")

print ("1.   -  Arma 1 ")
print ("3.   -  Arma 2 ")
print ("3.   -  Arma 3 ")
print ("4.   -  Arma 4 ")
print ("5.   -  Arma 5 \n")

print ("¿Cúal de estas armas desea usar?")
print ("Responda en la sección de abajo.\n")


while True :
    arma_a_escoger = int(input ("Ingrese el número del arma : "))
    if arma_a_escoger == 1 : 
        print ("Buena elección.")
        total_de_armas += 1
        print (f"Llevas un total de {total_de_armas}.\n")

    elif arma_a_escoger == 2 : 
        print ("Buena elección.")
        total_de_armas += 1
        print (f"Llevas un total de {total_de_armas}\n")

    elif arma_a_escoger == 3 : 
        print ("Buena elección.")
        total_de_armas += 1
        print (f"Llevas un total de {total_de_armas}\n")

    elif arma_a_escoger == 4 : 
        print ("Arma agotada, continue comprando.")
        continue
    
    elif arma_a_escoger == 5 : 
        print ("Buena elección.")
        total_de_armas += 1
        print (f"Llevas un total de {total_de_armas}\n")






