alumnos = ["Harry", "Hermonie", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []
for alumno in alumnos:
    if len(alumno) > 5:
        gryffindor.append(alumno)
    elif len(alumno) <= 5:
        slytherin.append(alumno)
print(f"La casa Gryffindor tiene : {gryffindor}.")
print(f"La casa Slytherin tiene : {slytherin}.")
for alumno_slytherin in slytherin:
    print(alumno_slytherin)
for alumno_gryffindor in gryffindor:
    print(alumno_gryffindor)