alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []
for alumno in alumnos:
    if len(alumno) > 5:
        gryffindor.append(alumno)
    elif len(alumno) <= 5:
        slytherin.append(alumno)
print(f"En Gryffindor se encuentra {gryffindor}")
print(f"En Slytherin se encuentra {slytherin}")