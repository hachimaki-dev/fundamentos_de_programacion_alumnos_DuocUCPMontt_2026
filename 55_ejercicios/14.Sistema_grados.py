nota_alumno = 3.6
asistencia_alumno = 85

if asistencia_alumno > 80:
    nota_alumno += 0.5
    if nota_alumno > 4.0:
        print("Aprobado")
    elif nota_alumno >= 3.5:
        print("Examen")
    else:
        print("Reprobado")