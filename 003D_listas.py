# Mi biblioteca de juegos en Steam.

mi_juego1 = "Left 4 Dead"
mi_juego2 = "Cs 1.6"
mi_juego3 = "Half Life"
mi_juego4 = "Portal 2"
mi_juego5 = "DOTA 2"
mi_juego6 = "Monster Hunter Wilds"
mi_juego7 = "Golfin over it with Alva Majo"

biblioteca_steam = ["Cs 1.6", "Left 4 Dead", "Half Life", "Portal 2", "Monster Hunter Wilds"]

print(biblioteca_steam)

biblioteca_steam.append("Among Us")
biblioteca_steam.append("Sonic")
biblioteca_steam.append("Pokémon")

print(biblioteca_steam)

biblioteca_steam.pop()
biblioteca_steam.remove("Portal 2")

print(biblioteca_steam)

for i in range(len(biblioteca_steam)) :
    print(f"{i+1}) {biblioteca_steam[i]}")