mochila = ["mapa","espada"]
piso = ["madera","piedra","oro"]
for item in piso:
    if len(mochila) == 4:
        print("Lleno")
        break
    else:
        mochila.append(item)
print(mochila)