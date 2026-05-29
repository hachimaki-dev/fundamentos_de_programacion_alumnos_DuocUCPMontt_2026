while True:
    usuario = input("Ingrese su numero de usuario: ")


    if len(usuario) >= 6 and " " not in usuario and not usuario.isdigit():
        print(f"Usuario creado {usuario}")
        break
    else:
        print("Nombre invalido, debe tener minimo 6 caracteres")