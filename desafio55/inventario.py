

mochila = ["mapa", "espada"]
objeto_del_piso = ["madera","piedra","oro"]

for n in objeto_del_piso:
    mochila_espacio = len(mochila)
    if mochila_espacio == 4:
        print("lleno")
        break
    mochila.append(n)


print(mochila)
    
    
















