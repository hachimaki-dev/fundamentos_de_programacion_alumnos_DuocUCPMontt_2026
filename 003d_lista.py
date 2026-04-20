#Mi biblioteca de juegos en steam

mi_juego1 = "Cs 1.6"
mi_juego2 = "Team fortress"
mi_juego3 = "left 4 dead"
mi_juego4 = "portal 2"
mi_juego5 = "dota 2"
mi_juego6 = "Monster hunter wilds"
mi_juego7 = "golfin overin with alva majo"
mi_juego8 = "half-life"

#print(f"En mi biblioteca de steam tengo el {mi_juego1}")
#print(f"En mi biblioteca de steam tengo el {mi_juego8}")
#print(f"En mi biblioteca de steam tengo el {mi_juego2}")
#print(f"En mi biblioteca de steam tengo el {mi_juego3}")
#print(f"En mi biblioteca de steam tengo el {mi_juego4}")
#print(f"En mi biblioteca de steam tengo el {mi_juego5}")
#print(f"En mi biblioteca de steam tengo el {mi_juego6}")
#print(f"En mi biblioteca de steam tengo el {mi_juego7}")


#manera algoritmica

biblioteca_steam = ["Cs 1.6", "Team fortress", "left 4 dead", "portal 2", "dota 2", "Monster hunter wilds", "golfin overin with alva majo", "half-life"]

#Obtener tamaño o la longitud de algo
print(len(biblioteca_steam))

#agregar elementos a la lista

biblioteca_steam.append("Among us")
biblioteca_steam.append("Sonic")
biblioteca_steam.append("Pokemon")


biblioteca_steam.pop()#elimina el ultimo elemento

#quiero eliminar un juego con su nombre
biblioteca_steam.remove("portal 2")

contador = 0
for elemento in biblioteca_steam:
    print(f"Juego N° {contador} {elemento}")
    contador += 1