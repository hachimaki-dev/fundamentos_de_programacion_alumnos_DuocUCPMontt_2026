while True:
    try:
        nombre_usuario = input("Cree su nombre de usuario: ")
        espacio = False
        for letra in nombre_usuario:
            if letra == " ":
                espacio = True
        if len(nombre_usuario) < 6 or espacio == True:
            print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")
    except:
        print("a")