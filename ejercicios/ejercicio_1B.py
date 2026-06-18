# Ejercicio 1B — Registro de pasajeros en un vuelo

print("======================")
print("Problema de Aeropuerto")
print("======================")

while True:
    try:
        pasajeros = int(input("Ingrese el numero de pasajeros de avion: "))

        if pasajeros > 0:
            print(f"Vuelo registrado con {pasajeros} pasajeros")
            break

    except ValueError:
        print("Error, ingrese un numero entero por favor.")