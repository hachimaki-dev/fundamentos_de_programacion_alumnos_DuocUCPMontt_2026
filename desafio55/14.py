notas_personales = 3.6
asistencia = 85
if asistencia >= 80:
    notas_personales = notas_personales + 0.5
else:
    notas_personales = notas_personales

if notas_personales >= 4.0:
    print("Aprobado")
elif notas_personales >= 3.5 and notas_personales <= 3.9:
    print("Examen")
else:
    print("Reprobao")