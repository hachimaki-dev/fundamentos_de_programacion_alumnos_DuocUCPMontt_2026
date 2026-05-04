nota = 3.6
asistencia = 85
if asistencia > 80:
    nota = nota + 0.5
    print(nota)
    if nota >= 4.0:
        print("aprobado")
elif nota == 3.5 or 3.9:
    print("vas a examen")
else:
    ("reprobado")