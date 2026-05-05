nota = 3.6
asistencia = 85
nota_asistencia = 0.5

nota_total = nota + nota_asistencia
 
if asistencia  >= 80 and nota_total >= 4.0:
    print("Aprobado")
elif nota >= 3.5 and nota_total == 3.9:
    print("Examentes")
else:
    nota_total < 3.5
    print("Reprobado")
