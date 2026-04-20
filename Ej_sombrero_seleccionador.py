alumnos = ['Harry', 'Hermione', 'Ron', 'Draco', 'Neville', 'Luna']

gryffindor = []
slytherin = []

for nombre in alumnos:
    if len(nombre) > 5:
        gryffindor.append(nombre)
    else:
        slytherin.append(nombre) 

print (f"Alumnos en Gryffindor: {gryffindor}")
print (f"Alumnos en Slytherin: {slytherin}")   