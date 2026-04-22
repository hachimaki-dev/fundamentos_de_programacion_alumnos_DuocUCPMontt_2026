""" Reto Medio: El Sombrero Seleccionador
Es el primer año en Hogwarts y tienes una lista de aspirantes. El Sombrero elegirá su casa dependiendo del tamaño de su nombre.

Instrucciones:

Crea una lista alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"] y otras dos listas vacías: gryffindor = [] y slytherin = [].
Recorre la lista alumnos con un ciclo for.
Dentro del ciclo, evalúa: si el nombre tiene más de 5 letras (recuerda que len() también sirve para medir un texto corto), el alumno será inyectado a gryffindor usando .append(). Si tiene 5 letras o menos, irá a slytherin.
Imprime ambas listas finales para ver quién quedó en qué casa."""

alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []

for cada_alumno_individualmente in alumnos:
    if len(cada_alumno_individualmente) > 5:
        gryffindor.append(cada_alumno_individualmente)
    else:
        slytherin.append(cada_alumno_individualmente)

print("Lista gryffindor")
for impresion_cada_valor in gryffindor:
    print(impresion_cada_valor)

print("Lista slytherin")
for impresion_cada_valor in slytherin:
    print(impresion_cada_valor)