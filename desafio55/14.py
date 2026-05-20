nota = 3.6
asistencia = 85
if asistencia > 80:
    nota_final = nota + 0.5

if nota_final > 4.0:
    print("Aprobado")
elif nota_final >= 3.5 or nota_final <= 3.9:
    print("Examen")
else:
    print("Rechazado")