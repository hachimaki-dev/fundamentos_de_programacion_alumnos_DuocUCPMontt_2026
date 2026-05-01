alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []
for alumno in alumnos:
    if len(alumno) > 5:
        slytherin.append(alumno)
    else:
        gryffindor.append(alumno)
for alumno_in_gryffindor in gryffindor:
    print(f"{alumno_in_gryffindor} es de Gryffindor")
for alumno_in_slytherin in slytherin:
    print(f"{alumno_in_slytherin} es de Slytherin")