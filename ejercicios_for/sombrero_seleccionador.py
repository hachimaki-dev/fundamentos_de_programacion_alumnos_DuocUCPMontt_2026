alumnos= ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor=[]
slytherin= []

for alumno in alumnos:

    if len(alumno) >= 5 :
        gryffindor.append(alumno)
    else:
        slytherin.append(alumno)
print(f"Gryffindor tiene a {gryffindor} y slytherin tiene a {slytherin}")