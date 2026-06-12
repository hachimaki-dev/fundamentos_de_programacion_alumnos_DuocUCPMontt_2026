membresia = 35000
casillero = 4500

meses = int(input("¿contrata el plan de 12 o 6 meses?:\n12 o 6 :"))
plan = int(input("cual plan seleccionara:(1,2,3,4):"))

descuento = 0

if meses >= 12:
    if plan == 1 or plan == 2:
        descuento = 0.22
    elif plan == 3 or plan == 4:
        descuento = 0.15
    else:
        descuento = 0
elif meses >= 6:
    if plan == 1 or plan == 2:
        descuento = 0.12
    elif plan == 3 or plan == 4:
        descuento = 0.07
else:
    descuento = 0

valor_descuento = membresia * descuento 
cuota_final= membresia - valor_descuento

descuento_casillero = 0
if plan == 1 or plan == 2:
    descuento_casillero = 0.15
    if meses >= 9:
        descuento_casillero += 0.05

total_descuento_casillero = casillero * descuento_casillero 
cuota_final_casillero = casillero - total_descuento_casillero
print("total de la cuota mensual", cuota_final)
print("total del casillero mensual", cuota_final_casillero)
