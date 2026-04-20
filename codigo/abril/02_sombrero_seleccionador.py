alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []

for alumno in alumnos:
    if len(alumno) > 5:
        gryffindor.append(alumno)
    else:
        slytherin.append(alumno)

print(f"Alumnos de Gryffindor: {gryffindor}")
print(f"Alumnos de Slytherin: {slytherin}")
