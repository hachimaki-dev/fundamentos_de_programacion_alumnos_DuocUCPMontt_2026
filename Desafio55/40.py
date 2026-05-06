mochila = ['mapa', 'espada']
piso = ['madera', 'piedra', 'oro']
for cosa in piso:
    mochila.append(cosa)
    if len(mochila) >= 4:
        print("Lleno")
        break

print(mochila)