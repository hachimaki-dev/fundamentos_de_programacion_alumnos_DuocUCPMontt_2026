print("****************** GRUPO K POP ******************")

grupo_favorito = ""

while grupo_favorito != "bts" and grupo_favorito != "blackpink" and grupo_favorito != "stray kids":

    grupo_favorito = input("¿Cual es tu grupo favorito de K-POP?: ").lower()

    if grupo_favorito != "bts" and grupo_favorito != "blackpink" and grupo_favorito != "stray kids":
        print("¡Acceso Denegado! Intente de nuevo.")

print("¡Acceso Concedido! Bienvenido al Fandom.")