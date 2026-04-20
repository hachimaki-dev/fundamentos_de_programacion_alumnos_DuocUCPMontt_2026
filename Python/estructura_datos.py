#Listas
#Es una estructura de datos mutable y ordenada que permite almacenar una coleccion de elementos. se cierran entre corchetes [] , separado por comas.
##Creacion y acceso 
frutas = ["manzanas" , "banana" , "naranja"]

#para acceder a los elementos de una lista , utiliza el indice del elemento entre corchetes. comienzan en 0
print(frutas[0]) #imprime "manzanas"
print(frutas[1]) #imprime "banana"
print(frutas[2]) #imprime "naranja"

#Tambien puedes acceder a los elementos desde el final de la lista utilizando indices negativos -1 representa el ultimo elemento , -2 representa el penultimo , asi sucesivamente 
print(frutas[-1]) #imprime "naranja"
print(frutas[-2]) #imprime "banana"
print(frutas[-3]) #imprime "manzana"

# Metodos de listas 
# Las listas en python tienen varios metodos incorporados que nos permiten manipular y modificar los elementos de la lista 
# append(elemento) = agrega un elemento al final de la lista
# insert(indice , elemento) = inserta un elemento en una posicion especifica de la lista 
# remove(elemento) = elimina la primera aparicion de un la lista
# pop(indice) = elimina y devuelve el elemento en una poscion especifica de la lista
# sort() = ordena los elementos de la lista en orden ascendente
# reverse() = invierte el orden de los elementos en la lista

##ejemplo

frutas = ["manzana" , "banana" , "naranja"]

frutas.append("pera") # imprime ["manzana" , "banana" , "naranja" , "pera"]

frutas.insert(1 , "uva") # imprime ["manzana" , "uva" , "banana" , "naranja" , "pera"]

frutas.remove("banana") # imprime ["manzana" . "uva" , "naranja" , "pera"]

fruta_eliminada = frutas.pop(2) 
print(frutas) # imprime ["manzana" , "uva" , "pera"]
print(fruta_eliminada) # imprime ["naranja"]

frutas.sort()
print(frutas) # imprime ["manzana" , "pera" , "uva"]

frutas.reverse()
print(frutas) # imprime ["uva" , "pera" , "manzana"]
