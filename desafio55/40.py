mochila = ["mapa", "espada"]
items = ["madera", "piedra", "oro"]
for item in items:
    if len(mochila) == 4:
        print("Lleno")
        print(mochila)
    mochila.append(item)