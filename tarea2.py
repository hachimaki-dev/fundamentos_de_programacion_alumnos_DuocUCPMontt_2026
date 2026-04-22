alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
slytherin = []
gryffindor = []

for alumno in alumnos:
    if len(alumno) > 5:
        #Se va Slytherin por que tiene 5 o mas letras
        slytherin.append(alumno)
    else:
        gryffindor.append(alumno)
print(slytherin)
print(gryffindor)

for alumno_slytherin in slytherin:
    print(alumno_slytherin)
for alumno_gryffindor in gryffindor:
    print(alumno_gryffindor)
