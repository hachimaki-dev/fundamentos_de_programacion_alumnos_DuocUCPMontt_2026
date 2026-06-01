while True:
    nombre_usuario = input("Ingrese su nombre de usuario: ")

    if len(nombre_usuario) < 6 and " " in nombre_usuario:
        print("Nombre invalido, debe tener más de 6 caracteres y no contener espacios.")
    else:
        print(f"Usuario creado: {nombre_usuario}")
        break