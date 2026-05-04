alumnos = [{"nombre": "Ana", "nota": 5.0}, {"nombre": "Luis", "nota": 3.0}]
aprobado = 0

for alumno in alumnos:
    if alumno["nota"] >= 4.0:
        aprobado += 1
print(aprobado)
