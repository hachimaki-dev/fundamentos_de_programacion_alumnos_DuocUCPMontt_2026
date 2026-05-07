mochila = ["mapa" ,"espada"]
encontrado = ["madera" ,"piedra" ,"oro"]

for i in encontrado:
    mochila.append(i)
    if len(mochila) == 4:
        print("mochila llena")
        break

    
print(mochila)
