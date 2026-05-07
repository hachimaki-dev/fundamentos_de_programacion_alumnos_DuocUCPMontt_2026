mochila = ["mapa", "espada"]
objetos_en_el_piso = ["madera", "piedra", "oro"]

for objeto in objetos_en_el_piso :
    if len(mochila) >= 4 :
        print("Lleno")
    else :
        mochila.append(objeto)

print(mochila)