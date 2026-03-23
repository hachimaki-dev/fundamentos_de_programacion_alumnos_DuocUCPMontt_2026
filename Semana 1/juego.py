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
    time.sleep(5)
    print(f"{name_user} es un detective de la PDI a quien le han encargado resolver el misterio detrás de las repentinas desapariciones.") 
    time.sleep(5)
    print(f"\033[1m| {name_user}: |\033[0m  La gente ya no sabe ni que inventar... Siempre le echan la culpa a lo paranormal. Por cosas como estas las personas desaparecen, por payasadas como esas.")
    time.sleep(5)
    print(f"\n~~~HORA DE SELECCIONAR ALTERNATIVAS~~~")
    print(f"escribe el número de la alternativa que deseas elegir\n")
    time.sleep(5)
    print(f"Frente a {name_user} se encuentra la puerta de entrada. ¿Qué hará {name_user}? /1. Entrar /2. Volver por donde vino\n")
    decision_1 = int(input("¿Qué decides hacer? "))
    if decision_1 == 1:
        print(f"\n{name_user} entra iluminando el lugar con su linterna, encontrando nada más que desastre y corrosión a causa de los años")
        time.sleep(5)
        print(f"\n\033[1m| {name_user}: |\033[0m  Pero que desastre de lugar... Normal que uno se pierda aquí")
    else:
        print(f"\n{name_user} decide abandonar el caso. Al volver a la estación de la PDI fue despedido por su superior al no cumplir con su trabajo.")
        time.sleep(5)
        print(f"\n\033[1m~~~ LOGRO DESBLOQUEADO: COBARDE PERO SOBREVIVIENTE ~~~\033[0m")
        time.sleep(3)
        print(f"\n\033[1;34m~~~ GAME OVER ~~~\033[0m")
else:
    print("Lo siento, no cumples con la edad necesaria para jugar")