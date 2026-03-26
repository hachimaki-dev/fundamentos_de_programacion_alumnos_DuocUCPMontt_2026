opcion_usuario1 = ""
opcion_usuario2 = ""
puntaje_usuario1 = 0
puntaje_usuario2 = 0

print("Bienvenido al cahipun extremo")
print("por favor escriba la palabra piedra, papel o tijeras")

while puntaje_usuario1 < 3 and puntaje_usuario2 < 3:
    opcion_usuario1 = input("J1 - por favor ingrese su elección")
    opcion_usuario2 = input("J2 - por favor ingrese su elección") 

    if opcion_usuario1 == "piedra" and opcion_usuario2 == "papel":
        puntaje_usuario2 = puntaje_usuario2 + 1
        print(f"Usuario2 haz ganado. Llevas {puntaje_usuario2} de 3")

    elif opcion_usuario1 == "piedra" and opcion_usuario2 == "tijeras":
        puntaje_usuario1 = puntaje_usuario1 + 1
        print(f"Usuario2 haz ganado. Llevas {puntaje_usuario1} de 3")

    elif opcion_usuario1 == "papel" and opcion_usuario2 == "piedra":
        print(f"Ha ocurrido un empate. Vuelva a intentarlo")

    elif opcion_usuario1 == "papel" and opcion_usuario2 == "tijeras":
        puntaje_usuario2 = puntaje_usuario2 + 1
        print(f"Usuario2 haz ganado. Llevas {puntaje_usuario2} de 3")

    elif opcion_usuario1 == "papel" and opcion_usuario2 == "piedra":
        puntaje_usuario1 = puntaje_usuario1 + 1
        print(f"Usuario2 haz ganado. Llevas {puntaje_usuario1} de 3")

    elif opcion_usuario1 == "papel" and opcion_usuario2 == "papel":
        print(f"Ha ocurrido un empate. Vuelva a intentarlo")

    elif opcion_usuario1 == "tijeras" and opcion_usuario2 == "piedra":
        puntaje_usuario2 = puntaje_usuario2 + 1
        print(f"Usuario2 haz ganado. Llevas {puntaje_usuario2} de 3")

    elif opcion_usuario1 == "tijeras" and opcion_usuario2 == "papel":
        puntaje_usuario1 = puntaje_usuario1 + 1
        print(f"Usuario2 haz ganado. Llevas {puntaje_usuario1} de 3")

    elif opcion_usuario1 == "tijeras" and opcion_usuario2 == "tijeras":
        print(f"Ha ocurrido un empate. Vuelva a intentarlo")

    
if puntaje_usuario1 > puntaje_usuario2:
    print("j1 haz ganado")
    
elif puntaje_usuario1 < puntaje_usuario2:
    print("j2 haz ganado")