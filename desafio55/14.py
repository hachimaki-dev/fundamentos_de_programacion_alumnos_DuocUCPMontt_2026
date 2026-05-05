# Ejercicio 14: Sistema de Grados con Bonificación


nota = 3.6
asistencia = 85

if asistencia >= 80:
    nota += 0.5
 
    if nota >= 4.0 :
        print("Estas aprobado")
    elif nota >= 3.5 and nota <= 3.9:
        print("vas a examen")
    else:
        print("reprobaste")


