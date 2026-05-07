
mochila = ['mapa', 'espada']
piso = ['madera', 'piedra', 'oro']
limite_maximo = 4


for objeto in piso:
    mochila.append(objeto) 
    print(objeto)
    if len(mochila) == limite_maximo:
        print("Lleno\n")
        break 

print("objetos de la mochila:", mochila)

