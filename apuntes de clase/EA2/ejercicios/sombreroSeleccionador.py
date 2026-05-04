'''Es el primer año en Hogwarts y tienes una lista de aspirantes. El Sombrero elegirá su casa dependiendo del tamaño de su nombre.

Instrucciones:

Crea una lista alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"] y otras dos listas vacías: gryffindor = [] y slytherin = [].
Recorre la lista alumnos con un ciclo for.
Dentro del ciclo, evalúa: si el nombre tiene más de 5 letras (recuerda que len() también sirve para medir un texto corto), el alumno será inyectado a gryffindor usando .append(). Si tiene 5 letras o menos, irá a slytherin.
Imprime ambas listas finales para ver quién quedó en qué casa.'''

alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []

for nombres in alumnos:
    if  len(nombres) > 5:
        gryffindor.append(nombres)
    else:
        slytherin.append(nombres)

print(f"Gryffindor: {gryffindor}")
print(f"Slytherin: {slytherin}")
