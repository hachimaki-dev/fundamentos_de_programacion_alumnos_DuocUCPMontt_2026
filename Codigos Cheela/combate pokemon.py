Pokemon1 = "Pikachu"
PokemonRival = "Eevee"
VidaPokemon1 = 20
VidaPokemonRival = 20

Combate = True
while Combate == True:
    

    print (f"{Pokemon1} tiene {VidaPokemon1} puntos de vida \n {PokemonRival} tiene {VidaPokemonRival} puntos de vida")
    Accion = input(f"""¿Que deberia hacer {Pokemon1}? Opciones: 
               Atacar
               Curar
               Huir\n""" )
    if Accion == "Atacar" or Accion == "atacar":
        print(f"\n{Pokemon1} atacó a {PokemonRival}")
        VidaPokemonRival = VidaPokemonRival-5
    elif Accion == "Curar" or Accion == "curar":
        print(f"\n{Pokemon1} se curo")
        
        VidaPokemon1 = VidaPokemon1 + 2
        
        if VidaPokemon1 >= 20:
                VidaPokemon1 = 20
        

    elif Accion == "Huir" or Accion == "huir":
        print(f"\nNO PUEDES HUIR")
    else:
        print("\nOpción invalida")
    print(f"{PokemonRival} ataco a {Pokemon1}")
    VidaPokemon1 = VidaPokemon1-3

    if VidaPokemon1 <= 0 or VidaPokemonRival <= 0:
        Combate = False

print(f"\nCombate terminado")        
