print("--- BIAS KPOP ---")

grupo_favorito = ""

while True:

    grupo_favorito = input("¿Cuál es tu grupo de kpop favorito?:").lower()

    if grupo_favorito != "BTS" and grupo_favorito != "BLACKPINK" and grupo_favorito != "Stray Kids":
        print("Lo siento no nos gusta ese grupo, intente de nuevo")
        continue