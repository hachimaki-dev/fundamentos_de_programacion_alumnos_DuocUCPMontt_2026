mochila=["mapa","espada"
         ]
piso=["madera","piedra","oro"]
capacidad_max=4

for i in piso:
    if len(mochila) >= capacidad_max:
        print("lleno")
        break
    else :
        mochila.append(i)
print(mochila)