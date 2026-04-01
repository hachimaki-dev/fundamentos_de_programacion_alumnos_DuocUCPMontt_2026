#. Pide 3 datos:
#- Edad (entero).
#- "Tiene dificultad para respirar" (respuesta "SI" o "NO").
#- Nivel de dolor del 1 al 10.
#2. LÓGICA DEL TRIAGE:
#- Si tiene dificultad para respirar == "SI", es URGENCIAS NIVEL 1 pase inmediatamente. (Lo demás no importa).
#- Elif si NO respira con dificultad, pero la edad > 60 Y el nivel de dolor > 7, es URGENCIAS NIVEL 2, pase pronto.
#- Elif si nivel de dolor es menor a 4, URGENCIAS NIVEL 5, puede irse a su casa o a consultorio.
#- Else, para los demás casos: URGENCIAS NIVEL 3-4, tome asiento por favor.
#3. Ojo con usar los comparadores adecuados (==) y anidar (if dentro de elif).

edad = int(input("ingrese la edad del paciente: "))
nivel_de_dolor = int(input("ingrese el nivel de dolor del paciente 1-10: "))

dificultad_respiracion = False
respuesta_respiracion = input("tiene el paciente dificultad para respirar? y/n: ")
if respuesta_respiracion == "y":
    dificultad_respiracion = True
elif respuesta_respiracion == "n":
    dificultad_respiracion = False

if dificultad_respiracion == True:
    print("URGENCIA NIVEL 1 PASE INMEDIATAMENTE")
elif dificultad_respiracion == False and edad >= 60 and nivel_de_dolor > 7:
    print("URGENCIA DE NIVEL 2 PASE PRONTO")
elif nivel_de_dolor < 4:
    print("URGENCIA NIVEL 5 PUEDE VOLVER A SU CASA O CONSULTARLO")
else:
    print("URGENCIA NIVEL 3-4 ESPERE SU TURNO")