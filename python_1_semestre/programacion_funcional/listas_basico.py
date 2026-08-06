#LISTAS:

lista = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"]
#se accede al dato atravez del indice con corchetes y llamando la lista y indice . te da lo que esta 
#adentro.
#index = "indice"
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#len(lista): da el valor total de elementos de la lista:
print(len(lista))

#.append: agrega a la lista un elemeno , resultado o variable al final de la lista y ya 
#su es escructura es : nombre_de_la_lista.append("elemento_a_agregar")
lista.append("goku")
print(lista)

# insert(numero_indice, elemento) esa es la estructura puede ser str , int, o float o resultado
# agrega a la lista por su N.indice y el elemento , en el indice dado moviendo los demas 1 a la derecha
lista.insert(0,"otro_pokemon")
print(lista)

# .pop() | .remove("texto_a_buscar") | 
# el .pop() elimina el ultimo elemento sin pregunat
lista.pop()
print(lista)
# el .remove("texto_a_buscar") elimina el parametro dado y busca ese en especifico para borrar
lista.remove("Pikachu")
print(lista)

# FOR CON LAS LISTAS: 
# sirve para leer elementos o variables y tanto tambien para transmutar las listas 
#originales cambiando su valor global. 

#modelo de "no me toques" estrae copias fugases de cada elemento de la lista:
#el for itera la cantidad de  elementos que hay en la lista.
# si intento cambiar el valor de pokemones = "algo" . esto no cambia nada y 
# la lista esta intacta.
for pokemones in lista:
    print("los pokemones que habitan son : ,",pokemones)

# el modelo avanazado de for : "for para mutar o cambiar la lista" :
# se transforma la lista en len(lista) con el operador de numero range() = 
# range(len(lista)) su union ingresa a la lista con su indice y elemento pudiendo asi
# cambiar los elementos de la lista de manera interna y global a todos los datos. 
# asignando nuevos datos  o valores a la lista completa:
lista_de_numeros = [ 1 , 2 , 3, 4, 5]
for numeros in range(len(lista_de_numeros)):
    lista_de_numeros[numeros] = lista_de_numeros[numeros] + 1
    print(lista_de_numeros[numeros])
print(lista_de_numeros)
print(lista_de_numeros[numeros])
#
