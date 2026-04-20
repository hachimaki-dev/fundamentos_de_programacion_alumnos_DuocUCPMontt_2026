canciones_favoritas = ["Paramar - Los Prisioneros", "Una nube cuelga sobre mi - Los Bunkers", 
"Milagrosa - Milo J", "Ven aqui - Los Bunkers", "Lalisa - Lisa", "Dimeloma - Marcianeke"]

# print(canciones_favoritas) # Toda la lista
# print(canciones_favoritas[2]) # Por posicion
# print(len(canciones_favoritas)) # Longitud de la lista, Cantidad de elementos
# print(canciones_favoritas[len(canciones_favoritas) - 1]) # Tamaño del arreglo - 1 = Ultimo elemento
# print(canciones_favoritas[-1]) # Ultimo elemento

# contador = 0
# for cancion in canciones_favoritas:
#     print(f"El nombre de la cancion {contador} es: {cancion}")
#     contador = contador + 1

canciones_favoritas.append("Congelao - Cachureos") # Agrega al final
canciones_favoritas.append("Mi gran noche - Rafael")

canciones_favoritas.pop() # Elimina la ultima

contador = 0
for cancion in canciones_favoritas:
    print(f"El nombre de la cancion {contador} es: {cancion}")
    contador = contador + 1