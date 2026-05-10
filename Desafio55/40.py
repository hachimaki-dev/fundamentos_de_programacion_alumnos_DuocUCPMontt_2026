mochila=["mapa", "espada"]
piso=["madera", "piedra", "oro"]
for x in piso:
    mochila.append(x)
    if len(mochila)==4:
        print("Lleno")
        print(mochila)
        break
