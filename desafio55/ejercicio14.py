bono_asistencia = 0.5
nota_alumno = 3.6
asistencia = 0.85
if asistencia >= 0.80:
    nota_alumno = nota_alumno + bono_asistencia
if nota_alumno >= 4.0:
    print("Aprobado")
elif nota_alumno >= 3.5 and nota_alumno <= 3.9:
    print("Examen")
elif nota_alumno < 3.5:
    print("Reprobado")