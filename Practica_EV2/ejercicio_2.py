membresia_mensual = 35000
casillero = 4500

meses = int(input("¿Cuanto meses de membresia desea pagar?: "))
plan = int(input("Seleccione su plan (1-2-3-4): "))

if meses >= 12:
    if plan == 1 or plan == 2:
        descuento_membresia = 0.22
    else:
        descuento_membresia = 0.15

elif 6 <= meses < 12:
    if plan == 1 or plan == 2:
        descuento_membresia = 0.12
    else:
        descuento_membresia = 0.07
    
elif meses < 6:
    descuento_membresia = 0

descuento_casillero = 0

if plan == 1 or plan == 2:
    descuento_casillero = 0.15
    if meses >= 9:
        descuento_casillero += 0.05
    
valor_final_membresia = membresia_mensual * (1 - descuento_membresia)
valor_final_casillero = casillero * (1 - descuento_casillero)

print(f"El valor final de su membresia es de: ${valor_final_membresia}")
print(f"El valor final del arriendo de su casillero es de: ${valor_final_casillero}")