alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]
griffindor = []
slitherin = []

for i in alumnos:
    if len(i) > 5:
        griffindor.append(i)
    elif len(i) <= 5:
        slitherin.append(i)

print(f"slitherin: {slitherin}")
print(f"griffindor: {griffindor}")