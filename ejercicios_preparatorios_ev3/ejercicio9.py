categoria_aprobados = 0
categoria_revision = 0
categoria_rechazados = 0

for i in range(1,9):
    while True:
    try:
        solicitud_credito = int("Ingrese su score: ")
        if solicitud_credito >= 0 and solicitud_credito <= 1000:
            break
        else:
            print("Error: el score debe estar entre 0 y 1000.")
    except ValueError:
        print("Error: ingresa un número entero.")
    
    if solicitud_credito > 750:
        print("Aprobado automáticamente")
        categoria_aprobados += 1
    elif solicitud_credito >= 500 and solicitud_credito <= 750:
        print("Revisión manual")
        categoria_revision += 1
    else:
        print("Rechazado")
        categoria_rechazados += 1

print("--- RESUMEN ---")
print(f"En categoria aprobado automaticamente: {categoria_aprobados}")
print(f"En categoria revision manual: {categoria_revision}")
print(f"En categoria rechazado: {categoria_rechazados}")