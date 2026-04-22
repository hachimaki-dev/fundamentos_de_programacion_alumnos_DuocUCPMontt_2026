alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []

for alumno in alumnos:
    if len(alumno) > 5:
        gryffindor.append(alumno)
    else:
        slytherin.append(alumno)
print("lista 1", gryffindor)
print("lista 2", slytherin)
