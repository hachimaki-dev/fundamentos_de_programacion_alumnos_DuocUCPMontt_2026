#variable con nombres y otras dos con listas vacias D:
alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []

#aqui viene el FOR \(oAo)/
for s in alumnos:
    if len(s) >= 5:
        gryffindor.append(s)
    else:
        slytherin.append(s)
        
print(f"Slytherin: {slytherin}")
print(f"Gryffindor:{gryffindor}")
