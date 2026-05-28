numero_pasajeros = 0

while numero_pasajeros <= 0 :
    try :
        numero_pasajeros = int(input("Ingrese la cantidad de pasajeros: "))

        if numero_pasajeros > 0 :
            break
        else :
            print("Error: ingresa un número entero positivo de pasajeros.")
    except ValueError :
        print("Error: ingresa un número entero positivo de pasajeros.")

print(f"Vuelo registrado con {numero_pasajeros} pasajeros.")