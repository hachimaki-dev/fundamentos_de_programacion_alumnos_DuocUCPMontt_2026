
aprobados_automáticamente = 0
revisiones_manuales = 0
postulantes_rechazados = 0
for Numero_score in range(1,9):
    while True:
        try:
            score_crediticio_usuario = int(input(f"Ingrese su Score Crediticio para solicitar el crédito N°{Numero_score}: "))
            if score_crediticio_usuario <= 1000 and score_crediticio_usuario >= 0:
                break
            else:
                print("Ingrese un número válido. del 0 al 1000")
        except ValueError:
            print("Ingrese un número válido. del 0 al 1000")
    if score_crediticio_usuario > 750:
        aprobados_automáticamente += 1
    elif score_crediticio_usuario >= 500 and score_crediticio_usuario <= 750:
        revisiones_manuales += 1
    else:
        postulantes_rechazados += 1

print(f"Postulantes rechazados: {postulantes_rechazados} \n Postulantes en espera de revisión manual: {revisiones_manuales} \n Postulantes aceptados automáticamente: {aprobados_automáticamente}")
        