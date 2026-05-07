
mochila = ["mapa" , "espada"]
cosas_suelo = ["madera","piedra","oro"]
for cosas in cosas_suelo:
    mochila.append(cosas)
    if len(mochila) == 4:
        print("--lleno--")
        break
print(mochila)
