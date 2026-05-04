nota = 3.6
porcentaje_asistencia = 85

if porcentaje_asistencia > 80 :
    nota += 0.5

if nota >= 4.0 :
    print("Aprobado")
elif nota >= 3.5 and nota <= 3.9 :
    print("Examen")
else :
    print("Reprobado")