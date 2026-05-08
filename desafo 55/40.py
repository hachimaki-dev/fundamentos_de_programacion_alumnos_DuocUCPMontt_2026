mochila = ["mapa", "esspada"]

cosas_del_piso = ["madera", "piedra", "oro"]

for objeto in cosas_del_piso:
    mochila.append(objeto)

    if len(mochila) == 4:
        print("lleno")
        break

print(mochila)