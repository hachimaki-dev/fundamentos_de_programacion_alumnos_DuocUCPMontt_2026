# Ejercicio 40: Gestión de Inventario (Minecraft)

print("=================================")
print("Sistema de inventario del jugador")
print("=================================")

mochila = ['mapa', 'espada']
limite = 4

piso = ['madera', 'piedra', 'oro']

for item in piso:
    mochila.append(item)

    if len(mochila) == limite:
        print("Lleno")
        break

print(mochila)