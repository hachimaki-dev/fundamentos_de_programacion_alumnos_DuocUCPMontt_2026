grupo_ingresado = ""

while grupo_ingresado != "bts" and grupo_ingresado != "blackpink" and grupo_ingresado != "stray kids":
    grupo_ingresado = input("Ingresa tu grupo favorito: ").lower()

    if grupo_ingresado == "bts" or grupo_ingresado == "blackpink" or grupo_ingresado == "stray kids":
        print("Bienvenido al Fandom")