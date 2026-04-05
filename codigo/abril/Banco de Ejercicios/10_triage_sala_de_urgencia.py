# Simulador de triage de sala de urgencias

# El programa se asegura de que el usuario ingrese datos válidos, simulando una situación de urgencia real.

print("Ingrese sus datos.")

while True: # Comprobación de dificultad respiratoria
    dificultad_respiratoria = input("¿Tiene dificultad para respirar? (SI/NO): ")

    if dificultad_respiratoria.isalpha() == True:
        dificultad_respiratoria = dificultad_respiratoria.lower()
        if dificultad_respiratoria == "si" or dificultad_respiratoria == "s":
            dificultad_respiratoria = True
            break
        elif dificultad_respiratoria == "no" or dificultad_respiratoria == "n":
            dificultad_respiratoria = False
            break
        else:
            print('Respuesta inválida. Recuerde que debe ingresar "SI" o "NO".')
    else:
        print('Respuesta inválida. Recuerde que debe ingresar "SI" o "NO".')

# Si el paciente posee dificultades respiratorias, la urgencia es inmediata, por lo que se saltan el resto de preguntas.
if dificultad_respiratoria == True: 
    print("URGENCIA NIVEL 1: PASE INMEDIATAMENTE")
    raise SystemExit # Similar a la función sys.exit() sin necesidad de importar el módulo sys

while True: # Comprobación de edad válida
    edad = input("¿Cuál es su edad?: ")
    if edad.isdigit() == True:
        edad = int(edad)
        if edad >= 0:
            break
        else:
            print("Por favor ingrese una edad válida.")
    else:
        print("Por favor ingrese una edad válida.")

while True: # Comprobación de nivel de dolor válido
    nivel_dolor = input("¿Cómo calificaría su nivel de dolor del 1 al 10? ")
    if nivel_dolor.isdigit() == True:
        nivel_dolor = int(nivel_dolor)
        if nivel_dolor >= 1 and nivel_dolor <= 10:
            break
        else:
            print("Por favor ingrese un número del 1 al 10.")
    else:
        print("Por favor ingrese solo un número.")

if edad > 60 and nivel_dolor > 7:
    print("URGENCIA NIVEL 2: LE LLAMAREMOS PARA PASAR EN BREVE")
elif nivel_dolor < 4:
    print("URGENCIA NIVEL 5: PUEDE IRSE A SU CASA O A CONSULTORIO")
else: # Para todo el resto de casos
    print("URGENCIA NIVEL 3-4: POR FAVOR TOME ASIENTO. LE LLAMAREMOS CUANDO SEA SU TURNO.")
