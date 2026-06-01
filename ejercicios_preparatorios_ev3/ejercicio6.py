while True:

    patente_auto = input("Ingrese su patente: ")

    if len(patente_auto) == 6 and " " not in patente_auto:
        print(f"Patente valida: {patente_auto}")
        break  
    else:
        print("Patente inválida. Ingresa exactamente 6 caracteres sin espacios.") 
    