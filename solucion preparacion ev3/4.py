while True:
    clave = input("ingrese una contraseña con minimmo de 6 caracteres y sin espacios")
    for i in clave:
        if i in clave == " ":
            print("ingrese su contraseña sin espacios")
            continue
        elif len(clave) < 6:
            print("minimo de 6 carecteres")
            continue
        elif len(clave) >= 6 and i in clave != " ":
            print("contraseña permitida")
            break