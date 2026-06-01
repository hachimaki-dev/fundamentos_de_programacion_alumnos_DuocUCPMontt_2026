while True:
    patente_vehiculo = input("Ingrese la patente de su vehiculo (Ejemplo: BB1234): ")

    if len(patente_vehiculo) == 6 and " " not in patente_vehiculo:
        
        print("Patente registrada con exito!")
        break
    
    else:
        print(f"Patente invalida {patente_vehiculo}, ingrese exactamente 6 caracteres sin espacios")