# Ejercicio 9 — Evaluación de solicitudes de crédito
# Un banco recibe solicitudes de crédito. El analista ingresa el score crediticio de cada solicitante (entero de 0 a 1000).

# Clasifica el score con estos rangos exactos:

# Mayor a 750 (> 750) → "Aprobado automáticamente"
# De 500 a 750 (>= 500 y <= 750) → "Revisión manual"
# Menor a 500 (< 500) → "Rechazado"
# Condiciones de borde: Un score de exactamente 750 es "Revisión manual". Un score de exactamente 500 también es "Revisión manual".

# Registra 8 solicitudes y muestra al final cuántas quedaron en cada categoría.

# Desafío: valida que el score esté entre 0 y 1000. Si no, pide ingresar de nuevo.

aprobado_automaticamente = 0
revision_manual = 0
rechazado = 0

for solicitudes in range(1, 9):

    while True:

        try:

            score_crediticio_del_solicitante = int(
                input(f"Ingrese el score N°{solicitudes}: ")
            )

            if 0 <= score_crediticio_del_solicitante <= 1000:
                break

            print("Ingrese un score entre 0 y 1000")

        except ValueError:
            print("Ingrese un número entero")

    if score_crediticio_del_solicitante > 750:
        print("Aprobado automáticamente")
        aprobado_automaticamente += 1

    elif 500 <= score_crediticio_del_solicitante <= 750:
        print("Revisión manual")
        revision_manual += 1

    else:
        print("Rechazado")
        rechazado += 1

print(f"Aprobado automáticamente: {aprobado_automaticamente}")
print(f"Revisión manual: {revision_manual}")
print(f"Rechazado: {rechazado}")