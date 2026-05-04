
nota = 3.6
asistencia = (85/100)
if asistencia >= (80/100):
    nota += 0.5
nota_final = nota
if nota_final >= 4.0:
    print("--Aprobado--")
elif 3.5 < nota_final <3.9:
    print("--Examen Especial--")
else:
    print("--Reprobado--")

