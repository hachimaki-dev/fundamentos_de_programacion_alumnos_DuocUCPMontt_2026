#Ejercicio 14: Sistema de Grados con Bonificación
#Calcula si un alumno aprueba su ramo sumando un bono por asistencia.
##
#Datos Iniciales: Tienes un 3.6 de nota y un 85% de asistencia.
##
#Reglas de Negocio: Si tienes 80% o más de asistencia, tu nota sube 0.5 puntos. 
# Luego de aplicar el bono (o no), revisa tu estado: si tu nota final es 4.0 o más,
#  estás 'Aprobado'. Si estás entre 3.5 y 3.9, vas a 'Examen'. Si tienes menos, estás 
# 'Reprobado'.
##
#Restricciones: Usa un `if` para el bono y luego un bloque `if/elif/else` para 
# definir el estado. Imprime solo el estado ('Aprobado', 'Examen' o 'Reprobado').
##
#Resultado# esperado en consola:
#Aprobado#n


nota_alumno = 3.6
porcentaje_asistencia = 85

if porcentaje_asistencia >= 80:
    nota_alumno += 0.5
    if nota_alumno >= 4.0:
        print("aprobado")

elif nota_alumno <= 3.5:
    if nota_alumno <= 3.9:
        print("vas a examen")
    
else:
    print("reprobado")