#Variables
Combate = True
Error= "Opcion Invalida"

Pokemon1 = "Heatmor"
Pokemon2 = "Cryonogal"
Pokemon3 = "Grandbull"
PokemonRival1 = "Spiritomb" #Hada x2
PokemonRival2 = "Lucario" #Fuego x2
PokemonRival3 = "Garchomp" #hielo x4
VidaPokemon1 = 20
VidaPokemon2 = 20
VidaPokemon3 = 20
VidaPokemonRival1 = 20
VidaPokemonRival2 = 20
VidaPokemonRival3 = 20

Combate = True
while Combate == True:
    print ("""                                   ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
LA CAMPEONA CYNTHIA TE DESAFIA A UN COMBATE""")

# Spirtomb
    Fase1 = True
    while Fase1 == True:
        if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
             Combate = False
        Opcion = int(input("""Seleccione uno de los siguientes pokemon:
                            1) Heatmor
                            2) Cryogonal
                            3) Grandbull
                            """))
        #OPCION HEATMOR (NO EFECTIVO)    
        if Opcion == 1:
                if VidaPokemon1 >= 0:
                     print (Error)
                else:
                    print (f"{Pokemon1} tiene {VidaPokemon1} puntos de vida \n {PokemonRival1} tiene {VidaPokemonRival1} puntos de vida")
                    Accion = input(f"""¿Que deberia hacer {Pokemon1}? Opciones: 
                            Atacar
                            Cambiar
                            Huir\n""" )
                    if Accion == "Atacar" or Accion == "atacar":
                        print(f"\n{Pokemon1} atacó a {PokemonRival1}")
                        VidaPokemonRival = VidaPokemonRival-5
                    elif Accion == "Cambiar" or Accion == "cambiar":
                        continue
                        
                                    
                    
                

                    elif Accion == "Huir" or Accion == "huir":
                        print(f"\nNO PUEDES HUIR")
                    else:
                        print(Error)
                    
                    print(f"{PokemonRival1} ataco a {Pokemon1}")
                    VidaPokemon1 = VidaPokemon1-5
                
        #OPCION CRYOGONAL (NO EFECTIVO)    
        elif Opcion == 2:
                if Pokemon2 >= 0:
                     print (Error)
                else:     
                    print (f"{Pokemon2} tiene {VidaPokemon1} puntos de vida \n {PokemonRival1} tiene {VidaPokemonRival1} puntos de vida")
                    Accion = input(f"""¿Que deberia hacer {Pokemon2}? Opciones: 
                            Atacar
                            Cambiar
                            Huir\n""" )
                    if Accion == "Atacar" or Accion == "atacar":
                        print(f"\n{Pokemon2} atacó a {PokemonRival1}")
                        VidaPokemonRival = VidaPokemonRival-5
                    elif Accion == "Cambiar" or Accion == "cambiar":
                        continue                         
                    
                

                    elif Accion == "Huir" or Accion == "huir":
                        print(f"\nNO PUEDES HUIR")
                    else:
                        print(Error)
                    print(f"{PokemonRival1} ataco a {Pokemon2}")
                    VidaPokemon2 = VidaPokemon2-5        
        #OPCION GRANDBULL (EFECTIVO)
        elif Opcion == 3:
                if Pokemon3 >= 0:
                     print(Error)
                else:
                    print (f"{Pokemon3} tiene {VidaPokemon3} puntos de vida \n {PokemonRival1} tiene {VidaPokemonRival1} puntos de vida")
                    Accion = input(f"""¿Que deberia hacer {Pokemon3}? Opciones: 
                            Atacar
                            Cambiar
                            Huir\n""" )
                    if Accion == "Atacar" or Accion == "atacar":
                        print(f"\n{Pokemon3} atacó a {PokemonRival1}")
                        VidaPokemonRival = VidaPokemonRival-10
                    elif Accion == "Cambiar" or Accion == "cambiar":
                        continue                         
                    
                

                    elif Accion == "Huir" or Accion == "huir":
                        print(f"\nNO PUEDES HUIR")
                    else:
                        print(Error)
                    print(f"{PokemonRival1} ataco a {Pokemon3}")
                    VidaPokemon3 = VidaPokemon3-2 
        
        
        if VidaPokemonRival >= 0:
             Fase1= False
             Fase2= True   

    
    
    if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0 or (VidaPokemonRival1+VidaPokemonRival2+VidaPokemonRival3) <= 0:
        Combate = False

print(f"\nCombate terminado")
if (VidaPokemon1+VidaPokemon2+VidaPokemon3) <= 0:
    print("Has perdido")
else:
    print("Has ganado")       


 





