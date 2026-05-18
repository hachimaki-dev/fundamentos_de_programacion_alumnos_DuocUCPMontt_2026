mensualidad = 85000
kit = 18000

edad_meses = -1

while edad_meses < 0:
    edad_meses = int(input("Edad (meses): "))

    if edad_meses < 0:
        print("Ingrese una edad válida")

nivel = 0

while nivel < 1 or nivel > 4:
    nivel = int(input("Nivel: "))

    if nivel < 1 or nivel > 4:
        print("Ingrese un nivel válido")

if edad_meses <= 18:
    if nivel == 1 or nivel == 2:
        dcto_mensualidad = .2
    else:
        dcto_mensualidad = .13
elif edad_meses >= 19 and edad_meses <= 36:
    if nivel == 1 or nivel == 2:
        dcto_mensualidad = .12
    else:
        dcto_mensualidad = .07
else:
    dcto_mensualidad = 0

if nivel == 1 or nivel == 2:
    dcto_kit = .1

    if edad_meses <= 12:
        dcto_kit_adicional = .05
    else:
        dcto_kit_adicional = 0
else:
    dcto_kit = 0
    dcto_kit_adicional = 0

mensualidad_final = int(mensualidad * (1 - dcto_mensualidad))
kit_final = int((kit * (1 - dcto_kit)) * (1 - dcto_kit_adicional))

print(f"Mensualidad: {mensualidad_final}")
print(f"Kit materiales: {kit_final}")