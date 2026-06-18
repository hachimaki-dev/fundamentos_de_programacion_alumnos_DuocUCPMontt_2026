# Ejercicio 6 — Patente de vehículo en un estacionamiento

while True:

    patente = input("Ingrese la patente: ")

    if len(patente) == 6 and " " not in patente:
        print(f"Patente registrada: {patente}")
        break

    else:
        print("Patente inválida. Ingresa exactamente 6 caracteres sin espacios.")