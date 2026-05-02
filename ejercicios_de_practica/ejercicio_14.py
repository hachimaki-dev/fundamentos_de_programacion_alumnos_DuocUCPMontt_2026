alumnos = [{"nombre": "Javier", "nota": 5.4}, {"nombre": "Francisco", "nota": 3.9}, {"nombre": "Juan", "nota": 4.2}]

aprobados = 0

for alumno in alumnos:
    if alumno["nota"] >= 4.0:
        aprobados += 1

print(f"Total de alumnos aprobados son: {aprobados}")