edad_registrada = 0

while edad_registrada <= 0 :
    try :
        edad_registrada = str(input("Ingrese la edad del conductor: "))

        if edad_registrada > 0 :
            break
        else :
            print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")
    except ValueError :
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")

print(f"Edad registrada: {edad_registrada} años.")