mochila = ["mapa", "espada"]

objetos_en_el_piso = ["madera", "piedra", "oro"]

for item in objetos_en_el_piso:
    if len(mochila) >= 4:
        print("Lleno!")
        break
    print(f"Añadiendo {item}")
    mochila.append(item)