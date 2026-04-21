print("=================== LISTA DE ASPIRANTES ===================\n")

alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]

gryffindor = []
slytherin = []

for nombre in alumnos:
    if len(nombre) > 5:
        gryffindor.append(nombre)

    else:
        slytherin.append(nombre)

print("Gryffindor:", gryffindor)
print("Slytherin:", slytherin)