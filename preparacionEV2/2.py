#Desarrolle un programa que calcule el valor final de una membresía mensual de gimnasio y el valor final del arriendo de casillero.

#Valores base:

#Membresía: $35.000
#Casillero: $4.500
#Reglas de descuento para la membresía:

#Meses >= 12:
#Plan 1 o 2 → 22%
#Plan 3 o 4 → 15%
#6 <= meses < 12:
#Plan 1 o 2 → 12%
#Plan 3 o 4 → 7%
#Menor a 6 meses → sin descuento.
#Reglas del casillero:

#Plan 1 o 2 → 15% descuento.
#Si además los meses son >= 9 → 5% adicional.
#Debe mostrar ambos valores finales.
membresia = 35000
casillero = 4500
meses = 12
plan = 1 
if meses >= 12 :
    if plan == 1 or plan == 2:
        membresia *= 0.78
    elif plan == 3 or plan == 4:
        membresia *= 0.85
elif 6 <= meses < 12:
    if plan == 1 or plan == 2:
        membresia *= 0.88
    elif plan == 3 or plan == 4:
        membresia *= 0.93
elif meses < 6:
    print("sin descuento")
if plan == 1 or plan == 2:
    casillero *= 0.85
    if meses >= 9:
        casillero *= 0.95
print (f"membresia es {membresia} \n casillero es {casillero}")

