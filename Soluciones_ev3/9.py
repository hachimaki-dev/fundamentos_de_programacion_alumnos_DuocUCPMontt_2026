aprobados = 0
revision = 0
rechazados = 0

for i in range (8):
    while True:
        try:
            score = int(input(f"Ingrese el score solicitante {i} de (0 a 1000): "))
            if score >= 0 and score <= 1000:
                break
            else:
                print("ERROR, el score debe de ser de 0 a 1000")
        except ValueError:
            print("ERROR, ingresa un numero entero porfavor")
        
    if score >750:
        print("Aprobado automáticamente")
        aprobados +=1
    elif score >= 500:
        print("Revisión manual")
        revision += 1
    else:
        print("Rechazado")
        rechazados +=1

print(f"Aprobados totales: {aprobados}")
print(f"En revision totales: {revision}")
print(f"Rechazados totales: {rechazados}")


