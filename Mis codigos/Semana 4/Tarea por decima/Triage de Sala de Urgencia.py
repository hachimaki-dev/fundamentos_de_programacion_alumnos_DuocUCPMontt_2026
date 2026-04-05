# Triage de Sala de Urgencia
# Objetivo: Evaluar la urgencia clínica de un paciente para determinar si necesita atención inmediata.

# 1. Pide 3 datos:
# - Edad (entero).
# - "Tiene dificultad para respirar" (respuesta "SI" o "NO").
# - Nivel de dolor del 1 al 10.
# 2. LÓGICA DEL TRIAGE:
# - Si tiene dificultad para respirar == "SI", es URGENCIAS NIVEL 1 pase inmediatamente. (Lo demás no importa).
# - Elif si NO respira con dificultad, pero la edad > 60 Y el nivel de dolor > 7, es URGENCIAS NIVEL 2, pase pronto.
# - Elif si nivel de dolor es menor a 4, URGENCIAS NIVEL 5, puede irse a su casa o a consultorio.
# - Else, para los demás casos: URGENCIAS NIVEL 3-4, tome asiento por favor.
# 3. Ojo con usar los comparadores adecuados (==) y anidar (if dentro de elif).


print("****Bienvenido a la Sal de Urgencia****")
print("Necesito algunos datos")
edad = int(input("¿Cuántos años tienes?: "))
dificultad_para_respirar = input("Tiene difucultad para respirar (respuesta SI o NO): ")
dolor = int(input("Nivel de dolor del 1 al 10: "))

if dificultad_para_respirar == "SI":
    print("URGENCIAS NIVEL 1 pase inmediatamente")
elif dificultad_para_respirar == "NO" and edad >60 and dolor > 7:
    print("URGENCIA NIVEL 2, pase pronto")
elif dolor < 4:
    print("Puede irse a su casa o consultorio")
else:
    print("Por favor espere su turno")

print("Fin del programa")