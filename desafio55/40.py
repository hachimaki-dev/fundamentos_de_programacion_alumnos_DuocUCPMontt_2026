mochila = ['mapa', 'espada']
piso_encontraste = ['madera', 'piedra', 'oro']

for i in piso_encontraste:
    mochila.append(i)
    if len(mochila) == 4:
        print("LLENO")
        break
print(mochila)


   

