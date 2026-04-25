import random
Pokemones_1 = ["Pikachu",  "Charizard",  "Gengar",  "Ninetales-Alola", " Tyranitar",  "Gardevoir"]
Pokemones_2 = ["Sandslash", "Snorlax", "Flygon", "Mimikyu", "Swampert"," Weavile"]
while True:
    Pokemon_Yo_Te_Elijo = input(f"¿Con cual pokemon quieres iniciar?{Pokemones_1}")
    print(f"Has comenzado con {Pokemon_Yo_Te_Elijo}")
    rival = random.choice(Pokemones_2)
    print(f"Tu rival va a comenzar con {rival}")

