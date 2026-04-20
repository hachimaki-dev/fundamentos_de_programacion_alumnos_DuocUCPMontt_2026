favoritos = [ "Para amar - Los Prisioneros", "Una nube cuelga sobre mi - Los Bunkers", "La Lisa - Lisa", "Milagrosa - Milo J", "Ven aqui - Los Bunkers", "Dimeloma - Marcianeke"]

print(favoritos[2])

print( len(favoritos)) #para saber la cantidad de elementos de algo
print(favoritos[-1])#solo se puede usar esa forma en python

favoritos.append("Congelao - Cachureo")#para agregar datos en el indice
favoritos.append("Mi gran noche - Rafael")

#avoritos.pop("Mi gran noche - Rafael")para borrar datos de la lista
favoritos.pop()#tambien se puede hacer asi

contador = 0
for cancion in favoritos:
    print(f" el nombre de la cancion {contador} es: {cancion}")
    contador += 1



#.insert(indice_num, elemento)
#Qué hace de vital? Cansado de ir al final, te permite forzar agresivamente la inserción de un elemento en una posición numérica y exacta, empujando pacíficamente a todos los vecinos actuales uno hacia la derecha para crear un espacio vacío y ceder paso.
#lista.insert(0, "Presidente") # Entra dictatorialmente a rango [0] inicial, el resto decae un sitio.

