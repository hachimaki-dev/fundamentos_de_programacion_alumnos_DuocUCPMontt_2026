while True:
    nombre_de_usuario = input("inresa un nombre de usuario  ")

    if len(nombre_de_usuario) >=6 and " " not in nombre_de_usuario:
        print(f"perfesto su nomre de usuario es: {nombre_de_usuario}")
        break
    else:
        print("invalido , minimo 6 caraster , sin espasio")
     
        