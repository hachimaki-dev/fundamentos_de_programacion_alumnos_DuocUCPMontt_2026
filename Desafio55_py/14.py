nota = 3.6
asistencia = 85

if asistencia >= 80:
    nota += 0.5


if nota >= 4.0:
    print("APROBADO")
elif nota >= 3.5 <= 3.9:
    print("VAS A EXAMEN")
else:
    print("REPROBADO")

