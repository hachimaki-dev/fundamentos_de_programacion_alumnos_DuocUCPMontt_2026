mochila = ["mapa", "espada"]
piso = ["madera", "piedra", "oro"]

for recogiendo in piso:
    mochila.append(recogiendo)    
    if len(mochila) == 4:
        print("lleno")
        break
print(mochila)
