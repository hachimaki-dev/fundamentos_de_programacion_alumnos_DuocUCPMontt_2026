import sys
print("\n\n~~~BIENVENIDO AL HOSPITAL DE OSORNO~~~\n\n")

name_user = input("¿Cómo deseas llamarte?")
confirmation = input("¿Estas seguro de ese nombre? (si/no) ")
if confirmation == "si" or confirmation == "SI" or confirmation == "Si" or confirmation ==  "sI":
    print("¡Perfecto! Continuemos con el juego.")
else:
    print("Comencemos de nuevo...")
    sys.exit(5) 
 
print(f"¡Es un placer tenerte aquí, {name_user}!") 