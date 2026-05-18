mochila = ["mapa", "espada"]
piso = ["madera", "piedra", "oro"]
for cosas in piso:
    mochila.append(cosas)
    if len(mochila) == 4:
        print("Lleno")
        break
print(mochila)