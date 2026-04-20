#Instrucciones:

#Crea una lista alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"] y otras dos listas vacías: gryffindor = [] y slytherin = [].
#Recorre la lista alumnos con un ciclo for.
#Dentro del ciclo, evalúa: si el nombre tiene más de 5 letras (recuerda que len() también sirve para medir un texto corto), el alumno será inyectado a gryffindor usando .append(). Si tiene 5 letras o menos, irá a slytherin.
#Imprime ambas listas finales para ver quién quedó en qué casa.

alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []
for alumno in alumnos:
    if len(alumno) > 5:
        gryffindor.append(alumno)
    elif len(alumno) <= 5:
        slytherin.append(alumno)
        
print(f"Los siguientes alumnos son de gryffindor: {gryffindor}")
print(f"Los siguientes alumnos son de slytherin:{slytherin}")