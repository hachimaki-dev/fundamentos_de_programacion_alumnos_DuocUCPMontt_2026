mochila =["mapa", "espada"]
cosas_piso = ["madera", "piedra", "oro"]
for objetos in cosas_piso:
    mochila.append(objetos)
    if len(mochila) == 4:
        print("lleno")
        break 
print(mochila)