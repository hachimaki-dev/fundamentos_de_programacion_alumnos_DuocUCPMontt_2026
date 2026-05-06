nota_alumno = 3.6
asistencia_alumno = 85

asistencia_minima_bono = 80
bono_asistencia = 0.5
nota_aprobacion = 4.0
nota_examen_minima = 3.5

if asistencia_alumno >= asistencia_minima_bono:
    nota_final = nota_alumno + bono_asistencia
else:
    nota_final = nota_alumno

if nota_final >= nota_aprobacion:
    print("Aprobado")
elif nota_final >= nota_examen_minima:
    print("Examen")
else:
    print("Reprobado")