while True:

    nombre_de_usuario = input("Cree su nombre de usuario : ")
    
    if len(nombre_de_usuario) < 6 or  " " in nombre_de_usuario:
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")
        continue
    else:
        print(f"Usuario Creado : {nombre_de_usuario}")
        break

