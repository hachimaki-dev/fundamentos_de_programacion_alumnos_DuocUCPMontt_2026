opcion_usuario1 = ""
opcion_usuario2 = ""

nombre_usuario1 = ""
nombre_usuario2 = ""

puntaje_usuario1 = 0
puntaje_usuario2 = 0

print("\n****************************************************")
print("********** BIENVENIDO AL CACHIPUN EXTREMO **********")
print("****************************************************\n")

# otra opcion de while con bandera + if

nombre_usuario1 = input("Jugador 1 ingresa tu nombre: ")
nombre_usuario2 = input("Jugador 2 ingresa tu nombre: ")
print("\nPor favor escriba la palabra piedra, papel o tijeras")
print("Ingrese 'salir' para terminar el juego")

while puntaje_usuario1 < 3 and puntaje_usuario2 < 3:

    opcion_usuario1 = input(f"\n{nombre_usuario1} ingrese su eleccion: ")
    if opcion_usuario1 == "salir" :
        break

    opcion_usuario2 = input(f"{nombre_usuario2} ingrese su eleccion: ")
    if opcion_usuario2 == "salir" :
        break

    if opcion_usuario1 == opcion_usuario2 :
        print("Empate - vuelva a jugar")

    elif opcion_usuario1 == "piedra" and opcion_usuario2 == "papel":
        puntaje_usuario2 = puntaje_usuario2 + 1
        print(f"\n{nombre_usuario2} suma una victoria")
        print(f"{nombre_usuario2} tu puntaje actual es {puntaje_usuario2}")

    elif opcion_usuario1 == "piedra" and opcion_usuario2 == "tijeras" :
        puntaje_usuario1 = puntaje_usuario1 + 1
        print(f"\n{nombre_usuario1} suma una victoria")
        print(f"{nombre_usuario1} tu puntaje actual es {puntaje_usuario1}")

    elif opcion_usuario1 == "papel" and opcion_usuario2 == "piedra" :
        puntaje_usuario1 = puntaje_usuario1 + 1
        print(f"\n{nombre_usuario1} suma una victoria")
        print(f"{nombre_usuario1} tu puntaje actual es {puntaje_usuario1}")

    elif opcion_usuario1 == "papel" and opcion_usuario2 == "tijeras":
        puntaje_usuario2 = puntaje_usuario2 + 1
        print(f"\n{nombre_usuario2} suma una victoria")
        print(f"{nombre_usuario2} tu puntaje actual es {puntaje_usuario2}")
    
    elif opcion_usuario1 == "tijeras" and opcion_usuario2 == "piedra":
        puntaje_usuario2 = puntaje_usuario2 + 1
        print(f"\n{nombre_usuario2} suma una victoria")
        print(f"{nombre_usuario2} tu puntaje actual es {puntaje_usuario2}")
    
    elif opcion_usuario1 == "tijeras" and opcion_usuario2 == "papel" :
        puntaje_usuario1 = puntaje_usuario1 + 1
        print(f"\n{nombre_usuario1} suma una victoria")
        print(f"{nombre_usuario1} tu puntaje actual es {puntaje_usuario1}")


if puntaje_usuario1 == 3 :
    print(f"\n¡FELICIDADES {nombre_usuario1}, ERES EL GANADOR!\n")
elif puntaje_usuario2 == 3 :
    print(f"\n¡FELICIDADES {nombre_usuario2}, ERES EL GANADOR!\n")
else :
    print("\n*******************************************")
    print(f"**** ¡Juego terminado, no hay ganador! ****")
    print("*******************************************\n")



