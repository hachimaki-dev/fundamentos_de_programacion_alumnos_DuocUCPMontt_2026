alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]

gryffindor = []
slytherin = []

for alumno in alumnos :
    if len(alumno) > 5 :
        gryffindor.append(alumno)
    else :
        slytherin.append(alumno)

print("Mostrando alumnos de Gryffindor:")
for alumno in gryffindor :
    print(alumno)

print("Mostrando alumnos de Slytherin:")
for alumno in slytherin :
    print(alumno)