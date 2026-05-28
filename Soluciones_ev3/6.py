while True:
    patente = input("Ingrese la patente del vehiculo: ")

    if len(patente) == 6 and " " not in patente:
        print(f"Patente registrada con exito: {patente}")
        break
    else:
        print("Patente invalida. Ingresa exactamente 6 caracteres sin espacios.")
