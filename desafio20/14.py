ana = {"nombre": "ana", "nota": 5.0}
luis = {"nombre": "luis", "nota": 3.0}
alumnos = {ana["nota"], luis["nota"]}
aprobados = 0
for alumno in alumnos:
    if alumno >= 4:
        aprobados += 1
print(aprobados)