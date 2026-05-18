mensualidad = 28000
instalacion = 15000

velocidad = 0

while velocidad < 1:
    velocidad = int(input("Velocidad (Mbps): "))

    if velocidad < 1:
        print("Ingrese una velocidad válida")

plan = 0

while plan < 1 or plan > 4:
    plan = int(input("Plan: "))

    if plan < 1 or plan > 4:
        print("Ingrese un plan válido")

if velocidad >= 600:
    if plan == 1 or plan == 2:
        dcto_mensualidad = .18
    else:
        dcto_mensualidad = .11
elif velocidad >= 300 and velocidad < 600:
    if plan == 1 or plan == 2:
        dcto_mensualidad = .1
    else:
        dcto_mensualidad = .06
else:
    dcto_mensualidad = 0

if plan == 1 or plan == 2:
    dcto_instalacion = .2

    if velocidad >= 500:
        dcto_instalacion_adicional = .1
    else:
        dcto_instalacion_adicional = 0
else:
    dcto_instalacion = 0
    dcto_instalacion_adicional = 0

mensualidad_final = int(mensualidad * (1 - dcto_mensualidad))
instalacion_final = int((instalacion * (1 - dcto_instalacion)) * (1 - dcto_instalacion_adicional))

print(f"Mensualidad: {mensualidad_final}")
print(f"Instalacion: {instalacion_final}")