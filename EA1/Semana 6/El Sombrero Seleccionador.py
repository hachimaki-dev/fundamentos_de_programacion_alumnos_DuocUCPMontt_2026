# 🟡 Reto Medio: El Sombrero Seleccionador
# Es el primer año en Hogwarts y tienes una lista de aspirantes. El Sombrero elegirá su casa dependiendo del tamaño de su nombre.

# Instrucciones:

# Crea una lista alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"] y otras dos listas vacías: gryffindor = [] y slytherin = [].
# Recorre la lista alumnos con un ciclo for.
# Dentro del ciclo, evalúa: si el nombre tiene más de 5 letras (recuerda que len() también sirve para medir un texto corto), el alumno será inyectado a gryffindor usando .append(). Si tiene 5 letras o menos, irá a slytherin.
# Imprime ambas listas finales para ver quién quedó en qué casa.

alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []

for alumno in alumnos:
    print(f"Cantidad de caracteres por nombre de alumno: {len(alumno)}")
    if len(alumno) > 5:
        gryffindor.append(alumno)
    else:
        slytherin.append(alumno)

print(f"Nombre con más de 5 caracteres: {", ".join(gryffindor)}")
print(f"Nombre con igual o menos que 5 caracteres: {", ".join(slytherin)}")
