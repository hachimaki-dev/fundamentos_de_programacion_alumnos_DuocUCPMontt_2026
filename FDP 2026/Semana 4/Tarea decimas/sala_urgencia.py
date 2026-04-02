edad = -1

while edad < 0:
    edad = int(input("Edad del paciente: "))

    if edad < 0:
        print("Por favor ingrese una edad válida\n")

dificultad_respirar = ""

while dificultad_respirar.lower() != "si" and dificultad_respirar.lower() != "no":
    dificultad_respirar = input("¿Tiene dificultad para respirar? (Si/No): ")

    if dificultad_respirar.lower() != "si" and dificultad_respirar.lower() != "no":
        print("Por favor ingrese una opción válida\n")

dolor = 0

while dolor < 1 or dolor > 10:
    dolor = int(input("Nivel de dolor del 1 al 10: "))

    if dolor < 1 or dolor > 10:
        print("Por favor ingrese un valor válido")

if dificultad_respirar.lower() == "si":
    print("URGENCIA NIVEL 1 - Pase inmediatamente")
elif edad > 60 and dolor > 7:
    print("URGENCIA NIVEL 2 - Pase pronto")
elif dolor < 4:
    print("URGENCIA NIVEL 5 - Vaya a su casa o a un consultorio")
else:
    print(" URGENCIA NIVEL 3 O 4 - Tome asiento")