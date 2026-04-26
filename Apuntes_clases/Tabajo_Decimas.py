import random
#Dicionarios
Pikachu = {"pokemon":"Pikachu","tipo":"Electrico","vida":20}
Charizard = {"pokemon":"Charizard","tipo":"Fuego","vida":20}
Venasaur ={"pokemon":"Venasaur","tipo":"Planta","vida":20}
Blastoise ={"pokemon":"Blastoise","tipo":"Agua","vida":20}
#Variables
Pokemones_jugador = [Pikachu,  Charizard,  Venasaur, Blastoise]
Pokemones_rival = ["Sandslash", "Gyarados", "Exeggutor", "Arcanine"]
Pokemones_Debilitados = []
Pokemon_activo_jugador = []
Pokemon_activo_rival = []
Combate = True
Error= "Opcion Invalida"
SeleccionJugador= True
Tipo_pokemon = ""
vida_pokemon_activo = ""
SelecionRival = True



while Combate == True:
    

    while SeleccionJugador == True:
        print(f"¿Con cual pokemon quieres iniciar?")
        print("Opciones:")
        
        for i in Pokemones_jugador:
            print (i)
        Pokemon_Yo_Te_Elijo = dict(input("Elija un pokemon "))

        if Pokemon_Yo_Te_Elijo in Pokemones_jugador:
            Pokemon_activo_jugador.append(Pokemon_Yo_Te_Elijo)
            Pokemones_jugador.remove(Pokemon_Yo_Te_Elijo)
            SeleccionJugador= False
        else:
            print (Error)


    print(f"DEBUG {Pokemones_jugador} y {Pokemon_activo_jugador}")  

    print(Pokemon_activo_jugador[0]["tipo"])       
            
    #Selecion Rival  
    while SelecionRival == True:
    
        rival = random.choice(Pokemones_rival)
        print(f"Tu rival va a comenzar con {rival}")
        Pokemon_activo_rival.append(rival)
        Pokemones_rival.remove(rival)
        SelecionRival = False
    
    #print(f"DEBUG {Pokemones_rival} y {Pokemon_activo_rival}")  
    
  
    
    
    Combate=False    





