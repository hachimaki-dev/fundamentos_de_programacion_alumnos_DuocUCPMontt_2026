nota_alumno = 3.6
porcentaje_asistencia_alumno = 85

if porcentaje_asistencia_alumno >= 80: # Bono por asistencia
    nota_final = nota_alumno + 0.5
else:
    nota_final = nota_alumno

if nota_final >= 4.0:
    print("Aprobado")
elif nota_final >= 3.5:
    print("Examen")
else:
    print("Reprobado")
