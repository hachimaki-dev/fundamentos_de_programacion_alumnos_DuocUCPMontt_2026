mochila = ["mapa", "espada"]
cosas_piso = ["madera", "piedra", "oro"]

print(f"Objetos en la mochila: {mochila}")
print(f"Objetos en el piso: {cosas_piso}")

for cosa in cosas_piso:
    print(f"Recoger {cosa}")
    mochila.append(cosas_piso[0])
    cosas_piso.pop(0)
    print(f"El inventario tiene {len(mochila)} objetos")
    if len(mochila) == 4:
        
        print("Lleno")
        break
    
print(f"Objetos en el inventario: {mochila}")