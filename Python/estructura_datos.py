#Listas
#Es una estructura de datos mutable y ordenada que permite almacenar una coleccion de elementos. se cierran entre corchetes [] , separado por comas.
##Creacion y acceso 
frutas = ["manzanas" , "banana" , "naranja"]

#para acceder a los elementos de una lista , utiliza el indice del elemento entre corchetes. comienzan en 0
print(frutas[0]) #imprime "manzanas"
print(frutas[1]) #imprime "banana"
print(frutas[2]) #imprime "naranja"

#Tambien puedes acceder a los elementos desde el final de la lista utilizando indices negativos -1 representa el ultimo elemento , -2 representa el penultimo , asi sucesivamente 
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

# Metodos de listas 
# Las listas en python tienen varios metodos incorporados que nos permiten manipular y modificar los elementos de la lista 
# append(elemento) = agrega un elemento al final de la lista
# insert(indice , elemento) = inserta un elemento en una posicion especifica de la lista 
# remove(elemento) = elimina la primera aparicion de un el