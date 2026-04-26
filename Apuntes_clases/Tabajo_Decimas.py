import random

#Variables
Pokemones_jugador = ["Pikachu",  "Charizard",  "Venasaur", "Blastoise"]
Pokemones_rival = ["Sandslash", "Gyarados", "Exeggutor", "Arcanine"]
Pokemones_Debilitados = []
Pokemon_activo_jugador = []
Pokemon_activo_rival = []
Combate = True
Error= "Opcion Invalida"
SeleccionJugador= True
Tipo_pokemon = ""
vida_pokemon_activo =
SelecionRival = True

#Dicionarios
dpikachu = {
    "tipo":"Electrico"
    "vida":20
}
dcharizard = {}

while Combate == True:
    

    while SeleccionJugador == True:
        print(f"¿Con cual pokemon quieres iniciar?")
        print("Opciones:")
        
        for i in Pokemones_jugador:
            print (i)
        Pokemon_Yo_Te_Elijo = (input("Elija un pokemon "))

        if Pokemon_Yo_Te_Elijo in Pokemones_jugador:
            Pokemon_activo_jugador.append(Pokemon_Yo_Te_Elijo)
            Pokemones_jugador.remove(Pokemon_Yo_Te_Elijo)
            SeleccionJugador= False
        else:
            print (Error)


    #print(f"DEBUG {Pokemones_jugador} y {Pokemon_activo_jugador}")  
           
            
    #Selecion Rival  
    while SelecionRival == True:
    
        rival = random.choice(Pokemones_rival)
        print(f"Tu rival va a comenzar con {rival}")
        Pokemon_activo_rival.append(rival)
        Pokemones_rival.remove(rival)
        SelecionRival = False
    
    #print(f"DEBUG {Pokemones_rival} y {Pokemon_activo_rival}")  
    
    Turno Jugador
    
    
    Combate=False    





