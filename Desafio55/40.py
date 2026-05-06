mochila = ['mapa', 'espada']

encontrado = ['madera', 'piedra', 'oro']

for item in encontrado:
    if len(mochila) + 1 > 4:
        print("Lleno")
        break
    else:
        mochila.append(item)

print(mochila)