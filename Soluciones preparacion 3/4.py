for i in range(1,4):
    nombre_del_usuario = input("Crea tu nombre de usuario :  ")

    if " " not in nombre_del_usuario:
        if len(nombre_del_usuario) < 6:
            print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")
            continue
        else:
            print(f"Usuario Creado :  {nombre_del_usuario} ")
            break
    else:
        print("No puede contener espacios")
        continue

