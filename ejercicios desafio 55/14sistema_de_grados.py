promedio_nota = 3.6
asistencia = 85
bono_asistencia = 0.5
if asistencia >= 80:
    promedio_nota = promedio_nota + bono_asistencia
    if promedio_nota >= 4.0:
        print("aprobado")
if 3.5 <= promedio_nota <= 3.9:
    print("va a examen")
if promedio_nota < 3.5:
    print("reprobado")