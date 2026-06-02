#Ejercicio 17 — Control de aforo en un evento masivo
#Un evento de música comienza con aforo de 500 cupos disponibles. El control de acceso usa:

#=== CONTROL DE ACCESO - FESTIVAL AUSTRAL ===
#1. Ver cupos disponibles
#2. Registrar entrada de grupo
#3. Registrar salida de grupo
#4. Total de personas que han ingresado
#5. Salir

opcion = 0
aforo = 500
total = 0
personas_dentro = 0

while True:
    print("\n=== CONTROL DE ACCESO - FESTIVAL AUSTRAL ===")
    print("1. Ver cupos disponibles")
    print("2. Registrar entrada de grupo")
    print("3. Registrar salida de grupo")
    print("4. Total de personas que han ingresado")
    print("5. Salir")

    while True:
        try:
            opcion = int(input("Ingresa número de la opción: "))
            if 1 <= opcion <= 5:
                break
            else:
                print("Error: Ingrese una opción válida")
        except ValueError:
            print("Error: Ingrese una opción válida")
    
    if opcion == 5:
        print(f"Saliste. Se usaron {total} cupos")
        break

    elif opcion == 1:
        cupos_disponibles = aforo - personas_dentro
        print(f"\nHay {cupos_disponibles} cupos disponibles.")

    elif opcion == 2:
        while True:
            try:
                entrada = int(input("\nEntrada de clientes: "))
                if entrada <= 0:
                    print("Error: La cantidad de ingresos debe ser mayor a 0.")
                elif (entrada + personas_dentro) > aforo:
                    print("Error: El aforo del recinto ha sido superado.")
                else:
                    personas_dentro += entrada
                    total += entrada
                    if personas_dentro == aforo:
                        print("Aforo máximo alcanzado")
                    print(f"Ingresaron {entrada} personas al festival.")
                    break
            except ValueError:
                print("Error: Ingresa la cantidad en fomarto numérico.")

    elif opcion == 3:
        while True:
            try:
                salida = int(input("\nSalida de clientes: "))
                if salida <= 0:
                    print("Error: La cantidad de salidas debe ser mayor a 0.")
                elif salida > personas_dentro:
                    print("Error: No pueden salir más personas de la que ingresaron.")
                else:
                    personas_dentro -= salida
                    print(f"Salieron {salida} personas del festival.")
                    break
            except ValueError:
                print("Error: Ingresa la cantidad en fomarto numérico.")

    elif opcion == 4:
        print(f"\nIngresaron {total} personas al festival.")