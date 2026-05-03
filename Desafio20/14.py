alumnos = [{"nombre": "Ana", "nota": 5.0}, {"nombre": "Luis", "nota": 3.0}]
aprobados = 0

for alumno in alumnos:
    if alumno["nota"] >= 4.0:
        aprobados +=1

print(aprobados)