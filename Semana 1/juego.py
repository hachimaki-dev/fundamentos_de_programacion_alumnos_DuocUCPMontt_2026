import sys
import time
print("\n\n~~~ BIENVENIDO AL HOSPITAL DE OSORNO ~~~\n\n")

name_user = input("¿Cómo deseas llamarte?")
confirmation = input("¿Estas seguro de ese nombre? (si/no) ")
if confirmation.lower() == "si":
    print("¡Perfecto! Continuemos con el juego.")
else:
    print("Comencemos de nuevo...")
    sys.exit(0) 
 
print(f"¡Es un placer tenerte aquí, {name_user}!") 

edad_user = int(input("¿Cuántos años tienes? "))
if edad_user >= 18 and edad_user <= 50:
    print("\n¡Genial! Puedes continuar con el juego.")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Ubicación: Hospital de Osorno, Chile...")
    time.sleep(2)
    print("Se han reportado varios casos de personas desaparecidas")
    time.sleep(2)
    print(f"{name_user} es un detective de la PDI a quien le han encargado resolver el misterio detrás de las repentinas desapariciones.") 
else:
    print("Lo siento, no cumples con la edad necesaria para jugar")