while True:
    usuario = input("Crea tu nombre de usuario: ")
    if len(usuario) >= 6 and " " not in usuario:
        print(f"Usuario creado: {usuario}")
        break
    else:
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")