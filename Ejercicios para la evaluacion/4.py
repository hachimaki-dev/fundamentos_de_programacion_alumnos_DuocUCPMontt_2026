flag = True
while flag:
    nombre_de_usuario = input("Ingrese un nombre de usuario: ")
    if len(nombre_de_usuario) < 6 or " " in nombre_de_usuario:
        print("Nombre invalido. Debe contener minimo 6 caracteres y sin espacios.")
    else:
        print(f"Usuario creado : {nombre_de_usuario}.")
        flag = False