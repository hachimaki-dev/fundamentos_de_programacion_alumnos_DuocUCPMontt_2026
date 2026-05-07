mochila = ["mapa" , "espada"]

piso = ["madera" , "piedra" ,"oro"]

for m in piso:

    mochila.append(m)
    if len(mochila) == 4:
        print("lleno\n")
        break

print(mochila) 