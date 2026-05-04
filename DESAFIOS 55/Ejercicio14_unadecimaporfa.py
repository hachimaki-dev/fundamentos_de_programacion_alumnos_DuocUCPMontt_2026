notainicial=3.6
asistencia=85 #porcentaje
notafinal=notainicial
if asistencia >= 80:
    notafinal += 0.5
if notafinal >= 4.0:
    print("Aprobado")
elif 3.9 >= notafinal >= 3.5:
    print ("Examen")
else:
    print("Reprobado")