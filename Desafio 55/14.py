nota_alumno=3.6
porcentaje_asistencia=85 #en %

if porcentaje_asistencia>=80:
    nota_alumno=nota_alumno+0.5
    if nota_alumno>= 4.0:
        print("Aprobado")
    elif nota_alumno >=3.5 and nota_alumno <= 3.9:
        print("Vas a Examen")
    else:
        print("Reprobado")
else:
    print(nota_alumno)