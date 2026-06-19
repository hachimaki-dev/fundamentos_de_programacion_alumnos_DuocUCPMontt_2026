
nota_estudiante = 3.6

asistencia = 85


if asistencia > 80:
    nota_estudiante += 0.5

if nota_estudiante > 4.0:
    print("aprobado")
elif nota_estudiante >= 3.5:
    print("examen")
else:
    print("reprobado")


