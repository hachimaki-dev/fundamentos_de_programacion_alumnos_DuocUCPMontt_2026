## Tuplas 

# Una tupla es una estructura de datos inmutable y ordenada que permite almacenar una coleccion de elementos. Los elementos de una tupla se encierran entre parentesis () , separados por comas.

## Creacion y acceso 
# para crear una tupla , encierra los elementos entre parentesis
punto = (3 ,4)
#para acceder a los elementos de una tupla , se utiliza el indice del elemento entre corchetes , similar a las listas :

print(punto[0]) # imprime 3
print(punto[1]) # imprime 4
# a diferencia de las listas , las tuplas son inmutables , lo que significa que no se pueden modificar una vez creadas. No se pueden agregar , eliminar o cambiar elementos en una tupla existente 
# Las tuplas son utiles cuando necesitas almacenar una coleccion de elementos que no deben modificarse , como coordenadas o datos de configuracion

## Metodos de tuplas
#Aunque las tuplas son inmutables , Python proporciona varios metodos utiles para trabajar con ellas
#count(elemento) = devuelve el numero de veces que aparece un elemento en la tupla
#index(elemento) = devuelve el indice de la primera aparicion de un elemento en la tupla. opcionalmente , se puede especificar el inicio y fin de la busqueda
#len(tupla) = aunque no es un metodo de tupla propiamente dicho , esta funcion incorporada devuelve la longitud de la tupla

mi_tupla = (1 , 2 , 3, 2 , 4 ,2)
print (mi_tupla.index(2)) #Salida : 1
print (mi_tupla.index(2 , 2)) #Salida : 3
print (mi_tupla.index(2, 2, 4))  #Salida : 3