alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []
for nombre in alumnos:
    if len(nombre) > 5:
        gryffindor.append(nombre)
    else:
        slytherin.append(nombre)
print(f"en slytherin estan: {slytherin}")
print(f"en gryffindor estan: {gryffindor}")