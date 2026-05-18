mochila = ['mapa' , 'espada']
piso = ['madera','piedra','oro']
limite=4

for objetos in piso:
    mochila.append(objetos)
    print(f"recogiste: {objetos}")

    if len(mochila)==limite:
        print("lleno")
        break

print("-----")
print(f"tu mochila final: {mochila}")
