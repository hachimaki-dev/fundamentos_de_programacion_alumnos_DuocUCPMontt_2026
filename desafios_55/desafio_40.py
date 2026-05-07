mochila = ['mapa', 'espada']
piso = ['madera', 'piedra', 'oro']
limite_mochila = 4

for objeto in piso:
    mochila.append(objeto)

    if len(mochila) == limite_mochila:
        print("Lleno")
        break

print(mochila)