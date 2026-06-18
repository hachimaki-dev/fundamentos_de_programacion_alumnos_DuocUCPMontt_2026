nota = 3.6
asistencia = 85

if asistencia >= 80:
    nota_final = nota + 0.5
    print("Aprobado")
elif nota >= 3.5 and nota <= 3.9:
    print("Examen")
else:
    print("Reprobado")