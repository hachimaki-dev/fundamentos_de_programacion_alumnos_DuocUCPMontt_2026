nota = 3.6
asistencia = 0.85
if asistencia >= 0.8:
    nota += 0.5
if nota >= 4:
    print("Aprobado")
elif nota >= 3.5 and nota <= 3.9:
    print("Examen")
else:
    print("Reprobado")