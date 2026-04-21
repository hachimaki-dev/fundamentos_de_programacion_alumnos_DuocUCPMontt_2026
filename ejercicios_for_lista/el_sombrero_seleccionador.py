alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]

gryffindor = [] 
slytherin = []

for casa in alumnos:
    if len(casa) > 5:
        gryffindor.append(casa)
    else:
        slytherin.append(casa)



print(f"Los alumnos que quedaron en Gryffindor son: {gryffindor}")
print(f"Los alumnos que quedaron en Slytherin son: {slytherin}\n")
print(f"Los alumnos que quedaron en Gryffindor son : {len(gryffindor)} ")
print(f"Los alumnos que quedaron en Slytherin son : {len(slytherin)}")
