# Objetivo: Evaluar la urgencia clínica de un paciente para determinar si necesita atención inmediata.ia
# Pide 3 datos:
# Edad (entero).
edad = int(input("Ingrese la edad del paciente: "))
# "Tiene dificultad para respirar" (respuesta "SI" o "NO"). 
dificultades_respirar = input("¿Tiene dificultades para respirar? (sí/no): ")
#  Nivel de dolor del 1 al 10.
nivel_dolor = int(input("En una escala del 1 al 10, ¿cuánto dolor siente? "))
# LÓGICA DEL TRIAGE
# Si tiene dificultad para respirar == "SI", es URGENCIAS NIVEL 1 pase inmediatamente. (Lo demás no importa).
if dificultades_respirar == "sí":
    print("URGENCIAS NIVEL 1: Pase inmediatamente.")
    #Elif si NO respira con dificultad, pero la edad > 60 Y el nivel de dolor > 7, es URGENCIAS NIVEL 2, pase pronto.
elif edad > 60 and nivel_dolor > 7:
    print("URGENCIAS NIVEL 2: Pase pronto.")
    #Elif si nivel de dolor es menor a 4, URGENCIAS NIVEL 5, puede irse a su casa o a consultorio.
elif nivel_dolor < 4:
    print("URGENCIAS NIVEL 5: Puede irse a su casa o a consultorio.")
    # else, para los demás casos: URGENCIAS NIVEL 3-4, tome asiento por favor.
else:
    print("URGENCIAS NIVEL 3-4: Tome asiento por favor.")