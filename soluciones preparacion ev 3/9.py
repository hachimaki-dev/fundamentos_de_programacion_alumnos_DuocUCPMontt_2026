contador_aprobado_automaticamente = 0
contador_revision_manual = 0
contador_rechazado = 0

for i in range(1, 9) :
    while True :
        try :
            score_crediticio = int(input(f"Ingrese el precio de la venta {i}: "))

            if not score_crediticio >= 0 or not score_crediticio <= 1000:
                print("Ingrese un valor entre 0 y 1000.")
                continue

            if score_crediticio < 500 :
                contador_rechazado += 1
            elif score_crediticio >= 500 and score_crediticio <= 750 :
                contador_revision_manual += 1
            elif score_crediticio > 750 :
                contador_aprobado_automaticamente += 1

            break
        except ValueError :
            print("Ingrese un valor numérico (entero).")
        
print(f"Aprobados automáticamente: {contador_aprobado_automaticamente}")
print(f"Revisiones manual: {contador_revision_manual}")
print(f"Rechazados: {contador_rechazado}")