mochila = ["mapa", "espada",]
piso = ["madera ", "piedra", "oro"]
for objeto in piso:
    mochila.append(objeto)
    if len(mochila) == 4:
        print("Lleno")
        break
print (mochila)
