print("Hola juan, tienes de nota un 3.6 y un 85% de asistencia.")
nota_alumno = 3.6
asistencia = 85

if asistencia >= 80:
    print("Se otorgara un bono de asistencia, +0.5 puntos a su nota")
    nota_alumno += 0.5
    if nota_alumno >= 4:
        print("Alumno aprobado")
    elif nota_alumno >= 3.5: 
        print("Vas a examen para mejorar tu nota")
    else:
        print("Alumno reprobado")
else:
    print("No se otorgara ningún bono por asistencia.")