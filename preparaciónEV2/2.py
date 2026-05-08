membresia = 35000
casillero = 4500
descuento_membresia = 0

meses = int(input("Ingrese la cantidad de meses: "))

print("Seleccione el plan para el GYM")
print("1. Plan 1")
print("2. Plan 2")
print("3. Plan 3")
print("4. Plan 4")
plan = int(input("Elija un plan por favor: "))

if meses >= 12:
    if plan == 1 or plan == 2:
        descuento_membresia = 0.22
    elif plan == 3 or plan == 4:
        descuento_membresia = 0.15
elif meses >= 6 and meses < 12:
    if plan == 1 or plan == 2:
        descuento_membresia = 0.12
    elif plan == 3 or plan == 4:
        descuento_membresia = 0.07
else:
    print("Sin descuento en membresía")

total_membresia = membresia * (1 - descuento_membresia)

if plan == 1 or plan == 2:
    casillero = casillero * 0.85        # 15% descuento
    if meses >= 9:
        casillero = casillero * 0.95    # 5% adicional en cadena

print(f"Membresia: {total_membresia}")
print(f"Casillero: {casillero}")