## Listas de comprension
# Las listas de comprension son una forma concisa de crear nuevas listas basadas en una secuencia existente , Permiten filtrar y transformar los elementos de una lista en una sola linea

#nueva_lista = [expresion for elemento in secuencia if condicion]

numeros = [1 , 2 , 3 , 4 , 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados) # imprime [4 , 16]