#Haz que un programa cuente cuántas veces se repite una palabra en un texto.

comentario_cliente = 'buen servicio mal precio buen ambiente'
contador = 0 
freq = {
    'buen': 0,
    'mal': 0
}

#Reglas de Negocio: Tienes que desarmar la frase en palabras sueltas. Luego, revisas si la palabra que estás mirando está en tu diccionario. Si está, le sumas 1 a su contador.

#Restricciones: Usa `.split()` para picar la frase en una lista de palabras. Usa un `for` para recorrerlas. Usa `if palabra in freq:` para evitar que el código explote con palabras que no te interesan (como 'servicio' o 'precio'). Imprime tu diccionario contador al terminar.

palabras = comentario_cliente.split()

for palabra in palabras:
    if palabra in freq:
        freq[palabra] += 1

print(freq)