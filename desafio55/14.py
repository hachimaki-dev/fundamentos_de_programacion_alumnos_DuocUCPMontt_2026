nota = 3.6
asistencia = 0.85 * 100

if asistencia > 0.80 * 100:
    nota += 0.5
    if nota >= 4.0:
        print("Aprobado")
    elif nota >= 3.5 and nota <= 3.9:
        print("Vas A examen")
    else:
        print("Reprobado")