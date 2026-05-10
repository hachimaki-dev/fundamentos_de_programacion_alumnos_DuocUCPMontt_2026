inventario=['mapa', 'espada']
piso=['madera', 'piedra', 'oro']

for i in piso:
    if len(inventario) == 4:
        print('Lleno')
        break
    inventario.append(i)

print(inventario)    
        