#Biblioteca de juegos steam

#arreglo_random = ["causa", 1, 2, "café", 9]

#arreglo_random_nombre = ["Carlo", "Josmer", "Conner"]
#arreglo_random_edad = [31, 19, 19]
#arreglo_random_estatura = [1.71, 1.76, 1.70]
biblioteca_steam = ["cs 1.6", "TFT2", "L4D","Half life","Portal", "Dota2", "Monster Hunter"]

#HalfLife imprimir
print(biblioteca_steam[3])

#Obtener longitud de la biblioteca o cantidad de caracteres
print(len(biblioteca_steam))

#añadir un elemento a la lista
biblioteca_steam.append("Among us")
print(biblioteca_steam)
#Eliminar ultimo elemento
#biblioteca_steam.pop()amongus

#ELIMINAR un elemento en base a su indice
#biblioteca_steam.pop(3)
#ELIMINAR un elemento por su nombre o valor.
biblioteca_steam.remove("Portal")
#por cada elemento dentro de una coleccion de elementos
contador = 0
for juego in biblioteca_steam:
 print(f"juego N {contador} {juego}")
 contador += 1
