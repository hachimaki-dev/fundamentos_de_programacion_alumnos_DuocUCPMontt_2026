mochila = ["mapa", "espada"]
loot = ["madera", "piedra", "oro"]

for i in loot:
    mochila.append(i)
    if len(mochila) == 4:
        print("Lleno")
        break

print(mochila)