#🟡 Rango: Cuidado
#Ejercicio 14: Sistema de Grados con Bonificación
#Calcula si un alumno aprueba su ramo sumando un bono por asistencia.

#Datos Iniciales: Tienes un 3.6 de nota y un 85% de asistencia.

#Reglas de Negocio: Si tienes 80% o más de asistencia, tu nota sube 0.5 puntos. Luego de aplicar el bono (o no), revisa tu estado: si tu nota final es 4.0 o más, estás 'Aprobado'. Si estás entre 3.5 y 3.9, vas a 'Examen'. Si tienes menos, estás 'Reprobado'.

#Restricciones: Usa un `if` para el bono y luego un bloque `if/elif/else` para definir el estado. Imprime solo el estado ('Aprobado', 'Examen' o 'Reprobado').

nota_estudiante = 3.6
asistencia_estudiante = 85
asistencia_bono = 80
nota_aprobado = 4.0
print("Comprobaremos si optas al bono de 0.5 decimas por asistencia")
if asistencia_estudiante >= asistencia_bono :
    nota_estudiante = nota_estudiante + 0.5
    print(f"Si has sido validado para este bono, por lo que tu nota nueva es {nota_estudiante}")
else : 
    print("Lo sentimos tu asistencia es muy baja como para optar a este bono.")
if nota_estudiante >= nota_aprobado :
    print(f"Tu nota es lo suficientemente alta para aprobar, felicidades")
elif nota estudiante >= 3.5 o
