mochila = ["mapa", "espada"]
espacio_maximo = 4
en_el_piso = ["madera" , "piedra" , "oro"]

for  objeto in en_el_piso:
    
    mochila.append (objeto)

    if len(mochila) == 5:
        print("llena")
    break 
print(mochila)