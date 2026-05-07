inventario = ["mapa", "espada"]
items_suelo = ["madera", "piedra", "oro"]

for n in inventario:
    espacio_mochila = len(inventario)
    if espacio_mochila == 4:
        print("Mochila Llena.")
        break
    inventario.append(items_suelo)
print(inventario)