print("MINECRAFT")
mochila = ["Mapa", "Espada"]
piso = ["Madera", "Piedra", "Oro"]

for item in piso:
    mochila.append(item)
    if len(mochila) == 4:
        print("LLENO")
        break
    
print(mochila)