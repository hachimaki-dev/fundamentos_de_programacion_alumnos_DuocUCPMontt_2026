"""Ejercicio 14: Sistema de Grados con Bonificación
Calcula si un alumno aprueba su ramo sumando un bono por asistencia.

Datos Iniciales: Tienes un 3.6 de nota y un 85% de asistencia.

Reglas de Negocio: Si tienes 80% o más de asistencia, tu nota sube 0.5 puntos. 

Luego de aplicar el bono (o no), revisa tu estado: si tu nota final es 4.0 o más, estás 'Aprobado'. 

Si estás entre 3.5 y 3.9, vas a 'Examen'. Si tienes menos, estás 'Reprobado'.

Restricciones: Usa un `if` para el bono y luego un bloque `if/elif/else` para definir el estado. Imprime solo el estado ('Aprobado', 'Examen' o 'Reprobado')."""

Nota = 3.6

Asistencia = 85 # % De 100

if Asistencia >= 80:
    Nota += 0.5
if Nota >= 4:
    print("Aprobado") 
elif Nota >= 3.5 and Nota <= 3.9:
    print("Examen")
else:
    print("Reprobado")   