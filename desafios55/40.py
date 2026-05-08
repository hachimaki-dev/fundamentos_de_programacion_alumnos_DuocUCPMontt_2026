inventario = ['mapa', 'espada']
objetos = ['madera', 'piedra', 'oro']
limite_mochila = 4

for objeto in objetos:
    inventario.append(objeto)
    
    if len(inventario) == limite_mochila:
        print("LLENO")
        break
    
print(inventario)
    
    
    



