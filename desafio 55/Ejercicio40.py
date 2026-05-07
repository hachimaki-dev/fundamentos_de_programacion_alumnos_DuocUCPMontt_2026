mochila = ["mapa", "espada"]
item_piso = ["madera", "piedra", "oro"]
print(f"En tu inventario tienes {mochila}")
for item in item_piso:
    print(f"Recoges {item}")
    if len(mochila) == 4:
        print("Inventario lleno")
    else:
        print(f"se ha agregado {item} a tu inventario")
        mochila.append(item)
print(f"Tu inventario tiene {mochila}")
