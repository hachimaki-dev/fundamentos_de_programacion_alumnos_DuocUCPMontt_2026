nombre_patente = ""

while True:
    try :
        nombre_patente = str(input("Ingrese la patente: ")).upper()

        if len(nombre_patente) == 6 and not " " in nombre_patente:
            break
        else :
            print("Patente inválida. Ingresa exactamente 6 caracteres sin espacios.")
    except TypeError :
        print("Patente inválida. Ingresa exactamente 6 caracteres sin espacios.")

print(f"Patente ingresada: {nombre_patente}")