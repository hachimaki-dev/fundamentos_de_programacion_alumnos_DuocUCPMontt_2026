inventario = ['mapa', 'espada']
objetos_del_suelo = ['madera', 'piedra', 'oro']
contador = 0
for i in objetos_del_suelo:
    if len(inventario) < 4:
        inventario.append(i)
    else:
        print("inventario lleno")
        break
    print(inventario)
    