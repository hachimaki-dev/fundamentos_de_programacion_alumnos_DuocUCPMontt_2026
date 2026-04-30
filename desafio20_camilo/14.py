alumnos = [{"Nombre" : "Ana", "Nota" : 5.0},
           {"Nombre" : "Luis", "Nota" : 3.0}]

aprobados = 0

for alumno in alumnos :
    if alumno["Nota"] >= 4.0 :
        aprobados += 1

print(aprobados)