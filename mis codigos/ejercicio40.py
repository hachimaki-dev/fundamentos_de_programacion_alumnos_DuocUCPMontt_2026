mochila = ['mapa', 'espada']
piso = ['madera', 'piedra', 'oro']

for item in piso:
    
    mochila.append(item)
    
    if len(mochila) == 4:
        print("Lleno")
        
        break

print(mochila)