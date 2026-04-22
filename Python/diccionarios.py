## Diccionarios 
# Un diccionario es una estructura de datos mutable y no ordenada que permite almacenar pares de claves-valor. Cada elemento en una diccionario consiste en una clave unica y su valor correspondiente Los diccionarios se encierran entre llaves {} , y los pares clave-valor se separan por comas. 

## Creacion y acceso 
# Para crear un diccionario , utiliza llaves y separa las claves y valores con dos puntos
persona = {"nombre":"juan","edad":25,"ciudad":"madrid"}
# Para acceder a los valores de un diccionario , utiliza la clave correspondiente entre corchetes
print(persona["nombre"]) # Imprime "Juan"
print(persona["edad"]) # Imprime 25
print(persona["ciudad"]) # Imprime "madrid"
# Tambien puedes utilizar el metodo get() para obtener el valor de una clave. Si la clave no existe , devuelve un valor predeterminado (por defecto , none)

## Metodos de diccionarios
# Los diccionarios en Python tienen varios metodos incorporados para manipular y acceder a los elementos. Algunos metodos comunes son :
# keys() = devuelve una vista de todas las claves del diccionario
# values() = devuelve una vista de todos los valores del diccionario
# items() = devuelve una vista de todoos los pares clave-valor del diccionario
# update(otro_diccionario) = actualiza el diccionario con los pares clave-valor de otro diccionario

# Ejemplo 

persona = {"nombre" : "Juan" , "edad" : 25 , "ciudad" : "Madrid"}

print(persona.keys()) # Imprime dict_keys (["nombre", "edad" , "ciudad"])
print(persona.values()) # Imprime dict_values (["Juan" , 25 , "Madrid"])
print(persona.items()) # Imprime dict_items (["nombre" ,])