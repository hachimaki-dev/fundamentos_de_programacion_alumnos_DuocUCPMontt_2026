nombre_usuario = ""

while True:
    try :
        nombre_usuario = str(input("Ingrese el nombre del usuario: "))

        if len(nombre_usuario) > 5 and not " " in nombre_usuario:
            break
        else :
            print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")
    except TypeError :
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")

print(f"Usuario creado: {nombre_usuario}.")