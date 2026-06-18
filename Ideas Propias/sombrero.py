# 🟡 Reto Medio: El Sombrero Seleccionador

alumnos = ["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna"]

gryffindor = []
slytherin = []

for alumno in alumnos :
    if len(alumno) > 5 :
        gryffindor.append(alumno)
    else:
        slytherin.append(alumno)
    
print(f"Gryffindor {gryffindor}")
print(f"Slytherin {slytherin}")