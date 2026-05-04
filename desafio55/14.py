nota_alumno = 3.6
porcentaje_de_asistencia = 85
if porcentaje_de_asistencia > 80 :
    nota_alumno = nota_alumno + 0.5


if nota_alumno >= 4.0:
    print("aprobado")
elif nota_alumno > 3.5 and nota_alumno < 4.0:
    print("examen")
elif nota_alumno < 3.5:
    print("reprobado")