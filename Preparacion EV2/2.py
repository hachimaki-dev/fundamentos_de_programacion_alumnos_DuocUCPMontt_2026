membresia = 35000
casillero = 4500

meses = 0

while meses < 1:
    meses = int(input("Cantidad de meses: "))

    if meses < 1:
        print("Ingrese una cantidad válida")

plan = 0

while plan < 1 or plan > 4:
    plan = int(input("Plan: "))

    if plan < 1 or plan > 4:
        print("Ingrese un plan válido")

if meses >= 12:
    if plan == 1 or plan == 2:
        dcto_membresia = .22
    else:
        dcto_membresia = .15
elif meses >= 6 and meses < 12:
    if plan == 1 or plan == 2:
        dcto_membresia = .12
    else:
        dcto_membresia = .07
else:
    dcto_membresia = 0

if plan == 1 or plan == 2:
    dcto_casillero = .15

    if meses >= 9:
        dcto_casillero_adicional = .05
    else:
        dcto_casillero_adicional = 0
else:
    dcto_casillero = 0
    dcto_casillero_adicional = 0

membresia_final = int(membresia * (1 - dcto_membresia))
casillero_final = int((casillero * (1 - dcto_casillero)) * (1 - dcto_casillero_adicional))

print(f"Membresia: {membresia_final}")
print(f"Casillero: {casillero_final}")