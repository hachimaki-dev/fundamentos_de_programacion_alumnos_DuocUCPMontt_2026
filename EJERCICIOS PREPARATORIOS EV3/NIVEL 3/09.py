#Ejercicio 9 — Evaluación de solicitudes de crédito
#Un banco recibe solicitudes de crédito. El analista ingresa el score crediticio de cada solicitante (entero de 0 a 1000).

#Clasifica el score con estos rangos exactos:

#Mayor a 750 (> 750) → "Aprobado automáticamente"
#De 500 a 750 (>= 500 y <= 750) → "Revisión manual"
#Menor a 500 (< 500) → "Rechazado"
#Condiciones de borde: Un score de exactamente 750 es "Revisión manual". Un score de exactamente #500 también es "Revisión manual".

#Registra 8 solicitudes y muestra al final cuántas quedaron en cada categoría.

#Desafío: valida que el score esté entre 0 y 1000. Si no, pide ingresar de nuevo.

aprobado = 0
revision_manual = 0
rechazado = 0

for i in range(8):

    while True:
        try:
            score_crediticio = int(input(f"Ingresa el score crediticio del solicitante {i + 1}: "))

            if score_crediticio < 0:
                print("Error: El score no puede ser un número negativo")
            elif 0 <= score_crediticio <=1000:
                break
            else:
                print("Error: El score no debe ser mayor que 1000")

        except ValueError:
            print("Error: Ingresa el score en formato numérico")

    if score_crediticio > 750:
        aprobado += 1
        print("Aprobado automáticamente")
    elif 500 <= score_crediticio <= 750:
        revision_manual += 1
        print("Revisión manual")
    else:
        rechazado += 1
        print("Rechazado automáticamente")

print("\n---------------------------------------------------")
print(f"Solicitantes aprobados = {aprobado}")
print(f"Solicitantes por revisar = {revision_manual}")
print(f"Solicitantes rechazados= {rechazado}")
print("---------------------------------------------------")