mochila=["mapa","espada"]

piso=["madera","piedra","oro"]

for i in piso:
    mochila.append(i)
    if len(mochila)==4:
        print("Lleno")
        break
print(mochila)
