alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []
tamaño_nombre = 0
for alumno in alumnos:
    tamaño_nombre = len(alumno)
    if tamaño_nombre > 5:
        gryffindor.append(alumno)
    elif tamaño_nombre <= 5:
        slytherin.append(alumno)

print(gryffindor)
print(slytherin)
        