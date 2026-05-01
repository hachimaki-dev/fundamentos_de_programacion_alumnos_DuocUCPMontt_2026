alumnos=[
    {"nombre":"Ana","nota":5.0},
    {"nombre":"luis","nota":3.0}
]
alumnos_aprobados=0
for alumno in alumnos:
    if alumno["nota"] >= 4.0:
        alumnos_aprobados+=1

print(alumnos_aprobados)
