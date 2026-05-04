nota=3.6
asistencia= 85
if asistencia > 80:
    nota+=0.5

if nota >= 4.0:
    print("Aprobado")
elif nota >= 3.6:
    print("Vas a examen")
else:
    print("reprobado")