mochila = ['Mapa', 'Espada']
encontrados_piso = ['Madera', 'Piedra', 'Oro']
for recogidas in encontrados_piso:
    mochila.append(recogidas)
    if len(mochila) ==4:
        print("lleno")
        break
print(mochila)