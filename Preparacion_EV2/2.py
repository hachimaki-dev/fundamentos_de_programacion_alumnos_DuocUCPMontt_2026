#Desarrolle un programa que calcule el valor final de una membresía mensual de gimnasio y el valor final del arriendo de casillero.
#Valores base:
#    Membresía: $35.000
#    Casillero: $4.500
#Reglas de descuento para la membresía:
#    Meses >= 12:
#        Plan 1 o 2 → 22%
#        Plan 3 o 4 → 15%
#    6 <= meses < 12:
#        Plan 1 o 2 → 12%
#        Plan 3 o 4 → 7%
#    Menor a 6 meses → sin descuento.
#Reglas del casillero:
#    Plan 1 o 2 → 15% descuento.
#    Si además los meses son >= 9 → 5% adicional.
#Debe mostrar ambos valores finales.
membresia = 35000
casillero = 4500
meses = int(input("ingrese la cantidad de meses de su membresia:\n"))
plan = input("ingrese su plan 1, 2, 3, 4:\n")
if meses >= 12:
    if plan == "1" or plan == "2":
        membresia = membresia - membresia * 0.22
    else:
        membresia = membresia - membresia * 0.15
elif 6 <= meses < 12:
    if plan == "1" or plan == "2":
        membresia = membresia - membresia * 0.12
    else:
        membresia = membresia - membresia * 0.07
if plan == "1" or plan == "2":
    casillero = casillero - casillero * 0.15
    if meses >= 9:
        casillero = casillero - casillero * 0.05
print(membresia)
print(casillero)