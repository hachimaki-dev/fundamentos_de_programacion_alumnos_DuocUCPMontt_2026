
mochila = ['mapa', 'espada']
piso = ['madera', 'piedra', 'oro']
limite = 4


for objeto in piso:
    mochila.append(objeto)
    
   
    if len(mochila) == limite:
        print("Lleno")
        break

# Estado final de la mochila
print(f"Mochila final: {mochila}")
