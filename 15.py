#Calcula si un alumno aprueba su ramo sumando un bono por asistencia

nota_inicial = float(input("ingresa tu nota actual :"))
asistencia = int(input("ingresa tu porcentaje de asistencia :"))

if asistencia >= 80:
    nota_final = nota_inicial + 0.5
else:
    nota_final = nota_inicial

if nota_final >= 4.0:
    print(f"felicidades usted aprobo el ramo")

elif nota_final >= 3.5: # Si llegó aquí, es porque es menor a 4.0
    print(" para aprobar el ramo tienes que irte a examen")
else: 
    print("lo siento usted reprobo el ramo")