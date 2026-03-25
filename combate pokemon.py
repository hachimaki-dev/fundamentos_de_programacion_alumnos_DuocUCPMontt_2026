import time
Pokemon1 = "Pikachu"
PokemonRival = "Eevee"
VidaPokemon1 = 20
VidaPokemonRival = 20
turno = True
Combate = True

while Combate == True:
        
    while turno == True:
        print (f"{Pokemon1} tiene {VidaPokemon1} puntos de vida \n {PokemonRival} tiene {VidaPokemonRival}")
        Accion = input(f"""¿Que deberia hacer {Pokemon1}? Opciones: 
                Atacar
                Curar
                Huir\n""" )
        if Accion == "Atacar" or Accion == "atacar":
            print(f"\n{Pokemon1} atacó a {PokemonRival}")
            VidaPokemonRival = VidaPokemonRival-5
            turno = False
        elif Accion == "Curar" or Accion == "curar":
            print(f"\n{Pokemon1} se curo")
            VidaPokemon1 = VidaPokemon1 + 2
            turno = False
            if VidaPokemon1 >= 20:
                    VidaPokemon1 = 20
        
        elif Accion == "Huir" or Accion == "huir":
            print(f"\nNO PUEDES HUIR")
            turno = False
        
        else:
            print("\nOpción invalida")
            turno = False
    print(f"Turno de {PokemonRival}")
    print(f"{PokemonRival} ataco a {Pokemon1} por {3} de daño")
    time.sleep(1)
    VidaPokemon1 = VidaPokemon1-3
    turno = True
if VidaPokemon1 <= 0 or VidaPokemonRival <= 0:
    Combate = False

print(f"\nCombate terminado")            