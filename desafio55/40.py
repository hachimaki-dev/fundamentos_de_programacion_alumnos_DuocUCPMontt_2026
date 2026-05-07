mochila = ["mapa","espada"]
cosas_nuevas = ['madera', 'piedra', 'oro']
contador = 0
for i in mochila:
    mochila.append(cosas_nuevas[contador])
    contador = contador + 1
    if len(mochila) == 4:
        print("mochila llena")
        break

print(mochila)