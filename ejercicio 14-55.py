#Tienes un 3.6 de nota y un 85% de asistencia.
#Si tienes 80% o más de asistencia, tu nota sube 0.5 puntos
#. Luego de aplicar el bono (o no), revisa tu estado: 
# si tu nota final es 4.0 o más, estás 'Aprobado'. Si estás entre 3.5 y 3.9, vas a 'Examen'.
#  Si tienes menos, estás 'Reprobado'.

nota = float(input("Ingresa tu nota: "))
asistencia = int(input("Ingresa tu asistencia: "))
if asistencia >= 80:
    nota = nota + 0.5

if nota > 4.0:
    print("APROBADO")
elif 3.5 <= nota <= 3.9: 
    print("VAS A EXAMEN")
else:
    print("REPROBADO")