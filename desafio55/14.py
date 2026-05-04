nota = 3.5
asistencia = 85
if asistencia > 80:
    nota = nota + 0.5
    print("Aprobado")
elif asistencia < 80 and nota == 3.5 or 3.9:
    print("Examen.")
else: 
    print("Reprobado")
    