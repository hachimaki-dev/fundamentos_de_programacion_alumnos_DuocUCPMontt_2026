#Variables base
membresia = 35000
locker = 4500

#inputs
print("------ Bienvenido ------")
meses = int(input("\n¿Cuantos meses deseas incribirte? "))
print("Revisa nuestros planes disponibles:\n")
print("Plan 1")
print("Plan 2")
print("Plan 3")
print("Plan 4")
plan = int(input("\nIngresa el número de tu plan: "))

#Descuento de membresía
if meses >= 12:
    if plan == 1 or plan == 2:
        membresia = membresia - (membresia * 0.22)
    elif plan == 3 or plan == 4:
        membresia = membresia - (membresia * 0.15)
elif 6 <= meses < 1:
    if plan == 1 or plan == 2:
        membresia = membresia - (membresia * 0.12)
    elif plan == 3 or plan == 4:
        membresia = membresia - (membresia * 0.07)

#Reglas de casilleros
if plan == 1 or plan == 2:
    locker = locker - (locker * 0.15)

if meses >= 9:
    locker = locker - (locker * 0.05)

print(f"Membresia: ${int(membresia)}")
print(f"Casillero: ${int(locker)}")