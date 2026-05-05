nota = 3.0
asistencia = 85
if asistencia >= 80:
    nota = nota + 0.5
else:
    print("No tienes bono por asistencia")

if nota >= 4.0:
    print("aprovado")
elif nota >= 3.5:
    print("Examen")
else:
    print("reprovado")
