#Calcula si un alumno aprueba su ramo sumando un bono por asistencia.

#Datos Iniciales: Tienes un 3.6 de nota y un 85% de asistencia.

#Reglas de Negocio: Si tienes 80% o más de asistencia, tu nota sube 0.5 puntos. Luego de aplicar el bono (o no), revisa tu estado: si tu nota final es 4.0 o más, estás 'Aprobado'. Si estás entre 3.5 y 3.9, vas a 'Examen'. Si tienes menos, estás 'Reprobado'.

#Restricciones: Usa un `if` para el bono y luego un bloque `if/elif/else` para definir el estado. Imprime solo el estado ('Aprobado', 'Examen' o 'Reprobado').

nota = 3.6
asistencia = 85

if asistencia >= 80:
    nota = nota + 0.5

if nota >= 4.0:
    print("Aprobado")
elif 3.5 <= nota >= 3.9:
    print("Examen")  
else:
    print("Reprobado")