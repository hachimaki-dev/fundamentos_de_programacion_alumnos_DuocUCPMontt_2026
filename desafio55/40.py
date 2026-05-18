mochila = ['mapa', 'espada']
piso = ['madera', 'piedra', 'oro']

for i in mochila:
    if len(mochila) == 4:
        print("Mochila llena")
        print(mochila)
        break
    else:
        if len(mochila) <= 4:
            for cosas in piso:
                mochila.append(cosas)

print(mochila)