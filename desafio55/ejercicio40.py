mochila = ["mapa","espada"]
piso = ["madera","piedra","oro"]
maximo = 4
for i in piso:
    mochila.append(i)
    if len(mochila) == maximo:
        print("Lleno")
        break
print(mochila)