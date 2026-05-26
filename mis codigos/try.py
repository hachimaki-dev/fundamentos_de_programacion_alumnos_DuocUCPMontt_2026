while True:
    try:
        edad = int(input("Por favor, introduce tu edad: "))
        if edad < 0:
            print("Tu edad no puede ser negativa.")
            continue  # Vuelve al inicio del bucle
        break  # Si todo sale bien, rompe el bucle
    except ValueError:
        print("¡Error! Debes introducir un número entero. Inténtalo de nuevo.")

print(f"Gracias. Tu edad registrada es: {edad}")