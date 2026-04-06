edad_usuario = int(input("¿Cual es la edad del paciente? "))
dificultad_r =  input("¿Tiene dificultad para respirar? SI/NO: ")
nivel_dolor = int(input("En una escala del 1 al 10, ¿Cuanto calificaria su dolor? "))
if dificultad_r == 'SI':
    print("URGENCIA NIVEL 1, ¡Pase inmediatamente!")
elif edad_usuario > 60 and nivel_dolor > 7:
    print("URGENCIA NIVEL 2, pase pronto")
elif nivel_dolor < 4:
    print("URGENCIA NIVEL 5, puede irse a su casa o al consultorio")
else:
    print("URGENCIA NIVEL 3-4, tome asiento y espere")