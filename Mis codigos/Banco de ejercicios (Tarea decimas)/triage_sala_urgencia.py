# Triage de Sala de Urgencia
# Objetivo: Evaluar la urgencia clínica de un paciente para determinar si necesita atención inmediata.

# 1. Pide 3 datos:
#     - Edad (entero).
#     - "Tiene dificultad para respirar" (respuesta "SI" o "NO").
#     - Nivel de dolor del 1 al 10.
# 2. LÓGICA DEL TRIAGE:
#     - Si tiene dificultad para respirar == "SI", es URGENCIAS NIVEL 1 pase inmediatamente. (Lo demás no importa).
#     - Elif si NO respira con dificultad, pero la edad > 60 Y el nivel de dolor > 7, es URGENCIAS NIVEL 2, pase pronto.
#     - Elif si nivel de dolor es menor a 4, URGENCIAS NIVEL 5, puede irse a su casa o a consultorio.
#     - Else, para los demás casos: URGENCIAS NIVEL 3-4, tome asiento por favor.
# 3. Ojo con usar los comparadores adecuados (==) y anidar (if dentro de elif).

print(" SALA DE URGENCIAS ".center(50,"-"))

while True:
    edad_paciente = int(input("¿Que edad tiene? "))
    if 0 <= edad_paciente <= 200:
        break
    print("*** Error: ingrese un valor entre 0 y 200 ***")

while True:
    dificultad_respirar = input("¿Tiene dificultad para respirar? Ingrese 'SI' o 'NO': ").upper()
    if dificultad_respirar == "SI" or dificultad_respirar == "NO":
        break
    print("*** Error: solo se acepta SI o NO como respuesta ***")

while True:
    nivel_dolor = int(input("Del 1 al 10 ¿Que nivel de dolor tiene? "))
    if 1 <= nivel_dolor <= 10:
        break
    print("*** Error: ingrese un numero entre 1 y 10 ***")

if dificultad_respirar == "SI":
    print("URGENCIAS NIVEL 1 pase inmediatamente")
elif dificultad_respirar == "NO" and (edad_paciente > 60 and nivel_dolor > 7):
    print("URGENCIAS NIVEL 2, pase pronto")
elif nivel_dolor < 4:
    print("URGENCIAS NIVEL 5, puede irse a su casa o a consultorio")
else:
    print("URGENCIAS NIVEL 3-4, tome asiento por favor")
