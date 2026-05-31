flag = True
while flag:
    patente_auto = input("Ingrese la patente de su vehiculo: ")
    if (len(patente_auto) == 6) and (" " not in patente_auto):
        print(f"Patente registrada: {patente_auto}.")
        flag = False
    else:
        print("Error, la patente debe tener 6 caracteres exactos, sin espacios.")
