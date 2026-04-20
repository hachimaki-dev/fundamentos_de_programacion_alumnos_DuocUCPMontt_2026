alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []

for alumno in alumnos:
    if len(alumno) >= 5:
        slytherin.append(alumno)
    else:
        gryffindor.append(alumno)

print(f"Gryffindor: {gryffindor}")
print(f"Slytherin: {slytherin} ")