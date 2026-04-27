print("Bienvenido a *Después de ti*")

cigarros_fumados = 0
relacion = 0
dia = 1

while dia <= 3:  # puedes cambiar la cantidad de días
    print(f"\n--- Día {dia} ---")
    horas = 16

    while horas > 0:
        print(f"\nTe quedan {horas} horas en el día.")
        print("¿Qué deseas hacer?")
        print("1. Ver a Pilar (3 horas)")
        print("2. Jugar videojuegos (2 horas)")
        print("3. Fumar (1 hora)")
        print("4. Dormir (pasar el día)")

        eleccion = input("Elige una opción: ")

        if eleccion == "1":
            if horas >= 3:
                print("Pasas tiempo con Pilar ❤️")
                relacion += 2
                horas -= 3
            else:
                print("No tienes suficiente tiempo.")

        elif eleccion == "2":
            if horas >= 2:
                print("Juegas videojuegos 🎮")
                horas -= 2
            else:
                print("No tienes suficiente tiempo.")

        elif eleccion == "3":
            if horas >= 1:
                print("Fumas un cigarro 🚬")
                cigarros_fumados += 1
                horas -= 1
            else:
                print("No tienes suficiente tiempo.")

        elif eleccion == "4":
            print("Decides descansar y terminar el día.")
            break

        else:
            print("Opción inválida.")

    dia += 1

# 🔚 FINAL
print("\n--- FINAL ---")

if cigarros_fumados >= 10:
    print("Desarrollas cáncer de boca... Final trágico.")
elif relacion >= 5:
    print("Logras una relación hermosa con Pilar ❤️")
else:
    print("Tu vida sigue sin grandes cambios.")