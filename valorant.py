print("Escoja una de las 3 opciones (BTS , BLACKPINK , Stray Kids)")
grupo_favorito = ""
while grupo_favorito != "bts" and grupo_favorito != "blackpink" and grupo_favorito != "stray kids":
    grupo_favorito = input("Ingrese su grupo favorito").lower()
    if grupo_favorito == "bts" or grupo_favorito == "blackpink" or grupo_favorito == "stray kids":
     print("Bienvenido al fandom")
     break