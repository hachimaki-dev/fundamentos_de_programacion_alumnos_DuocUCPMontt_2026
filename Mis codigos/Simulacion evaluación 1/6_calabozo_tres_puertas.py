# 6. El Calabozo de las 3 Puertas (Anidados Pro)
# Simula una aventura donde debes atravesar 3 habitaciones consecutivas para ganar.

# Requerimientos:
# 1. Usa un ciclo para las 3 habitaciones (for i in range(1, 4)).
# 2. En cada habitación, hay una puerta cerrada. El jugador debe elegir: 'Forzar', 'Ganzúa' o 'Buscar Llave'.
# 3. Lógica de la habitación:
#     - Si elige 'Buscar Llave', hay un 50% de probabilidad (puedes simularlo pidiendo un número y viendo si es par) de encontrarla. Si la tiene, puede abrir.
#     - Si elige 'Ganzúa', debe tener la habilidad (pregunta al inicio del juego si es Ladrón o Guerrero). Solo el Ladrón abre con ganzúa.
#     - Si elige 'Forzar', debe ser Guerrero.
# 4. Si el jugador no logra abrir la puerta tras 3 intentos fallidos por habitación (ciclo while interno), pierde el juego completo.

# Desglose de Lógica:
# Un 'for' de 1 a 3 para las habitaciones. Dentro, un 'intentos = 0' y un 'while intentos < 3 and not abierta:'. 
# Pide la acción y usa IFs anidados para comparar la acción con la clase del personaje elegida al inicio.


habilidad_jugador = ""
asignar_habilidad = False
terminar_juego = False
numero = 0

print(" EL CALABOZO DE LAS TRES PUERTAS ".center(45, "-"))
print("\nEn esta aventura deberas atravesar tres habitaciones consecutivas para ganar ...")

while asignar_habilidad == False:
    habilidad_jugador = input("\n¿Quieres ser 'Ladron' o 'Guerrero'? ").upper()
    if habilidad_jugador == "LADRON" or habilidad_jugador == "GUERRERO":
        print(f"\nHas elegido {habilidad_jugador}")
        asignar_habilidad = True
    elif habilidad_jugador == "SALIR":
        print("\n--------------------------")
        print("---- Juego Finalizado ----")
        print("--------------------------\n")
        terminar_juego = True
        break
    else:
        print("Ingrese una opcion valida o 'Salir' para finalizar el juego")

if terminar_juego == False:
    for habitacion in range(1,4):
        intentos = 0
        no_abierta = True
        if habilidad_jugador == "GUERRERO":
            while intentos < 3 and no_abierta:
                eleccion_jugador = input("\n1. Forzar | 2. Ganzua | 3. Buscar Llave: ").upper()
                if eleccion_jugador == "SALIR" or eleccion_jugador == "9":
                    print("\n--------------------------")
                    print("---- Juego Finalizado ----")
                    print("--------------------------\n")
                    terminar_juego = True
                    break
                elif eleccion_jugador == "FORZAR" or eleccion_jugador == "1":
                    print(f"\n¡Felicidades! Has salido de la habitacion {habitacion}")
                    no_abierta = False
                elif eleccion_jugador == "GANZUA" or eleccion_jugador == "2":
                    intentos += 1
                    print("\nNo tienes habilidad para abrir con ganzua, pierdes un intento")
                    print(f"Intentos disponibles: {3 - intentos}")
                elif eleccion_jugador == "BUSCAR LLAVE" or eleccion_jugador == "3":
                    print("Tienes un 50% de probabilidades de abrir la puerta...")
                    numero = int(input("Ingresa un numero: "))
                    if numero % 2 == 0:
                        print(f"\n¡Felicidades! Has salido de la habitacion {habitacion}")
                        no_abierta = False
                    else:
                        intentos += 1
                        print("\nIncorrecto. Has perdido un intento")
                        print(f"Intentos disponibles: {3 - intentos}")
                else:
                    print("\nIngresa una opcion o valida o 9. 'Salir' para terminar el juego")

                if intentos == 3:
                    no_abierta = False
                    print("\n-----------------------------------------------------")
                    print("     Te quedaste sin intentos. Perdiste el juego")
                    print("-----------------------------------------------------\n")
                    terminar_juego = True
                           
        elif habilidad_jugador == "LADRON":
            while intentos < 3 and no_abierta:
                eleccion_jugador = input("\n1. Forzar | 2. Ganzua | 3. Buscar Llave: ").upper()
                if eleccion_jugador == "SALIR" or eleccion_jugador == "9":
                    print("\n--------------------------")
                    print("---- Juego Finalizado ----")
                    print("--------------------------\n")
                    terminar_juego = True
                    break
                elif eleccion_jugador == "FORZAR" or eleccion_jugador == "1":
                    intentos += 1
                    print("\nNo tienes suficiente fuerza, pierdes un intento")
                    print(f"Intentos disponibles: {3 - intentos}")
                elif eleccion_jugador == "GANZUA" or eleccion_jugador == "2":
                    print(f"\n¡Felicidades! Has salido de la habitacion {habitacion}")
                    no_abierta = False
                elif eleccion_jugador == "BUSCAR LLAVE" or eleccion_jugador == "3":
                    print("\nTienes un 50% de probabilidades de abrir la puerta...")
                    numero = int(input("Ingresa un numero: "))
                    if numero % 2 == 0:
                        print(f"\n¡Felicidades! Has salido de la habitacion {habitacion}")
                        no_abierta = False
                    else:
                        intentos += 1
                        print("\nIncorrecto. Has perdido un intento")
                        print(f"Intentos disponibles: {3 - intentos}")
                else:
                    print("\nIngresa una opcion o valida o 9. 'Salir' para terminar el juego")

                if intentos == 3:
                    no_abierta = False
                    print("\n-----------------------------------------------------")
                    print("     Te quedaste sin intentos. Perdiste el juego")
                    print("-----------------------------------------------------\n")
                    terminar_juego = True
        
        if terminar_juego:
            break
    
    if terminar_juego == False:
        print("\n---------------------------------")
        print("     ¡FELICIDADES! ¡GANASTE!")
        print("---------------------------------\n")