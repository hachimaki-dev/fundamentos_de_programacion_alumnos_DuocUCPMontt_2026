alumnos = ["Harry", "Hermonie", "Ron", "Draco", "Neville", "Luna"]
gryffindor = []
slytherin = []
for letras in alumnos:
    if len(letras) > 5:
        alumnos.append(gryffindor)
    elif len(letras) <= 5:
        alumnos.append(slytherin)
print(f"La casa Gryffindor tiene : {gryffindor}.")
print(f"La casa Slytherin tiene : {slytherin}.")