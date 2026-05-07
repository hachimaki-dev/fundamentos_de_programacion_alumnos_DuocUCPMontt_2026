mochila=["mapa","espada"]
piso=["madera","piedra","oro"]
capacidad_max=4

for i in piso:
    mochila.append(i)

    if len(mochila)==capacidad_max:
        print("lleno")
        break
print(mochila)