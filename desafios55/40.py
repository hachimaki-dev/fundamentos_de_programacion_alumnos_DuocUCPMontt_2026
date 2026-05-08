mochila = ['Mapa', 'Espada']
cosas_piso = ['Madera', 'Piedra', 'Oro']
for cosa in cosas_piso:
    mochila.append(cosa)
    if len(mochila) == 4:
        print("lleno")
        break
print(mochila)